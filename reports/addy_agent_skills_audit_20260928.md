# Addy agent-skills 审计报告（2026-09-28）

> 对照对象: [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills)（99.5k★, MIT, 590 commits, pushed 2026-09-26）
> 审计范围: **已装插件 v0.6.10**（本地实读）+ 上游 main（页面级核验）
> 背景: 用户全局 CLAUDE.md 已引用 `ADDY_AGENT_SKILLS_ENGINEERING_PRINCIPLES.md`（其 15 条工程原则早已吸收）
> 边界: 只读审计；更新/清理等动作见"待决策"

---

## 现状

| 项 | 值 |
|----|----|
| 已装插件 | `agent-skills@addyosmani-agent-skills` v0.6.10（user scope, enabled） |
| 安装路径 | `~/.claude/plugins/cache/addyosmani-agent-skills/agent-skills/0.6.10/` |
| 上游当前版本 | **v0.6.11**（plugin.json, main 分支，2026-09-28 核验） |
| 版本差 | 落后 1 个 patch 版本（0.6.10 → 0.6.11），可更新；⚠️ 版本序列不单调（见发现 1） |
| 许可 | MIT（本地 LICENSE 文件实读确认） |

## 插件内容清单（本地 v0.6.10 实读）

| 组件 | 数量 | 说明 |
|------|------|------|
| `skills/` | 25 | 24 生命周期 + 1 meta（using-agent-skills）；覆盖 define（interview-me/idea-refine/spec/constraints）→ plan → build（TDD/incremental/context-engineering/doubt-driven…）→ verify → review → ship |
| `.claude/commands/` + `commands/` | 9 | `/spec` `/plan` `/build` `/test` `/constraints` `/review` `/webperf` `/code-simplify` `/ship`（.md 给 Claude Code，.toml 给其他宿主） |
| `agents/` | 4 | code-reviewer / test-engineer / security-auditor / web-performance-auditor |
| `references/` | 7 | definition-of-done、testing-patterns、security-checklist、performance-checklist、accessibility-checklist、observability-checklist、orchestration-patterns |
| `hooks/` | 8 文件 | ⚠️ **未注册**（无 hooks.json，plugin.json 也未声明 hooks 字段）→ 不会自动运行；属可选手动配置内容（sdd-cache / simplify-ignore / session-start 等脚本 + 文档） |
| 其他 | — | evals/、scripts/、docs/、AGENTS.md |

## 设计要点（其自述，值得注意的几条）

- **"Process, not prose"**：技能是可执行流程与质量门，不是散文。
- **Anti-rationalization 表**：把 agent 常见借口逐条列出并给出反驳——与你的"禁止抄近道"纪律同构。
- **Verification is non-negotiable**；**Progressive disclosure**（SKILL.md 只在需要时加载 references）。
- 贡献标准：specific / verifiable / battle-tested / minimal（四个词本身就是审 skill 的尺子）。

## 发现

1. **可更新，但有版本序列异常**：本地 marketplace 克隆（2026-05-21 快照）里 plugin.json 写的是 **1.0.0**，上游 main 现为 **0.6.11**，已装为 **0.6.10**——同一仓库版本号由 1.0.0 回落到 0.6.x，序列不单调（原因未查，疑似重构后重新编号）。**按 0.6.x 序列，已装 0.6.10 < 上游 0.6.11，可更新**。操作顺序：先 `claude plugin marketplace update addyosmani-agent-skills` 刷新本地克隆（当前是 5 月快照），再 `claude plugin update agent-skills@addyosmani-agent-skills`（重启后生效；更新前备份 cache 目录）。
2. **孤儿克隆**：`~/.claude/plugins/marketplaces/addy-agent-skills/`（May 21 09:41）与 `addyosmani-agent-skills/`（May 21 11:54）内容相同、均为 addyosmani/agent-skills 的克隆；但 `known_marketplaces.json` 只登记了后者 → **前者是残留孤儿**（不在任何注册表引用中）。清理需批准，并记入 `logs/deletion_log.md`（file-safety F1/F2）。
3. **hooks 未注册**：虽有 hooks/ 目录（含 sdd-cache、simplify-ignore、session-start 脚本），无 hooks.json → 不拦截、不自动执行。无拦截风险，也意味着这些能力当前**未启用**。
4. **与已装体系的交集**：其 4 个 personas 与你已装的 `pr-review-toolkit`、`security-scanning`、`code-review` 有功能重叠（不同供应商的同名职责）；其 25 技能中与你本地 skills 有部分同名（如 `code-simplification`、`test-driven-development`）——不同来源、可共存，但调用时注意区分来源。
5. **已知上游坑（#361）**：用 `npx skills add` 按单技能安装只拷贝 `skills/<name>/`，**不含 repo 级 `references/`**（7 张检查清单会丢）。你装的是整插件，不受影响；但若将来按技能拆分安装需注意。

## 待决策（等你点名）

- **A. 更新到 0.6.11**：一条命令 + 重启；低风险。
- **B. 清理孤儿克隆** `marketplaces/addy-agent-skills/`：删除前备份 + 记 deletion_log。
- **C. 保持现状**。
