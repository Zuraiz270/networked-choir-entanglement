import fs from "node:fs/promises";
import path from "node:path";
import { pathToFileURL } from "node:url";

const ROOT = process.cwd();
const ARTIFACT_BASE =
  "C:/Users/zurai/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/@oai/artifact-tool";

const tool = await import(pathToFileURL(`${ARTIFACT_BASE}/dist/artifact_tool.mjs`).href);
const { Canvas, loadImage } = await import(
  pathToFileURL(`${ARTIFACT_BASE}/node_modules/skia-canvas/lib/index.mjs`).href
);

const {
  Presentation,
  PresentationFile,
  column,
  row,
  grid,
  layers,
  panel,
  text,
  shape,
  rule,
  fill,
  fixed,
  hug,
  wrap,
  grow,
  fr,
  auto,
  drawSlideToCtx,
} = tool;

const OUT_DIR = path.join(ROOT, "output");
const SCRATCH_DIR = path.join(ROOT, "scratch", "apr30_deck");
const PREVIEW_DIR = path.join(SCRATCH_DIR, "previews");
const PPTX_PATH = path.join(OUT_DIR, "apr30_status_meeting_ii.pptx");
const QA_PATH = path.join(SCRATCH_DIR, "qa_report.json");
const MONTAGE_PATH = path.join(SCRATCH_DIR, "preview_montage.png");

await fs.mkdir(OUT_DIR, { recursive: true });
await fs.mkdir(PREVIEW_DIR, { recursive: true });

const W = 1920;
const H = 1080;

const C = {
  ink: "#172026",
  muted: "#52606D",
  quiet: "#7A8793",
  paper: "#F7F9F8",
  white: "#FFFFFF",
  coal: "#151A1E",
  red: "#B63A33",
  teal: "#007C89",
  green: "#2E7D55",
  amber: "#C58A23",
  violet: "#6554C0",
  line: "#D9E0DF",
  softTeal: "#E4F3F2",
  softRed: "#F7E8E6",
  softAmber: "#F8EEDB",
  softViolet: "#ECEAF7",
  softGreen: "#E6F2EB",
};

const font = "Aptos";
const titleFont = "Georgia";

function t(value, options = {}) {
  return text(value, {
    width: options.width ?? fill,
    height: options.height ?? hug,
    name: options.name,
    columnSpan: options.columnSpan,
    rowSpan: options.rowSpan,
    style: {
      fontFace: options.fontFace ?? font,
      fontSize: options.size ?? 26,
      color: options.color ?? C.ink,
      bold: options.bold ?? false,
      italic: options.italic ?? false,
      ...options.style,
    },
  });
}

function label(value, color = C.red) {
  return row({ width: hug, height: hug, gap: 10, align: "center" }, [
    shape({ width: fixed(12), height: fixed(12), geometry: "ellipse", fill: color }),
    t(value.toUpperCase(), {
      width: hug,
      size: 16,
      color: C.quiet,
      bold: true,
      style: { letterSpacing: 0 },
    }),
  ]);
}

function background() {
  return layers({ width: fill, height: fill }, [
    shape({ name: "bg", width: fill, height: fill, fill: C.paper }),
    grid(
      {
        name: "bg-grid",
        width: fill,
        height: fill,
        columns: [fr(1), fr(1), fr(1), fr(1)],
        rows: [fr(1)],
      },
      [
        shape({ width: fill, height: fill, fill: "#FFFFFF" }),
        shape({ width: fill, height: fill, fill: "#F3F7F7" }),
        shape({ width: fill, height: fill, fill: "#FAF9F4" }),
        shape({ width: fill, height: fill, fill: "#F6F8FA" }),
      ],
    ),
  ]);
}

