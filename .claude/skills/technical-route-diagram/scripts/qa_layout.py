"""Automatic layout QA for technical-route-diagram canvases.

Three-valued status: PASS / WARN / FAIL.
Checks are heuristics on the mm canvas; the visual inspection (>=2 rounds)
required by SKILL.md remains mandatory.

FAIL: out-of-bounds, solid-box overlap, container overlap, font < 6 pt,
      estimated text overflow.
WARN: font < 6.5 pt, grayscale luminance pairs closer than 0.05.
"""

from __future__ import annotations

import json
from pathlib import Path

from trd_kit import wrap_tokens

MIN_FONT_FAIL = 8.0  # SCI 默认（2026-09-28 修正）；venue override 需记录依据
MIN_FONT_WARN = 8.0
GRAY_MIN_DELTA = 0.05
OVERLAP_AREA_MM2 = 0.5


def _lum(hex_color: str) -> float:
    r, g, b = (int(hex_color[i : i + 2], 16) / 255.0 for i in (1, 3, 5))
    return 0.2126 * r + 0.7152 * g + 0.0722 * b


def _intersect_area(a, b) -> float:
    x = max(0.0, min(a[0] + a[2], b[0] + b[2]) - max(a[0], b[0]))
    y = max(0.0, min(a[1] + a[3], b[1] + b[3]) - max(a[1], b[1]))
    return x * y


def _make_line_counter(fig):
    """Real-metric line counter: wraps with the ACTUAL renderer text metrics
    (2026-09-28: replaced the character-width heuristic in the overflow check)."""
    fig.canvas.draw()
    renderer = fig.canvas.get_renderer()
    px_per_mm = fig.dpi / 25.4
    cache: dict = {}

    def width_px(s: str, fontsize: float) -> float:
        key = (s, fontsize)
        if key not in cache:
            t = fig.text(0.0, -10.0, s, fontsize=fontsize)
            cache[key] = float(t.get_window_extent(renderer=renderer).width)
            t.remove()
        return cache[key]

    def count(text: str, fontsize: float, usable_mm: float) -> int:
        usable = usable_mm * px_per_mm
        lines = 0
        for para in (text or "").split("\n"):
            tokens = wrap_tokens(para)
            if not tokens:
                lines += 1
                continue
            cur = ""
            n = 1
            for tok in tokens:
                if width_px(cur + tok, fontsize) <= usable:
                    cur += tok
                else:
                    n += 1
                    cur = tok.lstrip()
            lines += n
        return lines

    return count


def check(canvas, outdir=None, name: str = "qa_report") -> tuple[str, list[str], list[str]]:
    fails: list[str] = []
    warns: list[str] = []
    els = canvas.els

    for e in els:
        if not e.rect:
            continue
        x, y, w, h = e.rect
        if x < -0.05 or y < -0.05 or x + w > canvas.w + 0.05 or y + h > canvas.h + 0.05:
            fails.append(f"out-of-bounds: {e.kind} '{e.id}' rect=({x:.1f},{y:.1f},{w:.1f},{h:.1f})")

    for kind in ("box", "plot", "container"):
        group = [e for e in els if e.kind == kind and e.rect]
        for i in range(len(group)):
            for j in range(i + 1, len(group)):
                a, b = group[i], group[j]
                area = _intersect_area(a.rect, b.rect)
                if area > OVERLAP_AREA_MM2:
                    fails.append(f"overlap({kind}): '{a.id}' vs '{b.id}' area={area:.1f}mm2")

    for e in els:
        if not e.fontsize:
            continue
        if e.fontsize < MIN_FONT_FAIL:
            fails.append(f"font<{MIN_FONT_FAIL}pt: '{e.id}' = {e.fontsize}pt")
        elif e.fontsize < MIN_FONT_WARN:
            warns.append(f"font<{MIN_FONT_WARN}pt: '{e.id}' = {e.fontsize}pt")

    measure = _make_line_counter(canvas.fig)
    for e in els:
        if e.kind != "box" or not e.rect or not e.label:
            continue
        x, y, w, h = e.rect
        usable_w = w - 3.0
        need = measure(e.label, e.fontsize, usable_w) * e.fontsize * 1.25 * 25.4 / 72.0
        if need > h - 1.0:
            fails.append(f"text overflow: '{e.id}' needs ~{need:.1f}mm > {h - 1.0:.1f}mm: {e.label!r}")

    fills = {}
    for e in els:
        if e.kind == "box" and e.fill:
            fills.setdefault(e.fill, e.id)
    items = sorted(fills.items(), key=lambda kv: _lum(kv[0]))
    for i in range(len(items)):
        for j in range(i + 1, len(items)):
            d = abs(_lum(items[i][0]) - _lum(items[j][0]))
            if d < GRAY_MIN_DELTA:
                warns.append(f"grayscale close ({d:.3f}): {items[i][0]}({items[i][1]}) vs {items[j][0]}({items[j][1]})")

    status = "FAIL" if fails else ("WARN" if warns else "PASS")

    if outdir is not None:
        outdir = Path(outdir)
        outdir.mkdir(parents=True, exist_ok=True)
        payload = {"status": status, "fails": fails, "warns": warns}
        (outdir / f"{name}.json").write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
        lines = [f"# Layout QA — {status}", "", f"- FAIL: {len(fails)}", f"- WARN: {len(warns)}", ""]
        lines += [f"- FAIL: {m}" for m in fails] or ["- FAIL: (none)"]
        lines += [f"- WARN: {m}" for m in warns] or ["- WARN: (none)"]
        lines += ["", "注意：自动检查为启发式估算；视觉目检（>=2 轮）为强制项。"]
        (outdir / f"{name}.md").write_text("\n".join(lines), encoding="utf-8")

    print(f"[qa_layout] status={status} fails={len(fails)} warns={len(warns)}")
    for m in fails:
        print(f"  FAIL  {m}")
    for m in warns:
        print(f"  WARN  {m}")
    return status, fails, warns
