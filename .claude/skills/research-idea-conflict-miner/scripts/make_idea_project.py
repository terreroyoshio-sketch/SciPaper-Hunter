#!/usr/bin/env python3
"""
Research Idea Project Generator
Creates a standardized project directory for the research-idea-conflict-miner.

Usage:
    python make_idea_project.py --topic "Free breathing MRI GRASP" --output ./mri_idea
"""

import argparse
from pathlib import Path
from datetime import datetime
import shutil

TEMPLATES_DIR = Path(__file__).parent.parent / "templates"


def main():
    parser = argparse.ArgumentParser(
        description="Create a research idea incubation project"
    )
    parser.add_argument("--topic", "-t", required=True, help="Research topic")
    parser.add_argument("--output", "-o", default=".", help="Output directory")

    args = parser.parse_args()
    base = Path(args.output).resolve()
    base.mkdir(parents=True, exist_ok=True)

    dirs = [
        "00_plan", "01_materials", "02_evidence",
        "03_conflicts", "04_hypotheses",
        "05_constraints", "06_review", "07_output", "08_decision",
    ]
    for d in dirs:
        (base / d).mkdir(exist_ok=True)

    # Copy or create files
    template_map = {
        "00_plan/field_definition.md": "field_definition.md",
        "02_evidence/literature_evidence_matrix.csv": "literature_evidence_matrix.csv",
        "03_conflicts/conflict_map.md": "conflict_map.md",
        "04_hypotheses/hypothesis_translation.md": "hypothesis_translation.md",
        "05_constraints/constraint_audit.md": "constraint_audit.md",
        "06_review/reviewer_attack.md": "reviewer_attack.md",
        "07_output/minimal_viable_research_plan.md": "minimal_viable_research_plan.md",
        "08_decision/decision_report.md": "decision_report.md",
    }
    for rel_path, tmpl in template_map.items():
        src = TEMPLATES_DIR / tmpl
        dst = base / rel_path
        if src.exists():
            shutil.copy2(src, dst)

    # material_inventory.md
    with open(base / "01_materials/material_inventory.md", "w") as f:
        f.write(f"# Material Inventory\n\n**Topic:** {args.topic}\n**Date:** {datetime.now().strftime('%Y-%m-%d')}\n\n| Type | Source | Read | Usable | Risk |\n|------|--------|------|--------|------|\n| | | | | |\n")

    # README
    with open(base / "README.md", "w") as f:
        f.write(f"# {args.topic}\n\n**Created:** {datetime.now().strftime('%Y-%m-%d')}\n\n**Status:** Stage 0 — Task Freeze\n\n1. Edit 00_plan/field_definition.md\n2. Collect materials in 01_materials/\n3. Build evidence matrix in 02_evidence/\n")

    dir_count = len(list(base.rglob("*")))
    file_count = len(list(base.rglob("*.*")))
    print(f"Idea project created: {base}")
    print(f"  Topic: {args.topic}")
    print(f"  Files: {file_count}")


if __name__ == "__main__":
    main()