function slideRoot(title, kicker, bodyChildren, options = {}) {
  return layers({ width: fill, height: fill }, [
    background(),
    column(
      {
        name: "slide-root",
        width: fill,
        height: fill,
        padding: { x: 82, y: 60 },
        gap: options.gap ?? 28,
      },
      [
        row({ width: fill, height: fixed(options.headerHeight ?? 136), align: "end", justify: "between" }, [
          column({ width: fill, height: fill, gap: 10, justify: "end" }, [
            label(kicker, options.accent ?? C.red),
            t(title, {
              name: "slide-title",
              size: options.titleSize ?? 52,
              bold: true,
              fontFace: titleFont,
              color: C.ink,
            }),
          ]),
          t(options.slideNo ?? "", {
            width: fixed(72),
            size: 18,
            color: C.quiet,
            style: { textAlign: "right" },
          }),
        ]),
        rule({ name: "title-rule", width: fill, stroke: C.line, weight: 2 }),
        ...bodyChildren,
      ],
    ),
  ]);
}

function chip(textValue, color, fillColor) {
  return panel(
    {
      width: hug,
      height: hug,
      padding: { x: 18, y: 10 },
      fill: fillColor,
      borderRadius: "rounded-full",
    },
    t(textValue, { width: hug, size: 20, bold: true, color }),
  );
}

function fixedChip(textValue, color, fillColor, width = 132) {
  return panel(
    {
      width: fixed(width),
      height: hug,
      padding: { x: 14, y: 10 },
      fill: fillColor,
      borderRadius: "rounded-full",
    },
    t(textValue, { width: fill, size: 20, bold: true, color, style: { textAlign: "center" } }),
  );
}

function smallNote(value, color = C.muted) {
  return t(value, { size: 20, color, width: fill });
}

function coverSignal() {
  const bars = [120, 180, 250, 340, 420, 510, 420, 330, 240, 170, 110];
  return column({ width: fill, height: fill, justify: "center", align: "center", gap: 18 }, [
    row({ width: fill, height: hug, justify: "center", align: "center", gap: 18 }, [
      shape({ width: fixed(64), height: fixed(64), geometry: "ellipse", fill: C.red }),
      shape({ width: fixed(42), height: fixed(42), geometry: "ellipse", fill: C.teal }),
      shape({ width: fixed(86), height: fixed(86), geometry: "ellipse", fill: C.amber }),
      shape({ width: fixed(50), height: fixed(50), geometry: "ellipse", fill: C.violet }),
    ]),
    ...bars.map((w, i) =>
      row({ width: fixed(620), height: fixed(22), align: "center", justify: "center" }, [
        shape({
          name: `wave-${i}`,
          width: fixed(w),
          height: fixed(8),
          fill: i % 3 === 0 ? C.red : i % 3 === 1 ? C.teal : C.amber,
          borderRadius: "rounded-full",
        }),
      ]),
    ),
    t("audio + movement + influence", {
      width: fill,
      size: 22,
      bold: true,
      color: C.muted,
      style: { textAlign: "center" },
    }),
  ]);
}

function addSlide(presentation, node, notes) {
  const slide = presentation.slides.add();
  slide.compose(node, { frame: { left: 0, top: 0, width: W, height: H }, baseUnit: 8 });
  if (notes) slide.speakerNotes.setText(notes);
  return slide;
}

const presentation = Presentation.create({
  slideSize: { width: W, height: H },
});

addSlide(
  presentation,
  layers({ width: fill, height: fill }, [
    background(),
    grid(
      {
        width: fill,
        height: fill,
        columns: [fr(1.05), fr(0.95)],
        rows: [fr(1)],
        columnGap: 50,
        padding: { x: 86, y: 74 },
      },
      [
        column({ width: fill, height: fill, justify: "between", gap: 26 }, [
          column({ width: fill, height: hug, gap: 18 }, [
            label("status meeting ii", C.red),
            t("Entanglement in Online Choir", {
              size: 82,
              bold: true,
              fontFace: titleFont,
              color: C.ink,
            }),
            t("Measuring coordination when singers cannot share the same room", {
              width: wrap(820),
              size: 31,
              color: C.muted,
            }),
          ]),
          column({ width: fill, height: hug, gap: 12 }, [
            row({ width: fill, height: hug, gap: 12 }, [
              chip("Uni Bamberg", C.teal, C.softTeal),
              chip("Uni Köln", C.red, C.softRed),
              chip("HSLU", C.amber, C.softAmber),
            ]),
            t("Presented by Zuraiz, on behalf of the team", { size: 24, color: C.ink }),
            t("Supervisors: Prof. Janine Hacker and Prof. Peter Gloor", {
              size: 21,
              color: C.quiet,
            }),
          ]),
        ]),
        panel(
          {
            width: fill,
            height: fill,
            fill: "#EEF5F4",
            borderRadius: 30,
            padding: 44,
          },
          coverSignal(),
        ),
      ],
    ),
  ]),
  `Good afternoon. Project 8, Entanglement in Online Choir. I am Zuraiz, presenting on behalf of the team. We are four members from Uni Bamberg. Our supervisors are Prof. Hacker on the Bamberg side and Prof. Gloor as COIN seminar lead. Thank you for the meeting slot.`,
);

