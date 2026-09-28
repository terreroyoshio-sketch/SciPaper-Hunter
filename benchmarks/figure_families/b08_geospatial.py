"""b08: geospatial choropleth on a synthetic 1-degree grid (geopandas, no cartopy)."""

from __future__ import annotations

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib.patches import Patch
from shapely.geometry import Polygon

import bench_common as bc


def build():
    bc.apply_house_style()
    import geopandas as gpd

    rng = np.random.default_rng(108)
    cells, values = [], []
    for lon in range(100, 106):
        for lat in range(20, 24):
            cells.append(Polygon([(lon, lat), (lon + 1, lat), (lon + 1, lat + 1), (lon, lat + 1)]))
            values.append(round(10 + 5.0 * np.sin((lon - 100) / 1.7) + 3.0 * np.cos((lat - 20) / 1.3) + rng.normal(0, 0.9), 2))
    gdf = gpd.GeoDataFrame({"value": values}, geometry=cells, crs="EPSG:4326").to_crs("EPSG:32648")
    gdf["cls"] = pd.qcut(gdf["value"], 5, labels=False)
    edges = pd.qcut(gdf["value"], 5, retbins=True)[1]

    fig, ax = plt.subplots(figsize=bc.mm(122, 94))
    fig.subplots_adjust(left=0.14, right=0.68, top=0.93, bottom=0.10)

    cmap = plt.get_cmap("YlGnBu")
    colors = [cmap(t) for t in np.linspace(0.18, 0.95, 5)]
    gdf.plot(color=[colors[int(c)] for c in gdf["cls"]], edgecolor="#666666", linewidth=0.4, ax=ax)

    # a few labeled sites
    pts = gdf.geometry.representative_point()
    for i in (3, 10, 19):
        px, py = np.asarray(pts.iloc[i].coords)[0]
        ax.plot(px, py, marker="o", ms=3.2, color="#222222", zorder=6)
        ax.text(px + 6000, py + 6000, f"Site {i + 1}", fontsize=8.0, color="#222222", zorder=6)

    # scale bar below the map band (white letterbox margin: avoids dark cells and
    # avoids crossing the map boundary - standard cartographic placement)
    x0 = gdf.total_bounds[0] + 8000
    y0 = gdf.total_bounds[1] - 35000
    ax.plot([x0, x0 + 20000], [y0, y0], color="#222222", lw=2.0, solid_capstyle="butt", zorder=6)
    ax.text(x0 + 10000, y0 - 8000, "20 km", fontsize=8.0, ha="center", va="top", color="#222222", zorder=6)

    # UTM km ticks
    ax.ticklabel_format(style="plain")
    xt = ax.get_xticks()
    yt = ax.get_yticks()
    ax.set_xticks(xt)
    ax.set_xticklabels([f"{v / 1000:.0f}" for v in xt], fontsize=8.0)
    ax.set_yticks(yt)
    ax.set_yticklabels([f"{v / 1000:.0f}" for v in yt], fontsize=8.0)
    ax.set_xlabel("Easting (km)")
    ax.set_ylabel("Northing (km)")

    handles = [Patch(facecolor=colors[i], edgecolor="#666666", lw=0.4, label=f"{edges[i]:.1f} - {edges[i + 1]:.1f}") for i in range(5)]
    ax.legend(handles=handles, title="Quantile classes", fontsize=8.0, title_fontsize=8.0, loc="upper left", bbox_to_anchor=(1.01, 1.0), frameon=False, borderaxespad=0.0)

    fig.text(0.016, 0.026, "Synthetic example - EPSG:32648 - 1 deg grid",
             fontsize=8.0, color="#7A7A7A", style="italic")
    bc.panel_label(ax, "a")

    bc.mark(fig)
    return fig
