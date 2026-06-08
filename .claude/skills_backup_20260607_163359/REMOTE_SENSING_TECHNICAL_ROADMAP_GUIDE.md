# Remote Sensing Technical Roadmap Guide — 遥感/GIS 技术路线图绘制指南

> 基于 ISPRS JPRS / JAG 2025 年 10 篇论文的技术路线图结构规律总结。
> ⚠️ 未能访问原图，仅基于标题、摘要和 OpenAlex 元数据总结结构规律。

---

## 一、10 篇论文基本信息表

| # | DOI | 论文题名 | 期刊 | 年份 | 研究对象 | 遥感数据源 | 核心方法 | 最终输出 |
|---|-----|---------|------|------|---------|-----------|---------|---------|
| 1 | isprsjprs.2025.07.036 | Enhancing LiDAR place recognition using Retrieval-Trigger-Reranking paradigm | ISPRS JPRS | 2025 | LiDAR 地点识别 | LiDAR 点云 | Retrieval-Trigger-Reranking 范式 | 识别/定位结果 |
| 2 | isprsjprs.2025.10.012 | Effective feature matching for multimodal remote sensing images via sparse sampling description | ISPRS JPRS | 2025 | 多模态影像配准 | 多模态遥感影像 | 稀疏采样描述 + 特征匹配 | 配准结果图 |
| 3 | isprsjprs.2025.10.028 | A novel method for remote sensing phycocyanin leveraging optical classification and integrated ML | ISPRS JPRS | 2025 | 藻蓝蛋白遥感反演 | 多光谱/高光谱 | 光学分类 + 集成机器学习 | 藻蓝蛋白浓度图 |
| 4 | jag.2025.104513 | Leveraging moisture elimination and hybrid DL for soil organic carbon mapping with multi-modal RS data | JAG | 2025 | 土壤有机碳 | 多模态遥感 + 地面样本 | 水分消除 + 混合深度学习 (MCCL) | 土壤有机碳空间图 |
| 5 | jag.2025.104605 | SFD-YOLO: subsidence funnels detection in China based on large-scale SAR interferograms | JAG | 2025 | 沉降漏斗检测 | SAR / InSAR 干涉图 | SFD-YOLO | 沉降漏斗检测结果图 |
| 6 | jag.2025.105005 | Global high-resolution mapping of PV power plants 2019-2025 using unsupervised index-based multi-source fusion | JAG | 2025 | 光伏电站制图 | 多时相光学影像 | 无监督指数 + 多源融合 | 全球光伏分布图 |
| 7 | jag.2025.104997 | InSAR-based landslide susceptibility in karst erosion landforms using non-landslide sampling strategy | JAG | 2025 | 滑坡易发性 | InSAR + DEM + 地形因子 | 非滑坡样本策略 + 易发性模型 | 滑坡易发性分区图 |
| 8 | jag.2025.104887 | Bridging the cloud gap: AHI/ATMS synergy through CNN feature fusion for all-weather SST retrieval | JAG | 2025 | 海表温度反演 | AHI / ATMS 卫星数据 | CNN 特征融合 | 全天候 SST 图 |
| 9 | jag.2025.104904 | A layer-wise classification framework for coastal wetlands mapping using SAR time series | JAG | 2025 | 滨海湿地分类 | Sentinel-1 SAR 时间序列 (443景) | 分层分类 + 局部最优时空特征 | 10m 湿地分类图 (2017-2024) |
| 10 | jag.2025.104926 | A novel mechanism-guided retrieval framework for mangrove chlorophyll content based on active learning hybrid model | JAG | 2025 | 红树林叶绿素 | SDGSAT-1 / Sentinel-2 / 高光谱 | PROSAIL + 主动学习混合模型 | 叶绿素含量空间图 |

## 二、遥感 SCI 技术路线图共性结构

基于这 10 篇 ISPRS/JAG 论文的分析，遥感技术路线图普遍遵循 **六层结构**：

### 六层流水线结构

```
数据源层 → 预处理层 → 特征构建层 → 模型/算法核心层 → 验证与解释层 → 产品输出层
```

### 各层规律

#### 1. 数据源层（通常位于顶部或左侧）

**包含要素**：
- SAR/InSAR 数据（Sentinel-1, ALOS, 干涉图）
- 光学遥感（Sentinel-2, Landsat, SDGSAT-1, AHI/ATMS）
- LiDAR 点云
- DEM / 地形数据
- 气象/环境数据
- 地面样本/实测数据
- 行政边界矢量