const members = [
  ["Z", "Zuraiz", "Tree Hugger", "73% Ant", "Ant / Capybara"],
  ["HA", "Hammad Anwar", "Tree Hugger", "64% Ant", "Capybara 49%"],
  ["HS", "Hassan Ahmed", "Tree Hugger", "63% Ant", "Ant 40%"],
  ["K", "Kumaran Vasu", "Tree Hugger", "75% Ant", "Ant 80%"],
];

addSlide(
  presentation,
  slideRoot(
    "Team complete; self-analysis is planned",
    "team",
    [
      grid(
        {
          width: fill,
          height: grow(1),
          columns: [fr(1), fr(1), fr(1), fr(1)],
          columnGap: 22,
        },
        members.map(([initials, name, type, score, sym], i) =>
          panel(
            {
              width: fill,
              height: fill,
              padding: { x: 28, y: 30 },
              fill: C.white,
              borderRadius: 24,
            },
            column({ width: fill, height: fill, gap: 12, align: "start" }, [
              shape({
                width: fixed(92),
                height: fixed(92),
                geometry: "ellipse",
                fill: [C.red, C.teal, C.amber, C.violet][i],
              }),
              t(initials, {
                width: fill,
                size: 25,
                bold: true,
                color: [C.red, C.teal, C.amber, C.violet][i],
                style: { textAlign: "center" },
              }),
              t(name, {
                width: fill,
                size: 28,
                bold: true,
                color: C.ink,
                style: { textAlign: "center" },
              }),
              chip(type, C.green, C.softGreen),
              column({ width: fill, height: hug, gap: 8 }, [
                row({ width: fill, height: fixed(15), gap: 0 }, [
                  shape({
                    width: fixed(Math.max(20, Number.parseInt(score, 10) * 3.2)),
                    height: fixed(15),
                    fill: C.green,
                    borderRadius: "rounded-full",
                  }),
                  shape({ width: fill, height: fixed(15), fill: "#E4E9E8", borderRadius: "rounded-full" }),
                ]),
                t(score, { width: fill, size: 19, bold: true, color: C.green, style: { textAlign: "center" } }),
                t(sym, { width: fill, size: 19, color: C.quiet, style: { textAlign: "center" } }),
              ]),
            ]),
          ),
        ),
      ),
      panel(
        { width: fill, height: hug, padding: { x: 26, y: 18 }, fill: "#F1F5F4", borderRadius: 18 },
        row({ width: fill, height: hug, gap: 18, align: "center" }, [
          shape({ width: fixed(14), height: fixed(48), fill: C.red, borderRadius: "rounded-full" }),
          smallNote(
            "Archetype results are included because the May 21 Virtual Mirror asks us to analyse our own team communication. The scientific contribution today is the choir dataset and measurement strategy.",
          ),
        ]),
      ),
    ],
    { slideNo: "02", accent: C.teal },
  ),
  `Our team has four members, all M.Sc. students at Uni Bamberg. Three of us came from the chapter team; Kumaran joined at project signup. The archetype bars are here because the May 21 Virtual Mirror asks us to analyse our own team communication. For today, the important point is that the team is complete, role allocation is stable, and the self-analysis deliverable is planned.`,
);

