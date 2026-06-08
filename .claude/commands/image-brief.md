# /image-brief — 图像提示词与版式方案

## 适用场景
配图、信息图、PPT 图、流程图的提示词生成。

## 输入要求
- 图片用途
- 信息层级
- 风格参考

## 调用模块
`office-productivity-workbench` → `imagegen-helper`

## 工作流
1. 明确用途
2. 明确信息层级
3. 明确风格
4. 生成正向和负面提示词
5. 输出尺寸、背景、字体、构图建议
6. 科研图优先生成可编辑格式

## 输出文件
```
outputs/image_generation/
├── image_prompt.md
├── layout_plan.md
├── negative_prompt.md
└── figure_caption.md
```

## 禁止事项
- 不生成虚假实验图
- 不生成虚假截图
- 不生成伪造软件界面
- 不把示意图写为真实结果
- 无图像工具时只输出提示词

## 验收标准
- [ ] 提示词已包含正向和负面
- [ ] 示意图已标注"示意图"
- [ ] 科研图可编辑格式已优先
