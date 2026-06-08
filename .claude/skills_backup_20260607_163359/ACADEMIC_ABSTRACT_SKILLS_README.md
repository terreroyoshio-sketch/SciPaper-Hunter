# 学术摘要处理 Skills 总说明

## 安装信息

- 安装日期：2026-05-09
- Claude Code skill 根目录：C:\Users\张涵\.claude\skills
- 备份目录：C:\Users\张涵\.claude\skills_backup_20260509_165755
- 本次目标：安装并整理 10 个摘要审计 skill，以及 1 个总工作流 skill

## 本次新增的 10 个摘要审计 skill

1. abstract-length-auditor  
   用于控制摘要字数，保留研究目标、核心方法和主要结论。

2. research-gap-auditor  
   用于识别研究空白，并生成克制、明确的过渡句。

3. qualitative-method-summary-auditor  
   用于提取研究对象、数据来源、抽样方式和分析方法，并压缩为摘要中的方法句。

4. empirical-result-extraction-auditor  
   用于从结果文本中提取主要发现，区分结果、解释和意义。

5. academic-vocabulary-auditor  
   用于替换口语化、泛化或主观化表达，使词汇更正式、更准确。

6. syntax-clarity-auditor  
   用于拆分复杂长句，降低阅读负担，同时保留关键限定条件。

7. voice-conversion-auditor  
   用于在合适情况下把被动语态改为主动语态，并保留必要的客观被动表达。

8. logical-transition-auditor  
   用于补充必要的过渡词，使背景、空白、方法、结果和结论之间更连贯。

9. grammar-correction-auditor  
   用于终稿前语法、标点、时态、拼写和排版检查。

10. disciplinary-tone-auditor  
    用于删除主观评价和夸张表达，使文本保持客观学术语调。

## 总工作流 skill

academic-abstract-pipeline 是总工作流 skill。它会按顺序调用或模拟 10 个摘要审计 skill，对摘要进行系统优化。

推荐调用方式：

```text
请使用 academic-abstract-pipeline 处理以下摘要。目标字数为【填写字数范围】，学科领域为【填写领域】，目标期刊要求为【填写要求】。不得引入原文之外的数据。请输出最终摘要、字数统计和逐步修改说明。
```

处理顺序：

1. abstract-length-auditor
2. research-gap-auditor
3. qualitative-method-summary-auditor
4. empirical-result-extraction-auditor
5. academic-vocabulary-auditor
6. syntax-clarity-auditor
7. voice-conversion-auditor
8. logical-transition-auditor
9. grammar-correction-auditor
10. disciplinary-tone-auditor

## 每个 skill 适合什么任务

- abstract-length-auditor：摘要超字数或字数不足时使用。
- research-gap-auditor：背景和研究目标之间缺少清晰过渡时使用。
- qualitative-method-summary-auditor：方法部分太长，需要压缩进摘要时使用。
- empirical-result-extraction-auditor：结果段信息较多，需要提取关键发现时使用。
- academic-vocabulary-auditor：摘要词汇偏口语化，或术语不统一时使用。
- syntax-clarity-auditor：长句过多，句子结构复杂时使用。
- voice-conversion-auditor：被动语态过多，且动作执行者明确时使用。
- logical-transition-auditor：句子之间跳跃较大，需要增加连贯性时使用。
- grammar-correction-auditor：提交前做客观语法和排版校对时使用。
- disciplinary-tone-auditor：摘要中存在主观评价或夸张表达时使用。

## 与之前安装的 skill 和工具配合使用

本机已检测到以下相关旧 skill 或工具：

- using-superpowers：C:\Users\张涵\.claude\skills\using-superpowers
- brainstorming：C:\Users\张涵\.claude\skills\brainstorming
- skill-creator：C:\Users\张涵\.claude\skills\skill-creator
- obsidian-bases：C:\Users\张涵\.claude\skills\obsidian-bases
- obsidian-cli：C:\Users\张涵\.claude\skills\obsidian-cli
- obsidian-markdown：C:\Users\张涵\.claude\skills\obsidian-markdown
- keyword-literature-download：C:\Users\张涵\.claude\skills\keyword-literature-download
- keyword-literature-download：C:\Users\张涵\.codex\skills\keyword-literature-download
- keyword-literature-download：C:\Users\张涵\.agents\skills\keyword-literature-download
- playwright：C:\Users\张涵\.codex\skills\playwright
- markitdown：C:\Users\张涵\.claude\skills\markitdown
- Markitdown：已检测到命令 C:\Users\张涵\AppData\Local\Programs\Python\Python314\Scripts\markitdown.exe

## 组合方式

### 写论文摘要时

1. Using-Superpowers：先确认目标、边界和验收标准
2. Brainstorming：生成摘要结构方案
3. academic-abstract-pipeline：系统优化摘要
4. grammar-correction-auditor：最终校对

### 做文献检索时

1. keyword-literature-download：检索与下载文献
2. empirical-result-extraction-auditor：从论文结果中提取关键发现
3. research-gap-auditor：总结研究空白
4. EndNote 或 RIS/BibTeX 工作流：构建论文库

### 做论文翻译和整理时

1. Markitdown：把 PDF 或 Word 转成 Markdown
2. academic-vocabulary-auditor：统一学术术语
3. syntax-clarity-auditor：降低机翻腔和长句负担
4. disciplinary-tone-auditor：去除主观夸张表达

### 做项目申报书或说明书时

1. Using-Superpowers：确认任务边界
2. Brainstorming：生成方案
3. research-gap-auditor：明确研究问题
4. empirical-result-extraction-auditor：提取已有实验结果
5. logical-transition-auditor：增强段落逻辑
6. grammar-correction-auditor：最终校对

## 使用说明

以后可以在提示词中直接写“请使用 skill 名称处理以下文本”。如果要完整处理摘要，优先使用 academic-abstract-pipeline。如果只需要某一步，就单独调用对应 skill。
