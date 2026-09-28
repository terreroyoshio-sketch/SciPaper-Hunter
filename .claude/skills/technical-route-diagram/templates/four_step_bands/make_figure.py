"""Four-band technical route diagram template (v1) — 四步横带.

Content lives in content.json (text only); geometry lives here.
Renders SVG / PDF / PNG(+grayscale) and runs automatic layout QA.

Usage:
    python make_figure.py --out <outdir> [--name four_step_bands_demo]
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[1] / "scripts"))

import trd_kit as tk  # noqa: E402
from qa_layout import check  # noqa: E402

BAND_X = 5.0
BAND_W = 160.0
BAND_H = 42.5
BAND_GAP = 9.5
BANDS_TOP = 12.0
BOX_REGION = (10.0, 113.0)
BOX_H = 11.0
PLOT_X = 117.0
PLOT_W = 43.0
PLOT_TOP_OFFSET = 11.0
PLOT_H = 26.0
LEGEND_TOP = 6.0
FOOTER_TOP = 214.5


def _clean(ax) -> None:
    ax.set_xticks([])
    ax.set_yticks([])
    for spine in ax.spines.values():
        spine.set_linewidth(0.5)
        spine.set_color("#9E9E9E")


def draw_timeseries(ax) -> None:
    rng = np.random.default_rng(42)
    t = np.arange(60)
    a = 52 + 16 * np.sin(t / 9.0) + rng.normal(0, 3.2, 60)
    b = 34 + 9 * np.sin(t / 9.0 + 1.1) + rng.normal(0, 2.4, 60)
    ax.plot(t, a, lw=0.9, color="#4472C4")
    ax.plot(t, b, lw=0.9, color="#C55A11", ls="--")
    ax.set_xlim(0, 59)
    ax.set_ylim(0, 80)
    _clean(ax)


def draw_scatter(ax) -> None:
    rng = np.random.default_rng(7)
    x = rng.uniform(0, 12, 42)
    y = 0.55 * x + 1.0 + rng.normal(0, 1.1, 42)
    ax.scatter(x, y, s=5, color="#7030A0", alpha=0.75, linewidths=0)
    k, c = np.polyfit(x, y, 1)
    xs = np.linspace(0, 12, 20)
    ax.plot(xs, k * xs + c, lw=0.8, color="#C55A11")
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 9)
    _clean(ax)


def draw_stepseries(ax) -> None:
    rng = np.random.default_rng(3)
    t = np.arange(80)
    s = 1.1 * np.sin(t / 6.0) + rng.normal(0, 0.22, 80)
    thr = 0.55
    ax.plot(t, s, lw=0.8, color="#7030A0")
    ax.axhline(thr, lw=0.7, color="#C00000", ls="--")
    ax.fill_between(t, s, thr, where=(s > thr), color="#F4B183", alpha=0.45, lw=0)
    ax.set_xlim(0, 79)
    ax.set_ylim(-1.6, 1.8)
    _clean(ax)


def draw_bars(ax) -> None:
    names = ["Factor 1", "Factor 2", "Factor 3", "Factor 4", "Factor 5"]
    vals = np.array([0.42, 0.31, 0.18, 0.12, 0.07])
    order = np.argsort(vals)
    colors = ["#F7CDA8"] * (len(vals) - 1) + ["#C55A11"]
    ax.barh(range(len(vals)), vals[order], height=0.62, color=colors, edgecolor="#C55A11", linewidth=0.5)
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_xlim(0, 0.62)
    ax.set_ylim(-0.6, len(vals) - 0.4)
    for yi, idx in enumerate(order):
        ax.text(vals[idx] + 0.012, yi, names[idx], va="center", ha="left", fontsize=8.0, color="#222222")
    for side in ("top", "right", "left"):
        ax.spines[side].set_visible(False)
    ax.spines["bottom"].set_linewidth(0.5)
    ax.spines["bottom"].set_color("#9E9E9E")


PLOTS = {
    "timeseries": draw_timeseries,
    "scatter": draw_scatter,
    "stepseries": draw_stepseries,
    "bars": draw_bars,
}


def render(content: dict, outdir: Path, name: str) -> str:
    w, h = content["figure_size_mm"]
    c = tk.Canvas(w, h)
    c.legend(BAND_X, LEGEND_TOP, list(content["legend"]))

    for i, band in enumerate(content["bands"]):
        y_top = BANDS_TOP + i * (BAND_H + BAND_GAP)
        c.band(BAND_X, y_top, BAND_W, BAND_H, band["index"], band["title"])

        boxes = band["boxes"]
        n = len(boxes)
        box_w = 24.0 if n <= 3 else 23.0
        x0, x1 = BOX_REGION
        step = (x1 - x0 - box_w) / (n - 1) if n > 1 else 0.0
        box_top = y_top + 19.25
        mid = box_top + BOX_H / 2.0
        prev_x = None
        for j, (label, family) in enumerate(boxes):
            bx = x0 + j * step
            c.box(bx, box_top, box_w, BOX_H, label, family=family, id=f"b{band['index']}-box{j + 1}")
            if prev_x is not None:
                c.arrow(prev_x + box_w + 0.9, mid, bx - 0.9, mid, id=f"b{band['index']}-arrow{j}")
            prev_x = bx

        plot_ax = c.plot_slot(PLOT_X, y_top + PLOT_TOP_OFFSET, PLOT_W, PLOT_H, id=f"b{band['index']}-plot")
        PLOTS[band["plot"]](plot_ax)

        if i < len(content["bands"]) - 1:
            band_bottom = y_top + BAND_H
            c.block_arrow_down(BAND_X + BAND_W / 2.0, band_bottom + 0.7, band_bottom + 8.7, id=f"gap-arrow-{i + 1}")

    c.text(BAND_X, FOOTER_TOP, content["footer_marker"], fontsize=8.0, color=tk.MUTED, italic=True, id="footer-marker")

    paths = c.export(outdir, name)
    status, _, _ = check(c, outdir=outdir, name="qa_report")
    print("[render] outputs:")
    for k, v in paths.items():
        print(f"  {k}: {v}")
    return status


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default=str(HERE / "out"))
    ap.add_argument("--name", default="four_step_bands_demo")
    args = ap.parse_args()
    content = json.loads((HERE / "content.json").read_text(encoding="utf-8"))
    status = render(content, Path(args.out), args.name)
    sys.exit(1 if status == "FAIL" else 0)


if __name__ == "__main__":
    main()