addSlide(
  presentation,
  slideRoot(
    "Can we quantify online choir coordination?",
    "goals and scope",
    [
      grid(
        {
          width: fill,
          height: grow(1),
          columns: [fr(1.02), fr(0.98)],
          columnGap: 42,
        },
        [
          column({ width: fill, height: fill, justify: "center", gap: 26 }, [
            t("Research question", { size: 21, color: C.red, bold: true }),
            t("When a choir sings together over the internet, can we put a number on how well coordinated they are?", {
              size: 48,
              bold: true,
              fontFace: titleFont,
              color: C.ink,
            }),
            panel(
              { width: fill, height: hug, padding: 24, fill: C.white, borderRadius: 18 },
              column({ width: fill, height: hug, gap: 10 }, [
                t("Where this comes from", { size: 24, bold: true, color: C.ink }),
                smallNote("NMP studies latency/tool quality. Coordination research studies group flow. Choirs give an objective acoustic outcome."),
                smallNote("E(t) adapts Gloor's entanglement idea and Pentland's Honest Signals to choir audio/video; H1-H3 validate the adaptation."),
              ]),
            ),
          ]),
          column({ width: fill, height: fill, gap: 18 }, [
            panel(
              { width: fill, height: hug, padding: 26, fill: "#152225", borderRadius: 24 },
              column({ width: fill, height: hug, gap: 18 }, [
                t("E(t)", { width: fill, size: 56, bold: true, color: C.white, style: { textAlign: "center" } }),
                row({ width: fill, height: hug, justify: "center", gap: 12 }, [
                  chip("A(t) audio", C.teal, "#DDF1EF"),
                  chip("V(t) visual", C.amber, "#F5E8CF"),
                  chip("N(t) network", C.red, "#F4DED9"),
                ]),
                t("A proposed coordination index, not a pre-validated music metric.", {
                  size: 22,
                  color: "#D6E0DF",
                  style: { textAlign: "center" },
                }),
              ]),
            ),
            ...[
              ["H1", "Low-latency tools score higher on E(t) than Zoom-class tools.", C.teal],
              ["H2", "Influence network shifts from democratic to leader-dominated.", C.red],
              ["H3", "Body movement adds measurable explanatory power beyond audio.", C.amber],
            ].map(([h, body, color]) =>
              panel(
                { width: fill, height: hug, padding: { x: 22, y: 18 }, fill: C.white, borderRadius: 18 },
                row({ width: fill, height: hug, gap: 14, align: "center" }, [
                  shape({ width: fixed(10), height: fixed(54), fill: color, borderRadius: "rounded-full" }),
                  t(h, { width: fixed(48), size: 24, bold: true, color }),
                  t(body, { width: fill, size: 24, bold: true, color: C.ink }),
                ]),
              ),
            ),
          ]),
        ],
      ),
    ],
    { slideNo: "03", accent: C.red, titleSize: 50 },
  ),
  `Our research question is simple. When a choir sings together over the internet, can we put a number on how well coordinated they are? This question comes from a gap between two literatures. We are building a proposed number for that: E(t), the Entanglement Index. The formula is not copied directly from an online-choir paper; it is a domain adaptation inspired by Gloor's entanglement work and Pentland's Honest Signals. H1, H2, and H3 are the validation tests.`,
);

const tiers = [
  {
    tier: "Tier 0",
    title: "Seed URLs",
    what: "5 Jamulus / Choir@Home URLs from Prof. Hacker",
    action: "Guide search terms and inclusion rules",
    proves: "Starts the corpus search",
    color: C.quiet,
    fill: "#EEF2F2",
  },
  {
    tier: "Tier 1",
    title: "YouTube virtual choirs",
    what: "20-30 public videos, curated by May 15",
    action: "Pose, mouth movement, visible synchrony, ensemble audio",
    proves: "Visual coordination / H3 sanity check",
    color: C.teal,
    fill: C.softTeal,
  },
  {
    tier: "Tier 2",
    title: "Academic multitrack",
    what: "Dagstuhl ChoirSet, ESMUC, ChoralSynth",
    action: "Separate singer tracks for pitch, onsets, Granger influence",
    proves: "A(t), N(t), directed graph",
    color: C.amber,
    fill: C.softAmber,
  },
  {
    tier: "Tier 3",
    title: "Latency injection",
    what: "Artificial Zoom-class / low-latency versions of Tier 2",
    action: "Add delay, jitter, packet loss, recompute E(t)",
    proves: "Clean H1 test",
    color: C.red,
    fill: C.softRed,
  },
];

