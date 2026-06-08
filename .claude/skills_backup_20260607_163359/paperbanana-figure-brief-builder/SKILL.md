---
name: paperbanana-figure-brief-builder
description: 图件需求结构化转换器。将用户的学术插图需求转化为 PaperBanana 可处理的结构化 brief（method_text + caption），适用于图形摘要、机制图、方法流程图、技术路线图等。
---

# PaperBanana Figure Brief Builder

## 概述

将用户的非结构化图件需求转化为 PaperBanana MCP 的 `generate_diagram` 所需的 `method_text` 和 `caption` 参数。本 skill 不直接调用 PaperBanana，而是输出结构化的 brief，供 `paperbanana-mcp-wrapper` 使用。

## 工作流程

```
用户需求（自然语言）
    ↓
需求结构化分析
    ↓
图件类型分类
    ↓
撰写 method_text（详细的方法描述）
    ↓
撰写 caption（图题）
    ↓
输出结构化 brief
    ↓
→ 传递给 paperbanana-mcp-wrapper 执行生成
```

## 图件类型与 brief 模板

### 1. 方法论示意图 (Methodology Diagram)

**适用场景：** 模型架构、系统框架、算法流程

**brief 结构：**

```
## Figure Type: Methodology Diagram
## Method Text:
We propose [model/system name] consisting of [N] main components:
1. [Component 1]: [detailed description, inputs, process, outputs]
2. [Component 2]: [detailed description, inputs, process, outputs]
3. [Component 3]: [detailed description, inputs, process, outputs]

The data flow is: [input] → [step 1] → [step 2] → ... → [output].

Key architectural details:
- [Detail 1]
- [Detail 2]
- [Detail 3]

## Caption:
"Figure X: Overview of the proposed [model name]. 
(a) [component 1], (b) [component 2], (c) [component 3].
The pipeline processes [input] through [steps] to produce [output]."
```

### 2. 图形摘要 (Graphical Abstract)

**适用场景：** 论文图形摘要、TOC Graphic

**brief 结构：**

```
## Figure Type: Graphical Abstract
## Method Text:
This graphical abstract illustrates the core contribution of our study:

Research background: [1-2 sentences on the problem]
Key finding/method: [1-2 sentences on the approach]
Main result: [1-2 sentences on the outcome]
Significance: [1 sentence on the impact]

Visual elements to include:
- [Element 1]
- [Element 2]
- [Element 3]

## Caption:
"Graphical Abstract: [concise summary of the paper in one sentence]."
```

### 3. 方法流程图 (Method Flowchart)

**适用场景：** 实验步骤、数据处理流程、算法执行流程

**brief 结构：**

```
## Figure Type: Method Flowchart
## Method Text:
The experimental/data processing pipeline consists of [N] sequential stages:

Stage 1 - [name]: [description of inputs and process]
Stage 2 - [name]: [description of process]
Stage 3 - [name]: [description of process]
...
Stage N - [name]: [description of outputs]

Branches/decisions:
- At stage [X], if [condition] then go to [stage Y], else go to [stage Z]

Key parameters:
- [Parameter 1]: [value]
- [Parameter 2]: [value]

## Caption:
"Figure X: Workflow of [pipeline name]. See Methods section for detailed experimental conditions."
```

### 4. 技术路线图 (Technical Roadmap)

**适用场景：** 项目申报书、研究计划、国自然技术路线

**brief 结构：**

```
## Figure Type: Technical Roadmap
## Method Text:
The overall research roadmap is organized into [N] interconnected modules:

Module 1 - [theme]: 
  - Objective: [objective]
  - Approach: [approach]
  - Expected outcome: [outcome]

Module 2 - [theme]: 
  - Objective: [objective]
  - Approach: [approach]
  - Expected outcome: [outcome]

Module 3 - [theme]: 
  - Objective: [objective]
  - Approach: [approach]
  - Expected outcome: [outcome]

Interconnections: [Module 1 output → Module 2 input; Module 2 output → Module 3 input]

## Caption:
"Figure X: Technical roadmap of the proposed research program.
The research is organized into [N] modules spanning [scope]."
```

