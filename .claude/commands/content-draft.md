# /content-draft — 内容写作初稿

## 适用场景
通知、邮件、汇报稿、发言稿、口播稿、朋友圈文案、公众号草稿。

## 输入要求
- 内容类型
- 受众
- 目的
- 语气
- 必须包含的信息

## 调用模块
`office-productivity-workbench` → `content-writer`

## 工作流
1. 明确受众
2. 明确目的
3. 明确语气
4. 明确必须包含的信息
5. 生成初稿
6. 标注需要用户补充的真实细节
7. 输出精简版和正式版

## 输出文件
```
outputs/content_writer/
├── draft.md
├── concise_version.md
├── formal_version.md
└── missing_real_details.md
```

## 禁止事项
- 不编造个人经历
- 不编造项目成果
- 不编造获奖、数据、身份
- 邮件不可擅自发送

## 验收标准
- [ ] 缺失的真实细节已标注
- [ ] 精简版和正式版已输出
- [ ] 无编造内容
