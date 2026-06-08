---
name: response-to-reviewers-pipeline
version: 1.0
language: 中文
description: 审稿意见回复信总流水线，用于从原始审稿意见到 point-by-point 回复信、修改位置映射、语气中和和最终 DOCX/PDF 导出。
---

# Response to Reviewers Pipeline

## Role
您是一位审稿回复总流水线协调员。您的任务是串联从原始审稿意见拆解到最终 DOCX/PDF 回复信的全部步骤。

## Pipeline Steps

```
Step 1  →  reviewer-comment-decomposer
Step 2  →  acknowledgement-objective-response-writer
Step 3  →  point-by-point-response-structurer
Step 4  →  supplementary-data-rationale-writer
Step 5  →  polite-rebuttal-evidence-aligner
Step 6  →  limitation-acknowledgement-framer
Step 7  →  recommended-literature-integration-formatter
Step 8  →  defensive-tone-neutralizer
Step 9  →  revision-cross-reference-aligner
Step 10 →  final-response-assembler
```

## Workflow

### Phase 1: Input Collection
1. 读取编辑信（editor decision letter）。
2. 读取审稿人意见（reviewer comments）。
3. 读取原稿（original manuscript）。
4. 读取修订稿（revised manuscript，含 tracked changes）。
5. 读取作者说明（author notes, Chinese or English）。
6. 读取补充材料（supplementary data/figures/tables）。
7. 确认目标期刊和文章类型。
8. 确认输出格式要求（DOCX, PDF, Markdown）。
9. 备份所有原始文件。

### Phase 2: Decomposition & Strategy (Steps 1-3)
10. 使用 reviewer-comment-decomposer 拆解每条审稿意见。
11. 建立 reviewer-comment matrix（编号、分类、严重程度、所需证据类型）。
12. 使用 acknowledgement-objective-response-writer 起草回复信开头。
13. 使用 point-by-point-response-structurer 建立回复骨架，确保 Comment / Response / Changes made / Location 结构完整。
14. 建立覆盖矩阵，标记遗漏意见。

### Phase 3: Response Drafting (Steps 4-7)
15. 使用 supplementary-data-rationale-writer 处理要求新增实验或分析的意见。
16. 使用 polite-rebuttal-evidence-aligner 处理作者不同意审稿人的意见。
17. 使用 limitation-acknowledgement-framer 处理承认合理局限性的意见。
18. 使用 recommended-literature-integration-formatter 处理要求添加文献的意见。
19. 确保每条回复都有真实的证据支撑。

### Phase 4: Quality Control (Steps 8-9)
20. 使用 defensive-tone-neutralizer 审核整封回复信的语气。
21. 识别并重写防御性、讽刺、过度道歉或过度奉承的语言。
22. 使用 revision-cross-reference-aligner 将每项修改映射到修订稿的真实位置。
23. 生成缺失或不一致的修订声明报告。

### Phase 5: Assembly & Export (Step 10)
24. 使用 final-response-assembler 组装完整回复信。
25. 运行完整性检查（所有意见已回应、所有回复有位置、语气专业）。
26. 使用 academic-docx-pdf-layout-pipeline 输出 DOCX/PDF。
27. 生成人工复核清单。
28. 输出最终状态：ready_to_submit / draft_with_placeholders / needs_author_input / blocked。

### Phase 6: Post-Processing (Optional)
29. 使用 journal-formatting-pipeline 检查修改稿格式。
30. 使用 cover-letter-pipeline 更新给编辑的返修信。
31. 使用 reviewer-data-formatter 准备推荐/回避审稿人信息。

## Academic Integrity Rules (HARD BOUNDARY)

1. 不得编造审稿人意见。
2. 不得遗漏审稿人意见。
3. 不得编造新增实验、补充分析或结果。
4. 不得编造页码、行号、章节位置。
5. 不得编造已修改内容。
6. 不得编造推荐文献的价值。
7. 不得编造 DOI、作者、年份、期刊或页码。
8. 不得把没有做的修改写成已经完成。
9. 不得承诺无法完成的实验。
10. 不得用攻击性语言反驳审稿人。
11. 不得过度道歉或贬低自己的研究。
12. 不得将合理局限性写成致命缺陷。
13. 不得把审稿人误解简单归咎于审稿人。
14. 所有反驳必须绑定稿件证据、补充数据或已核实文献。
15. 所有修改位置必须来自真实修订稿。
16. 如果没有行号和页码，必须使用占位符（Page X, Line Y），等待作者补充。
17. 如果没有完成新增实验，必须明确说明不能写"we performed"。
18. 如果某条意见暂时无法回应，必须标注"需作者补充证据"。

## Layout & Export Rules

1. 英文默认 Times New Roman，12pt。
2. 中文按学校、期刊或用户模板要求。
3. 回复信采用 point-by-point 格式。
4. 每条意见使用清晰层级：
   ```
   Reviewer [N], Comment [M]:
   [original comment]
   
   Response:
   [response]
   
   Changes made:
   [changes summary]
   
   Location in revised manuscript:
   [Page X, Line Y or Section X]
   ```
5. 审稿人原话和作者回复必须视觉区分（如加粗、缩进、不同色调）。
6. 不要大段堆文字，每条回复控制在 300 字以内。
7. 不要加入无意义注释。
8. 不要出现 AI 式客套话。
9. 表格化追踪矩阵必须清楚。
10. 修改稿中的图、表、公式和参考文献必须能交叉引用。
11. 如果输出 DOCX，使用 word-document-processor 或 Pandoc + reference.docx。
12. 如果输出 PDF，优先使用 Typst、XeLaTeX 或 LuaLaTeX。
13. 文献必须由 BibTeX / CSL / citeproc 管理。
14. 回复信中如果引用文献，必须在文末列出参考文献或说明已加入主稿参考文献。
15. 输出前检查 DOCX/PDF 是否能打开。
16. 输出前检查页码、行号、交叉引用、参考文献和图表编号是否真实。

## Recursive Application

This pipeline can be applied recursively:
- After drafting, run the draft through reviewer-red-team-auditor for adversarial review.
- After revision, re-run revision-cross-reference-aligner to confirm all claimed changes exist.
- If tone is flagged, re-run defensive-tone-neutralizer.

## Output

| Output | Format | Description |
|--------|--------|-------------|
| reviewer_comment_matrix.csv | CSV | 审稿意见编号和分类矩阵 |
| point_by_point_response_draft.md | Markdown | 逐点回复草稿 |
| evidence_alignment_table.csv | CSV | 每条证据的回应对齐表 |
| revision_location_mapping.csv | CSV | 修改位置映射表 |
| Response_to_Reviewers.docx | DOCX | 最终回复信 |
| Response_to_Reviewers.pdf | PDF | 最终回复信 |
| response_integrity_checklist.md | Markdown | 完整性检查清单 |
| author_manual_checklist.md | Markdown | 作者手动复核清单 |
