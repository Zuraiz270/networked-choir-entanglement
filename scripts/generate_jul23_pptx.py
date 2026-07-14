"""Generate output/jul23_final_presentation.pptx from Jul-23 deck content.

Content source: jul23_deck.md (every number traces to a committed CSV; see the
HTML comments there). Layout follows the shared Studio Acoustic helpers.

Run from the project root:
    uv run python scripts/generate_jul23_pptx.py
"""

from __future__ import annotations

import sys
from pathlib import Path

from pptx import Presentation
from pptx.enum.text import PP_ALIGN
from pptx.util import Inches

ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from scripts.generate_jun11_pptx import (  # noqa: E402
    CREAM,
    FIG_DIR,
    GOLD_SOFT,
    IVORY,
    MARGIN,
    MIST,
    MUTED,
    SLIDE_H,
    SLIDE_W,
    TEAL,
    TEAL_DARK,
    _card,
    _kicker,
    _picture_fit,
    _solid_bg,
    _stat_card,
    _takeaway,
    _text,
    _title,
)

OUT_PATH = Path("output/jul23_final_presentation.pptx")
TOTAL_SLIDES = 15


def _content_slide(prs: Presentation, n: int, kicker: str, title: str):
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    _solid_bg(slide, CREAM)
    _kicker(slide, kicker)
    _title(slide, title)
    _text(slide, SLIDE_W - Inches(1.7), SLIDE_H - Inches(0.38),
          Inches(1.2), Inches(0.3), f"{n} / {TOTAL_SLIDES}", size=10, color=MUTED,
          align=PP_ALIGN.RIGHT)
    _text(slide, MARGIN, SLIDE_H - Inches(0.38), Inches(5.0), Inches(0.3),
          "Project 8 - Entanglement in Online Choir", size=10, color=MUTED)
    return slide


def s1_title(prs: Presentation) -> None:
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    _solid_bg(slide, TEAL_DARK)
    _text(slide, MARGIN, Inches(1.55), SLIDE_W - 2 * MARGIN, Inches(0.9),
          "Final Presentation", size=48, bold=True, color=IVORY, align=PP_ALIGN.CENTER)
    _text(slide, MARGIN, Inches(2.65), SLIDE_W - 2 * MARGIN, Inches(0.7),
          "Project 8: Entanglement in Online Choir", size=26, color=GOLD_SOFT,
          align=PP_ALIGN.CENTER)
    _text(slide, MARGIN, Inches(3.75), SLIDE_W - 2 * MARGIN, Inches(0.45),
          "SNA-OSN-M Summer 2026  -  Uni Bamberg x Uni Koeln x HSLU",
          size=15, color=MIST, align=PP_ALIGN.CENTER)
    _text(slide, MARGIN, Inches(4.65), SLIDE_W - 2 * MARGIN, Inches(0.4),
          "Team: Zuraiz - Hammad Anwar - Hassan Ahmed - Kumaran Vasu",
          size=16, bold=True, color=IVORY, align=PP_ALIGN.CENTER)
    _text(slide, MARGIN, Inches(5.35), SLIDE_W - 2 * MARGIN, Inches(0.4),
          "Supervisors: Prof. Janine Hacker - Prof. Peter Gloor",
          size=13, color=MIST, align=PP_ALIGN.CENTER)
    _text(slide, MARGIN, Inches(6.25), SLIDE_W - 2 * MARGIN, Inches(0.4),
          "2026-07-23", size=14, color=GOLD_SOFT, align=PP_ALIGN.CENTER)


def s2_question(prs: Presentation) -> None:
    slide = _content_slide(prs, 2, "Question", "The network is part of the instrument")
    _text(slide, MARGIN, Inches(1.45), SLIDE_W - 2 * MARGIN, Inches(0.6),
          "We measured what latency does to choir togetherness, with one score over time: E(t).",
          size=19, bold=True, color=TEAL)
    rows = [
        ("H1", "Higher latency reduces coordination. Metric: zero-lag onset synchrony; "
               "predicted to fall."),
        ("H2", "Influence networks show leadership structure. Metric: out-degree Gini vs a "
               "matched random null; predicted above null."),
        ("H3", "Visual body signals add information beyond audio. Metric: first visual-onset "
               "coupling; the full test needs paired data."),
    ]
    y = Inches(2.35)
    for title, body in rows:
        _card(slide, MARGIN, y, SLIDE_W - 2 * MARGIN, Inches(0.95), title, [body], size=13.5)
        y += Inches(1.1)
    _takeaway(slide, "Three testable claims, each with a metric and a direction fixed in advance.")


