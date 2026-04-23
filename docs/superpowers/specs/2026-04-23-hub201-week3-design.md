# Hub201 Week 3 — Customer Discovery and ICP Design Spec

**Date:** 2026-04-23
**Author:** Jamie Reynolds (designed with Claude)
**Status:** Approved for implementation planning
**Workshop context:** Hub201 Pre-Acceleration Programme, Belgrade. 19 cybersecurity startup teams, mostly technical CS students. Week 3 follows Week 2 (UVP + positioning, delivered 2026-04-08).

---

## 1. Context and goal

Hub201 Week 3 covers customer discovery and Ideal Customer Profile. The cohort is about to start reaching out to real customers for the first time. The workshop must leave each team with three concrete artefacts they can act on tomorrow:

1. A prioritised set of **hypotheses** about their customer and problem
2. A complete **interview plan** — script, cadence, write-up template
3. A **contact list** — narrow ICP, 20-30 named targets, channel-by-channel outreach plan

The workshop uses the same reusable pattern that Week 2 established (GitHub repo + CLAUDE.md coaching + knowledge files + worked examples + keynote + team-branded HTML deliverables), extended with a non-tech track that fixes the onboarding gap Week 2 hit with non-Claude-Code users.

The workshop must also **restructure the repo** so future weeks and future GNV workshops can reuse shared coaching material without duplication.

## 2. Decisions and principles

Settled during the brainstorm (2026-04-23):

- **Repo restructure to parallel `week2/` and `week3/` folders** with a `shared/` tree for cross-week material, not the current root-level Week 2 layout
- **Three exercises** for Week 3: Hypotheses, Interview Plan, Contact List — not the six in the original `week3-mapping.md`
- **Keynote story arc across three ventures** — Bondcube (warning), NPL Markets (B2B done right), P.S. Bridal (B2C done right), not a composite
- **Worked examples** — update both ShieldByte and ProcureSimple into Week 3 versions, not build fresh ones
- **Technical and non-technical tracks both required**, plus a keynote presentation that shows the worked examples
- **Low-tech track retained** — PPTX workbook + Excel contact tracker + printables, parallel to Week 2's pattern
- **Modular Option B architecture** — `shared/prompt-core/` + `shared/prompt-methodology/` + `week<N>/prompt-instance/`, combined by build scripts into the technical CLAUDE.md and the non-tech mega-prompt

Hard principles that govern the coach design:

- **Never hallucinate.** The coach does not invent stats, competitor names, market sizes, quotes, or references. If it does not know, it says so and tells the founder how to find out. Worked examples label every illustrative number explicitly.
- **Never block.** The coach does not refuse to produce outputs, does not gate on evidence quality, does not force the founder to go and validate before progressing. It produces best-effort drafts with weak spots flagged.
- **Enable progress, challenge fairly.** Friendly, coaching tone. Push on weak evidence, leading questions, vague segments — but always help the founder reach the next concrete action.
- **Behaviour over opinion.** Every exercise, every question, every output is anchored on real experience over stated intent.

## 3. Repository architecture

