# 科研视觉质量升级总报告（Scientific Visual Quality Upgrade）

2026-09-28 · 范围：**四项横向能力**（不新增图型）· 未安装任何新依赖 · 未 commit / 未 push / 未更新 registry
证据等级用语遵循用户级 `evidence-levels.md` 阶梯；结论仅用三值。

---

## 0. 边界声明（先说不能做的）

| 约束 | 执行情况 |
|---|---|
| 禁止安装新依赖 | **遵守**——adjustText / SciencePlots / great-tables 仅"学习"（README/文档级），`pip show` 验证未安装 |
| 不 commit / 不 push / 不更新 registry | **遵守**——工作区保持 dirty；r3 patch 仅为文本快照 |
| 不覆盖原始图件/数据 | **遵守**——b01–b12 为增量修改（同路径重生成）；原 4 张参考图未动；trd demo 为同版本重生成 |
| adjustText 自动避让当决策器 | **未采用**——引擎为自研 cost 候选位置器（adjustText 官方 README 自述 heuristic 非保证，本报告将其定位为辅助层） |
| 学习源真实性 | rougier 书代码与 SciencePlots 样式文件**已于 2026-09-28 补读（深克隆本地逐文件）**：`git clone --depth 1`（书仓加 `--filter=blob:none --sparse`）到 `~/.claude/reference/`，读 rougier `code/` 10 文件 + SciencePlots 3 样式文件；早期 api 403 / raw 404 的"原则级"标注已按事实升级为文件级（矩阵与规则库同步更新）。克隆为只读学习，不安装、不 import、不复制代码正文、不入交付包 |

## 1. 交付物总表（四项能力）

| 能力 | Skill | 核心脚本 | 接入点 |
|---|---|---|---|
| 字体系统 | `.claude/skills/scientific-typography/` | `scripts/typography.py`（tokens / CJK-Latin 分治 / mathtext custom / 缺字探测 smoke） | `trd_kit.apply_style`、`bench_common.apply_house_style` 均改为调用它（单源） |
| 碰撞感知布局 | `.claude/skills/collision-aware-layout/` | `scripts/collision_engine.py`（6 类碰撞）、`scripts/annotation_layout.py`（候选位置 + cost + leader + halo） | `figure-quality-gate/scripts/figure_qa.py` 懒加载集成（report 增 `collisions` 段） |
| 出版级三线表 | `.claude/skills/publication-table-layout/` | `scripts/three_line_table.py`（构造）、`scripts/table_qa.py`（XML+渲染双链 QA） | 独立；产出 docx→pdf→度量 |
| 视觉审美审查 | `.claude/skills/visual-aesthetic-critic/` | `scripts/visual_metrics.py`（密度/象限均衡/颜色数/饱和度） | 独立；横向 contact sheet 规则 |

统一路由：`scientific-figure-router` → 家族 skill → **`figure-quality-gate`**（机械缺陷门禁，含新碰撞段与 fail-closed 字体门）。

## 2. 用户要求执行序 → 实际执行 → 证据

| # | 要求步骤 | 达成 | 证据（文件） |
|---|---|---|---|
| 1 | 只读审计 | ✓ | `reports/visual_quality_gap_audit.md`（A–P 16 问逐题+证据） |
| 2 | GitHub/MCP 学习 | ✓（含补读） | `references/aesthetic_reference_matrix.md`（学习来源分级 + do_not_copy 列）；rougier 10 文件 + SciencePlots 3 样式已文件级 |
| 3 | 缺口审计 | ✓ | 同上 A–P 表 |
| 4 | 审美规则 | ✓ | `references/scientific_visual_aesthetics.md`（A–N 规则，定义/失败/正确处理/自动检查/人工判断） |
| 5 | typography | ✓ | skill 目录；smoke 双断言见 §3.4 |
| 6 | collision layout | ✓ | skill 目录；三处根因修复见 §4 |
| 7 | 三线表 | ✓ | skill 目录；TABLE01–05 见 §3.3 |
| 8 | aesthetic critic | ✓ | skill 目录 + `reports/visual_aesthetic_review.md` |
| 9 | T01–T04 + TABLE01–05 | ✓ | `benchmarks/visual_quality/out/`、`benchmarks/table_family/out/` |
| 10 | 回归（旧基准不退化） | ✓ | b01–b14 全量重跑见 §3.1 |
| 11 | contact sheet 横向审查 | ✓ | `benchmarks/figure_families/out/contact_sheet.png`（14 图统一格）+ 横向结论在审美报告 |
| 12 | 人工视觉审查 | ✓ | 审美报告逐图 14 维度表；b07 终版全尺寸专门复核 |
| 13 | Git diff | ✓ | `reports/final_git_diff_r3.patch`（95775 行，含排除清单） |
| 14 | 报告 | ✓ | 本文件 |

