"""T04: roadmap conflict benchmark - BEFORE must FAIL (text-arrow + text-text;
text-image recorded), AFTER (layout fixed) must PASS.

Deliberately engineered conflicts (synthetic): an arrow drawn THROUGH a label,
two labels overlapping each other, and a label crossing the edge of an image
inset.
"""

from __future__ import annotations

import sys
from pathlib import Path

_FAM = Path(__file__).resolve().parents[1] / "figure_families"
if str(_FAM) not in sys.path:
    sys.path.insert(0, str(_FAM))

import numpy as np

import bench_common as bc  # noqa: F401  (path setup for trd_kit)
import trd_kit as tk


def _scene(with_conflicts: bool):
    c = tk.Canvas(150.0, 80.0)
    c.box(10, 22, 28, 12, "Stage A", "input", id="a")
    c.box(112, 22, 28, 12, "Stage B", "result", id="b")
    c.arrow(38.5, 28, 111.5, 28, id="ab")

    ax_img = c.plot_slot(20, 48, 40, 24, id="img")
    rng = np.random.default_rng(404)
    ax_img.imshow(rng.normal(0, 1, (40, 60)), cmap="viridis", aspect="auto")
    ax_img.set_xticks([])
    ax_img.set_yticks([])

    if with_conflicts:
        # 1) text-arrow: label ON the arrow
        c.text(70, 27.2, "Transition pathway", fontsize=8.0, color="#222222", id="lbl1")
        # 2) text-text: two labels overlapping
        c.text(70.5, 26.4, "Pathway note", fontsize=8.0, color="#222222", id="lbl2")
        # 3) text-image boundary: label crossing the inset's right edge (20..60)
        c.text(58, 58, "Image zone label", fontsize=8.0, color="#222222", id="lbl3")
    else:
        # layout fixed: single label clear of the arrow, image label fully outside the inset
        c.text(75, 33.8, "Transition pathway", fontsize=8.0, color="#222222", id="lbl1")
        c.text(62.5, 58, "Image zone label", fontsize=8.0, color="#222222", id="lbl3")

    bc.mark(c.fig)
    return c.fig


def build_before():
    return _scene(with_conflicts=True)


def build_after():
    return _scene(with_conflicts=False)