```
hub201-workshop/
├── README.md                             # root index with week selector
├── SETUP.md                              # common setup; routes to technical vs non-tech
├── scripts/
│   ├── build-claude-md.sh                # assembles week<N>/CLAUDE.md from sources
│   └── build-web-prompt.sh               # assembles week<N>/web/prompt.md from sources
├── shared/
│   ├── prompt-core/                      # universal GNV coach rules
│   │   ├── 01-coaching-rules.md          # never hallucinate, never block, enabling tone
│   │   ├── 02-evidence-scales.md         # Evidence Strength + Commitment Ladder
│   │   ├── 03-founder-nightmares.md      # five nightmares with warning signs
│   │   ├── 04-nine-fits.md               # 9 Fits Model
│   │   └── 05-output-conventions.md      # branding, file formats, never-hallucinate in outputs
│   └── prompt-methodology/
│       ├── discovery/                    # used by Week 3 and any future discovery workshop
│       │   ├── 01-say-do-gap.md
│       │   ├── 02-five-signals.md        # recency, behaviour, time/money, problem-area, awareness
│       │   ├── 03-open-question-rule.md
│       │   ├── 04-interview-methodology.md
│       │   ├── 05-recruiting-playbook.md
│       │   └── 06-credibility.md
│       └── cyber-context.md              # cross-cutting cyber market context (lifted from Week 2)
├── week2/
│   ├── CLAUDE.md                         # regenerated via build script
│   ├── SETUP.md
│   ├── prompt-instance/                  # Week 2-specific sources, extracted from existing CLAUDE.md
│   ├── web/                              # added: non-tech launcher for Week 2 (nice-to-have, not required tonight)
│   ├── workshop/
│   │   ├── presentation.html
│   │   └── speaker-notes.html
│   ├── examples/
│   │   ├── shieldbyte/                   # Week 2 outputs (unchanged content, moved path)
│   │   └── procuresimple/                # Week 2 outputs (unchanged content, moved path)
│   └── low-tech/                         # Week 2 PPTX/Excel (unchanged content, moved path)
└── week3/
    ├── CLAUDE.md                         # generated by build-claude-md.sh
    ├── SETUP.md                          # explains technical and non-tech tracks
    ├── prompt-instance/
    │   ├── 01-identity.md                # Hub201, cybersecurity, Week 3, cohort context
    │   ├── 02-philosophy.md              # thinker list credited (Bland, Osterwalder, Fitzpatrick, Torres, Coelen, Snyder + Jamie's guide)
    │   ├── 03-venture-stories.md         # Bondcube / NPL / P.S. Bridal
    │   ├── 04-exercise-1-hypotheses.md
    │   ├── 05-exercise-2-interview-plan.md
    │   ├── 06-exercise-3-contact-list.md
    │   ├── 07-flow.md                    # flow for this chat (intro, branding, menu, execution, assessment)
    │   └── 08-close.md                   # starter line
    ├── web/
    │   ├── index.html                    # one-page launcher with copy-prompt button
    │   └── prompt.md                     # generated by build-web-prompt.sh
    ├── workshop/
    │   ├── presentation.html             # keynote
    │   └── speaker-notes.html
    ├── examples/
    │   ├── shieldbyte/week3/
    │   │   ├── hypotheses.md
    │   │   ├── interview-plan.md
    │   │   ├── contact-list.md
    │   │   └── presentation.html
    │   └── procuresimple/week3/
    │       ├── hypotheses.md
    │       ├── interview-plan.md
    │       ├── contact-list.md
    │       └── presentation.html
    └── low-tech/
        ├── week3-workbook.pptx           # three exercises as fillable slides
        ├── contact-tracker.xlsx          # contact list tracker template
        ├── interview-script-skeleton.pdf # printable Intro/Industry/Business/Personal/Outro template
        └── question-rewrite-cheatsheet.pdf # closed/leading → open behavioural rewrite examples
```

## 4. The coach

Two rendered artefacts, one source of truth.

### 4.1 Technical track — `week3/CLAUDE.md`

Generated by `scripts/build-claude-md.sh` from the sources. Output structure:

- **Identity + behaviours + flow inlined** at the top (the active brain Claude Code always sees)
- **Knowledge references as file paths** (e.g. `See shared/prompt-methodology/discovery/02-five-signals.md`) — Claude Code reads these on demand
- **Exercise definitions inlined** so the agent always has the three exercise flows available

### 4.2 Non-tech track — `week3/web/prompt.md`

Generated by `scripts/build-web-prompt.sh` from the same sources. Output structure:

