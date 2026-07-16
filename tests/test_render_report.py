"""Tests for the final-report PDF renderer."""

from __future__ import annotations

from pathlib import Path

from pypdf import PdfReader
from scripts.render_report import render_report


def test_render_report_creates_readable_pdf(tmp_path: Path) -> None:
    source = tmp_path / "report.md"
    source.write_text(
        "# Test Report\n\n"
        "**Authors:** A. Researcher\n\n"
        "## Abstract\n\n"
        "This report verifies the rendering pipeline.\n\n"
        "## 1. Results\n\n"
        "The result is reproducible.\n",
        encoding="utf-8",
    )
    output = tmp_path / "report.pdf"

    render_report(source, output)

    reader = PdfReader(output)
    text = "\n".join(page.extract_text() or "" for page in reader.pages)
    assert output.stat().st_size > 1_000
    assert "Test Report" in text
    assert "The result is reproducible." in text