def s3_data(prs: Presentation) -> None:
    slide = _content_slide(prs, 3, "Data", "Three tiers, one honest constraint")
    rows = [
        ("Tier 1 - video", "29 YouTube virtual-choir videos, 18 pose-usable. "
                           "Visual signals: sway and breathing gestures."),
        ("Tier 2 - multitrack", "Dagstuhl (5 pieces), ESMUC (3), ChoralSynth (20, synthetic). "
                                "Per-singer audio and influence networks."),
        ("Tier 3 - injection", "Controlled latency injection on Tier 2: ground-truth "
                               "latency variation, each piece its own control."),
    ]
    y = Inches(1.5)
    for title, body in rows:
        _card(slide, MARGIN, y, SLIDE_W - 2 * MARGIN, Inches(0.95), title, [body], size=13.5)
        y += Inches(1.1)
    _text(slide, MARGIN, Inches(5.0), SLIDE_W - 2 * MARGIN, Inches(1.2),
          "The constraint: no piece has audio, video, and network signals together. "
          "Tier 2 has audio without video; Tier 1 has video without per-singer audio. "
          "Every claim respects that boundary.",
          size=15, bold=True, color=TEAL)
    _takeaway(slide, "Two real corpora, one synthetic control, one visual corpus, "
                     "each used for what it is good for.")


def s4_method(prs: Presentation) -> None:
    slide = _content_slide(prs, 4, "Method", "E(t) and the latency grid")
    _text(slide, MARGIN, Inches(1.4), SLIDE_W - 2 * MARGIN, Inches(0.5),
          "Each clean piece is degraded through five regimes; every metric is recomputed "
          "per piece and regime.",
          size=15, bold=True, color=TEAL)
    regimes = [
        ("clean", "0 ms - 0 ms - 0%"),
        ("in-person", "25 ms - 10 ms - 0%"),
        ("Jamulus LAN", "47 ms - 46 ms - 1%"),
        ("Jamulus WAN", "83 ms - 57 ms - 3%"),
        ("Zoom-class", "150 ms - 80 ms - 8%"),
    ]
    x = MARGIN
    card_w = Inches(2.32)
    for name, vals in regimes:
        _stat_card(slide, x, Inches(2.1), card_w, Inches(1.35), name, vals, number_size=16)
        x += card_w + Inches(0.12)
    _text(slide, MARGIN, Inches(3.7), SLIDE_W - 2 * MARGIN, Inches(0.35),
          "Regime columns: delay - jitter SD - dropout.", size=12, color=MUTED)
    _card(slide, MARGIN, Inches(4.25), SLIDE_W - 2 * MARGIN, Inches(1.85),
          "Statistical floor",
          [
              "Every coordination number is tested against a circular-shift null that "
              "preserves each stream's own autocorrelation.",
              "Final grid: 2000 shuffles per cell, rerun as 140 SLURM array tasks on the "
              "NHR@FAU cluster (2026-07-14).",
          ], size=13.5)
    _takeaway(slide, "Known ground truth by construction, paired within piece, "
                     "with a defensible null.")


def s5_repro(prs: Presentation) -> None:
    slide = _content_slide(prs, 5, "Method", "The pipeline is reproducible")
    rows = [
        ("One command", "`make reproduce` regenerates the headline results from committed "
                        "data summaries."),
        ("44 tests", "Audio, video, network, latency, entanglement, and the H3 experiment "
                     "run in the automated suite."),
        ("Cluster protocol", "The 2000-shuffle grid ran as 140 SLURM array tasks; the "
                             "submission script is committed and cluster-validated."),
        ("Audit trail", "Every deck number traces to a committed CSV."),
    ]
    y = Inches(1.5)
    for title, body in rows:
        _card(slide, MARGIN, y, SLIDE_W - 2 * MARGIN, Inches(0.98), title, [body], size=13.5)
        y += Inches(1.13)
    _takeaway(slide, "The numbers can be regenerated without us in the room.")


def s6_h1(prs: Presentation) -> None:
    slide = _content_slide(prs, 6, "Result", "H1: latency breaks timing, not loudness")
    stats = [
        ("-56.5%", "Dagstuhl (real)"),
        ("-65.1%", "ESMUC (real)"),
        ("-75.1%", "ChoralSynth (synthetic)"),
        ("-70.7%", "Corpus, 28 pieces"),
    ]
    x = MARGIN
    for number, label in stats:
        _stat_card(slide, x, Inches(1.5), Inches(2.9), Inches(1.3), number, label)
        x += Inches(3.05)
    _picture_fit(slide, FIG_DIR / "tier3_corpus_summary.png",
                 MARGIN, Inches(3.05), SLIDE_W - 2 * MARGIN, Inches(3.4))
    _takeaway(slide, "Onset synchrony collapses clean to Zoom-class; envelope coupling "
                     "stays flat (Dagstuhl -0.4%).")