function tierPanel(item) {
  return panel(
    { width: fill, height: hug, padding: { x: 22, y: 18 }, fill: C.white, borderRadius: 18 },
    grid(
      {
        width: fill,
        height: hug,
        columns: [fixed(170), fr(1.05), fr(1.2), fr(0.85)],
        columnGap: 16,
        alignItems: "center",
      },
      [
        column({ name: `tier-label-${item.tier}`, width: fill, height: fixed(88), gap: 8 }, [
          shape({ width: fixed(54), height: fixed(8), fill: item.color, borderRadius: "rounded-full" }),
          t(item.tier, { size: 22, bold: true, color: item.color }),
          t(item.title, { size: 18, color: C.muted }),
        ]),
        t(item.what, { size: 20, color: C.ink, bold: true }),
        t(item.action, { size: 19, color: C.muted }),
        t(item.proves, { size: 19, color: C.ink, bold: true }),
      ],
    ),
  );
}

addSlide(
  presentation,
  slideRoot(
    "Four levels, four different jobs",
    "dataset strategy",
    [
      row({ width: fill, height: hug, gap: 14, align: "center" }, [
        chip("Tier 1: real-world but messy", C.teal, C.softTeal),
        chip("Tier 2: clean but academic", C.amber, C.softAmber),
        chip("Tier 3: controlled and experimental", C.red, C.softRed),
      ]),
      column({ width: fill, height: grow(1), gap: 8 }, tiers.map(tierPanel)),
      panel(
        { width: fill, height: hug, padding: { x: 24, y: 16 }, fill: "#172026", borderRadius: 18 },
        row({ width: fill, height: hug, gap: 18, align: "center" }, [
          t("Key limitation", { width: fixed(180), size: 22, color: C.white, bold: true }),
          t("Tier 1 YouTube audio is mixed stereo, so H1 and the influence graph rely on Tier 2 and Tier 3.", {
            size: 22,
            color: "#EAF0EF",
          }),
        ]),
      ),
    ],
    { slideNo: "04", accent: C.teal, titleSize: 48, headerHeight: 126, gap: 20 },
  ),
  `The dataset strategy has three tiers plus one seed set. Tier 0 is five URLs from Prof. Hacker. Tier 1 is real-world but messy: public YouTube virtual choir videos for visual coordination. Tier 2 is clean but academic: multitrack recordings where each singer has a separate track. Tier 3 is controlled and experimental: we create it from Tier 2 by adding latency, jitter, and packet loss. In one sentence: Tier 0 gives seed examples, Tier 1 gives real-world video, Tier 2 gives clean per-singer audio, and Tier 3 gives controlled latency experiments.`,
);

const phases = [
  ["Phase 1", "Apr 16-Apr 30", "Scope, dataset strategy, repo scaffold", C.green, 0.22],
  ["Phase 2", "May 1-Jul 7", "Audio, video, network pipelines; E(t)", C.teal, 0.54],
  ["Phase 3", "Jul 8-Jul 31", "Paper, dashboard, final presentation", C.red, 0.24],
];

