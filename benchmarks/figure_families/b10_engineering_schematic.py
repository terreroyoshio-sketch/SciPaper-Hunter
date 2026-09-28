"""b10: engineering schematic - RC low-pass circuit fragment (schemdraw, synthetic)."""

from __future__ import annotations

from matplotlib.figure import Figure

import bench_common as bc


def build():
    bc.apply_house_style()
    import schemdraw
    import schemdraw.elements as elm

    try:
        d = schemdraw.Drawing(fontsize=8.0)
    except TypeError:
        d = schemdraw.Drawing()

    d += elm.SourceSin().up().label("Vin")
    d += elm.Line().right().length(1.4)
    d += elm.Resistor().right().label("R1\n10 kΩ")
    d += elm.Dot()
    d += elm.Line().right().length(1.6)
    d += elm.Dot(open=True).label("Vout", loc="right")
    d += elm.Capacitor().down().label("C1\n0.1 µF")
    d += elm.Line().left().tox(0)  # close the loop back to the source base

    d.draw(show=False)
    wrapper = d.fig
    fig = wrapper.fig if hasattr(wrapper, "fig") and isinstance(wrapper.fig, Figure) else wrapper
    if not isinstance(fig, Figure):
        raise RuntimeError("schemdraw did not expose a matplotlib Figure")
    fig.set_facecolor("white")
    for sa in fig.axes:
        sa.margins(x=0.09, y=0.09)
    fig.text(0.012, 0.028, "Schematic only - not a simulation screenshot", fontsize=8.0, color="#7A7A7A", style="italic")
    bc.mark(fig)
    return fig
