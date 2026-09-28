# FINAL EVIDENCE FREEZE — 科研制图能力体系（2026-09-28）

- **总体状态：`PASS_WITH_LIMITATION`**（分项见 §11；限制原因见文末「总体限制」）
- **范围声明**：本轮为**只读复核与证据整理**。未修改任何 Skill / benchmark / DOCX / Python 源码 / 已有输出；未 commit、未 push、未更新主仓库注册表。仅新增 3 个证据文件（本报告、`final_git_diff.patch`、`benchmark_artifacts_manifest_20260928.csv`）。
- 分支：`claude/jolly-austin-91e98e` · 基线 HEAD：`f65b117abb190214dae07c2270dbe12ae0b4c191`
- 复核方式：全部结论来自本机实际命令的 stdout/stderr 与文件哈希；本报告不含无证据的"已完成"类描述。

---

## §1 Git 基线 — 状态：`PASS`

### 1.1 基线命令（verbatim）

```
$ git rev-parse HEAD
f65b117abb190214dae07c2270dbe12ae0b4c191

$ git status --short   （21 个条目）
 M .claude/skills/technical-route-diagram/SKILL.md
?? .claude/skills/engineering-schematic/
?? .claude/skills/figure-quality-gate/
?? .claude/skills/geospatial-figure/
?? .claude/skills/graphical-abstract/
?? .claude/skills/mechanism-schematic/
?? .claude/skills/multipanel-compositor/
?? .claude/skills/network-topology/
?? .claude/skills/scientific-3d/
?? .claude/skills/scientific-figure-router/
?? .claude/skills/scientific-flowchart/
?? .claude/skills/scientific-method-framework/
?? benchmarks/
?? outputs/install_smoke_20260928/
?? references/
?? reports/benchmark_artifacts_manifest_20260928.csv
?? reports/docx_patch_20260928.py
?? reports/docx_patch_log_20260928.md
?? reports/existing_figure_capabilities.md
?? reports/figure_capability_build_20260928.md
?? reports/final_git_diff.patch

$ git diff --stat        （仅已跟踪文件）
 .claude/skills/technical-route-diagram/SKILL.md | 9 +++++++++
 1 file changed, 9 insertions(+)

$ git diff --stat        （含 intent-to-add 的完整视图）
 122 files changed, 82595 insertions(+)
```

### 1.2 完整 diff 与索引还原验证

- 完整 diff 已保存：`reports/final_git_diff.patch`（**83,538 行 / 2,917,229 B**；体积主体为 `b12.svg` 的 71,870 行）。
- **方法披露**：为使新增（untracked）文件进入 `git diff`，使用了 `git add -N`（intent-to-add）→ 生成 patch → `git reset` 还原索引。**工作树文件未被改动**。
- 还原验证（verbatim）：

```
$ git diff --cached --stat
（空）
$ git status --porcelain | grep -v '^??'
 M .claude/skills/technical-route-diagram/SKILL.md
```

- 结论：索引已还原为与冻结前一致（唯一非 `??` 条目为既有修改 `trd SKILL.md`，未 staged）。条目数 19→20→21 的两次 +1 分别为：本冻结任务新增的 manifest CSV 与 patch 文件本身。

---

## §2 依赖版本 — 状态：`PASS`

```
$ python -m pip show cartopy pyvista vtk        （PIP_SHOW_EXIT=0）
Name: Cartopy    Version: 0.26.0    License-Expression: BSD-3-Clause
  Requires: matplotlib, numpy, packaging, pyproj, pyshp, shapely
Name: pyvista    Version: 0.49.0    License-Expression: MIT
  Requires: cyclopts, matplotlib, numpy, pillow, pooch, pyvista-validation, scooby, typing-extensions, vtk
Name: vtk        Version: 9.7.0     License: BSD
  Required-by: pyvista
```

- 与外部信息的交叉核对：PyVista 0.49 的依赖范围 `VTK >=9.3.1,<9.8.0` 覆盖 9.7.0——无版本冲突。

---

## §3 最小运行时检查 — 状态：`PASS`

