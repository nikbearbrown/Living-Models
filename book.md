# Living Models

*Causal Intelligence for the Decisions That Actually Matter*

**Nik Bear Brown**

*Per-book CLAUDE.md for `living-models`. Read by `/chapter`, `/essay`, `/bookmap`, `/nart` every run. Hard rules in root `CLAUDE.md` §7 are not adjustable here. Voice specifics may be adjusted below.*

> *The data was never the problem. It was always the question.*

---

## One-sentence description

A working architecture for causal intelligence — systems that reason about deliberate intervention, not just description — for executives, strategists, and engineers who have to act under conditions where the past is no longer a reliable guide to the future.

## Audience

Senior strategists, technical leaders, and engineers who build, evaluate, or rely on decision systems in fast-moving environments. Comfort with elementary probability and basic regression is assumed. Formalism is introduced as instruments under test rather than as prerequisites the reader has already paid for. The book is structured so that a strategy executive can read Part One alone for the diagnosis; the full argument requires Parts Two and Three together. The technical reader gets a complete pass at the architecture without being patronized; the executive reader gets the machinery without being pretended-at.

## Scope

- **In:** Pearl's three-rung ladder; the do-operator; Directed Acyclic Graphs and Structural Causal Models; Markov equivalence and the CPDAG; backdoor criterion; double machine learning; heterogeneous treatment effects; abduction-action-prediction counterfactuals; randomized trials and SUTVA; latent confounding and collider bias; expert elicitation as Knowledge Engineering with Bayesian Networks; LLM-guided causal interview architecture; the Causal Brain Executive Report; Bayesian parameter updating and structural drift detection; DecisionOps.

- **Out:** Descriptive analytics defended on its own terms; conventional dashboards treated as endpoints rather than inputs; deep ML internals beyond what causal validation requires; predictive accuracy maximization treated as the goal rather than as one input among others; pure ethics treatments separated from validation practice.

## Prerequisites

Elementary probability and basic regression. Willingness to read a graph as a structural claim about mechanism, not as a picture of correlations. Comfort with the idea that the same data can be consistent with multiple causal structures. No prior exposure to the do-operator is required — the book teaches it from first principles in Chapter 5.

## Voice notes (book-specific)

- **Register:** Feynman-flavored architecture pedagogy. Mechanism visible. The voice of someone working through the design out loud — not lecturing on settled doctrine. Pretension stripped, jargon translated or cut.

- **Origin frame:** the book opens from a concrete question that arrived in an email — *how do you build intelligence that actually keeps pace with decisions that have to be made in fast-moving environments?* The first-principles answer is the book. First person is used to label position-taking ("I conclude," "my reading is"); "you" invites the reader to predict and reason; "we" works through the harder mechanisms together.

- **Math on the page when it earns its place.** The do-operator is met as machinery in Chapter 5, not as decoration. Calculations are visible. A chapter that says "the model estimates" without showing what it estimates and how is not doing the method.

- **Pearl's Ladder is the spine.** Introduced in Chapter 5; rung-2 (intervention) revisited in Chapters 8, 11, 18; rung-3 (counterfactual) opened in Chapter 9 and closed in Chapter 19. Each return is explicit and adds a validation lens.

- **The forbidden phrases list applies in full.** "Real-time" is interrogated in Chapter 3 and replaced thereafter with *continually updated*. "Stakeholders" is cut. "Robust" is qualified or cut. "Risk" is never collapsed into a single number after Chapter 4.

- **Recommended over neutral.** The book takes positions. The diagnosis in Part One is sharp. The architectural choices in Part Three are recommended ones. Positions carry their evidence on the page; reasonable disagreement is named where it exists.

## Chapter cadence

Linear within each part, with deliberate handoffs between parts.

- **Part One (Chs. 1–4)** defines the failure mode without introducing formalism. A reader of Part One alone gets the diagnosis: why three decades of analytics have produced sophisticated hindsight and very little foresight.

- **Part Two (Chs. 5–12)** develops the mathematical apparatus from first principles. Chapters 5–9 build the Ladder; Chapters 10–12 name what the apparatus cannot do — confounders, colliders, the unconfoundedness assumption, the plumber's gap between estimate and intervention.

- **Part Three (Chs. 13–20)** is the architecture and operating model — what to build, how to keep it alive, and what its output looks like to the executive who has to act on it.

The full argument requires all three parts. A reader who skips Part Two will not be able to interrogate the architecture in Part Three; a reader who skips Part Three will not see the diagnosis in Part One closed.

## Running examples

- **Pearl's Ladder** — the spine across Parts Two and Three. Each rung is introduced as machinery, returned to as a validation lens, and used in the architecture chapters as a check on what kind of claim a given calculation is actually making.

- **Esther Duflo's experimental design and "economist as plumber"** — Chapters 11 and 12. The translation from clinical "treatment" to organizational "intervention" runs through Part Two and is operationalized in Part Three.

- **The Nina framework (LLM-guided expert interviews from brand strategy)** — Chapter 16's architectural analog. Used to show executives a system they can already picture before introducing the causal machinery underneath.

- **The Innovator's Dilemma** — reframed in Chapter 2 as a problem of organizational time-horizon and incentive design, not just strategic foresight. Returned to in Chapter 19 as one of the cases the executive report has to handle without flinching.

- **Ne-FMS case** — Chapter 12. What "fixing the plumbing" actually looks like when the causal estimate is correct and the implementation is the bottleneck.

## Hero image direction (optional)

*[Fill in. Suggestion: visual identity that distinguishes "graph as map of mechanism" from "graph as picture of correlation" — the cover and chapter heroes should make that distinction visible at a glance.]*

## Voice ground truth (optional)

The foreword (`chapters/2026-03-16-foreword.md`) is voice ground truth for this book — author's prose, written before the chapters. Until per-book samples accumulate in `books/living-models/style/`, skills will fall back to root `style/` and may flag drafts `voice-unanchored`. Recommended next move: drop the foreword and the first finalized chapter into `books/living-models/style/` so skills calibrate to this voice rather than the workshop default.

## Spine source

The book is structured around the four-property definition of a Living Model (causal, counterfactual, continually updated, treatment-oriented) — introduced in Chapter 13 and used as the integrity check across the architecture chapters that follow. Every architectural decision in Part Three is auditable against those four properties.

---

*Initial version: 2026-05-01.*
*Revisions logged inline; structural changes noted in workshop `CHANGELOG.md`.*