### 5. 机制图 (Mechanism Diagram)

**适用场景：** 分子机制、信号通路、生物学过程

**brief 结构：**

```
## Figure Type: Mechanism Diagram
## Method Text:
The molecular/cellular mechanism involves the following key players and interactions:

Key molecules/components:
- [Molecule 1]: [role, localization, state]
- [Molecule 2]: [role, localization, state]
- [Molecule 3]: [role, localization, state]

Interactions:
1. [Stimulus/Signal] → activates [Molecule 1] via [mechanism]
2. [Molecule 1] → phosphorylates/activates [Molecule 2]
3. [Molecule 2] → translocates to [location] and regulates [process]
4. [Molecule 3] → [downstream effect]

Cellular context: [cell type, tissue, condition]

## Caption:
"Figure X: Schematic diagram of the [pathway name] signaling pathway.
[Brief description of what is shown]."
```

### 6. 结果总结图 (Results Summary)

**适用场景：** 多实验结果汇总、定量结果可视化

**brief 结构：**

```
## Figure Type: Results Summary
## Method Text:
This figure summarizes the key experimental results:

Experiment 1 - [name]: 
  - Condition A: [value/outcome]
  - Condition B: [value/outcome]
  - Key finding: [finding]

Experiment 2 - [name]: 
  - Condition A: [value/outcome]
  - Condition B: [value/outcome]
  - Key finding: [finding]

Experiment 3 - [name]: 
  - Condition A: [value/outcome]
  - Condition B: [value/outcome]
  - Key finding: [finding]

Overall conclusion: [one-sentence takeaway]

## Caption:
"Figure X: Summary of experimental results. 
(a) [experiment 1], (b) [experiment 2], (c) [experiment 3].
Data suggest that [main conclusion]."
```

## 使用示例

### 用户需求 → 结构化 brief

**用户说：** "我需要一张图形摘要，展示我们提出的基于深度学习的遥感图像变化检测方法。模型先用 Siamese U-Net 提取双时相特征，然后通过差异增强模块突出变化区域，最后用边界感知损失函数优化分割边界。"

**输出的 method_text：**

```
This graphical abstract illustrates a deep learning-based remote sensing 
image change detection method.

The proposed method consists of three main components:
1. Siamese U-Net backbone: The model takes a pair of bitemporal remote 
   sensing images as input. A Siamese U-Net architecture with shared weights 
   extracts multi-scale features from both images.
2. Difference enhancement module: The extracted bitemporal features are compared 
   through a difference enhancement module that computes feature dissimilarities 
   and highlights changed regions while suppressing unchanged areas.
3. Boundary-aware refinement: The final change map is optimized using a 
   boundary-aware loss function that emphasizes the geometric boundaries of 
   changed regions for sharper segmentation.

The data flow is: Bitemporal images → Siamese U-Net feature extraction → 
Difference enhancement → Boundary-aware refinement → Final change map.

Key advantages:
- Shared-weight Siamese architecture for consistent feature extraction
- Attention-guided difference enhancement for robust change detection
- Boundary-aware loss for precise segmentation boundaries
```

**输出的 caption：**

```
"Graphical Abstract: Overview of the proposed change detection method 
using Siamese U-Net with difference enhancement and boundary-aware optimization."
```

## 注意事项

1. **method_text 要详细** — PaperBanana 的 Planner 和 Visualizer 需要足够的文字细节才能生成准确的图示
2. **caption 要简洁** — 类似于论文图题，概括而不啰嗦
3. **明确视觉元素** — 如果对颜色、布局、箭头方向有要求，必须在 method_text 中说明
4. **区分主次** — 核心创新点放在前面描述，次要细节简洁带过
5. **避免模糊描述** — "处理"、"分析"等泛泛动词换成具体的操作名称
