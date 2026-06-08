# Hooks 启用方案 — Hook Plan

## 概述
本文件定义科研工作台需要的 hooks 及其配置草案。**所有 hooks 默认禁用，需人工确认后启用。**

---

## Hook 总览

| Hook 名称 | 类型 | 触发时机 | 用途 | 风险等级 | 建议启用 |
|-----------|------|---------|------|---------|---------|
| session_start_context | SessionStart | 会话开始 | 加载项目状态和上下文 | 低 | ✅ 是 |
| pre_delete_guard | PreToolUse/Bash | 执行命令前 | 拦截危险删除操作 | 中 | ✅ 是 |
| post_write_log | PostToolUse/Write | 写入文件后 | 记录关键文件变更 | 低 | ⚠️ 可选 |
| session_end_summary | Stop/SessionEnd | 会话结束 | 生成会话摘要 | 低 | ✅ 是 |

---

## 各 Hook 详情

### 1. session_start_context.sh
- **类型:** SessionStart
- **触发:** 每次会话开始时
- **用途:**
  - 读取 CLAUDE.md
  - 读取 `reports/latest_status.md`（如果存在）
  - 读取 `logs/version_log.md`（如果存在）
  - 输出当前项目状态摘要
- **风险:** 低。只读操作，不影响会话
- **建议:** ✅ 启用（提高上下文连续性）

### 2. pre_delete_guard.sh
- **类型:** PreToolUse（Bash 命令）或 PreBash
- **触发:** 执行任何 Bash 命令前
- **用途:**
  - 拦截 `^rm -rf`、`^del /s`、`^rmdir /s`、`^format` 命令
  - 拦截对 `reports/citation_audit.md`、`final_draft/` 的写操作
  - 输出拦截警告并要求人工确认
- **风险:** 中。过度拦截可能干扰正常工作流
- **建议:** ⚠️ 谨慎启用。建议先只拦截 `rm -rf`，其他逐步放宽
- **检测模式建议:**
  ```bash
  # 匹配危险命令
  (rm\s+-rf|del\s+/s|rmdir\s+/s|format\s+)
  # 匹配敏感路径覆写
  (citation_audit\.md|final_draft/)
  ```

### 3. post_write_log.sh
- **类型:** PostToolUse（Write 操作）或 PostWrite
- **触发:** Write 工具调用后
- **用途:**
  - 检测写入路径是否为关键文件
  - 如果是，追加记录到 `logs/file_change_log.csv`
- **风险:** 低。但可能产生大量日志条目
- **建议:** ⚠️ 可选。如果日志噪音过大可关闭
- **关键文件列表:**
  - `reports/*`
  - `outputs/*`
  - `.claude/commands/*`
  - `.claude/rules/*`
  - `.claude/agents/*`
  - `CLAUDE.md`

### 4. session_end_summary.sh
- **类型:** Stop 或 SessionEnd
- **触发:** 会话结束时
- **用途:**
  - 生成 `reports/latest_status.md`
  - 记录本次会话完成了什么、未完成什么
  - 记录下一步最小动作
- **风险:** 低。只追加写，不删除
- **建议:** ✅ 启用（提高工作连续性）

---

## 启用方式

将需要启用的 hook 配置添加到 `.claude/settings.json`：

```json
{
  "hooks": {
    "SessionStart": "bash .claude/hooks/session_start_context.sh",
    "PreToolUse": {
      "matcher": "bash .claude/hooks/pre_delete_guard.sh {{tool}} {{input}}",
      "scope": "bash"
    },
    "PostToolUse": {
      "matcher": "bash .claude/hooks/post_write_log.sh {{tool}} {{input}}",
      "scope": "write"
    },
    "Stop": "bash .claude/hooks/session_end_summary.sh"
  }
}
```

---

## 人工确认清单

- [ ] 是否启用 SessionStart？
- [ ] 是否启用 PreDeleteGuard？（先只拦截 rm -rf）
- [ ] 是否启用 PostWriteLog？
- [ ] 是否启用 SessionEndSummary？
- [ ] hooks 脚本路径是否正确？
- [ ] hooks 脚本是否有执行权限？
