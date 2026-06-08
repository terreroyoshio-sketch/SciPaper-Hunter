#!/usr/bin/env python3
"""
Citation Coverage Checker
Verifies that:
1. All BibTeX entries are cited in the manuscript
2. All citations in the manuscript exist in BibTeX
3. No unused bibliography entries
4. Citation depth distribution (A/B/C/D)

Usage:
    python check_citation_coverage.py manuscript.tex references.bib
    python check_citation_coverage.py manuscript.tex references.bib --output report.md
"""

import re
import sys
import csv
import argparse
from pathlib import Path
from collections import Counter


def extract_tex_citations(tex_file: str) -> set:
    """Extract citation keys from a .tex file."""
    with open(tex_file, "r", encoding="utf-8") as f:
        content = f.read()

    citations = set()
    # \cite{key1,key2,...}
    cite_pattern = re.compile(r"\\cite(?:t|p|author|year|alt)?\s*\[.*?\]?\s*\{(.*?)\}")
    for match in cite_pattern.finditer(content):
        keys = [k.strip() for k in match.group(1).split(",")]
        citations.update(k for k in keys if k)

    # \citet{}, \citep{}, \citeauthor{}, etc.
    alt_pattern = re.compile(r"\\(?:citet|citep|citeauthor|citeyear|Citet|Citep)\s*\{(.*?)\}")
    for match in alt_pattern.finditer(content):
        keys = [k.strip() for k in match.group(1).split(",")]
        citations.update(k for k in keys if k)

    # nocite
    nocite_pattern = re.compile(r"\\nocite\s*\{(.*?)\}")
    for match in nocite_pattern.finditer(content):
        keys = [k.strip() for k in match.group(1).split(",")]
        if "*" in keys:
            return None  # nocite {*} means all

    return citations


def extract_md_citations(md_file: str) -> set:
    """Extract citation keys from a .md file (supports [@key] and @key patterns)."""
    with open(md_file, "r", encoding="utf-8") as f:
        content = f.read()

    citations = set()
    # [@key1; @key2]
    bracket_pattern = re.compile(r"\[([^\]]*@[^\]]*)\]")
    for match in bracket_pattern.finditer(content):
        inner = match.group(1)
        refs = re.findall(r"@(\w[\w:-]*)", inner)
        citations.update(refs)

    # standalone @key (not in brackets, not email)
    standalone = re.findall(r"(?<!\w)@(\w[\w:-]*)(?=\s|[.,;:!?)\]])", content)
    citations.update(standalone)

    return citations


def parse_bibtex_keys(bib_file: str) -> dict:
    """Extract citation keys and entry types from .bib file."""
    import check_bibtex as bt
    entries = bt.parse_bibtex(bib_file)
    return {key: entry["type"] for key, entry in entries.items()}


