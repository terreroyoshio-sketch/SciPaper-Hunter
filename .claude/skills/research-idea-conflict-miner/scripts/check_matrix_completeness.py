#!/usr/bin/env python3
"""
Check evidence matrix completeness.
Validates that all required fields are present and identifies unverified entries.

Usage:
    python check_matrix_completeness.py 02_evidence/literature_evidence_matrix.csv
"""

import sys
import csv
from pathlib import Path

REQUIRED_FIELDS = [
    "title", "authors", "year", "venue", "doi",
    "study_population", "sample_size", "core_variable",
    "comparator", "outcome", "statistical_method",
    "main_finding", "limitation", "data_source",
    "conflict_signal", "verification_status",
]


def main():
    if len(sys.argv) < 2:
        print("Usage: check_matrix_completeness.py <csv_file>")
        sys.exit(1)

    path = Path(sys.argv[1])
    if not path.exists():
        print(f"ERROR: File not found: {path}")
        sys.exit(1)

    with open(path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        rows = list(reader)

    print(f"Evidence Matrix: {path}")
    print(f"  Total entries: {len(rows)}")
    print(f"  Fields found: {list(rows[0].keys()) if rows else 'EMPTY'}")

    # Check required fields
    missing_fields = set()
    for row in rows:
        for rf in REQUIRED_FIELDS:
            val = row.get(rf, "")
            if val is None or str(val).strip() == "":
                missing_fields.add(rf)

    if missing_fields:
        print(f"\n  ⚠️  Missing fields: {', '.join(sorted(missing_fields))}")
    else:
        print(f"\n  ✅ All required fields present")

    # Check verification status
    def get_val(row, key):
        v = row.get(key, "")
        return str(v).lower().strip() if v else ""
    unverified = [r for r in rows if get_val(r, "verification_status") == "unverified"]
    abstract_only = [r for r in rows if get_val(r, "verification_status") == "abstract_only"]
    print(f"  Unverified entries: {len(unverified)}")
    print(f"  Abstract-only entries: {len(abstract_only)}")

    # Check conflict signals
    signals = set(str(r.get("conflict_signal", "")).strip() for r in rows if r.get("conflict_signal"))
    print(f"  Conflict signals found: {signals}")

    # Summary
    if unverified:
        print(f"\n  ⚠️  {len(unverified)} unverified entries — cannot be used for core conclusions")
        for u in unverified[:3]:
            print(f"      - {u.get('title', 'NO TITLE')[:60]}")
    if not rows:
        print(f"\n  ❌ Matrix is empty")
        sys.exit(1)
    else:
        print(f"\n  ✅ Matrix check complete")


if __name__ == "__main__":
    main()