addSlide(
  presentation,
  slideRoot(
    "Plan: scope now, build next, synthesize in July",
    "overall project plan",
    [
      column({ width: fill, height: hug, gap: 14 }, [
        row(
          { width: fill, height: fixed(120), gap: 0 },
          phases.map(([name, dates, desc, color, ratio]) =>
            panel(
              {
                width: grow(ratio * 100),
                height: fill,
                padding: { x: 22, y: 20 },
                fill: color,
              },
              column({ width: fill, height: fill, justify: "between" }, [
                t(name, { size: 26, bold: true, color: C.white }),
                t(dates, { size: 18, bold: true, color: "#ECF4F3" }),
                t(desc, { size: 18, color: "#ECF4F3" }),
              ]),
            ),
          ),
        ),
        row({ width: fill, height: hug, justify: "between" }, [
          ...["VS#1 Apr 16", "VS#2 Apr 30", "VS#3 May 21", "VS#4 Jun 11", "VS#5 Jun 25", "VS#6 Jul 9", "Final Jul 23"].map((m, i) =>
            column({ width: hug, height: hug, align: "center", gap: 8 }, [
              shape({
                width: fixed(i === 1 ? 18 : 12),
                height: fixed(i === 1 ? 18 : 12),
                geometry: "ellipse",
                fill: i === 1 ? C.red : C.quiet,
              }),
              t(m, { width: fixed(130), size: 16, color: i === 1 ? C.red : C.quiet, bold: i === 1, style: { textAlign: "center" } }),
            ]),
          ),
        ]),
      ]),
      grid(
        {
          width: fill,
          height: fixed(410),
          columns: [fr(1), fr(1), fr(1)],
          columnGap: 24,
        },
        [
          panel(
            { width: fill, height: fill, padding: 24, fill: C.white, borderRadius: 18 },
            column({ width: fill, height: fill, gap: 16 }, [
              fixedChip("Done today", C.green, C.softGreen, 166),
              ...["Research question and hypotheses defined", "Data tiers clarified", "Repo scaffold ready", "Seed URLs recorded"].map((x) =>
                row({ width: fill, height: hug, gap: 12 }, [
                  shape({ width: fixed(10), height: fixed(10), geometry: "ellipse", fill: C.green }),
                  t(x, { size: 20, color: C.ink }),
                ]),
              ),
            ]),
          ),
          panel(
            { width: fill, height: fill, padding: 24, fill: C.white, borderRadius: 18 },
            column({ width: fill, height: fill, gap: 16 }, [
              fixedChip("Next", C.teal, C.softTeal, 112),
              ...["Tier 2 datasets on disk", "Tier 1 corpus curated", "Video pose data", "Influence graph pipeline"].map((x) =>
                row({ width: fill, height: hug, gap: 12 }, [
                  shape({ width: fixed(10), height: fixed(10), geometry: "ellipse", fill: C.teal }),
                  t(x, { size: 20, color: C.ink }),
                ]),
              ),
            ]),
          ),
          panel(
            { width: fill, height: fill, padding: 24, fill: C.white, borderRadius: 18 },
            column({ width: fill, height: fill, gap: 16 }, [
              fixedChip("Later", C.red, C.softRed, 116),
              ...["E(t) end-to-end", "Dashboard alpha", "Paper draft v1", "Final presentation and paper"].map((x) =>
                row({ width: fill, height: hug, gap: 12 }, [
                  shape({ width: fixed(10), height: fixed(10), geometry: "ellipse", fill: C.red }),
                  t(x, { size: 20, color: C.ink }),
                ]),
              ),
            ]),
          ),
        ],
      ),
    ],
    { slideNo: "05", accent: C.green, titleSize: 48 },
  ),
  `We split the 14 weeks into three phases. Phase 1 closes today with the research question, hypotheses, data tiers, and repo scaffold in place. The honest status is: we have seed URLs, but we have not yet collected the analysis corpus or extracted features. That starts in Phase 2. Zero feature code yet. The audio pipeline lands May 8. We are on schedule and there are no critical blockers.`,
);

const wp = [
  ["Audio pipeline", "Pull Tier 2 datasets; run pitch tracking and onset detection.", "Per-singer feature parquet for 5 pieces", "May 8", C.amber],
  ["Video pipeline", "Run MediaPipe Pose and FaceMesh on first 10 YouTube videos.", "Pose parquet + calibration note", "May 22", C.teal],
  ["Curated corpus + GDPR", "Hand-curate 20-30 videos; file DPIA outline.", "Corpus manifest + DPIA outline", "May 15 / 21", C.red],
  ["Virtual Mirror", "Export team WhatsApp; run SocialCompass tools.", "Mirror write-up for VS#3", "May 21", C.violet],
];