```
$ python <runtime check>                        （无文件写出；截图经 return_img 内存返回）
cartopy: 0.26.0
cartopy transform (100E,30N -> Robinson): 9069777.574, 3208557.612
pyvista: 0.49.0 | vtk: n/a
sphere points: 1522
offscreen render array: (240, 320, 3) uint8
CHECK_EXIT 0
SHELL_EXIT=0
```

- 备注：`pv.vtk_version` 属性在 0.49 下不存在（输出 `n/a`），VTK 版本以 §2 的 `pip show` 为准。
- 早前（授权后执行时）的落盘 smoke 产物存证：`outputs/install_smoke_20260928/cartopy_smoke.png`（18,692 B）、`pyvista_sphere.png`（61,098 B）。

---

## §4 Benchmark 冻结核验（只验证、不重画）— 状态：`PASS`

核验方式：对 12×8 个文件逐一做存在性/非零/尺寸/哈希检查；缺失或空文件即 FAIL（本机无任何自动重生成）。**结果：无缺失、无空文件、无重复哈希。**

| key | gate 状态 | PNG 尺寸 | 灰度尺寸 | 缩印89mm | PDF B | SVG B |
|---|---|---|---|---|---|---|
| b01 | PASS | 4015×1417 | 4015×1417 | 2102×742 | 26,412 | 39,905 |
| b02 | PASS | 4015×1370 | 4015×1370 | 2102×717 | 32,046 | 84,192 |
| b03 | PASS | 2834×2409 | 2834×2409 | 2102×1787 | 17,236 | 33,132 |
| b04 | PASS | 4015×2362 | 4015×2362 | 2102×1237 | 34,232 | 24,673 |
| b05 | PASS | 4015×5102 | 4015×5102 | 2102×2671 | 41,424 | 52,023 |
| b06 | PASS | 2192×4619 | 2192×4619 | 2102×4429 | 14,846 | 13,572 |
| b07 | PASS | 3070×2007 | 3070×2007 | 2102×1374 | 14,036 | 10,248 |
| b08 | PASS | 2881×2220 | 2881×2220 | 2102×1620 | 22,479 | 21,993 |
| b09 | PASS | 2881×2267 | 2881×2267 | 2102×1654 | 21,248 | 47,670 |
| b10 | PASS | 3840×2880 | 3840×2880 | 2102×1576 | 13,196 | 7,556 |
| b11 | PASS | 4015×2551 | 4015×2551 | 2102×1336 | 26,787 | 49,814 |
| **b12** | **PASS_WITH_LIMITATION** | 2645×2125 | 2645×2125 | 2102×1689 | 344,161 | 2,350,607 |

- **完整性汇总**：out/ 下共 **87 个文件**（12×7 产物 + contact_sheet + summary.md/json），期望值 87 ✓；**零字节文件：无**；**重复哈希组：无**。
- **尺寸核验**：各 PNG/灰度 = 设计 mm × 600 dpi（±2 px）；缩印宽 = 2,102 px（= 89 mm @600 dpi）✓；b06/b10 画布由渲染器决定，仅记录不自证。
- **每图 gate 复核**：`min_fontsize=6.5pt`、`text_overlaps=0`、`out_of_bounds=0`（全部 12 图）。
- **b12 的 `PASS_WITH_LIMITATION` 具体限制（原文）**：`2 text extents unmeasurable (3D projection) - visual check mandatory` —— mplot3d 的轴文字经 3D 变换后 2D 包围盒不可测（属于渲染器事实，不是本图缺陷）；该图已人工目检（z 轴 labelpad 修正后无压字）。
- 逐文件哈希清单：`reports/benchmark_artifacts_manifest_20260928.csv`（87 行，path/bytes/sha256）。

---

## §5 contact_sheet.png 读取检查（只读）— 状态：`PASS_WITH_LIMITATION`

