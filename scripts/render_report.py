"""Render the final Markdown seminar report as a paginated A4 PDF.

Usage:
    uv run python -m scripts.render_report
    uv run python -m scripts.render_report report_final.md output/pdf/final_report.pdf
"""

from __future__ import annotations

import argparse
import html
import re
from collections.abc import Callable, Sequence
from pathlib import Path
from typing import Any

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY, TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import cm
from reportlab.platypus import (
    BaseDocTemplate,
    Flowable,
    Frame,
    Image,
    KeepTogether,
    ListFlowable,
    ListItem,
    PageBreak,
    PageTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
)

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_SOURCE = ROOT / "report_final.md"
DEFAULT_OUTPUT = ROOT / "output/pdf/networked_choir_final_report.pdf"

_IMAGE_RE = re.compile(r"^!\[(?P<caption>.*)]\((?P<path>[^)]+)\)$")
_LINK_RE = re.compile(r"\[([^]]+)]\(([^)]+)\)")
_CODE_RE = re.compile(r"`([^`]+)`")
_BOLD_RE = re.compile(r"\*\*([^*]+)\*\*")
_ITALIC_RE = re.compile(r"(?<!\*)\*([^*]+)\*(?!\*)")
_META_PREFIXES = ("**Authors:**", "**Course:**", "**Supervisors:**", "**Date:**", "**Keywords:**")


def _styles() -> dict[str, ParagraphStyle]:
    base = getSampleStyleSheet()
    return {
        "title": ParagraphStyle(
            "ReportTitle",
            parent=base["Title"],
            fontName="Times-Bold",
            fontSize=20,
            leading=24,
            alignment=TA_CENTER,
            textColor=colors.HexColor("#0B4F5C"),
            spaceAfter=16,
        ),
        "meta": ParagraphStyle(
            "ReportMeta",
            parent=base["Normal"],
            fontName="Times-Roman",
            fontSize=10,
            leading=14,
            alignment=TA_CENTER,
            spaceAfter=6,
        ),
        "h1": ParagraphStyle(
            "Heading1",
            parent=base["Heading1"],
            fontName="Times-Bold",
            fontSize=14,
            leading=17,
            textColor=colors.HexColor("#0B4F5C"),
            spaceBefore=13,
            spaceAfter=7,
            keepWithNext=True,
        ),
        "h2": ParagraphStyle(
            "Heading2",
            parent=base["Heading2"],
            fontName="Times-Bold",
            fontSize=11.5,
            leading=14,
            textColor=colors.HexColor("#0B4F5C"),
            spaceBefore=10,
            spaceAfter=5,
            keepWithNext=True,
        ),
        "body": ParagraphStyle(
            "Body",
            parent=base["BodyText"],
            fontName="Times-Roman",
            fontSize=9.5,
            leading=12.5,
            alignment=TA_JUSTIFY,
            spaceAfter=6,
            splitLongWords=True,
        ),
        "bullet": ParagraphStyle(
            "Bullet",
            parent=base["BodyText"],
            fontName="Times-Roman",
            fontSize=9.5,
            leading=12.5,
            leftIndent=0,
            firstLineIndent=0,
            spaceAfter=3,
        ),
        "caption": ParagraphStyle(
            "Caption",
            parent=base["BodyText"],
            fontName="Times-Italic",
            fontSize=8.5,
            leading=10.5,
            alignment=TA_CENTER,
            textColor=colors.HexColor("#444444"),
            spaceBefore=4,
            spaceAfter=9,
        ),
        "table": ParagraphStyle(
            "TableCell",
            parent=base["BodyText"],
            fontName="Times-Roman",
            fontSize=7.2,
            leading=8.7,
            alignment=TA_LEFT,
        ),
    }


def _inline(text: str) -> str:
    escaped = html.escape(text, quote=False)
    escaped = _LINK_RE.sub(r'<link href="\2">\1</link>', escaped)
    escaped = _CODE_RE.sub(r'<font name="Courier">\1</font>', escaped)
    escaped = _BOLD_RE.sub(r"<b>\1</b>", escaped)
    return _ITALIC_RE.sub(r"<i>\1</i>", escaped)


def _is_special(line: str) -> bool:
    stripped = line.strip()
    return bool(
        not stripped
        or stripped.startswith("#")
        or stripped.startswith("|")
        or stripped.startswith("- ")
        or re.match(r"^\d+\.\s", stripped)
        or _IMAGE_RE.match(stripped)
        or stripped == "---"
        or stripped == "<!-- pagebreak -->"
    )


def _image_flowables(source: Path, line: str, styles: dict[str, ParagraphStyle]) -> list[Flowable]:
    match = _IMAGE_RE.match(line.strip())
    if match is None:
        return []
    image_path = (source.parent / match.group("path")).resolve()
    if not image_path.exists():
        raise FileNotFoundError(f"report image not found: {image_path}")
    image = Image(str(image_path))
    max_width, max_height = 16.2 * cm, 9.2 * cm
    scale = min(max_width / image.imageWidth, max_height / image.imageHeight, 1.0)
    image.drawWidth = image.imageWidth * scale
    image.drawHeight = image.imageHeight * scale
    caption = Paragraph(_inline(match.group("caption")), styles["caption"])
    return [KeepTogether([image, caption])]