- **Part 1 — active brain** (concise, ~2k tokens): identity, 10 behaviours, flow
- **Part 2 — methodology** (inlined because the model has no file access): say-do-gap, five signals, open question rule, evidence scales, 9 fits, nightmares
- **Part 3 — three exercises** with output templates the coach writes to chat
- **Part 4 — reference**: three venture stories, recruiting playbook, credibility checklist, output format conventions
- **Closer line** that opens the first conversation

Founders copy this prompt from `week3/web/index.html`, paste into claude.ai (free account) or ChatGPT, and answer the coach's questions. The coach takes them through all three exercises end-to-end.

### 4.3 The 10 coaching behaviours

Both tracks inherit the same 10 behaviours from `shared/prompt-core/01-coaching-rules.md`:

1. Notice leading or closed questions and coach a rewrite
2. Rate every claim on evidence strength (strong / moderate / weak / assumption) as a signal, never as a blocker
3. Flag Founder Nightmares by name when the pattern appears
4. Push for segment specificity, produce a draft ICP anyway with assumptions flagged
5. Produce best-effort drafts from whatever evidence the team has; never refuse
6. Coach up the Commitment Ladder; name the next concrete step
7. Probe for behaviour over opinion
8. Recommend exercise order (Hypotheses → Interview Plan → Contact List) but do not enforce it
9. Final assessment per exercise — evidence rating + 2 biggest gaps + single next action
10. **Never hallucinate** — separate team inputs from coach suggestions; don't invent facts

## 5. Knowledge sources

### 5.1 `shared/prompt-core/`

- **`01-coaching-rules.md`** — the 10 behaviours above, tone guidance, never-hallucinate / never-block rules
- **`02-evidence-scales.md`** — Evidence Strength Scale (strong / moderate / weak / assumption) and Commitment Ladder (attention → time → reputation → money → repeat)
- **`03-founder-nightmares.md`** — Ego Echo-Chamber, Quicksand of No Validation, Frankensoft, Swamp of False Signals, Mirage of False Success, each with warning signs. Lifted from Week 2's CLAUDE.md and moved here for reuse.
- **`04-nine-fits.md`** — the 9 Fits Model. Pre-seed three fits (Customer/Problem, Problem/Solution, Revenue Model), seed four fits, Series A two fits. Week 3 focuses on Customer/Problem Fit.
- **`05-output-conventions.md`** — how outputs are structured (markdown file per exercise + consolidated HTML presentation in team branding), header format, evidence-assessment requirement, next-steps requirement, labelling illustrative content

### 5.2 `shared/prompt-methodology/discovery/`

- **`01-say-do-gap.md`** — belief vs behaviour; discovery must test behaviour; illustrative examples
- **`02-five-signals.md`** — the diagnostic frame the founder is running on every interviewee:
  - Recency + frequency ("when did you last do X")
  - Concrete behaviour ("give me a specific example")
  - Time + money spent (priority signal + whether this gets budget)
  - Problem-area match (segmentation signal)
  - Awareness level (market-maturity signal — do they know they have this problem, can we trigger awareness)
- **`03-open-question-rule.md`** — why/what/how used to surface real experience. Never do/would/could/should. Rewrite examples ("would you use this?" → "when did you last solve this, and how?")
- **`04-interview-methodology.md`** — adapted from Jamie's Notion guide:
  - Preparation (10-20 candidates, narrow segment, 2 weeks to 2 months)
  - Mindset (objective, get-the-why, never pitch)
  - Script skeleton Intro → Industry → Business → Personal → Outro (magic wand)
  - Recording + consent
  - Post-interview write-up (immediate, while fresh)
  - Affinity mapping after 10 interviews
  - VPC jobs/pains/gains as the lens for script design
  - Persona Canvas for synthesis
  - Credit to Bland & Osterwalder (Testing Business Ideas) preserved