- 文件：`benchmarks/figure_families/out/contact_sheet.png`，**756,804 B**，2026-09-28 14:50。
- 读取检查：完整渲染 12 图（4 列网格）；缩略级目检**未见遮挡、截断或错位**。
- **限制（为什么不是 PASS）**：缩略级目检不能证明全尺寸级无遮挡。全尺寸级遮挡由两层证据支撑：①每图 gate 的 0-overlap（自动，见 §4）；②单图人工目检（b01/b02/b04/b05/b12 全尺寸 + 修复前后对照）。

---

## §6 DOCX 补丁核验 — 状态：`PASS`

### 6.1 双哈希（verbatim）

```
SRC_SHA256 = df979a4fa792df00a83a9a773dd863f9bc73df2a3104f6bfef8a2ffad6e87c17   （桌面\制图提示词.docx，46,607 B，与补丁前一致 → 原件零改动）
DST_SHA256 = 6c7309d32994bd719728c51d891f36da08d4e37b35f0813655f3c045c0f6c983   （桌面\制图提示词.patched_20260928.docx，42,879 B）
```

### 6.2 17 处变更逐条复核（副本内定位；样式名全部 `<Normal>`；未新增样式；全部替换的旧文本零残留）

| # | 类型 | 副本段号 | 原文摘要 | 新文摘要 |
|---|---|---|---|---|
| 01 | INSERT 文档头 | 0 | （无） | 【2026-09-28 修订副本】…修正绝对规则并同步技能列表；原件未改动 |
| 02–09 | REPLACE 技能列表 | 30–37 | `research-task-router` 等 8 项（其中 6 项全库不存在） | `scientific-figure-router` / `figure-quality-gate` / `figurelab-publish` / `academic-figure-skill` / `scientific-visualization` / `nature-figure-style` / `technical-route-diagram` / `figure-preflight-checker` |
| 10 | REPLACE §17 标题 | 608 | `## 绝对禁止传统：` | `## 禁止对象（2026-09-28 修正）：无语义模板化流程图` |
| 11 | REPLACE §17 条目 | 624 | `* 大量方框 + 箭头` | `* 无语义、模板化的方框堆叠（大量同尺寸方框 + 箭头直连）` |
| 12 | REPLACE §18 标题 | 635 | `# 十八、流程图必须采用"几何叙事"` | `# 十八、流程图规则（2026-09-28 修正）：分场景处理` |
| 13 | REPLACE §19 结语 | 717 | `视觉上不得画成传统流程图。` | `视觉上不得画成"无语义模板化"的默认流程图；本类（数学建模算法）图应优先几何叙事。` |
| 14 | REPLACE §52 验收门 | 1743 | `19. 流程图不是方框+箭头；` | `19. 流程图不得是"无语义模板化方框堆叠"（默认 Mermaid/SmartArt 风、等尺寸节点直连）；允许承担信息组织功能的语义容器 + 箭头；` |
| 15 | REPLACE §54 | 1838 | `禁止方框堆叠。` | `禁止无语义、模板化的方框堆叠（允许承担信息组织功能的语义容器 + 箭头）。` |
| 16 | INSERT-AFTER §17 条目 | 626–629 | （无） | 修正段 4 条：`（2026-09-28 修正）`、`**禁止**…`、`**允许**…`、`技术路线图与方法框架图优先…`（逐段 startswith 核对全部 True） |
| 17 | INSERT-AFTER §18 标题 | 636–637 | （无） | 分场景说明 2 条：`几何叙事（用点…）仍是数学建模类算法流程图的优先路径`、`但方法框架图、技术路线图…允许使用语义容器 + 箭头`（逐段核对 True） |

- 复核结论：**17/17 全部落位；0 未命中；替换的旧文本在副本中 0 残留**（逐条 `old_hits=[]`）。
- 复现脚本：`reports/docx_patch_20260928.py`；明细日志：`reports/docx_patch_log_20260928.md`（含每处旧文/新文全文）。

---

## §7 Skill 落地与 router 一致性 — 状态：`PASS`

### 7.1 项目级技能目录树（本 worktree `.claude/skills/`，23 个技能）

