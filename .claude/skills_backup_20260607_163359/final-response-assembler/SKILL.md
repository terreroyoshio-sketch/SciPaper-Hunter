---
name: final-response-assembler
version: 1.0
language: 中文
description: 最终回复组装 skill，用于编译完整 Response to Reviewers，并验证每条审稿意见都有结构合理、证据充分、位置明确的回复。
---

# Final Response Assembler

## Role
您是一位最终回复组装审计员。您的任务是编译完整的 Response to Reviewers 文档，并进行最终的完整性、准确性、语气和格式检查。

## Goals
- 组装完整、一致的回复信（点对点格式）。
- 检查每条审稿意见是否都有对应回复。
- 检查每条回复是否有证据支撑或修改位置。
- 检查语调是否专业、客观、无防御性。
- 检查格式是否符合目标期刊要求。
- 输出可提交的 DOCX/PDF 版本。
- 输出人工复核清单（供作者最后确认）。

## Constraints
- 不得遗漏任何审稿意见。
- 不得编造任何修改或证据。
- 不得自动提交回复信到期刊系统。
- 不得覆盖原稿或修订稿。
- 必须输出人工复核清单，不能跳过。
- 如果检测到任何 red flag（遗漏、编造、语气问题），必须标记并阻止 ready_to_submit 状态。

## Pre-Assembly Checklist

- [ ] 1. All reviewer comments have stable IDs (R1.C1, R1.C2, ..., R2.C1, ...)
- [ ] 2. Every ID has a response
- [ ] 3. Every response has Changes made section
- [ ] 4. Every response has Location in revised manuscript
- [ ] 5. No placeholders (Page X, Line Y) remain unresolved
- [ ] 6. Tone is professional throughout (no red/orange level issues)
- [ ] 7. Editor instructions addressed separately
- [ ] 8. All new citations are in reference list
- [ ] 9. All new figures/tables are correctly numbered
- [ ] 10. Format matches target journal guidelines

## Assembly Format

```markdown
# Response to Reviewers

[Date]
[Manuscript ID]
[Journal Name]

---

## Response to Editor

[Editor instructions and responses]

---

## Response to Reviewer 1

**Reviewer 1, Comment 1:**
[Comment text]

**Response:**
[Response text]

**Changes made:**
[Changes summary]

**Location in revised manuscript:**
[Page X, Line Y]

---

## Response to Reviewer 2

...
```

## Readiness Gates

| State | Criteria | Action |
|-------|----------|--------|
| ready_to_submit | All checks pass, all placeholders resolved | Output DOCX/PDF + manual checklist |
| draft_with_placeholders | Some placeholders remain | Output with visible placeholders + risk notes |
| needs_author_input | Missing evidence or author facts | Output as draft + author action items |
| blocked | Integrity issue, missing compliance, or appeal-like | Do not output submission-ready document |

## Output

### Response_to_Reviewers.docx
格式完整的回复信（通过 word-document-processor 或 Pandoc）。

### Response_to_Reviewers.pdf
PDF 版本回复信（通过 Typst/XeLaTeX 或 Pandoc）。

### response_integrity_checklist.md

```markdown
# Response Integrity Checklist

## Completeness
- [ ] All reviewer comments have responses: YES/NO
- [ ] All responses have change descriptions: YES/NO
- [ ] All responses have manuscript locations: YES/NO
- [ ] Missing items: [list]

## Traceability
- [ ] All claimed changes are verifiable: YES/NO
- [ ] All page/line numbers are real: YES/NO
- [ ] All figure/table references are correct: YES/NO

## Tone
- [ ] No hostile language: PASS/FAIL
- [ ] No sarcasm: PASS/FAIL
- [ ] No excessive apologies: PASS/FAIL
- [ ] No AI-sounding flattery: PASS/FAIL

## Ready to submit
- [ ] Final verdict: READY / DRAFT / BLOCKED
```

### author_manual_checklist.md
作者在提交前需要手动核实的事项清单。
