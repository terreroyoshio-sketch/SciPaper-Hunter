#!/usr/bin/env python3
"""Basic spreadsheet profiling: structure, nulls, stats.
Usage: analyze_spreadsheet.py <input_xlsx> <output_dir>
"""

import sys
import os
from datetime import datetime

try:
    import openpyxl
except ImportError:
    print("[ERROR] openpyxl not installed. Run: pip install openpyxl")
    sys.exit(1)


def analyze(input_path, output_dir):
    os.makedirs(output_dir, exist_ok=True)

    wb = openpyxl.load_workbook(input_path, data_only=True)
    sheet_names = wb.sheetnames

    report_lines = [
        f"# Spreadsheet Profile",
        f"",
        f"**File:** {os.path.basename(input_path)}",
        f"**Sheets:** {len(sheet_names)}",
        f"**Analysed:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        f"",
    ]

    for name in sheet_names:
        ws = wb[name]
        rows = ws.max_row or 0
        cols = ws.max_column or 0
        report_lines.append(f"## Sheet: {name}")
        report_lines.append(f"- Dimensions: {rows} rows × {cols} cols")
        report_lines.append("")

        if rows > 1 and cols > 0:
            # Headers
            headers = [str(ws.cell(1, c).value or "") for c in range(1, min(cols + 1, 21))]
            report_lines.append(f"- Headers: {' | '.join(headers)}")
            report_lines.append("")

            # Null check per column
            null_counts = []
            for c in range(1, min(cols + 1, 21)):
                nulls = 0
                for r in range(2, min(rows + 1, 101)):
                    if ws.cell(r, c).value is None:
                        nulls += 1
                null_rate = nulls / max(rows - 1, 1) * 100
                hdr = headers[c - 1] if c <= len(headers) else f"Col{c}"
                null_counts.append(f"  - {hdr}: {nulls} nulls ({null_rate:.1f}%)")

            if null_counts:
                report_lines.append("- **Null check (first 100 rows sample):**")
                report_lines.extend(null_counts)
                report_lines.append("")

    out_path = os.path.join(output_dir, "data_profile.md")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write("\n".join(report_lines))

    print(f"[OK] Profile written to {out_path}")


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: analyze_spreadsheet.py <input_xlsx> <output_dir>")
        sys.exit(1)
    analyze(sys.argv[1], sys.argv[2])
