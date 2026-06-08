# Scientific Visualization — Prompt Templates

---

## Template 1: 论文统计图生成

```
请使用 matplotlib、seaborn 和 scientific-visualization。
以下是我的数据结构、变量说明和论文结论。请先判断适合的
图表类型，再生成可复现 Python 绘图代码。要求输出 PNG、
PDF、SVG，保留 source data traceability。不得更改原始
数据，不得编造统计结果。
```

## Template 2: 事件研究图

```
请使用 matplotlib 和 scientific-visualization。请基于
以下事件研究回归结果生成论文级 event-study plot，包括
点估计、置信区间、政策实施时间线、基准期标注、零线、
前趋势视觉检查和期刊导出参数。不得改变任何系数和置信区间。
```

## Template 3: 探索性数据分析图

```
请使用 seaborn。请基于以下 DataFrame 字段说明，生成
探索性统计图方案，包括分布图、分组比较图、相关矩阵和
异常值检查图。先输出图表计划，再生成代码。
```

## Template 4: 交互式图表

```
请使用 plotly。请基于以下数据生成交互式 HTML 图表，
用于组会或合作者查看。要求支持悬停查看数值、图例筛选
和缩放。不要上传数据到外部服务。
```

## Template 5: 期刊投稿图件审计

```
请使用 scientific-visualization、nature-figure 和
journal-formatting-pipeline。请检查以下图件是否满足
目标期刊的图幅、分辨率、字体、线宽、配色、图注和文件
格式要求。只输出问题清单、修订建议和导出参数，不得修改
原始数据。
```

## Template 6: 空间连接与地图制图

```
请使用 geopandas。以下是我的点数据、行政边界和研究目标。
请检查 CRS，执行空间连接，生成可复现代码，并输出地图
可视化方案。不得在未经投影转换时直接计算距离或面积。
```

## Template 7: 政策边界或地理断点分析

```
请使用 geopandas。请基于以下政策边界、观测点和行政区划，
设计空间匹配和边界距离计算流程。必须检查 CRS、边界拓扑、
缓冲区宽度和空间连接误差风险。
```

## Template 8: 遥感变量提取

```
请使用 geomaster。我要从 Sentinel/Landsat/GEE 中提取
【NDVI/EVI/NDWI/夜间灯光/气温/降水/PM2.5】变量，并汇总
到【省/市/县/栅格/样本点】层级。请给出数据源、时间范围、
波段选择、云掩膜、空间汇总、质量控制和可复现代码框架。
```

## Template 9: 经济学空间面板数据构建

```
请使用 geomaster 和 geopandas。请设计一个从遥感或地理
空间数据到面板数据的完整流程，包括数据源、空间边界、CRS、
栅格裁剪、区域统计、面板合并、缺失值处理和最终变量说明。
```

## Template 10: 项目申报书图件与地图

```
请使用 nsfc-proposal-architecture-pipeline、
objective-innovation-auditor-pipeline、scientific-visualization、
geopandas、geomaster 和 ppt-master。请基于以下项目内容
设计 1 张技术路线图、1 张数据来源地图、1 张结果展示图
和 1 张 PPT 展示图。不得编造数据。
```

---

*更多组合方式请参见 SCIENTIFIC_VISUALIZATION_COMBINED_WORKFLOWS.md*
