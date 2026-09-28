"""b12: 3D scientific figure - surface + scatter via mplot3d FALLBACK path (synthetic).

The primary 3D path (PyVista off-screen rendering) is exercised by b14;
this bench validates the declared matplotlib-mplot3d fallback.
"""

from __future__ import annotations

import matplotlib.pyplot as plt
import numpy as np

import bench_common as bc


def build():
    bc.apply_house_style()
    rng = np.random.default_rng(112)
    fig = plt.figure(figsize=bc.mm(112, 90))
    ax = fig.add_subplot(projection="3d")

    x = np.linspace(-6, 6, 110)
    X, Y = np.meshgrid(x, x)
    R = np.sqrt(X**2 + Y**2) + 1e-9
    Z = np.sin(R) / R
    surf = ax.plot_surface(X, Y, Z, cmap="viridis", linewidth=0, antialiased=True, alpha=0.95, rcount=110, ccount=110)

    sxp = rng.uniform(-5, 5, 40)
    syp = rng.uniform(-5, 5, 40)
    srp = np.sqrt(sxp**2 + syp**2) + 1e-9
    szp = np.sin(srp) / srp + 0.25 + rng.normal(0, 0.05, 40)
    ax.scatter(sxp, syp, szp, s=6, color="#C55A11", depthshade=False, zorder=5)

    ax.set_xlabel("x (m)", fontsize=8)
    ax.set_ylabel("y (m)", fontsize=8)
    # z 轴标签省略：z 量已由 colorbar "Elevation (m)" 表达（mplot3d 的 zlabel 会与刻度/色条互相挤压）
    ax.tick_params(labelsize=8.0)
    ax.view_init(elev=26, azim=-58)
    cbar = fig.colorbar(surf, ax=ax, shrink=0.6, pad=0.12)
    cbar.set_label("Elevation (m)", fontsize=8)
    cbar.ax.tick_params(labelsize=8.0)

    ax.text2D(0.0, 1.02, "a", transform=ax.transAxes, fontsize=9, fontweight="bold")
    bc.mark(fig, "BENCHMARK - synthetic data | 3D fallback path: mplot3d")
    return fig