**图中摆放规律**：
- 最常用布局：**顶部水平数据源带** — 各类数据作为独立图标/色块，平铺在顶部
- 次常用布局：**左侧垂直数据列表** — 分类型排列（如光学类、SAR 类、辅助数据类）
- 多模态研究常将数据源分为 2-3 组（如光学一组、SAR 一组、地面数据一组）

#### 2. 预处理层（数据源层正下方或右侧）

**图中表达方式**：
- 通常画成一行小模块或虚线框整体
- 每个处理步骤用简写：辐射定标、大气校正、几何校正、云掩膜、重采样、投影统一
- SAR 论文额外包含：去斑滤波、InSAR 干涉处理、形变提取
- 预处理模块常用 **浅色背景虚线框** 包裹，表示"通用处理阶段"
- 箭头从数据源指向预处理模块

#### 3. 特征构建层（预处理与模型之间的关键桥梁）

**图中表达方式**：
- 用独立模块表示"从原始数据到可输入特征的转换"
- 常见特征类别：
  - 光谱指数（NDVI, NDWI, EVI, 其他自定义指数）
  - 时序特征（年度变化、季节振幅、趋势）
  - 纹理特征（GLCM、Haralick）
  - 地形因子（坡度、坡向、曲率、高程）
  - 物理机制变量（叶面积指数、冠层参数）
  - 特征选择/降维（PCA、RF重要性）
- **关键规律**：特征层常被画为"汇聚节点"——多源数据→特征层→单一特征集→模型

#### 4. 模型/算法核心层（整张图的最突出区域）

**图中表达方式**：
- 位于图的**几何中心**
- 用**更深/更鲜艳的颜色**区别于其他层
- 包含子模块嵌套结构：
  - 深度学习模型：Encoder-Decoder 结构、注意力模块、特征金字塔
  - 混合模型：物理模型 + 机器学习
  - 检测模型：Backbone + Neck + Head
- 模型层输入箭头指向清晰，输出箭头明确
- 如果是创新模型，在该模块周围添加**虚线高亮框**或**星标**表示"本文方法"

#### 5. 验证与解释层（模型的右侧或正下方）

**图中表达方式**：
- 用独立虚线框表示
- 包含：训练/验证/测试集划分、精度评价指标（OA, Kappa, F1, RMSE, R²）
- 与模型层之间有**双向箭头**（训练反馈、调参）
- 常包含对比方法（baseline 模型）的比较结果
- **常见的错误**：把验证画成小角落 → 正确做法是验证模块与模型模块**视觉面积比例至少 1:3**

#### 6. 产品输出层（图的最右侧或底部）

**图中表达方式**：
- 分类图 / 反演图 / 检测结果图的小缩略图
- 用缩小的地图框（带图例）表示
- 两种输出类型：
  - **科学产品**：分类图、反演值图、密度图
  - **应用产品**：风险分区、管理建议、政策支持
- 部分论文在输出层下方加"应用场景"框

## 三、5 种推荐版式

### 1. 左到右流水线式

```
[数据源] → [预处理] → [特征提取] → [模型核心] → [输出产品]
                              ↑                    ↓
                         [地面样本] → [训练/验证]
```

**适合**: 普通遥感反演、分类、检测、制图论文
**结构**: 水平方向六阶段递进

### 2. 上下分层式

```
         ┌─────────── 数据源层 ──────────┐
         │  SAR  │ 光学  │  DEM  │ 地面  │
         └────────────────────────────────┘
                      ↓
         ┌─────── 预处理与特征层 ────────┐
         │  定标  校正  去云  指数计算   │
         └────────────────────────────────┘
                      ↓
         ┌──────── 模型核心层 ──────────┐
         │        深度学习模型          │
         └────────────────────────────────┘
                      ↓
         ┌── 验证层 ──┐ ┌── 输出层 ──┐
         │  精度评估  │ │  制图产品  │
         └────────────┘ └────────────┘
```

**适合**: 多源数据融合、多尺度建模、机制变量参与的研究

### 3. 中心模型辐射式

```
   [数据源A] ──┐              ┌── [输出产品1]
                ├── [模型核心] ──┼── [输出产品2]
   [数据源B] ──┘              └── [输出产品3]
                      ↑
                 [验证评估]
```

