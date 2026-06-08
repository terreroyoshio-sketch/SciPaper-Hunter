#!/usr/bin/env python3
"""
Research Project Structure Generator
Creates a comprehensive research project directory with all stages.

Usage:
    python make_project_structure.py --topic "Your Topic" --output ./my_project --lang en
"""

import os
import sys
import argparse
from pathlib import Path
from datetime import datetime
import shutil


TEMPLATES_DIR = Path(__file__).parent.parent / "templates"


def create_structure(base_path: Path, topic: str, lang: str):
    """Create the complete research project directory tree."""
    dirs = [
        "00_plan",
        "01_literature/bibtex",
        "01_literature/pdfs",
        "02_notes/evidence_cards",
        "02_notes/concept_notes",
        "02_notes/method_notes",
        "03_structure",
        "04_manuscript/sections",
        "05_figures_tables/figures",
        "05_figures_tables/tables",
        "06_review",
        "07_audit",
        "08_outputs/final_draft",
        "08_outputs/submission_package",
        "logs",
    ]

    for d in dirs:
        (base_path / d).mkdir(parents=True, exist_ok=True)

    # Create files
    create_project_plan(base_path, topic, lang)
    create_literature_files(base_path)
    create_manuscript_sections(base_path, topic, lang)
    create_tracking_files(base_path)
    create_readme(base_path, topic)


def create_project_plan(base_path: Path, topic: str, lang: str):
    """Create project_plan.md."""
    target = base_path / "00_plan/project_plan.md"
    template_src = TEMPLATES_DIR / "project_plan.md"

    if template_src.exists():
        shutil.copy2(template_src, target)
        # Read and replace placeholders
        with open(target, 'r', encoding='utf-8') as f:
            content = f.read()
        content = content.replace('{主题}', topic).replace('{语言}', lang)
        content = content.replace('{YYYY-MM-DD}', datetime.now().strftime('%Y-%m-%d'))
        with open(target, 'w', encoding='utf-8') as f:
            f.write(content)
    else:
        with open(target, 'w', encoding='utf-8') as f:
            f.write(f'# Project Plan: {topic}\n\nCreated: {datetime.now()}\n')

    # Create research questions
    rq_path = base_path / "00_plan/research_questions.md"
    with open(rq_path, 'w', encoding='utf-8') as f:
        f.write(f'# Research Questions\n\n## Main Question\n\n## Sub-questions\n1. \n2. \n3. \n')

    # Create inclusion/exclusion criteria
    ie_path = base_path / "00_plan/inclusion_exclusion_criteria.md"
    with open(ie_path, 'w', encoding='utf-8') as f:
        f.write(f'# Inclusion & Exclusion Criteria\n\n## Inclusion\n1. \n2. \n3. \n\n## Exclusion\n1. \n2. \n3. \n')


def create_literature_files(base_path: Path):
    """Create literature tracking files."""
    # raw_candidates.csv
    with open(base_path / "01_literature/raw_candidates.csv", 'w', encoding='utf-8') as f:
        f.write("title,authors,year,venue,doi,url,abstract,source_database,search_query,retrieval_date,pdf_status,verification_status\n")

    # screened_literature.csv
    with open(base_path / "01_literature/screened_literature.csv", 'w', encoding='utf-8') as f:
        f.write("title,authors,year,doi,lqs_score,category,reason,theme_cluster\n")

    # literature_matrix.csv
    template_src = TEMPLATES_DIR / "literature_matrix.csv"
    if template_src.exists():
        shutil.copy2(template_src, base_path / "01_literature/literature_matrix.csv")
    else:
        with open(base_path / "01_literature/literature_matrix.csv", 'w', encoding='utf-8') as f:
            f.write("title,authors,year,venue,doi,category,theme,key_finding\n")

    # search_log.md
    with open(base_path / "01_literature/search_log.md", 'w', encoding='utf-8') as f:
        f.write(f"# Search Log\n\nCreated: {datetime.now().strftime('%Y-%m-%d')}\n\n## Queries\n| # | Query | Database | Results | Relevant |\n|---|-------|----------|---------|----------|\n| 1 | | | | |\n")

    # citation_verification.csv
    template_src2 = TEMPLATES_DIR / "citation_verification.csv"
    if template_src2.exists():
        shutil.copy2(template_src2, base_path / "01_literature/citation_verification.csv")


