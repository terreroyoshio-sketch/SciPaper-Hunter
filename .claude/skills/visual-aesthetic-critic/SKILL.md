---
name: visual-aesthetic-critic
description: 科研图视觉审美审查：按 14 个观察维度（层级/平衡/对齐/留白/密度/字体/色彩语义/注释质量/AI 味等）对成图做独立审查，输出三值结论与具体位置；配套确定性视觉指标脚本（密度/象限均衡/颜色数/饱和度）与 contact-sheet 横向审查规则。图件终审、组图一致性、"AI 味"排查时使用。不修改数据/模型/统计（只观察、判断、提修改建议）；不负责机械碰撞检测（collision-aware-layout 已覆盖）。
---

# Visual Aesthetic Critic — 视觉审美审查

## 定位（诚实边界）

"让模型有审美" = **优秀案例库 → 提炼视觉原则 → style tokens → 候选方案 → 独立 critic 打分/指路 → QA → 人工目检 → 固化规则**——不是训练稳定主观审美。本 critic：**只观察/判断/提修改/复核，不改数据、模型、统计与结论**；结论只用三值 `PASS / PASS_WITH_LIMITATION / FAIL`，**禁止无依据的"美学分数"**（如"美观度 97"）。

## 审查输入（按序）

1. 渲染原尺寸 → 缩印版（89mm）→ 灰度版；2. 统一 contact sheet（跨图横向比较：字体一致性/颜色是否跳出全文/密度/留白/PPT 感/层级强弱/箭头混乱度）；3. `scripts/visual_metrics.py` 的确定性指标（**辅助定位，不是判决**）。

```bash
python scripts/visual_metrics.py <png...>   # density / quadrant imbalance / colors / saturation
```

## 14 个观察维度（逐图给三值 + 具体位置）

hierarchy · balance · alignment · spacing · density · typography · color harmony · color semantics · annotation quality · visual focus · panel rhythm · shape consistency · arrow consistency · whitespace · figure-to-caption dependency（选适用维度，逐项写"哪一处、什么问题"）。

## AI 味识别清单（命中即不得因"整齐"放行）

同尺寸同距的全套框、机械居中、过度圆角、浅色卡片堆叠、装饰渐变、高饱和色块、每模块都加 icon、箭头过多、无谓阴影、大标题条、视觉权重平均无主次、过度对称、文字密度过高、"漂亮但无语义"的配色。

## 判定纪律

1. **科学含义 > 信息层级 > 可读性 > 美观**；更少的元素/更简单的箭头/更大的留白/更普通的字体换到更清楚 → 选简单方案。
2. 自动 QA 通过 ≠ 图好看；机械无缺陷 ≠ 通过审美（两层结论分开写）。
3. 结论禁止用语：looks good / nice / beautiful / professional / 基本没问题——必须替换为可审计描述（"b05 第 3 段带内公式框与说明文字基线对齐，符合层级规则"）。
4. 高价值图（路线图/框架图/摘要/机制图）允许 2–3 个**候选方案**比较（只变布局/间距/层级/注释位置，严禁变数据/模型/统计），critic 用 `PASS/PASS_WITH_LIMITATION/REJECT` + 具体原因选择。

## 训练集来源（学习视觉规律，禁止像素级模仿）

用户参考图集（见 `references/aesthetic_reference_matrix.md` 与 `figure_style_catalog.md`）、rougier 书、Matplotlib / SciencePlots / Seaborn 官方 gallery。**不学习**：Dribbble / Canva 信息图 / 营销数据图 / dashboard / BI / Pinterest 风。参考图只学规律与比例关系——不复制受版权保护的插画、不把他人数据带入 benchmark。

## 何时不用

- 机械缺陷检测 → figure-quality-gate / collision-aware-layout；字体系统 → scientific-typography；表格 → publication-table-layout。