addSlide(
  presentation,
  slideRoot(
    "Sprint 2 turns the data strategy into files",
    "next iteration",
    [
      grid(
        {
          width: fill,
          height: grow(1),
          columns: [fr(1), fr(1)],
          rows: [fr(1), fr(1)],
          columnGap: 22,
          rowGap: 18,
        },
        wp.map(([name, step, output, date, color]) =>
          panel(
            { width: fill, height: fill, padding: 24, fill: C.white, borderRadius: 18 },
            column({ width: fill, height: fill, justify: "between", gap: 14 }, [
              row({ width: fill, height: hug, justify: "between", align: "center" }, [
                t(name, { width: fill, size: 25, bold: true, color: C.ink }),
                chip(date, color, "#F1F5F4"),
              ]),
              t(step, { size: 20, color: C.muted }),
              rule({ width: fill, stroke: C.line, weight: 2 }),
              t(output, { size: 21, bold: true, color }),
            ]),
          ),
        ),
      ),
      panel(
        { width: fill, height: hug, padding: { x: 24, y: 18 }, fill: "#172026", borderRadius: 18 },
        row({ width: fill, height: hug, align: "center", gap: 14 }, [
          chip("Dataset order", C.ink, C.white),
          t("Tier 2 on disk first -> Tier 1 curated second -> Tier 3 generated from Tier 2 after audio pipeline runs.", {
            size: 22,
            color: "#EAF0EF",
            bold: true,
          }),
        ]),
      ),
    ],
    { slideNo: "06", accent: C.amber, titleSize: 48 },
  ),
  `Sprint 2 runs from April 30 to May 21. First, the audio pipeline pulls the academic multitrack datasets to disk and outputs per-singer feature parquet by May 8. Second, the video pipeline starts pose and face tracking. Third, the curated YouTube corpus and GDPR work produce the corpus manifest and DPIA outline. Fourth, the Virtual Mirror produces the team self-analysis for May 21. If asked what exactly happens next: Tier 2 on disk first, Tier 1 curated second, then Tier 3 generated from Tier 2.`,
);

addSlide(
  presentation,
  slideRoot(
    "A lightweight operating rhythm for a short research build",
    "way of working",
    [
      grid(
        {
          width: fill,
          height: fixed(490),
          columns: [fr(1), fr(1), fr(1)],
          columnGap: 28,
        },
        [
          ["Cadence", C.green, ["3-week sprints", "Pre-VS review 1-2 days before", "Each sprint ends in an artefact", "Status meetings as checkpoints"]],
          ["Sync", C.teal, ["Weekly 30-minute team sync", "Daily async status posts", "WhatsApp + GitHub Issues", "Weekly check-in with Prof. Hacker"]],
          ["Toolstack", C.red, ["Python analysis pipeline", "Git + GitHub Actions", "Markdown source of truth", "Peer review through PRs"]],
        ].map(([heading, color, items]) =>
          panel(
            { width: fill, height: fill, padding: 28, fill: C.white, borderRadius: 20 },
            column({ width: fill, height: fill, gap: 22 }, [
              row({ width: fill, height: hug, gap: 14, align: "center" }, [
                shape({ width: fixed(44), height: fixed(44), geometry: "ellipse", fill: color }),
                t(heading, { size: 30, bold: true, color: C.ink }),
              ]),
              ...items.map((item) =>
                row({ width: fill, height: hug, gap: 12, align: "center" }, [
                  shape({ width: fixed(9), height: fixed(9), geometry: "ellipse", fill: color }),
                  t(item, { size: 22, color: C.muted }),
                ]),
              ),
            ]),
          ),
        ),
      ),
      panel(
        { width: fill, height: hug, padding: { x: 24, y: 18 }, fill: C.softViolet, borderRadius: 18 },
        row({ width: fill, height: hug, align: "center", gap: 16 }, [
          shape({ width: fixed(14), height: fixed(48), fill: C.violet, borderRadius: "rounded-full" }),
          t("Virtual Mirror link: our WhatsApp group is both the coordination channel and the May 21 self-analysis input.", {
            size: 22,
            bold: true,
            color: C.ink,
          }),
        ]),
      ),
    ],
    { slideNo: "07", accent: C.violet, titleSize: 46 },
  ),
  `Three pillars: cadence, sync, and toolstack. Cadence: three-week sprints aligned to status meetings, each ending in a defined artefact. Sync: weekly team meeting, daily async status posts, WhatsApp and GitHub Issues, plus a weekly check-in with Prof. Hacker. Toolstack: Python, Git and GitHub Actions, Markdown as source of truth, and peer review through pull requests. The team WhatsApp group is also our input data for the Virtual Mirror on May 21.`,
);