def s7_dissociation(prs: Presentation) -> None:
    slide = _content_slide(prs, 7, "Result", "Why the dissociation is the finding")
    rows = [
        ("The null we kept", "Constant delay + envelope coupling showed no effect; the "
                             "control caught the confound (envelope coupling is lag-tolerant)."),
        ("The a-priori fix", "Zero-lag onset synchrony is the physical quantity jitter should "
                             "break. It recovered the effect in every piece."),
        ("The claim", "Timing collapses while loudness holds. An envelope-only study would "
                      "have called latency harmless."),
        ("Replication", "Two real corpora and one independent synthetic corpus agree."),
    ]
    y = Inches(1.5)
    for title, body in rows:
        _card(slide, MARGIN, y, SLIDE_W - 2 * MARGIN, Inches(0.98), title, [body], size=13.5)
        y += Inches(1.13)
    _takeaway(slide, "The method audit trail is part of the result.")


def s8_h2(prs: Presentation) -> None:
    slide = _content_slide(prs, 8, "Result", "H2: weak but real leadership structure")
    _text(slide, MARGIN, Inches(1.4), SLIDE_W - 2 * MARGIN, Inches(0.65),
          "Leader dominance = Gini of out-degree in the Granger influence graph "
          "(0 democratic, 1 single driver), vs 1000 density-matched random graphs.",
          size=14, bold=True, color=TEAL)
    stats = [
        ("0.154", "Observed corpus mean"),
        ("0.138", "Matched random null"),
        ("3/5 - 2/3", "Dagstuhl - ESMUC significant"),
        ("2/20", "ChoralSynth (chance)"),
    ]
    x = MARGIN
    for number, label in stats:
        _stat_card(slide, x, Inches(2.25), Inches(2.9), Inches(1.3), number, label,
                   number_size=26)
        x += Inches(3.05)
    _picture_fit(slide, FIG_DIR / "wp3_flagship_LI_QuartetA_Take02_standard.png",
                 MARGIN, Inches(3.8), SLIDE_W - 2 * MARGIN, Inches(2.65))
    _takeaway(slide, "Leadership appears in human choirs, not synthetic renderings: a human "
                     "coordination signal, not an artifact.")


def s9_h3(prs: Presentation) -> None:
    slide = _content_slide(prs, 9, "Result", "H3: an honest null, and what it teaches")
    stats = [
        ("17 / 18", "videos analyzable (one silent window)"),
        ("1 / 17", "significant at p < 0.05 = chance"),
        ("0.068", "median max-lag r"),
    ]
    x = MARGIN
    for number, label in stats:
        _stat_card(slide, x, Inches(1.5), Inches(3.95), Inches(1.3), number, label,
                   number_size=26)
        x += Inches(4.1)
    _picture_fit(slide, FIG_DIR / "h3_visual_onset.png",
                 MARGIN, Inches(3.0), Inches(7.4), Inches(3.45))
    _text(slide, Inches(8.2), Inches(3.1), Inches(4.5), Inches(3.2),
          "The estimator recovers known lags on synthetic coupled signals (tested in CI), "
          "so the null is informative: ensemble motion of one tracked stream does not "
          "couple to a mixed audio envelope. H3's full test still needs per-singer "
          "audio + video together.",
          size=13.5, color=TEAL)
    _takeaway(slide, "We ran the promised experiment, it said no, and we report that.")


def s10_demo(prs: Presentation) -> None:
    slide = _content_slide(prs, 10, "Demo", "Live: E(t) on real recordings (60 seconds)")
    rows = [
        ("1. Audio/network piece", "Dagstuhl quartet: E(t) timeline updating with the "
                                   "influence graph."),
        ("2. Video/pose piece", "Tier-1 video playback with the live pose overlay."),
        ("Honesty layer", "The metadata panel shows which signals each piece really has; "
                          "no piece pretends to have all three."),
    ]
    y = Inches(1.6)
    for title, body in rows:
        _card(slide, MARGIN, y, SLIDE_W - 2 * MARGIN, Inches(1.05), title, [body], size=14)
        y += Inches(1.2)
    _takeaway(slide, "Real committed data, running locally, no mock content.")