def _table_flowable(lines: Sequence[str], styles: dict[str, ParagraphStyle]) -> Table:
    rows = [[cell.strip() for cell in line.strip().strip("|").split("|")] for line in lines]
    if len(rows) > 1 and all(set(cell) <= {":", "-"} for cell in rows[1]):
        rows.pop(1)
    formatted = [[Paragraph(_inline(cell), styles["table"]) for cell in row] for row in rows]
    column_count = max(len(row) for row in formatted)
    for row in formatted:
        row.extend(Paragraph("", styles["table"]) for _ in range(column_count - len(row)))
    table = Table(formatted, colWidths=[16.4 * cm / column_count] * column_count, repeatRows=1)
    table.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#DDEBED")),
                ("TEXTCOLOR", (0, 0), (-1, 0), colors.HexColor("#0B4F5C")),
                ("FONTNAME", (0, 0), (-1, 0), "Times-Bold"),
                ("GRID", (0, 0), (-1, -1), 0.35, colors.HexColor("#A9BEC2")),
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("LEFTPADDING", (0, 0), (-1, -1), 4),
                ("RIGHTPADDING", (0, 0), (-1, -1), 4),
                ("TOPPADDING", (0, 0), (-1, -1), 3),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 3),
            ]
        )
    )
    return table


def _list_flowable(
    items: Sequence[str], ordered: bool, styles: dict[str, ParagraphStyle]
) -> ListFlowable:
    children = [
        ListItem(Paragraph(_inline(item), styles["bullet"]), leftIndent=12) for item in items
    ]
    return ListFlowable(
        children,
        bulletType="1" if ordered else "bullet",
        start="1",
        leftIndent=18,
        bulletFontName="Times-Roman",
        bulletFontSize=9,
        spaceAfter=6,
    )


def _parse_markdown(source: Path, styles: dict[str, ParagraphStyle]) -> list[Flowable]:
    lines = source.read_text(encoding="utf-8").splitlines()
    story: list[Flowable] = []
    i = 0
    saw_title = False
    while i < len(lines):
        line = lines[i].strip()
        if not line or line == "---":
            i += 1
            continue
        if line == "<!-- pagebreak -->":
            story.append(PageBreak())
            i += 1
            continue
        if line.startswith("# "):
            story.extend([Spacer(1, 1.8 * cm), Paragraph(_inline(line[2:]), styles["title"])])
            saw_title = True
            i += 1
            continue
        if line.startswith("## "):
            story.append(Paragraph(_inline(line[3:]), styles["h1"]))
            i += 1
            continue
        if line.startswith("### "):
            story.append(Paragraph(_inline(line[4:]), styles["h2"]))
            i += 1
            continue
        image_items = _image_flowables(source, line, styles)
        if image_items:
            story.extend(image_items)
            i += 1
            continue
        if line.startswith("|"):
            table_lines: list[str] = []
            while i < len(lines) and lines[i].strip().startswith("|"):
                table_lines.append(lines[i])
                i += 1
            story.extend([_table_flowable(table_lines, styles), Spacer(1, 7)])
            continue
        if line.startswith("- "):
            items: list[str] = []
            while i < len(lines) and lines[i].strip().startswith("- "):
                items.append(lines[i].strip()[2:])
                i += 1
            story.append(_list_flowable(items, False, styles))
            continue
        if re.match(r"^\d+\.\s", line):
            items = []
            while i < len(lines) and re.match(r"^\d+\.\s", lines[i].strip()):
                items.append(re.sub(r"^\d+\.\s+", "", lines[i].strip()))
                i += 1
            story.append(_list_flowable(items, True, styles))
            continue
        paragraph_lines = [line]
        i += 1
        while i < len(lines) and not _is_special(lines[i]):
            paragraph_lines.append(lines[i].strip())
            i += 1
        style = styles["meta"] if saw_title and line.startswith(_META_PREFIXES) else styles["body"]
        story.append(Paragraph(_inline(" ".join(paragraph_lines)), style))
    return story


def _page_callback(title: str) -> Callable[[Any, Any], None]:
    def draw(canvas: Any, doc: Any) -> None:
        canvas.saveState()
        canvas.setStrokeColor(colors.HexColor("#B7CBCD"))
        canvas.setLineWidth(0.4)
        canvas.line(2.1 * cm, A4[1] - 1.45 * cm, A4[0] - 2.1 * cm, A4[1] - 1.45 * cm)
        canvas.setFont("Times-Roman", 8)
        canvas.setFillColor(colors.HexColor("#555555"))
        canvas.drawString(2.1 * cm, A4[1] - 1.18 * cm, title[:80])
        canvas.drawRightString(A4[0] - 2.1 * cm, 1.15 * cm, f"Page {doc.page}")
        canvas.restoreState()

    return draw


def render_report(source: Path, output: Path) -> None:
    """Render ``source`` to ``output`` and fail on missing figures."""
    source = source.resolve()
    output = output.resolve()
    output.parent.mkdir(parents=True, exist_ok=True)
    styles = _styles()
    first_line = source.read_text(encoding="utf-8").splitlines()[0]
    title = first_line.removeprefix("# ").strip()
    doc = BaseDocTemplate(
        str(output),
        pagesize=A4,
        leftMargin=2.1 * cm,
        rightMargin=2.1 * cm,
        topMargin=1.8 * cm,
        bottomMargin=1.8 * cm,
        title=title,
        author="Zuraiz, Hammad Anwar, Hassan Ahmed, Kumaran Vasu",
    )
    frame = Frame(doc.leftMargin, doc.bottomMargin, doc.width, doc.height, id="main")
    doc.addPageTemplates(PageTemplate(id="report", frames=[frame], onPage=_page_callback(title)))
    doc.build(_parse_markdown(source, styles))


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source", nargs="?", type=Path, default=DEFAULT_SOURCE)
    parser.add_argument("output", nargs="?", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    render_report(args.source, args.output)
    print(f"Wrote {args.output}")


if __name__ == "__main__":
    main()