**适合**: 突出新模型、新框架、新算法的论文

### 4. 双分支对比式

```
   ┌── [传统流程] ──→ [结果A] ──┐
   │                              ├── [对比评估]
   │  [同一数据源]                │
   └── [本文方法] ──→ [结果B] ──┘
```

**适合**: 新方法与基线方法的对比论文

### 5. 闭环迭代式

```
   [初始数据] → [初始模型] → [预测结果]
                    ↑              │
                    │     [误差/不确定性分析]
                    │              │
                    └── [样本优化/重训练] ←┘
                                    ↓
                              [最终模型] → [最终产品]
```

**适合**: 主动学习、半监督学习、样本优化、检索-重排序类论文

## 四、中文提示词母版

```
请绘制一张适合 SCI 论文发表的遥感/GIS 技术路线图，主题为【研究主题】。
图中应清晰展示从【数据源】到【预处理】、【特征构建】、【模型或算法核心】、
【验证评估】和【最终制图产品】的完整流程。
请采用【版式类型】布局，将多源数据输入放在【左侧/顶部】，将核心方法放在
图中央，将验证评估和输出结果放在右侧或底部。
请使用不同颜色区分"数据层、处理层、模型层、验证层、输出层"，
用箭头表示数据流、特征流和结果流。
整体风格应简洁、专业、适合 ISPRS/JAG 类遥感论文，避免海报化背景、
复杂装饰和大段文字。
```

## 五、英文提示词母版

```
Create a publication-ready remote sensing / GIS technical workflow diagram
for 【research topic】. The figure should clearly show the complete pipeline
from 【data sources】 to 【preprocessing】, 【feature construction】,
【model or algorithm core】, 【validation and assessment】, and
【final mapping products】.
Use a 【layout type】 layout, placing multi-source data inputs on the
【left/top】, the core method in the center, and validation and output
products on the right or at the bottom.
Use distinct colors to separate the data layer, processing layer, model layer,
validation layer, and output layer. Use arrows to indicate data flow, feature
flow, and result flow. The overall style should be clean, professional, and
suitable for ISPRS/JAG-style remote sensing papers, avoiding poster-like
backgrounds, excessive decoration, and long text blocks.
```

## 六、7 类研究场景专用模板

### 1. SAR / InSAR 监测技术路线图

```
请采用从左到右流水线式布局。
左侧列出 SAR 数据源【Sentinel-1 / ALOS / 其他】。
预处理模块包含【辐射定标 → 干涉处理 → 去斑滤波 → 形变提取】。
特征构建层提取【后向散射特征 / 干涉相干性 / 时序形变特征 / 统计特征】。
模型核心为【SFD-YOLO / CNN / 混合模型】进行【检测/分类/反演】。
验证层包含【地面样本验证 / 混淆矩阵 / 交叉验证】。
右侧输出【形变图 / 检测结果 / 风险分区图】。
```

### 2. 光学遥感反演技术路线图

```
请采用上下分层式布局。
顶部数据源层包含【Sentinel-2 / Landsat / 高光谱传感器】。
预处理层包含【云掩膜 → 大气校正 → 重采样 → 研究区裁剪】。
特征构建层计算【光谱指数 → 物理机制变量 → 纹理特征】。
中部模型核心采用【机器学习 / 混合物理-数据驱动模型 / 主动学习混合模型】。
验证层包含【地面实测样本 / 交叉验证 / 不确定性分析】。
底部输出【反演参数空间分布图】。
```

### 3. 多源数据融合技术路线图

```
请采用上下分层式布局。
顶部数据源层分为三组：【SAR 数据】、【光学数据】和【辅助数据（DEM/气象/样本）】。
预处理后，各数据源经【尺度统一 → 特征提取】进入特征融合层。
融合层采用【特征拼接 / 注意力融合 / 多模态融合策略】。
中部模型核心基于融合特征执行【分类 / 反演 / 检测】。
验证层评估各数据源贡献（消融实验），底部输出融合后的制图产品。
请用不同颜色区分"光学来源特征"、"SAR 来源特征"和"融合特征"。
```

### 4. 遥感目标检测技术路线图