def s11_fallback(prs: Presentation) -> None:
    slide = _content_slide(prs, 11, "Demo", "Fallback: dashboard on real outputs")
    _picture_fit(slide, FIG_DIR / "wp4_dashboard_realdata.png",
                 MARGIN, Inches(1.5), SLIDE_W - 2 * MARGIN, Inches(4.9))
    _takeaway(slide, "Backup frame in case the live demo cannot run; same content, one frame.")


def s12_limits(prs: Presentation) -> None:
    slide = _content_slide(prs, 12, "Limits", "Limitations, stated plainly")
    rows = [
        ("Simulated latency", "Injection models transmission, not live behavioural "
                              "adaptation of singers."),
        ("Signal split", "No piece carries audio + video + network together; full E(t) has "
                         "never run with all three channels."),
        ("H3 window", "Pose covers one tracked stream over each video's first minute."),
        ("Null caveats", "A minority of individual grid cells are not significant; "
                         "corpus-level trends carry the claims."),
        ("Domain transfer", "The entanglement formula was validated on email networks; this "
                            "is its first music-domain test."),
    ]
    y = Inches(1.45)
    for title, body in rows:
        _card(slide, MARGIN, y, SLIDE_W - 2 * MARGIN, Inches(0.86), title, [body], size=12.5)
        y += Inches(0.99)
    _takeaway(slide, "Registered, owned, and either mitigated or explicitly left as "
                     "future work.")


def s13_contributions(prs: Presentation) -> None:
    slide = _content_slide(prs, 13, "Close", "Contributions")
    rows = [
        ("Latency signature", "Timing collapses 56 to 75 percent while loudness holds, "
                              "28 pieces, three corpora, 2000-shuffle null."),
        ("Leadership measure", "An operational metric that separates human from synthetic "
                               "choir networks."),
        ("Visual requirement", "The first visual-onset experiment, honestly null: the "
                               "paired-corpus requirement is demonstrated, not assumed."),
        ("Open pipeline", "One command, 44 tests, cluster-validated protocol, every claim "
                          "traceable to a committed artifact."),
    ]
    y = Inches(1.5)
    for title, body in rows:
        _card(slide, MARGIN, y, SLIDE_W - 2 * MARGIN, Inches(0.98), title, [body], size=13.5)
        y += Inches(1.13)
    _takeaway(slide, "Supported, partially supported, honestly null, and all reproducible.")


def s14_close(prs: Presentation) -> None:
    slide = _content_slide(prs, 14, "Next", "What comes next, and thanks")
    rows = [
        ("Real latency sessions", "Record live latency-varied sessions: the only way to test "
                                  "H1 without simulation and H2's latency form."),
        ("Paired corpus", "A small per-singer audio + video corpus unlocks the H3 test."),
        ("Report", "Final seminar report due Jul 31; draft v1 complete since Jun 30."),
    ]
    y = Inches(1.6)
    for title, body in rows:
        _card(slide, MARGIN, y, SLIDE_W - 2 * MARGIN, Inches(1.0), title, [body], size=14)
        y += Inches(1.15)
    _text(slide, MARGIN, Inches(5.35), SLIDE_W - 2 * MARGIN, Inches(0.6),
          "Thank you. Questions welcome.", size=22, bold=True, color=TEAL,
          align=PP_ALIGN.CENTER)


def s15_backup(prs: Presentation) -> None:
    slide = _content_slide(prs, 15, "Backup", "Reproducibility protocol")
    rows = [
        ("Regenerate", "`make reproduce` rebuilds summary results from committed artifacts."),
        ("Grid protocol", "`scripts/hpc/tier3_2000.sbatch`: 140 array tasks (28 pieces x 5 "
                          "levels), merged and completeness-checked by "
                          "`scripts/tier3_merge_shards.py`."),
        ("H3 experiment", "`uv run python -m scripts.h3_visual_onset` (deterministic seeds)."),
        ("Environment", "Python 3.11.9 pinned, locked dependencies, `uv sync --extra all`."),
    ]
    y = Inches(1.5)
    for title, body in rows:
        _card(slide, MARGIN, y, SLIDE_W - 2 * MARGIN, Inches(0.98), title, [body], size=13.5)
        y += Inches(1.13)


def build() -> None:
    prs = Presentation()
    prs.slide_width = SLIDE_W
    prs.slide_height = SLIDE_H
    for builder in (
        s1_title, s2_question, s3_data, s4_method, s5_repro, s6_h1, s7_dissociation,
        s8_h2, s9_h3, s10_demo, s11_fallback, s12_limits, s13_contributions,
        s14_close, s15_backup,
    ):
        builder(prs)
    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    prs.save(OUT_PATH)
    print(f"Wrote {OUT_PATH} ({len(prs.slides)} slides)")


if __name__ == "__main__":
    build()