def read_lqs_csv(csv_file: str) -> dict:
    """Read LQS classification from CSV (optional)."""
    classification = {}
    try:
        with open(csv_file, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                key = row.get("bibtex_key", row.get("title", ""))
                category = row.get("category", row.get("lqs_score", "C"))
                classification[key] = category
    except FileNotFoundError:
        pass
    return classification


def generate_report(tex_cites: set, bib_keys: set, unused: set, missing: set,
                    lqs_data: dict, output_path: str = None):
    """Generate a markdown coverage report."""
    total_cited = len(tex_cites) if tex_cites else 0
    total_bib = len(bib_keys)
    coverage = len(bib_keys - unused)

    report_lines = [
        "# Citation Coverage Report",
        f"**Generated:** {__import__('datetime').datetime.now().strftime('%Y-%m-%d %H:%M')}",
        "",
        "## Summary",
        f"| Metric | Value |",
        f"|--------|-------|",
        f"| BibTeX entries | {total_bib} |",
        f"| Citations in manuscript | {total_cited} |",
        f"| Citations matched in BibTeX | {total_cited - len(missing)} |",
        f"| Unused BibTeX entries | {len(unused)} |",
        f"| Missing from BibTeX | {len(missing)} |",
        f"| Coverage rate | {coverage}/{total_bib} ({coverage/max(total_bib,1)*100:.1f}%) |",
        "",
    ]

    if missing:
        report_lines.extend([
            "## ❌ Citations Missing from BibTeX",
            "| Key |",
            "|-----|",
        ])
        for key in sorted(missing):
            report_lines.append(f"| {key} |")
        report_lines.append("")

    if unused:
        report_lines.extend([
            "## ⚠️ Unused BibTeX Entries",
            "| Key | Type |",
            "|-----|------|",
        ])
        for key in sorted(unused):
            entry_type = bib_keys.get(key, "unknown")
            report_lines.append(f"| {key} | {entry_type} |")
        report_lines.append("")

    # Citation depth distribution (if LQS data available)
    if lqs_data:
        depth_counts = Counter()
        for key in tex_cites or []:
            depth = lqs_data.get(key, "C")
            depth_counts[depth] += 1

        report_lines.extend([
            "## Citation Depth Distribution",
            "| Category | Count |",
            "|----------|-------|",
        ])
        for cat in ["A", "B", "C", "D"]:
            count = depth_counts.get(cat, 0)
            report_lines.append(f"| {cat} | {count} |")
        report_lines.append("")

    report_lines.append("## Status")
    if not missing and not unused:
        report_lines.append("✅ All citations match between manuscript and BibTeX.")
    else:
        report_lines.append("⚠️ Issues found (see above).")

    report = "\n".join(report_lines)

    if output_path:
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(report)
        print(f"Report written to: {output_path}")
    else:
        print(report)


def main():
    parser = argparse.ArgumentParser(
        description="Check citation coverage between manuscript and BibTeX"
    )
    parser.add_argument("manuscript", help="Path to .tex or .md manuscript file")
    parser.add_argument("bibfile", help="Path to .bib file")
    parser.add_argument("--output", "-o", help="Output report path")
    parser.add_argument("--lqs-csv", help="LQS classification CSV (optional)")

    args = parser.parse_args()

    # Verify files exist
    ms_path = Path(args.manuscript)
    bib_path = Path(args.bibfile)
    if not ms_path.exists():
        print(f"ERROR: Manuscript not found: {args.manuscript}")
        sys.exit(1)
    if not bib_path.exists():
        print(f"ERROR: BibTeX not found: {args.bibfile}")
        sys.exit(1)

    # Extract citations
    suffix = ms_path.suffix.lower()
    if suffix == ".tex":
        tex_cites = extract_tex_citations(args.manuscript)
    elif suffix == ".md":
        tex_cites = extract_md_citations(args.manuscript)
    else:
        print(f"ERROR: Unsupported file type: {suffix}")
        sys.exit(1)

    if tex_cites is None:
        print("Note: \\nocite{*} found - all BibTeX entries considered cited")
        # Can't check individual citations
    else:
        print(f"Found {len(tex_cites)} citations in manuscript")

    # Parse BibTeX
    bib_entries = parse_bibtex_keys(args.bibfile)
    bib_keys = set(bib_entries.keys())
    print(f"Found {len(bib_keys)} entries in BibTeX")

    # Check coverage
    missing = set()
    unused = set(bib_keys)

    if tex_cites is not None:
        missing = tex_cites - bib_keys
        for cite in tex_cites:
            unused.discard(cite)

        print(f"Missing from BibTeX: {len(missing)}")
        print(f"Unused entries: {len(unused)}")

        if missing:
            print(f"\n❌ Citations NOT in BibTeX:")
            for k in sorted(missing):
                print(f"  {k}")

        if unused:
            print(f"\n⚠️ Unused BibTeX entries:")
            for k in sorted(unused):
                print(f"  {k} (type: {bib_entries.get(k, '?')})")

    # Load LQS data
    lqs_data = {}
    if args.lqs_csv:
        lqs_data = read_lqs_csv(args.lqs_csv)

    # Generate report
    generate_report(tex_cites, bib_entries, unused, missing, lqs_data, args.output)

    # Exit code
    if missing:
        sys.exit(1)


if __name__ == "__main__":
    main()