```
本轮新增 11 + 修改 1（全部 files）:
scientific-figure-router/     SKILL.md
figure-quality-gate/          SKILL.md · scripts/figure_qa.py (+ __pycache__)
scientific-method-framework/  SKILL.md
scientific-flowchart/         SKILL.md
mechanism-schematic/          SKILL.md
graphical-abstract/           SKILL.md
geospatial-figure/            SKILL.md
network-topology/             SKILL.md
engineering-schematic/        SKILL.md
scientific-3d/                SKILL.md
multipanel-compositor/        SKILL.md
technical-route-diagram/（M） SKILL.md · scripts/trd_kit.py · scripts/qa_layout.py · templates/four_step_bands/{content.json, make_figure.py} (+ __pycache__)

既有 11（未改动；均含 SKILL.md + references/agents/templates 资产，完整 find 清单见本轮终端记录）:
academic-paper · academic-paper-reviewer · academic-pipeline · agent-execution-patterns ·
ai-powerpoint-research-workflow · autonomous-survey-agent · deep-research ·
my-academic-research-master · office-productivity-workbench · research-idea-conflict-miner ·
sci-research-writing-narrative
```

### 7.2 逐技能元信息表

| Skill | 路径 | 职责 | router 触发条件 | renderer | QA gate |
|---|---|---|---|---|---|
| scientific-figure-router | `.claude/skills/scientific-figure-router/` | 总路由：判家族/载体 → 分派 → 强制过门；**不绘图** | 任何画图/重绘请求 | —（决策树） | 强制派送 `figure-quality-gate` |
| figure-quality-gate | `.claude/skills/figure-quality-gate/` | 统一验收门；`figure_qa.py` 通用检查（重叠/字号/越界/灰度/缩印/PDF 字体） | 图件声明"完成"前；显式 QA 请求 | — | **即门本身**（三值状态） |
| scientific-method-framework | 同目录 | 数据→模型→指标→结果 分层框架图 | 方法总览/框架/研究框架 | matplotlib + trd_kit | gate |
| scientific-flowchart | 同目录 | 算法 DAG（一般通道）/ 数模几何叙事通道 | 算法流程/计算流程 | graphviz 布局 → matplotlib 呈现 | gate |
| mechanism-schematic | 同目录 | 物理/生态/医学机制示意 | 机制图/原理图/schematic | matplotlib primitives | gate |
| graphical-abstract | 同目录 | 图形摘要（一句核心信息驱动） | graphical abstract/总览图 | matplotlib 复合 → SVG 二次编辑 | gate |
| geospatial-figure | 同目录 | 地图/choropleth/栅格/分区 | 地图/空间分布 | geopandas + cartopy 0.26 | gate |
| network-topology | 同目录 | 节点-边关系网络 | 网络/拓扑/关系图 | networkx + 自绘 | gate |
| engineering-schematic | 同目录 | 电路/逻辑/时序/状态机 | 电路/框图/时序 | schemdraw 0.23 | gate |
| scientific-3d | 同目录 | 3D 点云/曲面/网格/体 | 3D/点云/三维 | pyvista 0.49（兜底 mplot3d 并声明） | gate（3D 文字以目检为准） |
| multipanel-compositor | 同目录 | 多面板编排（GridSpec/统一图例/跨面板对齐） | 组图/Figure 1 总图 | matplotlib GridSpec | gate（整图一次） |
| technical-route-diagram（M） | 同目录 | 技术路线图渲染器（四步横带模板） | 技术路线图/方法论流程图 | trd_kit（matplotlib，mm 画布） | gate + 自身 `qa_layout.py` |
| 既有 11 技能 | `.claude/skills/<name>/` | 论文写作/审稿/调研/办公（非绘图） | 各自领域 | — | — |

### 7.3 router 引用一致性（自动解析 backtick 引用 → 检查三个技能根）

- 结果：**全部命中**。worktree 根：11 个家族技能 + technical-route-diagram；用户级根：academic-figure-skill / figurelab-publish / nature-figure-style / scientific-visualization / technical-route-blueprint-planner；主检出根：drawio-diagram-workbench（在另一检出，router 与能力地图已显式声明）。
- 库/工具名（matplotlib/graphviz/networkx/geopandas/schemdraw/pyvista/cartopy/shapely/pyproj/dot/seaborn）不作为技能核查。

