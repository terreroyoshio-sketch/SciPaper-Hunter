---
name: proposal-report-assembler
version: 1.0
language: 中文
description: 开题报告组装 skill，将前序节点分析结果整合为结构完整、数据来源清晰、排版规范的开题报告 Markdown、DOCX 和 PDF。
---

# Proposal Report Assembler

## Goals
- 组装完整开题报告
- 严格对应学校或学院模板（如未提供则使用默认学术格式）
- 每个章节标注数据来源（来自哪个 Step 的哪份输出）
- 消除重复内容
- 统一术语
- 输出 Markdown 源稿 + DOCX + PDF + 检查报告

## Constraints
- 不添加新的分析内容（仅组织已有材料）
- 不编造文献、研究结果、引用
- 不覆盖原始文件
- 不跳过排版检查
- 缺少模板时使用默认学术格式并在报告中说明
- 排版规则严格执行（见 Layout Rules）

## Layout Rules
1. 源稿优先 Markdown
2. 公式使用 LaTeX 数学语法
3. DOCX 使用 Pandoc 或 word-document-processor 生成
4. DOCX 样式使用 reference.docx 控制
5. PDF 优先使用 Typst、XeLaTeX 或 LuaLaTeX
6. 英文默认 Times New Roman
7. 中文按学校/学院/导师模板要求
8. 图题在图下，表题在表上
9. 图、表、公式必须编号
10. 正文必须交叉引用图、表、公式
11. 参考文献由 BibTeX/CSL/citeproc/RIS/EndNote 管理
12. 正文引用必须与参考文献列表对应
13. 不得编造 DOI、作者、年份、页码
14. 图表靠近正文首次引用
15. 减少无意义注释和 AI 式解释
16. 代码只保留必要注释
17. 最终必须输出 DOCX 和 PDF 的可打开性检查报告
18. 检查公式是否正常显示
19. 检查交叉引用是否正常解析
20. 检查参考文献是否一一对应
21. 检查图表编号是否连续
22. 依赖缺失时必须报告，不能假装导出成功

## Required Sections
- 题目
- 研究背景与问题提出
- 国内外研究现状
- 理论基础与文献评述
- 研究问题与研究目标
- 研究内容
- 研究方法与技术路线
- 创新点
- 研究意义
- 研究范围与限制
- 可行性分析
- 进度安排
- 参考文献
- 附录或文献台账

## Workflow
1. 接收前 9 个 Step 的所有输出
2. 按 Required Sections 组织内容
3. 标注每个章节的数据来源
4. 消除重复和矛盾
5. 统一术语
6. 生成 Markdown 源稿
7. 调用排版流水线导出 DOCX/PDF
8. 执行完整质量检查
9. 输出检查报告

## Output
- proposal_report_source.md
- proposal_report.docx
- proposal_report.pdf
- references.bib
- proposal_layout_check_report.md（公式/引用/图表/文件可打开性）
- citation_check_report.md（文献真实性/引用对应）
- crossref_check_report.md（交叉引用完整性）
