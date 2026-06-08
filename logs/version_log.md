# Version Log

## v0.1 — 2026-06-08 科研工作台基础架构

## v0.2 — 2026-06-08 办公学习工作台

### 新增
- `office-productivity-workbench` skill（SKILL.md + README.md）
- 11 个模板文件（templates/）
- 8 个规则参考（references/）
- 6 个工具脚本（scripts/）
- 10 个办公命令（commands/）
- 4 个办公规则（rules/）
- 6 个办公 subagents（agents/）
- 3 个 hooks 草案（hooks/）
- `reports/office_workbench_environment_audit.md`

### 规则
- 网页信息必须有 URL 和访问日期
- PDF 引用必须有页码
- 表格分析必须保留原始文件
- 隐私字段不可导出
- 自动化任务不经确认不可启用

### 新增
- `.claude/commands/` — 7 个快捷命令（idea, review-lit, check-citations, redteam, paper-draft, format-doc, pacs-precheck）
- `.claude/rules/` — 5 个约束规则（anti-fabrication, citation-policy, chinese-academic-style, medical-research-ethics, file-safety）
- `.claude/hooks/` — 4 个 hooks 草案（hook_plan, session_start_context, pre_delete_guard, post_write_log, session_end_summary）
- `.claude/agents/` — 6 个 subagent（literature-scout, evidence-matrix-builder, citation-auditor, statistical-reviewer, figure-table-editor, red-team-reviewer）
- `CLAUDE.md` — 项目根目录总规则
- `.claude-plugin-draft/` — 插件打包预留
- `logs/` — 结构化日志系统
- `reports/claude_code_workbench_audit.md` — 环境审计报告
- `reports/mcp_audit_and_recommendation.md` — MCP 审计报告

### 规则
- 反造假规则始终生效
- 引用核验通过前不进入写作
- 删除前必须确认
- 所有修改记录到 file_change_log.csv
