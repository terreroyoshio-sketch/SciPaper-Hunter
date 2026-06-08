# /topic-research — 选题与汇报角度研究

## 适用场景
汇报角度、课程设计、分享主题、项目申报选题。

## 输入要求
- 任务场景（汇报 / 课程 / 科研 / 分享）
- 目标受众
- 已有材料

## 调用模块
`office-productivity-workbench` → `topic-research`
科研场景可选调用 `research-idea-conflict-miner`

## 工作流
1. 明确目标场景
2. 收集输入材料
3. 拆成 3-5 个可选角度
4. 评估新颖性、可行性、材料支撑、受众匹配
5. 输出推荐排序
6. 对高风险角度做反向质疑
7. 输出最小可执行方案

## 输出文件
```
outputs/topic_research/
├── topic_candidates.md
├── topic_score_table.csv
├── recommended_angle.md
└── risk_review.md
```

## 禁止事项
- 不凭空生成题目
- 不堆热点词
- 不写空泛创新点
- 选题必须有材料支撑

## 验收标准
- [ ] 角度有材料支撑
- [ ] 反向质疑已执行
- [ ] 推荐方案有明确理由
- [ ] 科研选题已调用对应 skill
