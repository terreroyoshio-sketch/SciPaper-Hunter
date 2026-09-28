"""T02: curve labels - BEFORE (naive overlapping) must FAIL, AFTER (engine) must PASS.

Synthetic two-curve plot; the BEFORE state deliberately places labels on the
curves and on top of each other. The AFTER state uses the candidate-position
engine (collision-aware-layout).
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


def _curves():
    t = np.linspace(0, 10, 220)
    a = 5 + 1.6 * np.sin(t * 1.1) + 0.05 * t
    b = 5 + 1.4 * np.cos(t * 1.1 + 0.6)
    return t, a, b


def _base_fig():
    bc.apply_house_style()
    t, a, b = _curves()
    fig, ax = plt.subplots(figsize=bc.mm(120, 70))
    fig.subplots_adjust(left=0.11, right=0.975, top=0.90, bottom=0.22)
    ax.plot(t, a, lw=1.0, color=bc.PALETTE["blue"])
    ax.plot(t, b, lw=1.0, color=bc.PALETTE["orange"], ls="--")
    ax.set_xlabel("Time (h)")
    ax.set_ylabel("Response (mm)")
    return fig, ax, t, a, b


def build_before():
    fig, ax, t, a, b = _base_fig()
    # deliberate: labels sit ON the curves and overlap each other
    ax.text(4.6, float(np.interp(4.6, t, a)), "Cyclic A", fontsize=8.0, color="#222222")
    ax.text(4.9, float(np.interp(4.9, t, b)) + 0.06, "Cyclic B", fontsize=8.0, color="#222222")
    bc.mark(fig, "BENCHMARK - synthetic (naive label placement)")
    return fig


def build_after():
    from annotation_layout import place_labels  # noqa: PLC0415

    fig, ax, t, a, b = _base_fig()
    bc.mark(fig, "BENCHMARK - synthetic (engine label placement)")  # mark FIRST: it is an obstacle
    place_labels(
        fig,
        ax,
        [
            {"text": "Cyclic A", "xy": (4.6, float(np.interp(4.6, t, a)))},
            {"text": "Cyclic B", "xy": (4.9, float(np.interp(4.9, t, b)))},
        ],
        fontsize=8.0,
    )
    return fig