## 3. 验证证据（全部为实际运行结果）

### 3.1 图件基准回归 14/14
`benchmarks/figure_families/out/summary.json`：**13 PASS + 1 PASS_WITH_LIMITATION**（b12：2 处 3D 投影文本 bbox 不可测 → 目检强制，非缺陷）。
新增 b13（graphical abstract：场景叙事 + 流程 + 2 内嵌小图）、b14（PyVista 3D 主路径 + matplotlib 合成）均 **PASS**；b06 回流虚线、b08 图例外置+比例尺、b09 布局、b10 回路闭合均已按 C4 子项修正并复验。
接触表：`out/contact_sheet.png` 14 格均匀、无跳色。

### 3.2 碰撞感知 T 套件 7/7 预期命中
| case | 期望 | 实得 | 证据冲突数 |
|---|---|---|---|
| t01_typography | PASS | PASS | 全 0 |
| t02_before | FAIL | FAIL | text_line=2（'Cyclic A' 等） |
| t02_after | PASS | PASS | 全 0 |
| t03_before | FAIL | FAIL | text_text=1 + text_scatter=2（'Site-042'） |
| t03_after | PASS | PASS | 全 0 |
| t04_before | FAIL | FAIL | text_text=1 + text_line=2（'Transition pathway'） |
| t04_after | PASS | PASS | 全 0 |

before=FAIL / after=PASS 全部达成；**未通过放宽阈值达成**（见 §4 根因）。

### 3.3 三线表 TABLE01–05 5/5 PASS（渲染实测）
| 表 | center_error | 表宽/版心 | 页数 | 表头重复 |
|---|---|---|---|---|
| TABLE01_short | -0.00mm | 62.5/152.4mm（短表不撑满） | 1 | — |
| TABLE02_wide_numeric | -0.00mm | 120.1/152.4 | 1 | — |
| TABLE03_long_text | -0.00mm | 138.9/152.4 | 1 | — |
| TABLE04_mixed_cn_en | -0.00mm | 101.8/152.4 | 1 | — |
| TABLE05_multipage | +0.02mm | 106.7/152.4 | 2 | ✓（第 2 页规则线 3/3） |

门槛 ≤1.0mm；实测最大 0.02mm。渲染链 = LibreOffice headless → pdfplumber 线宽/线长过滤 → 表 x 范围 vs 版心中心。

### 3.4 字体 smoke 双断言
`benchmarks/visual_quality/out/t01_fonts/font_smoke_test.*`：
- `clean_ok=True`（干净样本零告警——检测器不误报）
- `detector_caught_gap=True`（人工植入 U+2082 ₂ / U+207B ⁻，捕获 "Glyph missing from Microsoft YaHei"——检测器能抓）
- `fallback_status=NOT USED`（sci-sans：Microsoft YaHei 首选 + Arial 数学；rendered 无静默回退）
- 规则产物：上下标必须走 mathtext（YaHei 无 Unicode 下标字形）。

### 3.5 单元测试与机械门禁
`pytest .claude/skills/figure-quality-gate/scripts/test_figure_qa.py` **7/7 PASS**（含假禁用字体样本 → font_problems fail-closed；b07 风格真实擦边样本 → 检出）。

### 3.6 产物清单核验
`benchmarks/verify_artifacts.py` → `reports/benchmark_artifacts_manifest_r3_20260928.csv`：
**174 文件**（figure out 101 = 期望 101、visual_quality out、table out、typography smoke），**0 零字节、0 缺失、0 不可读 PNG**，逐文件 sha256。VERDICT: PASS。

## 4. 三处根因修复（记录以防回归）

1. **Annotation bbox 膨胀**——`Annotation.get_window_extent` 联并 leader 箭头，同字号文本框高 16px vs 31px。修复：`figure_qa.text_bbox()` 用基类 `Text.get_window_extent`。**教训：碰撞检查取自 bbox 必须在正确的类层级取。**
2. **FancyArrowPatch 幽灵线段**——`get_path()` 为数据空间且含 CLOSEPOLY 尾点 (0,0)，未过滤时在数据空间画出一条(0,0)出发的幻影线，误报 text-arrow 碰撞。修复：codes 过滤 0/79 + `get_transform()` 变换。
3. **缺字探测自证**——若只跑干净样本，检测器"永远绿"不可信。修复：smoke 改为双断言（clean + gap 双通过才算检测器有效）。

