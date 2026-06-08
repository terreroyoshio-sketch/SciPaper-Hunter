# /ppt-build — PPT 大纲与讲稿

## 适用场景
PPT 大纲、页面结构、讲稿、答辩逻辑。

## 输入要求
- 演示主题
- 听众
- 时长
- 核心信息

## 调用模块
`office-productivity-workbench` → `presentation-builder`
科研 PPT 可选调用 `ai-powerpoint-research-workflow`

## 工作流
1. 确定听众
2. 确定核心信息
3. 生成故事线
4. 拆成页面大纲
5. 每页只保留一个核心点
6. 给出图表/配图建议
7. 生成讲稿
8. 检查页面是否空、乱、丑

## 输出文件
```
outputs/presentation_builder/
├── slide_outline.md
├── slide_content_table.csv
├── speaker_notes.md
├── visual_suggestions.md
└── revision_checklist.md
```

## 禁止事项
- 不先做装饰
- 不塞太多字
- 答辩 PPT 不优先炫
- 课程设计 PPT 要图文对应

## 验收标准
- [ ] 每页一个核心点
- [ ] 故事线完整
- [ ] 讲稿已生成
- [ ] 视觉建议已输出
