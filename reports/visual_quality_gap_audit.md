# 视觉质量能力缺口审计（Visual Quality Gap Audit）

2026-09-28 · 只读审计（复核时点：能力升级前）· 逐题回答 + 事实证据

## A–P 逐题回答

| # | 问题 | 事实（升级前） | 证据 |
|---|---|---|---|
| A | 字体由谁控制？ | 仅 2 个控制点：`trd_kit.apply_style` 与 `bench_common.apply_house_style`，硬编码同一 FONT_STACK | grep（本轮） |
| B | fallback 可检测？ | **否**——无 findfont/缺字告警检查；matplotlib 静默 fallback | grep（无 match） |
| C | 中英文分别配置？ | **否**——单一混合栈 | 同上 |
| D | 数学字体与正文一致？ | **否**——未设 `mathtext.*`，默认 dejavusans | grep `mathtext` 无 match |
| E | font weight 是否滥用？ | 无成文规则（band 标题/徽章/panel label 用 bold，未 token 化） | SKILL 复核 |
| F | 字号只是 ≥8pt 还是有层级？ | 升级前：仅下限；panel 9 与其余 8/8.5 未 token 化 | gate SKILL |
| G | annotation 位置如何确定？ | 全部硬编码坐标；无候选 cost 机制 | bench/trd 源码 |
| H | text-line overlap 真检查？ | **否**（列为盲区） | gate SKILL 盲区清单 |
| I | text-image overlap 真检查？ | **否** | 同上 |
| J | arrow-text overlap 真检查？ | **否** | 同上 |
| K | 只靠 adjustText？ | adjustText **未安装未使用**（README 级学习：迭代调整、启发式非保证） | pip show 空 |
| L | Word 表格区分 table/paragraph alignment？ | **不区分**——既有 `check_docx_structure.py` 只查标题层级/空单元格/深色表头，无 tblPr 几何检查 | 文件通读 |
| M | 三线表宽度由什么决定？ | **无任何决策逻辑**（项目无三线表构造器） | grep `three_line/三线表/tblBorders` 无 match |
| N | 是否存在 aesthetic review？ | **无**（只有机械 gate + 人工目检） | 体系复核 |
| O | 是否有 contact-sheet 横向审查？ | 有统一格子 contact sheet（机械）；**无**横向审美规则 | run_all |
| P | 是否有"全居中"机械规则？ | 无此规则，亦无"元素对齐语义"成文规则 | — |

## 设计结论（落到本轮的共享视觉层）

```
scientific-figure-router
   └── shared visual system
        ├── scientific-typography      （tokens / CJK-Latin 分治 / math / fallback 检测）
        ├── collision-aware-layout     （scene objects / 多类碰撞 / 候选位置 / leader / halo）
        ├── publication-table-layout   （三线表 / XML+渲染双链 QA）
        └── visual-aesthetic-critic    （视觉指标 / 观察维度 / contact-sheet 横向审查）
                 ↓ 全部汇入
        figure-quality-gate（统一三值门禁）
```

## 学习阶段事实（S1 结果）

- **文件级学习完成**：python-docx 表格 API 文档（Table.alignment 语义、autofit 行为、EMU 列宽）、adjustText README（迭代式避让、定位为辅助）、great-tables README（header/stub/spanner 组件层级）。
- **未完成（S1 时点）**：rougier 书代码（api.github.com 403）、SciencePlots 样式文件（raw 404 ×3 路径/分支）——当时记录为原则级学习，不冒充代码级学习。
- **[2026-09-28 补记]** 上述两项已于同日补读完成：改用深克隆（`git clone --depth 1`，书仓 `--filter=blob:none --sparse`）读 rougier `code/` 10 文件 + SciencePlots 3 样式文件；分级列已升级为"已文件级"。本条保留 S1 原始记录，升级事实以 `references/aesthetic_reference_matrix.md` 与 `reports/visual_quality_upgrade_20260928.md` 为准。
- 依据：见 `references/aesthetic_reference_matrix.md` 的证据分级列。

## 本审计后的修订（完成态）

A–P 全部由新共享层覆盖：字体 tokens+fallback 检测（A–F）、候选位置引擎与全类别碰撞（G–K）、三线表四层分离与渲染实测（L–M）、critic 与 contact-sheet 规则（N–O）、对齐语义成文（P：单元格对齐按语义 + 表级居中分离）。
