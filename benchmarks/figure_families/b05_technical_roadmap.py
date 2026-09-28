"""b05: technical roadmap - four stage bands with embedded output plots (synthetic, trd_kit)."""

from __future__ import annotations

import numpy as np

import bench_common as bc  # noqa: F401  (sets sys.path for trd_kit)
import trd_kit as tk


def _timeseries(ax, seed):
    rng = np.random.default_rng(seed)
    t = np.arange(70)
    a = 50 + 14 * np.sin(t / 8.5) + rng.normal(0, 3.0, 70)
    b = 33 + 8 * np.sin(t / 8.5 + 1.0) + rng.normal(0, 2.2, 70)
    ax.plot(t, a, lw=0.9, color="#4472C4")
    ax.plot(t, b, lw=0.9, color="#C55A11", ls="--")
    ax.set_xlim(0, 69)
    ax.set_ylim(0, 80)
    ax.set_xticks([])
    ax.set_yticks([])


def _bars(ax):
    names = ["Driver 1", "Driver 2", "Driver 3", "Driver 4", "Driver 5"]
    vals = np.array([0.44, 0.30, 0.16, 0.10, 0.06])
    order = np.argsort(vals)
    colors = ["#F7CDA8"] * (len(vals) - 1) + ["#C55A11"]
    ax.barh(range(len(vals)), vals[order], height=0.62, color=colors, edgecolor="#C55A11", linewidth=0.5)
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_xlim(0, 0.62)
    ax.set_ylim(-0.6, len(vals) - 0.4)
    for yi, idx in enumerate(order):
        ax.text(vals[idx] + 0.014, yi, names[idx], va="center", ha="left", fontsize=8.0, color="#222222")
    for side in ("top", "right", "left"):
        ax.spines[side].set_visible(False)
    ax.spines["bottom"].set_linewidth(0.5)
    ax.spines["bottom"].set_color("#9E9E9E")


def _scatter(ax, seed):
    rng = np.random.default_rng(seed)
    x = rng.uniform(0, 12, 40)
    y = 0.55 * x + 1.0 + rng.normal(0, 1.1, 40)
    ax.scatter(x, y, s=5, color="#7030A0", alpha=0.75, linewidths=0)
    k, c = np.polyfit(x, y, 1)
    xs = np.linspace(0, 12, 20)
    ax.plot(xs, k * xs + c, lw=0.8, color="#C55A11")
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 9)
    ax.set_xticks([])
    ax.set_yticks([])


def build():
    W, H = 170.0, 216.0
    c = tk.Canvas(W, H)
    band_x, band_w, band_h, gap = 5.0, 160.0, 42.5, 9.5
    top0 = 13.0
    stages = [
        ("1", "Data Collection and Preprocessing", [["Field Data", "input"], ["Remote\nSensing", "input"], ["Quality\nControl", "process"]], "timeseries"),
        ("2", "Model Construction", [["Process\nModel", "process"], ["Parameter\nCalibration", "process"], ["Cross-\nValidation", "method"]], "scatter"),
        ("3", "Index Development", [["Marginal\nDistributions", "accent"], ["Dependence\nModel", "method"], ["Composite\nIndex", "result"], ["Event\nMetrics", "result"]], "timeseries2"),
        ("4", "Analysis and Application", [["Feature Set", "input"], ["Gradient\nBoosting", "process"], ["Attribution\nAnalysis", "method"], ["Contribution\nRanking", "result"]], "bars"),
    ]
    plots = {"timeseries": lambda ax: _timeseries(ax, 105), "timeseries2": lambda ax: _timeseries(ax, 205), "scatter": lambda ax: _scatter(ax, 115), "bars": _bars}

    for i, (idx, title, boxes, plot_id) in enumerate(stages):
        y_top = top0 + i * (band_h + gap)
        c.band(band_x, y_top, band_w, band_h, idx, title)
        n = len(boxes)
        box_w = 24.0 if n <= 3 else 23.0
        x0, x1 = 10.0, 113.0
        step = (x1 - x0 - box_w) / (n - 1) if n > 1 else 0.0
        box_top = y_top + 19.25
        mid = box_top + 5.5
        prev = None
        for j, (label, fam) in enumerate(boxes):
            bx = x0 + j * step
            c.box(bx, box_top, box_w, 11.0, label, family=fam, id=f"{idx}-{j + 1}")
            if prev is not None:
                c.arrow(prev + box_w + 0.9, mid, bx - 0.9, mid, id=f"{idx}-arr{j}")
            prev = bx
        if i == 2:
            c.box(117, y_top + 28.0, 43, 9.5, r"$P(X \leq x) = F(x)$", "accent", fontsize=8.0, id=f"{idx}-formula")
            axp = c.plot_slot(117, y_top + 10.5, 43, 15.0, id=f"p-{idx}")
        else:
            axp = c.plot_slot(117, y_top + 11.0, 43, 26.0, id=f"p-{idx}")
        plots[plot_id](axp)
        if i < len(stages) - 1:
            band_bottom = y_top + band_h
            c.block_arrow_down(band_x + band_w / 2.0, band_bottom + 0.6, band_bottom + (gap - 0.6), id=f"gap-{i}")

    c.legend(5.0, 7.2, [("input", "Input"), ("process", "Process"), ("method", "Method"), ("result", "Result"), ("accent", "Highlight")])
    bc.mark(c.fig)
    return c.fig
