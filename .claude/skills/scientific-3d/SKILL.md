---
name: scientific-3d
description: 3D 科研图绘制（点云、曲面、网格、体数据、3D 设备结构）：首选 pyvista（未装，待批），兜底 matplotlib mplot3d 并声明限制。用户要画 3D 表面图、三维点云、体渲染、装置结构时使用。不用于 2D 图（其余家族技能）。
---

# Scientific 3D — 三维科研图

## 渲染器现状（2026-09-28 更新）
- **首选 pyvista 0.49.0（已装，含 VTK 9.7.0）**：off-screen 渲染已实测（`outputs/install_smoke_20260928/pyvista_sphere.png`）
- **兜底 matplotlib mplot3d**（简单曲面/散点/线框）：无真实光照/材质/阴影、隐面处理弱 → 复杂网格会出现视觉歧义；兜底成图必须声明"mplot3d 生成（限制：无真光照）"

## mplot3d 兜底规范
1. 三轴必须带量名与单位；视角固定（`view_init(elev, azim)` 显式）并写进脚本（可复现）
2. 用 `plot_surface` 的 `cmap` 承载 z 值语义 + colorbar；点数 >200² 时降采样并说明
3. 网格线（`edgecolor`）按需：大曲面关网格或极细线
4. 禁默认 panes 灰底配色，用白底 + 浅灰网格面

## pyvista 规范（API 按 0.49.0 运行时实测）
- `off_screen=True` 无头渲染；高分辨率截图两条均有效：`screenshot(scale=N)`（0.49 签名含 `scale` 参数，实测核验）或 plotter 级 **`Plotter.image_scale` 属性**（非方法）
- 矢量导出：`Plotter.save_graphic()`（存在，实测核验）；3D 图通常仍以栅格呈现 + 矢量容器复合
- mesh 减面（decimate）控制体量；坐标轴单位、scale bar
- 相机参数（position/focal_point/up）写入脚本；体渲染（volume）注明传递函数设定
- **主路径基准**：`benchmarks/figure_families/b14_pyvista_3d.py`（PyVista 渲染 → matplotlib 复合 → figure-quality-gate）；兜底路径基准：b12（mplot3d，声明限制）

## 输入与证据
- 点云/mesh/体数据的真实来源文件；颜色映射的数量含义必须在 colorbar 注明单位
- 几何示意（非实测几何）标 schematic

## 输出与 QA
- PNG ≥300dpi（+ 可能的 SVG 轮廓）+ 灰度 + 缩印预览；**必经 `figure-quality-gate`**（文字重叠与字号照查）
- 附加目检：遮挡关系是否可读、色标语义、视角是否歧义

## 失败条件
- 需求超出 mplot3d 能表达的范围（复杂网格 hero 图）且 pyvista 因环境原因不可用 → 停手报告，不做伪 3D
