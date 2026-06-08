# 文献综述框架 — 提示词模板

## 模板 1：完整文献综述框架
```
请使用 literature-review-framework-pipeline。以下是我已核实的文献题录、摘要和全文摘录。请先锁定数据边界，然后提取变量和理论框架，映射理论演进，比较方法差异，执行主题聚类，隔离学术争议，识别文献共识，阐述研究空白，最后构建 H1-H3 大纲和最终框架。不得编造任何文献、理论、变量或方法。
```

## 模板 2：概念与变量提取
```
请使用 concept-variable-extractor。请从以下文献中提取自变量、因变量、中介变量、调节变量和理论框架，并绑定到具体引文。源文本未说明请标注。
```

## 模板 3：理论演进
```
请使用 theoretical-evolution-timeline-mapper。请根据以下文献按年份映射核心理论或概念的定义和测量方式变化。不得补写文献之外的理论史。
```

## 模板 4：方法差异比较
```
请使用 methodological-difference-comparator。提取以下文献中的样本量、数据来源、研究设计和评价指标，生成比较矩阵。只报告差异，不评价质量。
```

## 模板 5：主题聚类
```
请使用 literature-review-theme-clusterer。基于共同发现对以下文献进行主题聚类，每个主题需分配引文。
```

## 模板 6：争议隔离
```
请使用 academic-controversy-isolator。识别以下主题集群中相互冲突的结果或理论争论。不要解决争议。
```

## 模板 7：共识识别
```
请使用 literature-consensus-identifier。识别以下文献中多数共同支持的发现，标注共识强度。有反例时不要写强共识。
```

## 模板 8：研究空白
```
请使用 research-gap-knowledge-deficit-articulator。基于以下主题集群、争议和共识推导具体知识匮乏点。
```

## 模板 9：H1-H3 大纲
```
请使用 hierarchical-outline-structurer。将以下主题集群、争议和空白转化为 H1-H3 大纲。只输出大纲。
```

## 模板 10：逻辑过渡
```
请使用 logical-transition-mapper。为以下 H1-H3 大纲标注相邻章节的逻辑关系，给出过渡指令。
```

## 模板 11：最终框架组装
```
请使用 final-review-framework-assembler。将大纲、过渡映射和引文分配表组装为最终框架，检查引文是否全部分配。
```
