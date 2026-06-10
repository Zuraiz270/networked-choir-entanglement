"""Generate output/jun11_status_meeting_iv.pptx from the jun11_deck.md content.

Hardcoded slide content for reproducibility. Visual style reuses the
"Studio Acoustic" palette from generate_apr30_pptx.py (deep teal + warm gold)
so the deck reads as part of the same project family.

Run from the project root:
    uv run python scripts/generate_jun11_pptx.py
"""

from __future__ import annotations

from pathlib import Path

from pptx import Presentation
from pptx.dml.color import RGBColor
from pptx.enum.text import MSO_ANCHOR, PP_ALIGN
from pptx.util import Inches, Pt

ROOT = Path(__file__).resolve().parent.parent
OUT_PATH = ROOT / "output" / "jun11_status_meeting_iv.pptx"
FIG_DIR = ROOT / "data" / "figures"

# --- Studio Acoustic palette (mirrors apr30 deck) ---
TEAL = RGBColor(0x0E, 0x4D, 0x5E)
TEAL_DARK = RGBColor(0x07, 0x33, 0x40)
TEAL_MID = RGBColor(0x32, 0x80, 0x95)
GOLD = RGBColor(0xC4, 0x90, 0x2A)
GOLD_SOFT = RGBColor(0xE6, 0xC6, 0x70)
CREAM = RGBColor(0xFA, 0xF6, 0xEC)
IVORY = RGBColor(0xFD, 0xFB, 0xF5)
CHARCOAL = RGBColor(0x24, 0x26, 0x2E)
MUTED = RGBColor(0x6E, 0x6A, 0x60)
MIST = RGBColor(0xCB, 0xD9, 0xDD)
GREEN = RGBColor(0x4F, 0x8E, 0x5A)

SLIDE_W = Inches(13.333)
SLIDE_H = Inches(7.5)
MARGIN = Inches(0.55)
TITLE_TOP = Inches(0.45)
ACCENT_Y = Inches(1.05)
CONTENT_TOP = Inches(1.25)


def _solid_bg(slide, color: RGBColor) -> None:
    fill = slide.background.fill
    fill.solid()
    fill.fore_color.rgb = color


def _add_textbox(
    slide,
    left,
    top,
    width,
    height,
    *,
    text: str,
    font_size: int = 18,
    bold: bool = False,
    color: RGBColor = CHARCOAL,
    align=PP_ALIGN.LEFT,
    font_name: str = "Calibri",
) -> None:
    tb = slide.shapes.add_textbox(left, top, width, height)
    tf = tb.text_frame
    tf.word_wrap = True
    tf.margin_left = Inches(0.05)
    tf.margin_right = Inches(0.05)
    tf.margin_top = Inches(0.05)
    tf.margin_bottom = Inches(0.05)
    p = tf.paragraphs[0]
    p.alignment = align
    run = p.add_run()
    run.text = text
    run.font.size = Pt(font_size)
    run.font.bold = bold
    run.font.color.rgb = color
    run.font.name = font_name


def _add_bullets(
    slide,
    left,
    top,
    width,
    height,
    bullets: list[str],
    *,
    font_size: int = 18,
    color: RGBColor = CHARCOAL,
    bullet_char: str = "•",
) -> None:
    tb = slide.shapes.add_textbox(left, top, width, height)
    tf = tb.text_frame
    tf.word_wrap = True
    tf.margin_left = Inches(0.05)
    for i, text in enumerate(bullets):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.alignment = PP_ALIGN.LEFT
        run = p.add_run()
        run.text = f"{bullet_char}  {text}"
        run.font.size = Pt(font_size)
        run.font.color.rgb = color
        run.font.name = "Calibri"
        p.space_after = Pt(8)


