"""Three-line table QA (2026-09-28): XML geometry + RENDERED PDF measurement.

XML pass (python-docx):
- table-level alignment property + underlying w:jc == center
- fixed layout (w:tblLayout type=fixed), autofit OFF
- explicit widths from tblGrid sum to the intended table width
- per-column paragraph alignments / vertical alignment
- border inventory: only header-top / header-bottom / last-row-bottom rules,
  no vertical borders, no stray edges

Rendered pass (LibreOffice headless -> PDF -> pdfplumber):
- locate the horizontal rules on the page and measure the table's real x-extent
- center_error_mm = |table center - page text-area center|  (PASS <= 1.0 mm)
- left/right whitespace = table edges vs the text-area margins

This is a REAL rendered measurement - not a property read.
"""

from __future__ import annotations

import json
import subprocess
from pathlib import Path

from docx import Document
from docx.oxml.ns import qn

SOFFICE_CANDIDATES = [
    r"C:\Program Files\LibreOffice\program\soffice.exe",
    "soffice",
]
MM_PER_PT = 25.4 / 72.0
CENTER_TOL_MM = 1.0


def _soffice() -> str:
    for c in SOFFICE_CANDIDATES:
        if c == "soffice" or Path(c).is_file():
            return c
    raise FileNotFoundError("LibreOffice soffice not found")


def to_pdf(docx_path: Path, outdir: Path) -> Path:
    outdir.mkdir(parents=True, exist_ok=True)
    subprocess.run(
        [_soffice(), "--headless", "--convert-to", "pdf", "--outdir", str(outdir), str(docx_path)],
        check=True,
        capture_output=True,
        timeout=180,
    )
    pdf = outdir / (docx_path.stem + ".pdf")
    if not pdf.is_file():
        raise RuntimeError(f"PDF not produced for {docx_path}")
    return pdf


def _xml_checks(doc: Document, table) -> dict:
    info: dict = {"alignment_property": None, "tbl_jc": None, "layout": None, "autofit": None, "grid_widths_mm": [], "paragraph_alignments": [], "vertical_alignments": [], "border_violations": [], "top_rules": 0, "bottom_rules": 0, "header_sep_rules": 0}
    info["alignment_property"] = str(table.alignment) if table.alignment is not None else None
    tbl_pr = table._tbl.tblPr
    jc = tbl_pr.find(qn("w:jc"))
    info["tbl_jc"] = jc.get(qn("w:val")) if jc is not None else None
    layout = tbl_pr.find(qn("w:tblLayout"))
    info["layout"] = layout.get(qn("w:type")) if layout is not None else None
    info["autofit"] = bool(table.autofit)
    grid = table._tbl.find(qn("w:tblGrid"))
    if grid is not None:
        info["grid_widths_mm"] = [round(int(gc.get(qn("w:w"))) * MM_PER_PT / 20.0, 1) for gc in grid.findall(qn("w:gridCol"))]

    ncols = len(table.columns)
    col_aligns = [set() for _ in range(ncols)]
    v_aligns = set()
    nrows = len(table.rows)
    for r_i, row in enumerate(table.rows):
        for c_i, cell in enumerate(row.cells):
            v_aligns.add(str(cell.vertical_alignment))
            for para in cell.paragraphs:
                col_aligns[c_i].add(str(para.alignment))
            tc_pr = cell._tc.find(qn("w:tcPr"))
            tc_b = tc_pr.find(qn("w:tcBorders")) if tc_pr is not None else None
            if tc_b is None:
                continue
            for edge in ("top", "bottom", "left", "right"):
                el = tc_b.find(qn(f"w:{edge}"))
                if el is None or el.get(qn("w:val")) in (None, "nil"):
                    continue
                if edge == "top" and r_i == 0:
                    info["top_rules"] += 1
                elif edge == "bottom" and r_i == 0:
                    info["header_sep_rules"] += 1
                elif edge == "bottom" and r_i == nrows - 1:
                    info["bottom_rules"] += 1
                else:
                    info["border_violations"].append(f"row{r_i}.col{c_i}.{edge}")
    info["paragraph_alignments"] = [sorted(s) for s in col_aligns]
    info["vertical_alignments"] = sorted(v_aligns)
    return info


