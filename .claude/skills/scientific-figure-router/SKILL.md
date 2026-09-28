---
name: scientific-figure-router
description: 科研制图总入口：先判图件家族与目标载体，再分派到对应专业 Skill/库，最后必经 figure-quality-gate。用户要画、重绘、改进任何论文图、方法图、技术路线图、流程图、机制示意、图形摘要、GIS/网络/电路/3D 图时使用。本技能自身不绘图。
---

# Scientific Figure Router — 科研制图路由

只做三件事：**判家族 → 分派 → 强制进验收门**。不绘图、不写图代码。

## 路由流程（先问后画）

开始前必须能回答：

1. 数据是**真实数值**还是**概念关系**？（真实数据图 vs 概念图，决定证据规则）
2. 有没有：空间数据？网络拓扑？物理/几何关系？电路/控制结构？3D？需嵌入已有图片/地图？
3. **目标载体**是什么：SCI 投稿 / 学位论文 / 基金申报 / 竞赛论文 / 课程设计 / PPT / 办公汇报？（决定字号与风格阈值）
4. 单图还是拆 panel？

任一问题无法回答 → 先问用户，**不得默认开画**。

## 路由表

| 判定结果 | 分派到 | 备注 |
|---|---|---|
| 真实数据曲线/柱/散点/热力/误差 | `figurelab-publish` / `academic-figure-skill` / `scientific-visualization` | 已装，勿重复实现 |
| 统计分布/模型比较/贡献度 | `seaborn` + 统计类技能 | 不确定性表达规范见 gate |
| 多阶段科研方法（数据→模型→指标→结果） | `scientific-method-framework` | |
| 研究路线/技术路线 | `technical-route-diagram`；逻辑未成型先 `technical-route-blueprint-planner` | |
| 算法 DAG / 计算流程 | `scientific-flowchart` | Graphviz 只算布局，呈现自绘 |
| 物理/生态/医学/工程机制 | `mechanism-schematic` | |
| 论文总览 / graphical abstract | `graphical-abstract` | |
| 空间/栅格/分区/地图 | `geospatial-figure`（geopandas + cartopy 已装） | |
| 节点关系/拓扑/模型结构 | `network-topology` | |
| 电路/逻辑/时序/状态机 | `engineering-schematic`（schemdraw 已装） | |
| 3D 点云/网格/体数据 | `scientific-3d`（pyvista 已装） | |
| 混合多面板（地图+流程+曲线+表） | `multipanel-compositor` | |
| 办公/课程/PPT 可编辑 drawio 图 | 主仓库 `drawio-diagram-workbench` + `/diagram` 命令 | 该体系在另一检出 |
| 光路/光子/芯片/实验装置示意 | `nature-figure-style` | 已装 |

## 渲染器决策树

- 默认 `matplotlib`：数据图、几何图、机制示意、自定义路线图。
- `graphviz`（dot 二进制在本机 D:\Graphviz\bin，v14.1.3）：**只计算复杂 DAG 布局**，最终视觉必须自己呈现——禁止 dot 默认皮肤交稿。
- `networkx`：图数据结构 + 布局（spring / multipartite / circular）。
- `geopandas`（+shapely/pyproj）：GIS。真实投影与底图用 cartopy（0.26.0 已装；首次 `coastlines()` 需联网）。
- `schemdraw`：电路 / logic / timing / state machine。
- `pyvista`：3D（0.49.0 已装，off-screen 实测）；简单场景可用 matplotlib mplot3d 兜底并声明限制。
- **不因为某库存在就强用；最终图可由多个 renderer 组合。**

## 全家族硬规则

1. **必经 gate**：任何"完成"声明前跑 `figure-quality-gate`，输出三值状态（PASS / PASS_WITH_LIMITATION / FAIL）。禁止"应该没问题"。
2. **反造假**：内嵌小图/数据必须来自真实数据；示意图必须标注 schematic/示意图；PLACEHOLDER 合成内容不得投稿；数字与显著性无依据不得标注。
3. **字号按印幅反推**：SCI 默认 **≥8 pt**（tick/legend/annotation，@最终尺寸，单一来源 `figure_qa.DEFAULT_MIN_PT`）；学位论文 ≥8 pt；课程/PPT 图 ≥10 pt（主仓库规则）。目标期刊模板明确允许更小时，走**显式 venue override** 并在 QA 报告记录依据（`threshold_source` 字段）。
4. **语义容器允许**：矩形/圆角矩形/分区面板/箭头/虚线区域可用，但**禁止无语义、模板化的方框堆叠**（默认 Mermaid 风 / PPT SmartArt / 彩色卡片堆 / 全同尺寸节点 / 纯文字节点占主体）。算法流程图（数模场景）优先几何叙事；方法框架与路线图允许语义容器。
5. **矢量优先**：PDF/SVG 主交付，PNG 仅预览；栅格元素 ≥300 dpi；字体嵌入须实测。
6. **来源可追溯**：每张正式图记录 figure_id / 数据来源 / 脚本 / 参数 / 随机种子 / 时间戳。

## 何时不用

- 用户只问概念、不要图 → 不启用。
- 用户指名了具体技能 → 直接走指名技能，本 router 不介入。
- 纯文字排版/表格 → 不属于图件。
