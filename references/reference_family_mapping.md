# 参考图 → 家族 → 学习要点 映射（Reference → Family Mapping）

2026-09-28 · 与 `figure_style_catalog.md` 配套 · 覆盖本轮审查指出的全部参考图类型

## 证据分级（沿用用户证据等级规范，不越级）

- `SESSION-VISIBLE`：本会话内经原生视觉**直接分析**的参考图（结构记录见 `figure_style_catalog.md` §1）
- `SESSION-VISIBLE (partial)`：本会话可见图中**部分面板**覆盖该类型
- `USER-LISTED`：用户列举的参考图类型，**图像本体本会话不可见**——结构要点按该类型公认范式记录，**待图像核验**；升级只需提供图像本体（或图题+期刊），按 catalog 同口径补记录

## 映射表（19 类）

| # | 参考图类型 | 家族归属 | 应学结构要点（层次 / 空间叙事 / 嵌入元素 / 公式 / 阶段关系） | 已落实能力（家族 + benchmark） | 证据等级 |
|---|---|---|---|---|---|
| 1 | 干旱传播（SPEI/SSI/SRI→Copula→SHAP） | 技术路线图 | 4 阶段纵列；虚线容器+编号徽章；右侧嵌真实小图；公式框；块箭头推进 | technical-route-diagram；b05（四阶段带+公式框+内嵌图） | SESSION-VISIBLE |
| 2 | 洪水传播（事件筛选→特征→聚类→传播统计→1D 模型→归因） | 方法框架（hub 变体） | 中心模型+分区输入组织；Measured/Simulated 成对对比；底部汇总条 | scientific-method-framework；b04 三层结构 | SESSION-VISIBLE |
| 3 | 冰川/反照率数据融合 a/b/c | 多面板数据流 | 按数据角色着色+显式图例；逐操作节点细粒度流 | multipanel-compositor；b11（角色色族进 gate 灰阶检查） | SESSION-VISIBLE |
| 4 | 生态服务 / 人类福祉（SDG 图标映射） | 方法框架 + 概念映射 | 图标语义矩阵；1–5 编号映射；双向箭头；图标须有语义（禁止装饰性 icon） | scientific-method-framework | SESSION-VISIBLE (partial，图1 可见该 panel) |
| 5 | 宏观生态系统（区域带+通量箭头） | 机制示意图 | 介质分区；几何对象；通量方向语义 | mechanism-schematic；b07 | USER-LISTED |
| 6 | 大湖 ESSD / 积雪产品融合 | 多面板数据流 + GIS 复合 | 数据层级色族；多分辨率色标；显式图例 | multipanel-compositor + geospatial-figure | USER-LISTED |
| 7 | 植被干旱响应 | 技术路线图（长流程） | 多阶段带 + 响应链结构 | technical-route-diagram；b05 | USER-LISTED |
| 8 | GEE / MEGAN 平台工作流 | 算法流程 DAG | 云平台节点分层；数据→处理→产品 DAG | scientific-flowchart；b06 | USER-LISTED |
| 9 | Uncertainty quantification | 统计分析图 | 误差带/分布/敏感性表达规范 | 数据/统计图家族（figurelab 系）+ gate 显著性标注规则；b01 误差带、b02 分布 | USER-LISTED |
| 10 | CH₄ 机制（源-汇过程） | 机制示意图 + 通量场 | 源汇对象；方向箭头；预算/通量标注 | mechanism-schematic；b07 | USER-LISTED |
| 11 | Urban heat multiscale framework | 多尺度方法框架 | 尺度层级嵌套（多级分区）；跨尺度箭头 | scientific-method-framework（层次可嵌套）+ multipanel-compositor | USER-LISTED |
| 12 | LLM / bibliometric workflow | 算法流程 DAG | 数据→检索→分析 DAG；分支/回流虚线语义 | scientific-flowchart；b06（回流虚线已落地） | USER-LISTED |
| 13 | Wheelchair accessibility（空间可达性） | GIS + 网络 | 路网/缓冲区叠加；可达域渲染 | geospatial-figure + network-topology（组合） | USER-LISTED |
| 14 | Isotopic vapor process | 机制示意图 | 过程链；分馏箭头；储库标注 | mechanism-schematic | USER-LISTED |
| 15 | ET / precipitation contribution | 方法框架 + 贡献分解 | 贡献度分解条；分区对比 | scientific-method-framework；b05 贡献排序内嵌图 | USER-LISTED |
| 16 | Graphical Abstract | 图形摘要 | 一句核心信息；大场景叙事；结果小图融合；5 秒可读 | graphical-abstract；**b13（本轮新增）** | 家族补齐（无独立参考图本体） |
| 17 | 生态机制示意 | 机制示意图 | 同 #5 | mechanism-schematic；b07 | USER-LISTED |
| 18 | 多尺度研究路线 | 技术路线图 | 尺度分层 + 阶段带组合 | technical-route-diagram；b05 | USER-LISTED |
| 19 | GIS + 模型混合图 | 多面板复合 | 地图面板 + 模型流程 + 结果面板混排；统一图例 | multipanel-compositor（地图面板由 geospatial-figure 产出） | USER-LISTED |

## 覆盖性结论（诚实声明）

1. **家族覆盖（结构层）**：12 个 router 家族全部有对应条目；benchmark 覆盖：b01–b14（数据=b01、统计=b02+b03、方法框架=b04、路线=b05、DAG=b06、机制=b07、GIS=b08、网络=b09、工程=b10、多面板=b11、3D 兜底=b12、GA=b13、3D 主路径=b14）。
2. **视觉学习证据（图像层）**：19 类中 **4 类 SESSION-VISIBLE**（直接结构分析），**15 类 USER-LISTED**（类型级覆盖；结构要点按范式记录，**未经图像核验**）。审查指出的"参考图视觉学习证据不完整"在本表的处理方式是：**全类型有归属与要点，但证据等级如实分级，不冒充已见**。
3. 本表不复制任何参考图内容；升级核验仅需提供图像本体。
