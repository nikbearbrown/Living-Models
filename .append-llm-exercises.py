#!/usr/bin/env python3
"""Append the LLM Exercise block for the Causal Brain for One Decision project
to the bottom of each of the 20 content chapters in living-models/chapters/.
"""
from pathlib import Path

ROOT = Path(__file__).parent
CH = ROOT / "chapters"

# Each entry: (filename, chapter_number, chapter_title_short, what_youre_building, tool, prompt, what_produces, claude_code_note, claude_project_note, connection_back, preview_next)

EXERCISES = [
    # ---- Chapter 1 ----
    (
        "01-the-dashboard-that-lied.md",
        "1",
        "The Dashboard That Lied",
        "The decision you will spend the next twenty chapters building a Living Model for, classified on Pearl's Ladder with the silent-failure risk named.",
        "Claude Project",
        """I'm starting a project that will run across the next twenty chapters of *Living Models* by Nik Bear Brown. The book teaches the architecture of a *Living Model* — an analytical system that is causal, counterfactual, continually updated, and treatment-oriented — and the running project is to build one for a single consequential decision from my own world.

Help me set up Chapter 1's deliverable. I will paste my candidate decision below; if I haven't yet, ask me for it.

The chapter introduces:
- **Pearl's Ladder of Causation**: Rung 1 (association — *what tends to co-occur?*), Rung 2 (intervention — *what happens if we act?*), Rung 3 (counterfactual — *what would have happened if we'd acted differently?*).
- **Silent failure**: an analytical system that produces outputs indistinguishable from accurate reporting while measuring something systematically different from what users believe.
- **Observational vs. interventional distribution**: $P(Y \\mid X)$ vs. $P(Y \\mid do(X))$.

Produce four things, in this order:

1. **The decision, written precisely.** One paragraph. Name the actor, the action, the timing, the magnitude. Bad: "should we change pricing?" Good: "should the European enterprise tier price increase 12% in Q1 2026?"

2. **Pearl's Ladder classification.** Which rung does this decision require? Justify in two sentences. Identify what rung the data and reporting around this decision currently lives on.

3. **The silent-failure risk.** What is the most plausible way that a confidently-wrong answer could ship without anyone noticing? Be specific about which dashboard or model would produce the false confidence and which decision would propagate the error.

4. **A one-line stake statement.** "If this decision is wrong, the cost is roughly ___ in ___ within ___ months." A number you would defend in a meeting.

Format the output as a markdown document I can save as `01-decision-frame.md`. Be honest about uncertainty in the stake estimate — give a range, not a point.""",
        "A markdown document `01-decision-frame.md` containing your decision in precise form, its Pearl's Ladder classification, the silent-failure risk you most fear, and a defensible stake estimate. This document is the seed — every subsequent chapter's exercise refines it.",
        "If you'd rather build this as code from the start, ask Claude Code to scaffold a `living-model/` project folder with `decisions/01-decision-frame.md` and a `README.md` that names the project. Future chapters will populate `graph/`, `parameters/`, `counterfactuals/`, `report/`, and `ops/`.",
        "Create a Claude Project named *Living Model — [your decision]*. Put the four-property definition (causal / counterfactual / continually updated / treatment-oriented) in the system prompt, plus the rule: *every output must be saved as a file the project accumulates.* Each subsequent chapter's exercise becomes a new conversation in this project.",
        "First chapter — no prior exercise to build on. The decision you choose here governs every subsequent exercise; pick something you actually care about and have some access to data for.",
        "Chapter 2 takes the same decision and asks what a conventional predictive model would recommend — and which divergence mechanism (drift, covariate shift, intervention) would make that recommendation wrong.",
    ),

    # ---- Chapter 2 ----
    (
        "02-the-map-that-doesnt-move.md",
        "2",
        "The Map That Doesn't Move",
        "A diagnostic on what a conventional predictive model would say about your decision, and which of the three divergence mechanisms (concept drift, covariate shift, deployment-time intervention) would make that prediction wrong.",
        "Claude Project",
        """I'm working on a Living Model for the decision named in `01-decision-frame.md` (paste it below if not in the project context).

The book argues that predictive models trained on historical data answer the wrong question for any decision that *intervenes* on the system being predicted. The same data can be consistent with multiple causal structures; the model picks one and silently commits to it. There are three mechanisms by which the deployment world diverges from the training world:

- **Concept drift**: the data-generating mechanism itself has changed.
- **Covariate shift**: the input distribution has changed, but the mechanism is stable.
- **Intervention**: someone is acting on the system in a way that severs a relationship visible in historical data.

Produce a four-section diagnostic markdown document `02-predictive-diagnosis.md`:

1. **The conventional predictive answer.** In 3–5 sentences, describe what a competent analyst with access to historical data — but no causal apparatus — would recommend for this decision. Be charitable; assume the analyst is sharp. The point is not to mock the predictive answer; it is to show what it gets right and what it cannot see.

2. **The divergence diagnosis.** Of the three mechanisms above, which one most plausibly invalidates the conventional answer for this specific decision? One paragraph. Name the variable whose relationship will be severed by the intervention, and the historical correlation that will mislead the predictive model.

3. **The three diagnostic questions** from the chapter, asked of *your* decision:
   - Will deploying this intervention sever a relationship that was load-bearing in the training data?
   - Is there a confounder in the historical data that is about to be controlled-for in deployment, breaking the historical correlation?
   - Is there a feedback loop in the deployment environment that the training data did not contain?
   Answer each in 2–4 sentences with specifics.

4. **The do-statement.** Translate your decision into the formal $P(Y \\mid do(X))$ form. Name $Y$ (the outcome that matters), $X$ (the variable being intervened on), and the contrast: what value of $X$ is *do*-set, against what alternative.

Be specific. Place-holder claims like "the model could be wrong" are not the diagnosis. Name the variable, the relationship, the mechanism.""",
        "A markdown document `02-predictive-diagnosis.md` that names what a non-causal answer would recommend, names the divergence mechanism that breaks it, and writes your decision in formal $P(Y \\mid do(X))$ form.",
        "Not the right tool for this exercise — this chapter is about diagnosis, not code. Stay in chat.",
        "Append `02-predictive-diagnosis.md` to the project's running file collection. The do-statement at the end becomes the canonical formal version of your decision for every later chapter.",
        "Chapter 1 produced the decision; this chapter explains why answering it from historical data alone will fail.",
        "Chapter 3 audits any *real-time* claim your decision currently rests on — across the three latencies (data, model, decision) and the three layers (technical, organizational, epistemic).",
    ),

    # ---- Chapter 3 ----
    (
        "03-what-we-mean-when-we-say-realtime.md",
        "3",
        "What We Mean When We Say \"Real-Time\"",
        "A three-latency × three-layer audit of any \"real-time\" or \"continually updated\" claim that currently informs your decision — locating the binding bottleneck.",
        "Claude Project",
        """I'm working on a Living Model for the decision named in `01-decision-frame.md`. Pull it from the project context if available.

The chapter decomposes \"real-time\" into three independent latencies — *data latency* (time from event to dataset), *model latency* (time from updated dataset to updated model output), *decision latency* (time from updated output to acted-on decision). It also names three audit layers — technical (the pipeline), organizational (who is allowed to act on what), epistemic (whether the data still measures what it used to measure).

Produce `03-realtime-audit.md` with two parts:

**Part 1 — Inventory.** List every \"real-time\" or \"continually updated\" claim that currently informs the decision in `01-decision-frame.md`. For each, name the source (dashboard, model, report, executive summary) and quote the language used (\"real-time\", \"daily-refreshed\", \"live\").

**Part 2 — Audit.** For each claim, fill in this 3×3 table:

|                        | Technical layer | Organizational layer | Epistemic layer |
|------------------------|-----------------|----------------------|-----------------|
| **Data latency**       | actual minutes / hours / days from event to row in the dataset | who has authority to act on data this fresh | does the data still measure the construct it measured a year ago? |
| **Model latency**      | how often is the model re-trained / re-scored | who has authority to deploy a re-trained model | does the model's target variable still track the decision-relevant outcome? |
| **Decision latency**   | how long from updated output to acted-on decision | who is the named approver between output and action | by the time the decision is made, has the world moved past it? |

Fill in real numbers and named roles where possible. Use \"unknown — would need to ask [role]\" where you don't yet have the answer.

**Part 3 — The binding bottleneck.** Of the nine cells, which one is the binding constraint for *your* decision? Most often the answer is in the organizational or epistemic column even when the technical column gets all the attention. One paragraph; name the cell, name the consequence.

Close with one sentence the executive sponsor would have to say in writing for the binding bottleneck to be addressed.""",
        "A markdown document `03-realtime-audit.md` containing an inventory of \"real-time\" claims, a 3×3 audit grid, the binding bottleneck identified, and the one sentence required to address it.",
        "Not needed.",
        "Append `03-realtime-audit.md`. The binding-bottleneck finding becomes a constraint that the Living Model design (Chs 13–20) must accommodate or replace.",
        "Chapters 1–2 named the decision and showed that historical data alone cannot answer it. This chapter shows that *current* data is also weaker than the team likely thinks.",
        "Chapter 4 reframes risk as two numbers (probability × impact) and computes the first Expected Value of Intervention for your decision.",
    ),

    # ---- Chapter 4 ----
    (
        "04-risk-is-two-numbers-not-one.md",
        "4",
        "Risk Is Two Numbers, Not One",
        "Your first Expected Value of Intervention (EVI) estimate for the candidate action — with probability and impact kept as separate numbers, plus the distribution that the heat-map collapse would have destroyed.",
        "Claude",
        """I'm working through Chapter 4 of *Living Models*. The chapter argues that every standard risk framework collapses two independent numbers — probability and impact — into one. The collapse destroys information the decision requires.

My decision is in `01-decision-frame.md` (paste the do-statement and the stake estimate here if not in context).

Produce `04-evi-first-pass.md` with four parts:

1. **Decompose the candidate intervention into outcome scenarios.** List 4–7 outcomes that could plausibly result from acting on the decision. For each, give:
   - The outcome in one sentence (be specific — "revenue rises 8%" not "things go well")
   - A probability (your best honest number — calibrate it as a 90% confidence range, then take the midpoint)
   - An impact in dollars (or the unit native to your decision: lives, customers, headcount, runway days)
   The probabilities should sum to ≈ 1. The impacts should be signed (positive = good, negative = bad).

2. **Compute EVI.** Show the arithmetic: $\\text{EVI} = \\sum_i P_i \\times I_i$. Be explicit about the unit. Don't round prematurely.

3. **Compute the same scenario through the conventional heat-map collapse.** Map each scenario to a Low/Medium/High probability bucket and a Low/Medium/High impact bucket, then read the score off a 5×5 matrix. State the heat-map answer in one word (\"medium risk\", \"high risk\").

4. **What the heat map destroyed.** One paragraph. What did the collapse hide that the EVI revealed? Look specifically for: (a) a low-probability tail with catastrophic impact that the heat map averaged into a midrange score; (b) a high-probability moderate gain that the heat map flattened into the same cell as a low-probability moderate gain.

Close with one sentence: *Given EVI = X, the action is / is not justified relative to the alternative of doing nothing.*

Be honest about uncertainty in your probabilities. The exercise is not to produce defensible numbers — it is to produce numbers that stay honest about being uncertain.""",
        "A markdown document `04-evi-first-pass.md` containing the scenario decomposition, the computed EVI, the heat-map collapse for comparison, and an explicit statement of what the collapse destroyed.",
        "Optional — if the scenarios are large enough that you want a script that runs Monte Carlo over the probability ranges, ask Claude Code to scaffold one in `parameters/04-evi-mc.py`.",
        "Save `04-evi-first-pass.md` to the project. The EVI you compute here is a *first pass* — the parameter estimation in Chapter 8 and the counterfactual in Chapter 9 will refine the impact estimates substantially.",
        "Chapter 1 named a stake estimate; this chapter produces a structured version that the rest of the book will refine.",
        "Chapter 5 starts Part Two — the formal apparatus. You will translate your decision into a Pearl's Ladder framing that distinguishes what the data answers from what the decision requires.",
    ),

    # ---- Chapter 5 ----
    (
        "05-pearls-ladder.md",
        "5",
        "Pearl's Ladder",
        "A precise Rung 1 / Rung 2 / Rung 3 framing of your decision, with the bridging causal assumption named — the one assumption that, if true, lets you climb from observation to intervention.",
        "Claude Project",
        """I'm working through Chapter 5 of *Living Models*. The chapter establishes that Pearl's Ladder has three rungs (association, intervention, counterfactual) and that the rungs are *sealed* — observational data alone cannot answer interventional questions. Climbing from Rung 1 to Rung 2 requires a structural assumption.

My decision is in `01-decision-frame.md` and the diagnostic is in `02-predictive-diagnosis.md`.

Produce `05-ladder-framing.md` with five parts:

1. **The Rung 1 question your data can answer.** One sentence. The form is *what is the conditional distribution of $Y$ given $X$?* Specify $Y$ and $X$ and the conditioning set. Example: \"What is the conditional retention rate of enterprise customers, given the price tier they were on, controlling for company size and industry?\"

2. **The Rung 2 question your decision actually requires.** One sentence. The form is *what is $P(Y \\mid do(X))$?* Specify the intervention contrast — the value $X$ is set to vs. the alternative.

3. **The Rung 3 question that would change your mind, if you could answer it.** One sentence. The form is *given that we did $X$ and observed $Y$, what would $Y$ have been if we had done $X'$ instead?* This is the question a post-incident audit will ask.

4. **The bridging assumption.** What one structural claim, if true, would license going from Rung 1 to Rung 2 for *your* decision? Examples of valid claims: \"all common causes of $X$ and $Y$ are observed\"; \"a randomized rollout is feasible\"; \"the intervention does not interact with units of analysis\". Name it specifically. Then state the consequence if the assumption is false.

5. **The instrument check.** For each rung, name what tool from the book's apparatus (chapters 6–11) you would expect to use:
   - Rung 1 → which estimator?
   - Rung 2 → which identification strategy (backdoor adjustment, IV, RCT)?
   - Rung 3 → which counterfactual procedure (abduction-action-prediction)?

Save the file in the project. Be specific. \"My data is observational\" is not the Rung 1 question; it's a property of the data.""",
        "A markdown document `05-ladder-framing.md` containing your three-rung framing, the bridging assumption, and the instrument check that names which subsequent-chapter machinery you'll need.",
        "Not needed.",
        "Save to the project — the bridging assumption named here is the central claim the rest of Part Two will test (Ch 8 estimates under it, Ch 10 stress-tests it, Ch 11 designs the experiment that would replace it).",
        "Chapter 4's EVI was computed at Rung 1 — the impact estimates assumed the historical correlations would survive the intervention. This chapter exposes that as the assumption it is.",
        "Chapter 6 turns the bridging assumption into a drawn artifact: your first DAG, with mechanism arrows that the assumption either supports or violates.",
    ),

    # ---- Chapter 6 ----
    (
        "06-graphs-that-think.md",
        "6",
        "Graphs That Think",
        "A v0 directed acyclic graph (DAG) and structural causal model (SCM) for your decision, with each arrow labeled with the mechanism it represents.",
        "Claude Project",
        """I'm working through Chapter 6 of *Living Models*. The chapter introduces DAGs as maps of mechanism: each arrow represents a direct causal effect, each missing arrow represents the absence of one. An SCM augments the DAG with structural equations specifying how each variable is determined from its parents plus an exogenous noise term.

I want to draft a v0 DAG for my decision (see `01-decision-frame.md` and `05-ladder-framing.md`).

Produce `06-dag-v0.md` containing:

1. **Variable list.** 6–12 variables, one per line. For each: a short name (snake_case), a one-line definition, and whether it is *observable* (you have data on it), *measurable but not measured* (you could collect it but currently don't), or *latent* (you cannot directly measure it). Include $X$ (the intervention), $Y$ (the outcome), and the candidate confounders / mediators / colliders you suspect.

2. **The DAG, in Mermaid syntax.** Use the form `X --> Y` for direct causal arrows. Annotate each arrow with a one-phrase mechanism in `||...||` brackets. Example:
   ```
   pricing_tier -->|sets willingness to pay threshold| churn_risk
   company_size -->|drives both pricing tier and churn baseline| pricing_tier
   company_size --> churn_risk
   ```

3. **The structural equations.** For each non-exogenous variable $V$, write its structural equation in the form $V = f_V(\\text{parents}(V), U_V)$. Use plain function notation — e.g., `churn_risk = f(pricing_tier, company_size, industry, U_churn)`. You don't yet have the parameters; you have the mechanism.

4. **Confounder / mediator / collider census.** For each pair (treatment, outcome), list which variables are which:
   - **Confounders** of $X$ on $Y$: variables that cause both
   - **Mediators** on the path $X \\to Y$: variables on the causal path
   - **Colliders** on backdoor paths: variables caused by both $X$ and $Y$ (or descendants thereof)

5. **What the DAG commits you to.** Three to five claims the DAG makes that someone disagreeing with you could falsify by running an experiment. Example: \"Industry does not directly affect pricing tier, only through company size.\"

Save to the project. This is v0 — Chapter 7 will show you what the equivalence class looks like and which arrows you've chosen that the data alone cannot defend.""",
        "A markdown document `06-dag-v0.md` containing your variable list, a Mermaid-syntax DAG, the structural equations, the confounder/mediator/collider census, and the falsifiable commitments your DAG makes.",
        "If you want the Mermaid rendered, run `mmdc -i 06-dag-v0.md -o graph/v0.png`. Set up a `graph/` directory in the project folder; subsequent chapters will version successive DAGs there.",
        "Save in the project. From here forward, every chapter that touches the graph references this v0 file by version. After Chapter 17 the graph becomes `graph/validated.md`.",
        "Chapters 1–5 named the decision and the framing; Chapter 6 turns it into a structural object the rest of the apparatus can operate on.",
        "Chapter 7 reveals what the DAG looks like as an *equivalence class* — which arrows you committed to that the data alone could not have determined, and which therefore depend on your domain knowledge being right.",
    ),

    # ---- Chapter 7 ----
    (
        "07-the-equivalence-problem.md",
        "7",
        "The Equivalence Problem",
        "The CPDAG view of your v0 graph — which edges the data has determined, which edges depend on your domain knowledge, and what would change your mind about each undirected edge.",
        "Claude",
        """I'm working through Chapter 7 of *Living Models*. The chapter establishes that any DAG belongs to a *Markov equivalence class* — a set of DAGs that the same observational data cannot distinguish. The class is represented as a CPDAG (Completed Partially Directed Acyclic Graph): edges the data has determined are directed; edges within the equivalence class are undirected.

My v0 DAG is in `06-dag-v0.md`.

Produce `07-cpdag-and-expert-load.md` containing:

1. **Walk through each edge in your v0 DAG.** For each `A → B` arrow, ask:
   - Is this orientation forced by *temporal precedence* (A unambiguously happens before B)?
   - Is this orientation forced by *interventional data* (you have an experiment that breaks the symmetry)?
   - Is this orientation a *domain-knowledge claim* you are making that the observational data alone could not determine?

   Mark each edge as **D** (data-determined), **T** (temporally forced), **K** (domain-knowledge / expert).

2. **Render the CPDAG.** Convert each K-marked edge to *undirected* (`A — B`). The result is the CPDAG: what the data alone constrains. Render in Mermaid syntax.

3. **Count the expert load.** How many edges depend on your domain knowledge? This is the surface area of your model that an expert disagreement could reorient.

4. **Pick the riskiest K-edge.** Of the K-marked edges, which one would do the most damage if its orientation is wrong? \"Riskiest\" = (a) the edge whose reversal would change the deconfounding set most dramatically, or (b) the edge with the weakest domain-knowledge support. Write a paragraph naming the edge and explaining why.

5. **The intervention design.** For the riskiest K-edge, design — in 2–3 sentences — the experiment that would break the equivalence and *force* its orientation. \"If we randomized $X$, we would see the conditional independence $A \\perp B \\mid Z$ if our orientation is right and $A \\not\\perp B \\mid Z$ if reversed.\"

Save to the project. The K-edge count from this exercise is the load that Chapters 14–17 (the elicitation chapters) have to handle.""",
        "A markdown document `07-cpdag-and-expert-load.md` containing the per-edge classification, the CPDAG, the expert-load count, the riskiest K-edge, and the experiment that would resolve it.",
        "Not needed.",
        "Save to the project. The K-edge count is a key quantity — Chapter 14 will ask you to compare this number against the elicitation budget that traditional KEBN engagements assume.",
        "Chapter 6's v0 DAG was a confident structural claim; Chapter 7 surfaces what about that claim is data-determined and what is your domain knowledge speaking.",
        "Chapter 8 takes the data-determined edges and turns them into quantified causal effects using the backdoor criterion plus double machine learning.",
    ),

    # ---- Chapter 8 ----
    (
        "08-estimating-effects.md",
        "8",
        "Estimating Effects",
        "A first quantified estimate of the causal effect $E[Y \\mid do(X)]$ for your decision — with the deconfounding set identified by the backdoor criterion and the estimator chosen for your data shape.",
        "Claude Code",
        """I'm working through Chapter 8 of *Living Models*. The chapter establishes the **backdoor criterion** for identifying a sufficient deconfounding set, and shows how to estimate average and conditional treatment effects via **double machine learning** (DML) and **causal forests** for heterogeneity.

My DAG is in `06-dag-v0.md` and the CPDAG in `07-cpdag-and-expert-load.md`. My data is at `[describe the dataset path or schema]`.

Scaffold a Python script `parameters/08-estimate-effect.py` that does the following:

1. **Loads the data.** Assume tidy CSV or Parquet at the path I describe. Validate column names match the DAG's variable list.

2. **Identifies the backdoor adjustment set.** Given the DAG (encode it as a `networkx.DiGraph`), find a minimal set $Z$ such that (a) $Z$ blocks all backdoor paths from the treatment $X$ to outcome $Y$, and (b) $Z$ contains no descendants of $X$. Use `dowhy` or `causalnex` if available; otherwise hand-roll the path-blocking logic.

3. **Estimates the average causal effect (ACE).** Use **DoubleML** (the `doubleml` Python package) with `RandomForestRegressor` for both nuisance functions. Print the point estimate, standard error, and 95% confidence interval.

4. **Estimates heterogeneous effects (CATE).** Fit a **causal forest** via `econml.dml.CausalForestDML`. Plot the CATE distribution. Identify the top-decile and bottom-decile subpopulations defined by their CATE.

5. **Reports orthogonality and overlap diagnostics.** Plot the propensity-score distribution and flag if any region has propensity below 0.05 or above 0.95 (positivity violation).

6. **Saves results.** Write `parameters/08-effect-estimate.md` containing: the deconfounding set, the ACE with CI, the CATE summary, the diagnostic plots' file paths, and a one-paragraph interpretation that explicitly notes the assumption made (no unmeasured confounders within the identified set).

Make the script run with `python parameters/08-estimate-effect.py --config decisions/01-decision-frame.md`.

If the data isn't yet available, scaffold the script anyway and add a synthetic-data generator that respects the SCM in `06-dag-v0.md` — so the pipeline runs end-to-end on placeholder data and is ready when the real data arrives.""",
        "A runnable script `parameters/08-estimate-effect.py` plus the results file `parameters/08-effect-estimate.md` containing the ACE, CATE distribution, and overlap diagnostics. The first quantified causal estimate in the project.",
        "This is the right tool — Claude Code can scaffold the dependency tree, the synthetic-data generator, and the diagnostic plotting in one pass. Use the `--ide vscode` flag if you want it to open the result.",
        "Append `08-effect-estimate.md` to the project's running deliverables. The ACE estimated here is the *Rung-1-via-bridging-assumption* number that Chapters 10–12 will stress-test.",
        "Chapter 6 named the variables and arrows; Chapter 7 distinguished what the data determines from what your domain knowledge claims; Chapter 8 takes those claims as given and produces a number.",
        "Chapter 9 takes the same SCM and runs the abduction-action-prediction procedure on a *single specific past case* — answering the counterfactual question your post-incident audit will eventually ask.",
    ),

    # ---- Chapter 9 ----
    (
        "09-the-counterfactual.md",
        "9",
        "The Counterfactual",
        "A counterfactual answer for one specific past case in your decision's history — *what would have happened if we had done X' instead of X?* — produced via Pearl's abduction-action-prediction procedure.",
        "Claude Code",
        """I'm working through Chapter 9 of *Living Models*. The chapter introduces Pearl's **abduction-action-prediction** procedure — the formal method for computing individual-level counterfactuals from a structural causal model.

The procedure has three steps:
1. **Abduction.** Given an observed case (with known $X$, $Y$, and observed covariates), use the SCM's structural equations to back out the values of the exogenous noise terms $U$ that *must* have produced the observed outcome.
2. **Action.** Modify the SCM by replacing the structural equation for $X$ with $X = x'$ (the counterfactual treatment).
3. **Prediction.** Run the modified SCM forward, with the recovered noise terms held fixed, to compute $Y_{x'}$ — the counterfactual outcome.

My SCM is in `06-dag-v0.md` and the parameter estimates are in `parameters/08-effect-estimate.md`.

Pick **one specific past case** from your decision's history — a customer, a quarter, a product launch, a patient episode. Something where you know what happened.

Scaffold `counterfactuals/09-aap-case.py`:

1. Load the parameterized SCM (use `pyro.distributions` or `networkx`-plus-handwritten functions, whichever you prefer).
2. Implement `abduction(observed_case, scm)` that returns the inferred noise vector $U$.
3. Implement `action(scm, intervention)` that returns the modified SCM with the treatment fixed.
4. Implement `prediction(modified_scm, U)` that returns $Y_{x'}$.
5. Run the procedure on the chosen past case for two contrasts: the actual treatment vs. the most plausible alternative.
6. Compute and print:
   - **Probability of necessity (PN)**: $P(Y_{X=0} = 0 \\mid X=1, Y=1)$ — the probability that the outcome would not have occurred but for the action.
   - **Probability of sufficiency (PS)**: $P(Y_{X=1} = 1 \\mid X=0, Y=0)$ — the probability that the action would have produced the outcome in a case where it didn't occur.
7. Save `counterfactuals/09-aap-result.md` containing the case description, the actual outcome, the counterfactual outcome, the PN and PS values, and a one-paragraph interpretation.

If there's no real past case yet, simulate one from the SCM with realistic parameter values and label it explicitly as a synthetic example.""",
        "A script `counterfactuals/09-aap-case.py` plus a results file `counterfactuals/09-aap-result.md` containing one fully worked individual-level counterfactual with PN and PS. This is the first Rung 3 artifact in the project.",
        "This is the right tool — implementing abduction-action-prediction cleanly is a small but precise programming exercise. Claude Code can also generate a `tests/` folder that validates the implementation against the worked example in the chapter.",
        "Append `09-aap-result.md` to the project. The PN and PS computed here become the central inputs to the *Counterfactual* section of the four-part executive report in Chapter 19.",
        "Chapter 8 produced an *average* effect; Chapter 9 produces an *individual-level* counterfactual that an audit can rerun on any specific case.",
        "Chapter 10 stress-tests the unconfoundedness assumption that Chapter 8's estimate and Chapter 9's counterfactual both rest on — by computing the E-value and naming the latent confounder that would overturn the result.",
    ),

    # ---- Chapter 10 ----
    (
        "10-confounders-colliders-and-the-limits-of-observational-data.md",
        "10",
        "Confounders, Colliders, and the Limits of Observational Data",
        "A sensitivity analysis (E-value) for your headline causal estimate plus a named-and-defended list of plausible latent confounders — the honest account of what observational inference cannot rule out.",
        "Claude",
        """I'm working through Chapter 10 of *Living Models*. The chapter argues that the **unconfoundedness assumption** — that all common causes of treatment and outcome are measured — cannot be tested from observational data alone. The honest move is **sensitivity analysis**: how strong would an unmeasured confounder have to be to overturn the conclusion?

My estimates are in `parameters/08-effect-estimate.md`.

Produce `parameters/10-sensitivity.md` containing:

1. **The unconfoundedness statement, made specific.** Restate the unconfoundedness assumption *for your specific decision*. Replace the abstract \"all common causes are measured\" with: \"All variables that influence both [treatment] and [outcome] are among $\\{Z_1, Z_2, ..., Z_k\\}$.\" Name your $Z$'s.

2. **The E-value.** Compute the **E-value** for the headline causal estimate from Chapter 8. The E-value is the minimum strength of association (on the risk-ratio scale) that an unmeasured confounder would need with both treatment and outcome to fully explain away the observed effect. Use the formula in VanderWeele & Ding (2017): for a risk ratio RR > 1, $E = RR + \\sqrt{RR(RR-1)}$. Show the arithmetic.

3. **Three plausible latent confounders.** Brainstorm three structural-but-unmeasured variables that could plausibly affect both treatment and outcome in your case. Examples for a pricing decision: *latent customer financial stress*, *competitive activity that wasn't logged*, *sales-team enthusiasm during the rollout*. For each:
   - Name the confounder
   - Argue why it's plausible (one paragraph)
   - Estimate, qualitatively, how strong its association would need to be with treatment and outcome to overturn the conclusion. Compare to the E-value.

4. **The collider check.** Look at the conditioning set $Z$ from Chapter 8. Are any of those variables descendants of either treatment or outcome? Conditioning on a collider opens a backdoor path that was previously closed. If you find one, propose the corrected adjustment set.

5. **The honest conclusion.** One paragraph. Given the E-value and the plausibility of the listed confounders, how much should the executive trust the estimate? Choose your verb deliberately: *the data is consistent with*, *the estimate suggests*, *the evidence is weak*, *the result is robust to confounders weaker than X*.

Save to the project. The E-value here is a number that goes into the *Assumptions* section of the executive report (Ch 19).""",
        "A markdown document `parameters/10-sensitivity.md` containing the unconfoundedness statement, the E-value with arithmetic, three named latent confounders with plausibility arguments, the collider check, and an honest conclusion paragraph.",
        "Not needed for the analysis itself — but if you want the E-value computed for several point estimates simultaneously, ask Claude Code to add an `e-value()` function to your `parameters/` module.",
        "Append to the project. The E-value and the named confounders both become inputs to Chapter 19's *Assumptions* section.",
        "Chapter 8 produced the estimate as if unconfoundedness held; Chapter 10 prices the assumption.",
        "Chapter 11 designs the experiment that would *replace* the unconfoundedness assumption with randomization — and audits SUTVA.",
    ),

    # ---- Chapter 11 ----
    (
        "11-treatments.md",
        "11",
        "Treatments",
        "An experimental design — RCT, cluster-randomized rollout, or encouragement design — that would resolve the residual confounding, with an explicit SUTVA audit identifying which violations your deployment context creates.",
        "Claude",
        """I'm working through Chapter 11 of *Living Models*. The chapter argues that randomization establishes causation where observational methods cannot, and introduces **SUTVA** — the Stable Unit Treatment Value Assumption — which has two components:
- **No interference**: one unit's treatment status doesn't affect another unit's outcome
- **No hidden variations of treatment**: the treatment is the same thing everywhere it's applied

The chapter also catalogs design alternatives when SUTVA fails: cluster randomization, time-staggered rollout, encouragement design.

My decision is in `01-decision-frame.md` and the sensitivity finding is in `parameters/10-sensitivity.md`.

Produce `experiment/11-design.md` containing:

1. **The naive RCT design.** Describe the simplest possible randomized trial of your decision: unit of randomization, sample size, randomization mechanism, primary outcome, follow-up window. Be specific about numbers.

2. **The SUTVA audit.** For each of the two SUTVA components, ask:
   - **No interference.** Could one unit's treatment status affect another unit's outcome? Look for: customers talking to each other (consumer markets), employees discussing rollouts (organizational interventions), competitors observing prices (market interventions), patients in the same ward (clinical trials).
   - **No hidden variations.** Is \"the treatment\" actually the same thing everywhere it's applied? Look for: a training delivered through different instructors, a price change applied through different contract terms, a feature behind a feature flag with different fallback behavior across cohorts.

   For each component, write either *holds* (with one sentence of justification) or *violated* (with one paragraph of detail).

3. **The corrected design.** If SUTVA holds, the naive RCT is the design. If it doesn't:
   - **Interference** → cluster-randomize at the level above the interfering unit (district, store, cohort, ward).
   - **Hidden variations** → standardize the treatment, or randomize the variation as a second factor, or run the experiment within one variation only and label the result accordingly.
   - **Compliance heterogeneity** → encouragement design with intent-to-treat as the primary estimand.
   Specify the corrected design with the same level of detail as the naive design.

4. **The expected effect size and power.** Given the ACE and CATE estimates from Chapter 8, what sample size would your design need to detect a 50%-of-ACE effect at 80% power, alpha = 0.05? Use the standard formula or `statsmodels.stats.power`.

5. **What the trial result would and would not guarantee.** One paragraph. Even a well-run RCT estimates an *intent-to-treat* effect under your specific deployment conditions. Name two things the trial would not tell you (long-term effect, off-population effect, mechanism).

Save to the project.""",
        "A markdown document `experiment/11-design.md` containing the naive RCT, the SUTVA audit, the corrected design, the power calculation, and the honest list of what the trial would and would not establish.",
        "Optional — if you want the power calculation as a runnable function with sensitivity to effect-size assumptions, ask Claude Code to add `experiment/11-power.py`.",
        "Append to the project. This experimental design becomes the *Recommended evidence-strengthening action* in the Chapter 19 report.",
        "Chapter 10 named the residual confounders that observational methods couldn't rule out; Chapter 11 designs the experiment that would replace the unconfoundedness assumption with randomization.",
        "Chapter 12 takes the *clean* causal estimate (whether observational or experimental) and addresses the gap between a correct estimate and an effective organizational change — the plumber's problem.",
    ),

    # ---- Chapter 12 ----
    (
        "12-the-plumbers-objection.md",
        "12",
        "The Plumber's Objection",
        "An implementation plan for the candidate intervention, mapped against Duflo's hassle-cost lens — with the specific friction points that would degrade the estimated effect under deployment named and addressed.",
        "Claude",
        """I'm working through Chapter 12 of *Living Models*. The chapter introduces Duflo's *economist as plumber*: the distance between a correct causal estimate and an effective organizational change is filled with administrative friction, hassle costs, and implementation choices that no estimate captures. The Tangier study showed that removing administrative friction increased take-up sevenfold without changing the intervention's economic terms.

My estimates are in `parameters/08-effect-estimate.md` and the experimental design in `experiment/11-design.md`.

Produce `implementation/12-plumbing.md` containing:

1. **The implementation cascade.** List every step that has to happen between the *decision being made* and *the effect being realized*. Be granular — for a pricing change: legal review, contract template update, billing-system change, sales-team notification, customer communication, customer acceptance, billing cycle, downstream behavior change. Each row.

2. **The hassle-cost census.** For each step in the cascade, identify:
   - **Friction**: forms, approvals, sign-offs, manual steps that introduce delay or non-completion
   - **Take-up risk**: at what step is the most likely place that a unit drops out of the intervention?
   - **Heterogeneous compliance**: are there subgroups for whom this step is harder or easier?

3. **The mechanism preservation question.** Of the things that have to happen for the causal mechanism to operate, which depend on implementation fidelity? Example: a price-change effect depends on the customer *seeing* the new price clearly, not just on the database row updating. If the customer never sees the new price (e.g., they paid annually and won't see a bill for 11 months), the mechanism doesn't fire on schedule.

4. **The redesign.** For the worst friction point, propose a redesign — three to five sentences. The standard moves: default-on instead of default-off, removal of a form, automation of a manual step, integration into an existing workflow rather than a new one. Estimate qualitatively how much the redesign closes the gap between the trial-level effect and the deployment-level effect.

5. **The deployment-adjusted EVI.** Take the EVI from Chapter 4 and the ACE from Chapter 8. Apply your honest take-up multiplier (the fraction of the unit population for whom the intervention will actually fire). Compute the deployment-adjusted EVI. State plainly: *the trial-level effect is X; the deployment-level effect is roughly Y; the gap is closed by [the redesign].*

Save to the project.""",
        "A markdown document `implementation/12-plumbing.md` containing the implementation cascade, the hassle-cost census, the mechanism-preservation diagnosis, the redesign, and the deployment-adjusted EVI.",
        "Not needed.",
        "Append to the project. The deployment-adjusted EVI becomes the figure that goes in the headline recommendation in Chapter 19.",
        "Chapter 11 designed the trial that would produce a clean estimate; Chapter 12 prices the gap between trial and deployment.",
        "Chapter 13 closes Part Two by *defining* the Living Model architecture explicitly — and asking you to score what you've built so far against the four properties.",
    ),

    # ---- Chapter 13 ----
    (
        "13-the-living-model-defined.md",
        "13",
        "The Living Model Defined",
        "A scorecard of what you've built so far against the four Living Model properties (causal / counterfactual / continually updated / treatment-oriented), with a gap analysis identifying which properties Part Three needs to install.",
        "Claude",
        """I'm working through Chapter 13 of *Living Models*. The chapter defines a Living Model by **four properties** — it must be:
1. **Causal** — structured around interventional effects (Rung 2), not correlations
2. **Counterfactual** — capable of Rung 3 reasoning about specific cases
3. **Continually updated** — live link between incoming data and model parameters
4. **Treatment-oriented** — output is a ranked list of interventions evaluated by expected causal effect

My project files so far: `01-decision-frame.md`, `02-predictive-diagnosis.md`, `03-realtime-audit.md`, `04-evi-first-pass.md`, `05-ladder-framing.md`, `06-dag-v0.md`, `07-cpdag-and-expert-load.md`, `parameters/08-effect-estimate.md`, `counterfactuals/09-aap-result.md`, `parameters/10-sensitivity.md`, `experiment/11-design.md`, `implementation/12-plumbing.md`.

Produce `architecture/13-scorecard.md` containing:

1. **The four-property scorecard.** For each property, score what you have so far on a 0–3 scale:
   - 0 = absent
   - 1 = component exists but is not integrated into a runnable system
   - 2 = component is runnable but isolated (not connected to the others)
   - 3 = component is operating in an orchestrated loop with the others

   For each score, name the artifact in your project that supports it.

2. **The orchestration check.** The chapter argues that the four properties have to *operate together* — a system that is causal but not continually updated will silently drift; a system that is treatment-oriented but not counterfactual cannot diagnose its own past recommendations. For each pair of properties, ask: do they currently talk to each other in your project? Where are the broken handoffs?

3. **The gap analysis.** Which property is weakest? Which one is closest to a 3? Where would adding one engineering integration (a daily refresh, a counterfactual rerun, a parameter update) close the biggest gap?

4. **The remaining-chapters map.** Map each remaining chapter (14–20) to the property it most directly improves:
   - Ch 14–17 — elicitation and graph resolution → which property?
   - Ch 18 — graph to decision → which property?
   - Ch 19 — executive report → which property?
   - Ch 20 — keeping the model alive → which property?
   Use this map to set your expectations for the back half of the project.

Save to the project. This is the snapshot you take at the midpoint, before Part Three's architecture work begins.""",
        "A markdown document `architecture/13-scorecard.md` containing the four-property scores, the orchestration check, the gap analysis, and the remaining-chapter map.",
        "Not needed.",
        "Append to the project. The scorecard becomes the *baseline* against which Chapters 14–20 measure their additions.",
        "Chapters 1–12 built the components; Chapter 13 takes inventory of them as a system.",
        "Chapter 14 starts Part Three by introducing **Knowledge Engineering with Bayesian Networks** (KEBN) — the structured-elicitation discipline that addresses the Markov-equivalence problem from Chapter 7 by bringing in expert knowledge.",
    ),

    # ---- Chapter 14 ----
    (
        "14-the-expert-in-the-room.md",
        "14",
        "The Expert in the Room",
        "An elicitation plan for resolving the K-edges in your CPDAG (from Chapter 7) — including a candidate expert, a chosen protocol (Delphi or IDEA), and a session structure that fits inside two working hours.",
        "Claude",
        """I'm working through Chapter 14 of *Living Models*. The chapter argues that domain experts are *mathematically required* for causal model construction — Markov equivalence (Chapter 7) means the data alone cannot distinguish multiple DAGs, and the expert is the resolution mechanism. The chapter introduces:

- **KEBN** (Knowledge Engineering with Bayesian Networks): a 20-year-old discipline for structured elicitation
- **Delphi** protocol: anonymous, multiple rounds, used to suppress conformity and dominance bias
- **IDEA** protocol: Investigate–Discuss–Estimate–Aggregate; reduces overconfidence

My CPDAG and K-edges are in `07-cpdag-and-expert-load.md`.

Produce `elicitation/14-plan.md` containing:

1. **The candidate expert.** Name one specific person (real, in your network or accessible). Why them? — domain depth, decision context, willingness to commit two hours. If you cannot name a real person, name the *role* and the criteria you'd use to find them.

2. **The protocol choice.** Delphi or IDEA? Justify based on:
   - **Delphi** if the K-edges are mostly about *factual structural claims* and you have multiple plausible experts who shouldn't influence each other before the elicitation.
   - **IDEA** if the K-edges are mostly about *parameter ranges* (effect sizes, conditional probabilities) where overconfidence is the main risk.
   You can pick a hybrid — Delphi for the structure, IDEA for the parameters.

3. **The variable list to elicit.** Do not present the whole DAG to the expert at once. Pick the 6–10 variables most directly involved in the K-edges. List them with one-line definitions calibrated for the expert's vocabulary, not yours.

4. **The 90-minute session structure.** Allocate the time:
   - Frame the decision and the variables (10 min)
   - Variable refinement — does anything missing, is anything redundant? (15 min)
   - Edge elicitation on the K-edges, one at a time (40 min)
   - Equivalence-resolution probes — *if X were intervened on, would Y change?* (15 min)
   - Calibration — the expert states how confident they are, and where they would expect to be wrong (10 min)

5. **The barriers you anticipate.** The chapter names six structural barriers keeping KEBN out of corporate settings. Pick the two most likely to apply to your context (time, methodological skepticism, confidentiality, etc.) and write one sentence each on how you'll address them.

Save to the project.""",
        "A markdown document `elicitation/14-plan.md` containing the named expert, the protocol choice, the variable list, the 90-minute session agenda, and the anticipated barriers.",
        "Not needed.",
        "Save to the project. This plan is what Chapter 16's LLM-guided interview will *operationalize* — the same elicitation, run by an LLM-driven multi-agent system in 45 minutes instead of two hours.",
        "Chapter 7 surfaced the K-edges that depend on expert knowledge; Chapter 14 plans how to actually elicit that knowledge from a real human.",
        "Chapter 15 prepares you to *interrogate* the expert — the cognitive failures you should expect (collider blindness, feedback-loop simplification) and how to design probes that surface them.",
    ),

    # ---- Chapter 15 ----
    (
        "15-how-experts-get-causation-wrong.md",
        "15",
        "How Experts Get Causation Wrong",
        "A bias-stress-test of your v0 DAG against the four common cognitive failures (collider blindness, feedback-loop simplification, domain-matching heuristics, anchoring), with corrected probes added to your elicitation plan.",
        "Claude",
        """I'm working through Chapter 15 of *Living Models*. The chapter catalogs cognitive failures common in expert causal elicitation:
- **Collider blindness** — experts often miss that conditioning on a collider opens a path that was closed
- **Feedback-loop simplification** — bidirectional mechanisms get arbitrarily flattened into one direction
- **Domain-matching heuristic** — experts orient edges based on which variable \"feels more important,\" not on the mechanism
- **Anchoring** — early answers in the session over-constrain later ones

My DAG is in `06-dag-v0.md` and the elicitation plan is in `elicitation/14-plan.md`.

Produce `elicitation/15-bias-probes.md` containing:

1. **Stress-test your own v0 DAG.** Read `06-dag-v0.md` against each of the four failures:
   - **Collider check.** For each variable, ask: are *two of its ancestors* connected through it but not through any other path? If so, you have a collider. Name any colliders you find. Did you accidentally condition on one?
   - **Feedback-loop check.** For each arrow $A \\to B$, ask: is there a plausible backward effect $B \\to A$ (e.g., revenue affects pricing, *and* pricing affects revenue)? If so, the DAG is hiding a cycle. Name the simplification you made and the time-resolution at which it might be defensible (\"weekly\" vs. \"annually\").
   - **Domain-matching check.** For each arrow, ask: did I orient this because of *mechanism* or because of *importance*? Importance reasoning typically points the arrow from \"big\" to \"small\" — that's a heuristic, not a mechanism.
   - **Anchoring check.** Which arrow in your DAG was the *first* one you drew? Are later arrows oriented in a way that's consistent with that first commitment but possibly wrong because of it?

2. **The corrected DAG, v0.5.** Update your v0 DAG to fix any failures found above. Render in Mermaid syntax. List the changes made and the rationale.

3. **Probes for the elicitation session.** For each of the four failures, write one specific probe question to ask your expert during the Chapter 14 session:
   - **Collider probe**: \"If we filtered to only [collider] = high cases, would the relationship between [parent A] and [parent B] still hold?\"
   - **Feedback probe**: \"Over what time scale would you expect [effect] to feed back into [cause]?\"
   - **Domain-matching probe**: \"What would have to be true for [arrow] to run the other direction?\"
   - **Anchoring probe**: \"If we hadn't started with [variable], how would you have organized this picture?\"

   Insert each probe at the right point in the 90-minute agenda from Chapter 14.

4. **Your own anchoring confession.** One paragraph. Where in your v0 DAG were you most influenced by the first reading you did? What might you have committed to that an expert with no anchor would not?

Save to the project. The probes get used in Chapter 16's LLM interview as well as in any human elicitation.""",
        "A markdown document `elicitation/15-bias-probes.md` containing the four-failure stress-test, the corrected DAG v0.5 in Mermaid, the four probe questions inserted into the elicitation agenda, and your own anchoring confession.",
        "Not needed.",
        "Save to the project. The probes from this exercise are inputs to the Chapter 16 multi-agent interview design — specifically the *Bias-Watch* agent role.",
        "Chapter 14 planned the session; Chapter 15 prepares you to recognize when the expert (or you) is making a predictable cognitive error.",
        "Chapter 16 is the engineering specification: an LLM-guided multi-agent interview that runs the elicitation in 45 minutes instead of two hours, with the bias probes built into the *Bias-Watch* agent.",
    ),

    # ---- Chapter 16 ----
    (
        "16-the-machine-that-interviews-the-expert.md",
        "16",
        "The Machine That Interviews the Expert",
        "A working LLM-guided causal-interview agent — built in Cowork — that runs the four-phase elicitation (variable identification, edge elicitation, equivalence resolution, confidence calibration) on a real expert in 45 minutes.",
        "Cowork",
        """I'm working through Chapter 16 of *Living Models*. The chapter specifies a multi-agent LLM elicitation system with four roles:
- **Interviewer**: asks the questions, paces the session
- **Consistency**: tracks contradictions across answers and surfaces them
- **Equivalence**: detects when an answer doesn't resolve a Markov-equivalence ambiguity and prompts for clarification
- **Bias-Watch**: triggers the probes from Chapter 15 when the expert exhibits collider blindness, feedback simplification, anchoring, or domain matching

My elicitation plan is in `elicitation/14-plan.md` and the bias probes are in `elicitation/15-bias-probes.md`.

In **Cowork**, build the interview agent. Produce `elicitation/16-interview-system/` containing:

1. **`system-prompt.md`** — the master prompt for the Interviewer agent. It should:
   - Open with the project context: what decision the expert is helping with, what the K-edges are
   - State the four phases: variable identification, edge elicitation, equivalence resolution, confidence calibration
   - Include the temporal-precedence substitution: *which of these typically happens first?* as a soft proxy for orientation
   - End each phase with a check: *let me read back what we have; does this feel right?*

2. **`consistency-check.md`** — the prompt for the Consistency agent. It runs after every answer and asks:
   *Does this answer contradict any prior commitment? If so, surface the contradiction to the Interviewer before the next question.*

3. **`equivalence-check.md`** — the prompt for the Equivalence agent. It runs after every edge orientation and asks:
   *Is this orientation forced by the answer given, or is the orientation still observationally ambiguous? If ambiguous, prompt for the temporal-precedence question.*

4. **`bias-watch.md`** — the prompt for the Bias-Watch agent. It loads the four probes from `elicitation/15-bias-probes.md` and triggers them when patterns match.

5. **`run-interview.md`** — a Cowork instructions file that orchestrates: open with the Interviewer, run Consistency and Equivalence after every answer, run Bias-Watch when triggered, save the transcript to `elicitation/16-transcript.md`, save the resulting CPDAG (with the K-edges now resolved or flagged) to `elicitation/16-resolved-cpdag.md`.

Run the interview on your expert (or on yourself, as a dry run, before you bring in the real expert). The 45-minute target is real — if the system runs over, it's a sign one of the agents is over-prompting.

Save the transcript and the resolved CPDAG.""",
        "A working multi-agent interview system in `elicitation/16-interview-system/`, plus the transcript and resolved CPDAG from running it. The K-edges from Chapter 7 should now be either oriented (with the expert's reasoning attached) or flagged as still-ambiguous.",
        "Optional — if you want the orchestration as standalone code rather than Cowork instructions, ask Claude Code to scaffold a Python harness that calls Anthropic's API for each agent role. The Cowork version is simpler and runs in the browser.",
        "This exercise *is* a Claude Project use case in disguise — the four agent prompts are the system prompt, and each interview turn is one message. Cowork is the recommended packaging because it handles the file I/O for the transcript and the CPDAG.",
        "Chapters 14–15 planned and stress-tested the elicitation; Chapter 16 builds the system that runs it.",
        "Chapter 17 takes the resolved CPDAG and runs the discovery algorithms (PC, GES, NOTEARS, FCI) against your data — and resolves the inevitable conflicts between expert opinion and algorithmic output.",
    ),

    # ---- Chapter 17 ----
    (
        "17-resolving-the-graph.md",
        "17",
        "Resolving the Graph",
        "The validated DAG — produced by running causal-discovery algorithms (PC, GES, NOTEARS, FCI) against your data, comparing the algorithmic output to the expert-resolved CPDAG, and applying the three-step conflict-resolution protocol to commit a final graph under version control.",
        "Claude Code",
        """I'm working through Chapter 17 of *Living Models*. The chapter introduces four families of causal-discovery algorithms:
- **PC** (Peter–Clark): constraint-based, returns a CPDAG, assumes no latent confounders
- **GES** (Greedy Equivalence Search): score-based, returns a CPDAG, also assumes no latent confounders
- **NOTEARS**: continuous optimization, returns a fully directed DAG, scales to many variables but requires functional-form assumptions
- **FCI** (Fast Causal Inference): handles latent confounders, returns a PAG (Partial Ancestral Graph), more conservative

The chapter also specifies a three-step conflict-resolution protocol when expert and algorithm disagree:
1. Determine whether the disagreement is data-resolvable (more data could settle it) or assumption-driven (the algorithm assumes something the expert disputes)
2. If data-resolvable: gather more data or run a targeted intervention
3. If assumption-driven: surface the disputed assumption explicitly and decide which side bears the burden of proof

My resolved CPDAG from the expert interview is in `elicitation/16-resolved-cpdag.md` and my data is at `[describe path]`.

Scaffold `discovery/17-resolve.py` that does the following:

1. **Load the data and the expert CPDAG.**
2. **Run all four algorithms.** Use `causal-learn` (PC, GES, FCI) and `notears` (NOTEARS) Python packages. Save each algorithm's output graph to `discovery/17-{alg}-output.json`.
3. **Compute the agreement matrix.** For each edge in the expert CPDAG, classify the algorithmic vote as: all agree, majority agree, split, all disagree. Write `discovery/17-agreement-matrix.md` with one row per edge.
4. **Surface the conflicts.** For each edge where the expert and the algorithmic majority disagree, run the three-step resolution protocol:
   - Is this data-resolvable? Compute the conditional independence test in question; check if the test power is adequate (Type II risk under your sample size).
   - If assumption-driven, which assumption — linearity, no latent confounders, faithfulness — is in dispute?
   - Apply the protocol's tie-breakers and record the decision.
5. **Commit the validated graph.** Save the final DAG to `graph/validated.json` (machine-readable) and `graph/validated.md` (Mermaid + provenance — for each edge, who/what oriented it). Initialize a `graph/` directory under `git` so successive validated graphs are versioned.
6. **Record the governance metadata.** In `graph/validated.md`, record: the version number, the date, the expert(s) consulted, the data snapshot used, the re-elicitation trigger conditions (what would force re-running this whole pipeline).

Make the script run with `python discovery/17-resolve.py --data [path] --expert-cpdag elicitation/16-resolved-cpdag.md --out graph/validated.json`.""",
        "A runnable script `discovery/17-resolve.py`, an agreement matrix, conflict-resolution decisions, and the committed validated graph in `graph/validated.json` plus `graph/validated.md`. The graph is now under version control and ready for parameterization.",
        "This is the right tool — running four algorithms, computing agreement matrices, and version-controlling the output graph is exactly the kind of multi-step work Claude Code excels at. Use the `--watch` flag to keep the script running as you iterate on the conflict-resolution decisions.",
        "Append the validated graph artifacts to the project. From here forward, *the graph* refers to `graph/validated.md`. Future versions go in `graph/v2.md`, `graph/v3.md`, etc., with `git log` as the change record.",
        "Chapter 16 produced the expert's CPDAG; Chapter 17 reconciles it with what the algorithms find in the data and produces the artifact every later chapter operates on.",
        "Chapter 18 parameterizes the validated graph, runs counterfactuals, ranks interventions by Expected Value, and solves the budget-constrained knapsack from rankings to a portfolio recommendation.",
    ),

    # ---- Chapter 18 ----
    (
        "18-from-graph-to-decision.md",
        "18",
        "From Graph to Decision",
        "A parameterized SCM, a counterfactual rerun for the original decision, an EV-ranked intervention list, and the budget-constrained portfolio recommendation — the analytical output of the Living Model.",
        "Claude Code",
        """I'm working through Chapter 18 of *Living Models*. The chapter covers four moves:
1. **Parameterize the validated graph** — fit the structural equations from the data
2. **Run counterfactual queries** — for the original decision, *what would have happened under each alternative?*
3. **Rank candidate interventions by Expected Value** — using the parameterized SCM to predict $E[Y \\mid do(X = x_i)]$ for each candidate $x_i$
4. **Solve the budget-constrained knapsack** — pick the highest-EV portfolio of interventions subject to a budget and dependency constraints

My validated graph is in `graph/validated.json`, the data is at `[path]`, and the EVI from Chapter 4 / deployment-adjusted EVI from Chapter 12 are in the project.

Scaffold `decision/18-rank-and-portfolio.py`:

1. **Parameterize.** Load `graph/validated.json` and the data. For each node, fit the structural equation. Use the simplest functional form that the data supports (linear with interactions for continuous, logistic for binary, multinomial for categorical) and report goodness of fit. Save the parameterized SCM to `decision/18-scm-parameters.json`.

2. **Counterfactual rerun.** Take the original decision case from Chapter 9. Re-run abduction-action-prediction against the validated graph (rather than the v0 graph). Compare PN and PS to the Chapter 9 values. If they differ substantially, write one paragraph naming the structural change between v0 and `validated` that drove the difference.

3. **Generate the candidate intervention list.** Enumerate 5–15 interventions in the space around the original decision. Examples for a pricing decision: not just \"raise 12%\" but also \"raise 6%\", \"raise 18%\", \"raise 12% on tier A only\", \"raise 12% with grandfathered exception\", \"reduce 6% with bundled feature add-on\". For each, specify: the do-operation, the cost (in money or political capital), the dependencies (interventions that must precede it), and the eligibility constraints.

4. **Compute EV for each intervention.** For each candidate $x_i$, compute $E[Y \\mid do(X = x_i)]$ from the parameterized SCM. Multiply by the deployment-adjustment factor from Chapter 12. Generate a confidence interval via bootstrap. Save to `decision/18-ev-ranked.csv`.

5. **Solve the knapsack.** Given a budget $B$ and the dependency / eligibility constraints, find the subset of interventions that maximizes total EV. Use ILP if available (`pulp` or `scipy.optimize.milp`); fall back to a greedy heuristic with exchange moves if not. Save to `decision/18-portfolio.md`.

6. **Sensitivity check.** For the recommended portfolio, vary the headline parameter (the largest causal coefficient in the SCM) by ±20% and check whether the portfolio composition changes. Report the result.

7. **Save the recommendation as the executive-report draft input.** Write `decision/18-recommendation.md` containing: the top-ranked single intervention, the recommended portfolio, the EV with CI, the sensitivity-check result, and the assumptions the recommendation rests on (carry forward from Chapter 10).""",
        "A runnable script `decision/18-rank-and-portfolio.py`, a parameterized SCM (`decision/18-scm-parameters.json`), the EV-ranked CSV, the portfolio markdown, and a recommendation draft (`decision/18-recommendation.md`) ready for the executive report in Chapter 19.",
        "This is the right tool — parameter fitting, counterfactual rerun, EV ranking, and the knapsack solver are all standard but multi-step. Claude Code can also generate a Streamlit dashboard for the recommendation if you want one.",
        "Append everything to the project. The `decision/18-recommendation.md` is the input to Chapter 19's four-part executive report.",
        "Chapter 17 committed the validated graph; Chapter 18 turns it into the analytical recommendation.",
        "Chapter 19 takes the analytical recommendation and assembles it into the four-part Causal Brain Executive Report — *Recommendation, Evidence, Assumptions, Counterfactual* — with LLM narration that obeys the must-do and must-never-do rules.",
    ),

    # ---- Chapter 19 ----
    (
        "19-the-causal-brain-executive-report.md",
        "19",
        "The Causal Brain Executive Report",
        "The four-part executive report — *Recommendation, Evidence, Assumptions, Counterfactual* — produced from your Living Model's structured output, with LLM-narrated text evaluated against the must-do and must-never-do rules and decision-focused visualizations.",
        "Cowork",
        """I'm working through Chapter 19 of *Living Models*. The chapter specifies the executive report's four parts:
1. **Recommendation** — what to do, named, sized, and timed; the alternative; the case for choosing the recommended action
2. **Evidence** — which causal variables drove the recommendation; confidence indicator on each (data-grounded vs. expert-anchored)
3. **Assumptions** — what would have to be true for the recommendation to be wrong (drawn from the sensitivity analysis in Chapter 10 and the bridging assumption in Chapter 5)
4. **Counterfactual** — for the most recent past comparable case, what the model would have recommended

The chapter also specifies LLM narration rules:
- **Must do:** quantify uncertainty, name the alternative, attribute every claim to a model output
- **Must never do:** invent claims the model did not make, apologize for uncertainty rather than report it, hide assumptions in subordinate clauses

In **Cowork**, build `report/19-executive-report.md` containing:

**Section 1 — Recommendation (max 1 page).** Pull from `decision/18-recommendation.md`. State the recommended action specifically — actor, action, magnitude, timing. State the alternative the model considered next. State the EV difference between recommended and alternative, with confidence interval. Two short paragraphs of LLM-narrated rationale, referenced to model outputs by file path.

**Section 2 — Evidence (max 1 page).** Pull from `parameters/08-effect-estimate.md` and `graph/validated.md`. Name the 3–5 causal variables most responsible for the EV ranking. For each, mark the source: *data-grounded* (parameter from data with N and CI), *expert-anchored* (orientation from elicitation, with expert name and session date), or *mixed*. Include one decision-focused visualization — a tornado plot of variable importance, or a forest plot of CATE by subpopulation, or the validated graph with the active causal pathway highlighted. (Generate the plot in Python; embed.)

**Section 3 — Assumptions (max 1 page).** Pull from `parameters/10-sensitivity.md`. State the bridging assumption from Chapter 5 plainly. State the E-value for the headline estimate. State the three plausible latent confounders with the qualitative comparison to the E-value. End with: *the recommendation reverses if [specific named confounder] turns out to be associated with both treatment and outcome at strength greater than [number]*.

**Section 4 — Counterfactual (max 1 page).** Pull from `counterfactuals/09-aap-result.md`. Pick the most recent past case comparable to the current decision. State what the model would have recommended at that time, given the parameterized SCM available now. Compare to what was actually done. If the model would have made the same recommendation, say so. If it would have differed, name the difference and explain. This section is the auditable provenance — it lets a future review check whether the model is self-consistent.

**LLM narration audit.** After Cowork generates the narration, re-run it through a critique pass:
- For each sentence in the report, confirm it is grounded in a model output cited by file path.
- Flag any sentence that softens uncertainty (\"likely\", \"probably\" without a number).
- Flag any sentence that invents a claim — anything the model files do not directly support.

**Named-owner block.** End the report with: *This recommendation is owned by [name], dated [date]. The audit record for this recommendation is at [path]. The Living Model that produced it is at version [tag] of `graph/validated.md`.*""",
        "A four-part executive report in `report/19-executive-report.md`, with LLM-audited narration, named-owner accountability, and decision-focused visualizations. This is the central deliverable of the entire project.",
        "Optional — if you want the report rendered as a one-page PDF for board distribution, ask Claude Code to add a Pandoc step that produces `report/19-executive-report.pdf` with the visualizations embedded.",
        "Cowork is the right tool — it can read your scattered project files (`decision/`, `parameters/`, `counterfactuals/`, `graph/`) and assemble the report from them in one pass. The LLM narration audit can also run inside the same Cowork session.",
        "Every prior chapter contributed components; Chapter 19 assembles them into the artifact the executive sees.",
        "Chapter 20 specifies the DecisionOps maintenance plan — the drift detector, the re-elicitation triggers, and the minimum viable feedback loop that keeps this report's recommendations honest as the world changes.",
    ),

    # ---- Chapter 20 ----
    (
        "20-keeping-the-model-alive.md",
        "20",
        "Keeping the Model Alive",
        "The DecisionOps maintenance plan — drift detector, structural-change trigger, re-elicitation cadence, and the minimum viable feedback loop that closes the orchestration loop and keeps your Living Model honest after deployment.",
        "Claude Code",
        """I'm working through Chapter 20 of *Living Models*. The chapter distinguishes three modes of model decay:
- **Parametric drift** — edge coefficients shift while the graph structure holds; addressed by Bayesian parameter updating
- **Structural drift** — the graph itself becomes wrong; addressed by re-elicitation triggers
- **Mechanism failure** — a previously dominant mechanism is no longer load-bearing; addressed by mechanism review

It introduces **DecisionOps** as distinct from MLOps: the primary artifact is the *recommendation*, not the model; the integration point is the *executive review*, not the prediction API.

It specifies a four-stage minimum viable feedback loop:
1. The recommendation is logged with its inputs, parameters, assumptions, and counterfactual baseline
2. The actual outcome is recorded when it occurs
3. The realized outcome is compared to the recommendation's expected outcome
4. The discrepancy is routed: parametric drift → param update; structural drift → re-elicitation; mechanism failure → mechanism review

My validated graph is at `graph/validated.json`, the parameterized SCM at `decision/18-scm-parameters.json`, and the report at `report/19-executive-report.md`.

Scaffold `ops/20-decisionops.py` and `ops/20-runbook.md`:

**`ops/20-decisionops.py`:**

1. **Recommendation logger.** A function that, given the report metadata, writes a structured row to `ops/recommendation-log.csv`: timestamp, recommendation ID, recommended action, EV with CI, assumption hash, parameter version, expected outcome value with timing.

2. **Outcome recorder.** A function that, given a recommendation ID and the realized outcome, writes to `ops/outcome-log.csv`. Allows manual entry; no automatic system can know when a strategic decision's effect has \"realized\".

3. **Drift detector.** A function that, on a schedule, recomputes the headline parameters on the latest data window and compares to the saved version. Flags a parametric drift if any parameter has shifted by more than its 95% CI from the saved value.

4. **Structural-change detector.** A function that re-runs the discovery algorithms from Chapter 17 on the latest data window and compares the output graph to `graph/validated.json` using structural Hamming distance. Flags a structural drift if the distance exceeds a threshold (one or two edge changes).

5. **Bayesian parameter updater.** A function that, given new data, performs Bayesian updating on the SCM parameters using the current values as the prior. Saves the updated SCM to `decision/scm-parameters-v[N+1].json`.

6. **Re-elicitation trigger.** A function that fires when (a) the structural-change detector flags an alert, OR (b) more than 18 months have passed since the last full elicitation, OR (c) more than three parametric drifts have occurred since the last full elicitation. The trigger sends a notification to the named owner.

**`ops/20-runbook.md`:**

A page that, for the named owner, specifies:
- **Daily:** nothing (Living Models are not dashboards)
- **Weekly:** one-line review of the recommendation log; flag anything that seems off
- **Monthly:** review the drift-detector output; if parametric drift, run the updater
- **Quarterly:** review structural-change detector output; if alert, schedule re-elicitation
- **Annually:** full re-elicitation regardless; the world changes faster than 12 months

Wire all of this into a simple cron-style schedule (a `Makefile` or a GitHub Actions workflow).""",
        "A runnable maintenance system in `ops/20-decisionops.py` plus the named-owner runbook in `ops/20-runbook.md`. With this in place, the project moves from a one-time analytical deliverable to a Living Model under operational discipline.",
        "This is the right tool — implementing the loggers, the drift detectors, the Bayesian updater, and the cron schedule is exactly the kind of multi-component build Claude Code is designed for. Use the `--ide vscode` flag to scaffold the whole `ops/` directory in one pass.",
        "Append the ops artifacts to the project. The Claude Project session can serve as the *named owner's* working surface — the place the weekly recommendation-log review and the quarterly structural-change check actually happen.",
        "Chapter 19 produced the recommendation; Chapter 20 keeps it honest after deployment by closing the four-stage feedback loop.",
        "This is the final chapter of the running project. Your deliverable is now a complete Living Model — graph, parameters, counterfactuals, executive report, and the DecisionOps system that keeps it alive. The book's argument is: a Living Model maintained over a decade is the durable competitive advantage; the one-shot analytical deliverable is the project with an expiration date.",
    ),
]


