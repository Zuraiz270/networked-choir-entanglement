"""Tests for the IEEE-style report renderer."""

from __future__ import annotations

import base64
from pathlib import Path

from pypdf import PdfReader
from scripts.render_report_ieee import render_ieee_report


def test_render_ieee_report_creates_two_column_pdf(tmp_path: Path) -> None:
    body = "\n\n".join(
        f"ColumnBodyMarker paragraph {index} verifies the technical-paper layout."
        for index in range(80)
    )
    source = tmp_path / "report.md"
    image_path = tmp_path / "figure.png"
    image_path.write_bytes(
        base64.b64decode(
            "iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mNk"
            "YAAAAAYAAjCB0C8AAAAASUVORK5CYII="
        )
    )
    source.write_text(
        "# Test IEEE Report\n\n"
        "**Authors:** A. Researcher, B. Engineer\n\n"
        "**Course:** Systems Seminar\n\n"
        "**Supervisors:** Prof. Example\n\n"
        "**Date:** 31 July 2026\n\n"
        "**Keywords:** reproducibility, coordination\n\n"
        "## Abstract\n\n"
        "This abstract verifies the IEEE-style rendering pipeline.\n\n"
        "## 1. Introduction\n\n"
        f"{body}\n\n"
        "| Metric | Value |\n"
        "|:--|--:|\n"
        "| Test | 1 |\n\n"
        "![Figure 1. Test figure.](figure.png)\n\n"
        "## References\n\n"
        "1. A. Author, Test Reference, 2026.\n",
        encoding="utf-8",
    )
    output = tmp_path / "report_ieee.pdf"

    render_ieee_report(source, output)

    reader = PdfReader(output, strict=False)
    text = "\n".join(page.extract_text() or "" for page in reader.pages)
    assert output.stat().st_size > 2_000
    assert reader.metadata is not None
    assert reader.metadata.title == "Test IEEE Report"
    assert "Abstract" in text
    assert "Index Terms" in text
    assert "I. INTRODUCTION" in text

    marker_positions: list[float] = []
    table_positions: list[float] = []
    figure_positions: list[float] = []

    def record_marker(
        extracted: str,
        current_matrix: list[float],
        _text_matrix: list[float],
        _font: dict[str, object] | None,
        _font_size: float,
    ) -> None:
        if "ColumnBodyMarker" in extracted:
            marker_positions.append(float(current_matrix[4]))
        if "TABLE I" in extracted:
            table_positions.append(float(current_matrix[4]))
        if "Fig. 1." in extracted:
            figure_positions.append(float(current_matrix[4]))

    for page in reader.pages:
        page.extract_text(visitor_text=record_marker)

    width = float(reader.pages[0].mediabox.width)
    assert any(x < width / 2 for x in marker_positions)
    assert any(x > width / 2 for x in marker_positions)
    assert table_positions and all(x > width / 2 for x in table_positions)
    assert figure_positions and all(x > width / 2 for x in figure_positions)
