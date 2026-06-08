# 学术摘要处理 Skills 调用提示词模板

## 模板 1：完整摘要优化

```text
请使用 academic-abstract-pipeline 处理以下摘要。目标字数为【填写字数范围】，学科领域为【填写领域】，目标期刊要求为【填写要求】。不得引入原文之外的数据。请输出最终摘要、字数统计和逐步修改说明。
```

## 模板 2：只控制字数

```text
请使用 abstract-length-auditor 将以下摘要调整到【填写字数范围】。必须保留研究目标、核心方法和主要结论，不得新增数据。
```

## 模板 3：只提取研究空白

```text
请使用 research-gap-auditor 分析以下背景和目标段落，输出一句明确、克制、可放入摘要或引言中的研究空白表述。
```

## 模板 4：只提取结果

```text
请使用 empirical-result-extraction-auditor 从以下结果段中提取最重要的 3 条发现。不得生成任何外部数据。
```

## 模板 5：摘要终稿校对

```text
请依次使用 grammar-correction-auditor 和 disciplinary-tone-auditor 校对以下摘要。只修正客观错误和主观夸张表达，不改变研究含义。
```

## 模板 6：与文献检索 skill 联合使用

```text
请先使用 keyword-literature-download 检索【研究方向】相关论文，再用 research-gap-auditor 总结研究空白，用 empirical-result-extraction-auditor 提取代表性论文的主要结果，最后生成可写入项目申报书的研究现状段落。
```
