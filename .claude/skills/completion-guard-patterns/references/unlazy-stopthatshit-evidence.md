# 证据文件：completion-guard-patterns 来源出处

> 来源: Leonxlnx/unlazy（MIT）与 lennney/stop-that-shit（MIT），2026-09-28 抓取
> 引用级别: **页面/README 级**（非 file:line）；引文为抓取时所见原文或其紧邻转述
> 用途: 为 SKILL.md 的十条模式提供逐条出处；本文件不复制上游代码

---

## 模式 → 出处对照

### 1. 可运行验收台账
- unlazy README："Completion discipline for substantial AI-agent work, backed by runnable gates"；"Write an acceptance ledger (`GATES.md`) first, then execute reviewed checks and reverify returned work."
- Gate 字段：`CHECK:`、`EXPECT:`、`CWD:`、`EVIDENCE:`；"a runnable gate passes only if the process exits 0 **and** `EXPECT:` matches combined output"。
- 解析器："rejects empty ledgers, duplicate ids, and incomplete runnable gates"。

### 2. 证据绑定定义
- unlazy README："Automatic evidence is bound to a SHA-256 digest of the parsed `CHECK:`, `EXPECT:`, and `CWD:` definition, so structural drift makes a gate stale and unmet."
- 限定原文："The README explicitly warns this detects drift, not tampering."（检测漂移，不检测篡改。）

### 3. 重验证通道
- unlazy 模式：`--status`（"never executes"）；正常模式（"discloses resolved command/shell/CWD/PATH before executing an unapproved oracle"）；`--approve`；`--reverify`（"re-runs all gates, including ones already marked complete"）。

### 4. 放弃即交接
- unlazy README："abandoning a gate is a 'HANDOFF REQUIRED' outcome that exits `1` and cannot promote parent completion"。
- 辅助：orchestration 叶状态含 `WAITING`、`READY`、`IN-FLIGHT`、`VERIFIED`、`ABANDONED`；`OWNS:` 路径声明。

### 5. 无进展熔断
- unlazy README："An optional Claude Code Stop hook returns `decision: \"block\"` while gates are unmet or launch waves incomplete; it self-releases after six consecutive blocks with no semantic progress."
- 对照教训见本工作台 `agent-execution-patterns` 反面教材（DOT-2：修状态判定而非调大轮询间隔）。

### 6. 范围守恒（SHIT-S）
- stop-that-shit：**S — Scope creep**："touching unrelated modules while fixing one problem; extensions with no present use should stop."
- 其原则："the stated principle is to finish the current responsibility completely and let complexity grow with real need"（完成当前责任，复杂度随真实需求生长）。
- Guard 行为：`files=` 路径外写入 → stopped。

### 7. 防御最小化（SHIT-H）
- stop-that-shit：**H — Hashing & hypothetical hardening**："checksums nobody reads, compatibility layers built for imagined futures"；"The rule: defenses should detect problems and trigger refusal, recovery, or diagnosis."
- Guard 行为：可识别的哈希操作 → stopped（`hash=allow` 放行）；新增依赖 → asked（`deps=allow` 放行）。

### 8. 意图守恒（SHIT-I）
- stop-that-shit：**I — Intent violation**："e.g., a read-only review where files still get edited. '审查就报告问题，修改需要授权' — review reports, edits need authorization."
- Guard 行为：review / answer / monitor 模式下的文件写入 → stopped。

### 9. 免重复劳动（SHIT-T）
- stop-that-shit：**T — Task thrashing**："re-reading, re-testing, or re-reviewing without new problems or changes."

### 10. 拦截证据分离
- stop-that-shit："On denials, the Guard reports `permission_deny_returned` (OpenCode: `execution_denial_returned`) and records `hostEffect: unobserved` — whether the host actually enforced it is tracked separately."
- 状态机："After install the state is '`OBSERVING / unconfirmed`'; an explicit directive moves it to `ARMED`. `watch` stays observe-only, and a Skill-only install has no execution interception."
- 指令集：`review`、`answer`、`monitor`、`change`、`watch`、`status`/`runtime`；子代理预算 `agents=N`。

## 附：来源项目的自我限定（引用时必须保留）

**unlazy**
- 其 README 明确："research does not prove that unlazy produces a fixed improvement"。
- 引用文献含：Quantifying Laziness；s1 的 budget forcing；SlopCodeBench（"best agent passed 14.8% of checkpoints"）；METR Time Horizon 1.1（"196.5-day overall P50 fit, 130.8 days post-2023"）。
- 早期六次内部对比被其自注为"historical design input, not a benchmark guarantee"（原始工件不在库中）。
- 版本：2.1.0 **未发版**；"recommends pinning an exact commit for an immutable install"；要求 Node 16+。
- Depth Tree：README 仅一句摘要（"splits a task N layers deep"；叶节点拿"full time budget of the whole task"→"effort multiplies with depth"）；完整方法在其 `references/method.md`（本文件未读取其内容）。

**stop-that-shit**
- 版本 v0.2.3；79 commits；公开评测为"18 个 Bad/Good 判定用例"；要求 Node 18+（Pi 0.84.4 需 22.19+）。
- 平台：Codex / Claude Code / OpenCode / Hermes Agent CLI / Pi。
- 附带组件 STSS（Slop）：对 agent 散文的防御性填充做 `rewrite` / `audit` 修剪。
- "Sandbox-based isolation is left to the host"（沙箱隔离留给宿主）。
- Runtime events 自述"don't store code or conversation text"。

## 警示（勿在引用时省略）

1. 两项目均含 **hook / 拦截类能力**（unlazy Stop hook、stop-that-shit Guard）；本工作台**未启用**任何 hook，本 skill 仅提取模式。启用需单独审批 + 沙箱验证。
2. stop-that-shit 对其拦截效力自述为 `hostEffect: unobserved`——"我们拦了"与"宿主执行了"必须分开陈述；该限定本身是模式 10 的直接来源。
3. 两个项目的效果声明均为自述且自带保留（见上"自我限定"节），本 skill 不背书其效果，只引用其机制设计。
