# 科研视觉审美规则库（Scientific Visual Aesthetics）

2026-09-28 · 与 `scientific-typography` / `collision-aware-layout` / `visual-aesthetic-critic` 配套
来源分级：**[文件级学习]** = 实际读取的文档/源码；**[知识级]** = 既有知识 + 官方 gallery 经验（未逐文件核验）；**[参考图]** = 用户图集直接分析（4 张 SESSION-VISIBLE）
**2026-09-28 补读**：rougier 书 code/ 10 文件 + SciencePlots 3 样式文件已本地逐文件阅读（深克隆，路径见 `aesthetic_reference_matrix.md`）——E/H/I/J/K 项的 halo、直标、双编码、字号惯例参数均已有文件级证据（正文中以 [文件级:rougier]、[文件级:SciencePlots] 标注）。
每项结构：定义 / 典型失败 / 正确处理 / 自动检查可能性 / 必须人工判断的部分

## A. Hierarchy（层级）[知识级+参考图]
- 定义：读者 3 秒内按"标题→分区→主体→注释"顺序接收信息。
- 典型失败：全图同字重同字号；所有框同权重；标题条比内容还大。
- 正确处理：字号层级 tokens（panel 9 / axis 8.5 / tick≈legend 8 / 注释 8，见 typography）；bold 仅一级信息；hero 元素面积占比最大。
- 自动检查可能性：字号层级可查（figure_qa 下限 + tokens 对照）；bold 使用可查（统计 bold 文本数）。
- 人工判断：谁是 hero、层级是否服务科学信息。

## B. Alignment（对齐）[知识级+参考图]
- 定义：同族元素共享基线/列线；面板边缘对齐。
- 典型失败：盒子高度差 1–2mm 的"手抖感"；面板间距不均。
- 正确处理：网格先行（列基线/步距常数）；跨面板共享轴。
- 自动检查：同族等宽等距可由元素登记表核验（trd_kit 元素记录）。
- 人工：视觉对齐感（缩略级足够）。

## C. Proximity（邻近）[知识级]
- 定义：语义相关元素靠近，无关元素拉开；组间距 > 组内距。
- 典型失败：标签离目标太远且无 leader；两个不同组的元素贴在一起。
- 正确处理：leader line + 组间距 ≥ 组内距的 1.5 倍。
- 自动检查：engine 的 leader 长度与 off_norm 罚分即邻近约束的实现。
- 人工：语义分组是否合理。

## D. Repetition（重复/一致性）[参考图]
- 定义：同语义同样式（色、形状、线型）全文一致。
- 典型失败：同语义跨图换色；圆角半径忽大忽小；箭头样式两种以上无理由。
- 正确处理：token 化配色与形状；跨图 contact sheet 比对。
- 自动检查：跨文件配色哈希对比（参考图4 的"数据层级色族+图例"范式）。
- 人工：contact sheet 横向判断"哪张跳出全文"。

## E. Contrast（对比）[知识级+文件级:rougier]
- 定义：重要信息对比度更高；前景/背景分明。
- 典型失败：浅灰注释压浅色填充；深底上深字。
- 正确处理：文字与承载填充的灰阶差 ≥ 0.15（或加 halo）。**四级可读阶梯 [文件级:rougier typography-legibility.py]**：①纯黑/纯白 ②bold ③bbox 底色（白/黑，`alpha=0.75`，pad≈1）④halo（`Stroke(linewidth=1.5, foreground=白/黑)`）——底越乱越往下走；halo 与底色的配对必须同向（深字配白 halo、浅字配黑 halo）。
- 自动检查：灰阶差可纳入 gate（tokens 内填充已做实）。
- 人工：整体对比节奏。

## F. Negative Space（负空间）[知识级+参考图]
- 定义：留白是结构，不是浪费；边距 ≥1.5mm、组间距充分。
- 典型失败：贴边、挤成一团、无意义的大面积空白（单侧失衡）。
- 正确处理：显式设计边距与呼吸区；空白应分布而非集中。
- 自动检查：margin 检查（figure_qa）+ 象限不均衡指标（visual_metrics）。
- 人工：留白是否"有意图"。

## G. Visual Balance（视觉平衡）[参考图]
- 定义：视觉重量沿画布分布，无偏移塌陷。
- 典型失败：全部重量压左上；孤立点拉伸布局。
- 正确处理：象限墨量均衡（imbalance 指标 <~0.5 为参考线）；布局紧凑（balance 检查）。
- 自动检查：象限墨量 + 全幅/核心比（已实现）。
- 人工：平衡与叙事的关系（平衡不等于对称）。

## H. Figure Density（密度）[知识级]
- 定义：信息密度与服务目标匹配；单图单一主信息 + 必要支撑。
- 典型失败：文字密度过高（>15% 墨量为警戒线）；面板塞满无呼吸。
- 正确处理：删冗余注释、拆 panel、移入 caption。
- 自动检查：density/ink 指标（visual_metrics）。
- 人工：是否一个面板一个信息。

