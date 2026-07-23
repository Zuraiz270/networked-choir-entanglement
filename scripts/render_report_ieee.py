"""Render the final report as a separate IEEE-style two-column PDF.

This layout follows the visual conventions of IEEE conference papers. It is not
an IEEE Xplore compliance claim: formal submission still requires the official
conference template and PDF eXpress validation.

Official guidance:
    https://conferences.ieeeauthorcenter.ieee.org/write-your-paper/authoring-tools-and-templates/
    https://events.ieee.org/planning-basics/ieee-conference-publications/publishing-information-for-ieee-conference-authors/

Usage:
    uv run python -m scripts.render_report_ieee
"""

from __future__ import annotations

import argparse
import re
from collections.abc import Sequence
from pathlib import Path
from typing import Any

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY, TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import cm
from reportlab.platypus import (
    BalancedColumns,
    BaseDocTemplate,
    Flowable,
    Frame,
    Image,
    ListFlowable,
    ListItem,
    PageTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
)
from scripts.render_report import _IMAGE_RE, _inline, _is_special

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_SOURCE = ROOT / "report_final.md"
DEFAULT_OUTPUT = ROOT / "output/pdf/networked_choir_final_report_ieee.pdf"
_COLUMN_WIDTH = 8.2 * cm

_META_PREFIXES = {
    "Authors": "**Authors:**",
    "Course": "**Course:**",
    "Supervisors": "**Supervisors:**",
    "Date": "**Date:**",
    "Keywords": "**Keywords:**",
}
_TABLE_TITLES = (
    "Project hypotheses and final status",
    "Data corpora and analysis roles",
    "Entanglement components",
    "Controlled latency regimes",
    "H1 paired results",
    "H2 centralization results",
    "Result provenance",
    "Evidence trail",
)


def _styles() -> dict[str, ParagraphStyle]:
    base = getSampleStyleSheet()
    return {
        "title": ParagraphStyle(
            "IeeeTitle",
            parent=base["Title"],
            fontName="Times-Bold",
            fontSize=21,
            leading=23,
            alignment=TA_CENTER,
            spaceAfter=9,
        ),
        "authors": ParagraphStyle(
            "IeeeAuthors",
            parent=base["Normal"],
            fontName="Times-Roman",
            fontSize=11,
            leading=13,
            alignment=TA_CENTER,
            spaceAfter=4,
        ),
        "affiliation": ParagraphStyle(
            "IeeeAffiliation",
            parent=base["Normal"],
            fontName="Times-Roman",
            fontSize=8.5,
            leading=10.5,
            alignment=TA_CENTER,
            spaceAfter=2,
        ),
        "abstract": ParagraphStyle(
            "IeeeAbstract",
            parent=base["BodyText"],
            fontName="Times-Roman",
            fontSize=8.5,
            leading=10.2,
            alignment=TA_JUSTIFY,
            leftIndent=0.75 * cm,
            rightIndent=0.75 * cm,
            spaceAfter=4,
        ),
        "index": ParagraphStyle(
            "IeeeIndexTerms",
            parent=base["BodyText"],
            fontName="Times-Roman",
            fontSize=8.5,
            leading=10.2,
            alignment=TA_JUSTIFY,
            leftIndent=0.75 * cm,
            rightIndent=0.75 * cm,
            spaceAfter=9,
        ),
        "h1": ParagraphStyle(
            "IeeeHeading1",
            parent=base["Heading1"],
            fontName="Times-Roman",
            fontSize=10,
            leading=12,
            alignment=TA_CENTER,
            spaceBefore=7,
            spaceAfter=4,
            keepWithNext=True,
        ),
        "h2": ParagraphStyle(
            "IeeeHeading2",
            parent=base["Heading2"],
            fontName="Times-Italic",
            fontSize=9.5,
            leading=11.3,
            alignment=TA_LEFT,
            spaceBefore=5,
            spaceAfter=3,
            keepWithNext=True,
        ),
        "body": ParagraphStyle(
            "IeeeBody",
            parent=base["BodyText"],
            fontName="Times-Roman",
            fontSize=9.2,
            leading=10.8,
            alignment=TA_JUSTIFY,
            firstLineIndent=0.35 * cm,
            spaceAfter=2.2,
            splitLongWords=True,
        ),
        "bullet": ParagraphStyle(
            "IeeeBullet",
            parent=base["BodyText"],
            fontName="Times-Roman",
            fontSize=9.2,
            leading=10.8,
            alignment=TA_LEFT,
            spaceAfter=1.5,
        ),
        "caption": ParagraphStyle(
            "IeeeCaption",
            parent=base["BodyText"],
            fontName="Times-Roman",
            fontSize=8,
            leading=9.4,
            alignment=TA_CENTER,
            spaceBefore=3,
            spaceAfter=7,
        ),
        "table_caption": ParagraphStyle(
            "IeeeTableCaption",
            parent=base["BodyText"],
            fontName="Times-Roman",
            fontSize=7.8,
            leading=9,
            alignment=TA_CENTER,
            spaceBefore=5,
            spaceAfter=3,
            keepWithNext=True,
        ),
        "table": ParagraphStyle(
            "IeeeTableCell",
            parent=base["BodyText"],
            fontName="Times-Roman",
            fontSize=7.1,
            leading=8.3,
            alignment=TA_LEFT,
            splitLongWords=True,
        ),
    }


