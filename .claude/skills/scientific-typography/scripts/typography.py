"""Scientific typography tokens + apply + fallback detection (2026-09-28).

Single source of truth for figure font stacks / size hierarchy / math font.
Policy: system fonts only (no downloaded font files, no personal font paths).

Matplotlib constraint (documented honestly): it selects ONE font per text
object - there is no per-glyph fallback. Therefore the applied sans stack puts
a dual-coverage font first (Latin+CJK) and per-script precision is available
via `text_style()` for text objects whose content is purely one script.
"""

from __future__ import annotations

import warnings

from matplotlib import font_manager, rcParams

# ---- font tokens -----------------------------------------------------------
FONTS = {
    "latin_serif": ["Times New Roman", "Liberation Serif", "Nimbus Roman", "DejaVu Serif"],
    "latin_sans": ["Arial", "Helvetica", "Liberation Sans", "DejaVu Sans"],
    "cjk_serif": ["SimSun", "Noto Serif CJK SC", "Source Han Serif SC"],
    "cjk_sans": ["Microsoft YaHei", "SimHei", "Noto Sans CJK SC", "Source Han Sans SC"],
}

# ---- size hierarchy tokens (pt, final print size) --------------------------
# panel label > axis label >= legend ~ tick > annotation  (SCI floor: 8 pt)
SIZES = {
    "panel_label": 9.0,
    "axis_label": 8.5,
    "legend": 8.0,
    "tick": 8.0,
    "annotation": 8.0,
    "minor_annotation": 8.0,  # floor-bound at the SCI minimum
}
MIN_PT = 8.0  # keep in sync with figure_qa.DEFAULT_MIN_PT

# bold is reserved for level-1 information only
WEIGHTS = {"level1": "bold", "body": "normal"}

# NOTE (2026-09-28 smoke-test finding): Microsoft YaHei lacks Unicode
# sub/superscript glyphs (₂ U+2082, ⁻ U+207B). RULE: sub/superscripts ALWAYS go
# through mathtext ($10^{-3}$); never literal Unicode sub/superscript characters.
PROBE_CLEAN = "AaZz 0.0123 -1.5 中文样板 μ±×÷ ≤ ≥ °C α β γ Δ ∑"
PROBE_GAP = "font-gap probe: x₂ 10⁻³"  # deliberately uncovered glyphs


def first_available(names: list[str]) -> str | None:
    for n in names:
        try:
            font_manager.findfont(font_manager.FontProperties(family=n), fallback_to_default=False)
            return n
        except Exception:
            continue
    return None


def _has_cjk(s: str) -> bool:
    return any(ord(c) > 0x2E7F for c in (s or ""))


def text_style(s: str, serif: bool = False) -> dict:
    """Explicit per-object font for strings whose script is known.

    Pure-Latin content can use the journal Latin face (e.g. Arial / Times);
    any CJK content must use a dual-CJK font (matplotlib has no per-glyph fallback).
    """
    if _has_cjk(s):
        fam = first_available(FONTS["cjk_serif"] if serif else FONTS["cjk_sans"])
    else:
        fam = first_available(FONTS["latin_serif"] if serif else FONTS["latin_sans"])
    return {"family": fam} if fam else {}


def apply_typography(profile: str = "sci-sans") -> dict:
    """Apply tokens to rcParams. Profiles:

    - sci-sans  : bilingual-safe sans (CJK dual-coverage font first) - benchmark default
    - sci-latin : Latin-first sans for Chinese-free figures (journal look)
    - sci-serif : bilingual serif (SimSun-first) for 中文论文 (宋体正文)
    - 中文论文 requires per-object text_style() for pure-Latin strings (Times).
    """
    if profile == "sci-latin":
        sans_stack = [first_available(FONTS["latin_sans"])] + FONTS["latin_sans"][1:] + [first_available(FONTS["cjk_sans"])]
    elif profile == "sci-serif":
        sans_stack = [first_available(FONTS["cjk_serif"])] + FONTS["latin_serif"] + [first_available(FONTS["cjk_sans"]), "DejaVu Sans"]
    else:  # sci-sans
        sans_stack = [first_available(FONTS["cjk_sans"])] + FONTS["latin_sans"] + FONTS["cjk_sans"][1:] + ["DejaVu Sans"]

    sans_stack = [s for s in sans_stack if s]
    latin_for_math = first_available(FONTS["latin_sans"]) or "DejaVu Sans"

    rcParams.update(
        {
            "font.family": "sans-serif",
            "font.sans-serif": sans_stack,
            "font.size": SIZES["annotation"],
            "axes.labelsize": SIZES["axis_label"],
            "xtick.labelsize": SIZES["tick"],
            "ytick.labelsize": SIZES["tick"],
            "legend.fontsize": SIZES["legend"],
            "axes.unicode_minus": False,
            "svg.fonttype": "none",
            "pdf.fonttype": 42,
            "ps.fonttype": 42,
            "axes.edgecolor": "#333333",
            "axes.linewidth": 0.8,
            # math font consistent with the body sans (custom, not Computer Modern)
            "mathtext.fontset": "custom",
            "mathtext.rm": latin_for_math,
            "mathtext.it": f"{latin_for_math}:italic",
            "mathtext.bf": f"{latin_for_math}:bold",
            "mathtext.default": "regular",
        }
    )
    return {
        "profile": profile,
        "resolved": {
            "sans_first": sans_stack[0] if sans_stack else None,
            "math": latin_for_math,
        },
        "sizes": dict(SIZES),
    }


