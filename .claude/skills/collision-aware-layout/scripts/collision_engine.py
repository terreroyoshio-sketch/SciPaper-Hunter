"""Post-render collision engine (2026-09-28).

Derives scene objects from ACTUAL renderer geometry (no string-length guessing)
and reports collisions by category:

    text_text | text_line (curve/arrow) | text_scatter | text_patch_boundary
    | text_image | legend_data

Rules
- New categories apply a 1.5 pt (2 px @100dpi) visual padding: near-misses fail.
- text_text / legend_data reuse the figure-quality-gate definitions (one standard).
- Boundary rule for patches/images: a text fully INSIDE is intentional (label on a
  region/cell); a text CROSSING the boundary is a conflict.
- 3D axes are skipped (mplot3d extents are unreliable - see gate docs).
"""

from __future__ import annotations

import numpy as np

import figure_qa as fq

PAD_PX = 2.0


def _rect(x0, y0, x1, y1):
    return (x0, y0, x1, y1)


def _inter_area(a, b):
    x = max(0.0, min(a[2], b[2]) - max(a[0], b[0]))
    y = max(0.0, min(a[3], b[3]) - max(a[1], b[1]))
    return x * y


def _contains(outer, inner, tol=2.0):
    return outer[0] - tol <= inner[0] and outer[1] - tol <= inner[1] and outer[2] + tol >= inner[2] and outer[3] + tol >= inner[3]


def _seg_hits_rect(p1, p2, r):
    """Liang-Barsky segment/rect intersection."""
    x0, y0, x1, y1 = r
    dx = p2[0] - p1[0]
    dy = p2[1] - p1[1]
    t0, t1 = 0.0, 1.0
    for p, q in ((-dx, p1[0] - x0), (dx, x1 - p1[0]), (-dy, p1[1] - y0), (dy, y1 - p1[1])):
        if p == 0:
            if q < 0:
                return False
        else:
            t = q / p
            if p < 0:
                if t > t1:
                    return False
                t0 = max(t0, t)
            else:
                if t < t0:
                    return False
                t1 = min(t1, t)
    return True


def _polylines(art, ax):
    from matplotlib.patches import FancyArrowPatch

    if isinstance(art, FancyArrowPatch):
        # get_path() returns the arrow path in the patch's own coordinate space;
        # for our kit/standalone arrows that is DATA space (verified 2026-09-28:
        # verts [38.5,52.0]->[111.1,52.0] on an mm canvas) - transform to display.
        try:
            p = art.get_path()
            V = np.asarray(p.vertices, dtype=float)
            codes = p.codes
            if codes is not None:
                # drop structural vertices that are never drawn: STOP(0) and
                # CLOSEPOLY(79). The trailing CLOSEPOLY vertex of FancyArrowPatch
                # paths is (0,0) and, once transformed, forms a phantom segment
                # sweeping the whole canvas (found 2026-09-28).
                keep = [i for i, c in enumerate(codes) if c not in (0, 79)]
                if keep:
                    V = V[keep]
            if len(V) >= 2:
                V = art.get_transform().transform(V)
                return [(float(x), float(y)) for x, y in V]
        except Exception:
            return None
        return None
    pts, _kind = fq._artist_points(art, ax, cap=400)
    if pts is None or len(pts) < 2:
        return None
    b = ax.bbox
    keep = [(float(x), float(y)) for x, y in pts if b.x0 - 2 <= x <= b.x1 + 2 and b.y0 - 2 <= y <= b.y1 + 2]
    return keep if len(keep) >= 2 else None


def _is_background_zone(art) -> bool:
    """Large light-colored CHROMATIC fills (sky/zone bands) - boundary crossing is
    visually meaningless. White containers (chroma ~0) stay checked."""
    try:
        from matplotlib import colors as mcolors

        rgba = art.get_facecolor()
        if rgba is None or len(rgba) == 0:
            return False
        r, g, b = mcolors.to_rgb(rgba)
        luminance = 0.2126 * r + 0.7152 * g + 0.0722 * b
        chroma = max(r, g, b) - min(r, g, b)
        return luminance >= 0.85 and chroma >= 0.02
    except Exception:
        return False


def _rects_of(art, ax):
    """Display-space rectangle(s) for patch-like artists.

    Collections ALWAYS use the full path-union bbox (get_window_extent on
    collections can return partial boxes - found on geopandas maps, 2026-09-28).
    """
    from matplotlib.collections import Collection

    if isinstance(art, Collection):
        try:
            verts = [p.vertices for p in art.get_paths() if p.vertices is not None and len(p.vertices)]
            if verts:
                V = ax.transData.transform(np.vstack(verts))
                return [_rect(float(V[:, 0].min()), float(V[:, 1].min()), float(V[:, 0].max()), float(V[:, 1].max()))]
        except Exception:
            pass
        return []
    try:
        bb = art.get_window_extent()
        if bb.width > 0 and bb.height > 0:
            return [_rect(bb.x0, bb.y0, bb.x1, bb.y1)]
    except Exception:
        pass
    return []


