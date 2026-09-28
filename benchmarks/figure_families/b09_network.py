"""b09: network topology - three communities with degree-coded nodes (networkx, synthetic)."""

from __future__ import annotations

import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
from matplotlib.collections import LineCollection
from matplotlib.lines import Line2D

import bench_common as bc

COMMUNITY_COLORS = ["#2F6FB2", "#C55A11", "#3B7A57"]


def build():
    bc.apply_house_style()
    rng = np.random.default_rng(109)
    G = nx.Graph()
    communities = {}
    for c in range(3):
        members = [f"C{c + 1}-{i + 1:02d}" for i in range(15)]
        communities[c] = members
        G.add_nodes_from(members)
        for i, u in enumerate(members):
            for v in members[i + 1 :]:
                if rng.random() < 0.18:
                    G.add_edge(u, v)
    for _ in range(12):
        a, b = rng.integers(0, 3, 2)
        if a != b:
            G.add_edge(rng.choice(communities[int(a)]), rng.choice(communities[int(b)]))

    pos = nx.kamada_kawai_layout(G)  # deterministic; compacts outlier-stretched layouts
    degrees = dict(G.degree)

    fig, ax = plt.subplots(figsize=bc.mm(122, 96))
    fig.subplots_adjust(left=0.02, right=0.98, top=0.97, bottom=0.06)
    ax.set_aspect("equal")
    ax.axis("off")

    segs = [[pos[u], pos[v]] for u, v in G.edges()]
    ax.add_collection(LineCollection(segs, colors="#9A9A9A", linewidths=0.45, alpha=0.55, zorder=1))

    for c in range(3):
        members = communities[c]
        xs = [pos[m][0] for m in members]
        ys = [pos[m][1] for m in members]
        sizes = [10 + 7 * degrees[m] for m in members]
        ax.scatter(xs, ys, s=sizes, color=COMMUNITY_COLORS[c], edgecolors="#FFFFFF", linewidths=0.5, zorder=3)

    from annotation_layout import place_labels  # noqa: PLC0415  (candidate-position engine)

    label_names = sorted(degrees, key=lambda k: degrees[k], reverse=True)[:5]
    place_labels(fig, ax, [{"text": n, "xy": pos[n]} for n in label_names], fontsize=8.0, halo=True)

    handles = [Line2D([], [], marker="o", ls="", color=COMMUNITY_COLORS[c], label=f"Community {['I', 'II', 'III'][c]}") for c in range(3)]
    ax.legend(handles=handles, fontsize=8.0, loc="lower left", frameon=False)

    bc.mark(fig)
    return fig