## I. Typography（字体）[文件级: python-docx docs / rougier / SciencePlots]
- 定义：字体来源可解释、层级明确、混排协调（见 scientific-typography）。
- 典型失败：混搭字体；静默 fallback；上下标用 Unicode 字符（YaHei 缺 ₂ ⁻——本轮 smoke test 实测）。
- 正确处理：tokens + font_smoke_test；数学走 mathtext。**venue 字号惯例实例 [文件级:SciencePlots nature.mplstyle]**：Nature 全图 7pt、panel label 8pt bold、全 sans、单栏 ≤3.5in——本体系 SCI 8pt 为通用下限，投 Nature 系时经 `--min-pt` 覆盖为 7pt（threshold_source 记录依据）；mathtext fontset 可配 custom 与正文同族（[文件级:rougier typography-math-stacks.py] 含 custom 对照）。
- 自动检查：font_problems 已进 gate（fail-closed）。
- 人工：字体与venue的一致性。

## J. Color Semantics（颜色语义）[参考图+文件级:SciencePlots]
- 定义：颜色承载角色语义（输入/方法/结果/数据层级），全文唯一。
- 典型失败：同色跨图变换语义；"漂亮但无语义"的渐变；rainbow。
- 正确处理：低饱和功能色族 + 显式图例 + 灰阶冗余。**灰度冗余的文件级范式 [文件级:SciencePlots ieee.mplstyle]**：颜色环（k/r/b/g）与线型环（-/--/:/-.）**并联双编码**——黑白打印时线型仍可区分；单色渐变场景用同色系深浅 + 明值差（science.mplstyle hex 色环为低饱和蓝绿黄红紫灰）。
- 自动检查：色族灰阶阈值（gate）+ tokens 对照。
- 人工：语义是否被读者猜到。

## K. Annotation Placement（注释布置）[知识级 + 文件级:adjustText/rougier]
- 定义：注释近目标、不压数据、必要时 leader、避让不得破坏近邻关系。
- 典型失败：标签压在曲线/箭头上；为了不重叠把所有标签赶出图外；几十条交叉 leader。
- 正确处理：候选位置 cost（engine 已实现：碰撞/边界/距离/自锚净空）+ halo（网络等密集场景合法保护）。**引线范式 [文件级:rougier annotation-side.py]**：leader `arrowstyle="->", lw=0.75, shrinkA=20, shrinkB=5`（文字端留 20pt 净空、锚点端 5pt）；**引线自身加白 halo（Stroke lw=2）** 使其可越过杂乱背景；**锚点按 Y 值降序排序再逐条外引**——顺序一致引线即不交叉（先排序，再布局，勿靠事后避让）。
- 自动检查：full engine（text-* 全类别）。
- 人工：近邻语义与可读性权衡。
- 补：**直标优先梯 [文件级:rougier legend-alternatives.py]**：线端同色文本（"— label"）> 沿线内嵌小字（旋转角≈局部斜率 42.5°，白底 `bbox alpha=0.85`）> annotate 引线（`connectionstyle="arc3,rad=-0.3"`）> 图例盒——能用直标就不用图例框。

## L. Table Composition（表格构图）[文件级: python-docx docs / great-tables README]
- 定义：表级居中 ≠ 单元格居中；表宽由内容定；三线纪律；列对齐按语义（文本左/数值中）。
- 典型失败：短表撑满全页；全列机械居中；属性正确但渲染偏移。
- 正确处理：fixed layout + 显式列宽 + w:jc center + **渲染后实测 center_error ≤1.0mm**（已实现）。
- 自动检查：XML 链 + 渲染链（table_qa）。
- 人工：表题措辞与表内单位。

## M. Multi-panel Rhythm（多面板节奏）[参考图]
- 定义：面板大小按信息权重分配（hero 面板大）；标签 a/b/c 一致；共享图例去重。
- 典型失败：等大网格无主次；图例重复；共享轴被断开。
- 正确处理：GridSpec 非对称、共享轴、统一图例（multipanel-compositor 规则）。
- 自动检查：面板尺寸/标签一致性可查（元素登记）。
- 人工：叙事节奏。

## N. Image/Chart Integration（图与数据融合）[参考图]
- 定义：内嵌小图/地图/照片是"论证的一部分"，非贴纸；来源可追。
- 典型失败：小图与正文无关；标签压 ROI/scale bar；截屏当数据图。
- 正确处理：小图真实数据+来源、贴边留白、轻 halo/低信息区放字（engine 输出 text-image 供人工判 ROI）。
- 自动检查：text-image 边界越界（LIMITATION）；小图来源在流程规范中强制。
- 人工：关键 ROI 是否被压（必须目检）。
