"""Unified figure QA gate for matplotlib figures.

Usage (CLI; the builder module must expose build() -> Figure):
    python figure_qa.py --builder <module.py> --out <outdir> [--name fig1] [--min-pt 8]

Usage (import):
    from figure_qa import run_gate
    report = run_gate(fig, outdir, name="fig1")

Fail-closed policy (2026-09-28 corrective pass):
- pdf parser / font-entry errors are FAIL (never silently ignored);
- SCI default minimum font size is 8 pt (single source: DEFAULT_MIN_PT below);
  lowering it requires an explicit override (--min-pt) and a recorded venue basis.

Checks: text-text overlap | text out-of-bounds | min fontsize | legend-data
overlap | margin | layout balance | grayscale preview | print-89mm preview |
PDF page size + font embedding.

Known blind spots (visual inspection still mandatory): arrow-over-text,
data occlusion in dense plots, 3D text extents (mplot3d projection).
"""

from __future__ import annotations

import argparse
import importlib.util
import json
import sys
import warnings
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import numpy as np
from matplotlib.text import Text

# ---- thresholds (single source of truth) -----------------------------------
DEFAULT_MIN_PT = 8.0  # SCI 默认；venue override 需显式传入并记录依据
OVERLAP_PX2 = 6.0
OVERLAP_FRAC = 0.04
MARGIN_FAIL_MM = 0.5
MARGIN_WARN_MM = 1.5
LEGEND_MIN_POINTS_COLL = 5
LEGEND_MIN_FRAC = 0.02
LEGEND_MIN_POINTS_LINE = 8
LEGEND_ALPHA_MIN = 0.5
BALANCE_RATIO_FAIL = 4.0
PRINT_PREVIEW_MM = 89.0

_BASE14 = ("Helvetica", "Times-Roman", "Times-Bold", "Times-Italic", "Courier", "Symbol", "ZapfDingbats")


def _renderer(fig):
    fig.canvas.draw()
    return fig.canvas.get_renderer()


def text_bbox(t, renderer):
    """TEXT-ONLY window extent.

    Annotation.get_window_extent() unions the text bbox WITH its leader arrow,
    which inflates collision checks (found 2026-09-28 via height 16 vs 31 px on
    same-size labels). Call the Text base implementation instead.
    """
    from matplotlib.text import Annotation, Text

    if isinstance(t, Annotation):
        return Text.get_window_extent(t, renderer=renderer)
    return t.get_window_extent(renderer=renderer)


# ---------------------------------------------------------------- text guards
def _tick_index(fig):
    """Map id(tick-label Text) -> (ax, axis, tick). Tick labels have no .axes."""
    index = {}
    for ax in fig.get_axes():
        for axis in (getattr(ax, "xaxis", None), getattr(ax, "yaxis", None)):
            if axis is None:
                continue
            for tick in list(axis.get_major_ticks()) + list(axis.get_minor_ticks()):
                for lab in (getattr(tick, "label1", None), getattr(tick, "label2", None)):
                    if lab is not None:
                        index[id(lab)] = (ax, axis, tick)
    return index


def _skip_tick(info) -> bool:
    """True when the tick label is not rendered (axis off, or tick outside view)."""
    ax, axis, tick = info
    try:
        if not getattr(ax, "axison", True):
            return True
        loc = float(tick.get_loc())
        lo, hi = ax.get_xlim() if axis is ax.xaxis else ax.get_ylim()
        lo, hi = (lo, hi) if lo <= hi else (hi, lo)
        return not (lo - 1e-9 <= loc <= hi + 1e-9)
    except Exception:  # pragma: no cover - defensive
        return False


def _collect_texts(fig):
    """Return (items, unmeasurable_count) after structural guards."""
    r = _renderer(fig)
    w, h = (v * fig.dpi for v in fig.get_size_inches())
    ticks = _tick_index(fig)
    items = []
    unmeasurable = 0
    for t in fig.findobj(match=Text):
        if not t.get_visible():
            continue
        s = (t.get_text() or "").strip()
        if not s:
            continue
        info = ticks.get(id(t))
        if info is not None and _skip_tick(info):
            continue
        bb = text_bbox(t, r)
        if bb.width <= 0 or bb.height <= 0:
            continue
        if bb.x0 < -0.5 * w or bb.x1 > 1.5 * w or bb.y0 < -0.5 * h or bb.y1 > 1.5 * h:
            unmeasurable += 1
            continue
        items.append((s, bb))
    return items, unmeasurable


