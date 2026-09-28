"""b14: 3D PRIMARY path - PyVista off-screen render composed onto a matplotlib canvas (synthetic).

Runtime-verified API notes (pyvista 0.49.0, introspected at 2026-09-28):
- Plotter.screenshot(...) signature includes a `scale` parameter;
- Plotter.image_scale is a plotter-level PROPERTY (not a callable);
- Plotter.save_graphic() exists for vector export (not used here: the composite
  keeps the render as a raster inset inside a vector PDF).
"""

from __future__ import annotations

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.cm import ScalarMappable
from matplotlib.colors import Normalize

import bench_common as bc


def build():
    bc.apply_house_style()
    import pyvista as pv

    x = np.linspace(-3, 3, 140)
    X, Y = np.meshgrid(x, x)
    Z = 2.1 * np.exp(-(X**2 + Y**2) / 2.4) + 0.35 * np.sin(2.4 * X) * np.cos(2.0 * Y)
    grid = pv.StructuredGrid(X, Y, Z)
    grid["Elevation"] = Z.ravel(order="F")

    rng = np.random.default_rng(314)
    idx = rng.choice(grid.n_points, 40, replace=False)
    pts = grid.points[idx]

    pl = pv.Plotter(off_screen=True, window_size=(1200, 840))
    pl.background_color = "white"
    pl.add_mesh(grid, cmap="viridis", show_scalar_bar=False, smooth_shading=True)
    pl.add_points(pts, color="#C55A11", point_size=8, render_points_as_spheres=True)
    pl.camera_position = [(6.2, -5.6, 4.6), (0.0, 0.0, 0.6), (0.0, 0.0, 1.0)]
    img = pl.screenshot(return_img=True, scale=2)
    pl.close()

    fig = plt.figure(figsize=bc.mm(150, 100))
    ax = fig.add_axes((0.015, 0.03, 0.72, 0.94))
    ax.imshow(img)
    ax.axis("off")
    ax.text(0.0, 1.005, "a", transform=ax.transAxes, fontsize=9, fontweight="bold", va="bottom")

    cax = fig.add_axes((0.765, 0.14, 0.028, 0.72))
    norm = Normalize(vmin=float(Z.min()), vmax=float(Z.max()))
    cb = fig.colorbar(ScalarMappable(norm=norm, cmap=plt.get_cmap("viridis")), cax=cax)
    cb.set_label("Elevation (m)", fontsize=8)
    cb.ax.tick_params(labelsize=8)

    bc.mark(fig, "BENCHMARK - synthetic data | 3D primary path: PyVista 0.49")
    return fig
