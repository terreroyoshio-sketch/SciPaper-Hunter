# Core Workflow Skills — 总说明

## 新增 Skills

| Skill | 来源 | 用途 |
|-------|------|------|
| summarize | 本地封装 | 长文提炼核心观点、结论和行动项 |
| agent-browser | mxyhi/ok-skills | 浏览器 Agent 工作流 |
| git-workflow | 本地封装 | Git 分支、提交、PR、版本管理 |
| tmux | 本地封装 | 长任务终端会话管理 |
| research | mxyhi/ok-skills (autoresearch) | 系统化研究、资料搜集 |
| refactor | mxyhi/ok-skills (improve-codebase-architecture) | 代码重构、结构优化 |
| docs | 本地封装 | README、API 文档、项目文档生成 |
| testing | mxyhi/ok-skills (tdd) | TDD 测试工作流 |
| skill-creator | 此前已安装 (superpowers) | 将工作流封装为 skill |
| find-skills | 此前已安装 | 搜索可靠 skill |

## 风险边界

- agent-browser: 禁止绕过登录、验证码、付费墙
- research: 不能替代学术文献核查，需与 keyword-literature-download 和 literature-boundary-lock 联用
- git-workflow: 强制推送和删除分支前必须人工确认
- tmux: Windows 上需使用替代方案
- 其余 skills 均为纯 Markdown 行为指南，无安全风险

## 组合方式

详见 `CORE_WORKFLOW_COMBINED_WORKFLOWS.md`。
