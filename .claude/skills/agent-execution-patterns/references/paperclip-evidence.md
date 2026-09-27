# Paperclip 证据附录

> 全部证据来自 paperclipai/paperclip（MIT）公开仓库的只读深读，快照日期 **2026-09-27**（master 分支）。
> 行号基于该快照，随上游版本会漂移；引用原文保留英文以避免转译失真。
> **未运行其任何代码**，以下为静态阅读证据（STATICALLY_VERIFIED）。

## 已读文件清单

| 文件 | 用途 |
|------|------|
| `docs/agents-runtime.md` | 运行模型、唤醒源、适配器、安全注意 |
| `docs/guides/agent-developer/heartbeat-protocol.md` | agent 侧协议（9 步 + 硬规则） |
| `doc/architecture/durable-continuation-scheduler.md` | 持久续跑 + 孤儿对账 + DOT-2 复盘 |
| `server/src/onboarding-assets/ceo/HEARTBEAT.md` | CEO agent 心跳清单 |
| `packages/shared/src/types/heartbeat.ts` | 领域类型（运行/唤醒/静默） |
| `packages/db/src/schema/heartbeat_runs.ts` | 运行表 schema |
| `packages/db/src/schema/agent_wakeup_requests.ts` | 唤醒队列表 schema |
| `server/src/services/heartbeat.ts` | 主实现，29,762 行（提纲 + 定向读取） |
| `ROADMAP.md`、`DESIGN.md` | 产品边界与工程纪律 |

## 逐条模式证据

### 1. 心跳执行
- `agents-runtime.md` §1: "Agents in Paperclip do not run continuously. They run in **heartbeats**: short execution windows triggered by a wakeup."
- §2 四种唤醒源：`timer` / `assignment` / `on_demand` / `automation`。
- §9 安全边界: "Local CLI adapters run unsandboxed on the host machine."

### 2. 唤醒合并与调度抑制
- `agents-runtime.md` §2: "If an agent is already running, new wakeups are merged (coalesced) instead of launching duplicate runs."
- `agent_wakeup_requests` 表有 `coalescedCount` 列；`heartbeat.ts` `mergeCoalescedContextSnapshot`（L7253）。
- `heartbeat.ts` L9373-9397 `resolveHeartbeatSchedulingSuppression`，三类拒绝原因：`worktree_instance` / `database_restore_in_progress` / `task_drain`。

### 3. 原子领取 + 409 永不重试
- `heartbeat-protocol.md` Step 5: "If another agent owns it: `409 Conflict` — stop and pick a different task. **Never retry a 409.**"
- Critical Rules: "Always checkout before working — never PATCH to `in_progress` manually"；"Never cancel cross-team tasks — reassign to your manager"。

### 4. 持久续跑 + 孤儿对账
- `durable-continuation-scheduler.md`: "Paperclip does not keep an agent process alive between turns… If work must continue later, Paperclip represents that intent in database state and creates another heartbeat run when the continuation becomes eligible."
- 不变量（L99-101）: "an assigned open issue should have either a live execution path, a durable reason to wait, or a visible terminal/blocking disposition."
- 续跑 kind：`same_agent` / `retry` / `delegated_issue` / `response_wake` / `monitor`，各带 idempotency key。
- `reconcileStrandedAssignedIssues()` 开工前检查列表：已有活路径 / 有待处理交互 / 树被暂停 / 配额监控中 / 被操作员取消 / agent 不可调用 / 预算或退避阻止 / 恢复失败次数过多 → 升级人工。
- 调度器默认 30,000 ms（clamp ≥10,000），启动 + 每个 tick 各跑一次对账。

### 5. 幂等 = 存储层约束
- `packages/db/src/schema/agent_wakeup_requests.ts` L59-83，5 条按 key 前缀作用域的部分唯一索引：
  - `issue_review_path_lost:%`、`issue_disposition_repair:%`（谓词 `status <> 'skipped'`）
  - `question-response:%` / `interaction:%`、`connection-intent:%`、`tool-action-response:%`（谓词 `status NOT IN ('skipped','failed','cancelled')`）

