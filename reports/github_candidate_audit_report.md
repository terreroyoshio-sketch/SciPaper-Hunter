# GitHub 候选项目审计报告

> 审计日期: 2026-05-27
> 审计范围: 科研插图、论文写作、文档排版、学术工作流相关开源项目

---

## 审计结论总表

| 项目 | Stars | License | SKILL.md | 推荐等级 | 决策 |
|------|-------|---------|----------|---------|------|
| dwzhu-pku/PaperBanana | 6.4k | Apache-2.0 | ❌ | B | 创建本地 wrapper |
| llmsresearch/paperbanana | 1.8k | MIT | ❌（但有 MCP + skills） | A | 安装 + 配置 MCP |
| elpsykongloo/PaperBanana-Pro | — | Apache-2.0 | ❌ | C | 暂缓，等人工 |
| Mapika/nice-figures | — | MIT | ✅ | A | 插件安装 |
| wanshuiyin/ARIS | 6.9k | — | ✅（65+ skills） | A | 按需参考（不安装全部） |
| Yuan1z0825/nature-skills | 3.4k+ | — | ✅（nature-figure 等） | A | 已安装 ✓ |

---

## 详细审计表

### 1. dwzhu-pku/PaperBanana

| 项目 | 内容 |
|------|------|
| GitHub URL | https://github.com/dwzhu-pku/PaperBanana |
| 用途 | 学术插图自动生成（原论文作者 fork） |
| README | ✅ 详细 |
| LICENSE | ✅ Apache-2.0 |
| SKILL.md | ❌ 无 |
| 最近维护 | 64 commits，活跃 |
| 安装方式 | git clone + uv + Python 3.12 |
| 依赖 | uv, Python 3.12, requirements.txt |
| 需要 API Key | ✅ Google Gemini 或 OpenRouter |
| 需要浏览器登录 | ❌ 不需要 |
| 读取 Cookie/Token/密码 | ❌ 不涉及 |
| 上传本地文件 | ✅ 支持（上传文本和参考图） |
| 版权风险 | 低（Apache-2.0 但 Google 已申请核心专利） |
| 是否推荐安装 | ⚠️ 不优先推荐，代码较重 |
| 推荐方式 | 学习其 pipeline 设计思路，实际使用选 llmsresearch 版 |

**风险等级：** 中
**决策：** B — 创建本地 wrapper，引用其设计思路

### 2. llmsresearch/paperbanana

| 项目 | 内容 |
|------|------|
| GitHub URL | https://github.com/llmsresearch/paperbanana |
| 用途 | PaperBanana 社区实现 + 扩展（MCP、CLI、Studio） |
| README | ✅ 详细 |
| LICENSE | ✅ MIT |
| SKILL.md | ❌ 无，但有 `.claude/skills/`（3 个 slash commands） |
| 最近维护 | 229 commits，v0.1.2 (2026-02-13) |
| 安装方式 | `pip install paperbanana[mcp]` 或 `pip install paperbanana[studio]` |
| 依赖 | Python 3.10+, pydantic v2, typer |
| 需要 API Key | ✅ OpenAI / Google Gemini / Azure |
| 需要浏览器登录 | ❌ 不需要 |
| 读取 Cookie/Token/密码 | ❌ 不涉及 |
| 上传本地文件 | ✅ 支持本地文件输入（PDF/CSV/JSON），通过 API 调用 |
| 版权风险 | 低（MIT 许可） |
| 是否推荐安装 | ✅ **推荐** |

**风险等级：** 低
**决策：** A — 建议安装 + 配置 MCP

### 3. elpsykongloo/PaperBanana-Pro

| 项目 | 内容 |
|------|------|
| GitHub URL | https://github.com/elpsykongloo/PaperBanana-Pro |
| 用途 | PaperBanana 增强 Fork（中文 GUI、2K/4K 高清） |
| README | 需核实 |
| LICENSE | ✅ Apache-2.0 |
| SKILL.md | ❌ 无 |
| 最近维护 | 需核实 |
| 安装方式 | git clone |
| 风险等级 | 中（社区 Fork，稳定性和维护持续性不明确） |

**决策：** C — 暂缓，等待人工授权

### 4. Mapika/nice-figures

| 项目 | 内容 |
|------|------|
| GitHub URL | https://github.com/Mapika/nice-figures |
| 用途 | Soft-pastel 风格 matplotlib 科研图 Claude Code 插件 |
| README | ✅ 详细 |
| LICENSE | ✅ MIT |
| SKILL.md | ✅ 有（`plugins/nice-figures/skills/nice-figures/SKILL.md`） |
| 最近维护 | 6 commits |
| 安装方式 | Claude Code 插件管理器 |
| 依赖 | matplotlib, numpy |
| 需要 API Key | ❌ 不需要 |
| 版权风险 | 低（MIT 许可） |
| 是否推荐安装 | ✅ **推荐**（轻量、美观、即装即用） |

**风险等级：** 低
**决策：** A — 建议通过 Claude Code 插件安装

### 5. wanshuiyin/Auto-claude-code-research-in-sleep (ARIS)

| 项目 | 内容 |
|------|------|
| GitHub URL | https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep |
| 用途 | 全自动科研工作流（65+ skills，含 paper-illustration） |
| README | ✅ 详细（含中文版） |
| LICENSE | 需核实 |
| SKILL.md | ✅ 65+ 独立 SKILL.md |
| 最近维护 | 活跃，持续更新 |
| 安装方式 | git clone 或参考各 SKILL.md |
| 依赖 | 无（纯 Markdown） |
| 需要 API Key | 部分 skill 需要（如使用跨模型协作） |
| 是否推荐安装 | ⚠️ 不安装全部，按需参考 paper-illustration 和 paper-slides |

**风险等级：** 低
**决策：** A — 按需参考，不批量安装

### 6. Yuan1z0825/nature-skills

| 项目 | 内容 |
|------|------|
| GitHub URL | https://github.com/Yuan1z0825/nature-skills |
| 用途 | Nature 标准论文写作 + 科研绘图技能包 |
| README | ✅ |
| SKILL.md | ✅（nature-figure, nature-polishing 等） |
| 最近维护 | 2026-04 活跃 |
| 是否推荐安装 | ✅ **已安装**（`nature-figure` 已在本地 skills 中） |

**风险等级：** 低
**决策：** A — 已安装，无需重复操作

---

## 推荐等级说明

| 等级 | 含义 |
|------|------|
| A | 建议安装/使用 — 风险低、维护好、直接相关 |
| B | 建议创建本地 wrapper — 功能相关但不便直接安装 |
| C | 暂缓 — 需要你确认后再操作 |
| D | 不建议安装 — 风险/版权/维护问题 |

---

## 总计

- **A 级（建议直接使用）：** 3 项 — llmsresearch/paperbanana、nice-figures、ARIS（按需参考）
- **B 级（创建 wrapper）：** 1 项 — dwzhu-pku/PaperBanana（设计参考）
- **C 级（暂缓）：** 1 项 — PaperBanana-Pro
- **D 级（不建议）：** 0 项
- **已安装：** 1 项 — nature-skills（nature-figure 已在本地）
