# Environment Audit — research-idea-conflict-miner

**Date:** 2026-06-07

---

## 1. 可用工具

| 工具 | 版本 | 状态 |
|------|------|------|
| Git | 2.54.0 | ✅ |
| Python | 3.14.2 | ✅ |
| Node.js | v24.15.0 | ✅ |
| Pandoc | 3.9.0.2 | ✅ |
| Playwright | 1.59.0 | ✅ |
| Zotero | 已安装 | ✅ |
| LibreOffice | 已安装 | ✅ |
| Visio | 已安装 | ✅ |
| arxiv (Python) | 3.0.0 | ✅ |
| semanticscholar (Python) | 0.12.0 | ✅ |
| scholarly (Python) | 1.7.11 | ✅ |

## 2. 现有 Skills

| Skill | 位置 | 状态 |
|-------|------|------|
| using-superpowers | `~/.claude/skills/` | ✅ |
| brainstorming | `~/.claude/skills/` | ✅ |
| keyword-literature-download | `~/.claude/skills/` | ✅ |
| deep-research | `.claude/skills/` (ARS) | ✅ |
| academic-paper | `.claude/skills/` (ARS) | ✅ |
| academic-paper-reviewer | `.claude/skills/` (ARS) | ✅ |
| academic-pipeline | `.claude/skills/` (ARS) | ✅ |
| critical-literature-review-pipeline | `~/.claude/skills/` | ✅ |
| literature-boundary-lock | `~/.claude/skills/` | ✅ |
| citation-format-syntax-auditor | `~/.claude/skills/` | ✅ |
| objectivity-calibration-auditor | `~/.claude/skills/` | ✅ |
| reviewer-red-team-auditor | `~/.claude/skills/` | ✅ |
| my-academic-research-master | `.claude/skills/` | ✅ |
| autonomous-survey-agent | `.claude/skills/` | ✅ |

## 3. 缺失项

| 项 | 替代方案 |
|----|---------|
| 无缺失工具 | —— |
| Markitdown (未安装) | 使用 Pandoc 替代文档转换 |

## 4. 最稳执行路线

1. `arxiv` + `semanticscholar` Python API 做文献检索（最稳）
2. ARS `deep-research` 辅助深度研究
3. ARS `academic-paper-reviewer` + `reviewer-red-team-auditor` 做审稿模拟
4. Pandoc 做格式转换
5. 本地 CSV 做证据矩阵记录
