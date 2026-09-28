"""b04: scientific method framework - 3 semantic layers (synthetic, trd_kit)."""

from __future__ import annotations

import numpy as np

import bench_common as bc  # noqa: F401  (sets sys.path for trd_kit)
import trd_kit as tk


def build():
    W, H = 170.0, 108.0
    c = tk.Canvas(W, H)
    band_x, band_w, band_h = 4.0, 162.0, 27.5
    tops = [7.0, 39.0, 71.0]

    # Layer 1 — Data
    c.band(band_x, tops[0], band_w, band_h, "1", "Data")
    c.box(12, tops[0] + 10.5, 30, 12, "Meteorological\nSeries", "input", id="d1")
    c.box(50, tops[0] + 10.5, 30, 12, "Auxiliary\nData", "input", id="d2")
    c.box(88, tops[0] + 10.5, 30, 12, "Quality\nControl", "process", id="d3")
    c.arrow(42.9, tops[0] + 16.5, 49.1, tops[0] + 16.5, id="d12")
    c.arrow(80.9, tops[0] + 16.5, 87.1, tops[0] + 16.5, id="d23")

    # Layer 2 — Method (with formula)
    c.band(band_x, tops[1], band_w, band_h, "2", "Method")
    c.box(10, tops[1] + 10.5, 26, 12, "Preprocessing", "process", id="m1")
    c.box(41, tops[1] + 10.5, 26, 12, "Model\nEstimation", "process", id="m2")
    c.box(72, tops[1] + 10.5, 26, 12, "Uncertainty\nPropagation", "process", id="m3")
    c.arrow(36.9, tops[1] + 16.5, 40.1, tops[1] + 16.5, id="m12")
    c.arrow(67.9, tops[1] + 16.5, 71.1, tops[1] + 16.5, id="m23")
    c.box(108, tops[1] + 10.5, 52, 12, r"$y = f(X, \theta) + \varepsilon$", "accent", fontsize=8.0, id="formula")

    # Layer 3 — Result (with embedded mini plot)
    c.band(band_x, tops[2], band_w, band_h, "3", "Result")
    c.box(12, tops[2] + 10.5, 30, 12, "Composite\nIndex", "result", id="r1")
    c.box(50, tops[2] + 10.5, 30, 12, "Event\nMetrics", "result", id="r2")
    rng = np.random.default_rng(104)
    t = np.arange(80)
    s = 1.0 * np.sin(t / 7.0) + rng.normal(0, 0.18, 80)
    axp = c.plot_slot(108, tops[2] + 7.0, 52, 16.5, id="r-plot")
    axp.plot(t, s, lw=0.8, color="#7030A0")
    axp.axhline(0.55, lw=0.7, color="#C00000", ls="--")
    axp.set_xlim(0, 79)
    axp.set_ylim(-1.5, 1.6)
    axp.set_xticks([])
    axp.set_yticks([])

    for i in range(2):
        c.block_arrow_down(85, tops[i] + band_h + 0.6, tops[i + 1] - 0.6, id=f"gap{i}")

    c.legend(4.0, 103.5, [("input", "Data"), ("process", "Method"), ("result", "Result"), ("accent", "Formula")])
    bc.mark(c.fig)
    return c.fig
