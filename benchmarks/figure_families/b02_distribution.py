"""b02: statistical figure - histogram+KDE / box+strip / violin (synthetic)."""

from __future__ import annotations

import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import gaussian_kde

import bench_common as bc


def build():
    bc.apply_house_style()
    rng = np.random.default_rng(102)
    fig, axes = plt.subplots(1, 3, figsize=bc.mm(170, 58))
    fig.subplots_adjust(left=0.085, right=0.99, top=0.82, bottom=0.25, wspace=0.32)

    a = rng.normal(0, 1, 200)
    b = rng.normal(1.6, 1.3, 200)

    ax = axes[0]
    ax.hist(a, bins=18, density=True, color="#B9CDE5", edgecolor="#4A78B0", lw=0.6)
    xs = np.linspace(-4, 5, 220)
    ax.plot(xs, gaussian_kde(a)(xs), lw=1.1, color="#1F4E79")
    ax.set_xlabel("Value")
    ax.set_ylabel("Density")
    bc.panel_label(ax, "a")

    ax = axes[1]
    bp = ax.boxplot([a, b], widths=0.5, patch_artist=True, showfliers=False)
    for patch, col in zip(bp["boxes"], ["#B9CDE5", "#F2C7A7"]):
        patch.set_facecolor(col)
        patch.set_edgecolor("#444444")
        patch.set_linewidth(0.7)
    for med in bp["medians"]:
        med.set_color("#222222")
        med.set_linewidth(0.9)
    for i, arr in enumerate([a, b], start=1):
        jitter = rng.uniform(-0.12, 0.12, len(arr))
        ax.scatter(i + jitter, arr[: len(arr)], s=2.5, color="#333333", alpha=0.35, linewidths=0)
    ax.set_xticks([1, 2])
    ax.set_xticklabels(["Group A", "Group B"])
    ax.set_ylabel("Value")
    bc.panel_label(ax, "b")

    ax = axes[2]
    parts = ax.violinplot([a, b], showmedians=True)
    for body, col in zip(parts["bodies"], ["#B9CDE5", "#F2C7A7"]):
        body.set_facecolor(col)
        body.set_edgecolor("#444444")
        body.set_linewidth(0.7)
        body.set_alpha(0.9)
    parts["cmedians"].set_color("#222222")
    ax.set_xticks([1, 2])
    ax.set_xticklabels(["Group A", "Group B"])
    ax.set_ylabel("Value")
    bc.panel_label(ax, "c")

    bc.mark(fig)
    return fig
