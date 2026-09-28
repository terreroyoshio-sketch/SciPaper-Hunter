"""T01: typography sheet - hierarchy + bilingual + math + glyph coverage (synthetic).

Validates: scientific-typography tokens apply cleanly (no fallback / no missing
glyphs on the CLEAN sheet) and the gate passes at the SCI 8 pt floor.
The deliberate gap probe is covered by typography.smoke_test() (see runner).
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

import bench_common as bc  # noqa: F401  (path setup)
from typography import SIZES  # noqa: E402


def build():
    bc.apply_house_style()
    fig = plt.figure(figsize=bc.mm(150, 78))
    ax = fig.add_axes((0.03, 0.03, 0.94, 0.86))
    ax.axis("off")

    y = 0.92
    rows = [
        ("Panel label level", "a", SIZES["panel_label"], "bold"),
        ("Axis label level", "Response (mm)", SIZES["axis_label"], "normal"),
        ("Tick/legend level", "0 1 2 3  Legend", SIZES["tick"], "normal"),
        ("Annotation level", "Sampling window (12 h)", SIZES["annotation"], "normal"),
        ("Latin + digits", "AaZz 0.0123 -1.5 25 °C", SIZES["annotation"], "normal"),
        ("CJK bilingual", "中文样板：气温 25 °C，误差 ±0.2", SIZES["annotation"], "normal"),
        ("Greek/symbols", "α β γ Δ ∑ μ ± × ÷ ≤ ≥", SIZES["annotation"], "normal"),
        ("Math via mathtext", r"$r^{2}=0.93,\ 10^{-3},\ \sum_i x_i \leq \mu+\sigma$", SIZES["annotation"], "normal"),
    ]
    for label, sample, fs, weight in rows:
        ax.text(0.0, y, f"{label}:", transform=ax.transAxes, fontsize=SIZES["annotation"], color="#777777")
        ax.text(0.30, y, sample, transform=ax.transAxes, fontsize=fs, fontweight=weight, color="#222222")
        y -= 0.115

    bc.mark(fig, "BENCHMARK - synthetic typography sheet")
    return fig
