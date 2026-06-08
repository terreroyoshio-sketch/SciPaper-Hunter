# Claude Code Top 10 Skills — README

**安装日期**: 2026-05-15
**Skills 根目录**: C:\Users\张涵\.claude\skills\

---

## 一、本次核实的 10 类 Skills

### 第一梯队（优先安装）

| # | Skill | 实际名称 | 来源 | 安装路径 |
|---|-------|---------|------|---------|
| 1 | agent-browser | agent-browser | vercel-labs | .claude/skills/agent-browser/ |
| 2 | summarize | summarize | 本地中文版（参考 steipete/clawdis） | .claude/skills/summarize/ |
| 3 | find-skills | find-skills | vercel-labs/skills | .claude/skills/find-skills/ |

### 第二梯队（工作流沉淀）

| # | Skill | 实际名称 | 来源 | 安装路径 |
|---|-------|---------|------|---------|
| 4 | skill-creator | skill-creator | anthropics/skills | .claude/skills/skill-creator/ |
| 5 | tmux | tmux | 本地中文版 | .claude/skills/tmux/ |

### 工程扩展层

| # | Skill | 实际名称 | 来源 | 安装路径 |
|---|-------|---------|------|---------|
| 6 | testing | testing/tdd | anthropics/skills | .claude/skills/testing/ |
| 7 | docs | docs | 本地中文版 | .claude/skills/docs/ |
| 8 | refactor | improve-codebase-architecture | 本地 | .claude/skills/refactor/ |
| 9 | git-workflow | git-workflow | 本地中文版 | .claude/skills/git-workflow/ |
| 10 | research | research/autoresearch | anthropics/skills | .claude/skills/research/ |

## 二、每个 Skill 的用途

| Skill | 用途 |
|-------|------|
| agent-browser | 浏览器自动化：打开网页、点击、截图、抓取信息、测试 Web App |
| summarize | 长文压缩：论文、日志、会议纪要、文献提取要点和行动项 |
| find-skills | Skill 生态搜索入口：先找现成能力，避免重复造轮子 |
| skill-creator | 把高频工作流封装为可复用 SKILL.md |
| tmux | 长任务终端控制：多会话、后台进程、日志观察 |
| testing (tdd) | 测试驱动开发：红-绿-重构循环 |
| docs | 文档生成：README、API 文档、使用说明 |
| refactor | 代码重构：坏味道识别、复杂度控制、结构调整 |
| git-workflow | Git 工作流：commit、PR、changelog、冲突处理 |
| research | 技术调研：搜索、比较、形成结构化判断 |

## 三、风险边界

| Skill | 风险等级 | 关键限制 |
|-------|---------|---------|
| agent-browser | 中 | 不得绕过验证码/风控/付费墙；CDP 默认 9222 |
| summarize | 低 | 不得扩写或编造 |
| find-skills | 低 | 仅搜索推荐 |
| skill-creator | 低 | 仅创建 SKILL.md |
| tmux | 低 | 不得运行破坏性命令 |
| testing | 低 | 不提声称通过而不运行 |
| docs | 低 | 不得编造不存在的 API |
| refactor | 低 | 必须先出计划再修改 |
| git-workflow | 低 | 不得自 push/reset/clean/删除分支 |
| research | 低 | 不得编造来源 |

## 四、第一梯队 vs 第二梯队优先级

```
第一梯队（每天用）:
  agent-browser → 浏览器操作
  summarize    → 信息压缩
  find-skills  → 找现成技能

第二梯队（每周用）:
  skill-creator → 沉淀工作流
  tmux          → 长任务控制

工程扩展（按需用）:
  testing      → 写可靠代码
  docs         → 补文档
  refactor     → 清理代码
  git-workflow → 交付管理
  research     → 查资料
```

## 五、与已有 Skills 的组合方式

| 场景 | 组合方式 |
|------|---------|
| 学术调研 | find-skills → research → agent-browser → summarize → docs |
| 论文润色投稿 | summarize → nature-polishing → journal-formatting-pipeline |
| 代码重构 | testing → refactor → karpathy-guidelines → git-workflow |
| 文献综述 | keyword-literature-download → paper-reading → summarize → critical-literature-review-pipeline |
| Web 开发 | brainstorming → agent-browser (测试) → testing → git-workflow |
| 空间数据分析 | research → geopandas → scientific-visualization → docs |
| 项目申报 | nsfc-proposal-architecture-pipeline → technical-route-blueprint-planner → ppt-master |
| 长任务运行 | tmux → testing (观察) → summarize (日志) → docs |

## 六、适合与不适合的场景

| 场景 | 适合 | 不适合 |
|------|------|--------|
| 网页自动化 | agent-browser ✅ | 手动操作 |
| 信息压缩 | summarize ✅ | 重要信息不可逆压缩 |
| 找现成 skill | find-skills ✅ | 写定制 skill |
| 沉淀工作流 | skill-creator ✅ | 一次性任务 |
| 长任务控制 | tmux ✅ | 简单短命令 |
| 测试 | testing ✅ | 无测试环境 |
| 文档 | docs ✅ | 需要人工确认 |
| 重构 | refactor ✅ | 无测试覆盖的遗留代码 |
| Git 交付 | git-workflow ✅ | 紧急热修复 |
| 调研 | research ✅ | 需要一手实验 |
