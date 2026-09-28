# docx 补丁日志（2026-09-28）

- 源文件：`C:\Users\张涵\Desktop\制图提示词.docx`
- 输出副本：`C:\Users\张涵\Desktop\制图提示词.patched_20260928.docx`
- 变更条数：17

## INSERT 文档头修订说明
- 旧：（无）
- 新：【2026-09-28 修订副本】本副本修正了“方框+箭头 / 几何叙事”绝对规则（§十七 / §十八 / §五十二 / §五十四），并将技能列表同步为实际已装技能；生成方式为脚本补丁，原件未改动。变更明细见 docx_patch_log_20260928.md。

## REPLACE [段 30]
- 旧：* research-task-router
- 新：* scientific-figure-router

## REPLACE [段 31]
- 旧：* diagram-workflow
- 新：* figure-quality-gate

## REPLACE [段 32]
- 旧：* diagram-quality-engineering
- 新：* figurelab-publish

## REPLACE [段 33]
- 旧：* diagram-visual-output-guard
- 新：* academic-figure-skill

## REPLACE [段 34]
- 旧：* cognitive-illustration
- 新：* scientific-visualization

## REPLACE [段 35]
- 旧：* scientific-workbench-agent
- 新：* nature-figure-style

## REPLACE [段 36]
- 旧：* final-delivery-audit
- 新：* technical-route-diagram

## REPLACE [段 37]
- 旧：* paper-workflow
- 新：* figure-preflight-checker

## REPLACE [段 608]
- 旧：## 绝对禁止传统：
- 新：## 禁止对象（2026-09-28 修正）：无语义模板化流程图

## REPLACE [段 624]
- 旧：* 大量方框 + 箭头
- 新：* 无语义、模板化的方框堆叠（大量同尺寸方框 + 箭头直连）

## INSERT-AFTER [段 625] 锚点：* AI 信息图风格…
- 旧：（无）
- 新：（2026-09-28 修正） ‖ **禁止**无语义、模板化的方框堆叠和默认流程图风格（默认 Mermaid 风、PPT SmartArt、彩色圆角卡片堆、全节点同尺寸同箭头、纯文字节点占据全部视觉主体、装饰性图标）。 ‖ **允许**矩形、圆角矩形、分区面板、箭头、连接线、虚线区域、公式、地图、数据小图、几何示意——但每个容器必须承担明确的信息组织功能。 ‖ 技术路线图与方法框架图优先采用“数据层—方法层—分析层—结果层”或与论文实际方法一致的层级；重要步骤应结合真实小图、公式、地图、几何对象或结果缩略图，而不是全部用文字节点表达。

## REPLACE [段 631]
- 旧：# 十八、流程图必须采用“几何叙事”
- 新：# 十八、流程图规则（2026-09-28 修正）：分场景处理

## INSERT-AFTER [段 631] 锚点：# 十八、流程图规则（2026-09-28 修正）：…
- 旧：（无）
- 新：几何叙事（用点 / 射线 / 区域 / 轨迹等与数学模型对应的几何对象表达算法阶段，视觉信息 ≥60% 来自几何关系）仍是**数学建模类算法流程图**的优先路径（本节后续几何对象清单与示例继续适用）。 ‖ 但**方法框架图、技术路线图、一般工程与数据流程**允许使用语义容器 + 箭头，前提是语义明确、不得是模板化堆叠。

## REPLACE [段 711]
- 旧：视觉上不得画成传统流程图。
- 新：视觉上不得画成“无语义模板化”的默认流程图；本类（数学建模算法）图应优先几何叙事。

## REPLACE [段 1737]
- 旧：19. 流程图不是方框+箭头；
- 新：19. 流程图不得是“无语义模板化方框堆叠”（默认 Mermaid/SmartArt 风、等尺寸节点直连）；允许承担信息组织功能的语义容器 + 箭头；

## REPLACE [段 1832]
- 旧：禁止方框堆叠。
- 新：禁止无语义、模板化的方框堆叠（允许承担信息组织功能的语义容器 + 箭头）。
