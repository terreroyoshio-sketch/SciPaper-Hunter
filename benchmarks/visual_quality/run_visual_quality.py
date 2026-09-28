"""Run T01-T04 visual-quality benchmarks with BEFORE/AFTER expectations.

Each case: build -> figure-quality-gate. The runner requires the expected
three-valued status (e.g. t02_before MUST fail, t02_after MUST pass); a status
mismatch is reported as EXPECTATION_MISMATCH and fails the run.
"""

from __future__ import annotations

import argparse
import importlib
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
_FAM = HERE.parent / "figure_families"
if str(_FAM) not in sys.path:
    sys.path.insert(0, str(_FAM))

import matplotlib.pyplot as plt  # noqa: E402

import bench_common as bc  # noqa: E402

CASES = [
    ("t01_typography", "t01_typography", "build", "PASS"),
    ("t02_before", "t02_curve_labels", "build_before", "FAIL"),
    ("t02_after", "t02_curve_labels", "build_after", "PASS"),
    ("t03_before", "t03_scatter_labels", "build_before", "FAIL"),
    ("t03_after", "t03_scatter_labels", "build_after", "PASS"),
    ("t04_before", "t04_roadmap_conflicts", "build_before", "FAIL"),
    ("t04_after", "t04_roadmap_conflicts", "build_after", "PASS"),
]


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default=str(HERE / "out"))
    args = ap.parse_args()
    out = Path(args.out)

    results = []
    for name, module, fn, expected in CASES:
        subdir = out / name
        try:
            mod = importlib.import_module(module)
            fig = getattr(mod, fn)()
            rep = bc.run_gate(fig, subdir, name, min_pt=bc.DEFAULT_MIN_PT)
            plt.close(fig)
            got = rep["status"]
            ok = got == expected
            results.append(
                {
                    "case": name,
                    "expected": expected,
                    "got": got,
                    "ok": bool(ok),
                    "fails": rep["fails"],
                    "collisions": rep.get("collisions"),
                    "png": rep["paths"].get("png"),
                }
            )
        except Exception as exc:  # noqa: BLE001
            plt.close("all")
            results.append({"case": name, "expected": expected, "got": "ERROR", "ok": False, "fails": [f"{type(exc).__name__}: {exc}"]})
            print(f"[visual-quality] {name} ERROR: {exc}")

    # T01 companion: typography smoke test (clean sheet + detector self-test)
    smoke = None
    if str(_FAM) not in sys.path:
        sys.path.insert(0, str(_FAM))
    try:
        from typography import smoke_test

        smoke = smoke_test(out / "t01_fonts", profile="sci-sans")
    except Exception as exc:  # noqa: BLE001
        smoke = {"error": f"{type(exc).__name__}: {exc}"}

    lines = ["# Visual-quality benchmark summary", "", "| case | expected | got | ok | fails |", "|---|---|---|---|---|"]
    for r in results:
        lines.append(f"| {r['case']} | {r['expected']} | **{r['got']}** | {'OK' if r['ok'] else 'MISMATCH'} | {'; '.join(r['fails'])[:160] or '-'} |")
    if smoke is not None:
        lines += ["", f"- typography smoke: clean_ok={smoke.get('clean_ok')} detector_caught_gap={smoke.get('detector_caught_gap')} fallback={smoke.get('fallback_status')}"]
    (out / "summary.md").write_text("\n".join(lines), encoding="utf-8")
    (out / "summary.json").write_text(json.dumps({"cases": results, "smoke": smoke}, ensure_ascii=False, indent=2), encoding="utf-8")
    print("\n".join(lines))

    # acceptance: every case matched its expectation AND smoke holds
    smoke_ok = bool(smoke and smoke.get("clean_ok") and smoke.get("detector_caught_gap"))
    all_ok = all(r["ok"] for r in results) and smoke_ok
    print("AGGREGATE:", "PASS" if all_ok else "FAIL")
    sys.exit(0 if all_ok else 1)


if __name__ == "__main__":
    main()
