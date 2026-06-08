# Local Academic Research Pipeline

**文件:** `references/local_pipeline.md`
**用途:** 10 阶段标准科研流水线。

---

## Stage 0: 任务冻结

**输出:** `00_plan/project_plan.md`

**必须明确:**
1. 研究主题
2. 研究问题 (2-3 个)
3. 学科范围
4. 时间范围 (文献发表年份)
5. 目标期刊/课程要求
6. 输出格式 (LaTeX/Markdown/DOCX)
7. 文献数据库列表
8. 纳入标准
9. 排除标准
10. 人工确认点

---

## Stage 1: 文献检索

**调用:** `keyword-literature-download`, `deep-research`, `arxiv`, `semanticscholar`

**输出:** `01_literature/raw_candidates.csv`, `01_literature/search_log.md`

**每条文献必须记录:**
title, authors, year, venue, doi, url, abstract, database, query, retrieval_date, pdf_status, verification_status

---

## Stage 2: 文献筛选

**输出:** `01_literature/screened_literature.csv`

**评分维度:**
1. 主题相关性 (30%)
2. 方法代表性 (20%)
3. 发表质量 (15%)
4. 影响力 (15%)
5. 时效性 (10%)
6. 可验证性 (10%)

**分类:**
- A 类 (≥7.0): 核心，精读
- B 类 (5.0-7.0): 重要，关键论据
- C 类 (3.0-5.0): 背景，补充
- D 类 (<3.0): 剔除

---

## Stage 3: 证据卡片

**输出:** `02_notes/evidence_cards/{author_year}.md`

每篇 A/B 类文献包含:
1. 研究问题
2. 方法
3. 数据
4. 主要发现
5. 局限
6. 可支持论点
7. 不可过度解释边界
8. 是否已人工核查

---

## Stage 4: 主题聚类与 Taxonomy

**调用:** `critical-literature-review-pipeline`, `literature-theme-clustering`

**输出:** `03_structure/taxonomy.md`, `03_structure/outline_v1.md`

**要求:**
- 必须形成主题分类
- 必须指出争议和方法限制
- 必须指出研究空白
- 每个分类有代表文献

---

## Stage 5: 初稿写作

**调用:** `academic-paper`, `academic-abstract-pipeline`, `citation-format-syntax-auditor`

**输出:** `04_manuscript/sections/*.md`, `04_manuscript/manuscript.md`

**规则:**
1. 每段中心论点
2. 每段证据来源
3. 不写无来源的强判断
4. 不用文献摘要拼接
5. 不用公众号语言

---

## Stage 6: 图表生成

**输出:** `05_figures_tables/figure_table_plan.md`, `figures/*`, `tables/*`

**必须:** 文献流程图、Taxonomy 图、方法对比表、研究空白表
**规则:** 三线表、SVG 优先、图题含关键信息

---

## Stage 7: 引用核验

**调用:** `check_bibtex.py`, `check_citation_coverage.py`, `check_claim_source_alignment.py`

**输出:** `07_audit/citation_audit.md`, `07_audit/claim_source_alignment.md`

**10 项检查:**
1. BibTeX 存在性
2. 正文引用匹配 BibTeX
3. BibTeX 条目都被使用
4. DOI 真实性
5. 元数据一致性
6. AI 编造检查
7. 引用-论点匹配
8. 引用 A 论证 B
9. 数据来源
10. 过度结论

---

## Stage 8: 模拟审稿

**调用:** `academic-paper-reviewer`, `reviewer-red-team-auditor`

**输出:** `06_review/reviewer_round_1.md`, `06_review/revision_plan.md`

**5 个审稿角色:** 主编、领域审稿人、方法审稿人、引用审稿人、魔鬼代言人

---

## Stage 9: 修订

**输出:** `06_review/revision_log.md`, `07_audit/ai_failure_mode_check.md`

**检查:**
1. 逐条回应审稿意见
2. 修改未引入新错误
3. 未新增未核查引用
4. 未夸大创新点
5. 无 AI 风格痕迹
6. 有学术诚信风险

---

## Stage 10: 最终导出

**输出:** `08_outputs/final_draft/`

必须包含:
1. manuscript.md + .docx + .tex + .pdf
2. references.bib
3. literature_matrix.csv
4. citation_verification.csv
5. citation_audit.md
6. reviewer_reports.md
7. revision_log.md
8. submission_checklist.md
9. ai_usage_disclosure.md
