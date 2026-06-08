---
name: claudemd-optimizer
version: 1.0
language: 中文
description: CLAUDE.md 项目上下文优化 skill，用于审计、压缩和重构 CLAUDE.md，使 Claude Code 获得更准确、更高信噪比、更安全的项目上下文。
---

# CLAUDE.md Optimizer

## Goals
- 审计 CLAUDE.md 是否过长、过泛、重复、矛盾或过期。
- 提取真正影响项目执行的规则。
- 删除无效套话和低价值说明。
- 检查敏感信息（密钥、密码、Token、隐私路径）。
- 将规则拆成项目概览、命令、架构、测试、禁用操作、风格约定和常见坑。
- 输出优化建议和新草稿。

## Constraints
- 不得自动覆盖原 CLAUDE.md。
- 必须先备份。
- 不得删除关键安全规则。
- 不得引入不存在的项目结构。
- 不得编造技术栈。
- 不得保留 Token、密码、密钥或隐私路径。

## Workflow
1. 读取 CLAUDE.md。
2. 扫描项目结构（package.json、pyproject.toml、requirements.txt、README、docs）。
3. 对 CLAUDE.md 打分（冗长度、准确度、时效性、安全性）。
4. 标记冗余、重复、矛盾、过期和敏感内容。
5. 输出精简版草稿。
6. 生成变更说明。
7. 等用户确认后再写入。

## Scoring
- 冗长度: 是否包含低价值说明、背景故事、通用 AI 建议
- 准确度: 规则是否与项目实际结构一致
- 时效性: 是否仍反映当前架构
- 安全性: 是否包含密钥、密码、Token 或暴露敏感路径

## Output
- claude_md_audit_report.md
- CLAUDE.optimized.draft.md
- sensitive_info_findings.md
- rewrite_diff.md