def _add_title_bar(slide, title: str) -> None:
    _add_textbox(
        slide,
        MARGIN,
        TITLE_TOP,
        SLIDE_W - 2 * MARGIN,
        Inches(0.6),
        text=title,
        font_size=28,
        bold=True,
        color=TEAL,
    )
    accent = slide.shapes.add_connector(1, MARGIN, ACCENT_Y, MARGIN + Inches(1.5), ACCENT_Y)
    accent.line.color.rgb = GOLD
    accent.line.width = Pt(2.5)


def _new_content_slide(prs):
    slide = prs.slides.add_slide(prs.slide_layouts[6])  # blank
    _solid_bg(slide, CREAM)
    return slide


def _new_dark_slide(prs):
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    _solid_bg(slide, TEAL_DARK)
    return slide


# ---------- Slide builders ----------


def slide_1_title(prs) -> None:
    slide = _new_dark_slide(prs)
    _add_textbox(
        slide, MARGIN, Inches(1.6), SLIDE_W - 2 * MARGIN, Inches(0.9),
        text="Status Meeting IV", font_size=46, bold=True, color=IVORY, align=PP_ALIGN.CENTER,
    )
    _add_textbox(
        slide, MARGIN, Inches(2.7), SLIDE_W - 2 * MARGIN, Inches(0.8),
        text="Project 8: Entanglement in Online Choir", font_size=28, color=GOLD_SOFT,
        align=PP_ALIGN.CENTER,
    )
    _add_textbox(
        slide, MARGIN, Inches(3.7), SLIDE_W - 2 * MARGIN, Inches(0.5),
        text="SNA-OSN-M Summer 2026   ·   Uni Bamberg × Uni Köln × HSLU",
        font_size=16, color=MIST, align=PP_ALIGN.CENTER,
    )
    _add_textbox(
        slide, MARGIN, Inches(5.0), SLIDE_W - 2 * MARGIN, Inches(0.5),
        text="Presented by Hassan Ahmed", font_size=18, color=IVORY, align=PP_ALIGN.CENTER, bold=True,
    )
    _add_textbox(
        slide, MARGIN, Inches(5.5), SLIDE_W - 2 * MARGIN, Inches(0.4),
        text="on behalf of the team",
        font_size=14, color=MIST, align=PP_ALIGN.CENTER,
    )
    _add_textbox(
        slide, MARGIN, Inches(6.5), SLIDE_W - 2 * MARGIN, Inches(0.4),
        text="2026-06-11   ·   14:00 CET", font_size=14, color=GOLD_SOFT, align=PP_ALIGN.CENTER,
    )


def slide_2_plan_recap(prs) -> None:
    slide = _new_content_slide(prs)
    _add_title_bar(slide, "What we said we'd do,Sprint 3 plan recap")
    _add_textbox(
        slide, MARGIN, Inches(1.5), SLIDE_W - 2 * MARGIN, Inches(0.5),
        text="Six deliverables. Four core, two pull-forward stretch. All six shipped.",
        font_size=16, color=MUTED,
    )

    rows = [
        ("Deliverable", "Brief target", "Status"),
        ("WP1 audio on all Dagstuhl pieces", "Jun 4", "✓ done May 22"),
        ("WP2 pose on 10 Tier-1 videos", "Jun 11", "✓ done May 22"),
        ("WP3 Granger + COP-GC on 5 pieces", "Jun 11", "✓ done May 22"),
        ("WP4 dashboard scaffold", "Jun 11", "✓ done May 22"),
        ("E(t) end-to-end + null (stretch)", "Jun 14", "✓ done May 22 (23 days early)"),
        ("WP3 full-corpus metrics (stretch)", "Jun 14", "✓ done May 22 (23 days early)"),
    ]
    rows_table = slide.shapes.add_table(
        len(rows), 3, MARGIN, Inches(2.2), SLIDE_W - 2 * MARGIN, Inches(4.5)
    ).table
    rows_table.columns[0].width = Inches(6.5)
    rows_table.columns[1].width = Inches(2.5)
    rows_table.columns[2].width = Inches(3.0)
    for r, row_data in enumerate(rows):
        for c, text in enumerate(row_data):
            cell = rows_table.cell(r, c)
            cell.text = text
            cell.fill.solid()
            cell.fill.fore_color.rgb = TEAL if r == 0 else (CREAM if r % 2 else IVORY)
            for para in cell.text_frame.paragraphs:
                for run in para.runs:
                    run.font.size = Pt(14)
                    run.font.bold = r == 0
                    run.font.color.rgb = IVORY if r == 0 else CHARCOAL
                    run.font.name = "Calibri"


