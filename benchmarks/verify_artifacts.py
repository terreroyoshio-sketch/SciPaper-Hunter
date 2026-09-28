"""Benchmark artifact verification: existence / zero-byte / image dims / sha256.

Usage:
  python benchmarks/verify_artifacts.py [--out reports/benchmark_artifacts_manifest_r3_20260928.csv]

Covers: figure_families/out, visual_quality/out, table_family/out,
and outputs/visual_quality_smoke. Emits one CSV row per file plus a
console summary (counts, zero-byte, dims, missing expected files).
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

SCAN_DIRS = [
    ROOT / "benchmarks" / "figure_families" / "out",
    ROOT / "benchmarks" / "visual_quality" / "out",
    ROOT / "benchmarks" / "table_family" / "out",
    ROOT / "outputs" / "visual_quality_smoke",
]

EXPECTED_FIGURE_FILES = 101  # 14 benches x (png/pdf/svg/gate.json/report.md/...) + contact sheet


def sha256_of(p: Path) -> str:
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def png_dims(p: Path):
    try:
        from PIL import Image
    except ImportError:
        return None
    try:
        with Image.open(p) as im:
            return im.size
    except Exception:
        return None


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default=str(ROOT / "reports" / "benchmark_artifacts_manifest_r3_20260928.csv"))
    args = ap.parse_args()

    rows = []
    zero_byte = []
    missing_dirs = []
    fig_count = 0
    for d in SCAN_DIRS:
        if not d.exists():
            missing_dirs.append(str(d.relative_to(ROOT)))
            continue
        for p in sorted(d.rglob("*")):
            if not p.is_file() or p.suffix == ".pyc":
                continue
            rel = p.relative_to(ROOT).as_posix()
            size = p.stat().st_size
            if size == 0:
                zero_byte.append(rel)
            if d.name == "out" and "figure_families" in str(d):
                fig_count += 1
            dims = ""
            if p.suffix.lower() == ".png":
                wh = png_dims(p)
                if wh:
                    dims = f"{wh[0]}x{wh[1]}"
            rows.append((rel, size, sha256_of(p), dims))

    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    with open(out, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["path", "bytes", "sha256", "img_dims"])
        w.writerows(rows)

    print(f"files scanned : {len(rows)}")
    print(f"figure_families/out : {fig_count} files (expected {EXPECTED_FIGURE_FILES})")
    print(f"zero-byte : {len(zero_byte)} {zero_byte if zero_byte else ''}")
    print(f"missing dirs : {len(missing_dirs)} {missing_dirs if missing_dirs else ''}")
    bad_dims = [r[0] for r in rows if r[0].endswith(".png") and not r[3]]
    print(f"png with unreadable dims : {len(bad_dims)} {bad_dims if bad_dims else ''}")
    print(f"manifest -> {out}")

    ok = (not zero_byte) and (not missing_dirs) and (not bad_dims)
    print("VERDICT:", "PASS" if ok else "FAIL")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
