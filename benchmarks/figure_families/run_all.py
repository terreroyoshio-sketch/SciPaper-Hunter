"""Run all figure-family benchmarks through the unified figure-quality-gate.

Usage:
    python run_all.py [--out <dir>] [--only b04 b05 ...]

Outputs (under --out, default ./out):
    <key>/<key>.pdf|.svg|.png|<key>_grayscale.png|<key>_print89mm.png|<key>_gate.md|.json
    summary.md / summary.json
    contact_sheet.png  (4-col grid of all rendered PNGs)
"""

from __future__ import annotations

import argparse
import importlib
import json
import sys
import traceback
from pathlib import Path

import matplotlib.pyplot as plt
from PIL import Image, ImageDraw

HERE = Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))

import bench_common as bc  # noqa: E402

BENCHES = [
    ("b01", "b01_line_scatter", "数据图：时序+散点"),
    ("b02", "b02_distribution", "统计图：分布三面板"),
    ("b03", "b03_heatmap", "统计图：相关热力图"),
    ("b04", "b04_method_framework", "方法框架：三层结构（trd_kit）"),
    ("b05", "b05_technical_roadmap", "技术路线图：四阶段带（trd_kit）"),
    ("b06", "b06_algorithm_dag", "算法流程图：dot 布局→自绘"),
    ("b07", "b07_mechanism_schematic", "机制示意图：几何构图"),
    ("b08", "b08_geospatial", "GIS：choropleth（geopandas）"),
    ("b09", "b09_network", "网络图：社区结构（networkx）"),
    ("b10", "b10_engineering_schematic", "工程图：RC 电路（schemdraw）"),
    ("b11", "b11_multipanel", "多面板复合：2x3"),
    ("b12", "b12_3d", "3D 兜底路径：mplot3d 曲面+散点"),
    ("b13", "b13_graphical_abstract", "图形摘要：大场景+流程+结果小图"),
    ("b14", "b14_pyvista_3d", "3D 主路径：PyVista 渲染 + matplotlib 复合"),
]


def contact_sheet(rows: list[tuple[str, Path | None]], outpath: Path, cols: int = 4, cell_w: int = 540, cell_h: int = 700, pad: int = 14) -> None | str:
    """Uniform letterboxed cells (fixes the ragged aspect-ratio whitespace)."""
    tiles = []
    for name, p in rows:
        if not (p and p.exists()):
            continue
        im = Image.open(p).convert("RGB")
        im.thumbnail((cell_w - 2 * pad, cell_h - 2 * pad), Image.Resampling.LANCZOS)
        tile = Image.new("RGB", (cell_w, cell_h), "white")
        tile.paste(im, ((cell_w - im.width) // 2, (cell_h - im.height) // 2))
        d = ImageDraw.Draw(tile)
        d.rectangle([0, 0, cell_w - 1, cell_h - 1], outline="#CCCCCC")
        d.text((pad, pad), name, fill="#888888")
        tiles.append(tile)
    if not tiles:
        return "no images"
    rows_n = (len(tiles) + cols - 1) // cols
    sheet = Image.new("RGB", (cols * (cell_w + 10) + 10, rows_n * (cell_h + 10) + 10), "#EDEDED")
    for i, t in enumerate(tiles):
        r, c = divmod(i, cols)
        sheet.paste(t, (10 + c * (cell_w + 10), 10 + r * (cell_h + 10)))
    sheet.save(outpath)
    return None


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default=str(HERE / "out"))
    ap.add_argument("--only", nargs="*", default=None)
    args = ap.parse_args()
    outroot = Path(args.out)

    selected = [b for b in BENCHES if not args.only or b[0] in args.only]
    results = []
    for key, module, title in selected:
        subdir = outroot / key
        print(f"=== {key} {title} ===")
        try:
            mod = importlib.import_module(module)
            fig = mod.build()
            rep = bc.run_gate(fig, subdir, key, min_pt=bc.DEFAULT_MIN_PT)
            plt.close(fig)
            results.append({"key": key, "title": title, "status": rep["status"], "fails": rep["fails"], "limitations": rep["limitations"], "png": rep["paths"].get("png")})
        except Exception as exc:  # noqa: BLE001 - benchmark harness must survive one bad bench
            plt.close("all")
            results.append({"key": key, "title": title, "status": "ERROR", "fails": [f"{type(exc).__name__}: {exc}"], "limitations": [], "png": None})
            print(f"[bench] {key} ERROR: {traceback.format_exc(limit=2)}")

    sheet_err = contact_sheet([(r["key"], Path(r["png"]) if r["png"] else None) for r in results], outroot / "contact_sheet.png")

    lines = ["# Figure-family benchmark summary", "", f"- benches: {len(results)}", ""]
    lines += ["| key | family | status | fails | limitations |", "|---|---|---|---|---|"]
    for r in results:
        lines.append(f"| {r['key']} | {r['title']} | **{r['status']}** | {'; '.join(r['fails']) or '-'} | {'; '.join(r['limitations']) or '-'} |")
    if sheet_err:
        lines += ["", f"- contact sheet: {sheet_err}"]
    (outroot / "summary.md").write_text("\n".join(lines), encoding="utf-8")
    (outroot / "summary.json").write_text(json.dumps({"results": results, "contact_sheet": str(outroot / 'contact_sheet.png')}, ensure_ascii=False, indent=2), encoding="utf-8")
    print("\n".join(lines))
    bad = [r for r in results if r["status"] == "FAIL"]
    sys.exit(1 if bad or any(r["status"] == "ERROR" for r in results) else 0)


if __name__ == "__main__":
    main()