def _overlaps_from(items, min_area_px2: float = OVERLAP_PX2, frac_of_smaller: float = OVERLAP_FRAC):
    out = []
    for i in range(len(items)):
        for j in range(i + 1, len(items)):
            a, b = items[i][1], items[j][1]
            if items[i][0] == items[j][0] and abs(a.x0 - b.x0) < 1.0 and abs(a.y0 - b.y0) < 1.0:
                continue  # same string drawn twice at the same spot = one visual label
            x = max(0.0, min(a.x1, b.x1) - max(a.x0, b.x0))
            y = max(0.0, min(a.y1, b.y1) - max(a.y0, b.y0))
            area = x * y
            if area <= min_area_px2:
                continue
            smaller = min(a.width * a.height, b.width * b.height)
            if smaller <= 0 or area / smaller < frac_of_smaller:
                continue
            out.append(
                {
                    "a": items[i][0][:48],
                    "b": items[j][0][:48],
                    "area_px2": round(area, 1),
                    "frac_of_smaller": round(area / smaller, 3),
                }
            )
    return out


def text_overlaps(fig, min_area_px2: float = OVERLAP_PX2, frac_of_smaller: float = OVERLAP_FRAC):
    items, _ = _collect_texts(fig)
    return _overlaps_from(items, min_area_px2, frac_of_smaller)


def min_fontsize(fig):
    ticks = _tick_index(fig)
    best = None
    for t in fig.findobj(match=Text):
        if not t.get_visible():
            continue
        s = (t.get_text() or "").strip()
        if not s:
            continue
        info = ticks.get(id(t))
        if info is not None and _skip_tick(info):
            continue
        fs = float(t.get_fontsize())
        if best is None or fs < best[0]:
            best = (fs, s[:40])
    return best if best else (0.0, "")


def out_of_bounds(fig):
    w, h = (v * fig.dpi for v in fig.get_size_inches())
    items, _ = _collect_texts(fig)
    bad = []
    for s, bb in items:
        if bb.x0 < -1 or bb.y0 < -1 or bb.x1 > w + 1 or bb.y1 > h + 1:
            bad.append({"text": s[:40], "bbox": [round(v, 1) for v in (bb.x0, bb.y0, bb.x1, bb.y1)]})
    return bad


