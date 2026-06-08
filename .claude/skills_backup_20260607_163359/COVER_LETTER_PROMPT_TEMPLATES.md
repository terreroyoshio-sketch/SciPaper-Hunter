# Cover Letter — 提示词模板

---

## 模板 1：完整 Cover Letter 生成

```
请使用 cover-letter-pipeline。以下是我的稿件标题页、摘要、引言、结论、
目标期刊名称、期刊宗旨和范围、原创性声明、伦理与资金信息。
请严格基于我提供的数据生成 Cover Letter，不得虚构任何作者、编辑、
期刊范围、研究发现、基金号、伦理批准号或审稿人信息。
主信正文控制在 400 英文词以内。
```

---

## 模板 2：稿件元数据提取

```
请使用 manuscript-metadata-extractor。
请从以下稿件扉页中提取标题、通讯作者、机构和邮箱。
不得更改标题或作者姓名。缺失信息请标注"未提供"。
```

---

## 模板 3：期刊称呼核查

```
请使用 journal-editor-verification-auditor。
请根据以下目标期刊名称和编辑信息生成正式称呼。
如果未提供主编姓名，请默认使用 Editor-in-Chief，不要猜测。
```

---

## 模板 4：研究意义压缩

```
请使用 research-significance-compressor。
请从以下引言中提取研究空白和研究必要性，
并压缩为 1 到 2 句适合 Cover Letter 的客观表述。
不得使用"开创性""革命性"等夸张词。
```

---

## 模板 5：贡献提取

```
请使用 empirical-contribution-extractor。
请从以下摘要和结论中提取主要实证发现、理论贡献或方法学进展，
并生成适合 Cover Letter 的贡献段落。不得外推结果。
```

---

## 模板 6：期刊范围对齐

```
请使用 journal-scope-alignment-writer。
请将以下稿件贡献与目标期刊 scope 文本进行交叉对齐，
写出为什么适合该期刊读者。只能使用我提供的 scope，
不得凭空猜测期刊偏好。
```

---

## 模板 7：原创性声明

```
请使用 originality-status-statement-generator。
根据以下用户确认信息，生成原创、未发表、未同时投稿声明。
如果确认信息不完整，请列出待确认项。
```

---

## 模板 8：伦理合规声明

```
请使用 ethics-compliance-statement-formatter。
请根据以下利益冲突、资金、伦理批准和知情同意信息生成合规声明。
不得编造基金号或伦理批准号。
```

---

## 模板 9：审稿人列表格式化

```
请使用 reviewer-data-formatter。
请将以下推荐审稿人和回避审稿人信息整理成干净表格。
不得编造邮箱、机构或理由。
```

---

## 模板 10：语调标准化

```
请使用 academic-tone-standardizer。
请检查以下 Cover Letter 草稿，删除口语化、奉承、夸张和 AI 痕迹表达，
保持正式、客观、专业。
```

---

## 模板 11：长度和结构审计

```
请使用 cover-letter-assembly-length-auditor。
请将以下模块组装成最终 Cover Letter，检查强制声明是否完整，
并将正文控制在 400 英文词以内。
```
