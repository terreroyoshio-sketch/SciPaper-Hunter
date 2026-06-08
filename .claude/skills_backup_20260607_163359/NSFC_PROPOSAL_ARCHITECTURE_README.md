# NSFC 基金架构流水线 Skills — 总说明

## 一、背景

本组 skills 的核心目标：让 Claude Code 在撰写国家自然科学基金、科研项目申请书、项目摘要、立项依据、研究内容、技术路线、创新点和函评答辩材料时，完成**科学问题提炼、目标内容对齐、立项依据论证、可行性审计、前期基础组织、创新点提炼、技术路线规划、摘要压缩、术语一致性校对和专家质询模拟**。

**核心禁止**：
- 不要自由发挥式代写基金申请书。
- 不要虚构研究基础、实验结果、论文成果、基金经历或技术路线。
- 不要将普通技术瓶颈伪装成关键科学问题。
- 不要把"首次开展""样本更多""方法套用"直接写成核心创新。

---

## 二、新增 Skills 清单

| 序号 | 文件夹名称 | 用途 | 输入 | 输出 |
|------|-----------|------|------|------|
| 1 | `key-scientific-question-extractor` | 关键科学问题提炼 | 研究设想+前期数据 | 科学问题+技术瓶颈区分 |
| 2 | `objective-content-alignment-planner` | 目标内容对齐 | 科学问题+研究内容 | 层级矩阵+游离内容 |
| 3 | `proposal-rationale-gap-locator` | 立项依据逻辑定位 | 文献清单+科学问题 | 逐段大纲+转折句 |
| 4 | `feasibility-methodology-auditor` | 方案可行性审计 | 研究方案+实验方法 | 审查报告+缺失清单 |
| 5 | `proposal-innovation-extractor` | 特色与创新点提炼 | 申请书草稿 | 2-3个实质创新点 |
| 6 | `preliminary-work-coherence-planner` | 前期基础连贯规划 | 前期数据+研究内容 | 映射表+叙事框架 |
| 7 | `technical-route-blueprint-planner` | 技术路线蓝图 | 研究内容+方案 | 文本骨架+泳道图 |
| 8 | `nsfc-abstract-compressor` | 400字摘要压缩 | 申请书全文 | 合规摘要+字数统计 |
| 9 | `terminology-coherence-editor` | 术语一致性校对 | 章节草稿 | 术语统一+AI套话删除 |
| 10 | `nsfc-reviewer-simulation-auditor` | 函评专家模拟 | 申请书草稿 | 3条尖锐质询 |
| 11 | `nsfc-proposal-architecture-pipeline` | 完整架构流水线 | 全部输入 | 完整审计报告 |

---

## 三、流水线调用流程

调用 `nsfc-proposal-architecture-pipeline` 时，自动依次执行：

```
第一步：夯实核心基础
  step 1: key-scientific-question-extractor
  step 2: objective-content-alignment-planner

第二步：构建论证逻辑
  step 3: proposal-rationale-gap-locator
  step 4: feasibility-methodology-auditor
  step 5: preliminary-work-coherence-planner

第三步：凝练创新点与技术路线
  step 6: proposal-innovation-extractor
  step 7: technical-route-blueprint-planner

第四步：核心内容高度浓缩
  step 8: nsfc-abstract-compressor

第五步：压力测试与文本润色
  step 9: terminology-coherence-editor
  step 10: nsfc-reviewer-simulation-auditor
```

---

## 四、为什么国自然申请书不是自由发挥式写作

| 错误做法 | 正确做法 |
|---------|---------|
| AI 自行生成"该领域研究热点……" | 基于用户提供的真实文献清单 |
| AI 虚构研究基础 | 基于用户提供的前期数据 |
| AI 包装"首次提出……" | `surface-innovation-auditor` 驳回表面创新 |
| AI 写"机制尚不明确" | `key-scientific-question-extractor` 提炼科学问题 |

国自然评审重点关注：科学问题是否明确、论证是否严谨、方案是否可行、基础是否扎实。这些都不能由 AI 虚构。

---

## 五、为什么关键科学问题不能等同于技术瓶颈

- **技术瓶颈**：现有方法精度不够、效率不高、成本高。
- **科学问题**：造成精度不够的根本机制是什么？效率瓶颈的理论根源在哪里？

`key-scientific-question-extractor` 会通过理论悖论、认知冲突或关键缺失环节的判断，将表层技术问题上升为关键科学问题。

---

## 六、为什么立项依据不能写成文献流水账

流水账 = 文献 A 发现了 X，文献 B 发现了 Y，文献 C 发现了 Z。

正确做法（`proposal-rationale-gap-locator`）：
1. 宏观需求（为什么重要）
2. 已有进展（目前已知什么）
3. 具体空白（什么还不知道）
4. 本项目的方案（如何填补空白）

---

## 七、为什么创新点不能停留在"首次开展"

"首次开展""样本量更大""数据集更新"属于表面创新。
`proposal-innovation-extractor` 会拒绝这些主张，要求提炼理论概念创新、方法学创新或机制体系创新。

---

## 八、为什么前期基础必须映射到研究内容

评审关注：申请人是否具备完成该项目的能力。
`preliminary-work-coherence-planner` 将每张前期图表对应到具体研究内容，建立"基础→研究内容"的强关联。

---

## 九、如何保护敏感数据

如果使用公共 AI 模型：
- 对特定靶点、分子名称进行匿名化（蛋白 A、变量 X）
- 对患者信息、企业信息进行脱敏
- 不要上传未公开发表的完整论文或完整数据集
- 用"工艺参数 Y""材料 Z"等替代

---

## 十、与已有 Skills 的组合方式

详见 `NSFC_PROPOSAL_WORKFLOWS.md`。

---

## 十一、安全性说明

1. 所有 skills 均为本地 SKILL.md 文件，不执行代码。
2. 不连接外部网络或 API。
3. 不修改系统级配置。
4. 原始 skills 已在安装前备份。