def _roman(number: int) -> str:
    values = (
        (1000, "M"),
        (900, "CM"),
        (500, "D"),
        (400, "CD"),
        (100, "C"),
        (90, "XC"),
        (50, "L"),
        (40, "XL"),
        (10, "X"),
        (9, "IX"),
        (5, "V"),
        (4, "IV"),
        (1, "I"),
    )
    result: list[str] = []
    remaining = number
    for value, symbol in values:
        while remaining >= value:
            result.append(symbol)
            remaining -= value
    return "".join(result)


def _front_matter(lines: Sequence[str]) -> tuple[str, dict[str, str], str, list[str]]:
    title = next(
        (line.removeprefix("# ").strip() for line in lines if line.startswith("# ")),
        "Final Report",
    )
    metadata: dict[str, str] = {}
    for label, prefix in _META_PREFIXES.items():
        metadata[label] = next(
            (line.removeprefix(prefix).strip() for line in lines if line.startswith(prefix)), ""
        )

    abstract_index = next(
        (index for index, line in enumerate(lines) if line.strip() == "## Abstract"), None
    )
    if abstract_index is None:
        return title, metadata, "", list(lines)

    body_index = abstract_index + 1
    abstract_parts: list[str] = []
    while body_index < len(lines) and not lines[body_index].strip().startswith("## "):
        if lines[body_index].strip():
            abstract_parts.append(lines[body_index].strip())
        body_index += 1
    return title, metadata, " ".join(abstract_parts), list(lines[body_index:])


class _FigureBlock(Flowable):  # type: ignore[misc]
    """Keep a column-sized image and caption together without frame breaks."""

    def __init__(self, image: Image, caption: Paragraph) -> None:
        super().__init__()
        self.image = image
        self.caption = caption
        self.caption_height = 0.0

    def wrap(self, available_width: float, available_height: float) -> tuple[float, float]:
        if self.image.drawWidth > available_width:
            scale = available_width / self.image.drawWidth
            self.image.drawWidth *= scale
            self.image.drawHeight *= scale
        _, self.caption_height = self.caption.wrap(available_width, available_height)
        self.width = available_width
        self.height = self.image.drawHeight + self.caption_height + 3
        return self.width, self.height

    def draw(self) -> None:
        image_x = (self.width - self.image.drawWidth) / 2
        self.image.drawOn(self.canv, image_x, self.caption_height + 3)
        self.caption.drawOn(self.canv, 0, 0)


