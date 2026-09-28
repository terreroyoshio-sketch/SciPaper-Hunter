---
name: collision-aware-layout
description: 渲染后碰撞感知布局：从真实渲染几何提取场景对象，检查 text-text/line/curve/arrow/scatter/patch-boundary/image/legend-data 多种碰撞（含 1.5pt 安全间距），并提供候选位置 + cost 函数 + leader line 的标注布局器。图内文字/公式/标签/曲线/箭头/图片遮挡问题时使用。不负责字号（scientific-typography）、不负责最终审美判断（visual-aesthetic-critic）。
---

# Collision-Aware Layout — 碰撞感知布局

## 原则

1. **渲染后按实测几何检查**，不按字符串长度猜宽度（`figure_qa` 同源护栏：视野外刻度/幽灵文字/3D 不可测均剔除）。
2. **擦边即失败**：新类别统一 1.5 pt 视觉 padding——"刚好不相交"按冲突处理。
3. **包含规则**：文字完全位于 patch/图像内部 = 有意标注（如区域名、单元格数值）→ 允许；**跨越边界** = 冲突。
4. **3D 轴跳过**（mplot3d 包围盒不可靠，以目检为准）。
5. 半透明填充（alpha<0.15）不参与 patch 检查（误差带不计遮挡）。

## 检查矩阵（`scripts/collision_engine.py`）

| 类别 | 判定 | 级别 |
|---|---|---|
| text_text | 与 gate 同标准（面积>6px² 且 >较小框 4%） | FAIL |
| text_line / text_curve / **text_arrow** | 折线段（轴内裁剪后）命中文字 bbox+pad | FAIL |
| text_scatter | 数据点落入文字 bbox+pad | FAIL |
| text_patch_boundary | 文字跨越 patch 边界（完全在内/在外不算） | FAIL |
| text_image | 文字跨越图像边界；完全压图内 → LIMITATION 待人工判断 ROI | FAIL / LIMIT |
| legend_data | 与 gate 同标准（不透明数据点入图例框） | FAIL |

```python
import collision_engine as ce   # 需 figure_qa 在 sys.path（由 figure-quality-gate 提供）
rep = ce.check(fig); print(ce.counts(rep), ce.fail_lines(rep), ce.limitation_lines(rep))
```
**已集成进 `figure-quality-gate`**：跑 gate 自动带全部碰撞类别。

## 标注布局器（`scripts/annotation_layout.py`）

适用于**局部标签**（散点/点位/曲线标签）：候选位置 = 原位 + 8 方向 × 3 半径（偏移点 pt），cost = 碰撞罚分 + 画布/轴边界罚分 + 距离罚分；贪心放置，先放的成为后放的障碍；超出阈值自动加**细 leader line**（0.5 pt，灰）。

```python
from annotation_layout import place_labels
place_labels(fig, ax, [{"text": "A", "xy": (2.0, 3.5)}, ...], fontsize=8.0)
```

## 硬性禁止（防"为无重叠而变丑"）

- 不允许把标签一律扔到图外、几十条 leader line、标签远离数据、图例永远最右、大量留白换零碰撞。
- leader 不得穿过其他文字/marker，不造成大量交叉。
- 文字背景只允许极淡 halo / path effect；禁止大白框盖数据。
- 复杂流程图 / 机制图 / 公式布局：**不得**依赖自动避让（adjustText 定位为辅助层；本环境未安装，布局器仅覆盖简单情形）。

## 何时不用

- 排版字体问题 → scientific-typography；表格 → publication-table-layout；最终视觉判断 → visual-aesthetic-critic。
