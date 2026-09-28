# 审美参考矩阵（Aesthetic Reference Matrix）

2026-09-28 · 只学**视觉规律**（排版/布局/间距/颜色/注释），不复制内容、不做像素级模仿、不把他人数据带入 benchmark。
`do_not_copy` 列显式声明每类参考中**禁止照搬**的部分。

| reference | figure_family | typography | layout | spacing | color | annotation | strength | weakness | learned_rule | do_not_copy |
|---|---|---|---|---|---|---|---|---|---|---|
| 用户参考图2（干旱 4 步横带） | 技术路线图 | 无衬线 6.5–8pt（按印幅）；标题加粗 | 4 虚线分区带 + 每带左容器链右小图 | 带内留白 ≥1 盒高；步骤间距均等 | 深红编号 + 绿/蓝/紫/粉功能色族 | 公式独立框；块箭头承担阶段推进 | 结构一眼可读；内嵌真实小图把流程升级为论证 | 灰度冗余不足（仅色族区分） | 语义容器+箭头是正当范式；内嵌小图必须真实数据 | 论文图内容、字体文件、图标素材 |
| 用户参考图3（洪水 hub） | 方法框架（hub 变体） | 分组标题灰底加粗；表内小号 | 中心模型+分区输入；底部汇总条 | 分区间的呼吸区分明 | cream 底+白卡 | Measured/Simulated 成对标注范式 | 多输入输出显式组织；验证语义强 | 信息密度高，依赖图注 | 对比语义用成对编码；底部结论条 | 具体研究数据与结论 |
| 用户参考图4（反照率 a/b/c） | 多面板数据流 | a/b/c 标签加粗左上 | 数据角色分色 + 右侧显式图例框 | 细粒度操作节点 | 数据层级色族（黄/粉/蓝） | 图例声明色块语义 | 多分辨率/多层级数据的图例范式 | 粒度细导致图注依赖高 | 按"数据角色"着色 + 显式图例 | 论文边界与数据 |
| rougier/scientific-visualization-book | 全家族（教材） | typography 章设计与字重纪律 | GridSpec/构图/负空间 | ornaments 与间距 | 色彩语义章节 | 沿路径文字、文字 halo 等技巧 | 设计思想系统完整 | 逐文件读取许可混杂（部分 BSD / 部分 CC BY-NC-SA / 部分 CeCILL）——只提炼规律，不复制代码 | **已文件级**（2026-09-28 深克隆 `~/.claude/reference/svbook-ref/code/` 读 10 文件）：legibility 四级阶梯（plain/bold/bbox α=0.75/halo 1.5pt）；text-outline 分层 halo（zorder=-lw）；annotation-side 引线 lw0.75+shrinkA20/B5+**引线自身白 halo 2pt** + **锚点按 Y 排序防引线交叉**；complex-layout 象限说明外置 margin+clip_on=False 短引线；legend-alternatives 直标优先梯（线端同色 / 沿线旋转 42.5°+bbox α0.85 / annotate arc / 字母键） | 书正文与图（CC BY-NC-SA 非商用）；不逐像素模仿 |
| garrettj403/SciencePlots | 数据图 | 期刊字号/线宽参数族 | figure size/scale 约定 | tick/legend 参数 | 期刊风格色环 | — | 参数化期刊风格 | **已文件级**（2026-09-28 深克隆 `~/.claude/reference/scienceplots-ref/src/scienceplots/styles/` 读 3 样式）：nature.mplstyle 注释载明 **Nature 惯例=全 sans + 全图 7pt + panel label 8pt bold**、单栏 ≤3.5in；science.mplstyle 刻度朝内+四边 tick+次刻度 3/1.5+图例无框+savefig tight pad 0.05；ieee.mplstyle **颜色 k/r/b/g × 线型 -/--/:-/. 双编码（灰度冗余的文件级证据）** | 学参数结构，不做默认依赖 | 不无脑 style.use；不因它引入 LaTeX |
| Phlya/adjustText | 散点标签（局部） | — | 迭代避让 | — | — | 文本相斥/引线 | 简单散点的辅助避让 | README 自述"heuristic 非保证"；不覆盖复杂结构 | 定位为**辅助层**；复杂图用约束式布局 | 不把自动避让当最终决策器 |
| matplotlib/matplotlib（docs/gallery） | 全家族 | Text/font_manager 体系 | GridSpec/constrained_layout | offsetbox/anchored 布局 | — | PathEffect/halo | 渲染后实测 bbox 是测量唯一正道 | — | renderer-based measurement（已落入 figure_qa/engine） | — |
| posit-dev/great-tables（README） | 表格 | — | header/stub/body 组件层级；spanner 多级表头 | — | — | — | 表格信息层级的组件化思想 | README 未覆盖 rule weight/间距细节（文档站为准） | 表头层级与 stub 分离的原则（落入 publication-table-layout） | 不安装、不作为 Word 渲染器 |
| python-openxml/python-docx（文档） | 表格 | — | Table.alignment=整表定位；autofit 影响列宽 | — | — | — | 澄清"表级居中 ≠ 单元格居中" | — | w:jc + fixed layout + 渲染实测（已实现） | — |
| 禁止学习源 | — | — | — | — | — | — | — | — | 明确排除：Dribbble / Canva 信息图 / 营销数据图 / dashboard / 商业 BI / Pinterest 风 | 全部 |

## 学习来源分级（诚实声明）
- **文件级学习（实际读取）**：python-docx 表格 API 文档、adjustText README、great-tables README、matplotlib（仓库内既有实现与知识）；**2026-09-28 补读**：rougier 书 `code/` 10 文件（`typography/typography-legibility.py`、`typography/text-outline.py`、`ornaments/annotation-side.py`、`layout/layout-gridspec.py`、`layout/complex-layout.py`、`ornaments/legend-alternatives.py`、`typography/typography-math-stacks.py`、`typography/typography-font-stacks.py`、`defaults/mystyle.txt`、`rules/helper.py`）+ SciencePlots 3 样式文件（`science.mplstyle`、`journals/nature.mplstyle`、`journals/ieee.mplstyle`）——均为**深克隆后本地逐文件阅读**（`~/.claude/reference/svbook-ref`、`~/.claude/reference/scienceplots-ref`，只读学习，未安装、未 import、未复制代码）。
- **历史失败与补救**：早期 api.github.com 403（限流）与 raw 404（路径猜测）导致两行曾标"原则级"；本次改用 `git clone --depth 1`（书仓加 `--filter=blob:none --sparse` 只取 code/rst/fonts）解决——教训：**逐文件读取第三方源码用深克隆，不用 API/raw 猜路径**。
- **许可核对（阅读前）**：SciencePlots=MIT；书仓逐文件混杂（BSD / CC BY-NC-SA 4.0 / CeCILL）——只提炼设计规律、不复制代码正文，`do_not_copy` 列继续适用；两仓均不入交付包。
- **参考图**：4 张 SESSION-VISIBLE（结构记录见 `figure_style_catalog.md`）；其余类型见 `reference_family_mapping.md` 证据分级。