- **`05-recruiting-playbook.md`** — B2B hacks (cold outreach personalised, industry events negotiated free, industry panels for credibility, social media, advisory networks), B2C hacks (social + value-first offers), paid platforms flagged for later. Lifted from Jamie's Notion guide.
- **`06-credibility.md`** — NPL Markets lesson as a concrete pre-outreach checklist: basic website, proper LinkedIn, at least one piece of social proof (advisor / press mention / event appearance / industry body association). How to manufacture credibility when you don't have it yet.

### 5.3 `week3/prompt-instance/`

- **`01-identity.md`** — Hub201 Week 3, cybersecurity cohort, Belgrade, first-time discovery context
- **`02-philosophy.md`** — thinker attribution: Bland & Osterwalder, Fitzpatrick, Torres, Coelen, Snyder, plus explicit credit to Jamie's own guide as the methodology backbone
- **`03-venture-stories.md`** — three story entries:
  - **Bondcube** — warning. Jamie personally signed 40 LoIs, team got to 250 LoIs with investment institutions, never collected meaningful feedback. "Thought we were heroes, were setting ourselves up for failure." Lessons: Quicksand of No Validation + Ego Echo-Chamber + LoIs without behavioural data are vanity signals.
  - **NPL Markets** — B2B done right. 100+ customer + expert conversations, cold outreach via LinkedIn/email/phone + advisory networks. First meeting = credibility-first posture (present self + concept, discovery in second half, treated like sales for high-status hedge funds and banks). Concierge-style MVP validated need after market mapping. Social proof engine: industry events, expert interviews producing market research reports, partnerships with industry bodies + regulator. Lesson: credibility (website, LinkedIn, social proof) buys the meeting with high-status buyers.
  - **P.S. Bridal** — B2C done right. B2C is harder because customers won't give you interview time. Solution: tiny prototypes that deliver value AND collect info (wedding dress style finder, WhatsApp concierge). Iterative prototype ladder (style finder → booking → style pack → directory). Two years part-time, found value prop, had to change business model to rental. Lesson: in B2C, the prototype is the interview — you earn the conversation by giving value first.
  - **Common arc**: both NPL and P.S. Bridal reached Customer/Problem Fit → Problem/Solution Fit through different routes but same discipline (narrow target, behaviour over opinion, iteration, social proof built into the process)
- **`04-exercise-1-hypotheses.md`** — purpose, inputs, coaching flow (assumption inventory → D/F/V split → riskiest-first prioritisation → PULL hypothesis format with kill/validate criteria), output template, evidence check
- **`05-exercise-2-interview-plan.md`** — purpose, inputs (hypotheses), coaching flow (script skeleton + open question rule + five-signal tagging per question + consent + cadence + write-up template), output template with questions tagged by both hypothesis and signal, evidence check
- **`06-exercise-3-contact-list.md`** — purpose, inputs, coaching flow (ICP narrowing drill + credibility checklist + channel sourcing + first-touch templates + tracking sheet), output template, evidence check
- **`07-flow.md`** — sequencing for this chat: greet → ask startup one-liner → ask branding → present menu → run chosen exercise → post-exercise assessment → loop → offer consolidated presentation
- **`08-close.md`** — starter line that ends the prompt and opens the conversation

## 6. Exercises

### 6.1 Exercise 1 — Hypotheses

**Purpose.** Turn assumptions about customer + problem into prioritised testable hypotheses.

**Output (`/outputs/week3/hypotheses.md`):**
- Current customer/problem statement (pulled from Week 2 if present, drafted fresh if not)
- Assumption inventory grouped Desirability / Feasibility / Viability
- Top 5 assumptions ranked by risk, with reasoning
- PULL hypothesis for each top 5 (Population / Understanding / Learning / Limit)
- Kill/validate criteria per hypothesis
- Evidence rating per hypothesis (strong / moderate / weak / assumption)
- Single biggest risk flagged

**Evidence check.** Are hypotheses testable through an interview, or are they dressed-up features?

### 6.2 Exercise 2 — Interview Plan

**Purpose.** Design a discovery script that tests Exercise 1's hypotheses without leading or prompting politeness bias.