def _texts_with_halo(fig):
    """Same guards as figure_qa._collect_texts, but keeps the halo flag per text.

    White-halo labels (path effects) are intentionally protected overlays
    (sanctioned by the style rules, e.g. network node labels): they are exempt
    from line/scatter/patch/image checks; text-text stays enforced.
    """
    from matplotlib.text import Text

    r = fq._renderer(fig)
    ticks = fq._tick_index(fig)
    w, h = (v * fig.dpi for v in fig.get_size_inches())
    out = []
    for t in fig.findobj(match=Text):
        if not t.get_visible():
            continue
        s = (t.get_text() or "").strip()
        if not s:
            continue
        info = ticks.get(id(t))
        if info is not None and fq._skip_tick(info):
            continue
        bb = fq.text_bbox(t, r)
        if bb.width <= 0 or bb.height <= 0:
            continue
        if bb.x0 < -0.5 * w or bb.x1 > 1.5 * w or bb.y0 < -0.5 * h or bb.y1 > 1.5 * h:
            continue
        pe = getattr(t, "get_path_effects", None)
        halo = bool(pe and pe())
        out.append((s, bb, halo))
    return out


def check(fig, pad_px: float = PAD_PX) -> dict:
    texts = _texts_with_halo(fig)
    from matplotlib.collections import LineCollection, PatchCollection, PathCollection, PolyCollection
    from matplotlib.image import AxesImage
    from matplotlib.lines import Line2D
    from matplotlib.patches import FancyArrowPatch, FancyBboxPatch, Polygon, Rectangle

    out = {
        "text_text": fq._overlaps_from([(s, bb) for s, bb, _h in texts]),
        "text_line": [],
        "text_scatter": [],
        "text_patch_boundary": [],
        "text_image": [],
        "legend_data": fq.legend_conflicts(fig),
    }
    for ax_i, ax in enumerate(fig.get_axes()):
        if getattr(ax, "name", "") == "3d":
            continue
        children = list(ax.get_children())
        for s, bb, halo in texts:
            if halo:
                continue  # protected overlay: exempt from scene-object checks
            rt = _rect(bb.x0, bb.y0, bb.x1, bb.y1)
            rp = _rect(bb.x0 - pad_px, bb.y0 - pad_px, bb.x1 + pad_px, bb.y1 + pad_px)
            for art in children:
                if isinstance(art, (Line2D, LineCollection, FancyArrowPatch)):
                    pl = _polylines(art, ax)
                    if not pl:
                        continue
                    kind = "arrow" if isinstance(art, FancyArrowPatch) else "curve"
                    for p1, p2 in zip(pl, pl[1:]):
                        if _seg_hits_rect(p1, p2, rp):
                            out["text_line"].append({"text": s[:42], "ax": ax_i, "artist": kind})
                            break
                    continue
                if isinstance(art, PathCollection):
                    pts, _k = fq._artist_points(art, ax)
                    if pts is None or not len(pts):
                        continue
                    n = int(
                        np.count_nonzero(
                            (pts[:, 0] >= rp[0]) & (pts[:, 0] <= rp[2]) & (pts[:, 1] >= rp[1]) & (pts[:, 1] <= rp[3])
                        )
                    )
                    if n:
                        out["text_scatter"].append({"text": s[:42], "ax": ax_i, "markers": n})
                    continue
                if isinstance(art, AxesImage):
                    try:
                        ib = art.get_window_extent()
                    except Exception:
                        continue
                    irect = _rect(ib.x0, ib.y0, ib.x1, ib.y1)
                    if _inter_area(rt, irect) > 2.0 and not _contains(irect, rt):
                        out["text_image"].append({"text": s[:42], "ax": ax_i})
                    continue
                if isinstance(art, (FancyBboxPatch, Rectangle, Polygon, PatchCollection, PolyCollection)):
                    if art is getattr(ax, "patch", None) or art is getattr(ax, "background_patch", None):
                        continue  # the axes' own background patch is not an obstacle
                    try:
                        a = art.get_alpha()
                        if a is not None and a < 0.15:
                            continue
                    except Exception:
                        pass
                    ax_area = ax.bbox.width * ax.bbox.height
                    for prect in _rects_of(art, ax):
                        prect_area = (prect[2] - prect[0]) * (prect[3] - prect[1])
                        if ax_area > 0 and prect_area >= 0.85 * ax_area:
                            continue  # background zone band: boundary crossing is visually meaningless
                        if ax_area > 0 and prect_area >= 0.30 * ax_area and _is_background_zone(art):
                            continue  # large light-colored chromatic zone (e.g. sky band)
                        if _inter_area(rt, prect) > 2.0 and not _contains(prect, rt):
                            out["text_patch_boundary"].append({"text": s[:42], "ax": ax_i, "artist": type(art).__name__})
                            break

    for k in ("text_line", "text_scatter", "text_patch_boundary", "text_image"):
        seen, uniq = set(), []
        for e in out[k]:
            key = (e["text"], e["ax"], e.get("artist", ""))
            if key not in seen:
                seen.add(key)
                uniq.append(e)
        out[k] = uniq
    return out


def fail_lines(report: dict) -> list[str]:
    lines = []
    if report.get("text_line"):
        w = report["text_line"][0]
        lines.append(f"text-{w['artist']} collision x{len(report['text_line'])} (e.g. {w['text']!r})")
    if report.get("text_scatter"):
        w = report["text_scatter"][0]
        lines.append(f"text-scatter collision x{len(report['text_scatter'])} (e.g. {w['text']!r}, markers={w['markers']})")
    if report.get("text_patch_boundary"):
        w = report["text_patch_boundary"][0]
        lines.append(f"text-patch boundary crossing x{len(report['text_patch_boundary'])} (e.g. {w['text']!r})")
    return lines


def limitation_lines(report: dict) -> list[str]:
    lines = []
    if report.get("text_image"):
        w = report["text_image"][0]
        lines.append(f"text-image overlap x{len(report['text_image'])} (e.g. {w['text']!r}) - judge critical ROI manually")
    return lines


def counts(report: dict) -> dict:
    return {k: len(v) for k, v in report.items()}