# ---------------------------------------------------------------- new checks
def _sub(arr, cap):
    return arr[:: max(1, len(arr) // cap)]


def _artist_points(art, ax, cap: int = 600):
    """Return (display_points, kind) for data-bearing artists; (None, kind) otherwise.

    Covers: Line2D, PathCollection (scatter, via offsets - its paths are unit
    markers), PolyCollection / LineCollection / PatchCollection (geopandas
    polygons, via path vertices in data coords).
    """
    from matplotlib.collections import LineCollection, PatchCollection, PathCollection, PolyCollection
    from matplotlib.lines import Line2D

    try:
        if isinstance(art, PathCollection):
            off = art.get_offsets()
            if off is None or len(off) == 0:
                return None, "coll"
            return _sub(ax.transData.transform(np.asarray(off, dtype=float)), cap), "coll"
        if isinstance(art, Line2D):
            d = art.get_xydata()
            if d is None or len(d) == 0:
                return None, "line"
            return _sub(ax.transData.transform(np.asarray(d, dtype=float)), cap), "line"
        if isinstance(art, (PolyCollection, LineCollection, PatchCollection)):
            vs = [p.vertices for p in art.get_paths() if p.vertices is not None and len(p.vertices)]
            if not vs:
                return None, "coll"
            return _sub(ax.transData.transform(np.vstack(vs)), cap), "coll"
    except Exception:
        return None, "coll"
    return None, "coll"


def legend_conflicts(fig):
    """Detect legends drawn on top of opaque data (legend-data overlap).

    Collections (scatter/polygons) count only when essentially opaque, so a
    translucent fill band under a legend does not trip the check.
    """
    from matplotlib.collections import Collection

    out = []
    for idx, ax in enumerate(fig.get_axes()):
        try:
            leg = ax.get_legend()
            if leg is None or not leg.get_visible():
                continue
            lbb = leg.get_window_extent(renderer=_renderer(fig)).expanded(0.96, 0.96)
        except Exception:
            continue
        n_coll = n_line = s_coll = 0
        for art in ax.get_children():
            pts, kind = _artist_points(art, ax)
            if pts is None or not len(pts):
                continue
            inside = int(np.count_nonzero((pts[:, 0] >= lbb.x0) & (pts[:, 0] <= lbb.x1) & (pts[:, 1] >= lbb.y0) & (pts[:, 1] <= lbb.y1)))
            if not inside:
                continue
            if kind == "coll":
                if isinstance(art, Collection):
                    a = art.get_alpha()
                    if a is not None and a < LEGEND_ALPHA_MIN:
                        continue
                n_coll += inside
                s_coll += len(pts)
            else:
                n_line += inside
        frac = (n_coll / s_coll) if s_coll else 0.0
        if (n_coll >= LEGEND_MIN_POINTS_COLL and frac >= LEGEND_MIN_FRAC) or n_line >= LEGEND_MIN_POINTS_LINE:
            out.append({"ax": idx, "points_collection": n_coll, "points_line": n_line, "frac_of_sampled": round(frac, 3)})
    return out


def margin_check(fig):
    """Worst margin (in mm) between any rendered text/legend and the canvas edge."""
    r = _renderer(fig)
    w, h = (v * fig.dpi for v in fig.get_size_inches())
    items, _ = _collect_texts(fig)
    boxes = [(s[:24], bb) for s, bb in items]
    for idx, ax in enumerate(fig.get_axes()):
        try:
            leg = ax.get_legend()
            if leg is not None and leg.get_visible():
                boxes.append((f"legend#{idx}", leg.get_window_extent(renderer=r)))
        except Exception:
            continue
    worst = None
    for label, bb in boxes:
        px = min(bb.x0, bb.y0, w - bb.x1, h - bb.y1)
        if worst is None or px < worst[0]:
            worst = (px, label)
    if worst is None:
        return None, ""
    return worst[0] / fig.dpi * 25.4, worst[1]


def balance_issues(fig):
    """Detect sparsely-peripheried layouts (outlier-stretched, compressed core)."""
    out = []
    for idx, ax in enumerate(fig.get_axes()):
        try:
            if getattr(ax, "name", "") == "3d":
                continue
            parts = []
            for art in ax.get_children():
                pts, _k = _artist_points(art, ax, cap=2000)
                if pts is not None and len(pts):
                    parts.append(pts)
            if not parts:
                continue
            P = np.vstack(parts)
            if len(P) < 20:
                continue
            full = (float(P[:, 0].max() - P[:, 0].min())) * (float(P[:, 1].max() - P[:, 1].min()))
            q = np.percentile(P, [5, 95], axis=0)
            core = max(1.0, float(q[1, 0] - q[0, 0]) * float(q[1, 1] - q[0, 1]))
            ratio = full / core
            if ratio > BALANCE_RATIO_FAIL:
                out.append({"ax": idx, "extent_ratio": round(ratio, 2), "points": int(len(P))})
        except Exception:
            continue
    return out


# ---------------------------------------------------------------- pdf check
def pdf_check(path):
    """PDF page size + font embedding. Fail-closed: any parser/font-entry error is
    reported in `font_errors` / `status` and MUST be treated as FAIL by run_gate."""
    try:
        from pypdf import PdfReader
    except ImportError:
        return {"status": "error", "reason": "pypdf not installed"}
    try:
        reader = PdfReader(str(path))
        page = reader.pages[0]
        mb = page.mediabox
        fonts, errors = [], []
        try:
            font_dict = page.get("/Resources", {}).get("/Font", {})
            for key, ref in font_dict.items():
                try:
                    fo = ref.get_object()
                    base = str(fo.get("/BaseFont"))
                    subtype = str(fo.get("/Subtype"))
                    # Type3 glyphs are procedure streams stored inline (/CharProcs):
                    # the glyph data lives in the PDF itself -> embedded by construction.
                    embedded = subtype == "/Type3"
                    desc = fo.get("/FontDescriptor")
                    if desc is not None:
                        d = desc.get_object()
                        embedded = embedded or any(k in d for k in ("/FontFile", "/FontFile2", "/FontFile3"))
                    if not embedded and subtype == "/Type0":
                        for df in fo.get("/DescendantFonts") or []:
                            dfobj = df.get_object()
                            dd = dfobj.get("/FontDescriptor")
                            if dd is not None and any(
                                k in dd.get_object() for k in ("/FontFile", "/FontFile2", "/FontFile3")
                            ):
                                embedded = True
                                break
                    fonts.append({"name": base, "subtype": subtype, "embedded": bool(embedded)})
                except Exception as exc:
                    errors.append(f"{key}: {type(exc).__name__}: {exc}")
        except Exception as exc:
            errors.append(f"resources: {type(exc).__name__}: {exc}")
        return {
            "width_mm": round(float(mb.width) / 72.0 * 25.4, 1),
            "height_mm": round(float(mb.height) / 72.0 * 25.4, 1),
            "fonts": fonts,
            "font_errors": errors,
        }
    except Exception as exc:
        return {"status": "error", "reason": f"{type(exc).__name__}: {exc}"}


def _is_base14(name: str) -> bool:
    return any(x in name for x in _BASE14)


def font_problems(fig) -> list[str]:
    """Capture font-related warnings during a draw: findfont fallback / missing glyphs.

    A silent matplotlib fallback is NOT acceptable for a PASS (2026-09-28 review, item C1/C2).
    """
    with warnings.catch_warnings(record=True) as rec:
        warnings.simplefilter("always")
        try:
            fig.canvas.draw()
        except Exception:
            return []
    out = []
    for w in rec:
        m = str(w.message)
        if ("findfont" in m) or ("missing from font" in m) or ("missing from current font" in m):
            out.append(m)
    return out


# ---------------------------------------------------------------- export
def export_bundle(fig, outdir, name: str, dpi: int = 600, print_mm: float = PRINT_PREVIEW_MM):
    outdir = Path(outdir)
    outdir.mkdir(parents=True, exist_ok=True)
    paths = {
        "pdf": outdir / f"{name}.pdf",
        "svg": outdir / f"{name}.svg",
        "png": outdir / f"{name}.png",
    }
    fig.savefig(paths["pdf"], facecolor="white")
    fig.savefig(paths["svg"], facecolor="white")
    fig.savefig(paths["png"], dpi=dpi, facecolor="white")
    try:
        from PIL import Image

        with Image.open(paths["png"]) as im:
            paths["grayscale"] = outdir / f"{name}_grayscale.png"
            im.convert("L").save(paths["grayscale"], dpi=(dpi, dpi))
            target_px = int(round(print_mm / 25.4 * dpi))
            if im.width != target_px:
                ratio = target_px / im.width
                im2 = im.resize((target_px, max(1, int(round(im.height * ratio)))), Image.Resampling.LANCZOS)
            else:
                im2 = im
            paths["print_preview"] = outdir / f"{name}_print{int(print_mm)}mm.png"
            im2.save(paths["print_preview"], dpi=(dpi, dpi))
    except ImportError:
        pass
    return {k: str(v) for k, v in paths.items()}


# ---------------------------------------------------------------- gate
def run_gate(fig, outdir, name: str, min_pt: float = DEFAULT_MIN_PT):
    outdir = Path(outdir)
    items, unmeasurable = _collect_texts(fig)
    overlaps = _overlaps_from(items)
    oob = out_of_bounds(fig)
    fs, fs_text = min_fontsize(fig)
    legend_hits = legend_conflicts(fig)
    worst_margin_mm, margin_label = margin_check(fig)
    balance = balance_issues(fig)
    fmsgs = font_problems(fig)
    ce_fail, ce_limit, ce_counts = [], [], {}
    try:
        _ce_path = Path(__file__).resolve().parents[2] / "collision-aware-layout" / "scripts"
        if str(_ce_path) not in sys.path:
            sys.path.insert(0, str(_ce_path))
        import collision_engine as _cem

        _rep = _cem.check(fig)
        ce_fail = _cem.fail_lines(_rep)
        ce_limit = _cem.limitation_lines(_rep)
        ce_counts = _cem.counts(_rep)
    except Exception as exc:  # engine absence must be visible, never silent
        ce_limit = [f"collision engine unavailable: {type(exc).__name__}: {exc}"]
    paths = export_bundle(fig, outdir, name)
    pdf = pdf_check(paths["pdf"])

    fails, limitations = [], []
    if overlaps:
        fails.append(f"text-text overlap x{len(overlaps)}")
    if oob:
        fails.append(f"text out-of-bounds x{len(oob)}")
    if fs and fs < min_pt:
        fails.append(f"min fontsize {fs}pt < {min_pt}pt ({fs_text!r})")
    if fmsgs:
        fails.append(f"font fallback/missing glyph x{len(fmsgs)}: {fmsgs[0][:140]}")
    fails.extend(ce_fail)
    limitations.extend(ce_limit)
    if legend_hits:
        worst = max(legend_hits, key=lambda d: d["points_collection"] + d["points_line"])
        fails.append(
            f"legend-data overlap: ax#{worst['ax']} collection_points={worst['points_collection']} "
            f"line_points={worst['points_line']} frac={worst['frac_of_sampled']}"
        )
    if worst_margin_mm is not None:
        if worst_margin_mm < MARGIN_FAIL_MM:
            fails.append(f"margin {worst_margin_mm:.2f}mm < {MARGIN_FAIL_MM}mm ({margin_label})")
        elif worst_margin_mm < MARGIN_WARN_MM:
            limitations.append(f"margin {worst_margin_mm:.2f}mm < {MARGIN_WARN_MM}mm ({margin_label})")
    if balance:
        worst_b = max(balance, key=lambda d: d["extent_ratio"])
        fails.append(
            f"layout balance: ax#{worst_b['ax']} extent_ratio={worst_b['extent_ratio']} "
            f"(> {BALANCE_RATIO_FAIL}) - sparse periphery / compressed core"
        )
    if unmeasurable:
        limitations.append(f"{unmeasurable} text extents unmeasurable (3D projection) - visual check mandatory")

    # ---- PDF fail-closed ----
    if isinstance(pdf, dict) and (pdf.get("status") == "error" or pdf.get("font_errors")):
        fails.append("pdf font check failed: " + str(pdf.get("reason") or "; ".join(pdf.get("font_errors", []))[:180]))
    elif isinstance(pdf, dict) and pdf.get("fonts"):
        non_emb = [f for f in pdf["fonts"] if isinstance(f, dict) and f.get("embedded") is False]
        hard = [f for f in non_emb if not _is_base14(str(f.get("name")))]
        soft = [f for f in non_emb if _is_base14(str(f.get("name")))]
        if hard:
            fails.append("non-embedded fonts: " + ", ".join(str(f.get("name")) for f in hard[:5]))
        if soft:
            limitations.append("base14 fonts not embedded: " + ", ".join(str(f.get("name")) for f in soft[:5]))

    threshold_source = "default-SCI-8pt" if abs(min_pt - DEFAULT_MIN_PT) < 1e-9 else "override"
    status = "FAIL" if fails else ("PASS_WITH_LIMITATION" if limitations else "PASS")
    report = {
        "name": name,
        "status": status,
        "min_pt_threshold": min_pt,
        "threshold_source": threshold_source,
        "min_fontsize": fs,
        "min_fontsize_text": fs_text,
        "text_overlaps": overlaps,
        "out_of_bounds": oob,
        "legend_conflicts": legend_hits,
        "collisions": ce_counts,
        "margin_mm": None if worst_margin_mm is None else round(worst_margin_mm, 3),
        "margin_label": margin_label,
        "balance_issues": balance,
        "pdf": pdf,
        "fails": fails,
        "limitations": limitations,
        "paths": paths,
        "note": "自动检查为辅助；目检（含灰度与缩印预览）必须执行；箭头压字/数据遮挡不在自动范围。",
    }
    (outdir / f"{name}_gate.json").write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    lines = [f"# Figure Gate — {name} — {status}", ""]
    lines += [
        f"- min fontsize: {fs} pt (threshold {min_pt}, source {threshold_source})",
        f"- text overlaps: {len(overlaps)}",
        f"- out-of-bounds: {len(oob)}",
        f"- legend conflicts: {len(legend_hits)}",
        f"- margin: {report['margin_mm']} mm ({margin_label})",
        f"- balance issues: {len(balance)}",
    ]
    if isinstance(pdf, dict) and "width_mm" in pdf:
        lines.append(f"- pdf page: {pdf['width_mm']} x {pdf['height_mm']} mm; fonts: {len(pdf.get('fonts', []))}; errors: {len(pdf.get('font_errors', []))}")
    lines += [f"- FAIL: {m}" for m in fails] or ["- FAIL: (none)"]
    lines += [f"- LIMITATION: {m}" for m in limitations] or ["- LIMITATION: (none)"]
    (outdir / f"{name}_gate.md").write_text("\n".join(lines), encoding="utf-8")
    print(f"[figure-qa] {name}: {status} (min {fs}pt, overlaps {len(overlaps)}, oob {len(oob)}, legend {len(legend_hits)}, margin {report['margin_mm']}mm, balance {len(balance)})")
    for m in fails:
        print(f"  FAIL  {m}")
    for m in limitations:
        print(f"  LIMIT {m}")
    return report


def _load_builder(path):
    spec = importlib.util.spec_from_file_location("qa_builder", path)
    if spec is None or spec.loader is None:
        raise SystemExit(f"cannot load builder: {path}")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--builder", required=True, help="python file exposing build() -> Figure")
    ap.add_argument("--out", required=True)
    ap.add_argument("--name", default=None)
    ap.add_argument("--min-pt", type=float, default=DEFAULT_MIN_PT, help="venue override only; record the basis")
    args = ap.parse_args()
    mod = _load_builder(args.builder)
    fig = mod.build()
    name = args.name or Path(args.builder).stem
    rep = run_gate(fig, outdir=args.out, name=name, min_pt=args.min_pt)
    sys.exit(1 if rep["status"] == "FAIL" else 0)


if __name__ == "__main__":
    main()