**Output (`/outputs/week3/interview-plan.md`):**
- Full 20-30 question script organised Intro → Industry → Business → Personal → Outro
- Each question tagged with (a) the hypothesis it tests and (b) which of the Five Signals it is there to elicit
- Consent-to-record script
- Length guidance (30-45 min target)
- Cadence plan (5 interviews per week, script review after interview 1, affinity mapping after interview 10)
- Post-interview write-up template
- Red-flag list of question patterns to avoid

**Evidence check.** Does every question probe behaviour over opinion? Does the script cover all five signals?

### 6.3 Exercise 3 — Contact List

**Purpose.** Build a concrete narrow list of 20-30 target interviewees with channel-by-channel first-touch plan.

**Output (`/outputs/week3/contact-list.md`):**
- Narrow ICP definition (one sentence: specific, triggered, reachable)
- Credibility checklist with status (website, LinkedIn, social proof)
- Target contact table: Name | Role | Company | Why them (fit) | Channel | First-touch plan | Status
- Outreach templates by channel: personalised cold email, LinkedIn opener, cold call script
- Channel mix recommendation
- Referral-ask template for after a good interview

**Evidence check.** Is the ICP specific enough that two different team members would independently identify the same person as a target?

### 6.4 Consolidated deliverable — `/outputs/week3/presentation.html`

Same pattern as Week 2. Team-branded single-file HTML with inlined CSS and Google Fonts:
1. Title + team name + date
2. Hypotheses — top 5 PULL hypotheses ranked by risk with evidence ratings
3. Interview Plan — full script organised by theme with signal + hypothesis tags
4. Contact List — ICP, credibility checklist, contact table, channel templates
5. Commitments — next 4 weeks of interviews, review cadence, affinity mapping date
6. Evidence summary — overall rating, biggest risk, single most valuable next action

## 7. Keynote presentation

`week3/workshop/presentation.html` + `week3/workshop/speaker-notes.html`. Single self-contained HTML each, inlined CSS, Inter via Google Fonts, Hub201 / GNV brand.

**Slide structure (45 slides in 8 parts):**

- **Part 1 (1-5)** — Opening, 9 Fits Model, what discovery is, Say-Do Gap, the pre-seed trap
- **Part 2 (6-19)** — Three venture stories:
  - Bondcube (6-8): setup, what happened (40 personal + 250 total LoIs, no behavioural feedback, "thought we were heroes"), lesson
  - NPL Markets (9-14): setup, outreach channels, credibility-first first meetings, social proof engine, concierge MVP validation, lesson (credibility buys the meeting)
  - P.S. Bridal (15-19): B2C discovery problem, prototype-as-discovery, iterative prototype ladder, 2-year journey to rental pivot, lesson (prototype is the interview)
- **Part 3 (20-21)** — Common arc: both reached Customer/Problem Fit → Problem/Solution Fit
- **Part 4 (22-27)** — Methodology: attribution credits, open question rule with rewrite examples, the Five Signals diagnostic frame, VPC lens, Intro → Industry → Business → Personal → Outro skeleton, cadence, Evidence + Commitment Ladders
- **Part 5 (28-30)** — Three exercise briefs
- **Part 6 (31-37)** — Worked examples: ShieldByte Week 3 snapshots (hypotheses, interview plan, contact list), ProcureSimple Week 3 snapshots, side-by-side pattern recognition
- **Part 7 (38-40)** — How to use the coach: technical track (Claude Code + clone repo), non-tech track (claude.ai + paste mega-prompt), branding behaviour
- **Part 8 (41-45)** — Between-now-and-Week-4 commitments, credibility baseline check, success criteria for Week 4, Q&A, close