```
请采用从左到右流水线式布局。
左侧数据源为【高分辨率光学/SAR影像】。
预处理包含【影像切片 → 样本标注 → 数据增强】。
模型核心采用【YOLO / CNN检测框架】，突出【多尺度特征增强 / 小目标检测模块】。
后处理步骤包含【NMS / 误检剔除 / 空间过滤】。
验证模块使用【Precision-Recall曲线 / mAP / F1】。
右侧输出【检测结果图 / 密度图 / 目标框标注图】。
```

### 5. 滑坡/灾害易发性技术路线图

```
请采用中心模型辐射式布局。
左侧输入数据：【InSAR形变】、【地形地貌因子（坡度/高程/曲率）】、
【诱发因子（降水/人类活动）】。
预处理包含【因子栅格化 → 重采样统一 → 空间匹配】。
特征层进行【因子筛选 → 相关性分析 → 多重共线性检验】。
模型核心为【易发性评价模型】，强调【正负样本策略 / 非滑坡采样方法】。
验证层含【ROC曲线 / AUC / 易发性分区统计】。
右侧输出【易发性分区图（低/中/高/极高）】。
```

### 6. 湿地/生态分类技术路线图

```
请采用分层分类式布局。
顶部数据源：【Sentinel-1 SAR时间序列（443景）】。
预处理包含【时序合成 → 云掩膜 → 去斑滤波】。
特征构建提取【时序特征 → 极化特征 → 空间纹理 → 局部最优时空特征】。
模型核心采用【分层分类框架】，第一层区分植被/非植被，第二层细分湿地类型。
验证模块评估逐类精度和混淆矩阵，与分析区时间序列对比。
底部输出【年度湿地分类图 / 各湿地类型面积统计】。
```

### 7. 光伏/能源设施制图技术路线图

```
请采用左到右流水线式布局。
左侧数据源：【多时相光学影像（Landsat/Sentinel-2）】。
预处理：【云掩膜 → 年度合成 → 指数计算】。
特征层：【光谱指数 / 光伏特征规则/ 候选区域提取】。
模型核心：【无监督指数法 / 多源融合方法】。
验证模块：【随机抽样验证 / 时序一致性检查 / 误检剔除】。
右侧输出【全球/区域光伏分布图 / 年度变化图】。
```

## 七、技术路线图质量检查清单

| # | 检查项 | 说明 |
|---|-------|------|
| 1 | 是否有明确数据源 | 图中必须标注具体传感器或数据产品名称 |
| 2 | 是否标注关键预处理 | 大气校正、云掩膜、几何校正等不能省略 |
| 3 | 是否区分特征构建和模型训练 | 特征不是模型的一部分 |
| 4 | 是否突出本文创新模块 | 核心方法用更深色或虚线高亮框标注 |
| 5 | 是否包含验证数据和评价指标 | 验证不是可有可无的附属 |
| 6 | 是否说明最终输出产品 | 缩略图加注图例或说明文字 |
| 7 | 箭头方向是否表示真实数据流 | 不能有反向箭头 |
| 8 | 是否避免所有模块同等重要 | 创新模块视觉权重应高于常规模块 |
| 9 | 是否避免纯文字堆积 | 每模块用 2-5 词，不用段落 |
| 10 | 是否避免无关图标和装饰 | 卫星图标用标准符号，不用卡通图 |
| 11 | 是否保留可编辑性 | 用矢量格式保存源文件 |
| 12 | 是否适合黑白打印 | 配色要考虑灰度可区分度 |
| 13 | 是否与正文方法章节一一对应 | 图不能遗漏正文中的关键步骤 |
| 14 | 是否没有夸大方法能力 | 图上不写未验证的性能声明 |

## 八、与我已有 Skills 的组合方式

| 场景 | 使用的 Skills |
|------|-------------|
| 论文技术路线图 | remote-sensing-technical-roadmap-designer + geomaster + geopandas + scientific-visualization + nature-figure |
| 项目申报书技术路线图 | nsfc-proposal-architecture-pipeline + technical-route-blueprint-planner + remote-sensing-technical-roadmap-designer + ppt-master |
| 遥感数据处理流程图 | geomaster + geopandas + scientific-visualization + docs |
| 论文图形摘要 | scientific-image-prompting-guide + remote-sensing-technical-roadmap-designer + nature-figure |
| PPT 展示图 | brainstorming + ppt-master + remote-sensing-technical-roadmap-designer |
| 真实数据图（统计/分类结果） | matplotlib + seaborn + scientific-visualization（不用图像生成模型） |
| 空间数据制图 | geopandas + geomaster + scientific-visualization |
