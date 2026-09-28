---
name: geospatial-figure
description: 空间分析图绘制（地图、choropleth、栅格叠加、空间分区）：geopandas/shapely/matplotlib 链路，CRS 纪律 + 比例尺 + 图例分级。用户要画地图、空间分布图、土地利用图、栅格图、空间流程时使用。不用于普通曲线图（figurelab）、不用于地图+流程复合的编排（multipanel-compositor 组装）。
---

# Geospatial Figure — 空间分析图

## 渲染链路（本机现状，2026-09-28 更新）
- **已装**：geopandas 1.1.3 + shapely 2.1.2 + pyproj；**cartopy 0.26.0（2026-09-28 安装；Robinson 投影 + gridlines 冒烟测试通过）**
- 简单图仍可用降级路径（`.to_crs(投影CRS)` 后直接 plot）；海岸线等 Natural Earth 底图要素走 cartopy——**首次调用 `coastlines()` 需联网下载数据**，离线环境先声明

## CRS 纪律（硬规则）
1. 每张空间图必须声明数据 CRS（EPSG 号）；来源数据 CRS 不明 → 停手询问。
2. 面积/距离有意义的图（比例尺、密度）：**先投影到等面积/等距 CRS**（如本地 UTM / Albers）再绘制；球面（地理）CRS 只用于纯展示。
3. 比例尺与指北针：比例尺必须有（用投影后坐标换算实际公里数）；指北针按刊例可选。
4. 图角注来源（数据名+年份+EPSG）。

## 地图要素规范
- **Choropleth 分级**：明示分级方法（quantile / equal-interval / natural breaks），图例显示分级断点；**禁 rainbow/jet**，用单色渐变（如 viridis/单色系）或发散色仅用于正负偏离
- **栅格叠加**：`imshow(extent=[xmin,xmax,ymin,ymax])` 须与矢量同 CRS；栅格透明度让底图可读
- 类别图（土地利用）：色觉友好离散色 + 类别图例；同色语义全文一致
- 文字标注：地名/分区名贴要素；数量单位进图例

## 输入与证据
- 空间数据文件（shp/gpkg/geojson/栅格）+ 来源与许可；**不得手工描边界冒充真实行政区**
- 示意性空间结构（非真实数据）标 schematic

## 输出与 QA
- SVG + PDF + PNG + 灰度 + 缩印预览；**必经 `figure-quality-gate`**
- 附加检查：分级边界是否被误读（目检图例）、比例尺换算抽查

## 失败条件
- 数据 CRS 不明 / 数据来源与许可不明
- 需要真实海岸线底图但用户不批 cartopy 安装 → 降级并声明
