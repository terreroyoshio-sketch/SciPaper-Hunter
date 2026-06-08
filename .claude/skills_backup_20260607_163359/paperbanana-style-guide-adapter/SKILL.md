---
name: paperbanana-style-guide-adapter
description: PaperBanana 输出风格适配器。在 PaperBanana 生成图片后，对输出进行中英文学术风格适配检查，包括配色方案、字体、布局密度、标注规范等。
---

# PaperBanana Style Guide Adapter

## 概述

PaperBanana 默认采用 NeurIPS/CVPR 等顶会学术风格。本 adapter 根据目标场景（中文期刊、英文顶刊、项目申报书、PPT）对生成图件进行风格适配检查，输出需要修改的视觉元素清单。

## 风格适配矩阵

| 目标场景 | 主色调 | 字体 | 背景 | 布局 | 标注语言 |
|---------|--------|------|------|------|---------|
| Nature/Science 顶刊 | 低饱和度学术色 | Arial/Helvetica 6-7pt | 白色 | 紧凑 | 英文 |
| IEEE/CVPR 会议 | 蓝绿色系 | Times New Roman 8-9pt | 白色 | 中等 | 英文 |
| 中文核心期刊 | 低饱和度色 | 中文宋体+英文Times New Roman | 白色 | 略宽松 | 中文 |
| 国自然申报书 | 蓝/绿/灰色系 | 中文宋体/Arial | 白色 | 宽松可读 | 中文 |
| 学术 PPT | 高对比度色 | Arial/微软雅黑 ≥18pt | 浅色 | 宽松 | 中文/英文 |
| 学位论文 | 统一灰度色系 | Times New Roman + 宋体 | 白色 | 适中 | 中文/英文 |

## 检查清单

### 配色

```
[ ] 主色不超过 3 种
[ ] 色盲友好（避免红绿对比）
[ ] 颜色有明确的语义区分（不是纯装饰）
[ ] 背景白色/浅色（非深色背景，除非 PPT）
[ ] 字号颜色与背景有足够对比度
```

### 字体

```
[ ] 英文 → Times New Roman 或 Arial（按目标期刊要求）
[ ] 中文 → 宋体（中文期刊）或微软雅黑（PPT）
[ ] 字号 ≥ 6pt（印刷版）/ ≥ 14pt（PPT）
[ ] 标注文字清晰可读，无重叠
[ ] 图内无手写体/艺术字
```

### 布局

```
[ ] 多面板高度/宽度对齐
[ ] 面板间距一致
[ ] 箭头/连线不交叉
[ ] 文字框不超出边界
[ ] 整体左上→右下阅读顺序
[ ] 逻辑层级清晰（主→次）
```

### 标注

```
[ ] 所有面板有 (a)(b)(c) 标号
[ ] 箭头方向明确（单/双箭头有意义）
[ ] 缩写有图注说明
[ ] 数值/参数标注准确
[ ] 无多余装饰性元素
```

### 通用学术规范

```
[ ] 无 3D 效果（除非必要展示立体结构）
[ ] 无投影/透明度渐变（除非有物理意义）
[ ] 无线条粗细不统一
[ ] 无像素化/锯齿
[ ] 图题与图内内容一致
[ ] 符合目标期刊的Figure Guidelines
```

## 使用方式

### 方法一：生成前适配（推荐）

在调用 `paperbanana-figure-brief-builder` 时，直接在 method_text 中注入风格要求：

```
Style adaptation:
- Color palette: Nature-style muted blue (#3B7DD8), warm gray (#8B8B8B), 
  and accent coral (#E87B6C)
- Font: Arial, 7pt for axis labels, 8pt for panel labels
- White background, no grid lines
- Panel labels (a)(b)(c) in bold 9pt
- Arrows: 1.5pt line width, #555555
```

### 方法二：生成后适配

通过 `continue_run` 工具传递风格反馈：

```
"Please adjust the style:
1. Change the main color to Nature blue palette (#3B7DD8 primary)
2. Reduce the saturation by 20%
3. Replace current font with Arial
4. Make all panel labels bold
5. Add white background with no grid"
```

## 中英文学术插图差异

| 维度 | 英文期刊（Nature/Science） | 中文期刊 | 国自然申报书 |
|------|---------------------------|---------|------------|
| 信息密度 | 高（紧凑） | 中 | 高（信息量大） |
| 色彩饱和度 | 低（学术色） | 中 | 低（庄重） |
| 箭头风格 | 细线、直角 | 中等线宽 | 清晰导向 |
| 文字量 | 少（仅关键标注） | 中等 | 较多（含说明） |
| 布局 | 追求紧凑美观 | 追求清晰易读 | 追求逻辑完整 |
| 格式要求 | 严格的Figure Guidelines | 相对宽松 | 无严格限制 |

## 常见问题修复指南

| 问题 | 解决方案 |
|------|---------|
| 文字太小 | 通过 continue_run 要求增加字号 |
| 颜色太鲜艳 | 要求降低饱和度，换成低饱和度色系 |
| 箭头方向错误 | 提供具体的流向描述 |
| 面板不对齐 | 要求对齐面板，统一间距 |
| 缺少标注 | 要求添加 (a)(b)(c) 或具体数值 |
| 背景不是白色 | 要求改为白色背景 |
| 字体不对 | 指定具体字体名称 |