def _image_flowable(source: Path, line: str, styles: dict[str, ParagraphStyle]) -> Flowable:
    match = _IMAGE_RE.match(line.strip())
    if match is None:
        raise ValueError(f"invalid report image: {line}")
    image_path = (source.parent / match.group("path")).resolve()
    if not image_path.exists():
        raise FileNotFoundError(f"report image not found: {image_path}")

    image = Image(str(image_path))
    max_width, max_height = _COLUMN_WIDTH, 6.8 * cm
    scale = min(max_width / image.imageWidth, max_height / image.imageHeight, 1.0)
    image.drawWidth = image.imageWidth * scale
    image.drawHeight = image.imageHeight * scale
    caption_text = re.sub(r"^Figure\s+(\d+)\.", r"Fig. \1.", match.group("caption"))
    caption = Paragraph(_inline(caption_text), styles["caption"])
    return _FigureBlock(image, caption)


def _table_flowable(lines: Sequence[str], styles: dict[str, ParagraphStyle]) -> Table:
    rows = [[cell.strip() for cell in line.strip().strip("|").split("|")] for line in lines]
    if len(rows) > 1 and all(set(cell) <= {":", "-"} for cell in rows[1]):
        rows.pop(1)
    formatted = [[Paragraph(_inline(cell), styles["table"]) for cell in row] for row in rows]
    column_count = max(len(row) for row in formatted)
    for row in formatted:
        row.extend(Paragraph("", styles["table"]) for _ in range(column_count - len(row)))

    table = Table(formatted, colWidths=[_COLUMN_WIDTH / column_count] * column_count, repeatRows=1)
    table.setStyle(
        TableStyle(
            [
                ("FONTNAME", (0, 0), (-1, 0), "Times-Bold"),
                ("LINEABOVE", (0, 0), (-1, 0), 0.7, colors.black),
                ("LINEBELOW", (0, 0), (-1, 0), 0.45, colors.black),
                ("LINEBELOW", (0, -1), (-1, -1), 0.7, colors.black),
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("LEFTPADDING", (0, 0), (-1, -1), 3),
                ("RIGHTPADDING", (0, 0), (-1, -1), 3),
                ("TOPPADDING", (0, 0), (-1, -1), 2.5),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 2.5),
            ]
        )
    )
    return table


def _list_flowable(
    items: Sequence[str], ordered: bool, styles: dict[str, ParagraphStyle]
) -> ListFlowable:
    children = [
        ListItem(Paragraph(_inline(item), styles["bullet"]), leftIndent=9) for item in items
    ]
    return ListFlowable(
        children,
        bulletType="1" if ordered else "bullet",
        start="1",
        leftIndent=13,
        bulletFontName="Times-Roman",
        bulletFontSize=8.5,
        spaceAfter=3,
    )


def _main_heading(text: str) -> str:
    if text == "References":
        return "REFERENCES"
    if text.startswith("Appendix "):
        return text.upper()
    match = re.match(r"^(\d+)\.\s*(.+)$", text)
    if match is None:
        return text.upper()
    return f"{_roman(int(match.group(1)))}. {match.group(2).upper()}"


def _subheading(text: str, index: int) -> str:
    title = re.sub(r"^\d+\.\d+\s+", "", text)
    return f"{chr(ord('A') + index)}. {title}"


def _two_columns(flowables: Sequence[Flowable]) -> BalancedColumns:
    return BalancedColumns(
        list(flowables),
        nCols=2,
        needed=2.2 * cm,
        innerPadding=0.46 * cm,
        leftPadding=0,
        rightPadding=0,
        topPadding=0,
        bottomPadding=0,
        spaceAfter=2,
    )


