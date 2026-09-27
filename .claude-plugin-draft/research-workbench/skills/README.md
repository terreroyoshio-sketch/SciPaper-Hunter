# skills/ — 技能（草稿槽位，当前为空）

- 格式：每个技能一个子目录 + `SKILL.md`（frontmatter 含 `name`、`description`）。
- 迁移优先级：先迁 3 个通用模式技能 —— `agent-execution-patterns`、`agent-memory-patterns`、`decision-engine-patterns`（无本地依赖、可分发）。
- 项目类技能（academic-paper、ppt-master 等 12 个）中含本机路径或个人配置者，先做路径参数化改造再迁，否则破坏插件可移植性。
- 迁移后须删除项目级原件或改名，避免双份注册（见 `../../README.md` 风险节）。
