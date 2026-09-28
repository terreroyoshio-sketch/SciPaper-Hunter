"""T03: scatter labels - BEFORE (naive overlap) must FAIL, AFTER (engine) must PASS.

The engine plays the everyday role of adjustText for LOCAL scatter labels
(adjustText itself is not installed; if installed it may run as an auxiliary
layer - see collision-aware-layout SKILL).
"""

from __future__ import annotations

import sys
from pathlib import Path

_FAM = Path(__file__).resolve().parents[1] / "figure_families"
if str(_FAM) not in sys.path:
    sys.path.insert(0, str(_FAM))

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

import bench_common as bc  # noqa: F401


def _data():
    rng = np.random.default_rng(303)
    x = rng.uniform(0, 10, 60)
    y = 1.1 * x + 1.5 + rng.normal(0, 1.1, 60)
    return x, y


def _base_fig():
    bc.apply_house_style()
    x, y = _data()
    fig, ax = plt.subplots(figsize=bc.mm(120, 78))
    fig.subplots_adjust(left=0.11, right=0.975, top=0.90, bottom=0.22)
    ax.scatter(x, y, s=10, color=bc.PALETTE["green"], alpha=0.85, linewidths=0)
    ax.set_xlabel("Variable X")
    ax.set_ylabel("Variable Y")
    return fig, ax, x, y


def build_before():
    fig, ax, _x, _y = _base_fig()
    # deliberate: two labels overlapping each other and sitting on markers
    ax.text(6.0, 8.3, "Site-042", fontsize=8.0, color="#222222")
    ax.text(6.15, 8.34, "Site-017", fontsize=8.0, color="#222222")
    bc.mark(fig, "BENCHMARK - synthetic (naive scatter labels)")
    return fig


def build_after():
    from annotation_layout import place_labels  # noqa: PLC0415

    fig, ax, x, y = _base_fig()
    bc.mark(fig, "BENCHMARK - synthetic (engine scatter labels)")  # mark FIRST: it is an obstacle
    order = np.argsort(y)[-5:]  # top-5 points get labels
    place_labels(
        fig,
        ax,
        [{"text": f"Site-{46 + i:03d}", "xy": (float(x[j]), float(y[j]))} for i, j in enumerate(order)],
        fontsize=8.0,
    )
    return fig