def slide_3_headline(prs) -> None:
    slide = _new_content_slide(prs)
    _add_title_bar(slide, "Headline,E(t) works, 5/5 pieces beat null at p < 0.001")
    _add_textbox(
        slide, MARGIN, Inches(1.5), Inches(7.6), Inches(0.5),
        text="The Entanglement Index is operational end-to-end.",
        font_size=18, bold=True, color=GREEN,
    )

    fig = FIG_DIR / "et_corpus_comparison.png"
    if fig.exists():
        slide.shapes.add_picture(
            str(fig), MARGIN, Inches(2.1), height=Inches(4.6)
        )
    # right column commentary
    right_left = Inches(8.5)
    right_width = Inches(4.3)
    _add_bullets(
        slide, right_left, Inches(2.1), right_width, Inches(4.7),
        bullets=[
            "All 5 Dagstuhl WP3 pieces tested.",
            "200-shuffle circular-shift null per piece.",
            "Observed mean E(t): 0.57 to 0.80.",
            "Null mean: 0.48 to 0.61.",
            "Every piece > null by >17 σ.",
            "Pattern splits by piece, not size:",
            "   LI 0.74-0.80, TP 0.57-0.68.",
        ],
        font_size=14,
    )


def slide_4_wp1(prs) -> None:
    slide = _new_content_slide(prs)
    _add_title_bar(slide, "WP1 audio scale,25 Dagstuhl musical takes")
    _add_bullets(
        slide, MARGIN, Inches(1.5), Inches(7.0), Inches(5.5),
        bullets=[
            "Sprint 2: 1 piece (LI Quartet A Take 02).",
            "Sprint 3: all 25 musical takes across Locus Iste + Tu Pauper Es.",
            "130 newly extracted singer parquets, 288 pairwise couplings.",
            "Total runtime: 78 minutes.",
            "Pipeline resumable; prefers DYN > HSM > LRX mic per singer.",
            "Pattern matches musical structure:",
            "   Within-section (LI Basses): 0.78–0.87",
            "   Full-choir polyphonic (TP): 0.40–0.53",
        ],
        font_size=15,
    )
    fig = FIG_DIR / "wp1_satb_coupling.png"
    if fig.exists():
        slide.shapes.add_picture(
            str(fig), Inches(8.0), Inches(1.6), width=Inches(4.8)
        )


def slide_5_wp3(prs) -> None:
    slide = _new_content_slide(prs)
    _add_title_bar(slide, "WP3 influence graph + COP-GC,Hacker flagship v2")
    fig = FIG_DIR / "wp3_influence_graphs_5pieces.png"
    if fig.exists():
        slide.shapes.add_picture(
            str(fig), MARGIN, Inches(1.5), width=Inches(8.0)
        )
    _add_bullets(
        slide, Inches(8.8), Inches(1.5), Inches(4.0), Inches(5.5),
        bullets=[
            "5 pieces × 2 methods.",
            "Standard Granger + COP-GC (Zanin 2021).",
            "Sprint-2 reference reproduces:",
            "   11/12 edges, density 0.917, S leads.",
            "Method divergence,TP_FullChoir:",
            "   Standard: 42/56 edges significant",
            "   COP-GC:   25/56 edges significant",
            "Both methods carried forward.",
        ],
        font_size=13,
    )


