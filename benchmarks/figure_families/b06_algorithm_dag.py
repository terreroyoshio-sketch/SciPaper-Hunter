"""b06: algorithm flowchart - Graphviz computes layout, matplotlib renders (synthetic)."""

from __future__ import annotations

import shutil
import subprocess

import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch, Polygon

import bench_common as bc
import trd_kit as tk

DOT = """digraph G {
  graph [rankdir=TB, splines=polyline, nodesep=0.45, ranksep=0.55];
  node [shape=box, fontsize=9, margin="0.16,0.09"];
  A [label="Load raw data"];
  B [label="Clean & normalize"];
  C [label="Split train / test"];
  D [label="Train model"];
  E [label="Evaluate metrics"];
  F [shape=diamond, label="Converged?", margin="0.02,0.02"];
  G [label="Tune hyperparameters"];
  H [label="Export results"];
  A -> B -> C -> D -> E -> F;
  F -> H [label="yes"];
  F -> G [label="no"];
  G -> D;
}
"""

FAMILY_OF = {"A": "input", "B": "process", "C": "process", "D": "process", "E": "method", "F": "accent", "G": "method", "H": "result"}
FEEDBACK_EDGES = {("G", "D")}  # loop edges render dashed (回流虚线语义)


def dot_positions(dot_src: str):
    dot_bin = shutil.which("dot") or r"D:\Graphviz\bin\dot.exe"
    proc = subprocess.run([dot_bin, "-Tplain"], input=dot_src, capture_output=True, text=True, encoding="utf-8", check=True)
    nodes, edges, gsize = {}, [], (6.0, 8.0)
    for line in proc.stdout.splitlines():
        parts = line.split()
        if not parts:
            continue
        if parts[0] == "graph" and len(parts) >= 4:
            gsize = (float(parts[2]), float(parts[3]))
        elif parts[0] == "node" and len(parts) >= 6:
            nodes[parts[1]] = (float(parts[2]), float(parts[3]), float(parts[4]), float(parts[5]))
        elif parts[0] == "edge" and len(parts) >= 6:
            tail, head, n = parts[1], parts[2], int(parts[3])
            pts = [(float(parts[4 + 2 * i]), float(parts[5 + 2 * i])) for i in range(n)]
            label = None
            if len(parts) >= 4 + 2 * n + 3:
                label = (parts[4 + 2 * n], float(parts[5 + 2 * n]), float(parts[6 + 2 * n]))
            edges.append({"tail": tail, "head": head, "pts": pts, "label": label})
    return nodes, edges, gsize


def build():
    bc.apply_house_style()
    nodes, edges, (gw, gh) = dot_positions(DOT)
    fig, ax = plt.subplots(figsize=(gw + 1.2, gh + 0.9))
    fig.subplots_adjust(left=0.02, right=0.98, top=0.97, bottom=0.05)
    ax.set_xlim(-0.6, gw + 0.6)
    ax.set_ylim(-0.45, gh + 0.45)
    ax.set_aspect("equal")
    ax.axis("off")

    for e in edges:
        pts = e["pts"]
        is_feedback = (e["tail"], e["head"]) in FEEDBACK_EDGES
        style = (0, (3, 2)) if is_feedback else "-"
        color = "#666666" if is_feedback else "#555555"
        if len(pts) >= 2:
            xs = [p[0] for p in pts]
            ys = [p[1] for p in pts]
            ax.plot(xs[:-1], ys[:-1], lw=0.9, color=color, linestyle=style, zorder=1)
            ax.add_patch(FancyArrowPatch(pts[-2], pts[-1], arrowstyle="-|>", mutation_scale=7, linewidth=0.9, color=color, linestyle=style, zorder=2, shrinkA=0, shrinkB=0))
        if e["label"]:
            txt, lx, ly = e["label"]
            ax.text(lx, ly, txt, fontsize=8.0, color="#555555", ha="center", va="center", zorder=3)

    for name, (x, y, w, h) in nodes.items():
        fam = tk.FAMILIES[FAMILY_OF[name]]
        if name == "F":
            ax.add_patch(Polygon([(x, y + h / 2), (x + w / 2, y), (x, y - h / 2), (x - w / 2, y)], closed=True, facecolor=fam["fill"], edgecolor=fam["edge"], linewidth=0.8, zorder=4))
        else:
            ax.add_patch(FancyBboxPatch((x - w / 2, y - h / 2), w, h, boxstyle="round,pad=0,rounding_size=0.06", linewidth=0.8, edgecolor=fam["edge"], facecolor=fam["fill"], zorder=4))

    labels = {"A": "Load raw data", "B": "Clean & normalize", "C": "Split train / test", "D": "Train model", "E": "Evaluate metrics", "F": "Converged?", "G": "Tune hyperparameters", "H": "Export results"}
    for name, (x, y, w, h) in nodes.items():
        ax.text(x, y, labels[name], fontsize=8.0, ha="center", va="center", color="#222222", zorder=5)

    bc.mark(fig)
    return fig