---

## §8 异常文本检查 — 状态：`PASS`

- 对上一轮汇报中出现的词 `vuitton`（会话输出污染）做全库检索：**worktree 0 命中、记忆目录 0 命中**。确认该词未进入任何文件；如最终审计记录中出现，应按"会话输出污染、非文件内容"处理。

---

## §9 证据文件与哈希

| 文件 | 大小 | SHA-256 |
|---|---|---|
| `reports/final_git_diff.patch` | 2,917,229 B / 83,538 行 | `3ab6a75af3b4def5c8f73b06cfdcd67870ddabee88f15701a57b92fe394e5dd2` |
| `reports/benchmark_artifacts_manifest_20260928.csv` | 7,694 B / 87 行 | `9406a90977c33bc03af430988f14068b4adc3da119e62e2a2bd62020a04e67a2` |
| `benchmarks/figure_families/out/contact_sheet.png` | 756,804 B | （哈希在 manifest CSV 内） |
| `C:\Users\张涵\Desktop\制图提示词.docx`（原件） | 46,607 B | `df979a4fa792df00a83a9a773dd863f9bc73df2a3104f6bfef8a2ffad6e87c17`（补丁前后一致） |
| `C:\Users\张涵\Desktop\制图提示词.patched_20260928.docx` | 42,879 B | `6c7309d32994bd719728c51d891f36da08d4e37b35f0813655f3c045c0f6c983` |
| 本报告 | （生成后未再修改；可随时重算 sha256 核对） | — |

---

## §10 commit 前待处理事项（本冻结未执行，等待你的指示）

1. **`__pycache__` 混入**：`figure-quality-gate/scripts/__pycache__/` 与 `technical-route-diagram/scripts/__pycache__/`（共 2 目录 / 3 个 `.pyc`）——benchmark 导入产生的字节码缓存。建议第一次 commit 前删除并在 `.gitignore` 排除 `__pycache__/`。
2. **b12 大文件**：`b12.svg` 71,870 行 / 2.35 MB（3D 曲面多边形）——是否随源码入库需决定（可选：入 PDF/PNG 不入 SVG）。
3. **产物提交策略**：87 个 benchmark 产物 + 2 张 smoke 图，建议与源码分开 commit 或进 `.gitignore`。
4. **主仓库 `research-stack-index` 注册表**更新未做（属另一检出）。

---

## §11 分项状态汇总

| 分项 | 状态 |
|---|---|
| §1 Git 基线捕获 + 索引还原 | `PASS` |
| §2 依赖版本与兼容性交叉核对 | `PASS` |
| §3 最小运行时检查（exit 0） | `PASS` |
| §4 Benchmark 87/87 完整性（0 空文件 / 0 重复 / 尺寸达标 / gate 状态一致） | `PASS` |
| §5 contact_sheet 读取检查 | `PASS_WITH_LIMITATION`（缩略级目检；全尺寸级由每图 gate + 单图目检支撑） |
| §6 DOCX 双哈希 + 17/17 变更复核 | `PASS` |
| §7 Skill 目录树 + router 引用一致性（23/23 解析） | `PASS` |
| §8 异常文本（`vuitton`）0 命中 | `PASS` |
| §9 证据文件哈希已记录 | `PASS` |

**总体 `PASS_WITH_LIMITATION`** —— 限制原因（均已在上文对应小节声明，非未知项）：
① b12（3D）的 2 个文字包围盒不可测（mplot3d 投影）→ 该图文字质量以人工目检为准；
② contact_sheet 的全览检查为缩略级（全尺寸级证据为每图 0-overlap gate + 单图目检）；
③ 自动图件检查为启发式（贴边裁剪类需目检兜底，已在 gate SKILL.md 列为已知盲区）；
④ `__pycache__` 混入待清理（§10.1）。
