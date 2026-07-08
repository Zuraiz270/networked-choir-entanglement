# Jul 9 Status Meeting VI, Speaker Script

**Project 8 - Entanglement in Online Choir - 2026-07-09 - 14:00 CET**

> 9 slides, about 9 minutes spoken. Presenters: Hammad and Zuraiz. Tone: clear, factual, presentation-ready.

---

## Slide 1: Title

Hello, we are Hammad and Zuraiz, presenting Status Meeting Six for Project 8, Entanglement in Online Choir. This is our final status meeting before the Jul 23 final presentation.

## Slide 2: Goals and plan

Before the progress update, I want to restate the project goal because not everyone may remember the full context.

We are measuring how well online choirs coordinate when singers are not in the same room. The main project metric is E(t), which gives one coordination score over time from audio, network, and visual signals.

The three project questions are simple. H1 asks whether higher latency reduces choir coordination. H2 asks whether influence networks show leadership structure. H3 asks whether visual and body signals add information beyond audio. The plan is to use verified datasets, write the final report, and prepare a dashboard demo for the final presentation.

Today I will connect that project goal to the latest results and the final-presentation plan.

## Slide 3: Progress during the last iteration

Since Status Meeting Five, we completed the Jul-9 report checkpoint.

The report draft v1 now writes up the H1 result. H1 is ready to use in the report as the main timing result. H2 has a cleaner interpretation: weak leadership signal in human choir networks. H3 remains open because the needed paired audio-video data is unavailable.

The main shift is that the work moved from finding results to preparing the final presentation and report.

## Slide 4: Report draft v1

The Jul-9 report milestone from the last meeting is met. Report draft v1 is ready for review.

The draft has the full structure: abstract, hypotheses, data, methods, results, limitations, conclusion, and reproducibility appendix. H1 is written as the headline result. H2 is presented as a measured leadership signal in human datasets. H3 is presented as an open data-availability limitation.

This matters because we are not entering the final phase with only code and figures. The project argument is already in prose and can now be reviewed.

## Slide 5: H1 result summary

The H1 result is a timing dissociation. Loudness-envelope coupling stays almost flat under jitter, while onset synchrony falls sharply. So latency does not mainly break how loud singers are together; it breaks when they land note attacks.

Across datasets, from clean to Zoom-class jitter, onset synchrony drops by 57 percent for Dagstuhl, 66 percent for ESMUC, and 76 percent for ChoralSynth. That gives us two independent human datasets plus one synthetic contrast dataset.

The key methodological point is that an envelope-only metric would have missed the latency effect. The timing-sensitive onset channel is necessary.

## Slide 6: H2 result summary

The original H2 asked whether networks become more leader-dominated as latency rises. By leader-dominated, I mean influence is concentrated around one singer or one section, instead of being shared across the choir. Our current design cannot test the latency part cleanly, because injected delay on pre-recorded audio cannot create a real behavioral leader.

The result we can support is this: clean human choir influence networks show weak leadership structure above a density-matched random null. Dagstuhl has 3 of 5 significant pieces, ESMUC has 2 of 3, and ChoralSynth has 2 of 20, approximately chance.

The interpretation is not that choirs are strongly hierarchical. It is that weak leadership appears in real human coordination and is mostly absent in synthetic renderings.

## Slide 7: Dashboard alpha

The dashboard alpha uses real outputs. This screenshot is the current real-data dashboard alpha. I am using it here to discuss the final demo plan, not to claim that this is a new screenshot from the last iteration.

The timeline comes from the real E(t) pipeline, the graph from a real Granger GEXF, the pose overlay from real MediaPipe parquet, and the metadata shows which signals each piece actually carries.

The honest demo structure is two examples. One audio/network example shows E(t) and the influence graph. One video/pose example shows playback and the pose overlay. This is necessary because no current piece has all three signals together.

## Slide 8: Plan for the next iteration

The next iteration is the final presentation and report phase. The plan is to build the 20-minute Jul-23 deck, finish the final report from draft v1, run the final reproducibility checks, and prepare the dashboard for the presentation with a few final demo tests.

The scientific framing should stay consistent: H1 is the main finding, H2 is a partial human-leadership result, and H3 remains open until the required paired audio-video data exists.

## Slide 9: What we need to align before the final presentation

The retrospective output is that the project became stronger because we kept the null results and explained them. The constant-delay result did not support the first metric, and that led to the stronger jitter and onset-timing analysis. Dataset claims now trace to project files and generated outputs.

For the retrospective part, I will explain what we fixed during the project.

The first latency method was replaced after the control check showed it was not strong enough. Dataset selection now uses verified availability, not memory. The dashboard wording is also clearer now: it separates current results from final-demo planning.

For feedback, I want to ask three things. First, what should the final presentation structure be? Second, which part should receive the most attention in the final presentation? Third, because we created the dashboard, is a screenshot enough in the slides, or should we open the dashboard and show it live?

Thank you. I am happy to take questions.

---

## Timing Cheat Sheet

| Slide | Target |
|:--|:--|
| 1 | 0:15 |
| 2 | 0:40 |
| 3 | 0:55 |
| 4 | 1:10 |
| 5 | 1:25 |
| 6 | 1:15 |
| 7 | 1:05 |
| 8 | 0:55 |
| 9 | 1:00 |

Total: about 8:40 before Q&A.
