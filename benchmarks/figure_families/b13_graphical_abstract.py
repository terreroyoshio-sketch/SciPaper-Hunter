"""b13: graphical abstract - geometric scene + process column + embedded result insets (synthetic).

One core message, single reading path (left -> right), geometric scene rather
than icon soup; result insets are the only data-bearing elements.
"""

from __future__ import annotations

import numpy as np
from matplotlib.patches import Circle, Polygon, Rectangle

import bench_common as bc  # noqa: F401  (sets sys.path for trd_kit)
import trd_kit as tk


def _timeseries(ax) -> None:
    rng = np.random.default_rng(313)
    t = np.arange(60)
    a = 50 + 13 * np.sin(t / 8.0) + rng.normal(0, 2.6, 60)
    ax.plot(t, a, lw=0.9, color="#4472C4")
    ax.set_xlim(0, 59)
    ax.set_ylim(20, 80)
    ax.set_xticks([])
    ax.set_yticks([])
    for s in ax.spines.values():
        s.set_linewidth(0.5)
        s.set_color("#9E9E9E")


def _bars(ax) -> None:
    names = ["A", "B", "C", "D"]
    vals = np.array([0.62, 0.45, 0.28, 0.15])
    ax.bar(names, vals, color="#CDD8E8", edgecolor="#4A78B0", linewidth=0.6)
    ax.set_ylim(0, 0.78)
    ax.set_xticks(range(4))
    ax.set_xticklabels(names, fontsize=8)
    ax.set_yticks([])
    for s in ax.spines.values():
        s.set_linewidth(0.5)
        s.set_color("#9E9E9E")
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)


def build():
    W, H = 170.0, 100.0
    c = tk.Canvas(W, H)
    ax = c.ax

    # ---- scene (bottom-origin coords): ground band, hills, trees, sun
    ax.add_patch(Rectangle((6, 8), 66, 26, facecolor="#F3EAD8", edgecolor="none", zorder=1))
    ax.plot([6, 72], [34, 34], color="#8B7355", lw=1.2, zorder=2)
    ax.add_patch(Polygon([(6, 34), (24, 54), (40, 36), (56, 56), (70, 34)], closed=True, facecolor="#E6EFDF", edgecolor="#9BB98A", lw=0.6, zorder=2))
    for cx in (18, 32, 46):
        ax.add_patch(Rectangle((cx - 1.2, 34), 2.4, 9, facecolor="#9C7A4D", edgecolor="none", zorder=3))
        ax.add_patch(Circle((cx, 47), 5.2, facecolor="#8FBC77", edgecolor="#5E8A4C", lw=0.8, zorder=4))
    ax.add_patch(Circle((62, 70), 5.5, facecolor="#F4D03F", edgecolor="#C9A715", lw=0.8, zorder=3))

    # ---- process column (semantic containers)
    c.box(80, 20, 30, 12, "Observe", "input", id="ga1")
    c.box(80, 42, 30, 12, "Model", "process", id="ga2")
    c.box(80, 64, 30, 12, "Predict", "method", id="ga3")
    c.arrow(95, 33.5, 95, 41.5, id="ga12")
    c.arrow(95, 55.5, 95, 63.5, id="ga23")
    c.arrow(73.5, 26, 79, 26, id="scene2obs")

    # ---- embedded result insets
    c.text(118, 17.0, "Response", fontsize=8.0, color="#444444", id="lbl1")
    axp = c.plot_slot(118, 19.5, 44, 26, id="inset1")
    _timeseries(axp)
    c.text(118, 51.0, "Sensitivity", fontsize=8.0, color="#444444", id="lbl2")
    axp = c.plot_slot(118, 53.5, 44, 26, id="inset2")
    _bars(axp)
    c.arrow(110.5, 26, 117, 26, id="obs2inset")
    c.arrow(110.5, 66, 117, 66, id="pred2inset")

    c.legend(6.0, 6.5, [("input", "Observe"), ("process", "Model"), ("method", "Predict")])
    bc.mark(c.fig)
    return c.fig
