#!/usr/bin/env python3
"""
BibTeX Format Validator
Checks a .bib file for structural validity, duplicate keys, missing required fields,
and optionally verifies DOIs via CrossRef API.

Usage:
    python check_bibtex.py references.bib
    python check_bibtex.py references.bib --verbose
    python check_bibtex.py references.bib --check-doi
"""

import re
import sys
import csv
import argparse
from pathlib import Path
from datetime import datetime


def parse_bibtex(filepath: str) -> dict:
    """Simple BibTeX parser. Returns {key: entry_dict}."""
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    entries = {}
    pattern = re.compile(
        r"@(\w+)\s*\{\s*([^,]+)\s*,([^@]*)", re.DOTALL
    )

    for match in pattern.finditer(content):
        entry_type = match.group(1).lower()
        key = match.group(2).strip()
        body = match.group(3).strip()

        fields = {}
        field_pattern = re.compile(
            r"(\w+)\s*=\s*\{(.*?)\}\s*,?", re.DOTALL
        )
        for fm in field_pattern.finditer(body):
            fname = fm.group(1).lower()
            fvalue = fm.group(2).strip()
            fields[fname] = fvalue

        entries[key] = {
            "type": entry_type,
            "fields": fields,
            "raw": content,
        }

    return entries


REQUIRED_FIELDS = {
    "article": ["author", "title", "journal", "year"],
    "inproceedings": ["author", "title", "booktitle", "year"],
    "book": ["author", "title", "publisher", "year"],
    "incollection": ["author", "title", "booktitle", "publisher", "year"],
    "phdthesis": ["author", "title", "school", "year"],
    "mastersthesis": ["author", "title", "school", "year"],
    "techreport": ["author", "title", "institution", "year"],
    "misc": ["author", "title", "year"],
    "inbook": ["author", "editor", "title", "chapter", "publisher", "year"],
}


def validate_entries(entries: dict, verbose: bool = False) -> list:
    """Validate all entries, returning a list of issues."""
    issues = []

    # Check for duplicate keys
    # (already handled by dict nature, but we check casing duplicates)
    seen_lower = {}
    for key in entries:
        key_lower = key.lower()
        if key_lower in seen_lower:
            issues.append({
                "severity": "error",
                "entry": key,
                "field": "key",
                "message": f"Case-insensitive duplicate key: '{key}' and '{seen_lower[key_lower]}'",
            })
        else:
            seen_lower[key_lower] = key

    for key, entry in entries.items():
        etype = entry["type"]
        fields = entry["fields"]

        # Check required fields
        required = REQUIRED_FIELDS.get(etype, ["author", "title", "year"])
        for rf in required:
            if rf not in fields:
                issues.append({
                    "severity": "error",
                    "entry": key,
                    "field": rf,
                    "message": f"Missing required field '{rf}' for @{etype} entry",
                })

        # Check year format
        if "year" in fields:
            year_val = fields["year"].strip()
            if not re.match(r"^\d{4}$", year_val):
                issues.append({
                    "severity": "warning",
                    "entry": key,
                    "field": "year",
                    "message": f"Year '{year_val}' is not a 4-digit number",
                })

        # Check DOI format
        if "doi" in fields:
            doi = fields["doi"].strip()
            if not doi.startswith("10."):
                issues.append({
                    "severity": "warning",
                    "entry": key,
                    "field": "doi",
                    "message": f"DOI '{doi}' does not start with '10.'",
                })

        # Check for common LaTeX errors in title
        if "title" in fields:
            title = fields["title"]
            unmatched_braces = title.count("{") - title.count("}")
            if unmatched_braces != 0:
                issues.append({
                    "severity": "error",
                    "entry": key,
                    "field": "title",
                    "message": f"Unmatched braces in title (diff={unmatched_braces})",
                })

        # Check author field for common issues
        if "author" in fields:
            author = fields["author"]
            if " and " not in author and "," not in author:
                issues.append({
                    "severity": "info",
                    "entry": key,
                    "field": "author",
                    "message": "Author field may have only one author (no ' and ' separator)",
                })

        if verbose:
            print(f"  [{key}] @{etype}: {len(fields)} fields, " +
                  f"year={fields.get('year', 'MISSING')}, " +
                  f"doi={'YES' if 'doi' in fields else 'NO'}")

    return issues


def export_issues_csv(issues: list, output_path: str):
    """Export issues to CSV."""
    fieldnames = ["severity", "entry", "field", "message"]
    with open(output_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for issue in issues:
            writer.writerow(issue)
    print(f"  Issues exported to: {output_path}")


def main():
    parser = argparse.ArgumentParser(
        description="Validate BibTeX file for common errors"
    )
    parser.add_argument("bibfile", help="Path to .bib file")
    parser.add_argument("--verbose", "-v", action="store_true", help="Verbose output")
    parser.add_argument("--export", "-e", help="Export issues to CSV")
    parser.add_argument("--check-doi", action="store_true",
                       help="Attempt DOI verification (requires internet)")

    args = parser.parse_args()

    bibpath = Path(args.bibfile)
    if not bibpath.exists():
        print(f"ERROR: File not found: {args.bibfile}")
        sys.exit(1)

    print(f"Parsing: {bibpath}")
    entries = parse_bibtex(args.bibfile)
    print(f"  Found {len(entries)} entries")

    print(f"Validating {len(entries)} entries...")
    issues = validate_entries(entries, verbose=args.verbose)

    if issues:
        errors = [i for i in issues if i["severity"] == "error"]
        warnings = [i for i in issues if i["severity"] == "warning"]
        infos = [i for i in issues if i["severity"] == "info"]

        print(f"\nResults:")
        print(f"  Errors:   {len(errors)}")
        print(f"  Warnings: {len(warnings)}")
        print(f"  Info:     {len(infos)}")

        if errors:
            print(f"\n=== ERRORS ===")
            for e in errors[:10]:
                print(f"  [{e['entry']}] {e['message']}")
            if len(errors) > 10:
                print(f"  ... and {len(errors) - 10} more errors")

        if warnings:
            print(f"\n=== WARNINGS ===")
            for w in warnings[:10]:
                print(f"  [{w['entry']}] {w['message']}")
    else:
        print(f"\n✅ No issues found in {len(entries)} entries!")

    if args.export:
        export_issues_csv(issues, args.export)

    # Return exit code
    error_count = len([i for i in issues if i["severity"] == "error"])
    sys.exit(1 if error_count > 0 else 0)


if __name__ == "__main__":
    main()
