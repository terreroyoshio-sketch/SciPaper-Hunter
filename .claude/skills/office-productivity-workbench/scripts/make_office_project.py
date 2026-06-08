#!/usr/bin/env python3
"""Create a standard office project directory structure.

Usage:
    python make_office_project.py --name <project_name>
"""

import argparse
import os
from datetime import datetime


def create_project(name, base_dir="."):
    """Create office project directory structure."""
    project_dir = os.path.join(base_dir, name)

    structure = {
        "00_inputs": {
            "web": [],
            "pdf": [],
            "docs": [],
            "sheets": [],
            "images": [],
            "ppt": [],
        },
        "01_extracted": {
            "web_extract": [],
            "pdf_notes": [],
            "sheet_profile": [],
        },
        "02_drafts": {
            "documents": [],
            "slides": [],
            "content": [],
        },
        "03_review": {
            "fact_check": [],
            "style_check": [],
            "privacy_check": [],
        },
        "04_outputs": {
            "final_docs": [],
            "final_ppt": [],
            "final_images": [],
            "final_reports": [],
        },
        "05_archive": {},
        "logs": {},
        "reports": {},
    }

    created = []

    for parent, children in structure.items():
        parent_path = os.path.join(project_dir, parent)
        os.makedirs(parent_path, exist_ok=True)
        created.append(parent_path)

        if isinstance(children, dict):
            for child in children:
                child_path = os.path.join(parent_path, child)
                os.makedirs(child_path, exist_ok=True)
                created.append(child_path)

    # Create placeholder files
    placeholders = {
        "logs/file_change_log.csv": "timestamp,action,file_path,reason,agent_or_command,backup_path\n",
        "logs/task_log.csv": "timestamp,task,status,risk,notes\n",
        "logs/source_log.csv": "timestamp,source_url,title,access_date,notes\n",
        "reports/project_status.md": f"# {name} — Project Status\n\nCreated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n",
        "reports/final_delivery_checklist.md": f"# Final Delivery Checklist — {name}\n\nSee `.claude/skills/office-productivity-workbench/templates/final_delivery_checklist.md`\n",
    }

    for rel_path, content in placeholders.items():
        full_path = os.path.join(project_dir, rel_path)
        os.makedirs(os.path.dirname(full_path), exist_ok=True)
        with open(full_path, "w", encoding="utf-8") as f:
            f.write(content)
        created.append(full_path)

    print(f"[OK] Project '{name}' created at {project_dir}")
    print(f"     {len(created)} directories/files created")

    # Print structure
    print(f"\n{name}/")
    for parent, children in structure.items():
        print(f"  ├── {parent}/")
        if isinstance(children, dict):
            for child in children:
                print(f"  │   ├── {child}/")
    print(f"  ├── logs/")
    print(f"  │   ├── file_change_log.csv")
    print(f"  │   ├── task_log.csv")
    print(f"  │   └── source_log.csv")
    print(f"  └── reports/")
    print(f"      ├── project_status.md")
    print(f"      └── final_delivery_checklist.md")

    return project_dir


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Create office project structure")
    parser.add_argument("--name", required=True, help="Project name")
    parser.add_argument("--base", default=".", help="Base directory (default: current)")
    args = parser.parse_args()

    create_project(args.name, args.base)
