# .claude-plugin-draft — 科研工作台插件迁移草稿

> 状态: **DRAFT / 未激活**。此目录不属于任何 marketplace、未安装、不会被 Claude Code 自动加载。
> 目的: 预留的插件化迁移骨架（对应 CLAUDE.md 6 层架构表中"Plugin | .claude-plugin-draft/ | 预留迁移方案"）。
> 结构依据: Claude Code 官方插件规范（`plugin-dev:plugin-structure` skill，2026-09-27 读取）+ `anthropics/knowledge-work-plugins`（Apache-2.0，2026-09-27 页面核验）的参照实现。
> 边界: 只读参考；本目录不改动现有 `.claude/` 层的任何加载行为；激活需单独批准。

---

## 目录结构（照官方规范）

```
research-workbench/
├── .claude-plugin/
│   └── plugin.json          # 必需清单（name 必填，kebab-case）
├── .mcp.json                # MCP 服务器声明（当前为空槽位）
├── commands/                # 斜杠命令（.md + YAML frontmatter，自动发现）
├── agents/                  # 子代理定义（.md，自动发现）
├── skills/<name>/SKILL.md   # 技能（每技能一个子目录）
└── hooks/                   # 事件钩子（当前留空说明，见该目录 README）
```

关键规则（官方规范）：组件目录在**插件根**、不在 `.claude-plugin/` 里；只建实际用到的组件目录；插件内路径引用用 `${CLAUDE_PLUGIN_ROOT}`，禁止硬编码本机路径。

## 现有资产 → 插件组件映射（迁移蓝图）

| 现有位置 | 数量 | 插件内目标 | 迁移建议 |
|---------|------|-----------|---------|
| `.claude/commands/*.md` | 18 | `research-workbench/commands/` | 可直接迁（格式已一致：`name` + `description` frontmatter） |
| `.claude/agents/*.md` | 13 | `research-workbench/agents/` | 可直接迁 |
| `.claude/skills/` 通用模式类 | 3（agent-execution-patterns / agent-memory-patterns / decision-engine-patterns） | `research-workbench/skills/` | **优先迁**：通用模式、无本地依赖、可分发 |
| `.claude/skills/` 项目类 | 12（academic-paper、ppt-master、my-academic-research-master 等） | 待定 | 依赖本地路径/个人工作流 → 建议留项目级，或先路径参数化再迁 |
| `.claude/rules/*.md` | 10 | **无对应组件** | 插件规范无 rules 组件（结构决定，非选择）。两条路：①留项目级；②浓缩为 `workbench-governance` skill |
| `.claude/hooks/` | 草案阶段 | `research-workbench/hooks/hooks.json` | 迁移后随插件启用自动注册；注意幂等与 Windows 路径转义 |
| MCP（matlab / semantic-scholar / vision-bridge 等） | 用户级配置 | `research-workbench/.mcp.json` | 插件化声明会随插件**自动启动** → 迁移前先算工具描述预算（见 agent-memory-patterns 模式 6） |

范围说明：用户级 `~/.claude/skills` 不属本迁移范围（那是跨项目资产，非本仓组件）。

## 未来激活步骤（需要时逐项批准，当前不执行）

1. 建立 marketplace 清单（`.claude-plugin/marketplace.json`，含插件路径与元数据）
2. `claude plugin marketplace add <本地路径或仓库>`
3. `claude plugin install research-workbench@<marketplace>`
4. 验收清单：斜杠命令出现在 /help；技能可按描述触发；hooks 注册无报错；**无与项目级重复的组件**（见下）

## 已识别风险（草稿阶段不处理，迁移时逐条核）

- **重复加载**：插件组件与项目级同名组件并存会双份注册 → 迁移时须移除或改名原件。
- **路径可移植性**：插件内引用一律 `${CLAUDE_PLUGIN_ROOT}`；现有命令/技能中若有本机绝对路径需先清理。
- **MCP 预算**：插件声明的 MCP 随插件自动启动，工具描述会占上下文（参考 `agent-memory-patterns` 模式 6 的预算纪律）。
- **rules 无插件组件**：这是规范的结构限制，迁移方案必须显式设计（留层 or 转 skill），不能默认"迁过去就行"。
