# /automation-plan — 自动化方案设计

## 适用场景
提醒、复盘、任务清单、周期性检查方案。

## 输入要求
- 任务描述
- 周期
- 触发条件

## 调用模块
`office-productivity-workbench` → `automation-assistant`

## 工作流
1. 明确任务
2. 明确周期
3. 明确触发条件
4. 生成提醒文本
5. 生成复盘模板
6. 如需系统自动化只生成脚本草案

## 输出文件
```
outputs/automation_assistant/
├── reminder_plan.md
├── review_template.md
├── automation_script_draft.md
└── safety_notes.md
```

## 禁止事项
- 不擅自启用定时任务
- 不擅自发送邮件
- 不擅自发布内容
- 不擅自删除文件
- 不保存敏感账号密码
- 不把提醒当作已完成

## 验收标准
- [ ] 提醒方案已生成
- [ ] 复盘模板已生成
- [ ] 安全提醒已输出
- [ ] 未启用任何自动化
