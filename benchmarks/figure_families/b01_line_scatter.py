"""b01: publication data figure - time series + scatter (synthetic)."""

from __future__ import annotations

import matplotlib.pyplot as plt
import numpy as np

import bench_common as bc


def build():
    bc.apply_house_style()
    rng = np.random.default_rng(101)
    fig, axes = plt.subplots(1, 2, figsize=bc.mm(170, 60))
    fig.subplots_adjust(left=0.078, right=0.985, top=0.90, bottom=0.24, wspace=0.27)

    ax = axes[0]
    t = np.arange(120)
    y1 = 40 + 12 * np.sin(t / 14) + 0.08 * t + rng.normal(0, 2.2, 120)
    y2 = 32 + 8 * np.sin(t / 14 + 0.9) + rng.normal(0, 1.8, 120)
    ax.fill_between(t, y1 - 3.5, y1 + 3.5, color=bc.PALETTE["blue"], alpha=0.15, lw=0)
    ax.plot(t, y1, lw=1.0, color=bc.PALETTE["blue"], label="Series A")
    ax.plot(t, y2, lw=1.0, color=bc.PALETTE["orange"], ls="--", label="Series B")
    ax.set_xlabel("Time (months)")
    ax.set_ylabel("Value (mm)")
    ax.legend(frameon=False, loc="upper left")
    bc.panel_label(ax, "a")

    ax = axes[1]
    x = rng.uniform(0, 10, 60)
    y = 1.4 * x + 2 + rng.normal(0, 1.5, 60)
    ax.scatter(x, y, s=9, color=bc.PALETTE["green"], alpha=0.8, linewidths=0)
    k, c = np.polyfit(x, y, 1)
    xs = np.linspace(0, 10, 20)
    ax.plot(xs, k * xs + c, lw=1.0, color=bc.PALETTE["red"])
    ax.set_xlabel("Variable X")
    ax.set_ylabel("Variable Y")
    bc.panel_label(ax, "b")

    bc.mark(fig)
    return fig
