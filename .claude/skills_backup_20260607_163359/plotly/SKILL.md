---
name: plotly
description: Interactive visualization library for web-based plots with hover, zoom, filtering, and animation. Use when you need interactive charts, dashboards, or shareable HTML figures. For static publication figures use matplotlib; for statistical exploration use seaborn.
license: MIT License
metadata:
    skill-author: K-Dense Inc. (via scientific-agent-skills), adapted for local installation
---

# Plotly

## Overview

Plotly is a graphing library for creating interactive, publication-quality visualizations that work in Jupyter notebooks, web browsers, and dashboards. Plotly Express provides a high-level API for quick chart creation, while the graph_objects API offers fine-grained control.

## When to Use This Skill

- Creating interactive charts for data exploration
- Building dashboards with Plotly Dash
- Generating shareable HTML figures for collaborators
- Adding hover tooltips, zooming, and panning to visualizations
- Animating temporal data
- Exporting static images for publication (via kaleido)
- Plotly is NOT a substitute for matplotlib when vector PDF/SVG is required for journal submission

## Quick Start

```python
import plotly.express as px
import pandas as pd

df = pd.DataFrame({
    'x': [1, 2, 3, 4, 5],
    'y': [10, 11, 12, 13, 14],
    'category': ['A', 'B', 'A', 'B', 'A']
})

fig = px.scatter(df, x='x', y='y', color='category', title='Interactive Scatter Plot')
fig.show()
```

## Plotly Express (High-Level API)

### Scatter and Line Plots

```python
# Basic scatter
px.scatter(df, x='col_x', y='col_y', color='category', size='magnitude')

# Line chart
px.line(df, x='date', y='value', color='category')

# Connected scatter
px.scatter(df, x='x', y='y', trendline='ols')
```

### Distribution Plots

```python
# Histogram
px.histogram(df, x='value', color='category', nbins=30)

# Box plot
px.box(df, x='category', y='value', color='category')

# Violin plot
px.violin(df, x='category', y='value', box=True)

# Density heatmap
px.density_heatmap(df, x='x', y='y', nbinsx=20, nbinsy=20)

# Marginal plots
px.scatter(df, x='x', y='y', color='category', marginal_x='histogram', marginal_y='box')
```

### Multi-Panel (Facet) Plots

```python
px.scatter(df, x='x', y='y', color='category', facet_col='group', facet_row='experiment')
```

### 3D Plots

```python
px.scatter_3d(df, x='x', y='y', z='z', color='category')
```

### Animations

```python
px.scatter(df, x='x', y='y', animation_frame='time', color='category', range_x=[0, 100], range_y=[0, 100])
```

## Graph Objects API (Fine-Grained Control)

```python
import plotly.graph_objects as go

fig = go.Figure()

# Add traces
fig.add_trace(go.Scatter(x=[1, 2, 3], y=[4, 5, 6], mode='lines+markers', name='Series 1'))
fig.add_trace(go.Bar(x=['A', 'B', 'C'], y=[10, 11, 12], name='Series 2'))

# Customize layout
fig.update_layout(
    title='Custom Plot',
    xaxis_title='X Axis',
    yaxis_title='Y Axis',
    template='plotly_white',
    width=800,
    height=500,
    font=dict(family='Arial, sans-serif', size=12),
    legend=dict(x=0.8, y=0.9)
)

fig.show()
```

## Subplots

```python
from plotly.subplots import make_subplots

fig = make_subplots(
    rows=2, cols=2,
    subplot_titles=('Plot A', 'Plot B', 'Plot C', 'Plot D'),
    specs=[[{'type': 'scatter'}, {'type': 'bar'}],
           [{'type': 'pie'}, {'type': 'scatter'}]]
)

fig.add_trace(go.Scatter(x=[1,2,3], y=[4,5,6]), row=1, col=1)
fig.add_trace(go.Bar(x=['A','B'], y=[10,11]), row=1, col=2)
fig.show()
```

## Exporting Figures

```python
# HTML (interactive, shareable)
fig.write_html('figure.html')

# Static image (requires kaleido or orca)
fig.write_image('figure.png', scale=3)    # ~300 DPI
fig.write_image('figure.pdf')             # Vector
fig.write_image('figure.svg')             # Vector

# For publications: use scale=3-4 for ~300 DPI at typical sizes
fig.write_image('figure.tiff', width=800, height=500, scale=3)
```

## Statistical Charts

```python
# Correlation heatmap
import plotly.figure_factory as ff

corr = df.corr()
fig = ff.create_annotated_heatmap(
    z=corr.values,
    x=list(corr.columns),
    y=list(corr.index),
    colorscale='viridis'
)

# Error bars
fig = px.scatter(data, x='x', y='y', error_x='x_err', error_y='y_err')

# Confidence bands
fig = px.line(data, x='x', y='y_upper', color='group')
fig.add_ribbon(x=data['x'], y1=data['y_lower'], y2=data['y_upper'], color='rgba(0,100,200,0.2)')
```

## Best Practices

1. **Use Plotly Express first** - 80% of needs covered in one line
2. **Fall back to graph_objects** - when you need custom layouts or trace types
3. **Export format selection**:
   - HTML for collaboration and exploration
   - PDF/SVG for publications (requires kaleido)
   - PNG for quick sharing (use scale=2-3 for quality)
4. **Always set template** - `plotly_white` or `plotly` for clean defaults
5. **Interactive vs static** - Design for both; test static exports at target resolution
6. **Large datasets** - Use `plotly.graph_objects.Scattergl` for WebGL acceleration

## Color Palettes

```python
# Plotly defaults (colorblind-friendly qualitative palette)
# Use built-in templates
fig.update_layout(template='plotly_white')

# Custom color sequence
color_seq = px.colors.qualitative.Set2
color_seq = px.colors.sequential.Viridis  # For continuous

# Diverging
color_seq = px.colors.diverging.RdBu
```

## Limitations

- **Not for vector journal submission** - Use matplotlib for PDF/EPS that journals require
- **Performance with big data** - Use `Scattergl`, `datashader`, or downsample
- **Kaleido required** - Static export needs `pip install kaleido`
- **No offline maps by default** - Mapbox requires token for some features

## Integration with Other Tools

- **Dash** - Build full dashboard applications
- **Jupyter** - Interactive display in notebooks
- **Streamlit** - `st.plotly_chart(fig)` for web apps
- **scientific-visualization** - Apply publication styling via figure export parameters
