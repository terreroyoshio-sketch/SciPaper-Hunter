# Scientific Visualization — Combined Workflows

---

## A. 论文统计图工作流

```
1. Using-Superpowers
   明确图件目的、目标期刊、数据来源和验收标准。

2. empirical-result-extraction-auditor
   提取真实结果，防止图件结论超出数据。

3. seaborn
   快速探索数据分布和分组关系。

4. matplotlib
   生成精细可控的最终图。

5. scientific-visualization
   对齐期刊格式、尺寸、字体、配色和导出格式。

6. nature-figure
   用于 Nature 风格多面板图。
```

## B. 交互式探索工作流

```
1. summarize
   提炼分析目标。

2. plotly
   生成交互式 HTML。

3. docs
   记录变量、筛选条件和图表解释。
```

## C. 投稿图件审计工作流

```
1. scientific-visualization
   检查图幅、分辨率、字体和格式。

2. nature-figure
   检查图件结构和面板逻辑。

3. journal-formatting-pipeline
   检查图表标题、编号、图注和投稿格式。

4. word-document-processor
   把图件和图注嵌入 DOCX。
```

## D. 矢量空间数据工作流

```
1. geopandas
   读取边界、点位和属性表。

2. CRS 检查
   任何距离、面积和空间连接前必须明确坐标系。

3. 空间连接 / 缓冲区 / 叠加
   生成空间变量。

4. matplotlib 或 plotly
   输出静态地图或交互式地图。

5. docs
   记录可复现流程。
```

## E. 遥感与栅格数据工作流

```
1. geomaster
   确定遥感数据源、波段、指数和时间范围。

2. Google Earth Engine 或 STAC
   按授权和数据可得性选择执行路径。

3. raster / xarray / rioxarray
   处理栅格数据。

4. geopandas
   汇总到行政边界或样本点。

5. scientific-visualization
   输出论文图件。
```

## F. 项目申报书空间图工作流

```
1. nsfc-proposal-architecture-pipeline
   明确研究内容和数据路径。

2. geomaster
   设计遥感或地理数据方案。

3. geopandas
   生成研究区、样本区和空间变量图。

4. nature-figure
   提升图件质量。

5. ppt-master
   生成展示 PPT。
```

## G. 经济学空间面板数据构建工作流

```
1. geomaster
   设计遥感数据提取方案（NDVI/夜间灯光/气象等）。

2. geopandas
   执行行政边界匹配和空间连接。

3. pandas / numpy
   面板数据整理与合并。

4. statsmodels / scipy
   空间计量分析。

5. matplotlib / scientific-visualization
   输出论文级图表。
```

## H. 文献综述 + 可视化工作流

```
1. critical-literature-review-pipeline
   生成文献综述。

2. keyword-literature-download
   获取相关数据。

3. seaborn / matplotlib
   可视化文献计量结果。

4. docs
   生成综合报告。
```
