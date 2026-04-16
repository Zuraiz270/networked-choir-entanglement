---
title: "SocialCompass Tools — Four-Instrument Suite"
type: concept
alchemy_stage: citrinitas
tags: [socialcompass, symbiont, sc-chat-analyzer, perceptiface, beecome, honest-signals, ffi, measurement]
ingested_date: 2026-04-16
source_count: 4
related: ["[[Team_Profile]]", "[[seminar_signup]]", "[[chapter_14_presentation]]", "[[Peter_Gloor]]", "[[Project_Overview]]", "[[presentation_deliverables]]"]
---

# SocialCompass Tools — Four-Instrument Suite

The **SocialCompass** suite is the measurement apparatus at the core of the COINs seminar. Four tools capture different modalities of individual and team behavior, all grounded in the **honest signals** framework — they measure non-self-reported signals that reveal underlying states the person may not consciously produce or control.

This Citrinitas page synthesizes how the four tools relate to each other, what they agree on, and where they structurally diverge.

---

## The Four Tools

| Tool | What it measures | Input | Output |
|:---|:---|:---|:---|
| **Symbiont Analyzer** | Collaboration archetype from actual language used | WhatsApp group chat export (.txt) | Archetype label (Bee/Ant/Butterfly/Capybara/Leech) + % breakdown + top word patterns |
| **SC Chat Analyzer** | Communication role in social network; who initiates, who responds | WhatsApp group chat export (.txt) | Network role (Star/Supporter/Observer/Loner) · avg response latency · network graph |
| **Perceptiface** | Dominant facial emotion + FFI Big Five personality from micro-expressions | Smartphone front camera while watching video | Dominant emotion label · FFI personality profile |
| **Beecome** | FFI Big Five personality from behavioral game choices | Smartphone swipe-left/right story game | FFI Big Five profile derived from decision patterns |

---

## Alchemical Mapping (Chapter 14 Framework)

Per [[chapter_14_presentation]] Slide 12, each tool corresponds to an alchemical stage:

| Stage | Tool Operation |
|:---|:---|
| **Nigredo** | Raw signal collection (chat export, video capture, swipe data) |
| **Albedo** | Feature extraction (word patterns, network metrics, spectrogram of facial micro-movements) |
| **Citrinitas** | Model training (archetype classification, FFI prediction) |
| **Rubedo** | Human interpretation — does the label fit? Where do I agree or push back? |

---

## What the Tools Agree On (Convergence)

From the cohort-wide data in [[seminar_signup]]:

- **Symbiont + SC Chat**: Both measure communication patterns from the same WhatsApp data. High Ant% in SC Chat often co-occurs with Capybara Symbiont label — because Ant (executor, process-follower) and Capybara (harmonizer, low-conflict) are behaviorally compatible.
- **SC Chat network position**: Almost universally **Tree Hugger** across the cohort regardless of Symbiont archetype. This suggests Tree Hugger is the dominant structural role in WhatsApp-based team chats, not a team-specific finding.
- **Beecome FFI**: High Agreeableness + Conscientiousness is the modal result across the cohort — consistent with a self-selected seminar group of conscientious students.

---

## Where the Tools Diverge (The Key Insight)

**Perceptiface vs. Beecome/Chat** — systematic divergence:

- Perceptiface reads **momentary emotional state** (micro-expressions during a brief video stimulus).
- Beecome reads **stable behavioral disposition** (accumulated decision pattern in a 10-minute game).
- Chat/Symbiont reads **habitual communication style** (weeks of actual group chat behavior).

**Result**: The face captures the moment. The chat and game capture the person. These are not contradictory — they are measuring different temporal scales of the same signal.

**Tree Huggers case**: Sad (Zuraiz) / Neutral (Hammad) / Happy (Hassan) on Perceptiface co-exist with Ant-type communication patterns in SC Chat. This is structurally expected, not an anomaly.

**Cohort-scale evidence** (per [[presentation_deliverables]] slide-16 script): Sad and Neutral dominate Perceptiface **across the entire ~25-student cohort**, including students who describe themselves as emotionally stable. This upgrades the context-artifact reading from hypothesis to **cited claim**: the result is measuring the recording context (webcam novelty, tool stress), not the person.

---

## The Capybara Puzzle

A striking cohort-wide finding from [[seminar_signup]]: the **dominant Symbiont archetype is Capybara** (harmonizer) across nearly all students, institutions, and chapter teams. Cohort testimony from [[presentation_deliverables]] (Q2 fallback):

> "Everyone is always a Capybara." — **Sarah Löhnert**
> Same observation corroborated by **Michael Sova**.

The Tree Huggers' own input was a WhatsApp chat spanning **>1 year** of group-study / exam-prep / project collaboration — not a short artificial sample. The archetype still came out Capybara-dominant, matching the cohort pattern.

This raises three questions:

1. Is Capybara the natural self-selection attractor for students who join a COINs seminar?
2. Does WhatsApp group chat structurally reward Capybara-type language (low-friction, agreement-affirming) — i.e., is the tool measuring the **platform**, not the person?
3. What does it mean for a seminar on Swarm Creativity that most participants are harmonizers rather than Bees (coordinators) or Butterflies (networkers)?

The long-sample evidence from the Tree Huggers team pushes toward hypothesis #2 — a platform-artifact reading.

---

## Disagreements Between Tool Pairs (Structural)

| Comparison | Nature of divergence | Chapter 14 explanation |
|:---|:---|:---|
| Perceptiface emotion vs. Beecome FFI | Face = momentary state; Beecome = behavioral trait. Context effects (Zoom fatigue, test novelty) affect face; game choices are more deliberate. | Tools measure different temporal windows; divergence is expected. |
| Symbiont archetype vs. SC Chat role | Symbiont uses word categories; SC Chat uses network position and latency. A Capybara (harmonizer by language) can be a Star (central network node) or Observer (peripheral). | The pipeline matters: same data (chat), different feature extraction = different output. |
| Self-report vs. any tool | Students frequently surprised by results (see cohort quotes in [[seminar_signup]]). | Core argument of honest signals: the body and behavior reveal what the mind edits out. |

---

## Open Questions

- Are the four tools validated independently in peer-reviewed literature, or are they Gloor's proprietary instruments? (Affects how strongly claims can be made in Q&A.)
- Does the Perceptiface FFI prediction (Big Five from face) have published accuracy benchmarks?
- Could the Capybara dominance in Symbiont be an artifact of academic WhatsApp chat style (formal, agreement-seeking) rather than true personality?
