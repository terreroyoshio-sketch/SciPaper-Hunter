#!/usr/bin/env python3
"""
LaTeX Compilation Checker
Runs latexmk on a .tex file and captures compilation results.
Reports errors, warnings, and undefined references.

Usage:
    python check_latex_compile.py manuscript.tex
    python check_latex_compile.py manuscript.tex --clean
    python check_latex_compile.py manuscript.tex --timeout 120
"""

import os
import sys
import subprocess
import argparse
import re
from pathlib import Path
from datetime import datetime


def check_dependencies():
    """Check if latexmk and bibtex are available."""
    missing = []
    for cmd in ["latexmk", "bibtex"]:
        result = subprocess.run(
            ["where" if os.name == "nt" else "which", cmd],
            capture_output=True, text=True
        )
        if result.returncode != 0:
            missing.append(cmd)

    return missing


def compile_latex(tex_path: str, clean: bool = False, timeout: int = 120) -> dict:
    """Run latexmk on the given .tex file."""
    result = {
        "success": False,
        "errors": [],
        "warnings": [],
        "undefined_refs": [],
        "undefined_citations": [],
        "log_path": None,
        "pdf_path": None,
        "return_code": -1,
    }

    tex_file = Path(tex_path)
    work_dir = tex_file.parent

    # Step 1: Clean if requested
    if clean:
        print("Cleaning auxiliary files...")
        subprocess.run(
            ["latexmk", "-C", tex_file.name],
            cwd=work_dir,
            capture_output=True, text=True
        )

    # Step 2: Compile with latexmk
    print(f"Compiling: {tex_path}")
    print(f"Working directory: {work_dir}")

    try:
        proc = subprocess.run(
            ["latexmk", "-pdf", "-interaction=nonstopmode",
             "-halt-on-error", tex_file.name],
            cwd=work_dir,
            capture_output=True, text=True,
            timeout=timeout
        )
        result["return_code"] = proc.returncode
        full_log = proc.stdout + "\n" + proc.stderr
    except subprocess.TimeoutExpired:
        result["errors"].append(f"Compilation timed out after {timeout}s")
        return result
    except FileNotFoundError:
        result["errors"].append("latexmk not found. Is LaTeX installed?")
        return result

    # Step 3: Parse output for errors and warnings
    error_patterns = [
        (r"!\s*(.*)", "error"),
        (r"LaTeX Error:\s*(.*)", "error"),
        (r"Package.*Error:\s*(.*)", "error"),
        (r"LaTeX Warning:\s*(.*)", "warning"),
        (r"Package.*Warning:\s*(.*)", "warning"),
        (r"Citation\s+`(.*?)'\s+on page.*undefined", "undef_cite"),
        (r"Reference\s+`(.*?)'\s+on page.*undefined", "undef_ref"),
        (r"Undefined citation\s+`(.*?)'", "undef_cite"),
        (r"Undefined reference\s+`(.*?)'", "undef_ref"),
    ]

    for line in full_log.split("\n"):
        for pattern, category in error_patterns:
            match = re.search(pattern, line)
            if match:
                msg = match.group(1).strip()
                if category == "error":
                    result["errors"].append(msg)
                elif category == "warning":
                    result["warnings"].append(msg)
                elif category == "undef_cite":
                    result["undefined_citations"].append(msg)
                elif category == "undef_ref":
                    result["undefined_refs"].append(msg)
                break

    # Deduplicate
    result["errors"] = list(dict.fromkeys(result["errors"]))
    result["warnings"] = list(dict.fromkeys(result["warnings"]))
    result["undefined_citations"] = list(dict.fromkeys(result["undefined_citations"]))
    result["undefined_refs"] = list(dict.fromkeys(result["undefined_refs"]))

    # Check for output PDF
    pdf_path = work_dir / tex_file.stem.replace(".tex", ".pdf")
    if pdf_path.exists():
        result["pdf_path"] = str(pdf_path)
        result["success"] = True

    # Log file
    log_path = work_dir / (tex_file.stem + ".log")
    if log_path.exists():
        result["log_path"] = str(log_path)

    return result


def generate_report(result: dict, output_path: str = None):
    """Generate a compilation report."""
    now = datetime.now().strftime("%Y-%m-%d %H:%M")

    lines = [
        "# LaTeX Compilation Report",
        f"**Generated:** {now}",
        "",
        "## Summary",
        f"| Metric | Value |",
        f"|--------|-------|",
        f"| Compilation success | {'✅ Yes' if result['success'] else '❌ No'} |",
        f"| Errors | {len(result['errors'])} |",
        f"| Warnings | {len(result['warnings'])} |",
        f"| Undefined citations | {len(result['undefined_citations'])} |",
        f"| Undefined references | {len(result['undefined_refs'])} |",
        f"| PDF output | {'Yes' if result['pdf_path'] else 'No'} |",
        "",
    ]

    if result["errors"]:
        lines.extend(["## ❌ Errors", ""])
        for i, e in enumerate(result["errors"], 1):
            lines.append(f"{i}. {e}")
        lines.append("")

    if result["undefined_citations"]:
        lines.extend(["## ❓ Undefined Citations", ""])
        for c in result["undefined_citations"]:
            lines.append(f"- `{c}`")
        lines.append("")

    if result["undefined_refs"]:
        lines.extend(["## ❓ Undefined References", ""])
        for r in result["undefined_refs"]:
            lines.append(f"- `{r}`")
        lines.append("")

    if result["warnings"]:
        lines.extend(["## ⚠️ Warnings", ""])
        for i, w in enumerate(result["warnings"], 1):
            lines.append(f"{i}. {w}")
        lines.append("")

    if result["success"]:
        lines.append(f"**PDF:** {result['pdf_path']}")
        lines.append("")
        lines.append("✅ Compilation succeeded.")
    else:
        lines.append("❌ Compilation failed. Review errors above.")

    report = "\n".join(lines)

    if output_path:
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(report)
        print(f"Report written to: {output_path}")
    else:
        print(report)


def main():
    parser = argparse.ArgumentParser(
        description="Check LaTeX compilation and report errors"
    )
    parser.add_argument("texfile", help="Path to main .tex file")
    parser.add_argument("--clean", "-c", action="store_true",
                       help="Clean auxiliary files before compiling")
    parser.add_argument("--output", "-o", help="Output report path")
    parser.add_argument("--timeout", "-t", type=int, default=120,
                       help="Compilation timeout in seconds")

    args = parser.parse_args()

    # Check file
    tex_path = Path(args.texfile)
    if not tex_path.exists():
        print(f"ERROR: File not found: {args.texfile}")
        sys.exit(1)

    # Check dependencies
    missing_deps = check_dependencies()
    if missing_deps:
        print(f"ERROR: Missing dependencies: {', '.join(missing_deps)}")
        print("Install MiKTeX or TeX Live to proceed.")
        sys.exit(1)

    # Compile
    print(f"Checking LaTeX compilation: {args.texfile}")
    result = compile_latex(args.texfile, clean=args.clean, timeout=args.timeout)

    # Generate report
    generate_report(result, args.output)

    # Return exit code
    sys.exit(0 if result["success"] else 1)


if __name__ == "__main__":
    main()
