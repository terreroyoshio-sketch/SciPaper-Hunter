---
name: scientific-method-framework
description: 科研方法框架图（数据→模型→指标→结果 的多层方法学总览图）绘制：语义容器分层 + 跨层箭头 + 内嵌真实小图/公式。用户要画方法总览、研究框架、方法框架、methodological framework、数据-方法-结果分层图时使用。不用于纯数据图（figurelab）、不用于技术路线图（technical-route-diagram）、不用于机制物理示意（mechanism-schematic）。
---

# Scientific Method Framework — 方法框架图

## 职责
把论文方法学组织成 **分层框架图**：层（layer）用分区带，层内对象用语义容器，跨层用箭头表达数据/信息流，关键节点内嵌真实小图、公式或数据表示。

## 常用层级（按论文实际选，**不得固定套模板**）
`Data → Method → Model → Analysis → Validation → Result`（或子集；或按实际方法命名）。

## 输入与证据要求
- 方法章节文本 / 流程图初稿 / 变量与数据说明
- 内嵌小图必须来自真实数据文件；演示内容标 PLACEHOLDER
- 公式必须来自论文原文，禁止自造

## 渲染器
- 首选：matplotlib + `technical-route-diagram/scripts/trd_kit.py` 基元（band / box / arrow / plot_slot / legend）
- 兜底：纯 matplotlib FancyBboxPatch（参考已装 `nature-figure-style/references/architecture_diagram.md`）

## 视觉规则
1. 网格先行：层高一致，层内对象同宽等距；布局先于连线。
2. 每层一个区域带（可虚线框 + 层名）；层名加粗；语义色族（输入/方法/结果）全图一致并进图例。
3. 每层 2–4 个对象；**至少一个内嵌小图**（结果缩略图/示意曲线）与至少一个公式或数据表示（表/样本）/层级组合。
4. 箭头承载语义：主线单方向；跨层箭头不得穿越容器主体（走层间走廊）。
5. 字号按印幅（SCI 默认 ≥8 pt；venue override 需记录依据）；低饱和配色、灰度可辨。
6. 禁止：全同尺寸盒子平铺、无方向约定、装饰性图标。

## 科学正确性
- 框架必须与论文方法一一对应，不得添加论文没有的步骤；层级归属按原文。
- 内嵌小图的统计标注须有分析输出支持。

## 输出与 QA
- 输出：SVG（可编辑）+ PDF（投稿）+ PNG 预览 + 灰度 + 缩印预览
- **必经 `figure-quality-gate`**（三值状态）；目检 ≥1 轮。

## 失败条件（触发即停并报告）
- 论文方法无法归纳为 ≥2 层且用户无法补充说明
- 内嵌小图无真实数据来源
- 目标期刊尺寸/载体不明且用户拒绝确认
