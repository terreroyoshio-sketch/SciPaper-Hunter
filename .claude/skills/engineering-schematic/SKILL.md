---
name: engineering-schematic
description: 电子信息类工程示意图绘制（电路、逻辑门、时序图、状态机、DSP/控制框图）：schemdraw 为主渲染器。用户要画电路原理图、数字逻辑图、时序波形图、状态机、信号链框图时使用。不用于办公流程图（drawio）、不用于物理机制（mechanism-schematic）。
---

# Engineering Schematic — 电路 / 逻辑 / 时序 / 状态机

## 渲染器（本机已装 schemdraw 0.23，MIT）
- 电路：`schemdraw.Drawing` 标准元件（`d.Resistor / d.Capacitor / d.SourceSin / d.Ground / d.Dot / d.Line / d.Label`）
- 逻辑：`schemdraw.logic`（Gate / ~A 取反等）
- 时序：`schemdraw.logic.timing` 或自绘阶梯波形（matplotlib step，风格统一）
- 状态机：`schemdraw.flow` 或自绘圆角状态 + 转移弧
- **API 以使用时实测为准**（0.23 版本）；渲染结果取 matplotlib Figure 后走统一导出与 gate

## 制图规范（工程图惯例）
1. 标准符号，不自造；元件值带单位（10 kΩ、0.1 µF）
2. 网络/节点命名规范（Vin、Vout、CLK、RST）；端口方向明确（输入左/上，输出右/下）
3. 时序图：时间轴必须有刻度与单位；关键时序参数（建立/保持/传播延迟）如需标注必须有来源或标注为示意
4. 状态机：状态名 + 转移条件；初态标记
5. 框图：信号链单方向 + 回流（反馈）用虚线

## 反造假边界（强）
- **不得冒充软件截图**（Multisim/Proteus/示波器界面）——示意图必须能看出是示意图（`diagram-integrity` 规则）
- 电路参数若来自课设/实测，标注来源；仿真波形截图必须是真实软件输出，不得绘制造假
- 课程设计图：工程绘图风格，符合课设模板（图题、图号）

## 输出与 QA
- SVG + PDF + PNG（课程/PPT 载体时也出 300dpi PNG）；**必经 `figure-quality-gate`**
- 载体为课程/办公时字号阈值 ≥10pt（见 gate 场景表）

## 失败条件
- 电路拓扑与原理不明；参数来源不明且用户要求标注数值
- 用户要求"画得像仿真软件截图" → 拒绝（反造假）
