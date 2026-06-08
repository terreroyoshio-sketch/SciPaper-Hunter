#!/usr/bin/env python3
"""
Export final decision report for research ideas.
Aggregates outputs from previous stages into a summary decision.

Usage:
    python export_decision_report.py --input 07_output/ --output 08_decision/decision_report.md
"""

import sys
import argparse
from pathlib import Path
from datetime import datetime


def collect_plans(plan_dir: Path) -> list:
    """Collect minimal viable research plans."""
    plans = []
    plan_file = plan_dir / "minimal_viable_research_plan.md"
    if plan_file.exists():
        plans.append(plan_file)
    return plans


def extract_title(text: str) -> str:
    for line in text.split("\n"):
        if line.strip().startswith("## 1.") or line.strip().startswith("##1."):
            parts = line.split("##")
            return parts[-1].strip() if parts else "Untitled"
    return "Untitled"


def extract_scores(plan_dir: Path) -> dict:
    """Try to extract constraint scores from the plan."""
    scores = {"variable": "?", "data": "?", "total": "?"}
    plan_file = plan_dir / "minimal_viable_research_plan.md"
    if not plan_file.exists():
        return scores
    text = plan_file.read_text()
    return scores


def main():
    parser = argparse.ArgumentParser(description="Export decision report")
    parser.add_argument("--input", "-i", default="07_output", help="Output directory with plans")
    parser.add_argument("--output", "-o", default="08_decision/decision_report.md", help="Output path")
    args = parser.parse_args()

    input_dir = Path(args.input)
    if not input_dir.exists():
        print(f"WARNING: Input directory not found: {args.input}")
        print("Creating minimal report.")

    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    plans = collect_plans(input_dir) if input_dir.exists() else []

    lines = [
        "# Decision Report",
        f"**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M')}\n",
        "## Ideas Evaluated",
    ]

    if plans:
        for p in plans:
            title = extract_title(p.read_text())
            lines.append(f"- {title}")
    else:
        lines.append("- No completed plans found")

    lines.extend([
        "",
        "## Recommendations",
        "",
        "**Most recommended:**",
        "**Not recommended:**",
        "**Needs more literature:**",
        "**Needs more data:**",
        "**Ethics concern:**",
        "**Highest publication risk:**",
        "",
        "## Final Conclusion",
        "- [ ] A. 立即推进",
        "- [ ] B. 收缩后推进",
        "- [ ] C. 补材料后再判断",
        "- [ ] D. 放弃",
        "",
        "## Next Step",
        "1.",
        "2.",
        "3.",
    ])

    report = "\n".join(lines)
    with open(output_path, "w") as f:
        f.write(report)
    print(f"Decision report written: {output_path}")
    print(f"Plans evaluated: {len(plans)}")


if __name__ == "__main__":
    main()