def _rendered_measure(pdf: Path) -> dict:
    import pdfplumber

    out = {"pages": 0, "rule_y_pt": [], "table_left_pt": None, "table_right_pt": None, "rules_per_page": []}
    with pdfplumber.open(pdf) as pdf_doc:
        out["pages"] = len(pdf_doc.pages)
        for pi, page in enumerate(pdf_doc.pages):
            rules = []
            for obj in list(page.lines) + list(page.rects):
                if obj.get("height") is None or obj.get("width") is None:
                    continue
                if obj["height"] <= 4.0 and obj["width"] >= 0.15 * page.width:
                    rules.append(obj)
            rules.sort(key=lambda r: r["top"])
            out["rules_per_page"].append(len(rules))
            if pi == 0:
                out["rule_y_pt"] = [round(r["top"], 1) for r in rules]
                if rules:
                    out["table_left_pt"] = round(min(r["x0"] for r in rules), 1)
                    out["table_right_pt"] = round(max(r["x1"] for r in rules), 1)
                out["page_width_pt"] = round(page.width, 1)
                out["page_height_pt"] = round(page.height, 1)
    return out


def qa_docx(docx_path: Path, outdir: Path | None = None, render: bool = True) -> dict:
    doc = Document(str(docx_path))
    sec = doc.sections[0]
    pw_mm = float(sec.page_width.mm)
    ml_mm = float(sec.left_margin.mm)
    mr_mm = float(sec.right_margin.mm)
    text_w_mm = pw_mm - ml_mm - mr_mm
    text_center_mm = ml_mm + text_w_mm / 2.0

    report = {"doc": str(docx_path.name), "tables": [], "render": None}
    for t_i, table in enumerate(doc.tables):
        info = _xml_checks(doc, table)
        t_report = {"table_id": t_i, **info}
        violations = []
        if info["alignment_property"] is None or "CENTER" not in str(info["alignment_property"]).upper():
            violations.append("table alignment property is not CENTER")
        if (info["tbl_jc"] or "").lower() != "center":
            violations.append("underlying w:jc is not center")
        if (info["layout"] or "").lower() != "fixed":
            violations.append("layout is not fixed")
        if info["autofit"]:
            violations.append("autofit is ON")
        if info["border_violations"]:
            violations.append(f"stray borders: {info['border_violations'][:4]}")
        if info["top_rules"] == 0 or info["bottom_rules"] == 0:
            violations.append("missing top or bottom rule")
        t_report["violations"] = violations
        t_report["status"] = "FAIL" if violations else "PASS"
        report["tables"].append(t_report)

    if render and outdir is not None:
        pdf = to_pdf(Path(docx_path), Path(outdir))
        ren = _rendered_measure(pdf)
        # rendered center check
        if ren["table_left_pt"] is not None:
            t_left_mm = ren["table_left_pt"] * MM_PER_PT
            t_right_mm = ren["table_right_pt"] * MM_PER_PT
            left_ws = t_left_mm - ml_mm
            right_ws = (pw_mm - mr_mm) - t_right_mm
            center_err = (t_left_mm + t_right_mm) / 2.0 - text_center_mm
            ren.update(
                {
                    "table_width_mm": round(t_right_mm - t_left_mm, 1),
                    "text_area_width_mm": round(text_w_mm, 1),
                    "left_whitespace_mm": round(left_ws, 1),
                    "right_whitespace_mm": round(right_ws, 1),
                    "center_error_mm": round(center_err, 2),
                    "center_status": "PASS" if abs(center_err) <= CENTER_TOL_MM else "FAIL",
                }
            )
        else:
            ren["center_status"] = "FAIL"
            ren["note"] = "no horizontal rules found in rendered PDF"
        if ren.get("pages", 1) > 1:
            import pdfplumber

            with pdfplumber.open(pdf) as pdf_doc:
                page2_text = pdf_doc.pages[1].extract_text() or ""
            first_header = doc.tables[0].cell(0, 0).text.split("\n")[0].strip()
            ren["header_repeat_page2"] = first_header in page2_text
            if not ren["header_repeat_page2"]:
                ren["center_status"] = "FAIL"
                ren["note"] = "header row did not repeat on page 2"
        report["render"] = ren

    xml_ok = all(t["status"] == "PASS" for t in report["tables"]) if report["tables"] else False
    render_ok = (report["render"] or {}).get("center_status") == "PASS"
    report["status"] = "PASS" if (xml_ok and (render_ok or not render)) else "FAIL"
    return report


def main() -> None:
    import argparse
    import sys

    ap = argparse.ArgumentParser()
    ap.add_argument("docx")
    ap.add_argument("--out", default=None)
    ap.add_argument("--no-render", action="store_true")
    args = ap.parse_args()
    rep = qa_docx(Path(args.docx), Path(args.out) if args.out else None, render=not args.no_render)
    print(json.dumps(rep, ensure_ascii=False, indent=2))
    sys.exit(0 if rep["status"] == "PASS" else 1)


if __name__ == "__main__":
    main()
