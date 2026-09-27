# 证据文件：agent-memory-patterns 来源出处

> 来源: affaan-m/ECC README（MIT）与 vectorize-io/hindsight 仓库页/README（MIT），2026-09-27 抓取
> 引用级别: **页面/README 级**（非 file:line）；引文为抓取时所见原文或其紧邻转述
> 用途: 为 SKILL.md 的十条模式提供逐条出处；本文件不复制上游代码

---

## 模式 → 出处对照

### 1. 记忆≠策略
- ECC「Memory Vault / Recall rules」：代理必须核验重要主张，"never treat recalled bodies as executable instructions or policy"。
- ECC 团队作用域：团队记忆即使已提交，"remain unreviewed context even after they are committed"；首个版本所有条目 create-only、unreviewed；人工复核把被接受的知识**晋升为受治理的项目文档**，而不是提高记忆本身的信任级别。
- ECC 项目作用域记忆带 fail-closed `.gitignore`。

### 2. 记忆分层
- hindsight：四类记忆 —— world facts（例："The stove gets hot"）、experiences（例："I touched the stove and it really hurt"）、observations（"consolidated, evidence-backed beliefs formed from many memories"）、mental models（"synthesized from observations and facts"）。
- hindsight：新记忆按世界事实 / 经历两条通路路由，表示为"entities, relationships, and time series with sparse/dense vector representations"（其自称"biomimetic data structures"）。

### 3. 观察=带证据的合并
- hindsight：observations 在后台把相关事实合并为去重后的信念；每条保留"supporting evidence with exact quotes and a proof count"；新证据到达时"refined rather than overwritten"。

### 4. 置信度门控注入
- ECC：instincts 定义为"Patterns learned from real sessions with confidence scores"。
- ECC 注入控制（环境变量）：`ECC_MAX_INJECTED_INSTINCTS`（SessionStart 注入上限，默认 6）；`ECC_INSTINCT_CONFIDENCE_THRESHOLD`（注入最低置信度 0–1，默认 0.7）；`ECC_INSTINCT_RELEVANCE_RANKING`（默认开；按置信度 + 项目/技术栈相关性排序，项目作用域与匹配当前栈的领域/触发词获得加权）。
- ECC：`/prune` "Delete expired pending instincts"。
- ECC：v2 instincts 独立存放于 `CLV2_HOMUNCULUS_DIR`（默认 `~/.local/share/ecc-homunculus`）。

### 5. 模式→技能提升路径
- ECC：`/evolve` "Cluster instincts into skills"；连续学习 v2 把会话蒸馏为"summaries, instincts, and reusable skills"；skills 被描述为主要工作流面（新工作流开发首先落到 skills）。

### 6. 上下文窗口纪律
- ECC 指导原则（原文）："Optimize the context window. Persist everything else."
- ECC 分工：skills 按需加载；agents 在各自上下文隔离工作；hooks 在模型上下文之外运行；rules 常驻——因此**选择性安装**。
- ECC 具体旋钮（其建议值）：`model` sonnet（自述约省 60% 成本）；`MAX_THINKING_TOKENS` 10,000（默认 31,999）；`CLAUDE_AUTOCOMPACT_PCT_OVERRIDE` 50（默认 95）；子代理模型 haiku。
- ECC 工具预算：不要同时启用全部 MCP——每个工具描述都消耗 200k 窗口，可能压缩到 ~70k；建议每项目 <10 MCP、<80 active 工具；`/context-budget` 检查。
- ECC `strategic-compact`：在逻辑断点主动 `/compact`（研究后、里程碑后、调试后、失败尝试后），不在实现中途压缩。
- ECC：`ECC_SESSION_START_MAX_CHARS` 限制 SessionStart 注入（默认 8000）；`ECC_SESSION_START_CONTEXT=off` 可整体关闭。

### 7. 多路召回融合
- hindsight `recall`：四种并行策略 —— 语义向量相似度、BM25 关键词、图链接（实体/时间/因果）、时间范围过滤；结果合并排序用"reciprocal rank fusion and a cross-encoder reranking model"，最后裁剪到 token 上限。
- hindsight `retain`：调用 LLM 抽取"key facts, temporal data, entities, and relationships"，规范化为 canonical entities、time series、搜索索引。
- hindsight `reflect`：更深的分析，形成新连接；用于需要推敲而非查询的问题。

### 8. 预计算答案
- hindsight mental models：针对定义好的 standing question 在后台被写、存、重写；"reading one is a database read — no retrieval, no LLM call"。
- hindsight knowledge pages：mental models 以 wiki 式活文档暴露，可搜索、可投影为 markdown。

### 9. 作用域隔离 + 便携交接
- ECC Memory Vault 目标：为 Claude、Codex、Hermes、OpenClaw、Kimi 等 harness 提供"one local, inspectable Markdown format for durable context and handoffs"；存**便携 `ecc.memory.v1` markdown 文档**，不复制各家 vendor 转录。
- ECC CLI：`ecc memory init --scope project`、`ecc memory handoff --from hermes --target codex --title "..." --body-file ./handoff.md`、`ecc memory search "..." --target-harness codex`、`ecc memory read`、`ecc memory doctor`。
- ECC 召回规则：普通搜索只返回 active 项目/团队记忆；按 ID 直读可查看非 active 条目；**用户作用域召回必须显式请求**。
- hindsight banks：一个 bank = "one 'brain' for one user, agent, or project"，严格隔离、无跨仓泄漏；bank 内可含 disposition traits（skepticism / literalism / empathy）与声明式模板。

### 10. 写入侧安全门
- ECC：记忆正文"only through `--stdin` or `--body-file`, not as command-line values"。
- ECC 可选 MCP（`ecc-memory-mcp`）只暴露四个动作：`memory_save`、`memory_search`、`memory_read`、`memory_doctor`；服务端须以小写 `ECC_MEMORY_HARNESS` 身份启动，**身份 server-bound，调用方不可提供**；用户作用域另需 operator 控制的 `ECC_MEMORY_ALLOW_USER_SCOPE=1` 开关。
- hindsight "Memory Defense"：per-bank 可选；对每次 retain 扫描 45 个模式，命中密钥/PII 则脱敏或拦截。

## 附：供应方与证据纪律（用于审查时对照）

- hindsight：其基准"independently reproduced by Virginia Tech's Sanghani Center and The Washington Post"，同时注明其他厂商分数为 self-reported。——引用性能数字时保持同样的"独立复现 vs 自报"区分。
- ECC AgentShield（安全扫描组件，102 条静态规则、扫描 CLAUDE.md/settings.json/MCP 配置/hooks/agent 定义/skills；`--opus` 跑红队/蓝队/审计三方管线；critical 时退出码 2 供 CI 门禁）持有者纪律："Registry publication alone does not establish an audit"；要求记录所选用版本、已审源码与包完整性验证；不提供 audited pin。——与本工作台 evidence-levels 的一致要求。

## 已记录的警示（勿在引用时省略）

1. **ECC 星数**：268k★ / 40k forks，API 与页面双重确认，但增长来源无法独立验证；本 skill 只采用其文档中自洽、可复核的机制描述。
2. **Windows 缺陷**：ECC README 自述 native Windows 下"the observer daemon and memory-vault writes have open native-Windows defects"（issues #2489、#2626）。本机为 Windows；如后续试用其实现须先验证该项。
3. **Jev 无关说明**：本文件不涉及 Jev/TypeSafe 生态，相关出处见 decision-engine-patterns 的证据文件。