**Speaker notes file** — one paragraph per slide plus check-in prompts at key moments:
- After slide 4 (Say-Do Gap) — "hands up, who has interviewed a customer before?"
- After slide 14 (NPL lesson) — "look at your LinkedIn right now. Would a CTO at a Belgrade bank take a meeting based on what they see?"
- After slide 19 (P.S. Bridal lesson) — "what tiny thing could you give someone in exchange for 15 minutes?"
- After slide 30 (exercises) — "which exercise is the biggest unknown for your team?"
- Exercise transition prompt after slide 37 — "now open your coach and start Exercise 1"

"Never hallucinate" pinned visibly on slide 39 so teams know not to trust invented facts from the coach.

## 8. Worked examples

Two fictional teams, each with `examples/{company}/week3/{hypotheses,interview-plan,contact-list}.md` + `presentation.html` in the team's fictional branding.

**Discipline rule applied to both.** Every fabricated number, buyer title, event name, industry body, or company name is explicitly labelled **[illustrative]** in the output. The coach never presents invented data as market truth.

### 8.1 ShieldByte Week 3 (cyber, matches cohort)

Continues the Week 2 positioning: phishing response automation for security teams at 200-500 person regulated fintechs.

- **Hypotheses.** Top 5 ranked by risk, each flagged as weak evidence or assumption. Biggest risk: analyst time-per-triage assumption, which drives the ROI story.
- **Interview Plan.** 24-question script tagged by hypothesis + five-signal. Models behavioural probes ("when was the last phishing incident your team triaged, walk me through exactly what happened" / "show me how you handle these today" / "what did you spend on security tooling in the last 12 months").
- **Contact List.** Narrow ICP ("Head of Security at a 200-500 person regulated fintech in DACH, CEE, or UK that has hired at least one SOC analyst in the last 12 months"). Credibility checklist. 25 [illustrative] named targets across LinkedIn / events / industry body / Hub201 advisor channels. Outreach templates.
- **Evidence summary.** Assumption-Heavy (honest and expected). Next action tomorrow: send first five outreach messages.

### 8.2 ProcureSimple Week 3 (B2B procurement, maps to Groundley)

Continues the Week 2 positioning: spend management for European mid-sized manufacturers.

- **Hypotheses.** Top 5 ranked by risk. Biggest risk: who controls budget for spend-management software (procurement vs finance) — if wrong, GTM motion changes.
- **Interview Plan.** 26-question script tagged by hypothesis + five-signal. Behavioural probes ("when did you last onboard a new supplier, walk me through the first week" / "who signed off the last software purchase" / "show me last month's supplier spend").
- **Contact List.** Narrow ICP ("Head of Procurement at a 500-2000 person European manufacturer in metals, machinery, or food processing that has acquired or merged in the last 18 months"). Credibility checklist. 30 [illustrative] targets across LinkedIn / trade shows / advisory network / regional industry body channels. Second-touch plan for unresponsive contacts.
- **Evidence summary.** Assumption-Heavy. Biggest risk: budget ownership. Next action: send the advisory-network warm intro first.

### 8.3 Consolidated presentations

Each example gets its own `presentation.html` styled in the fictional team's brand. These double as the source for keynote slides 31-37 — the slides render excerpts from these files, so there is one source of truth per example.

## 9. Web launcher — `week3/web/index.html`

One page. Hub201 / GNV brand. Opens at `https://theginjaninja.github.io/hub201-workshop/week3/web/`.

**Structure:**
- Header — "Hub201 Week 3 — Customer Discovery and ICP"
- Hero block — "Non-technical track. Copy the prompt, paste it into claude.ai (free), answer the coach's questions."
- Three numbered steps:
  1. Click the button below to copy the coach prompt
  2. Open claude.ai (free account) or ChatGPT — start a new chat
  3. Paste the prompt and send; the coach runs all three exercises
- **Big "Copy coach prompt" button** — on click, copies `prompt.md` content to clipboard, shows success state
- Collapsed `<details>` preview showing the prompt content so founders see what they are pasting
- Secondary block — "Using Claude Code instead? See the technical setup guide" with link to `week3/SETUP.md`
- Footer — links to the three worked example presentations and the keynote