BLOCK_TEMPLATE = """
---

###  LLM Exercise — Chapter {n}: {title}

**Project:** The Causal Brain for One Decision
**What you're building this chapter:** {what}
**Tool:** {tool}

---

**The Prompt:**

```
{prompt}
```

---

**What this produces:** {produces}

**How to adapt this prompt:**

- *For your own project:* Replace the bracketed domain placeholders with your specific decision, dataset, or context. The exercise structure is domain-agnostic; the content is yours.
- *For ChatGPT / Gemini:* Works as-is. For ChatGPT, save the project to a Custom GPT instead of a Claude Project. For Gemini, paste the running project files into the context window each session (Gemini's persistent-context support varies).
- *For Claude Code:* {claude_code}
- *For a Claude Project:* {claude_project}

**Connection to previous chapters:** {back}

**Preview of next chapter:** {next}
"""


def main():
    for entry in EXERCISES:
        filename, n, title, what, tool, prompt, produces, claude_code, claude_project, back, next_ch = entry
        path = CH / filename
        text = path.read_text()
        if "###  LLM Exercise — Chapter" in text:
            print(f"  SKIP (already has LLM Exercise): {filename}")
            continue
        block = BLOCK_TEMPLATE.format(
            n=n, title=title, what=what, tool=tool, prompt=prompt,
            produces=produces, claude_code=claude_code, claude_project=claude_project,
            back=back, next=next_ch,
        )
        new_text = text.rstrip() + "\n" + block + "\n"
        path.write_text(new_text)
        print(f"  appended LLM Exercise to {filename}")


if __name__ == "__main__":
    main()
