#!/usr/bin/env python3
"""
Survey Project Structure Generator
Creates a standardized directory structure for a survey/literature review project.

Usage:
    python make_project_structure.py --topic "My Survey Topic" --output ./my_survey
    python make_project_structure.py --topic "Transformer Surveys" --output ./transformer_survey --lang en
    python make_project_structure.py --topic "机器学习可解释性综述" --output ./xai_survey --lang zh
"""

import os
import sys
import argparse
from pathlib import Path
from datetime import datetime


TEMPLATE_DIR = Path(__file__).parent.parent / "templates"


def create_directory_structure(base_path: Path):
    """Create the full directory tree."""
    dirs = [
        "docs",
        "papers",
        "references",
        "notes/evidence_cards",
        "structure",
        "manuscript/sections",
        "figures",
        "tables",
        "reviews",
        "reports",
        "outputs/final",
        "outputs/review_reports",
        "logs",
        "versions",
    ]

    for d in dirs:
        (base_path / d).mkdir(parents=True, exist_ok=True)
        (base_path / d / ".gitkeep").touch(exist_ok=True)

    return dirs


def create_project_plan(base_path: Path, topic: str, lang: str):
    """Generate project_plan.md from template with default values."""
    plan_path = base_path / "project_plan.md"
    template_path = TEMPLATE_DIR / "review_project_plan.md"

    if template_path.exists():
        with open(template_path, "r", encoding="utf-8") as f:
            content = f.read()
    else:
        content = "# Project Plan: {综述标题}\n\n*Edit this file to define your review scope.*\n"

    content = content.replace("{综述标题}", topic)
    content = content.replace("{研究主题}", topic)
    content = content.replace("{YYYY-MM-DD}", datetime.now().strftime("%Y-%m-%d"))
    content = content.replace("{语言}", "中文" if lang == "zh" else "English")
    content = content.replace("{学科方向}", "待补充")
    content = content.replace("{目标期刊/课程/项目}", "待补充")
    content = content.replace("{页数或字数}", "待补充")
    content = content.replace("{叙述性综述/系统综述/范围综述/元分析}", "叙述性综述 (Narrative Review)")

    with open(plan_path, "w", encoding="utf-8") as f:
        f.write(content)

    return plan_path


def create_search_log(base_path: Path, topic: str):
    """Generate search_log.md template."""
    log_path = base_path / "references/search_log.md"
    content = f"""# Search Log

**Project:** {topic}
**Created:** {datetime.now().strftime("%Y-%m-%d")}

## Search Queries

| # | Query | Database | Date | Results | Relevant | Notes |
|---|-------|----------|------|---------|----------|-------|
| 1 |  |  |  |  |  |  |

## Source Databases

- arXiv:
- Semantic Scholar:
- Google Scholar:
- PubMed:
- IEEE Xplore:
- Other:

## Notes

*Record each query here. Track what worked and what didn't.*
"""
    with open(log_path, "w", encoding="utf-8") as f:
        f.write(content)
    return log_path


def create_literature_matrix(base_path: Path):
    """Copy literature_matrix.csv template or create default."""
    target = base_path / "references/literature_matrix.csv"
    template_path = TEMPLATE_DIR / "literature_matrix.csv"

    if template_path.exists():
        with open(template_path, "r", encoding="utf-8") as src:
            with open(target, "w", encoding="utf-8") as dst:
                dst.write(src.read())
    else:
        with open(target, "w", encoding="utf-8") as f:
            f.write("title,authors,year,venue,doi,lqs_score,category,theme_cluster,key_finding,limitation\n")

    return target


def create_citation_verification(base_path: Path):
    """Copy citation_verification.csv template or create default."""
    target = base_path / "references/citation_verification.csv"
    template_path = TEMPLATE_DIR / "citation_verification.csv"

    if template_path.exists():
        with open(template_path, "r", encoding="utf-8") as src:
            with open(target, "w", encoding="utf-8") as dst:
                dst.write(src.read())
    else:
        with open(target, "w", encoding="utf-8") as f:
            f.write("bibtex_key,title,doi,title_match,doi_resolvable,year_match,status\n")

    return target