### 6. 配置指纹
- `heartbeat.ts`：`buildEffectiveRunSessionConfigMetadata`（L6487）、`buildEffectiveRunWorkspaceConfigMetadata`（L6587）、`resolveExecutionWorkspaceConfigFreshness`（L6640）、`shouldResetTaskSessionForModelChange`（L6812）、`resolveTaskSessionConfigFreshness`（L6842）。
- 机制：session / workspace 配置类目分别计算指纹并持久化，变更 → 重置会话或重建工作区，而非假设"改过即生效"。
- instructions 指纹：`resolveInstructionsConfigFingerprintMetadata`（L6386）、`resolveRootBoundInstructionsFingerprintPath`（L6350）；类目集合定义在 `buildSessionConfigCategoryValues`（L6434）/ `buildWorkspaceConfigCategoryValues`（L6540），未逐类目展开。

### 7. 进程身份 + 输出监护
- `heartbeat_runs.ts` L70-72 注释: "Legacy controller lease. **A PID alone is not an identity across containers.**"（列：`controllerBootId` / `controllerLeaseExpiresAt`）
- `types/heartbeat.ts` L253-269 `HeartbeatRunOutputSilence`：级别 `not_applicable | ok | suspicious | critical | snoozed`，含 `suspicionThresholdMs` / `criticalThresholdMs` / `snoozedUntil` 与自动评估 issue 引用。
- `heartbeat.ts`：`isProcessAlive`（L8843）、`terminateHeartbeatRunProcess`（L8889）、热重启收养 `readHotRestartAdoptionMetadata`（L8935）、任务 drain `startTaskDrain/stopTaskDrain/getTaskDrainStatus`（L1345/1354/1366）。

### 8. 预算门 + 重试预算守恒
- `heartbeat.ts`：adapter 调用前 `budgets.getInvocationBlock(...)`（L13122、L13487、L26595）；被拦时写入 `budget.blocked` 的 skipped 唤醒记录（L26604）；L17182-17191 超 per-day 预算先取消。
- `heartbeat.dailyBudgetCents`（L16605）。
- 拦截记录含 `scopeType` / `scopeId`（L26605-26609）；调用签名 `budgets.getInvocationBlock(companyId, agentId, …)` 表明至少含公司 + agent 两级作用域；完整枚举未逐一核实。
- 重试守恒注释：L14346 "process loss must not open a second retry budget"；L27100 "Repair does not reset the remaining automatic retry budget"。
- `cancelPendingWakeupsForBudgetScope`（L28706）与 "Cancelled due to budget pause"（L28757）。

### 9. 协议即清单
- `heartbeat-protocol.md`：9 步协议 + Critical Rules + Run Liveness。
  - "Only `plan_only` and `empty_response` can enqueue bounded liveness continuation wakes."
  - "Workspace provisioning alone is not treated as concrete task progress. Durable progress should appear as tool/action events, issue comments, document or work-product revisions, activity log entries, commits, or tests."
- `ceo/HEARTBEAT.md`："Above 80% spend, focus only on critical tasks."；"Never look for unassigned work"；写操作强制 `X-Paperclip-Run-Id`。

### 10. 工程纪律
- 根 `package.json` scripts：`check:no-git-push`、`check:token-gates`、`check:module-boundaries`、`test:lifecycle-baseline`、`evals:smoke` 等。
- 失败模式专属测试（仓库树）：`heartbeat-zombie-guard`、`heartbeat-orphaned-active-lease-sweep`、`heartbeat-issue-rewake-throttle`、`heartbeat-process-recovery`（533 KB）、`heartbeat-stale-queue-invalidation`。
- `DESIGN.md` Enforcement：Storybook 视觉快照基线证明"零视觉变化"；codemod 提交进 `scripts/`。
- 日志治理：`heartbeat_runs` 只存 `logStore/logRef/logBytes/logSha256/logCompressed`；载荷截断与脱敏 `boundHeartbeatRunEventPayloadForStorage`（L3612）、`redactInlineBase64ImageData`（L3619）。

## 反面教材：DOT-2 循环
- `durable-continuation-scheduler.md` §"Why DOT-2 looped"：成功结果未被证据分类器接受 → 状态保持 `in_progress` → 每 ~30s 对账补唤醒 → 重复同一答案。
- 修复：唤醒 prompt 补上触发评论上下文；低风险完成可接受 schema-valid 完成声明（工具 / 审批门不动）。
- 原文: "Fix the status or continuation decision; **increasing the polling interval only hides the bug.**"

## 安全备注（供边界判断）
- 该仓库有 12 条已披露安全公告（2026-04 ~ 2026-07，含 critical 级），且其本地适配器默认在宿主机上无沙箱运行 agent CLI。
- 本 skill 只提取执行可靠性模式；是否/如何部署该产品不在本 skill 范围。相关审计结论见项目记忆 `paperclip-repo-audit-20260927`。