设计性修复（非阈值放宽）：t02/t03 after 案例经 radii 扩至 58pt、placed-label 罚 24、own-anchor 净空 +15、点罚 8→14、mark-before-place 时序修正后通过——即"候选位置器真的找到了不重叠的合法位置"，而非放低门槛。

## 5. 第 25 条规则遵守说明（不得为无重叠制造难看图）

- **halo 的合法地位**：b09 网络图标签用 `withStroke` 白边——密集网络场景的合法保护，引擎将其列为豁免而非缺陷；不为清零碰撞数把标签全赶出图外。
- **b07 修复的是真擦边**：本轮因此暴露 3 处箭头—文字净空 <0.5mm 的真实近距（rain/sun/Energy label），修的是真实可读性风险，修后全尺寸目检通过。
- **b13/b14 平衡项只给建议不给强制**：quadrant imbalance 0.86 记录为 PWL + 具名可操作项（增强右上小图组 或 收缩左下地面带，二选一），不强制对称、不为了指标好看破坏叙事。
- **b04/b05 灰度冗余为 PWL 而非 FAIL**：只在"目标期刊要求灰度可辨"时触发处理，避免为灰度牺牲彩版语义。

## 6. 审美审查结论（两层分离）

1. 机械层：14/14 通过（13 PASS + 1 PWM b12）、T 7/7、TABLE 5/5、pytest 7/7——未检出已定义机械缺陷。
2. 审美层（`reports/visual_aesthetic_review.md`）：**PASS_WITH_LIMITATION**——无 FAIL；5 处 PWL 均具名（b04/b05 灰度冗余、b08 几何诚实留白带、b12 3D 文本、b13/b14 平衡），无"looks nice"式空判。

## 7. 已知限制与未完成项

| 项 | 状态 | 说明 |
|---|---|---|
| rougier 书 / SciencePlots 文件级学习 | **DONE（2026-09-28 补读）** | 深克隆读 13 文件（书 10 + 样式 3）；新增文件级证据：四级可读阶梯参数、引线 halo/锚点排序、直标优先梯、IEEE 颜色×线型双编码、Nature 7pt 惯例；矩阵"原则级"行已升级。读前核对许可（SciencePlots=MIT；书仓逐文件混杂 BSD/CC BY-NC-SA/CeCILL），只提炼规律不复制代码 |
| text_image 碰撞 | LIMITATION | 仅报边界越界 + 强制人工判 ROI——不做自动"压了关键区域"判断 |
| b12 3D 文本 | LIMITATION | mplot3d 投影文本不可测，目检兜底；主路径 b14（PyVista）无此限制 |
| `metrics_out/`、`outputs/_diag/` | 诊断副产物 | 探测阶段生成，未纳入 r3 包；如需清理将先列清单再确认 |
| Git 状态 | dirty（预期） | 用户授权范围内不 commit |

## 8. 证据等级（用户级阶梯）

| 能力 | 最高等级 | 依据 |
|---|---|---|
| 四处 skill 文件存在且可导入 | STATICALLY_VERIFIED | import + pytest |
| 碰撞引擎/T 套件/表 QA/字体 smoke | RUNTIME_VERIFIED | 本机实际运行 + 真实输出 + 退出码 0 |
| 图件 14 基准全链（生成→gate→contact sheet） | RUNTIME_VERIFIED | `run_all.py` 全量运行 |
| 表渲染度量（LibreOffice→pdfplumber） | RUNTIME_VERIFIED | TABLE01–05 实测 |
| 集成到真实任务 | NOT YET VERIFIED | 需在下一篇真实论文图件中走一遍 |
| 从全新检出重建 | NOT YET VERIFIED | 未 commit，尚无干净检出可测 |

## 9. 下一步最小动作

1. 用户在 WPS/本地对 TABLE 系列 docx 做一次人工目检（保真确认）。
2. 在真实论文或申报书任务里走一遍 router→家族→gate 全链，验证 INTEGRATION_VERIFIED。
3. 如收录：按项目惯例 commit（本次未获授权，未执行）。