def create_version_log(base_path: Path):
    """Create version_log.md."""
    target = base_path / "version_log.md"
    content = """# Version Log

## v0.1 — {date}
**Status:** Draft
**Changes:**
- Initial project structure created
- (Fill in as work progresses)

---

| Version | Date | Status | Notes |
|---------|------|--------|-------|
| v0.1 | {date} | Initial | Project scaffold |
""".replace("{date}", datetime.now().strftime("%Y-%m-%d"))

    with open(target, "w", encoding="utf-8") as f:
        f.write(content)
    return target


def create_agent_run_log(base_path: Path):
    """Create agent run log CSV."""
    target = base_path / "logs/agent_run_log.csv"
    content = "timestamp,task,input_files,output_files,model,estimated_tokens,needs_human_approval,passed_gates\n"
    with open(target, "w", encoding="utf-8") as f:
        f.write(content)
    return target


def create_manuscript_template(base_path: Path, topic: str, lang: str):
    """Create manuscript section templates."""
    if lang == "zh":
        sections = {
            "00_abstract": "# 摘要\n\n*待补充*\n\n**关键词：** ",
            "01_introduction": "# 引言\n\n## 研究背景\n\n*待补充*\n\n## 当前矛盾\n\n*待补充*\n\n## 现有综述不足\n\n*待补充*\n\n## 本文贡献\n\n*待补充*\n\n## 文章结构\n\n*待补充*",
            "02_background": "# 背景\n\n## 核心概念\n\n*待补充*\n\n## 任务定义\n\n*待补充*\n\n## 基础理论\n\n*待补充*",
            "03_taxonomy": "# Taxonomy\n\n## 分类依据\n\n*待补充*\n\n## 分类结构\n\n*待补充*\n\n## 各类别关系\n\n*待补充*",
            "04_main_body_1": "# 主体：{主题1}\n\n*待补充*",
            "05_main_body_2": "# 主体：{主题2}\n\n*待补充*",
            "06_main_body_3": "# 主体：{主题3}\n\n*待补充*",
            "07_comparative_analysis": "# 对比分析\n\n## 方法对比\n\n*待补充*\n\n## 优缺点分析\n\n*待补充*",
            "08_challenges": "# 挑战与开放问题\n\n## 未解决问题\n\n*待补充*\n\n## 方法瓶颈\n\n*待补充*\n\n## 数据瓶颈\n\n*待补充*",
            "09_future_directions": "# 未来方向\n\n*待补充*",
            "10_conclusion": "# 结论\n\n*待补充*",
        }
    else:
        sections = {
            "00_abstract": "# Abstract\n\n*To be added*\n\n**Keywords:** ",
            "01_introduction": "# Introduction\n\n## Background\n\n*To be added*\n\n## Open Challenges\n\n*To be added*\n\n## Limitations of Existing Surveys\n\n*To be added*\n\n## Contributions\n\n*To be added*\n\n## Structure\n\n*To be added*",
            "02_background": "# Background\n\n## Core Concepts\n\n*To be added*\n\n## Problem Definition\n\n*To be added*\n\n## Foundational Knowledge\n\n*To be added*",
            "03_taxonomy": "# Taxonomy\n\n## Classification Criteria\n\n*To be added*\n\n## Taxonomy Structure\n\n*To be added*\n\n## Relationships\n\n*To be added*",
            "04_main_body_1": "# Main Body: {Topic 1}\n\n*To be added*",
            "05_main_body_2": "# Main Body: {Topic 2}\n\n*To be added*",
            "06_main_body_3": "# Main Body: {Topic 3}\n\n*To be added*",
            "07_comparative_analysis": "# Comparative Analysis\n\n*To be added*",
            "08_challenges": "# Challenges & Open Problems\n\n*To be added*",
            "09_future_directions": "# Future Directions\n\n*To be added*",
            "10_conclusion": "# Conclusion\n\n*To be added*",
        }

    section_dir = base_path / "manuscript/sections"
    for filename, content in sections.items():
        filepath = section_dir / f"{filename}.md"
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)

    return section_dir