**Single source of truth.** The HTML `fetch()`es `prompt.md` at page load into the copy-to-clipboard textarea and the preview block. No build step in the browser, no duplication of content.

**Context-length warning.** The page tells founders: "works best with Claude.ai or GPT-4 class models. Older ChatGPT tiers may not fit the full prompt."

## 10. Low-tech track — `week3/low-tech/`

For teams that cannot or will not use an AI tool. Parallel to Week 2's low-tech pattern.

- **`week3-workbook.pptx`** — three exercises as fillable slide templates. Cover slide, then per-exercise: context slide, template slide for the team to complete, assessment slide for evidence rating.
- **`contact-tracker.xlsx`** — contact list tracker with columns for Name / Role / Company / Why them / Channel / First-touch plan / Status / Interview date / Notes / Evidence rating.
- **`interview-script-skeleton.pdf`** — printable Intro → Industry → Business → Personal → Outro template with blank question slots.
- **`question-rewrite-cheatsheet.pdf`** — closed/leading → open behavioural rewrite examples, the Five Signals frame, the open question rule.

Teams on the low-tech track follow the keynote and fill in the templates by hand, with a facilitator or mentor in the role the coach would otherwise play.

## 11. Build scripts

Both scripts live in `scripts/` at the repo root and take a week number as argument (`scripts/build-claude-md.sh 3`).

**`scripts/build-claude-md.sh`**

- Concatenates in order: week instance identity + shared core (coaching rules, evidence scales, nightmares, nine fits, output conventions) + week instance philosophy + week instance exercises + week instance flow
- Inserts methodology references as file paths (e.g. "See `shared/prompt-methodology/discovery/02-five-signals.md`") rather than inlining content
- Writes output to `week<N>/CLAUDE.md`

**`scripts/build-web-prompt.sh`**

- Concatenates in Part 1 / Part 2 / Part 3 / Part 4 order
  - Part 1 (active brain): week identity + shared coaching rules + week flow
  - Part 2 (methodology): shared evidence scales + nightmares + nine fits + full methodology folder inlined
  - Part 3 (exercises): week instance exercises with templates
  - Part 4 (reference): week instance venture stories + recruiting playbook + credibility + output conventions
- Closes with the starter line from `week<N>/prompt-instance/08-close.md`
- Writes output to `week<N>/web/prompt.md`

Both scripts are plain bash, idempotent, no external dependencies. Running them updates the generated files. Generated files are committed to the repo so cloners do not need to run the build — maintainers regenerate when sources change.

## 12. Week 2 migration

Step 1 of the implementation order. Moves existing Week 2 files into the new `week2/` structure.

