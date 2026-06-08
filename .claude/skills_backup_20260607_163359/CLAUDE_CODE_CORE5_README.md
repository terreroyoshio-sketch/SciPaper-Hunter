# Claude Code Core 5 Skills — README

---

## 1. Caveman (✅ 已安装)

**来源**: JuliusBrussee/caveman (60.5K stars, MIT)
**路径**: `.claude/skills/caveman/`
**触发**: 说"caveman mode"或"talk like caveman"

**用途**: 输出压缩 ~75%，保留技术准确性

**不适合场景**:
- 论文正文、正式申报书、教学推导
- 用户要求详细讲解时需临时关闭
- 涉及复杂逻辑推理可能需要降低压缩强度

## 2. Claude Memory Compiler (⚠️ 仅核实，未安装)

**来源**: coleam00/claude-memory-compiler
**状态**: 因无 LICENSE + hooks 隐私风险，仅核实不安装

**隐私风险**: 捕获全量会话内容写入明文文件。包含对话中出现的密钥、Token 和未公开数据。

## 3. Paper2Code (✅ 已安装)

**来源**: PrathamLearnsToCode/paper2code (MIT)
**路径**: `.claude/skills/paper2code/`
**触发**: `/paper2code <arXiv URL>`

**用途**: 论文 → citation-anchored 代码。每个模块标注论文章节/公式，未明确部分标注 UNSPECIFIED。

**边界**:
- 不保证代码正确性
- 不下载数据集
- 不实现 baseline
- 必须用测试和小样例验证

## 4. CLAUDE.md Optimizer (✅ 本地 wrapper)

**路径**: `.claude/skills/claudemd-optimizer/`

**用途**: 审计、压缩、重构 CLAUDE.md。检查冗长、重复、矛盾、过期和敏感信息。

**规则**:
- 不自动覆盖原文件
- 必须先备份
- 输出草稿待确认

## 5. TestDrift / Testing (⚠️ TestDrift 未找到，采用等效方案)

**来源**: TestDrift 无可靠仓库。替代方案：
- testing/tdd — Anthropic 官方 TDD
- webapp-testing — Playwright E2E
- Addy /test — slash command
- testdrift-wrapper — 本地创建的变更缺口检测

## 推荐启用顺序

```
1. CLAUDE.md Optimizer  → 先整理项目上下文
2. testing/tdd/TestDrift → 先保证不遗漏测试
3. Caveman              → 再降低 token 和废话
4. Paper2Code           → 仅在论文复现任务中启用
5. Memory Compiler      → 最后谨慎评估后启用（目前不安装）
```

## 与已有 Skills 组合

| 场景 | 组合 |
|------|------|
| 高效开发 | CLAUDE.md Optimizer → testing → Caveman |
| 论文复现 | paper-reading → paper-parse → Paper2Code → testing → docs |
| 项目初始化 | grill-with-docs → /spec → CLAUDE.md Optimizer → docs |
| Token 治理 | Caveman + summarize + CLAUDE.md Optimizer |
| 测试补齐 | git diff → testdrift-wrapper → testing → git-workflow |
