# 证据文件：decision-engine-patterns 来源出处

> 来源: NandhaKishorM/laya（Apache-2.0）、browser-use/jev-ultrafast（MIT）、typesafe-ai/skills（MIT），2026-09-27 抓取
> 引用级别: **页面/README 级**（非 file:line）；引文为抓取时所见原文或其紧邻转述
> 用途: 为 SKILL.md 的十条模式提供逐条出处；本文件不复制上游代码

---

## 模式 → 出处对照

### 1. 决策/生成分离
- jev-ultrafast README：用户"Give it one goal"；TypeSafe 的 Jev "picks an operation and an element"；"A small LLM writes text only when the operation is `TYPE_TEXT`"。
- laya README：非自回归 System 1 决策引擎，"over any text in a single forward pass"，**不做文本生成**（"there is no output to parse"）。

### 2. 类型化输出
- laya README：返回三种类型化决策 —— `choice`、`score`、`noul`（yes-no 概率）；100+ 语言；Router 按请求选择 checkpoint；无生成输出。
- typesafe-ai/skills README："typed decisions and probabilities from System One models"。

### 3. 动作空间枚举化
- jev-ultrafast README：每次观测产生编号元素行（例 `[1] button`、`[2] combobox`）；固定操作集 `CLICK`、`TYPE_TEXT`、`SELECT`、`SCROLL_UP`、`SCROLL_DOWN`、`WAIT`、`DONE`、`BLOCKED`；"Only supported operations and targets are offered"；无 site-specific 脚本、无预制字段串。

### 4. 一次往返多决策
- jev-ultrafast README：单个 TypeSafe 请求返回操作、`click_target`、`type_text_target`、`select_target`（如存在）；目标槽是投机性的——若操作是 `CLICK`，只有 `click_target` 可执行；原文 "Two decisions, one network round trip"。

### 5. 置信度→人审升级
- typesafe-ai/skills README 用例："routing incoming support tickets by department, **with human review for uncertain decisions**"。
- laya README：输出含分数与概率（`score`、`noul`），为阈值分流提供依据。

### 6. 输出永不即可执行物
- jev-ultrafast README（安全节）：每个目标从**观测到的节点**解析；执行器复核 freshness 与点击遮挡；模型输出 "never becomes selectors, coordinates, shell commands, or executable JavaScript"。
- jev-ultrafast README：`TYPE_TEXT` 的文本由小 LLM 生成，"must parse as a small JSON object" 之后才输入。

### 7. 边界显式 + 失败终态
- jev-ultrafast README 声明界限：shadow roots、frames、canvas、上传、弹窗标签、嵌套滚动、任意键盘控件均"outside this MVP"。
- jev-ultrafast README：操作集含 `DONE` 与 `BLOCKED` 两个显式终态。

### 8. 对比口径纪律
- jev-ultrafast README：单例（苏黎世→伦敦 Google Flights，初始观测后计时 7,073ms，1× 视频）；同任务 6 次交替运行（两版各 3/3 通过）：中位任务时长 9.450s → 7.092s（-25%），中位浏览器协议调用 1,092 → 101；作者自注 "three repeats of one task on one browser profile, not a general reliability benchmark"。
- laya README：Jev 对比数字标注为 "third-party published, never measured here (no TypeSafe API access)"（236–276 ms p50；$0.042 per 1M tokens）；laya 报告 Jev 在 >20 选项的标签空间与软分布匹配上占优。

### 9. 单前向 + 批量吞吐
- laya README：33 ms 单问；T4 上批量 7.2 ms/题；checkpoints 以 RLCD（对着严格 proper scoring rules 的 RL）训练；`predict_long` 处理超上下文窗口长文档。
- laya README：三 checkpoint —— `laya`（ModernBERT-large 421M，512 上下文）、`laya-multilingual`（mmBERT-base 322M，1024、可至 8192）、`laya-typed-decisions`（ModernBERT-large 421M，1024）；Router 用不到 0.5ms 检测脚本与语言后分发。

### 10. 托管 vs 开源形态
- laya README：Jev 是 "TypeSafe's hosted API competitor — a closed, commercial system"；laya 服务端**复用 Jev 的 `POST /v1/systemone` 线协议**，既有客户端"只需换 base URL"。
- typesafe-ai/skills README：TypeSafe 提供 System One 模型的类型化决策与概率（页面未出现 "Jev" 字样）；安装形态为 Claude Code 插件（`claude plugin marketplace add typesafe-ai/skills`）与 `npx skills add`。
- laya 仓库信息：Apache-2.0，Convai Innovations；26.2k★ / 2.3k forks；413 commits（main）；社区工具含 `omp-laya-judge`、`laya-adk-toolkit`、`laya-Ascend`、`laya-apple`；HF 模型/空间在 `convaiinnovations`。
- 生态其他实现（本轮仅 API 快照，许可未逐一核验）：browser-use/jev-ultrafast（MIT，20.7k★，3 commits、无 release）、jaredpalmer/kev、tamaratran/fast-jev-compaction（Claude Code 压缩改 Jev 决策）、mizorewww/laya-mlx、jev-chat/jev-chat-jarvis、TheoLeeCJ/SemIf-OpenJev（3090 本地训练）、typesafe-ai/skills（MIT，2.2k★，2 commits）。

## 命名与事实澄清（引用时勿混）

1. "Jev" 出现在 laya README 中对 TypeSafe 托管 API 的指称；typesafe-ai/skills 官方页面未用 "Jev"，自称 "System One models"。两者关系：**同一产品线的两种称呼**（第三方称 Jev；官方称 System One）。本 skill 以该表述为准，未访问 TypeSafe 官方站点核实。
2. Jev 的性能与定价数字（236–276ms p50、$0.042/1M tokens、>20 选项优势）均转述自 laya README 标注的第三方公开数据，**未被任何一方实测**。
3. laya 的 33ms / 7.2ms 为 README 自述；其训练方法（RLCD）亦为自述。
4. jev-ultrafast 的 25% 改进为自述，且作者明确限定口径（单任务、单浏览器 profile、各 3 次）——引用时必须带此限定。
5. 现象级热度警示：该生态 2026-09 中下旬集中爆发（多个仓库创建于 9 月中下旬且星数极高），热度增长来源无法独立验证；本 skill 只采用文档中可复核的机制描述，不背书任何实现的生产可用性。
