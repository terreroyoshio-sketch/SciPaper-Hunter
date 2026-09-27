# hooks/ — 事件钩子（草稿槽位，当前无实现）

- 本工作台 hooks 仍处草案阶段（`.claude/hooks/`），无已验证脚本。
- 因此此目录**暂不建 hooks.json**——避免产生"配置存在 = 行为已验证"的误读（对应 evidence-levels 纪律）。
- 未来迁移注意：hooks 随插件启用自动注册；Windows 下的路径、引号与转义问题须先过专项审查；事件幂等性须验证。
- 可用事件参考：PreToolUse、PostToolUse、SessionStart、SessionEnd、UserPromptSubmit、PreCompact、Stop、SubagentStop、Notification。
