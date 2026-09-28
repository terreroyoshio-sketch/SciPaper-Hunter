---
name: scientific-typography
description: 科研图字体排版系统：字体 tokens（中英/数学分治）、字号层级、字重纪律、fallback 与缺字检测（font_smoke_test）。任何图件排版、字体不统一、中文缺字方框、公式字体不一致时使用。不负责具体绘图（走各家族技能）、不负责碰撞检查（走 collision-aware-layout）。
---

# Scientific Typography — 科研字体系统

**单一来源**：所有图件字体/字号/数学字体从 `scripts/typography.py` 的 tokens 取；禁止各脚本自行定义字体栈。

## 字体选择顺序（硬规则）

1. 论文 / 学校 / 期刊模板明确指定 → 从模板。
2. 正文当前字体 → 从正文继承。
3. 安全 fallback（下表）——**Fallback status 必须报告**。

| token | 首选 | 后备 |
|---|---|---|
| latin_sans | Arial | Helvetica / Liberation Sans / DejaVu Sans |
| latin_serif | Times New Roman | Liberation Serif / DejaVu Serif |
| cjk_sans | Microsoft YaHei | SimHei / Noto Sans CJK |
| cjk_serif | SimSun | Noto Serif CJK |

- **只使用系统已安装字体**；禁止下载字体文件、禁止硬编码个人机器字体路径。
- **禁止无意混搭**：同一张图不得出现"中文宋体 + 英文 Calibri + 公式 Computer Modern + 图例 DejaVu"。

## 中英混排（matplotlib 约束的诚实处理）

matplotlib 每个文本对象只解析**一种**字体（无逐字形 fallback）。因此：

- 全局默认采用**双语安全栈**（`sci-sans`：中文字体在前，同时覆盖拉丁）；纯英文图可用 `sci-latin`；中文论文用 `sci-serif`（SimSun 在前）。
- **纯拉丁字符串**（数字、英文标签）需要期刊拉丁字体时，用 `typography.text_style(s)` 显式返回字体——含 CJK 的字符串必须走 CJK 字体（否则方框）。

## 字号层级（不是只设最小值）

| 层级 | token | 默认（pt） |
|---|---|---|
| 面板标签 (a/b/c) | panel_label | 9.0 |
| 轴标签 | axis_label | 8.5 |
| 图例 / 刻度 | legend / tick | 8.0 |
| 注释 | annotation | 8.0 |
| 次级注释 | minor_annotation | 8.0（SCI 下限约束，不得更低） |

关系：panel > axis ≥ legend ≈ tick ≥ annotation。**禁止为了塞内容把字号降到 8 pt 以下**（venue override 需记录依据）。

## 字重纪律

bold 只用于一级信息：面板标签、阶段/分区标题、编号徽章、关键结果。正文注释一律 regular；禁止"所有标题都粗体 / 所有节点都 bold"。

## Fallback 与缺字检测（不得静默通过）

```bash
python .claude/skills/scientific-typography/scripts/typography.py <outdir>
# → font_smoke_test.pdf/.png + JSON：resolved fonts / fallback_status / font_warnings / missing_glyph_detected
```

`figure-quality-gate` 已内建同源检查：渲染期捕获 `findfont` / `Glyph ... missing` 警告 → FAIL（不得因为 matplotlib 沉默 fallback 就判 PASS）。

## 可审计报告格式（交付时必写）

```
正文英文：Times New Roman ｜ 图中文字：Arial ｜ 中文：Microsoft YaHei ｜ 数学：Arial(custom)
原因：论文模板要求 / 正文继承 / 安全 fallback
Fallback: DejaVu Sans
Fallback status: NOT USED
```

## 何时不用

- 数据图的外置排版（Word/LaTeX 层）→ 不属本技能。
- 表格字体（DOCX）→ publication-table-layout。
