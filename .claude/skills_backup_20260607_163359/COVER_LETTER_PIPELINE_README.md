# Cover Letter 生成流水线 Skills — 总说明

## 背景

本组 skills 的核心目标：让 Claude Code 在写论文投稿信、Cover Letter、投稿前声明、伦理合规声明、推荐审稿人清单、期刊匹配说明时，能够**严格基于已核实稿件数据**生成专业、客观、简洁、符合顶刊要求的投稿信。

**核心禁止**：
- 不得凭空生成稿件元数据、作者、编辑、期刊范围、研究发现
- 不得编造伦理批准号、基金号、推荐审稿人信息
- 所有内容必须来自用户提供的核实材料

## 新增 Skills 清单

| 序号 | 技能名称 | 用途 |
|------|---------|------|
| 1 | `manuscript-metadata-extractor` | 提取标题、通讯作者、机构、邮箱 |
| 2 | `journal-editor-verification-auditor` | 核查期刊/编辑信息并生成称呼 |
| 3 | `research-significance-compressor` | 压缩研究背景和空白为 1-2 句 |
| 4 | `empirical-contribution-extractor` | 提取主要实证发现和理论贡献 |
| 5 | `journal-scope-alignment-writer` | 将贡献与期刊收稿范围对齐 |
| 6 | `originality-status-statement-generator` | 生成原创、未发表、未一稿多投声明 |
| 7 | `ethics-compliance-statement-formatter` | 格式化利益冲突、资金、伦理声明 |
| 8 | `reviewer-data-formatter` | 格式化推荐/回避审稿人信息 |
| 9 | `academic-tone-standardizer` | 删除奉承、夸张、AI 痕迹 |
| 10 | `cover-letter-assembly-length-auditor` | 组装修信、控制 400 词以内 |
| 11 | `cover-letter-pipeline` | 完整流水线（串联全部模块） |

## 完整调用流程

```
第一阶段：数据提取与核实
  manuscript-metadata-extractor
  journal-editor-verification-auditor

第二阶段：学术综合与对齐
  research-significance-compressor
  empirical-contribution-extractor
  journal-scope-alignment-writer

第三阶段：声明与伦理合规
  originality-status-statement-generator
  ethics-compliance-statement-formatter
  reviewer-data-formatter
  academic-tone-standardizer
  cover-letter-assembly-length-auditor
```

## 为什么 Cover Letter 不能凭空生成

| 问题 | 风险 |
|------|------|
| 猜测主编姓名 | 可能送到错误编辑，造成负面第一印象 |
| 编造期刊范围 | 审稿编辑可能直接看出不匹配 |
| 编造基金号/伦理号 | 一旦被核查，可能直接退稿或被认为学术不端 |
| 编造推荐审稿人 | 邮箱不存在导致审稿延误，或被发现虚构 |

## 为什么伦理、资金、利益冲突声明必须严格依据用户信息

这些声明具有法律效力。编造基金号、伦理批准号或隐瞒利益冲突可能导致：
- 退稿
- 撤稿
- 机构调查
- 资助方追责

## 组合方式

详见 `COVER_LETTER_COMBINED_WORKFLOWS.md`。
