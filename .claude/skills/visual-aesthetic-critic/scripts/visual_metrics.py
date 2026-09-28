"""Deterministic visual metrics to SUPPORT aesthetic review (2026-09-28).

These numbers do NOT judge beauty; they flag review targets (density, balance,
color count, saturation, whitespace). The aesthetic verdict stays human/critic
(three-valued, with concrete locations - never "looks nice").
"""

from __future__ import annotations

import json
from pathlib import Path

import numpy as np


def metrics(png_path) -> dict:
    from PIL import Image

    with Image.open(png_path) as im:
        g = np.asarray(im.convert("L"), dtype=float)
        rgb = np.asarray(im.convert("RGB"), dtype=float)
    h, w = g.shape
    ink = g < 250.0  # non-white
    density = float(ink.mean())

    qh, qw = h // 2, w // 2
    quads = {
        "TL": float(ink[:qh, :qw].mean()),
        "TR": float(ink[:qh, qw:].mean()),
        "BL": float(ink[qh:, :qw].mean()),
        "BR": float(ink[qh:, qw:].mean()),
    }
    qvals = np.array(list(quads.values()))
    imbalance = float(qvals.max() - qvals.min()) / max(1e-9, float(qvals.max()))

    # whitespace margins (rows/cols fully white at the border)
    def border_run(mask_1d):
        n = 0
        for v in mask_1d:
            if v:
                n += 1
            else:
                break
        return n

    top = border_run(~ink.any(axis=1))
    bottom = border_run(~ink.any(axis=1)[::-1])
    left = border_run(~ink.any(axis=0))
    right = border_run(~ink.any(axis=0)[::-1])

    # quantized color count + saturation
    q = (rgb // 32).astype(np.int16)
    colors = np.unique(q.reshape(-1, 3), axis=0)
    mx = rgb.max(axis=2)
    mn = rgb.min(axis=2)
    sat = np.where(mx > 0, (mx - mn) / np.maximum(1.0, mx), 0.0)
    colorful = (mx - mn) > 24
    mean_sat_colored = float(sat[colorful].mean()) if colorful.any() else 0.0

    return {
        "file": str(Path(png_path).name),
        "size_px": [w, h],
        "density": round(density, 4),
        "quadrants": {k: round(v, 4) for k, v in quads.items()},
        "quadrant_imbalance": round(imbalance, 3),
        "whitespace_px": {"top": top, "bottom": bottom, "left": left, "right": right},
        "quantized_colors": int(len(colors)),
        "mean_saturation_colored_frac": round(float(colorful.mean()), 4),
        "mean_saturation_of_colored": round(mean_sat_colored, 3),
    }


def main() -> None:
    import sys

    paths = sys.argv[1:]
    out = Path("metrics_out")
    out.mkdir(exist_ok=True)
    allm = {}
    for p in paths:
        m = metrics(p)
        allm[Path(p).stem] = m
        print(json.dumps(m, ensure_ascii=False))
    (out / "visual_metrics.json").write_text(json.dumps(allm, ensure_ascii=False, indent=2), encoding="utf-8")


if __name__ == "__main__":
    main()
