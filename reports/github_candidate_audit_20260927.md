# GitHub 候选项目审计报告（2026-09-27）

> 审计日期: 2026-09-27
> 审计范围: AI agent 基建 / 科研工作台 / skill 生态 / 决策引擎 / 办公与文档 相关近期热门开源项目
> 数据快照: 2026-09-27（星数、许可、活跃度均为该时点数据，会过期）
> 关联产物: `.claude/skills/agent-memory-patterns/`、`.claude/skills/decision-engine-patterns/`、`.claude-plugin-draft/`、`reports/open-science_gap_analysis_20260927.md`
> 前置轮次: paperclip 审计（2026-09-27 早先）已产出 `.claude/skills/agent-execution-patterns/`，本报告不重复

---

## 数据方法与诚实声明

核验方式分三级，逐行标注：

| 标记 | 含义 |
|------|------|
| **A** | API 核验 — 星数/许可/创建与推送时间来自 GitHub 公共 API 实测 |
| **P** | 页面核验 — 来自仓库页 WebFetch（含 README/结构信息） |
| **T** | 仅 trending 榜出现，未独立核验，数字不可引用 |

- 匿名 API 限流 60/时，中途耗尽后部分条目改用页面核验；未核验项一律标 T 或不入核心表。
- 星数异常高者已查 fork 比：正常开源项目 fork/star 约 5–20%；明显偏离者列入存疑。
- 所有「融合」均为模式提取或结构参考，**零安装、不拷贝上游代码**（沿用 registry wrapper_policy）。
- 性能数字（延迟/成本）如为第三方自述，一律标注"自述未复测"。

---

## 决策分级定义

| 级别 | 含义 |
|------|------|
| `PATTERN_SKILL` | 提取为模式参考技能（零安装，带证据文件与来源边界声明） |
| `STRUCTURE_ALIGN` | 结构对齐——用作本仓结构的参照物（草稿，不激活） |
| `GAP_AUDIT` | 对照审计——出差距清单，不改动现有 canonical skill |
| `WATCH` | 观察——本轮不动作，列入后续轮次候选 |
| `REJECT` | 不建议采用或直接安装 |

---

## 表 A：核心决策（本轮融合，已批准）