# ---- fallback / missing-glyph detection ------------------------------------
_FONT_WARN_PATTERNS = ("findfont", "missing from font", "missing from current font", "Glyph")


def capture_font_warnings(render_callable) -> list[str]:
    """Run `render_callable` (e.g. fig.canvas.draw) capturing font-related warnings."""
    with warnings.catch_warnings(record=True) as rec:
        warnings.simplefilter("always")
        render_callable()
    msgs = [str(w.message) for w in rec]
    return [m for m in msgs if any(p in m for p in _FONT_WARN_PATTERNS)]


def smoke_test(outdir, profile: str = "sci-sans") -> dict:
    """Render a glyph-coverage probe; report resolved fonts, fallback and glyph warnings."""
    import matplotlib

    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    from pathlib import Path as _P

    info = apply_typography(profile)
    outdir = _P(outdir)
    outdir.mkdir(parents=True, exist_ok=True)

    fig, ax = plt.subplots(figsize=(150 / 25.4, 55 / 25.4))
    fig.subplots_adjust(left=0.02, right=0.98, top=0.86, bottom=0.10)
    ax.axis("off")
    lines = [
        ("Bilingual clean", PROBE_CLEAN, 10),
        ("Math (custom sans)", r"$r^{2}=0.93,\ \mu\pm\sigma,\ \sum_i x_i \leq 10^{-3}$", 10),
        ("CJK check", "中文检测：气温 25 °C，误差 ±0.2", 10),
    ]
    y = 0.78
    for label, s, fs in lines:
        ax.text(0.01, y, f"{label}: {s}", transform=ax.transAxes, fontsize=fs)
        y -= 0.3
    paths = {
        "pdf": outdir / "font_smoke_test.pdf",
        "png": outdir / "font_smoke_test.png",
    }
    with warnings.catch_warnings(record=True) as rec:
        warnings.simplefilter("always")
        fig.canvas.draw()
        fig.savefig(paths["pdf"], facecolor="white")
        fig.savefig(paths["png"], dpi=300, facecolor="white")
    clean_warnings = [str(w.message) for w in rec if any(p in str(w.message) for p in _FONT_WARN_PATTERNS)]
    plt.close(fig)

    # self-test of the detector: the gap probe uses glyphs known to be missing
    # from YaHei; the detector MUST catch them (else the detector is broken).
    fig2, ax2 = plt.subplots(figsize=(150 / 25.4, 20 / 25.4))
    ax2.axis("off")
    ax2.text(0.01, 0.4, PROBE_GAP, transform=ax2.transAxes, fontsize=10)
    with warnings.catch_warnings(record=True) as rec2:
        warnings.simplefilter("always")
        fig2.canvas.draw()
    gap_warnings = [str(w.message) for w in rec2 if any(p in str(w.message) for p in _FONT_WARN_PATTERNS)]
    plt.close(fig2)

    resolved_first = (info["resolved"]["sans_first"] or "")
    return {
        "profile": profile,
        "resolved": info["resolved"],
        "fallback_status": "NOT USED" if resolved_first in FONTS["cjk_sans"][:1] + FONTS["latin_sans"][:1] else "USED",
        "clean_ok": len(clean_warnings) == 0,
        "clean_warnings": clean_warnings,
        "detector_caught_gap": len(gap_warnings) > 0,
        "gap_warnings_sample": gap_warnings[:2],
        "paths": {k: str(v) for k, v in paths.items()},
    }


if __name__ == "__main__":
    import json
    import sys

    out = sys.argv[1] if len(sys.argv) > 1 else "."
    rep = smoke_test(out)
    print(json.dumps(rep, ensure_ascii=False, indent=2))