def _parse_body(
    source: Path, lines: Sequence[str], styles: dict[str, ParagraphStyle]
) -> list[Flowable]:
    story: list[Flowable] = []
    column_items: list[Flowable] = []
    table_index = 0
    subsection_index = 0

    def flush_columns() -> None:
        if column_items:
            story.append(_two_columns(column_items))
            column_items.clear()

    i = 0
    while i < len(lines):
        line = lines[i].strip()
        if not line or line == "---" or line == "<!-- pagebreak -->":
            i += 1
            continue
        if line.startswith("## "):
            subsection_index = 0
            column_items.append(Paragraph(_inline(_main_heading(line[3:])), styles["h1"]))
            i += 1
            continue
        if line.startswith("### "):
            column_items.append(
                Paragraph(_inline(_subheading(line[4:], subsection_index)), styles["h2"])
            )
            subsection_index += 1
            i += 1
            continue
        if _IMAGE_RE.match(line):
            column_items.append(_image_flowable(source, line, styles))
            i += 1
            continue
        if line.startswith("|"):
            table_lines: list[str] = []
            while i < len(lines) and lines[i].strip().startswith("|"):
                table_lines.append(lines[i])
                i += 1
            table_index += 1
            title = (
                _TABLE_TITLES[table_index - 1]
                if table_index <= len(_TABLE_TITLES)
                else f"Report table {table_index}"
            )
            caption = Paragraph(
                f"TABLE {_roman(table_index)}<br/>{_inline(title.upper())}",
                styles["table_caption"],
            )
            column_items.extend([caption, _table_flowable(table_lines, styles), Spacer(1, 5)])
            continue
        if line.startswith("- "):
            items: list[str] = []
            while i < len(lines) and lines[i].strip().startswith("- "):
                items.append(lines[i].strip()[2:])
                i += 1
            column_items.append(_list_flowable(items, False, styles))
            continue
        if re.match(r"^\d+\.\s", line):
            items = []
            while i < len(lines) and re.match(r"^\d+\.\s", lines[i].strip()):
                items.append(re.sub(r"^\d+\.\s+", "", lines[i].strip()))
                i += 1
            column_items.append(_list_flowable(items, True, styles))
            continue

        paragraph_lines = [line]
        i += 1
        while i < len(lines) and not _is_special(lines[i]):
            paragraph_lines.append(lines[i].strip())
            i += 1
        column_items.append(Paragraph(_inline(" ".join(paragraph_lines)), styles["body"]))

    flush_columns()
    return story


def _page_callback(canvas: Any, doc: Any) -> None:
    canvas.saveState()
    canvas.setFont("Times-Roman", 7.5)
    canvas.drawCentredString(A4[0] / 2, 0.78 * cm, str(doc.page))
    canvas.restoreState()


def render_ieee_report(source: Path, output: Path) -> None:
    """Render ``source`` to ``output`` in an IEEE-style two-column layout."""
    source = source.resolve()
    output = output.resolve()
    output.parent.mkdir(parents=True, exist_ok=True)

    lines = source.read_text(encoding="utf-8").splitlines()
    title, metadata, abstract, body_lines = _front_matter(lines)
    styles = _styles()
    story: list[Flowable] = [
        Paragraph(_inline(title), styles["title"]),
        Paragraph(_inline(metadata["Authors"]), styles["authors"]),
        Paragraph(_inline(metadata["Course"]), styles["affiliation"]),
        Paragraph(_inline(metadata["Supervisors"]), styles["affiliation"]),
        Paragraph(_inline(metadata["Date"]), styles["affiliation"]),
        Spacer(1, 6),
        Paragraph(f"<b><i>Abstract</i>-</b> {_inline(abstract)}", styles["abstract"]),
        Paragraph(f"<b><i>Index Terms</i>-</b> {_inline(metadata['Keywords'])}", styles["index"]),
    ]
    story.extend(_parse_body(source, body_lines, styles))

    doc = BaseDocTemplate(
        str(output),
        pagesize=A4,
        leftMargin=1.8 * cm,
        rightMargin=1.8 * cm,
        topMargin=1.55 * cm,
        bottomMargin=1.45 * cm,
        title=title,
        author=metadata["Authors"],
        subject="IEEE-style seminar report",
        keywords=metadata["Keywords"],
    )
    frame = Frame(
        doc.leftMargin,
        doc.bottomMargin,
        doc.width,
        doc.height,
        leftPadding=0,
        rightPadding=0,
        topPadding=0,
        bottomPadding=0,
        id="full-width",
    )
    doc.addPageTemplates(PageTemplate(id="ieee-style", frames=[frame], onPage=_page_callback))
    doc.build(story)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source", nargs="?", type=Path, default=DEFAULT_SOURCE)
    parser.add_argument("output", nargs="?", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    render_ieee_report(args.source, args.output)
    print(f"Wrote {args.output}")


if __name__ == "__main__":
    main()
