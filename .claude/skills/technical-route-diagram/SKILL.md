---
name: technical-route-diagram
description: 生成可复现的科研技术路线图/方法流程图（分区带、步骤徽章、功能配色、内嵌真实数据小图），输出 SVG/PDF/PNG 并附自动布局 QA 与灰度检查。触发词：技术路线图、方法流程图、方法论示意图、methodology flowchart、technical route diagram、论文方法图重绘。不适用于纯数据图表、PPT 制作、交互式图表。
---

# 技术路线图（Technical Route Diagram）

把论文方法拆成 3–5 个步骤/带，渲染为可复现的矢量技术路线图。版式范式（四步横带、五带竖版、多栏框架、多面板 a/b/c）来自对 SCI 论文方法图的归纳与开源技能生态的模式提炼（见"参考与致谢"）。

## 何时用 / 不用

- **用**：论文/学位论文/申报书的方法论流程图、技术路线图；需要把方法步骤 + 内嵌结果小图排到一张矢量图里；需要可复现脚本而非手绘。
- **不用**：纯数据图表 → figurelab；PPT 演示 → ppt-master；单张框图/示意图（无步骤带结构）→ nature-figure-style 的 architecture_diagram 规则；交互图表 → plotly 类工具。
- **上游衔接**：技术路线逻辑尚未成型时，先用 `technical-route-blueprint-planner` 产出文本蓝图（泳道/输入-过程-输出映射），再把蓝图填进本技能的 `content.json`。

## 硬规则

1. **mm 画布**：1 数据单位 = 1 mm 实际印幅（`trd_kit.Canvas`）。字号按 pt 直接对应最终印刷尺寸，尺寸预算不靠猜。
2. **网格先行，布局先于连线**：先定带高/列基线/步距，同族元素同宽同距，再放形状和箭头。
3. **一号一色族**：每步一个编号徽章；功能配色 5 族（input / process / method / result / accent），色块语义必须进图例。
4. **内嵌小图必须真实**：小图数据来自 source_data 文件；演示/占位内容必须带 `PLACEHOLDER` 标记，且**不得用于投稿/申报**。
5. **字号下限**：正文标签 ≥ 6.5 pt（< 6 pt 直接 FAIL）。像素画布缩到 A4 正文宽会掉到 ~6.5 pt，务必按最终尺寸设计。
6. **箭头即语义**：主链单一方向；每条箭头要说得出来含义；不用无法解释的斜线连接。
7. **中文宽度模型**：全角 ≈ 字号 × 0.353 mm，半角 ≈ 一半；QA 用估算法查文字溢出，目检兜底。
8. **灰度与目检**：导出含灰度版；自动 QA 跑完后必须**目检 ≥ 2 轮**——自动检查抓不到坐标轴标签溢出、箭头压字这类问题（本技能开发过程中自动 QA 全 PASS 时目检仍抓到过 1 处标签重叠，已修复）。

## 工作流

1. **内容清单**：编辑 `templates/four_step_bands/content.json`——带标题、盒子文本与色族、内嵌图类型、图例、页脚标记。几何常量在 `make_figure.py` 顶部调。
2. **渲染**：
   ```bash
   python .claude/skills/technical-route-diagram/templates/four_step_bands/make_figure.py --out <outdir>
   ```
3. **自动 QA**：`qa_layout.py` 输出 PASS/WARN/FAIL 三值状态 + `qa_report.md/.json`；FAIL 时退出码 1。
   - FAIL 项：越界、实体块重叠、容器重叠、字号 < 6 pt、估算文字溢出
   - WARN 项：字号 < 6.5 pt、灰阶明度对差 < 0.05
4. **目检 ≥ 2 轮 + 灰度目检**：重点查坐标轴标签、箭头指向、同族对齐、数字抄录。
5. **交付**：SVG（可编辑主件，文字保持 `<text>`，Illustrator/Inkscape 可改）+ PDF（矢量投稿件，字体嵌入）+ PNG 600 dpi + 灰度 PNG + QA 报告 + 复现命令。

## 文件地图与扩展

| 文件 | 作用 |
|------|------|
| `scripts/trd_kit.py` | 基元库：`band / box / arrow / block_arrow_down / plot_slot / legend / text / export`；元素自动登记供 QA |
| `scripts/qa_layout.py` | 布局 QA（启发式；非渲染级检测） |
| `templates/four_step_bands/` | 四步横带模板（content.json + make_figure.py） |

新模板 = 复制 `templates/four_step_bands/` 改布局常量与绘图函数。版式参考模式：四步横带（本模板）、五带竖版（问题 → 数据指标 → 方法机制 → 结果对比 → 评估推广）、三栏框架、多面板 a/b/c（数据层级色族 + 图例）。

## 反造假约束

- 图中一切数字/曲线必须来自真实数据文件；统计标注（p 值/显著性）必须有分析输出支持，无依据不得标注。
- 本模板自带的演示数据为合成数据，且带 `PLACEHOLDER` 页脚标记；**替换为真实内容前不得删除标记**。
- 演示图不得用于任何投稿、申报或对外材料。

## 参考与致谢（模式来源，未复制任何代码）

- 本机 `nature-figure-style`：matplotlib 框图骨架与配色思路（MIT 系）。
- `jihe520/sci-box`（**无许可 → 仅提取模式**）：网格先行、中文宽度模型、连接线走廊、排版检查脚本思想。
- `QIANJINYDX/research-drawio-skill`（**无许可 → 仅提取模式**）：契约先行、"图是视觉论证"、语义字模思想。
- `0xE1337/thesis-figure-skill`（MIT）：编译前后重叠检测与多轮审查清单的思路。

本技能为独立实现。

## 局限（诚实声明）

- v1 仅四步横带一个模板；其余版式需用基元自行搭建（未模板化）。
- 自动 QA 为启发式估算（文字换行按字符宽度模型、灰阶按明度矩阵），不是渲染级检测；坐标轴标签溢出等盲区靠目检。
- SVG 文字依赖打开端安装 Microsoft YaHei / Arial 等字体（本机 Windows 已具备）。
- 无自动布局优化（无力导向/自动布线）；布局由模板常量控制。
