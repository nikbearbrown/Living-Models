# Living Models — Chapter Outline

*One-line title + one-sentence purpose per chapter. Purpose = what the reader will understand after the chapter that they did not understand before. Planning tool, not a table of contents.*

---

## To write

### Front matter

- **Foreword (drafted, parked in `chapters/2026-03-16-foreword.md`)** — *Why this book exists: an email, a first-principles question, a working answer.*
- **Preface — The Monday Morning Meeting** — *Why dashboards reliably describe the past but unreliably navigate the future, and what this book asks of the reader.*

### Part One — The Problem
*Why three decades of analytics have produced sophisticated hindsight and very little foresight. **All four chapters drafted 2026-05-01 — awaiting Nik's review.***

### Part Two — The Theory
*The mathematical foundations of causal intelligence — made readable. **Chapters 5–11 drafted 2026-05-01 — awaiting Nik's review. Chapter 12 still to write.***

- **Chapter 12 — The Plumber's Objection** — *Duflo's "economist as plumber"; the distance between a correct causal estimate and an effective organizational change; the Ne-FMS case.*

### Part Three — The Architecture
*How to build systems that actually use this theory. **Chapter 13 drafted 2026-05-01 — awaiting Nik's review.***

- **Chapter 14 — The Expert in the Room** — *Knowledge Engineering with Bayesian Networks: what the field knows, the validated elicitation protocols, and why those methods have not reached the corporate boardroom.*
- **Chapter 15 — How Experts Get Causation Wrong** — *Collider blindness, feedback-loop simplification, domain-matching heuristics; when to trust expert causal judgment and when to interrogate it.*
- **Chapter 16 — The Machine That Interviews the Expert** — *LLM-guided causal elicitation; the Nina-framework architectural parallel; the forty-five-minute first-pass DAG; multi-agent design for elicitation, consistency, and equivalence.*
- **Chapter 17 — Resolving the Graph** — *PC, GES, NOTEARS, FCI; the CPDAG handoff; when to gather more data and when to run more expert sessions; the validated graph as a living artifact.*
- **Chapter 18 — From Graph to Decision** — *Parameterizing the graph, running the counterfactual, ranking interventions by Expected Value, and the constrained-knapsack from rankings to portfolio decisions.*
- **Chapter 19 — The Causal Brain Executive Report** — *The auditable recommendation: recommendation, evidence, assumptions, counterfactual; what LLM narration must do, must never do, and where accountability sits when the decision is wrong.*
- **Chapter 20 — Keeping the Model Alive** — *Bayesian updating of edge parameters, structural change detection, DecisionOps vs. MLOps, and the minimum viable feedback loop.*

## Drafted

*Chapters with a draft in `chapters/`, awaiting Nik's review.*

- **Foreword — *(2026-03-16)*** — `chapters/2026-03-16-foreword.md` — author's note; voice ground truth.

### Part One — The Problem (all four drafted 2026-05-01)

- **Chapter 1 — The Dashboard That Lied** — `chapters/2026-05-01-chapter-1-the-dashboard-that-lied.md` — *WAU silent failure + J.C. Penney 2012; Pearl's Ladder; four rungs of analytics maturity. Largely Nik's prose, lightly cleaned and given chapter frontmatter.*
- **Chapter 2 — The Map That Doesn't Move** — `chapters/2026-05-01-chapter-2-the-map-that-doesnt-move.md` — *Zillow Offers 2021 cold open; observational vs interventional distribution; Innovator's Dilemma as time-horizon/incentives problem.*
- **Chapter 3 — What We Mean When We Say "Real-Time"** — `chapters/2026-05-01-chapter-3-what-we-mean-when-we-say-real-time.md` — *Three latencies (data, model, decision); fraud detection three-system worked example; "continually updated" as the honest replacement.*
- **Chapter 4 — Risk Is Two Numbers, Not One** — `chapters/2026-05-01-chapter-4-risk-is-two-numbers-not-one.md` — *LTCM 1998 cold open; the heat map's structural failure; Expected Value of Intervention as foundational metric.*

### Part Three — The Architecture (all eight chapters drafted 2026-05-01)

