---
name: figure-quality-gate
description: 科研图件统一验收门：对已生成的 matplotlib 图件执行三值状态（PASS/PASS_WITH_LIMITATION/FAIL）自动检查——文字重叠、最小字号、文字越界、灰度版、单栏缩印预览、PDF 页面尺寸与字体嵌入——并产出验收报告。任何图件声明"完成"前必须过本门。不负责绘图本身。
---

# Figure Quality Gate — 图件统一验收门

定位：**统一口径**。具体检查复用既有实现（figurelab QA、scipilot visual_qa、technical-route-diagram 的 qa_layout）；本门提供通用检查器与三值判定。

## 验收流程（缺一不可）

1. **自动检查**：`scripts/figure_qa.py`（见下）——文字重叠 / 最小字号 / 文字越界 / PDF 页面与字体 / 灰度版 / 缩印预览。
2. **目检 ≥1 轮**：打开成图逐项看——箭头指向、图例语义、对齐、缩印版（`*_print89mm.png` 按 100% 查看）、灰度版。
3. **三值结论**：`PASS` / `PASS_WITH_LIMITATION` / `FAIL`，写入报告。**禁止用语**：looks fine / probably okay / 基本没问题 / 应该可以。

## 自动检查项与阈值（2026-09-28 修正版）

| 检查 | 阈值 | 级别 |
|---|---|---|
| 文字-文字重叠 | 交叠面积 >6 px² 且 >较小框 4% | FAIL |
| 最小字号 | **SCI 默认 ≥8 pt**（单一来源 `figure_qa.DEFAULT_MIN_PT`）；venue override 需显式 `--min-pt` 且报告记录 `threshold_source=override` | FAIL |
| 文字越界 | 出画布 >1 px | FAIL |
| **图例压数据（legend-data）** | 不透明数据点落入图例框：collection ≥5 点且占比 ≥2%，或 line ≥8 点（alpha<0.5 的半透明填充不计） | FAIL |
| **边距（margin）** | 文字/图例距画布边缘 <0.5 mm（FAIL）；<1.5 mm（LIMITATION）——兼作 clipping/贴边检查 | FAIL / LIMIT |
| **布局均衡（balance）** | 单轴数据点全幅/核心(5–95%)面积比 >4（稀疏外围/核心压缩）；3D 轴跳过 | FAIL |
| PDF 字体 | **fail-closed**：parser 错误 / font-entry 错误 → FAIL；非嵌入字体（Base14 除外）→ FAIL；Type3 视为已嵌入（字形内联在 /CharProcs） | FAIL |
| 缩印预览 / 灰度版 | 生成 `*_print89mm.png` / `*_grayscale.png` | 人工判读 |
| 文字-线/箭头遮挡 | 自动检查不覆盖 | 目检必查 |

回归测试：`scripts/test_figure_qa.py`（pytest，7 用例：双字体模式 PDF、fail-closed、图例冲突检出与空角不误报、均衡检出、8pt 阈值强制）。

## 结构性护栏（防误报，2026-09-28 实测校准）

- **幽灵刻度文字**：matplotlib 会保留 `axis("off")` 与视野外刻度的 Text 对象（`axison=False`、`tick.get_loc()` 在视图区间外）——它们不被渲染，检查器已自动剔除（刻度标签对象没有 `.axes` 属性，必须按轴枚举识别）。
- **3D 投影**：mplot3d 的刻度/轴标签经 3D 变换后 2D 包围盒不可靠（可能落在 ±10⁴ px），此类文字计入 `LIMITATION`（"unmeasurable"）而非 FAIL——**3D 图件的文字检查以目检为准**。
- **重复绘制对象**：同一字符串且包围盒完全重合的多个 Text（同一视觉标签被画两次）按一个处理。

> 已知盲区（必须目检兜底）：箭头压字、数据点遮挡、贴边裁剪（渲染宽度可能略大于测量值，边距请留 ≥1%）、3D 图件文字。technical-route-diagram 开发中自动检查全 PASS 时目检仍抓到过条形图标签与盒子重叠；本 benchmark 调优中目检又抓到"贴边截字"（测量在界内、渲染裁掉尾字符）——**目检不可省**。

## 用法

```bash
# CLI：builder 模块需暴露 build() -> matplotlib.figure.Figure
python .claude/skills/figure-quality-gate/scripts/figure_qa.py \
  --builder <module.py> --out <outdir> [--name fig1] [--min-pt 8]
# 退出码：0 = PASS / PASS_WITH_LIMITATION；1 = FAIL
```

```python
# 代码内调用（benchmark / 绘图脚本尾部）
from figure_qa import run_gate
report = run_gate(fig, outdir, name="fig1", min_pt=6.5)
```

产出：`<name>.pdf/.svg/.png`、`<name>_grayscale.png`、`<name>_print89mm.png`、`<name>_gate.json`、`<name>_gate.md`。

## 与其它 QA 技能的关系（去重约定）

- `figurelab-publish` / `scipilot-figure-skill`：承载具体图件流水线 QA —— 保留，本门不重复其内部检查。
- `technical-route-diagram` 的 `qa_layout.py`：结构化元素级检查 —— 保留；本门是**跨家族统一层**。
- 数据正确性（伪造数据、显著性标注）由 `figure-data-integrity-auditor` 与反造假规则负责；本门只管视觉与交付形态。

## 何时不用

- 图件尚在探索阶段（草图、内部讨论用）→ 不强制。
- 用户明确说"只看个大概" → 免 gate，但不得进入投稿/申报包。
