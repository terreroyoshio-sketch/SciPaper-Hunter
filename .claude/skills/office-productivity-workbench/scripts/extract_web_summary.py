#!/usr/bin/env python3
"""Extract structured summary from web content (markdown input).
Usage: extract_web_summary.py <input_markdown> <output_dir>
"""

import sys
import os
import re
from datetime import datetime


def extract_summary(input_path, output_dir):
    """Parse a markdown web extract and generate structured summary."""
    os.makedirs(output_dir, exist_ok=True)

    with open(input_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Extract basic info
    url = _extract_field(content, r"\*\*URL:\*\*\s*(.*)")
    title = _extract_field(content, r"\*\*标题:\*\*\s*(.*)")
    access_date = _extract_field(content, r"\*\*访问日期:\*\*\s*(.*)")

    summary = f"""# Web Summary

**URL:** {url}
**Title:** {title}
**Access Date:** {access_date or datetime.now().strftime('%Y-%m-%d')}
**Processed:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

## Key Points
"""

    # Extract key points
    points = re.findall(r"^\d+\.\s*(.*)", content, re.MULTILINE)
    for i, point in enumerate(points[:10], 1):
        summary += f"{i}. {point}\n"

    summary += "\n## Source\n"
    summary += f"- Input file: {input_path}\n"
    summary += f"- Extracted: {datetime.now().isoformat()}\n"

    out_path = os.path.join(output_dir, "web_summary.md")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(summary)

    print(f"[OK] Summary written to {out_path}")
    return out_path


def _extract_field(text, pattern):
    match = re.search(pattern, text)
    return match.group(1).strip() if match else ""


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: extract_web_summary.py <input_markdown> <output_dir>")
        sys.exit(1)
    extract_summary(sys.argv[1], sys.argv[2])