addSlide(
  presentation,
  layers({ width: fill, height: fill }, [
    background(),
    grid(
      {
        width: fill,
        height: fill,
        columns: [fr(1.1), fr(0.9)],
        columnGap: 50,
        padding: { x: 90, y: 82 },
      },
      [
        column({ width: fill, height: fill, justify: "between", gap: 30 }, [
          column({ width: fill, height: hug, gap: 18 }, [
            label("thank you", C.red),
            t("Questions welcome", {
              size: 88,
              bold: true,
              fontFace: titleFont,
              color: C.ink,
            }),
            t("Especially on dataset strategy, formula provenance, and research-question framing.", {
              width: wrap(880),
              size: 31,
              color: C.muted,
            }),
          ]),
          column({ width: fill, height: hug, gap: 12 }, [
            t("Project 8: Entanglement in Online Choir", { size: 27, bold: true, color: C.ink }),
            t("Zuraiz, on behalf of the team", { size: 22, color: C.quiet }),
          ]),
        ]),
        panel(
          { width: fill, height: fill, fill: "#172026", borderRadius: 30, padding: 44 },
          column({ width: fill, height: fill, justify: "center", gap: 24 }, [
            t("The core dataset answer", { size: 28, bold: true, color: C.white }),
            rule({ width: fixed(180), stroke: C.red, weight: 5 }),
            t("Seed examples -> real-world video -> clean multitrack -> controlled latency experiments", {
              size: 41,
              bold: true,
              fontFace: titleFont,
              color: "#EEF5F4",
            }),
          ]),
        ),
      ],
    ),
  ]),
  `That covers our team, scope, dataset strategy, project plan, next iteration, and way of working. Thank you for listening. I am happy to take your questions.`,
);

const pptxBlob = await PresentationFile.exportPptx(presentation);
await pptxBlob.save(PPTX_PATH);

const pptxBytes = await fs.readFile(PPTX_PATH);
const imported = await PresentationFile.importPptx(pptxBytes);

const previewPaths = [];
for (let i = 0; i < imported.slides.count; i += 1) {
  const slide = imported.slides.getItem(i);
  const canvas = new Canvas(W, H);
  const ctx = canvas.getContext("2d");
  await drawSlideToCtx(slide, imported, ctx);
  const file = path.join(PREVIEW_DIR, `slide_${String(i + 1).padStart(2, "0")}.png`);
  await canvas.toFile(file);
  previewPaths.push(file);
}

const thumbW = 480;
const thumbH = 270;
const montage = new Canvas(thumbW * 2, thumbH * 4);
const montageCtx = montage.getContext("2d");
montageCtx.fillStyle = C.paper;
montageCtx.fillRect(0, 0, thumbW * 2, thumbH * 4);
for (let i = 0; i < previewPaths.length; i += 1) {
  const img = await loadImage(previewPaths[i]);
  const x = (i % 2) * thumbW;
  const y = Math.floor(i / 2) * thumbH;
  montageCtx.drawImage(img, x, y, thumbW, thumbH);
  montageCtx.strokeStyle = "#CBD5D4";
  montageCtx.lineWidth = 2;
  montageCtx.strokeRect(x, y, thumbW, thumbH);
}
await montage.toFile(MONTAGE_PATH);

const report = {
  pptx: PPTX_PATH,
  slideCount: imported.slides.count,
  previews: previewPaths,
  montage: MONTAGE_PATH,
  renderedFrom: "saved pptx imported with PresentationFile.importPptx",
};
await fs.writeFile(QA_PATH, JSON.stringify(report, null, 2));
console.log(JSON.stringify(report, null, 2));
