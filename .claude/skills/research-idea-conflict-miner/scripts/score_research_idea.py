#!/usr/bin/env python3
"""
Score research ideas based on constraint audit.
Reads a constraint_audit.md file and produces a scored evaluation.

Usage:
    python score_research_idea.py 05_constraints/constraint_audit.md
    python score_research_idea.py 05_constraints/constraint_audit.md --output report.md
"""

import re
import sys
import argparse
from pathlib import Path


def extract_scores(text: str) -> list:
    """Extract scores from constraint audit markdown."""
    ideas = []
    current_idea = None
    dimensions = {}

    for line in text.split("\n"):
        # Match idea headers
        m = re.match(r"^###\s+(H\d+|[A-Z][^:]+)", line)
        if m:
            if current_idea and dimensions:
                ideas.append({"name": current_idea, "dimensions": dict(dimensions)})
            current_idea = m.group(1).strip()
            dimensions = {}

        # Match dimension lines like "| 变量 | 3/5 | ..."
        dm = re.match(r"^\|\s*(\w+)\s*\|\s*(\d+)/5\s*\|", line)
        if dm and current_idea:
            dimensions[dm.group(1)] = int(dm.group(2))

    if current_idea and dimensions:
        ideas.append({"name": current_idea, "dimensions": dict(dimensions)})

    return ideas


def classify(total: int) -> str:
    if total >= 35:
        return "A. 值得立即做"
    elif total >= 25:
        return "B. 可以做，但需收缩"
    elif total >= 15:
        return "C. 补材料再判断"
    else:
        return "D. 不建议做"


def main():
    parser = argparse.ArgumentParser(description="Score research ideas")
    parser.add_argument("audit_file", help="Path to constraint_audit.md")
    parser.add_argument("--output", "-o", help="Output report path")
    args = parser.parse_args()

    path = Path(args.audit_file)
    if not path.exists():
        print(f"ERROR: File not found: {args.audit_file}")
        sys.exit(1)

    with open(path) as f:
        text = f.read()

    ideas = extract_scores(text)

    if not ideas:
        print("No ideas found in the audit file.")
        print("Ensure ideas are formatted as ### headers with | dimension | X/5 | rows.")
        sys.exit(1)

    lines = ["# Research Idea Scores\n"]
    for idea in ideas:
        dims = idea["dimensions"]
        total = sum(dims.values())
        classification = classify(total)
        lines.append(f"## {idea['name']}")
        lines.append(f"| Dimension | Score |")
        lines.append(f"|-----------|-------|")
        for d, s in dims.items():
            bars = "█" * s + "░" * (5 - s)
            lines.append(f"| {d} | {s}/5 {bars} |")
        lines.append(f"| **Total** | **{total}/40** |")
        lines.append(f"| **Conclusion** | **{classification}** |\n")

    report = "\n".join(lines)

    if args.output:
        with open(args.output, "w") as f:
            f.write(report)
        print(f"Report written: {args.output}")
    else:
        print(report)

    # Show summary
    print("\n=== Score Summary ===")
    for idea in ideas:
        total = sum(idea["dimensions"].values())
        print(f"  {idea['name']}: {total}/40 → {classify(total)}")


if __name__ == "__main__":
    main()
