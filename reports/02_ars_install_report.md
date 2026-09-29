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

---

## 8. 2026-09-18 升级附记（v3.11.1 → v3.22.0）

**触发**：用户看到一份 ARS 提问手册，描述的是 v3.20.1 的功能；核对发现本地为 v3.11.1，手册里约一半场景会落空。

**升级前的实测差距**（v3.11.1 本地）：
- 斜杠命令只有 5 个（ars-audit / ars-draft / ars-lit / ars-pipeline-test / ars-review），
  手册依赖的 `/ars-revision-coach`、`/ars-rebuttal-audit`、`/ars-outline`、`/ars-plan`、
  `/ars-reviewer`、`/ars-disclosure`、`/ars-3w`、`/ars-citation-check`、`/ars-full` 全部不存在。
- 模式实测缺失：revision-coach 0 文件、rebuttal-audit 0、claim-strength 梯子 0、答辩委员会变体 0。

**发现的一个长期缺陷**：4 个技能大量引用 `shared/...`（academic-paper 18 个文件、
academic-paper-reviewer 9、academic-pipeline 13、deep-research 16），引用写作 `../../shared/`，
即 `shared/` 必须是技能目录的同级。**但原始安装（见 §1）只拷了 4 个技能目录，从未拷 `shared/`**，
因此这些引用一直是断链的。

**本轮操作**（全部在 worktree `elegant-almeida-f7d963` 内，主仓未动）：
1. `git fetch --depth 1 origin main` → 上游 HEAD `3c546bc` (2026-09-16)，**实际版本 v3.22.0**
   （比手册说的 v3.20.1 更新）。
2. 用 `git archive origin/main | tar -x` 非破坏性解出到 `~/.claude/reference/ars-v3.20-extract/`。
3. 验证上游确有手册所述功能：`commands/` 下 16 个 `ars-*.md`（含 revision-coach、rebuttal-audit、
   outline、plan、reviewer、disclosure、3w、citation-check、full）；`claim-strength` 命中 32 个 md、
   `committee` 113 个、`direct-mode` 14 个。
4. 备份原版本到 `backups/ars_v3.11.1_20260918/`（185 个文件）。
5. 安装：4 个技能更新（63/28/30/53 文件）+ **补上 `shared/`（149 文件）** + 16 个命令。
6. 验证：45 个被引用的 `shared/` 路径**全部命中，0 缺失**。

**未做**：未更新主仓（`C:/Users/张涵/Desktop/项目/skill/.claude/`）——主仓当时在 `test/office-smoke`
分支且有未提交改动，不宜叠加。两份副本升级前完全相同，升级后 worktree 领先。

**许可**：仍为 CC-BY-NC 4.0（非商用），Copyright (c) 2026 Cheng-I Wu，未变。
