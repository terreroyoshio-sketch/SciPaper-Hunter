# 现有科研制图能力地图与缺口分析

- 审计日期：2026-09-28（只读审计，未修改任何现有文件；未安装任何包）
- 审计范围：本 worktree `.claude/`、主仓库 `C:\Users\张涵\Desktop\项目\skill\.claude\`、用户级 `~/.claude/skills`、休眠副本 `~/.agents/skills`、本地文档 `C:\Users\张涵\Desktop\制图提示词.docx`
- 方法：目录枚举 + 关键词检索（方框/几何叙事/figure_manifest/SmartArt/Mermaid）+ 文件通读；所有结论以实际路径为据

## 一、现有资产清单（三层 + 文档）

### A. 本 worktree（项目级，本分支可改）
- skills(12)：含 **technical-route-diagram**（2026-09-28 新建：四步横带渲染器 + 布局 QA）
- agents(12)：figure-table-editor（图注/格式）等
- commands(17)：image-brief / format-doc / ppt-build 等
- rules(9)：反造假/引用/文件安全/办公类——**无任何绘图专用规则**

### B. 主仓库（另一检出，不直接修改）
- rules：**diagram-style.md**（12 条）/ **diagram-integrity.md**（8 条，反造假）/ **diagram-file-safety.md**（8 条，版本与来源）
- agents：diagram-architect / diagram-integrity-auditor / diagram-style-editor
- commands：/diagram /diagram-check /diagram-revise /flowchart /ppt-figure /sequence /research-route
- skills：**drawio-diagram-workbench**（brief 先行 → .drawio，12 类图，输出 SVG/PNG/PDF 需 draw.io Desktop）、nature-figure
- research-stack-index/：skills.index.md、workflow-router.md（数百技能注册表——新增技能与其注册口径的关系待确认）

### C. 用户级 ~/.claude/skills（全局，不修改）
- 数据/统计图：scientific-visualization、matplotlib、seaborn、plotly、figurelab-publish、scipilot-figure-skill（含 visual_qa 回看闭环）、academic-figure-skill、scientific-figure-making
- 框图/示意图：nature-figure-style（架构图实证规则）、scientific-schematics（AI 出图，需 OpenRouter key）、markdown-technical-diagram-suite
- 流程图库级：graphviz、networkx、uml、bpmn、archimate、archify、mermaid 系
- QA 相关：figure-preflight-checker、figure-data-integrity-auditor、figure-text-consistency-checker、layout-spacing-constraint-validator、plot-extraction-replot-verify、image-reuse-self-audit、paperbanana-output-auditor
- 上游规划：technical-route-blueprint-planner（文本蓝图）；数模：cumcm-plot、math-modeling-skill
- GIS/工程：geopandas（库级）；电路/DSP/3D：无技能

### D. 《制图提示词.docx》（`C:\Users\张涵\Desktop\制图提示词.docx`）
- 54 节、约 1,919 段，与"约 65 页"相符；自述角色"科研可视化工程师 + 最终 Figure QA 验收负责人"
- §29–36 声明"优先读取"8 个技能：**其中 6 个在全库不存在**（research-task-router 存在于仓库 `.agents/skills` 非 worktree；diagram-workflow / diagram-quality-engineering / diagram-visual-output-guard / cognitive-illustration / scientific-workbench-agent / final-delivery-audit 未找到）→ 文档与实际资产脱节
- §17/18/22/44/52/54 的"绝对禁止方框+箭头 / 必须几何叙事"——修正方案见 `references/figure_style_catalog.md` §3；该规则亦固化在自动记忆 `figure_qa_protocol_advantages` 第 8 条（本次一并修正）

## 二、12 图件家族覆盖矩阵

| 家族 | 现有覆盖 | 缺口 |
|---|---|---|
| 数据结果图 | figurelab-publish / academic-figure-skill / scientific-visualization（强） | 无 SciencePlots 式期刊参数统一入口（可选增强） |
| 统计分析图 | seaborn / matplotlib / 统计类技能 | 不确定性与显著性表达规范散落 → 收进统一 gate |
| 技术路线图 | technical-route-diagram（渲染） + blueprint-planner（蓝图） | 五带竖版等版式未模板化 |
| 方法框架图 | 部分（nature-figure-style 的框图规则） | 无独立家族工作流 |
| 算法流程图 | graphviz / networkx（库级） | 无"布局→呈现"工作流；几何叙事规则未落地 |
| 机制示意图 | nature-figure-style（部分） | 无物理/生态/医学几何基元工作流 |
| Graphical abstract | 无 | **完全缺失** |
| GIS / 空间分析 | geopandas 库技能 | 无图件工作流；cartopy 未装（无真实投影能力） |
| 网络/拓扑 | networkx / graphviz 库技能 | 无图件工作流 |
| 电路/DSP/控制 | 无技能（**schemdraw 0.23 已装**可用） | 缺技能包装 |
| 3D 科学图 | 无 | 缺技能 + 缺库（pyvista） |
| 多面板复合 | academic-figure-skill 有 multipanel 参考 | 无统一编排（GridSpec + 统一图例）工作流 |
| 图件 QA | **多头重叠**：figurelab QA / scipilot visual_qa / figure-preflight-checker / technical-route-diagram 的 qa_layout 等 ≥5 处 | **无统一验收口径与三值状态** |

## 三、冲突与风险（只读观察）

1. **规则冲突（本次修正对象）**：docx 绝对禁令 vs 参考图范式 vs 现有技能（nature-figure-style、technical-route-diagram 均以语义容器为默认）。
2. **字号场景冲突**：主仓库 diagram-style 规则 3"字号 ≥10pt"面向课程/办公图；SCI 图按印幅 6.5–8pt 设计。→ 路由按目标载体分流，gate 按载体选阈值；**不改原规则，仅记录并用 gate 区分场景**。
3. **QA 重复**：≥5 个技能声称管出图后 QA，边界交叠 → 新 gate 只做"统一口径 + 三值状态 + 缺口检查"，具体实现复用既有脚本。
4. **docx 技能引用失效**（6/8 不存在）→ 修 docx 补丁副本时同步修正引用列表为实际存在技能。
5. **draw.io Desktop 未装** → drawio-diagram-workbench 的 SVG/PNG/PDF 导出链路本机不可用（.drawio 源可用，导出走 web 或待装）。
6. **路由密度**：用户级技能总数已达数百；新增前需去重，新技能 description 必须写"何时不用"。

## 四、Skill 设计（最小实现，去重后）

**新增 11 个薄技能（职责单一）**：
`scientific-figure-router`（路由 + 渲染器决策树 + 门禁规则）、`figure-quality-gate`（三值状态统一验收）、`scientific-method-framework`、`scientific-flowchart`、`mechanism-schematic`、`graphical-abstract`、`geospatial-figure`、`network-topology`、`engineering-schematic`、`scientific-3d`、`multipanel-compositor`

**扩展 1 个**：`technical-route-diagram`（按修正后的方框规则更新 + 路由对接）

**不新建（路由到现有）**：technical-roadmap → technical-route-diagram；publication-data-plot → figurelab-publish / academic-figure-skill / scientific-visualization；statistical-figure → seaborn / matplotlib / 统计技能。理由：同职责已覆盖，遵"优先扩展、不重复创建"。

**与主仓库 diagram 体系的分工**：drawio-diagram-workbench 负责"办公/课程/PPT/可编辑 drawio 类图"；新体系负责"SCI 投稿级图件"（矢量、印幅字号、内嵌真实数据）；两者由 router 按"目标载体"分流，不互相替代。

## 五、未做 / 待授权

- 未安装任何包（待批清单见 `references/github_visualization_audit.md` §C）
- 未修改主仓库、用户级技能、docx 原件
- 未 commit、未推送
- 注册表 `research-stack-index/skills.index.md` 的更新属主仓库动作，待确认后执行
