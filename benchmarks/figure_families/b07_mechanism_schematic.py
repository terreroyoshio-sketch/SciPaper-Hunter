"""b07: mechanism schematic - geometric composition of a water-balance process (synthetic)."""

from __future__ import annotations

import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyArrowPatch, Rectangle

import bench_common as bc


def _arrow(ax, p1, p2, color, style="-|>", lw=1.1, ls="-"):
    ax.add_patch(FancyArrowPatch(p1, p2, arrowstyle=style, mutation_scale=8, linewidth=lw, color=color, linestyle=ls, shrinkA=0, shrinkB=0, zorder=4))  # noqa: E501


def build():
    bc.apply_house_style()
    W, H = 130.0, 85.0
    fig, ax = plt.subplots(figsize=bc.mm(W, H))
    fig.subplots_adjust(left=0.01, right=0.99, top=0.99, bottom=0.03)
    ax.set_xlim(0, W)
    ax.set_ylim(0, H)
    ax.set_aspect("equal")
    ax.axis("off")

    # regions
    ax.add_patch(Rectangle((0, 45), W, 40, facecolor="#EAF2FA", edgecolor="none", zorder=0))
    ax.add_patch(Rectangle((0, 0), W, 45, facecolor="#F3EAD8", edgecolor="none", zorder=0))
    ax.plot([0, W], [45, 45], color="#8B7355", lw=1.0, zorder=2)
    ax.plot([0, W], [20, 20], color="#5B8CB8", lw=0.8, ls=(0, (4, 3)), zorder=2)

    # objects
    ax.add_patch(Rectangle((28, 44), 4, 9, facecolor="#9C7A4D", edgecolor="none", zorder=2))
    ax.add_patch(Circle((30, 58), 8.5, facecolor="#8FBC77", edgecolor="#5E8A4C", lw=0.8, zorder=3))
    ax.add_patch(Circle((86, 73), 5.5, facecolor="#F4D03F", edgecolor="#C9A715", lw=0.8, zorder=3))

    # process arrows
    for x in (62, 69, 76):
        _arrow(ax, (x, 74.5), (x, 59), "#4A78B0", lw=0.9, ls=(0, (3, 2)))
    _arrow(ax, (30, 67), (30, 76), "#3B7A57")
    _arrow(ax, (62, 56), (62, 47), "#4A78B0")
    _arrow(ax, (62, 44), (62, 26), "#8B7355", ls=(0, (3, 2)))
    _arrow(ax, (44, 46.5), (92, 46.5), "#2F6FB2")
    _arrow(ax, (92, 44.5), (104, 27), "#2F6FB2", ls=(0, (3, 2)))

    # labels
    ax.text(62, 77, "Precipitation", fontsize=8.0, ha="center", color="#222222")
    ax.text(33, 71, "Evapotranspiration", fontsize=8.0, ha="left", color="#222222")
    ax.text(64, 52, "Runoff", fontsize=8.0, ha="left", color="#222222")
    ax.text(64, 34, "Infiltration", fontsize=8.0, ha="left", color="#222222")
    ax.text(6, 31, "Root zone", fontsize=8.0, color="#6E6E6E")
    ax.text(6, 9, "Groundwater", fontsize=8.0, color="#6E6E6E")
    ax.text(86, 64.5, "Energy", fontsize=8.0, ha="center", color="#6E6E6E")
    ax.text(6, 5, "Schematic process diagram (synthetic example)", fontsize=8.0, color="#7A7A7A", style="italic")

    bc.mark(fig)
    return fig
