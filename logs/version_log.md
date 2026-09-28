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

## v0.3 — 2026-09-27 GitHub 候选融合批次（标准集）

### 新增
- `.claude/skills/agent-memory-patterns/`（SKILL.md + references/ecc-hindsight-evidence.md；用户级镜像同）
- `.claude/skills/decision-engine-patterns/`（SKILL.md + references/jev-laya-evidence.md；用户级镜像同）
- `.claude-plugin-draft/`（官方插件结构骨架 + 迁移蓝图；research-workbench/ 含 plugin.json、.mcp.json、commands/agents/skills/hooks 槽位说明；未激活）
- `reports/github_candidate_audit_20260927.md`（全量决策报告，A/P/T 核验标注 + 五档决策）
- `reports/open-science_gap_analysis_20260927.md`（对照审计：10 维度 + 4 吸收建议 + 5 不吸收理由）

### 规则
- 零安装：只提取模式，不部署来源项目；任何安装需单独批准
- 来源数字标注核验方式（API/页面/未核）与快照日期；自报与独立复测分开写
- 下轮候选：写作治理波（sepia/CCFA-Skills 等 6 项）、addyosmani/agent-skills、CLI-Anything（见决策报告）

## v0.4 — 2026-09-28 第二批：插件安装 + 写作波 + Addy 审计 + provenance 落地

### 新增
- `.claude/skills/completion-guard-patterns/`（SKILL.md + references/unlazy-stopthatshit-evidence.md；用户级镜像同）
- `reports/github_writing_wave_audit_20260928.md`（写作治理波 7 项决策报告）
- `reports/addy_agent_skills_audit_20260928.md`（Addy agent-skills 审计）

### 安装与外部变更（用户级 ~/.claude，均经批准）
- knowledge-work-plugins 市场 + 4 插件：bio-research 1.2.0 / data 1.1.0 / pdf-viewer 0.2.0 / cowork-plugin-management 0.2.2（user scope, enabled）
- sepia@sepia 0.12.2（只读快审通过后安装：MIT、无 hooks/MCP、脚本纯本地）
- agent-skills@addyosmani-agent-skills 0.6.10 → 0.6.11（经一次性 HTTPS 改写绕过 SSH 阻塞）
- 删除孤儿克隆 marketplaces/addy-agent-skills（备份 + deletion_log）

### 主 checkout（workbench-v2 线，未提交，留给你）
- `.codex` + `.agents` provenance skill → v1.1.1：新增 `references/artifact-and-review-evidence.md` + SKILL.md 引用行；.agents 由 1.0.0 同步至与 .codex 一致（既有漂移修复）
- 备份：`.research-ai/backups/20260928-115533-before-provenance-1.1.1/`

### 规则/发现
- claude CLI 位于 `%LOCALAPPDATA%\Claude-3p\claude-code\2.1.128\claude.exe`（不在 PATH）；插件更新遇 SSH 阻塞时，用一次性 `GIT_CONFIG_*` 环境变量改写为 HTTPS（不改全局 git 配置）

## v0.5 — 2026-09-28 CCFA 评审格式补充（方案 D 补做）

### 新增
- `.claude/skills/manuscript-review-format/`（SKILL.md + references/ccfa-source-notes.md；用户级镜像同）
- 只读 extract：`~/.claude/reference/ccfa-skills-extract-20260928/`（CCFA-Skills，MIT）

### 内容
- 三档固定格式（详细 14 节 / 写作 9 节 / 简明 5 节）、finding record 九字段与反证复核纪律、七维量表（1-5）+ 总评 1-10 + 置信度 1-5、scorecard 模板、改判条件表、跨版本对比三分规则
- 边界：只提取格式规范；其写作子量表与校验脚本留在源仓库（未安装）
