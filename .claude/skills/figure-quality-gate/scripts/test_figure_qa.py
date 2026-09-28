"""Regression tests for figure_qa (run from this directory):
    python -m pytest test_figure_qa.py -q

Covers the 2026-09-28 corrective pass:
- pdf_check: no font-entry errors on a real matplotlib PDF (Type0/TrueType path),
  fail-closed on a non-PDF file;
- legend-data overlap detection;
- layout-balance detection (outlier-stretched layout);
- 8 pt threshold enforcement producing FAIL.
"""

from __future__ import annotations

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.lines import Line2D

import figure_qa as fq


def test_pdf_check_fonts_both_modes(tmp_path):
    # default rcParams -> Type3 (glyph procedures inline in /CharProcs)
    fig, ax = plt.subplots(figsize=(3, 2))
    ax.plot([0, 1, 2], [0, 1, 0])
    ax.set_xlabel("type3")
    p1 = fq.export_bundle(fig, tmp_path, "t_type3")["pdf"]
    plt.close(fig)
    r1 = fq.pdf_check(p1)
    assert r1.get("status") != "error", r1.get("reason")
    assert r1.get("font_errors") == [], r1.get("font_errors")
    assert r1.get("fonts"), "expected font entries"
    assert all(f.get("embedded") is True for f in r1["fonts"]), r1["fonts"]

    # pdf.fonttype 42 -> TrueType subset with /FontFile2
    with plt.rc_context({"pdf.fonttype": 42}):
        fig, ax = plt.subplots(figsize=(3, 2))
        ax.plot([0, 1, 2], [0, 1, 0])
        ax.set_xlabel("truetype")
        p2 = fq.export_bundle(fig, tmp_path, "t_tt42")["pdf"]
        plt.close(fig)
    r2 = fq.pdf_check(p2)
    assert r2.get("status") != "error", r2.get("reason")
    assert r2.get("font_errors") == [], r2.get("font_errors")
    assert r2.get("fonts"), "expected font entries"
    assert any(f.get("embedded") is True for f in r2["fonts"]), r2["fonts"]


def test_pdf_check_fail_closed_on_bad_file(tmp_path):
    bad = tmp_path / "bad.pdf"
    bad.write_bytes(b"this is not a pdf")
    res = fq.pdf_check(bad)
    assert res.get("status") == "error" and res.get("reason")


def test_run_gate_fails_on_pdf_error(tmp_path, monkeypatch):
    fig, ax = plt.subplots(figsize=(3, 2))
    ax.plot([0, 1], [0, 1])
    monkeypatch.setattr(fq, "pdf_check", lambda p: {"status": "error", "reason": "synthetic"})
    rep = fq.run_gate(fig, tmp_path, "t_pdf_fail")
    plt.close(fig)
    assert rep["status"] == "FAIL"
    assert any("pdf font check failed" in m for m in rep["fails"])


def test_legend_data_overlap_detected():
    fig, ax = plt.subplots(figsize=(3, 3))
    rng = np.random.default_rng(0)
    x = rng.uniform(0, 10, 400)
    y = rng.uniform(0, 10, 400)
    ax.scatter(x, y)
    ax.legend([Line2D([], [], marker="o", ls="")], ["pts"], loc="upper right")
    hits = fq.legend_conflicts(fig)
    plt.close(fig)
    assert hits, "expected legend-data conflict"


def test_legend_data_no_false_positive_on_empty_corner():
    fig, ax = plt.subplots(figsize=(3, 3))
    ax.scatter([0.1, 0.2, 0.3], [0.1, 0.2, 0.3])
    ax.legend([Line2D([], [], marker="o", ls="")], ["pts"], loc="upper right")
    hits = fq.legend_conflicts(fig)
    plt.close(fig)
    assert hits == []


def test_balance_flags_outlier_stretched_layout():
    fig, ax = plt.subplots(figsize=(4, 4))
    rng = np.random.default_rng(1)
    x = np.concatenate([rng.normal(0, 0.5, 200), [10.0, -10.0]])
    y = np.concatenate([rng.normal(0, 0.5, 200), [10.0, -10.0]])
    ax.scatter(x, y)
    issues = fq.balance_issues(fig)
    plt.close(fig)
    assert issues, "expected balance issue"


def test_run_gate_enforces_8pt_default(tmp_path):
    with plt.rc_context({"font.size": 6, "axes.labelsize": 6, "xtick.labelsize": 6, "ytick.labelsize": 6}):
        fig, ax = plt.subplots(figsize=(3, 2))
        ax.plot([0, 1], [0, 1])
        ax.set_xlabel("small")
        ax.set_xticks([0, 1])
        ax.set_xticklabels(["0", "1"])
        rep = fq.run_gate(fig, tmp_path, "t_8pt")
    plt.close("all")
    assert rep["status"] == "FAIL"
    assert any("fontsize" in m for m in rep["fails"])
    assert rep["threshold_source"] == "default-SCI-8pt"
