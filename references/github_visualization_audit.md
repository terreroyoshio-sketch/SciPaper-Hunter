# GitHub 可视化仓库只读审计

> **PRE-INSTALL AUDIT SNAPSHOT** —— 本报告正文记录的是 **2026-09-28 上午（安装前）** 的状态；
> 当天下午 cartopy / pyvista / vtk 已获授权安装并冒烟测试，**安装后状态见文末 §D**。
> 正文表格保持快照原样不动，避免出现"同一文档两个当前状态"的矛盾。

- 日期：2026-09-28 · 方式：GitHub API（license / stars / pushed_at / archived）+ raw LICENSE 逐条核验
- **只读观察：未安装任何包、未运行任何第三方脚本、未复制任何代码**
- 分类：`CORE_REFERENCE` / `SPECIALIZED_REFERENCE` / `OPTIONAL` / `REJECT`

## A. 本批 14 仓库

| 仓库 | 性质 | 最近推送 | ★ | 许可（核验方式） | 本机状态 | 有用组件 | Windows 关注点 | 分类 |
|---|---|---|---|---|---|---|---|---|
| matplotlib/matplotlib | 官方 | 2026-09-26 | 23.3k | **Matplotlib License Agreement**（raw LICENSE 核验；BSD 风格自有许可，需保留声明+变更摘要） | 已装 3.10.8 | patches / GridSpec / inset_axes / annotations / transforms / artist | 无 | **CORE** |
| rougier/scientific-visualization-book | 官方 | 2026-01-04 | 11.6k | 正文 **CC BY-NC-SA 4.0（非商用）**，代码部分另有条款（/license API 核验） | 未使用 | 排版/构图/颜色/坐标 设计思想 | 无 | SPECIALIZED（**仅学习，不商用、不复制**） |
| garrettj403/SciencePlots | 官方 | 2026-06-23 | 9.3k | **MIT** ✓ | 未装 | 期刊 style 参数（尺寸/字体/线宽/配色） | 无 | SPECIALIZED（学参数，不做强依赖） |
| mwaskom/seaborn | 官方 | 2026-07-06 | 14.0k | **BSD-3-Clause** ✓ | 已装 0.13.2 | 分布/类别/回归/不确定性/facet | 无 | **CORE**（统计图） |
| has2k1/plotnine | 官方 | 2026-09-27 | 4.8k | **MIT** ✓ | 未装 | Grammar of Graphics 思想 | 无 | OPTIONAL |
| Phlya/adjustText | 官方 | 2026-06-08 | 1.7k | **MIT** ✓ | 未装 | 标签避让（辅助） | 已知与 FancyArrowPatch 配合问题（issue 有记录）；**复杂场景不依赖自动避让** | OPTIONAL |
| networkx/networkx | 官方 | 2026-09-28 | 17.3k | **BSD-3-Clause**（raw LICENSE 核验；API 误标 Other） | 已装 3.6.1 | 图结构 / 分层布局 | 无 | SPECIALIZED |
| xflr6/graphviz | 官方 | 2026-07-11 | 1.8k | **MIT** ✓ | 已装 0.21；**dot 二进制 14.1.3 在 D:\Graphviz\bin** | DOT 布局计算 | 依赖本机 dot（已就位，实测可调用） | **CORE**（仅算布局，不决定最终视觉） |
| mingrammer/diagrams | 官方 | 2026-09-22 | 42.6k | **MIT** ✓ | 未装 | cluster / hierarchy / edge routing 模式 | 云厂商图标风**禁止**进入 SCI 图 | SPECIALIZED（仅学模式） |
| SciTools/cartopy | 官方 | 2026-09-24 | 1.6k | **BSD-3-Clause** ✓ | **未装** | 地图投影 / CRS | 依赖 GEOS/PROJ（geopandas 链路已在，风险低） | SPECIALIZED（**待批安装**） |
| geopandas/geopandas | 官方 | 2026-09-24 | 5.3k | **BSD-3-Clause** ✓ | 已装 1.1.3（+shapely 2.1.2 / pyproj） | 矢量空间数据 / choropleth / 空间连接 | 无 | **CORE**（GIS） |
| cdelker/schemdraw | 官方 | 2026-07-18 | 268 | **MIT** ✓ | 已装 0.23 | 电路 / logic / timing / state machine | 无 | SPECIALIZED（已可用） |
| pyvista/pyvista | 官方 | 2026-09-27 | 3.8k | **MIT** ✓ | **未装** | 3D mesh / surface / volume / headless | 依赖 VTK（体积大，~百 MB 级）；GPU 非必需 | SPECIALIZED（**待批安装**） |
| matplotlib/pytest-mpl | 官方 | 2026-08-20 | 272 | Other（matplotlib 同族许可） | 未装 | baseline 图像回归（视觉漂移） | 与 matplotlib 3.10 兼容性需实测 | OPTIONAL |

## B. 前序已核验（AI 出图生态，2026-09-28 同日上轮）

| 仓库 | 许可 | 结论 |
|---|---|---|
| ResearAI/AutoFigure · AutoFigure-Edit | **MIT** ✓ | 可吸收；参考图风格迁移→可编辑 SVG；需 Docker+API key（安装列待批） |
| google-research/papervizagent（原 PaperBanana） | Apache-2.0 ✓ | 可参考；输出栅格 PNG |
| 0xE1337/thesis-figure-skill | **MIT** ✓ | 可参考（TikZ+drawio 双轨、编译级重叠检测思路） |
| jihe520/sci-box | **无许可** | **仅自用/仅模式**，代码不并入本仓 |
| QIANJINYDX/research-drawio-skill | **无许可** | **仅自用/仅模式**，代码不并入本仓 |
| OpenDCAI/Paper2Any | Apache-2.0（legacy 快照） | 参考；重栈 |

## C. 结论

1. 14 仓库全部**活跃、未归档**；许可无 REJECT 级问题；三个"许可证元数据异常"（matplotlib=null、rougier=NOASSERTION、networkx=Other）均已用 raw/API 逐条澄清。
2. **覆盖缺口需要安装的只有两项**：`cartopy`（真实地图投影）、`pyvista`（3D）。其余 OPTIONAL：SciencePlots / plotnine / adjustText / pytest-mpl（不装不阻塞，或仅学思想）。
3. **明确不引入**：mingrammer 图标风（只学 cluster/hierarchy 模式）；无许可仓库（只提取模式，不复制代码）。
4. Windows 关注点：Graphviz dot 已实测（D:\Graphviz\bin\dot v14.1.3）；其余为纯 Python 或成熟轮子，无平台阻断。
5. 安装原则（按用户规范）：任何安装需单独批准（包名/版本/原因/收益/风险/Windows 兼容性/传递依赖/回滚方式），优先用已装库。
