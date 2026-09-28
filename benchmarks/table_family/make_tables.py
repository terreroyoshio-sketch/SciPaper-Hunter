"""TABLE01-05 benchmark: three-line tables (synthetic content) + rendered QA.

Run: python make_tables.py [--out out]
Per table: <id>.docx + <id>.pdf (QA render) + <id>_qa.json; aggregate:
table_layout_report.json. Exit 0 only when every table passes.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
SKILL_SCRIPTS = HERE.parents[1] / ".claude" / "skills" / "publication-table-layout" / "scripts"
if str(SKILL_SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SKILL_SCRIPTS))

from docx import Document  # noqa: E402
from three_line_table import add_three_line_table, style_document  # noqa: E402
import table_qa  # noqa: E402


def t01_short(doc):
    add_three_line_table(
        doc,
        headers=["Method", "Accuracy", "F1"],
        rows=[["Baseline", "0.812", "0.780"], ["Variant A", "0.845", "0.826"], ["Ours", "0.879", "0.851"]],
        col_align=["left", "center", "center"],
        caption="表 1. 方法对比（合成基准数据）",
    )


def t02_wide_numeric(doc):
    add_three_line_table(
        doc,
        headers=["Year", "R²", "RMSE", "MAE", "NSE", "KGE", "PBIAS (%)"],
        rows=[[str(y), f"{0.60 + 0.03 * i:.2f}", f"{1.20 - 0.05 * i:.2f}", f"{0.90 - 0.04 * i:.2f}",
               f"{0.55 + 0.04 * i:.2f}", f"{0.62 + 0.03 * i:.2f}", f"{-8.0 + 1.5 * i:.1f}"] for i, y in enumerate(range(2016, 2024))],
        col_align=["center"] * 7,
        caption="表 2. 逐年指标（合成数据）",
    )


def t03_long_text(doc):
    add_three_line_table(
        doc,
        headers=["建模方案", "输入变量", "输出指标"],
        rows=[
            ["分段线性回归叠加残差校正的多阶段建模框架", "降水、蒸散、土壤水", "综合指数"],
            ["基于耦合分布的联合概率模型", "边际分布参数", "事件强度"],
            ["梯度提升树与归因分解的联合分析", "特征矩阵", "贡献排序"],
        ],
        col_align=["left", "left", "center"],
        caption="表 3. 建模方案（长文本首列，合成）",
    )


def t04_mixed_cn_en(doc):
    add_three_line_table(
        doc,
        headers=["样本 Sample", "均值 Mean", "标准差 SD", "区间 Range"],
        rows=[
            ["训练集 Train", "0.612", "0.081", "0.40 – 0.78"],
            ["验证集 Valid", "0.598", "0.093", "0.35 – 0.77"],
            ["测试集 Test", "0.604", "0.088", "0.38 – 0.79"],
        ],
        col_align=["left", "center", "center", "center"],
        caption="表 4. 中英混排表（合成数据）",
    )


def t05_multipage(doc):
    rows = [[str(1970 + i), f"{12.5 + 0.4 * i:.1f}", f"{3.1 - 0.02 * i:.2f}", f"{88 - i:.0f}"] for i in range(40)]
    add_three_line_table(
        doc,
        headers=["Year", "Inflow (10⁸ m³)", "Sediment (kg/m³)", "Index"],
        rows=rows,
        col_align=["center"] * 4,
        caption="表 5. 多年序列（多页表，合成数据）",
    )


TABLES = {
    "TABLE01_short": t01_short,
    "TABLE02_wide_numeric": t02_wide_numeric,
    "TABLE03_long_text": t03_long_text,
    "TABLE04_mixed_cn_en": t04_mixed_cn_en,
    "TABLE05_multipage": t05_multipage,
}


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default=str(HERE / "out"))
    args = ap.parse_args()
    out = Path(args.out)
    out.mkdir(parents=True, exist_ok=True)

    results = []
    for name, builder in TABLES.items():
        doc = Document()
        style_document(doc)
        builder(doc)
        docx_path = out / f"{name}.docx"
        doc.save(str(docx_path))
        rep = table_qa.qa_docx(docx_path, out, render=True)
        (out / f"{name}_qa.json").write_text(json.dumps(rep, ensure_ascii=False, indent=2), encoding="utf-8")
        ren = rep.get("render") or {}
        results.append(
            {
                "id": name,
                "status": rep["status"],
                "center_error_mm": ren.get("center_error_mm"),
                "table_width_mm": ren.get("table_width_mm"),
                "text_area_width_mm": ren.get("text_area_width_mm"),
                "left_whitespace_mm": ren.get("left_whitespace_mm"),
                "right_whitespace_mm": ren.get("right_whitespace_mm"),
                "pages": ren.get("pages"),
                "rules_per_page": ren.get("rules_per_page"),
                "header_repeat_page2": ren.get("header_repeat_page2"),
                "violations": [v for t in rep["tables"] for v in t["violations"]],
            }
        )
        print(f"{name}: {rep['status']} center_error={ren.get('center_error_mm')}mm width={ren.get('table_width_mm')}mm")

    agg = {"tables": results, "status": "PASS" if all(r["status"] == "PASS" for r in results) else "FAIL"}
    (out / "table_layout_report.json").write_text(json.dumps(agg, ensure_ascii=False, indent=2), encoding="utf-8")
    print("AGGREGATE:", agg["status"])
    sys.exit(0 if agg["status"] == "PASS" else 1)


if __name__ == "__main__":
    main()