def create_readme(base_path: Path, topic: str):
    """Create project README."""
    target = base_path / "README.md"
    content = f"""# {topic}

## Project Structure

```
project/
├── docs/                  # Documentation and notes
├── papers/                # Downloaded PDFs
├── references/            # BibTeX, literature matrix, citation verification
├── notes/evidence_cards/  # Per-paper evidence cards
├── structure/             # Taxonomy and outline
├── manuscript/sections/   # Chapter drafts
├── figures/               # Generated figures
├── tables/                # Generated tables
├── reviews/               # Review reports
├── reports/               # Audit and quality reports
├── outputs/               # Final deliverables
├── logs/                  # Agent run logs
├── versions/              # Versioned snapshots
├── project_plan.md        # Stage 0 output
├── version_log.md         # Change tracking
└── agent_run_log.csv      # Run records
```

## Status

**Current Phase:** Stage 0 — Topic Freeze
**Last Updated:** {datetime.now().strftime("%Y-%m-%d")}

## Quick Start

1. Edit `project_plan.md` to define your review scope
2. Begin literature search (Stage 1)
3. Score and classify papers (Stage 2)
4. ... follow the 9-stage pipeline

*Generated by autonomous-survey-agent*
"""
    with open(target, "w", encoding="utf-8") as f:
        f.write(content)
    return target


def main():
    parser = argparse.ArgumentParser(
        description="Create a standardized survey project directory structure"
    )
    parser.add_argument("--topic", "-t", required=True,
                       help="Survey topic name")
    parser.add_argument("--output", "-o", default=".",
                       help="Output directory (default: current directory)")
    parser.add_argument("--lang", "-l", choices=["en", "zh"], default="en",
                       help="Language for templates (en/zh)")

    args = parser.parse_args()

    # Create base directory
    base_path = Path(args.output).resolve()
    if not base_path.exists():
        base_path.mkdir(parents=True, exist_ok=True)
        print(f"Created directory: {base_path}")
    else:
        print(f"Using existing directory: {base_path}")

    # Create directory structure
    print("\nCreating directory structure...")
    dirs = create_directory_structure(base_path)
    for d in dirs:
        print(f"  ✓ {d}/")

    # Create files
    print("\nCreating project files...")

    plan = create_project_plan(base_path, args.topic, args.lang)
    print(f"  ✓ project_plan.md")

    log = create_search_log(base_path, args.topic)
    print(f"  ✓ references/search_log.md")

    matrix = create_literature_matrix(base_path)
    print(f"  ✓ references/literature_matrix.csv")

    citation = create_citation_verification(base_path)
    print(f"  ✓ references/citation_verification.csv")

    vlog = create_version_log(base_path)
    print(f"  ✓ version_log.md")

    arlog = create_agent_run_log(base_path)
    print(f"  ✓ logs/agent_run_log.csv")

    sections = create_manuscript_template(base_path, args.topic, args.lang)
    print(f"  ✓ manuscript/sections/ (11 files)")

    readme = create_readme(base_path, args.topic)
    print(f"  ✓ README.md")

    print(f"\n{'='*50}")
    print(f"Survey project created successfully!")
    print(f"Location: {base_path}")
    print(f"Topic: {args.topic}")
    print(f"Language: {'中文' if args.lang == 'zh' else 'English'}")
    print(f"{'='*50}")
    print(f"\nNext steps:")
    print(f"  1. Edit project_plan.md to define your scope")
    print(f"  2. Start Stage 1: Literature search")
    print(f"  3. Follow the 9-stage pipeline in SKILL.md")


if __name__ == "__main__":
    main()
