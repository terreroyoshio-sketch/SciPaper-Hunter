"""b11: multipanel composite - 2x3 grid of heterogeneous panels (synthetic)."""

from __future__ import annotations

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch

import bench_common as bc


def _mini_flow(ax):
    fams = [("#DAEAC9", "#70AD47"), ("#AFC9E5", "#4472C4"), ("#F7CDA8", "#C55A11")]
    labels = ["Input", "Model", "Result"]
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 4)
    ax.axis("off")
    for i, (lab, (fill, edge)) in enumerate(zip(labels, fams)):
        x = 0.3 + i * 3.3
        ax.add_patch(FancyBboxPatch((x, 1.3), 2.4, 1.4, boxstyle="round,pad=0,rounding_size=0.25", facecolor=fill, edgecolor=edge, linewidth=0.8))
        ax.text(x + 1.2, 2.0, lab, fontsize=8.0, ha="center", va="center", color="#222222")
        if i:
            ax.add_patch(FancyArrowPatch((x - 0.4, 2.0), (x - 0.05, 2.0), arrowstyle="-|>", mutation_scale=7, lw=0.9, color="#222222"))


def build():
    bc.apply_house_style()
    rng = np.random.default_rng(111)
    fig = plt.figure(figsize=bc.mm(170, 108))
    gs = fig.add_gridspec(2, 3, left=0.088, right=0.985, top=0.90, bottom=0.09, wspace=0.45, hspace=0.46)

    ax = fig.add_subplot(gs[0, 0])
    t = np.arange(60)
    ax.plot(t, np.sin(t / 8) + rng.normal(0, 0.12, 60), lw=0.9, color=bc.PALETTE["blue"])
    ax.set_xlabel("t")
    ax.set_ylabel("signal")
    bc.panel_label(ax, "a")

    ax = fig.add_subplot(gs[0, 1])
    m = rng.normal(0, 1, (6, 6))
    m = np.asarray(np.corrcoef(m))
    im = ax.imshow(m, vmin=-1, vmax=1, cmap="RdBu_r")
    ax.set_xticks([])
    ax.set_yticks([])
    fig.colorbar(im, ax=ax, fraction=0.045, pad=0.03).ax.tick_params(labelsize=8.0)
    bc.panel_label(ax, "b")

    ax = fig.add_subplot(gs[0, 2])
    x = rng.uniform(0, 1, 50)
    y = 0.8 * x + rng.normal(0, 0.12, 50)
    ax.scatter(x, y, s=6, color=bc.PALETTE["green"], alpha=0.8, linewidths=0)
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    bc.panel_label(ax, "c")

    ax = fig.add_subplot(gs[1, 0])
    vals = rng.normal(1.0, 0.25, (4, 12))
    ax.boxplot(vals.T, widths=0.5, showfliers=False)
    ax.set_xticks([1, 2, 3, 4])
    ax.set_xticklabels(["S1", "S2", "S3", "S4"])
    ax.set_ylabel("level")
    bc.panel_label(ax, "d")

    ax = fig.add_subplot(gs[1, 1])
    names = ["A", "B", "C", "D"]
    vals = np.array([0.62, 0.48, 0.31, 0.22])
    ax.bar(names, vals, color="#CDD8E8", edgecolor="#4A78B0", linewidth=0.6)
    ax.set_ylabel("score")
    bc.panel_label(ax, "e")

    ax = fig.add_subplot(gs[1, 2])
    _mini_flow(ax)
    bc.panel_label(ax, "f")

    bc.mark(fig)
    return fig