def slide_6_wp2(prs) -> None:
    slide = _new_content_slide(prs)
    _add_title_bar(slide, "WP2 pose on 10 Tier-1 videos,5/10 pass detection floor")
    _add_bullets(
        slide, MARGIN, Inches(1.5), Inches(6.5), Inches(5.5),
        bullets=[
            "Sprint 2: 1 video. Sprint 3: 10, stratified by NMP regime.",
            "Total runtime: 2.3 minutes.",
            "5/10 pass 50% detection: ZKthfLPWBCQ 98.5%, Z-cH7j5iB3k 94.0%,",
            "   ouFyQKszE_Y 79.5%, w0ywMP8mOc4 78.2%, VsnvueTan4I 66.7%.",
            "5/10 fail: software-UI captures or dense low-res tile grids",
            "   (no body for MediaPipe to find).",
            "Matches Status Meeting III \"try and iterate\" decision.",
            "5 passing videos define WP2 inclusion set for H1.",
        ],
        font_size=14,
    )
    fig = FIG_DIR / "wp2_visual_features_v2.png"
    if fig.exists():
        slide.shapes.add_picture(
            str(fig), Inches(7.5), Inches(2.5), width=Inches(5.4)
        )


def slide_7_wp4_et(prs) -> None:
    slide = _new_content_slide(prs)
    _add_title_bar(slide, "WP4 dashboard scaffold + E(t) integration")
    fig = FIG_DIR / "wp4_dashboard_scaffold.png"
    if fig.exists():
        slide.shapes.add_picture(
            str(fig), MARGIN, Inches(1.5), height=Inches(5.0)
        )
    _add_bullets(
        slide, Inches(7.0), Inches(1.5), Inches(5.8), Inches(5.5),
        bullets=[
            "Dashboard: React 18 + Vite 5 + TS strict + D3 + Plotly.",
            "Backend: FastAPI 0.111, 3 mock endpoints.",
            "4 panels render end-to-end (Playwright-verified).",
            "Real-data wiring is the WP4 sub-plan (Jun 21).",
            "",
            "E(t) integration module:",
            "   compute_entanglement() with NaN-safe weight reallocation.",
            "   200-shuffle circular-shift null at composite level.",
            "   Tests: 23/23 pass.",
        ],
        font_size=13,
    )


def slide_8_sprint4(prs) -> None:
    slide = _new_content_slide(prs)
    _add_title_bar(slide, "Sprint 4 plan,Jun 12 to Jun 25")
    rows = [
        ("Track", "Sprint 4 work", "Due"),
        ("WP1 audio", "Per-window Granger → time-varying N(t)", "Jun 21"),
        ("WP2 video", "Pose on remaining 21 Tier-1 videos (triage)", "Jun 30"),
        ("WP3 network", "Tier-3 latency injection: jitter on Dagstuhl audio", "Jun 21"),
        ("WP4 dashboard", "Swap mock JSON → real parquet readers + pose overlay", "Jun 21"),
    ]
    t = slide.shapes.add_table(
        len(rows), 3, MARGIN, Inches(1.8), SLIDE_W - 2 * MARGIN, Inches(3.5)
    ).table
    t.columns[0].width = Inches(2.5)
    t.columns[1].width = Inches(7.5)
    t.columns[2].width = Inches(2.0)
    for r, row_data in enumerate(rows):
        for c, text in enumerate(row_data):
            cell = t.cell(r, c)
            cell.text = text
            cell.fill.solid()
            cell.fill.fore_color.rgb = TEAL if r == 0 else (CREAM if r % 2 else IVORY)
            for para in cell.text_frame.paragraphs:
                for run in para.runs:
                    run.font.size = Pt(14)
                    run.font.bold = r == 0
                    run.font.color.rgb = IVORY if r == 0 else CHARCOAL
                    run.font.name = "Calibri"
    _add_textbox(
        slide, MARGIN, Inches(5.7), SLIDE_W - 2 * MARGIN, Inches(0.5),
        text="Hard milestone: dashboard alpha runs on real data by Jun 21.",
        font_size=18, bold=True, color=GOLD,
    )