def create_manuscript_sections(base_path: Path, topic: str, lang: str):
    """Create manuscript section templates."""
    if lang == 'zh':
        sections = {
            "00_abstract.md": "# 摘要\n\n**关键词:** ",
            "01_introduction.md": "# 引言\n\n## 研究背景\n\n## 研究问题\n\n## 本文贡献\n\n## 文章结构\n",
            "02_related_work.md": "# 相关工作\n\n",
            "03_background.md": "# 背景\n\n## 核心概念\n\n## 理论基础\n",
            "04_method.md": "# 方法\n\n",
            "05_experiments.md": "# 实验\n\n## 设置\n\n## 结果\n\n## 分析\n",
            "06_discussion.md": "# 讨论\n\n## 主要发现\n\n## 局限性\n\n## 未来工作\n",
            "07_conclusion.md": "# 结论\n\n",
            "08_references.md": "# 参考文献\n\n",
        }
    else:
        sections = {
            "00_abstract.md": "# Abstract\n\n**Keywords:** ",
            "01_introduction.md": "# Introduction\n\n## Background\n\n## Problem Statement\n\n## Contributions\n\n## Structure\n",
            "02_related_work.md": "# Related Work\n\n",
            "03_background.md": "# Background\n\n## Core Concepts\n\n## Foundations\n",
            "04_method.md": "# Method\n\n",
            "05_experiments.md": "# Experiments\n\n## Setup\n\n## Results\n\n## Analysis\n",
            "06_discussion.md": "# Discussion\n\n## Key Findings\n\n## Limitations\n\n## Future Work\n",
            "07_conclusion.md": "# Conclusion\n\n",
            "08_references.md": "# References\n\n",
        }

    section_dir = base_path / "04_manuscript/sections"
    for filename, content in sections.items():
        with open(section_dir / filename, 'w', encoding='utf-8') as f:
            f.write(content)


def create_tracking_files(base_path: Path):
    """Create tracking and log files."""
    # agent_run_log.csv
    with open(base_path / "logs/agent_run_log.csv", 'w', encoding='utf-8') as f:
        f.write("timestamp,task,input_files,output_files,model,estimated_tokens,needs_human_approval,passed_gates\n")

    # cost_log.csv
    with open(base_path / "logs/cost_log.csv", 'w', encoding='utf-8') as f:
        f.write("date,phase,task,tokens_in,tokens_out,estimated_cost_usd,notes\n")

    # version_log.md
    with open(base_path / "logs/version_log.md", 'w', encoding='utf-8') as f:
        f.write(f"# Version Log\n\n## v0.1 — {datetime.now().strftime('%Y-%m-%d')}\n**Status:** Initial scaffold\n**Changes:** Project structure created\n")

    # figure_table_plan.md
    with open(base_path / "05_figures_tables/figure_table_plan.md", 'w', encoding='utf-8') as f:
        f.write("# Figure & Table Plan\n\n## Figures\n| # | Type | Description | Status |\n|---|------|-------------|--------|\n| 1 | | | planned |\n\n## Tables\n| # | Type | Description | Status |\n|---|------|-------------|--------|\n| 1 | | | planned |\n")


def create_readme(base_path: Path, topic: str):
    """Create project README."""
    with open(base_path / "README.md", 'w', encoding='utf-8') as f:
        f.write(f"""# {topic}

**Created:** {datetime.now().strftime('%Y-%m-%d')}

## Directory Structure
```
00_plan/              # Project plan, research questions
01_literature/        # Literature search results, BibTeX, PDFs
02_notes/             # Evidence cards, concept/method notes
03_structure/         # Taxonomy and outline
04_manuscript/        # Manuscript sections and full drafts
05_figures_tables/    # Figures, tables, and plan
06_review/            # Review reports and revision plans
07_audit/             # Citation, ethics, reproducibility audits
08_outputs/           # Final deliverables
logs/                 # Run logs, cost logs, version logs
```

## Status
**Phase:** 0 — Task Freeze

*Generated by my-academic-research-master*
""")


def main():
    parser = argparse.ArgumentParser(
        description='Create a comprehensive research project structure'
    )
    parser.add_argument('--topic', '-t', required=True, help='Research topic')
    parser.add_argument('--output', '-o', default='.', help='Output directory')
    parser.add_argument('--lang', '-l', choices=['en', 'zh'], default='en',
                       help='Language for templates')

    args = parser.parse_args()

    base_path = Path(args.output).resolve()
    if not base_path.exists():
        base_path.mkdir(parents=True)

    create_structure(base_path, args.topic, args.lang)

    # Count created items
    dirs = [d for d in base_path.rglob('*') if d.is_dir()]
    files = [f for f in base_path.rglob('*') if f.is_file()]

    print(f'Research project created successfully!')
    print(f'  Location: {base_path}')
    print(f'  Topic: {args.topic}')
    print(f'  Directories: {len(dirs)}')
    print(f'  Files: {len(files)}')
    print(f'\nNext: Edit 00_plan/project_plan.md to define your scope.')


if __name__ == '__main__':
    main()
