"""Candidate-position label placement with leader lines (2026-09-28).

Lightweight deterministic placer for LOCAL labels (scatter / point / curve
labels). adjustText is NOT installed in this environment; this module covers
its auxiliary role for simple cases ONLY. Complex flowcharts / mechanism
figures / formula layouts must keep explicit placement decisions - the engine
is a fallback scorer, not a final decider.

Candidate set: center + 8 compass directions x 3 radii (offset points).
Cost: overlap penalties (text/line/scatter/rect obstacles) + canvas/axes
boundary penalties + distance + leader usage. Greedy placement in input order;
each placed label becomes an obstacle for later ones.
"""

from __future__ import annotations

import collision_engine as ce
import figure_qa as fq

DIRS = {
    "E": (1.0, 0.0),
    "NE": (0.71, 0.71),
    "N": (0.0, 1.0),
    "NW": (-0.71, 0.71),
    "W": (-1.0, 0.0),
    "SW": (-0.71, -0.71),
    "S": (0.0, -1.0),
    "SE": (0.71, -0.71),
}


def measure_text(fig, s: str, fontsize: float = 8.0):
    fig.canvas.draw()
    t = fig.text(0.0, -10.0, s, fontsize=fontsize)
    bb = t.get_window_extent()
    t.remove()
    return float(bb.width), float(bb.height)


def collect_obstacles(fig, pad_px: float = 2.0):
    from matplotlib.collections import LineCollection, PatchCollection, PathCollection, PolyCollection
    from matplotlib.image import AxesImage
    from matplotlib.lines import Line2D
    from matplotlib.patches import FancyArrowPatch, FancyBboxPatch, Polygon, Rectangle

    rects, segs, pts = [], [], []
    texts, _ = fq._collect_texts(fig)
    for _s, bb in texts:
        rects.append(ce._rect(bb.x0 - pad_px, bb.y0 - pad_px, bb.x1 + pad_px, bb.y1 + pad_px))
    for ax in fig.get_axes():
        if getattr(ax, "name", "") == "3d":
            continue
        for art in ax.get_children():
            if isinstance(art, (Line2D, LineCollection, FancyArrowPatch)):
                pl = ce._polylines(art, ax)
                if pl:
                    segs.extend(zip(pl, pl[1:]))
            elif isinstance(art, PathCollection):
                p, _k = fq._artist_points(art, ax)
                if p is not None and len(p):
                    pts.extend((float(x), float(y)) for x, y in p)
            elif isinstance(art, AxesImage):
                try:
                    bb = art.get_window_extent()
                    rects.append(ce._rect(bb.x0, bb.y0, bb.x1, bb.y1))
                except Exception:
                    pass
            elif isinstance(art, (FancyBboxPatch, Rectangle, Polygon, PatchCollection, PolyCollection)):
                if art is getattr(ax, "patch", None) or art is getattr(ax, "background_patch", None):
                    continue
                ax_area = ax.bbox.width * ax.bbox.height
                for prect in ce._rects_of(art, ax):
                    prect_area = (prect[2] - prect[0]) * (prect[3] - prect[1])
                    if ax_area > 0 and prect_area >= 0.85 * ax_area:
                        continue  # background zone
                    rects.append(prect)
    return rects, segs, pts


def _score(rect, static_rects, placed_rects, segs, pts, figbb, axbb, off_norm):
    cost = 0.0
    for r in static_rects:
        if ce._inter_area(rect, r) > 2.0:
            cost += 12.0
    for r in placed_rects:
        if ce._inter_area(rect, r) > 2.0:
            cost += 24.0  # label-label overlap is worse than label-object
    for p1, p2 in segs:
        if ce._seg_hits_rect(p1, p2, rect):
            cost += 10.0
    rx0, ry0, rx1, ry1 = rect
    for px, py in pts:
        if rx0 <= px <= rx1 and ry0 <= py <= ry1:
            cost += 14.0
    fx0, fy0, fx1, fy1 = figbb
    if rect[0] < fx0 + 2 or rect[1] < fy0 + 2 or rect[2] > fx1 - 2 or rect[3] > fy1 - 2:
        cost += 25.0
    ax0, ay0, ax1, ay1 = axbb
    if not (ax0 <= rect[0] and rect[2] <= ax1 and ay0 <= rect[1] and rect[3] <= ay1):
        cost += 6.0
    cost += 3.0 * off_norm
    return cost


def place_labels(fig, ax, items, fontsize: float = 8.0, pad_px: float = 2.0, radii_pt=(6.0, 12.0, 20.0, 30.0, 42.0, 58.0), leader_threshold_pt: float = 7.0, halo: bool = False):
    """items: [{"text": str, "xy": (data_x, data_y)}]. Greedy by input order.

    halo=True adds a subtle white stroke (sanctioned protected overlay for dense
    networks); the collision engine exempts haloed labels from scene checks.
    Returns placement records; the labels are DRAWN on the figure.
    """
    rects, segs, pts = collect_obstacles(fig, pad_px)
    figbb = (0.0, 0.0, float(fig.dpi * fig.get_size_inches()[0]), float(fig.dpi * fig.get_size_inches()[1]))
    axbb = (ax.bbox.x0, ax.bbox.y0, ax.bbox.x1, ax.bbox.y1)
    px_per_pt = fig.dpi / 72.0
    placed_rects: list = []
    results = []

    for it in items:
        s = it["text"]
        tx, ty = ax.transData.transform(it["xy"])
        w, h = measure_text(fig, s, fontsize)
        candidates = [(0.0, 0.0, "C")]
        for r in radii_pt:
            for name, (vx, vy) in DIRS.items():
                candidates.append((vx * r, vy * r, f"{name}@{r:g}"))

        best = None
        own_clear = h / 2.0 + pad_px + 3.0  # keep the label clear of its OWN anchor marker
        for dx_pt, dy_pt, dname in candidates:
            cx = tx + dx_pt * px_per_pt
            cy = ty + dy_pt * px_per_pt
            rect = ce._rect(cx - w / 2 - pad_px, cy - h / 2 - pad_px, cx + w / 2 + pad_px, cy + h / 2 + pad_px)
            off_norm = min(1.0, ((dx_pt**2 + dy_pt**2) ** 0.5) / (max(radii_pt) if radii_pt else 1.0))
            cost = _score(rect, rects, placed_rects, segs, pts, figbb, axbb, off_norm)
            dist = ((cx - tx) ** 2 + (cy - ty) ** 2) ** 0.5
            if dist < own_clear:
                cost += 15.0
            if best is None or cost < best[0]:
                best = (cost, dx_pt, dy_pt, dname, rect)

        cost, dx_pt, dy_pt, dname, rect = best
        use_leader = ((dx_pt**2 + dy_pt**2) ** 0.5) > leader_threshold_pt
        effects = None
        if halo:
            import matplotlib.patheffects as pe

            effects = [pe.withStroke(linewidth=2.2, foreground="white")]
        ax.annotate(
            s,
            xy=it["xy"],
            xytext=(dx_pt, dy_pt),
            textcoords="offset points",
            fontsize=fontsize,
            ha="center",
            va="center",
            color="#222222",
            zorder=8,
            path_effects=effects,
            arrowprops=dict(arrowstyle="-", lw=0.5, color="#777777", shrinkA=1.0, shrinkB=2.0) if use_leader else None,
        )
        placed_rects.append(rect)
        results.append({"text": s, "dir": dname, "offset_pt": (round(dx_pt, 1), round(dy_pt, 1)), "leader": use_leader, "cost": round(cost, 2)})
    return results
