"""technical-route-diagram rendering kit (v1).

Canvas units are millimetres (1 data unit = 1 mm at final print size), so
font sizes in pt and box sizes in mm map directly onto the printed sheet.
Every placed element is recorded on the Canvas for qa_layout checks.
"""

from __future__ import annotations

import sys
from dataclasses import dataclass
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyArrowPatch, FancyBboxPatch, Polygon

_TYP_SCRIPTS = Path(__file__).resolve().parents[2] / "scientific-typography" / "scripts"
if str(_TYP_SCRIPTS) not in sys.path:
    sys.path.insert(0, str(_TYP_SCRIPTS))
try:
    from typography import apply_typography as _apply_typography
except Exception:  # pragma: no cover - fallback keeps the kit standalone
    _apply_typography = None

INK = "#222222"
MUTED = "#6E6E6E"
BAND_EDGE = "#9E9E9E"
BAND_TITLE = "#B03A2E"
BLOCK_ARROW = "#70AD47"

FAMILIES = {
    "input": {"fill": "#DAEAC9", "edge": "#70AD47"},
    "process": {"fill": "#AFC9E5", "edge": "#4472C4"},
    "method": {"fill": "#BAAAD9", "edge": "#7030A0"},
    "result": {"fill": "#F7CDA8", "edge": "#C55A11"},
    "accent": {"fill": "#FFF2CC", "edge": "#BF9000"},
    "neutral": {"fill": "#FFFFFF", "edge": "#7F7F7F"},
}

FONT_STACK = ["Microsoft YaHei", "SimHei", "Arial", "DejaVu Sans"]
PT_TO_MM = 25.4 / 72.0


def apply_style() -> None:
    if _apply_typography is not None:
        _apply_typography("sci-sans")
        return
    plt.rcParams.update(
        {
            "font.family": "sans-serif",
            "font.sans-serif": FONT_STACK,
            "axes.unicode_minus": False,
            "svg.fonttype": "none",  # keep text as <text> so SVG stays editable
            "pdf.fonttype": 42,  # embed TrueType subsets
            "ps.fonttype": 42,
        }
    )


def est_text_mm(text: str, fontsize_pt: float) -> float:
    """Approximate single-line width in mm (CJK full-width, Latin half-width)."""
    width = 0.0
    for ch in text:
        width += (1.0 if ord(ch) > 0x2E7F else 0.56) * fontsize_pt * PT_TO_MM
    return width


def wrap_tokens(text: str) -> list[str]:
    """Split into wrap tokens: each CJK char is its own token, Latin runs stay whole."""
    tokens: list[str] = []
    buf = ""
    for ch in text:
        if ord(ch) > 0x2E7F:
            if buf:
                tokens.append(buf)
                buf = ""
            tokens.append(ch)
        elif ch == " ":
            buf += ch
            tokens.append(buf)
            buf = ""
        else:
            buf += ch
    if buf:
        tokens.append(buf)
    return tokens


@dataclass
class El:
    kind: str  # container | box | plot | text | arrow
    id: str
    rect: tuple[float, float, float, float] | None
    fontsize: float = 0.0
    label: str = ""
    fill: str = ""
    edge: str = ""


