"""Shared helpers for figure-family benchmarks.

All benchmark figures use SYNTHETIC data with fixed seeds and carry a visible
"BENCHMARK - synthetic data" marker. They must never be presented as real
research results.
"""

from __future__ import annotations

import sys
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

BENCH_DIR = Path(__file__).resolve().parent
WORKTREE = BENCH_DIR.parents[1]
GATE_SCRIPTS = WORKTREE / ".claude" / "skills" / "figure-quality-gate" / "scripts"
TRD_SCRIPTS = WORKTREE / ".claude" / "skills" / "technical-route-diagram" / "scripts"
TYP_SCRIPTS = WORKTREE / ".claude" / "skills" / "scientific-typography" / "scripts"
CE_SCRIPTS = WORKTREE / ".claude" / "skills" / "collision-aware-layout" / "scripts"
for _p in (GATE_SCRIPTS, TRD_SCRIPTS, TYP_SCRIPTS, CE_SCRIPTS, BENCH_DIR):
    _sp = str(_p)
    if _sp not in sys.path:
        sys.path.insert(0, _sp)

from figure_qa import DEFAULT_MIN_PT, run_gate  # noqa: E402
from typography import SIZES, apply_typography  # noqa: E402

FONT_STACK = ["Microsoft YaHei", "SimHei", "Arial", "DejaVu Sans"]

PALETTE = {
    "blue": "#2F6FB2",
    "orange": "#C55A11",
    "green": "#3B7A57",
    "red": "#8C2D2D",
    "gray": "#555555",
    "ink": "#222222",
}


def apply_house_style() -> None:
    """Fonts/sizes/math come from the scientific-typography tokens (single source)."""
    apply_typography("sci-sans")


def mark(fig, text: str = "BENCHMARK - synthetic data (not real research)") -> None:
    """Bottom-right-fixed marker; adaptive so the text keeps a 2 mm canvas margin."""
    w_in, h_in = fig.get_size_inches()
    x = 1.0 - (2.0 / 25.4) / float(w_in)
    y = 1.0 - (2.0 / 25.4) / float(h_in)
    fig.text(x, y, text, fontsize=8.0, color="#7A7A7A", style="italic", ha="right", va="top")


def panel_label(ax, letter: str, x: float = 0.0, y: float = 1.02) -> None:
    ax.text(x, y, letter, transform=ax.transAxes, fontsize=9, fontweight="bold", va="bottom", ha="left")


def mm(x: float, y: float):
    return (x / 25.4, y / 25.4)
