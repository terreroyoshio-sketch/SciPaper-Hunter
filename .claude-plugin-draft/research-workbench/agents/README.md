# agents/ — 子代理定义（草稿槽位，当前为空）

- 格式：`.md` + YAML frontmatter（`description`、capabilities），kebab-case 文件名，放入即自动发现。
- 迁移来源：`.claude/agents/` 共 13 个（citation-auditor、red-team-reviewer、statistical-reviewer 等，清单见 `../../README.md`）。
- 迁移时核对：代理职责描述是否含本机路径；与插件 skills 的引用关系是否仍成立。