class Canvas:
    def __init__(self, width_mm: float, height_mm: float):
        apply_style()
        self.w = float(width_mm)
        self.h = float(height_mm)
        self.fig = plt.figure(figsize=(self.w / 25.4, self.h / 25.4))
        self.ax = self.fig.add_axes((0.0, 0.0, 1.0, 1.0))
        self.ax.set_xlim(0, self.w)
        self.ax.set_ylim(0, self.h)
        self.ax.set_aspect("equal", adjustable="box")
        self.ax.axis("off")
        self.els: list[El] = []

    def _y(self, y_top: float) -> float:
        return self.h - y_top

    # ------------------------------------------------------------------ containers
    def band(
        self,
        x: float,
        y_top: float,
        w: float,
        h: float,
        index: str,
        title: str,
        title_size: float = 9.0,
        badge_size: float = 8.0,
    ) -> None:
        y = self._y(y_top + h)
        self.ax.add_patch(
            FancyBboxPatch(
                (x, y),
                w,
                h,
                boxstyle="round,pad=0,rounding_size=2.0",
                linewidth=0.7,
                edgecolor=BAND_EDGE,
                facecolor="#FFFFFF",
                linestyle=(0, (4, 2)),
                zorder=1,
            )
        )
        cy = self._y(y_top + 5.0)
        self.ax.add_patch(Circle((x + 5.0, cy), 2.1, facecolor=BAND_TITLE, edgecolor="none", zorder=4))
        self.ax.text(
            x + 5.0, cy, index, ha="center", va="center",
            fontsize=badge_size, color="white", fontweight="bold", zorder=5,
        )
        self.ax.text(
            x + 8.8, cy, title, ha="left", va="center",
            fontsize=title_size, color=BAND_TITLE, fontweight="bold", zorder=5,
        )
        self.els.append(El("container", f"band-{index}", (x, y, w, h)))
        self.els.append(El("text", f"band-{index}-title", None, title_size, title))

    # ------------------------------------------------------------------ boxes
    def box(
        self,
        x: float,
        y_top: float,
        w: float,
        h: float,
        label: str,
        family: str = "process",
        fontsize: float = 8.0,
        id: str = "",
    ) -> None:
        fam = FAMILIES[family]
        y = self._y(y_top + h)
        self.ax.add_patch(
            FancyBboxPatch(
                (x, y),
                w,
                h,
                boxstyle="round,pad=0,rounding_size=1.6",
                linewidth=0.8,
                edgecolor=fam["edge"],
                facecolor=fam["fill"],
                zorder=2,
            )
        )
        self.ax.text(
            x + w / 2.0, y + h / 2.0, label, ha="center", va="center",
            fontsize=fontsize, color=INK, zorder=3, linespacing=1.25,
        )
        self.els.append(El("box", id, (x, y, w, h), fontsize, label, fam["fill"], fam["edge"]))

    # ------------------------------------------------------------------ arrows
    def arrow(
        self,
        x1: float,
        y1_top: float,
        x2: float,
        y2_top: float,
        color: str = INK,
        lw: float = 1.0,
        id: str = "",
    ) -> None:
        y1, y2 = self._y(y1_top), self._y(y2_top)
        self.ax.add_patch(
            FancyArrowPatch(
                (x1, y1), (x2, y2),
                arrowstyle="-|>", mutation_scale=7,
                linewidth=lw, color=color, shrinkA=0, shrinkB=0, zorder=4,
            )
        )
        self.els.append(El("arrow", id, None))

    def block_arrow_down(
        self,
        cx: float,
        y1_top: float,
        y2_top: float,
        width: float = 7.0,
        color: str = BLOCK_ARROW,
        id: str = "",
    ) -> None:
        y1, y2 = self._y(y1_top), self._y(y2_top)
        head = 2.6
        shaft = width * 0.45
        pts = [
            (cx - shaft / 2, y1), (cx - shaft / 2, y2 + head), (cx - width / 2, y2 + head),
            (cx, y2), (cx + width / 2, y2 + head), (cx + shaft / 2, y2 + head),
            (cx + shaft / 2, y1),
        ]
        self.ax.add_patch(Polygon(pts, closed=True, facecolor=color, edgecolor="none", zorder=2))
        self.els.append(El("arrow", id, None))

    # ------------------------------------------------------------------ misc primitives
    def plot_slot(self, x: float, y_top: float, w: float, h: float, id: str = ""):
        y = self._y(y_top + h)
        ax2 = self.fig.add_axes((x / self.w, y / self.h, w / self.w, h / self.h))
        ax2.set_zorder(5)
        for spine in ax2.spines.values():
            spine.set_linewidth(0.5)
            spine.set_color("#9E9E9E")
        ax2.tick_params(labelsize=8.0, width=0.4, length=2, colors="#444444")
        self.els.append(El("plot", id, (x, y, w, h), 8.0))
        return ax2

    def text(
        self,
        x: float,
        y_top: float,
        s: str,
        fontsize: float = 6.5,
        color: str = INK,
        ha: str = "left",
        italic: bool = False,
        id: str = "",
    ) -> None:
        y = self._y(y_top)
        self.ax.text(
            x, y, s, fontsize=fontsize, color=color, ha=ha, va="center",
            style="italic" if italic else "normal", zorder=6,
        )
        self.els.append(El("text", id, None, fontsize, s))

    def legend(
        self,
        x: float,
        y_top: float,
        items: list[tuple[str, str]],
        prefix: str = "Legend:",
        sw: float = 4.0,
        sh: float = 2.8,
        fontsize: float = 8.0,
        gap: float = 3.5,
    ) -> None:
        cx = x
        if prefix:
            self.ax.text(cx, self._y(y_top), prefix, fontsize=fontsize, color=INK, ha="left", va="center", zorder=6)
            cx += est_text_mm(prefix, fontsize) + 2.0
        for family, label in items:
            fam = FAMILIES[family]
            self.ax.add_patch(
                FancyBboxPatch(
                    (cx, self._y(y_top) - sh / 2.0), sw, sh,
                    boxstyle="round,pad=0,rounding_size=0.6",
                    linewidth=0.7, edgecolor=fam["edge"], facecolor=fam["fill"], zorder=3,
                )
            )
            self.ax.text(cx + sw + 1.2, self._y(y_top), label, fontsize=fontsize, color=INK, ha="left", va="center", zorder=6)
            cx += sw + 1.2 + est_text_mm(label, fontsize) + gap
        self.els.append(El("text", "legend", None, fontsize, prefix))

    # ------------------------------------------------------------------ export
    def export(self, outdir, name: str, dpi: int = 600) -> dict[str, str]:
        outdir = Path(outdir)
        outdir.mkdir(parents=True, exist_ok=True)
        out = {
            "svg": outdir / f"{name}.svg",
            "pdf": outdir / f"{name}.pdf",
            "png": outdir / f"{name}.png",
        }
        self.fig.savefig(out["svg"], facecolor="white")
        self.fig.savefig(out["pdf"], facecolor="white")
        self.fig.savefig(out["png"], dpi=dpi, facecolor="white")
        try:
            from PIL import Image

            with Image.open(out["png"]) as im:
                gray_path = outdir / f"{name}_grayscale.png"
                im.convert("L").save(gray_path, dpi=(dpi, dpi))
            out["grayscale"] = gray_path
        except ImportError:
            pass
        return {k: str(v) for k, v in out.items()}