- Existing `CLAUDE.md` is the extraction source for:
  - `shared/prompt-core/03-founder-nightmares.md` (Section 7 of CLAUDE.md)
  - `shared/prompt-core/02-evidence-scales.md` (Evidence Strength Scale + Commitment Ladder from Section 2)
  - `shared/prompt-core/04-nine-fits.md` (Section 8 of CLAUDE.md)
  - `week2/prompt-instance/01-identity.md`, `02-philosophy.md`, `07-flow.md` (Sections 1, 2, 4)
  - `week2/prompt-instance/03-coaching-behaviours.md` (Section 3 — kept as Week 2's variant; `shared/prompt-core/01-coaching-rules.md` is the Week 3-onwards set)
  - After extraction, a regenerated `week2/CLAUDE.md` is produced by `scripts/build-claude-md.sh 2`. Committed. Original root `CLAUDE.md` deleted.
- Existing `knowledge/` maps file-by-file:
  - `cyber-context.md` → `shared/prompt-methodology/cyber-context.md`
  - `competition-matrix.md`, `differentiation-statement.md`, `personas.md`, `sales-battlecard.md`, `solution-one-pager.md`, `value-proposition.md` → `week2/prompt-instance/` (Week 2-specific positioning knowledge)
  - `week3-mapping.md` → deleted (its purpose is superseded once Week 3 ships)
- `examples/` → `week2/examples/` (path moves, content unchanged)
- `workshop/` → `week2/workshop/` (path moves, content unchanged)
- `low-tech/` → `week2/low-tech/` (path moves, content unchanged)
- `SETUP.md` → `week2/SETUP.md` and a new common `SETUP.md` at root routing to weeks

**Risk flagged.** Any Week 2 URL a team bookmarked will move. The cohort has their Week 2 outputs in their own `/outputs/` folders so that is safe, but shared links to the keynote or worked-example pages break. Mitigation: the root `README.md` has a week selector that links to each week's top-level page. If a team lost a bookmark, one click from the root restores navigation.

## 13. Implementation order

1. Restructure Week 2 into `week2/` folder (files move, content unchanged). Smoke-test GitHub Pages still serves.
2. Build `shared/prompt-core/` (five files) and `shared/prompt-methodology/discovery/` (six files).
3. Build `week3/prompt-instance/` (eight files) including venture stories with Bondcube LoI numbers (40 personal, 250 total) and the NPL + P.S. Bridal detail.
4. Write `scripts/build-claude-md.sh` and `scripts/build-web-prompt.sh`. Test on Week 3 sources.
5. Generate and commit `week3/CLAUDE.md` and `week3/web/prompt.md`. Review output end-to-end.
6. Build `week3/web/index.html` — launcher page with copy-prompt button and three-step setup.
7. Build worked examples: `week3/examples/shieldbyte/week3/*` and `week3/examples/procuresimple/week3/*` including the consolidated presentations.
8. Build keynote and speaker notes: `week3/workshop/presentation.html` + `speaker-notes.html`. Slides 31-37 render from the worked example files.
9. Write `week3/SETUP.md` explaining technical + non-tech tracks and linking the web launcher.
10. Build low-tech track: `week3-workbook.pptx`, `contact-tracker.xlsx`, `interview-script-skeleton.pdf`, `question-rewrite-cheatsheet.pdf`.
11. Smoke-test both tracks end-to-end:
    - Run the non-tech prompt in a fresh claude.ai chat with a fake startup — confirm the coach opens correctly, asks for branding, presents the menu, runs an exercise, produces output, rates evidence.
    - Run the technical version in a fresh Claude Code session — same test.
12. Commit, push, deploy GitHub Pages, confirm URLs live.

## 14. Non-goals

- Not rebuilding Week 1 content (delivered by Marcus Sandberg, out of Hub201's scope for Jamie).
- Not building a hosted Claude.ai project version. The launcher-plus-mega-prompt approach is deliberately portable to both claude.ai and ChatGPT.
- Not building a second round of interviews or customer-validation content. That is out of scope for Week 3 and explicitly mentioned in Jamie's Notion guide as a future companion piece.
- Not changing the Week 2 delivered content (coach behaviour, knowledge files, examples). Only the paths change.

## 15. Open items flagged for implementation planning

- **Build script edge cases.** What happens if a source file is missing? (Suggested: fail loudly with a clear error pointing to the missing file.)
- **Cross-browser clipboard API support.** Some environments block `navigator.clipboard.writeText`. The launcher should fall back to the legacy `document.execCommand('copy')` on failure.
- **Low-tech artefact authoring tool choice.** PPTX and XLSX authored in what — Keynote export, Google Slides/Sheets export, or direct `.pptx`/`.xlsx` generation? Implementation plan to decide.
- **GitHub Pages routing.** Confirm the new `week3/web/` path resolves correctly as `/week3/web/` on the deployed site.

## 16. Approval state

Design approved by Jamie Reynolds on 2026-04-23. Ready for writing-plans skill to build the detailed implementation plan.
