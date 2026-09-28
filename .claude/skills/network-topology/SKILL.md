---
name: network-topology
description: 网络/拓扑/关系图绘制（节点-边结构、模型关系、依赖网络、共现网络）：networkx 布局 + 自绘呈现，语义编码显式化。用户要画网络图、拓扑图、关系图、节点链接图时使用。不用于有向流程/算法 DAG（scientific-flowchart）、不用于层级架构（drawio-diagram-workbench）。
---

# Network Topology — 网络 / 拓扑图

## 与相邻技能的分工
- 有**流程/时序语义**的有向图 → `scientific-flowchart`
- **办公/架构**分层框图 → `drawio-diagram-workbench`
- 本技能只管**关系网络**：谁与谁相连、强度、社区、中心性

## 布局选择（先定语义再选布局）
| 布局 | 适用 | networkx |
|---|---|---|
| spring / kamada_kawai | 一般关系网、社区结构 | `spring_layout(seed=42)` |
| multipartite | 分层二分/多层关系（如 作者-主题） | `multipartite_layout` |
| circular / shell | 环形结构、周期关系 | `circular_layout` |
| 层级 DAG | 上下位关系 | 转 `scientific-flowchart` 用 dot |

**随机布局必须固定 seed** 并在脚本注明（可复现）。

## 语义编码（每个编码必须有含义 + 图例）
- 节点大小 = 度/流量/规模；节点颜色 = 类别/社区（色觉友好，≤6 类）；边宽 = 权重；边虚线 = 推断/弱连接
- 中心性标注（如有）：说明算法（degree / betweenness）与用途
- 标签：只标关键节点（hub / 目标节点）；大图禁全标（用编号+图例表）

## 大图纪律（>50 节点）
- 社区着色 + 布局聚类；边 α≤0.5 避免毛球
- 可给"骨架图 + 全图缩略"双面板（multipanel-compositor 组装）

## 输入与证据
- 边列表/邻接矩阵的真实来源文件；**不得凭空连边**；网络统计量（度分布、模块度）有输出支持才能标注

## 输出与 QA
- SVG + PDF + PNG + 灰度 + 缩印预览；**必经 `figure-quality-gate`**
- 附加目检：节点标签碰撞（自动检查覆盖文字重叠，但密集图仍需目检）

## 失败条件
- 边/节点语义不明（谁连谁、权重含义）且用户无法说明
