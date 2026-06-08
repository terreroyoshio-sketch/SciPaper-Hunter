# Scientific Visualization Skills — README

**安装日期**: 2026-05-15
**来源仓库**: K-Dense-AI/scientific-agent-skills
**Skills 根目录**: C:\Users\张涵\.claude\skills\

---

## 1. 本次安装的 6 个 Skills

| # | Skill | 来源 | 路径 |
|---|-------|------|------|
| 1 | matplotlib | K-Dense → 本地已安装 | .claude/skills/matplotlib/ |
| 2 | seaborn | K-Dense → 本地已安装 | .claude/skills/seaborn/ |
| 3 | plotly | **本地创建**（仓库中不存在） | .claude/skills/plotly/ |
| 4 | scientific-visualization | K-Dense → 本地已安装 | .claude/skills/scientific-visualization/ |
| 5 | geopandas | K-Dense → 本地已安装 | .claude/skills/geopandas/ |
| 6 | geomaster | K-Dense → 本地已安装 | .claude/skills/geomaster/ |

## 2. 每个 Skill 的用途

| Skill | 用途 | 适合场景 |
|-------|------|---------|
| **matplotlib** | 精细控制图表元素、多面板图、事件研究图、期刊投稿级矢量图 | 论文最终图件、复杂自定义图、多面板 figure |
| **seaborn** | 快速统计可视化、分组比较、数据分布探索 | 数据探索、组会展示、回归前分布检查 |
| **plotly** | 交互式图表、HTML 可分享图、悬停/缩放/筛选 | 探索性数据分析、合作者共享、演示汇报 |
| **scientific-visualization** | 投稿级图件元技能，统筹 matplotlib/seaborn/plotly | 论文投稿最终图表、期刊格式统一 |
| **geopandas** | 矢量空间数据处理、空间连接、缓冲区、CRS 转换 | 空间面板数据构建、行政边界制图、地理断点回归 |
| **geomaster** | 遥感影像处理、GEE 工作流、卫星指数提取、栅格分析 | 卫星影像变量提取、长时序环境变量、农业/环境/灾害数据 |

## 3. 风险边界

| Skill | 风险等级 | 关键限制 |
|-------|---------|---------|
| matplotlib | 🟢 低 | 仅生成图件，不改数据 |
| seaborn | 🟢 低 | 仅统计可视化 |
| plotly | 🟢 低 | 仅交互式图表（本地创建，无脚本） |
| scientific-visualization | 🟢 低 | 含可执行脚本（figure_export.py, style_presets.py） |
| geopandas | 🟢 低 | 仅空间数据处理 |
| geomaster | 🟡 中低 | GEE 需用户认证、遥感依赖建议 conda |

## 4. 科研场景分工

| 场景 | 优先使用 | 辅助使用 |
|------|---------|---------|
| 探索性统计图 | **seaborn** | plotly |
| 精细投稿图 | **matplotlib** | scientific-visualization |
| 交互式展示 | **plotly** | — |
| 投稿级统一规范 | **scientific-visualization** | nature-figure |
| 矢量空间数据 | **geopandas** | matplotlib |
| 遥感与栅格数据 | **geomaster** | geopandas |
| Nature 最终图件 | **nature-figure** | scientific-visualization, matplotlib |
| 期刊格式检查 | **journal-formatting-pipeline** | scientific-visualization |

## 5. 与已有 Skills 的组合方式

| 已有 Skill | 新 Skill 组合 | 用途 |
|-----------|-------------|------|
| nature-figure | scientific-visualization, matplotlib | Nature 投稿图件 |
| journal-formatting-pipeline | scientific-visualization | 期刊格式 + 图件统一检查 |
| word-document-processor | matplotlib, geopandas | 图件嵌入 DOCX |
| ppt-master | plotly, seaborn | 演示汇报 |
| nsfc-proposal-architecture-pipeline | geopandas, geomaster | 项目申报书空间数据与制图 |
| objective-innovation-auditor-pipeline | scientific-visualization | 图件客观性检查 |
| rstudio-research-agent | geomaster | R 与 Python 协同遥感分析 |
| summarize | seaborn, plotly | 分析结果可视化汇报 |
| docs | 所有 6 个 | 可复现流程记录 |

## 6. 学生推荐使用顺序

如果你是本科生或研究生，推荐优先级：

| 顺序 | Skill | 原因 |
|------|-------|------|
| 1 | **seaborn** | 先学会快速看懂数据 |
| 2 | **matplotlib** | 再做论文级精细图 |
| 3 | **scientific-visualization** | 投稿或比赛展示时统一规范 |
| 4 | **geopandas** | 做空间数据或地图时使用 |
| 5 | **plotly** | 组会和演示时使用 |
| 6 | **geomaster** | 只有涉及遥感、卫星、GEE 或栅格数据时再深入 |

## 7. 依赖安装快速参考

```bash
# 基础可视化
pip install matplotlib seaborn plotly pandas numpy scipy kaleido pillow

# 矢量空间分析（推荐 conda-forge）
conda install -c conda-forge geopandas shapely pyproj folium contextily

# 遥感分析（可选，按需安装）
conda install -c conda-forge rasterio rioxarray xarray
pip install earthengine-api geemap pystac-client planetary-computer
```