- **Chapter 13 — The Living Model Defined** — `chapters/2026-05-01-chapter-13-the-living-model-defined.md` — *Aerospace boardroom cold open; four properties defined precisely; comparison to dashboards, predictive models, 3D digital twins, ontological systems; analytics maturity revisited as orthogonal to Pearl's Ladder; orchestrated outcomes as emergent property of the four together.*
- **Chapter 14 — The Expert in the Room** — `chapters/2026-05-01-chapter-14-the-expert-in-the-room.md` — *Goulburn-Broken Catchment cold open; Markov equivalence as mathematical necessity for expert input; Feigenbaum's knowledge bottleneck; KEBN protocols (variable identification, edge elicitation, noisy-OR, Delphi, IDEA); validated successes in clinical, environmental, military domains; six structural barriers to corporate adoption.*
- **Chapter 15 — How Experts Get Causation Wrong** — `chapters/2026-05-01-chapter-15-how-experts-get-causation-wrong.md` — *Berkson 1946 gallbladder cold open; collider blindness with the bullwhip effect as a worked example; feedback-loop simplification (reinforcing, balancing); domain-matching heuristics with physics envy and the 2008 financial crisis; Hogarth's kind vs wicked learning environments; three architectural implications for the elicitation in Ch16.*
- **Chapter 16 — The Machine That Interviews the Expert** — `chapters/2026-05-01-chapter-16-the-machine-that-interviews-the-expert.md` — *Founder's Nina-framework interview cold open; interview-as-software insight; four-phase causal elicitation protocol (variable identification, edge elicitation, equivalence resolution, confidence calibration); forty-five-minute benchmark; four-agent architecture (Interviewer, Consistency, Equivalence, Bias-Watch); honest accounting of what the system can and cannot do.*
- **Chapter 17 — Resolving the Graph** — `chapters/2026-05-01-chapter-17-resolving-the-graph.md` — *Product team after the elicitation cold open; PC, GES, NOTEARS, FCI as four algorithmic paradigms; CPDAG handoff and the three patterns (agreement, refinement, disagreement); aleatory-vs-epistemic decision framework for more-data-vs-more-experts; validated graph as living artifact under version control, drift monitoring, re-elicitation triggers, and audit.*
- **Chapter 18 — From Graph to Decision** — `chapters/2026-05-01-chapter-18-from-graph-to-decision.md` — *VP of operations with thirty-one candidate interventions cold open; four operational steps from validated graph to recommendation: parameterization (linear and DSCM), counterfactual engine (abduction-action-prediction with heterogeneity), Expected Value ranking with uncertainty bounds and persuadable segmentation, constrained-knapsack portfolio optimization (multidimensional, logical-dependency, multiple-choice, chance-constrained); the structured package handed to Ch19's executive report.*
- **Chapter 19 — The Causal Brain Executive Report** — `chapters/2026-05-01-chapter-19-the-causal-brain-executive-report.md` — *CEO before her board meeting cold open; the four-part report structure (recommendation, evidence, assumptions, counterfactual) and why that order; six must-do behaviors for LLM narration; six must-never-do behaviors enforced by guardrails; decision-focused visualization that abandons the full graph as primary visual; accountability located in the audit record with the named human owner.*
- **Chapter 20 — Keeping the Model Alive** — `chapters/2026-05-01-chapter-20-keeping-the-model-alive.md` — *Logistics company eighteen months in with drift detector firing cold open; three modes of decay (parametric, structural, mechanism failure); Bayesian updating with uncertainty propagation, informative-data weighting, interventional data; structural change detection (CMSI, DOCL, CaSCo) with graduated escalation; DecisionOps vs MLOps along four axes (decision vs prediction, contested vs stable world, pipeline vs model artifact, throughout vs end review); the minimum viable feedback loop in four stages; closing of the architectural arc.*

### Part Two — The Theory (Chapters 5–12 drafted 2026-05-01)

- **Chapter 5 — Pearl's Ladder** — `chapters/2026-05-01-chapter-5-pearls-ladder.md` — *Welcome-survey cold open; three rungs explained; do-operator; why the rungs are sealed.*
- **Chapter 6 — Graphs That Think** — `chapters/2026-05-01-chapter-6-graphs-that-think.md` — *Regression vs causal claim; DAGs as maps of mechanism; SCMs; same data fits multiple structures.*
- **Chapter 7 — The Equivalence Problem** — `chapters/2026-05-01-chapter-7-the-equivalence-problem.md` — *Markov equivalence; CPDAG as honest output; expert knowledge mathematically necessary.*
- **Chapter 8 — Estimating Effects** — `chapters/2026-05-01-chapter-8-estimating-effects.md` — *Pricing-team cold open; backdoor criterion in operation; double machine learning; causal forests; heterogeneous treatment effects.*
- **Chapter 9 — The Counterfactual** — `chapters/2026-05-01-chapter-9-the-counterfactual.md` — *Board-chair retrospective; abduction-action-prediction worked through; individual-level counterfactual; necessary vs sufficient causes.*
- **Chapter 10 — Confounders, Colliders, and the Limits of Observational Data** — `chapters/2026-05-01-chapter-10-confounders-colliders-and-the-limits.md` — *HRT reversal cold open; unconfoundedness assumption; latent confounders; sensitivity analysis as the honest response.*
- **Chapter 11 — Treatments** — `chapters/2026-05-01-chapter-11-treatments.md` — *Duflo's economist-as-plumber; why randomization works; SUTVA and what breaks it; spillover and clinical-to-organizational translation.*
- **Chapter 12 — The Plumber's Objection** — `chapters/2026-05-01-chapter-12-the-plumbers-objection.md` — *Tangier piped-water 10%-vs-69% take-up cold open; Duflo's scientist/engineer/plumber framework; what fills the gap (administrative friction, defaults, incentive architectures, behavioral biases, institutional inertia); Ne-FMS as principal worked example; corporate B2B SaaS plumbing case; three implications for Living Model architecture.*

## Finalized

*Chapters Nik has approved.*

## Killed

*Chapters removed from the book's plan, with a one-line note on why.*