def slide_9_retro(prs) -> None:
    slide = _new_content_slide(prs)
    _add_title_bar(slide, "Retrospective and four honest limitations")
    _add_textbox(
        slide, MARGIN, Inches(1.5), Inches(6.2), Inches(0.5),
        text="What worked", font_size=18, bold=True, color=GREEN,
    )
    _add_bullets(
        slide, MARGIN, Inches(2.0), Inches(6.2), Inches(2.5),
        bullets=[
            "6/6 Sprint-3 deliverables shipped.",
            "2 stretch items 23 days early.",
            "Doc-update discipline kept brief + guide + vault in sync after every phase.",
        ],
        font_size=14,
    )
    _add_textbox(
        slide, MARGIN, Inches(4.5), Inches(6.2), Inches(0.5),
        text="What slipped", font_size=18, bold=True, color=GOLD,
    )
    _add_bullets(
        slide, MARGIN, Inches(5.0), Inches(6.2), Inches(2.0),
        bullets=[
            "ESMUC + ChoralSynth not acquired (proprietary / gate slipped May 15).",
            "To be revisited in Sprint 4 if licensing path opens.",
        ],
        font_size=14,
    )
    # Right column: limitations
    right_left = Inches(7.0)
    _add_textbox(
        slide, right_left, Inches(1.5), Inches(5.8), Inches(0.5),
        text="Four honest limitations", font_size=18, bold=True, color=TEAL,
    )
    _add_bullets(
        slide, right_left, Inches(2.0), Inches(5.8), Inches(5.0),
        bullets=[
            "V(t) is NaN across all current E(t) (Dagstuhl is audio-only).",
            "WP3 corpus is all Dagstuhl studio,no NMP-regime variation yet.",
            "WP2 detection is 50%,the 5/10 pass rate defines our inclusion set.",
            "p_null reports as 0.0000,correct read is \"p < 1/200\", not literal zero.",
        ],
        font_size=14,
    )


def slide_10_questions(prs) -> None:
    slide = _new_content_slide(prs)
    _add_title_bar(slide, "Open questions for the room")
    _add_textbox(
        slide, MARGIN, Inches(1.7), SLIDE_W - 2 * MARGIN, Inches(0.5),
        text="Three questions before we open the floor.",
        font_size=18, color=MUTED,
    )
    _add_bullets(
        slide, MARGIN, Inches(2.5), SLIDE_W - 2 * MARGIN, Inches(4.5),
        bullets=[
            "To Prof. Hacker,do you have access to ESMUC or ChoralSynth multitrack data we could fold into Tier-2 before Sprint 4 acquisition?",
            "To Prof. Gloor,for the final paper figure, matplotlib-clean or Gephi/Cytoscape SVG-polished for the alchemical-stage diagram?",
            "To everyone,is the Jul 23 final presentation in-person at Bamberg or remote? Affects how Hassan and Hammad coordinate travel.",
        ],
        font_size=18,
    )
    _add_textbox(
        slide, MARGIN, Inches(6.5), SLIDE_W - 2 * MARGIN, Inches(0.5),
        text="Thank you. Questions.",
        font_size=24, bold=True, color=TEAL, align=PP_ALIGN.CENTER,
    )


def build() -> None:
    prs = Presentation()
    prs.slide_width = SLIDE_W
    prs.slide_height = SLIDE_H

    slide_1_title(prs)
    slide_2_plan_recap(prs)
    slide_3_headline(prs)
    slide_4_wp1(prs)
    slide_5_wp3(prs)
    slide_6_wp2(prs)
    slide_7_wp4_et(prs)
    slide_8_sprint4(prs)
    slide_9_retro(prs)
    slide_10_questions(prs)

    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    prs.save(OUT_PATH)
    print(f"Wrote {OUT_PATH}")
    print(f"  Slides: {len(prs.slides)}")
    print(f"  Size: {OUT_PATH.stat().st_size / 1024:.1f} KB")


if __name__ == "__main__":
    build()
