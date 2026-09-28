"""b03: statistical figure - annotated correlation heatmap (synthetic)."""

from __future__ import annotations

import matplotlib.pyplot as plt
import numpy as np

import bench_common as bc


def build():
    bc.apply_house_style()
    rng = np.random.default_rng(103)
    n = 8
    series = rng.normal(0, 1, (n, 40))
    corr = np.asarray(np.corrcoef(series))
    labels = [f"V{i + 1}" for i in range(n)]

    fig, ax = plt.subplots(figsize=bc.mm(120, 102))
    fig.subplots_adjust(left=0.11, right=0.84, top=0.92, bottom=0.11)

    im = ax.imshow(corr, vmin=-1, vmax=1, cmap="RdBu_r")
    ax.set_xticks(range(n))
    ax.set_yticks(range(n))
    ax.set_xticklabels(labels)
    ax.set_yticklabels(labels)
    ax.tick_params(length=0)
    for i in range(n):
        for j in range(n):
            v = corr[i, j]
            color = "white" if abs(v) > 0.62 else "#222222"
            ax.text(j, i, f"{v:.2f}", ha="center", va="center", fontsize=8.0, color=color)
    cbar = fig.colorbar(im, ax=ax, fraction=0.045, pad=0.02)
    cbar.set_label("Pearson r", fontsize=8.0)
    cbar.ax.tick_params(labelsize=8.0)

    bc.mark(fig)
    return fig
