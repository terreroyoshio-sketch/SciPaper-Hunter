# ARS Installation Report

**Date:** 2026-06-07
**Repository:** Imbad0202/academic-research-skills (v3.11.1)

---

## 1. 安装方式

由于当前 Claude Code 环境不支持 `/plugin` 命令（claude CLI 在 PATH 中不可用），使用手动安装：

```bash
git clone --depth 1 https://github.com/Imbad0202/academic-research-skills.git external/academic-research-skills
cp -R external/academic-research-skills/deep-research     .claude/skills/deep-research
cp -R external/academic-research-skills/academic-paper     .claude/skills/academic-paper
cp -R external/academic-research-skills/academic-paper-reviewer .claude/skills/academic-paper-reviewer
cp -R external/academic-research-skills/academic-pipeline .claude/skills/academic-pipeline
```

---

## 2. 四个 Skill 的存在状态

| Skill | 路径 | SKILL.md | 状态 |
|-------|------|----------|------|
| deep-research | `.claude/skills/deep-research/SKILL.md` | ✅ 可读取 | ✅ 已安装 |
| academic-paper | `.claude/skills/academic-paper/SKILL.md` | ✅ 可读取 | ✅ 已安装 |
| academic-paper-reviewer | `.claude/skills/academic-paper-reviewer/SKILL.md` | ✅ 可读取 | ✅ 已安装 |
| academic-pipeline | `.claude/skills/academic-pipeline/SKILL.md` | ✅ 可读取 | ✅ 已安装 |

---

## 3. 外部仓库备份

完整仓库保留在 `external/academic-research-skills/`（~920 文件），包含：
- 4 个核心 skills
- `agents/` — 插件代理文件
- `commands/` — 10 个 `/ars-*` 快捷命令
- `docs/` — 架构/设置/性能文档
- `evals/` — 评估基础设施
- `shared/` — 模式、合同、评分标准、模板
- `scripts/` — Python 适配器、验证器、迁移工具

---

## 4. License 和使用限制

- **License:** CC-BY-NC 4.0 (Creative Commons Attribution-NonCommercial 4.0 International)
- **署名要求:** `Based on Academic Research Skills by Cheng-I Wu (https://github.com/Imbad0202/academic-research-skills)`
- **允许:** 教学、学术研究、个人使用
- **禁止:** 商业使用、商业研究、企业部署
- **不影响:** 用 ARS 辅助写的论文本身不属于"商业使用"

---

## 5. 是否需要重启 Claude Code

Skill 文件是运行时加载的。当前会话已可直接发现 ARS skills。无需重启。

---

## 6. 是否建议开启 auto-update

建议手动管理。手动安装的情况下，更新流程为：

```bash
cd external/academic-research-skills
git pull --depth 1
# 然后重新复制 4 个 skill 目录到 .claude/skills/
```

不建议设 cron 自动更新，因为：
1. 新版本可能修改 SKILL.md 结构
2. 我们可能有自定义修改
3. 手动控制更安全

---

## 7. Claude Code 最终 skills 结构

```
.claude/skills/
├── deep-research/        # ARS — 13-agent 研究团队
├── academic-paper/       # ARS — 12-agent 论文写作
├── academic-paper-reviewer/  # ARS — 7-agent 审稿
├── academic-pipeline/    # ARS — 10 阶段流水线
├── ai-powerpoint-research-workflow/  # 已有
├── autonomous-survey-agent/          # 已有（之前创建）
└── sci-research-writing-narrative/   # 已有
```