| 项目 | Stars | License | 核验 | 决策 | 说明 |
|------|-------|---------|------|------|------|
| [affaan-m/ECC](https://github.com/affaan-m/ECC) | 268k / 40k forks | MIT | A+P | `PATTERN_SKILL` → agent-memory-patterns | Agent harness OS：68 agents / 292 skills / instincts（置信度模式）/ Memory Vault。**星数超现象级，含金量无法独立验证，仅提取其公开文档可站得住的机制** |
| [vectorize-io/hindsight](https://github.com/vectorize-io/hindsight) | 34.5k | MIT | A | `PATTERN_SKILL` → agent-memory-patterns | "Agent Memory That Learns"，记忆机制第二来源 |
| [NandhaKishorM/laya](https://github.com/NandhaKishorM/laya) | 26.2k / 2.3k forks | Apache-2.0 | P+A | `PATTERN_SKILL` → decision-engine-patterns | Jev/System-1 决策引擎开源实现（Convai Innovations）。Jev 性能数字为第三方自述 |
| [anthropics/knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins) | 25.7k | Apache-2.0 | P | `STRUCTURE_ALIGN` → .claude-plugin-draft | 官方 11 插件；结构 = plugin.json + .mcp.json + commands/ + skills/，纯 markdown/JSON |
| [aipoch/open-science](https://github.com/aipoch/open-science) | 4.9k | Apache-2.0 | P | `GAP_AUDIT` → 对照审计报告 | AI 科研工作台：provenance / skills marketplace / reviewer 循环 / 文献库。同名项目 synthetic-sciences/openscience（3.6k★）同日创建，关系未查清 |
| [paperclipai/paperclip](https://github.com/paperclipai/paperclip) | 88.2k | MIT | A | 已审（前置轮次） | 产出 agent-execution-patterns（10 模式）；本报告不重复 |

### 生态条目（供 decision-engine-patterns 引用，不单独提取）

| 项目 | Stars | 核验 | 说明 |
|------|-------|------|------|
| [browser-use/jev-ultrafast](https://github.com/browser-use/jev-ultrafast) | 20.7k / 1.4k forks | A | web agent，Jev 类决策 |
| [jaredpalmer/kev](https://github.com/jaredpalmer/kev) | 7.3k | A | 可自训练的 Jev 系决策模型 |
| [tamaratran/fast-jev-compaction](https://github.com/tamaratran/fast-jev-compaction) | 7.0k | A | 把 Claude Code 压缩摘要换成 Jev 决策 |
| [mizorewww/laya-mlx](https://github.com/mizorewww/laya-mlx) | 6.4k | A | laya 的 MLX 原生运行时 |
| [jev-chat/jev-chat-jarvis](https://github.com/jev-chat/jev-chat-jarvis) | 6.7k | A | 手机端对话副驾（只读屏幕） |
| [TheoLeeCJ/SemIf-OpenJev](https://github.com/TheoLeeCJ/SemIf-OpenJev) | 4.4k | A | 家训 3090 上的开放实现 |
| [typesafe-ai/skills](https://github.com/typesafe-ai/skills) | 2.2k | A | TypeSafe（Jev 官方）的 skill 集 |

---

## 表 B：重点观察（WATCH，后续轮次候选）

按与本工作台相关度排序；许可未核者已标注。

| 项目 | Stars | License | 核验 | 相关点 |
|------|-------|---------|------|--------|
| [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | 99.4k / 10.4k forks | MIT | A | **与全局 CLAUDE.md 里的 Addy 工程原则同源**；生产级工程 skill 集，高优先观察 |
| [stablyai/orca](https://github.com/stablyai/orca) | 79.2k | MIT | P | 并行 agent fleet（每 agent 独立 worktree、对比合并、SSH 远程） |
| [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | 58.6k | MIT | P | 523 课学习课程（含 agent 工程/多智能体阶段） |
| [HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything) | 50.7k | Apache-2.0 | P | CLI 作为 agent 通用接口；CLI-Hub 注册表（含 Zotero/LibreOffice） |
| [alibaba/open-code-review](https://github.com/alibaba/open-code-review) | 41.7k | Apache-2.0 | A | 确定性管线 + LLM 混合代码评审 |
| [davila7/claude-code-templates](https://github.com/davila7/claude-code-templates) | 31.9k | MIT | A | Claude Code 配置/监控 CLI |
| [Tencent/WeKnora](https://github.com/Tencent/WeKnora) | 30.4k | MIT | P | 文档→RAG/推理 agent/自维护 Wiki 三合一，含 skill 沙箱与知识图谱 |
| [xai-org/grok-build](https://github.com/xai-org/grok-build) | 27.1k / 5.1k forks | 未核 | A | 编码 agent harness（TUI） |
| [cloudflare/security-audit-skill](https://github.com/cloudflare/security-audit-skill) | 22.1k | MIT | A | 机器可读、可独立复核的多阶段安全审计 skill |
| [dream-num/univer](https://github.com/dream-num/univer) | 19.8k | Apache-2.0 | A | "Office Harness for AI Agents"（表格/文档/幻灯片/PDF） |
| [dataelement/dsh-desktop](https://github.com/dataelement/dsh-desktop) | 9.9k | 未核 | A | DeepSeek Harness 桌面版 |
| [trailhq/Graft](https://github.com/trailhq/Graft) | 9.3k | 未核 | A | Claude Code/Codex 等 harness 的上下文加速降本 |
| [genspark-ai/genoffice](https://github.com/genspark-ai/genoffice) | 7.9k | 未核 | A | 开源 AI Office 套件 |
| [Human-Agent-Society/reef](https://github.com/Human-Agent-Society/reef) | 6.3k | 未核 | A | 持续自改进 agent 基础设施 |
| [XiaoDuoYa/codex-with-chatgpt](https://github.com/XiaoDuoYa/codex-with-chatgpt) | 6.7k | 未核 | A | ChatGPT 规划 + Codex 执行（与既有 codex-claude 桥接同思路） |
| [alphaXiv/OpenResearch](https://github.com/alphaXiv/OpenResearch) | 5.8k | 未核 | A | 把编码 agent 变研究 agent |
| [larashero3-dotcom/lieflat-charts](https://github.com/larashero3-dotcom/lieflat-charts) | 5.7k | 未核 | A | 图表类 agent skill（中文项目） |
| [bojieli/ai-infra-book](https://github.com/bojieli/ai-infra-book) | 5.4k | 未核 | A | 《深入理解 AI Infra》开源书稿 |
| [sapientinc/PRAXIST](https://github.com/sapientinc/PRAXIST) | 5.0k | 未核 | A | 可执行研究自治系统 |
| [NVIDIA/Model-Optimizer](https://github.com/NVIDIA/Model-Optimizer) | 4.9k | Apache-2.0 | A | 量化/蒸馏/剪枝/NAS 统一库 |
| [NVlabs/SoL-Pi](https://github.com/NVlabs/SoL-Pi) | 3.1k | 未核 | A | 自研究循环扩展（NVIDIA Labs） |
| [EvoMap/AutoResearch](https://github.com/EvoMap/AutoResearch) | 2.8k | 未核 | A | idea→paper-ready 证据的科研 agent |
| [google-research/tabfm](https://github.com/google-research/tabfm) | 2.7k | 未核 | A | 表格基础模型（Tabular Foundation Model） |
| [jakubkrehel/skills](https://github.com/jakubkrehel/skills) | 7.2k | 未核 | A | 界面构建类 agent skill 集 |

### 写作与治理波（WATCH，整波留待下轮，需逐项查许可）

| 项目 | Stars | 核验 | 用途 |
|------|-------|------|------|
| [Nanako0129/sepia](https://github.com/Nanako0129/sepia) | 2.9k | A | "去 AI 味"写作 skill |
| [mikubaka88/CCFA-Skills](https://github.com/mikubaka88/CCFA-Skills) | 2.9k | A | CCF-A 论文叙事线 skill 家族（TeX） |
| [Leonxlnx/unlazy](https://github.com/Leonxlnx/unlazy) | 3.7k | A | 反偷懒 Depth Tree 方法 |
| [lennney/stop-that-shit](https://github.com/lennney/stop-that-shit) | 2.3k | A | hook+guard 拦截 agent 任务范围膨胀 |
| [AminBlg/SimpleEnglish](https://github.com/AminBlg/SimpleEnglish) | 3.6k | A | STE100 简化技术英语 |
| [danyuchn/asd-ste100-skill](https://github.com/danyuchn/asd-ste100-skill) | 2.3k | A | STE100 规则改写（Claude Code skill） |

---

## 表 C：存疑与否决

| 项目 | Stars | 核验 | 决策 | 原因 |
|------|-------|------|------|------|
| [zhaoxuya520/reverse-skill](https://github.com/zhaoxuya520/reverse-skill) | 38.2k | A | `REJECT`（暂不） | 逆向/授权渗透 skill 包；该细分领域 38k★ 异常偏高，且属双用途工具，无明确授权场景不引入 |
| [unicity-aos/aos-ce](https://github.com/unicity-aos/aos-ce) | 8.5k / 22 forks | A | `REJECT` | fork 比 0.26%，疑似刷星 |
| [elder-plinius/T3MP3ST](https://github.com/elder-plinius/T3MP3ST) | 6.3k | A | `REJECT` | 自主红队/攻防平台，超出本工作台范围 |
| synthetic-sciences/openscience | 3.6k | A | 观察 | 与 aipoch/open-science 同名且同日创建，先查清关系再论 |

---

## 附录：扫描覆盖面

本轮扫描覆盖约 60 个仓库（Trending 日/周榜 + 两个 API 搜索 + 定向核验）。未入表条目为与科研工作台无关或纯消费类项目（媒体客户端、游戏工具、壁纸/Logo 生成、财务数据 API、社交抽取、量化交易等），在此不逐一列出。断言范围仅限：**本表所列为已核验的相关项；未列入不等于不存在相关项目**。

### 数据局限性

1. 星数为快照，且 trending 榜本身滞后于真实热度；ECC 268k★ 为 API 与页面双重确认的数值，但其增长来源无法独立验证。
2. 部分条目许可未核（标注"未核"），在未核清许可前不得提取其内容，仅作观察。
3. Jev/TypeSafe 相关信息来自第三方 README 转述，未访问其官方渠道。
4. 本报告不构成安装建议；任何安装动作需单独批准（registry install_policy）。

## 后续轮次候选（按优先级）

1. 写作与治理波（6 项，先逐项查许可后决定吸收方式）
2. addyosmani/agent-skills（与全局 Addy 原则同源，建议下一轮优先审计）
3. CLI-Anything（CLI 化模式，关联 Zotero/办公自动化）
4. cloudflare/security-audit-skill（审计模式）
5. stablyai/orca / Graft（并行与上下文基建）
