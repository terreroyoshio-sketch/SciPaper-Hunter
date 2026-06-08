# NSFC 基金架构 — 与已有 Skills 组合工作流

---

## A. 写国自然申请书全流程

```
1. using-superpowers
   先明确申请类别、研究方向、目标学部、篇幅、截止时间和验收标准。

2. brainstorming
   生成 2 到 3 套研究构想方案，但不直接定稿。

3. keyword-literature-download
   检索并构建核心文献库。

4. markitdown
   将论文、前期成果、申请书模板转为 Markdown。

5. critical-literature-review-pipeline
   构建立项依据中的批判性文献综述。

6. nsfc-proposal-architecture-pipeline
   完成基金申请书整体逻辑架构审计。

7. objective-innovation-auditor-pipeline
   审计特色与创新点是否成立。

8. nsfc-reviewer-simulation-auditor
   模拟函评专家质询。
```

---

## B. 写"立项依据"

```
1. literature-boundary-lock
   锁定人工核实文献。

2. literature-theme-clustering
   按主题聚类文献。

3. methodological-limitation-synthesizer
   提取方法论局限。

4. proposal-rationale-gap-locator
   构建宏观需求、研究进展、具体空白、项目方案的论证结构。

5. objectivity-calibration-auditor
   防止过度贬低前人研究。
```

---

## C. 写"关键科学问题与研究内容"

```
1. key-scientific-question-extractor
   提炼关键科学问题。

2. objective-content-alignment-planner
   建立问题、目标、内容、预期结果矩阵。

3. technical-route-blueprint-planner
   生成技术路线图文本骨架。
```

---

## D. 写"特色与创新"

```
1. proposal-innovation-extractor
   初步提炼创新点。

2. surface-innovation-auditor
   驳回表面创新。

3. benchmark-comparison-defender
   与代表性文献做客观对比。

4. three-point-innovation-packager
   封装成三点式创新说明。

5. hype-language-cleaner
   删除夸张语言。
```

---

## E. 写"项目摘要"

```
1. nsfc-proposal-architecture-pipeline
   先完成全文架构。

2. nsfc-abstract-compressor
   压缩为 400 字以内摘要。

3. academic-abstract-pipeline
   进一步做摘要结构审计。

4. grammar-correction-auditor
   终稿校对。
```

---

## F. 写提示词时

以后在生成 Claude Code 提示词时，优先综合调用：
- using-superpowers
- brainstorming
- keyword-literature-download
- markitdown
- critical-literature-review-pipeline
- objective-innovation-auditor-pipeline
- nsfc-proposal-architecture-pipeline
- nsfc-reviewer-simulation-auditor
- terminology-coherence-editor

---

## G. 与已有文献综述流水线结合

```
第一步：使用 critical-literature-review-pipeline
        完成文献主题聚类、争议梳理、方法局限、研究空白界定。
        输出 → 立项依据的文献基础。

第二步：使用 nsfc-proposal-architecture-pipeline
        基于上一步的输出，完成科学问题提炼、目标对齐、
        方案可行性审计等后续任务。

第三步：使用 objective-innovation-auditor-pipeline
        审计创新点是否成立。

第四步：使用 nsfc-reviewer-simulation-auditor
        模拟评审。
```
