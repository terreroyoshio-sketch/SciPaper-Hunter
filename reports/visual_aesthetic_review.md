# 视觉审美审查报告（Visual Aesthetic Review）

2026-09-28 · critic 角色 · 仅观察/判断/建议，未改数据/模型/统计
维度取值：`PASS / PASS_WITH_LIMITATION / FAIL`；**证据口径**：`全尺寸目检`（本会话查看过原图）或 `缩略目检`（仅 contact sheet 级）+ 确定性指标（`reports/visual_metrics_20260928.json`）
说明：本表**不给出"美学分数"**；所有结论指向具体位置。

## 逐图审查（14 基准）

| 图 | Typography | Hierarchy | Alignment | Spacing | Collision | Color | Balance | Scientific clarity | AI-style risk | 证据 / 位置说明 |
|---|---|---|---|---|---|---|---|---|---|---|
| b01 | PASS | PASS | PASS | PASS | PASS（0/0/0） | PASS | PASS（irrig 数据均匀） | PASS：双序列+统计关系清晰 | LOW：两面板数据图，无卡片堆 | 全尺寸目检（会话内两轮） |
| b02 | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS：分布三视图互为支撑 | LOW | 全尺寸目检 |
| b03 | PASS | PASS | PASS | PASS | PASS | PASS：RdBu 发散+白字阈值 | PASS | PASS：相关矩阵注释可读 | LOW | 全尺寸目检；单元格注解=有意标注（contained） |
| b04 | PASS | PASS：层带+徽章层级清楚 | PASS | PASS | PASS | PWL：灰度冗余依赖描边/明度差 | PASS | PASS：数据→方法→结果叙事完整 | LOW-MED：容器审美接近参考图2范式，**非**卡片堆 | 全尺寸目检 |
| b05 | PASS | PASS | PASS | PASS | PASS | PWL：同 b04 灰度冗余 | PASS | PASS | LOW-MED：同上；阶段带即论文范式 | 全尺寸目检 |
| b06 | PASS | PASS | PASS：dot 布局均匀 | PASS | PASS（回流虚线语义） | PASS | PASS | PASS：DAG 分支/收敛可读 | LOW：**非**默认 dot 皮肤（自绘） | 全尺寸目检 |
| b07 | PASS | PASS | PASS | PASS：箭头—文字净空 ≥0.5mm | PASS（本轮修复 3 处真实擦边） | PASS | PASS | PASS：过程方向语义正确 | LOW：几何对象叙事，无图标堆 | **全尺寸目检（终版专门复核）** |
| b08 | PASS | PASS | PASS：渲染实测居中带（地图）+ 外部图例 | PASS | PASS | PASS：分级单色系 | PWL：等比例坐标导致上下留白带（几何诚实） | PASS | LOW | 全尺寸目检（含修复前对照） |
| b09 | PASS | PASS | PASS | PASS：KK 紧凑布局 | PASS（halo 合法保护） | PASS：三社区色觉友好 | PASS（修复前 imbalance 已消除） | PASS | LOW | 缩略目检 + 几何指标 |
| b10 | PASS | PASS | PASS | PASS | PASS：回路闭合、标签环外 | PASS | PASS | PASS：RC 拓扑正确 | LOW | 全尺寸目检 |
| b11 | PASS | PASS：hero 行（b 热图） | PASS | PASS | PASS | PASS | PASS（0.499） | PASS | LOW-MED：面板多但每格一信息 | 全尺寸目检 |
| b12 | PASS | PASS | PASS | PASS | PWL：2 处 3D 文字包围盒不可测→目检 | PASS | PASS | PWL：mplot3d 为兜底路径（主路径=b14） | LOW | 全尺寸目检（z 标签处置已复核） |
| b13 | PASS | PASS：场景→流程→结果单一路径 | PASS | PASS | PASS | PASS：低饱和场景色 | **PWL**：quadrant imbalance 0.86（左下重）→ 增强右上两组小图/或缩减左下地面带，二选一 | PASS：5 秒可述"观测→建模→预测+结果" | MED：GA 体裁本身信息集中；未见图标堆 | 缩略目检+指标；**建议终稿前全尺寸复核 BL 象限** |
| b14 | PASS | PASS | PASS | PASS | PASS | PASS：viridis+色条 8pt | **PWL**：imbalance 0.86（渲染主体偏左下）→ 与色条/标签的视觉重量再平衡 | PASS：3D 主路径证据 | LOW | 全尺寸目检（PyVista 渲染）+指标 |

## 横向审查（contact sheet 级）

- **字体一致性**：14 图同源 tokens（YaHei-first + Arial 数学），缩略级未见跳字；无 PPT 感粗体泛滥。
- **颜色一致性**：同一语义色族跨图一致（输入绿/过程蓝/方法紫/结果橙/强调黄）；无"跳出全文"的图。
- **密度**：最高 b14 0.306 / b13 0.264（含大色块渲染，属内容而非拥挤）；最低 b10 0.024（电路天然留白）——两端均有意图，非失衡。
- **留白**：全图 margin ≥1.6mm；b08/b12 的留白带为几何/投影诚实结果（已声明）。
- **箭头/形状**：无"同尺寸同距全套框"；b06 回流虚线、b10 回路、b13 流程箭头均具语义。
- **最弱图**：b13（若强制挑一）：BL 象限重量偏高；其余维度均过。

## 表格与排版件

| 件 | 结论 | 说明 |
|---|---|---|
| TABLE01–05 | PASS | 渲染实测 center_error ≤0.02mm；多页表头重复 ✓；短表不撑满全页（62.5mm 居中） |
| T01–T04（before/after） | PASS（回归口径） | before 全部按设计 FAIL（三类冲突均被检出）；after 全部 PASS |
| trd demo（8pt 版） | PASS | qa_layout 真实度量 PASS；目检版式干净 |

## 两层结论（分离声明）

1. **机械 QA 层**：14/14（13 PASS + 1 PWM）、T 套件期望全达、表 5/5、pytest 7/7 —— 未检测到已定义机械缺陷。
2. **审美层（本报告）**：**PASS_WITH_LIMITATION** —— 全部维度无 FAIL；5 处 PWL 均为具名、可操作项（b04/b05 灰度冗余、b08 留白带、b12 3D 文本、b13/b14 平衡），不存在"looks nice"式空判。

## 必改（≥1 项才升级为全 PASS）
- 无阻塞项。b13 的 BL 象限平衡为**建议性修改**（非阻塞）。
- 触发条件（任一）：目标期刊要求灰度无信息损失 → 处理 b04/b05；GA 进入正式投稿 → 处理 b13。
