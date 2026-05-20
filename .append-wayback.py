#!/usr/bin/env python3
"""Append `## AI Wayback Machine` blocks to each of the 20 living-models content
chapters, immediately after the existing LLM Exercise block.
Figures: lesser-known, diverse, pre-2001 dead OR foundational pre-2001 work, none
overlapping the existing botspeak / branding-and-ai / computational-skepticism-for-ai
Wayback lists.
"""
from pathlib import Path

ROOT = Path(__file__).parent
CH = ROOT / "chapters"

# (filename, full_name, framing_one_phrase, chapter_concept, run_prompt, search_term, variant_1, variant_2, variant_3)
ENTRIES = [
    (
        "01-the-dashboard-that-lied.md",
        "John Snow",
        "mapping cholera deaths to street addresses to expose what the prevailing miasma dashboards could not see",
        "the silent failure of an analytical system that confidently reports the wrong thing",
        "Who was John Snow, and how does his 1854 cholera map connect to the chapter's claim that an analytical dashboard can confidently report the wrong thing while every error signal stays silent? Keep it to three paragraphs. End with the single most surprising thing about his career or ideas.",
        "John Snow physician",
        "Ask it to explain *spot-mapping* in plain language, as if you've never read epidemiology",
        "Ask it to compare Snow's Broad Street pump argument to a modern dashboard that conflates association with intervention",
        'Add a constraint: "Answer as if you\'re writing the executive summary of a post-mortem on a silent-failure incident"',
    ),
    (
        "02-the-map-that-doesnt-move.md",
        "Trygve Haavelmo",
        "publishing *The Probability Approach in Econometrics* in 1944 to argue that observational econometric models cannot, by themselves, support claims about deliberate intervention",
        "predictive models breaking under intervention",
        "Who was Trygve Haavelmo, and how does his 1944 distinction between observational fit and intervention-supporting structure connect to why predictive models break when used to recommend deliberate action? Keep it to three paragraphs. End with the single most surprising thing about his career or ideas.",
        "Trygve Haavelmo",
        "Ask it to explain the *autonomy of structural equations* in plain language, as if you've never seen an economic model",
        "Ask it to compare Haavelmo's structural-vs-reduced-form distinction to today's predictive-vs-causal model debate",
        'Add a constraint: "Answer as if you\'re writing the warning label on a forecast that will be used to set policy"',
    ),
    (
        "03-what-we-mean-when-we-say-realtime.md",
        "Konrad Zuse",
        "designing the Z3 in 1941 — the first programmable, fully automatic digital computer — under conditions where every notion of *real-time* had to be invented from scratch",
        "the three latencies hiding inside any 'real-time' claim",
        "Who was Konrad Zuse, and how do the design choices in the Z3 (1941) and the Plankalkül connect to the chapter's argument that *real-time* is three independent latencies — data, model, and decision — not one? Keep it to three paragraphs. End with the single most surprising thing about his career or ideas.",
        "Konrad Zuse",
        "Ask it to explain *Plankalkül* in plain language, as if you've never seen a programming language",
        "Ask it to compare Zuse's hand-built relay timing to the data / model / decision latencies named in this chapter",
        'Add a constraint: "Answer as if you\'re auditing a vendor\'s claim that their system is real-time"',
    ),
    (
        "04-risk-is-two-numbers-not-one.md",
        "Frank Knight",
        "drawing the foundational distinction between *measurable risk* and *Knightian uncertainty* in *Risk, Uncertainty and Profit* (1921)",
        "probability and impact as two independent numbers, not one",
        "Who was Frank Knight, and how does his 1921 distinction between measurable risk and Knightian uncertainty connect to the chapter's argument that collapsing probability and impact into a single risk score destroys the information a decision requires? Keep it to three paragraphs. End with the single most surprising thing about his career or ideas.",
        "Frank Knight economist",
        "Ask it to explain *Knightian uncertainty* in plain language, as if you've never taken an economics course",
        "Ask it to compare Knight's distinction to what a heat-map collapse hides about a tail risk",
        'Add a constraint: "Answer as if you\'re writing the case against COSO ERM-style heat maps for a board"',
    ),
    (
        "05-pearls-ladder.md",
        "Karl Pearson",
        "arguing in *The Grammar of Science* (1892) that *all science is description of association* — the position Pearl's Ladder is, structurally, a refutation of",
        "the categorical distinction between association, intervention, and counterfactual",
        "Who was Karl Pearson, and how does his program — that science consists of describing associations, not mechanisms — connect, by contrast, to Pearl's argument that observational data alone cannot answer interventional questions? Keep it to three paragraphs. End with the single most surprising thing about his career or ideas.",
        "Karl Pearson",
        "Ask it to explain why *correlation is not causation* was once a contested rather than obvious claim, in plain language",
        "Ask it to compare Pearson's correlationist program to Pearl's Rung 1 / Rung 2 distinction",
        'Add a constraint: "Answer as if you\'re writing the historical preface to a chapter on the do-operator"',
    ),
    (
        "06-graphs-that-think.md",
        "Sewall Wright",
        "inventing *path analysis* in 1918 — the diagrammatic method whose path coefficients are the direct ancestor of every directed acyclic graph in this book",
        "DAGs as maps of mechanism",
        "Who was Sewall Wright, and how does his 1918 invention of path analysis — and the long debate it provoked with R. A. Fisher and Karl Pearson — connect to the chapter's argument that a DAG is a map of mechanism, not a picture of correlations? Keep it to three paragraphs. End with the single most surprising thing about his career or ideas.",
        "Sewall Wright",
        "Ask it to explain *path coefficients* in plain language, as if you've only ever seen regression coefficients",
        "Ask it to compare Wright's path diagrams (1918) to the modern DAGs in this chapter",
        'Add a constraint: "Answer as if you\'re writing the rationale for using a DAG instead of a regression equation in a board memo"',
    ),
    (
        "07-the-equivalence-problem.md",
        "Bertrand Russell",
        "arguing in *On the Notion of Cause* (1913) that observational data could not, in principle, distinguish A→B from B→A from a common cause — the philosophical anticipation of what Markov equivalence formalizes",
        "Markov equivalence and the necessity of expert input",
        "Who was Bertrand Russell, and how does his 1913 essay *On the Notion of Cause* — arguing that observation cannot distinguish causal direction from common-cause explanations — connect to the chapter's claim that Markov-equivalence makes expert input mathematically necessary, not merely useful? Keep it to three paragraphs. End with the single most surprising thing about his career or ideas.",
        "Bertrand Russell",
        "Ask it to explain why Russell wanted to *eliminate* the notion of cause from physics, in plain language",
        "Ask it to compare Russell's 1913 critique to the formal Markov-equivalence theorem proved decades later",
        'Add a constraint: "Answer as if you\'re writing the introduction to a chapter on why DAGs require domain experts"',
    ),
    (
        "08-estimating-effects.md",
        "Gertrude Cox",
        "co-authoring *Experimental Designs* (1950, with William Cochran) — the foundational textbook on factorial experiments and adjustment for confounding that the modern backdoor and DML estimators inherit from",
        "the backdoor criterion and the deconfounded effect estimate",
        "Who was Gertrude Cox, and how does her work on experimental design and statistical adjustment connect to the modern apparatus of the backdoor criterion and double machine learning for estimating causal effects from observational data? Keep it to three paragraphs. End with the single most surprising thing about her career or ideas.",
        "Gertrude Cox",
        "Ask it to explain *adjustment for confounding* in plain language, as if you've never run a regression",
        "Ask it to compare Cox's hand-tabulated factorial designs to a modern double-machine-learning pipeline",
        'Add a constraint: "Answer as if you\'re writing the introduction to a chapter on identifying causal effects from observational data"',
    ),
    (
        "09-the-counterfactual.md",
        "Charles Sanders Peirce",
        "naming and developing the inferential move he called *abduction* — the same name Pearl gives to the first step of the abduction-action-prediction procedure",
        "Pearl's abduction-action-prediction procedure for individual-level counterfactuals",
        "Who was Charles Sanders Peirce, and how does his concept of *abduction* — the inference from a surprising observation to the hypothesis that would make it unsurprising — connect to the first step of Pearl's abduction-action-prediction procedure for computing individual-level counterfactuals? Keep it to three paragraphs. End with the single most surprising thing about his career or ideas.",
        "Charles Sanders Peirce",
        "Ask it to explain Peirce's *abduction* in plain language, as if you've never read pragmatist philosophy",
        "Ask it to compare Peirce's three-step inference (abduction, deduction, induction) to Pearl's three-step counterfactual (abduction, action, prediction)",
        'Add a constraint: "Answer as if you\'re writing a footnote in a chapter on the but-for test"',
    ),
    (
        "10-confounders-colliders-and-the-limits-of-observational-data.md",
        "Jerome Cornfield",
        "deriving the bound that bears his name in 1959 — the original sensitivity analysis showing that an unmeasured confounder would have to be implausibly strong to overturn the observed association between smoking and lung cancer",
        "the unconfoundedness assumption and how to bound the influence of latent confounders",
        "Who was Jerome Cornfield, and how does his 1959 sensitivity bound — used to defend the smoking-cancer causal claim against tobacco-industry critics — connect to the chapter's E-value approach for stress-testing causal claims against unmeasured confounders? Keep it to three paragraphs. End with the single most surprising thing about his career or ideas.",
        "Jerome Cornfield",
        "Ask it to explain *the Cornfield bound* in plain language, as if you've never seen a sensitivity analysis",
        "Ask it to compare Cornfield's 1959 reasoning about smoking and lung cancer to a modern E-value computed for a contemporary causal claim",
        'Add a constraint: "Answer as if you\'re writing the assumptions section of a model card"',
    ),
    (
        "11-treatments.md",
        "Janet Lane-Claypon",
        "designing the first modern cohort and case-control studies in the 1910s and 1920s — the experimental templates that the RCT would refine and the SUTVA framework would later formalize",
        "randomized controlled trials and the SUTVA assumption",
        "Who was Janet Lane-Claypon, and how do her early-twentieth-century cohort and case-control study designs connect to the chapter's argument that randomization establishes causation where observational methods cannot — and to the SUTVA assumptions every trial silently makes? Keep it to three paragraphs. End with the single most surprising thing about her career or ideas.",
        "Janet Lane-Claypon",
        "Ask it to explain *case-control design* in plain language, as if you've never seen an epidemiology textbook",
        "Ask it to compare Lane-Claypon's 1926 breast-cancer case-control study to a modern A/B test against the SUTVA criterion",
        'Add a constraint: "Answer as if you\'re writing the design rationale for an organizational intervention trial"',
    ),
    (
        "12-the-plumbers-objection.md",
        "Esther Boserup",
        "documenting in *The Conditions of Agricultural Growth* (1965) how interventions that look correct on paper run aground on the implementation realities of the populations they target",
        "the gap between a correct causal estimate and an effective organizational change",
        "Who was Esther Boserup, and how does her work on agricultural intensification — particularly her insistence on documenting how peasants actually responded to interventions, not how they were modeled to respond — connect to the chapter's argument that a clean causal estimate does not survive contact with the implementation cascade? Keep it to three paragraphs. End with the single most surprising thing about her career or ideas.",
        "Esther Boserup",
        "Ask it to explain *induced intensification* in plain language, as if you've never read development economics",
        "Ask it to compare Boserup's field-level documentation of take-up to the *plumber* discipline this chapter teaches",
        'Add a constraint: "Answer as if you\'re writing the implementation section of a deployment plan"',
    ),
    (
        "13-the-living-model-defined.md",
        "Kenneth Boulding",
        "publishing *General Systems Theory: The Skeleton of Science* in 1956 — the foundational case that a system is defined by the integrated operation of its properties, not by any property in isolation",
        "the four properties of a Living Model operating together as one system",
        "Who was Kenneth Boulding, and how does his 1956 *General Systems Theory* — the argument that systems are defined by integration across levels, not by any single property — connect to the chapter's claim that a Living Model's four properties (causal, counterfactual, continually updated, treatment-oriented) only deliver decision intelligence when they operate together? Keep it to three paragraphs. End with the single most surprising thing about his career or ideas.",
        "Kenneth Boulding",
        "Ask it to explain Boulding's *hierarchy of systems* in plain language, as if you've never read systems theory",
        "Ask it to compare Boulding's integration argument to the orchestrated-outcomes claim in this chapter",
        'Add a constraint: "Answer as if you\'re writing the architectural rationale for why all four Living Model properties have to operate together"',
    ),
    (
        "14-the-expert-in-the-room.md",
        "Michael Polanyi",
        "naming and analyzing *tacit knowledge* in *Personal Knowledge* (1958) — the form of expert knowledge that, by definition, cannot be transferred without a structured elicitation discipline",
        "Knowledge Engineering with Bayesian Networks and the necessity of structured expert elicitation",
        "Who was Michael Polanyi, and how does his concept of *tacit knowledge* — the claim that experts know more than they can articulate — connect to the chapter's argument that causal-graph construction requires structured elicitation protocols (Delphi, IDEA, KEBN), not just an expert in the room? Keep it to three paragraphs. End with the single most surprising thing about his career or ideas.",
        "Michael Polanyi",
        "Ask it to explain *tacit knowledge* in plain language, as if you've never read philosophy of science",
        "Ask it to compare Polanyi's claim that experts know more than they can articulate to the structured probes a KEBN session uses to extract causal claims",
        'Add a constraint: "Answer as if you\'re writing the rationale for the elicitation budget in a Living Model proposal"',
    ),
    (
        "15-how-experts-get-causation-wrong.md",
        "Amos Tversky",
        "co-developing the heuristics-and-biases program with Daniel Kahneman in the 1970s — the foundational catalog of the cognitive failures the chapter's elicitation probes are designed to surface",
        "the cognitive failures (collider blindness, feedback simplification, anchoring) that an expert elicitation has to detect",
        "Who was Amos Tversky, and how does his work with Kahneman on heuristics and biases — anchoring, availability, representativeness — connect to the specific cognitive failures (collider blindness, feedback-loop simplification, domain-matching, anchoring) the chapter teaches you to design probes for? Keep it to three paragraphs. End with the single most surprising thing about his career or ideas.",
        "Amos Tversky",
        "Ask it to explain *the anchoring effect* in plain language, as if you've never seen a behavioral economics paper",
        "Ask it to compare Tversky's general anchoring research to the specific anchoring failure that the first edge in an elicitation imposes on every later edge",
        'Add a constraint: "Answer as if you\'re writing the cognitive-bias-watch agent\'s system prompt"',
    ),
    (
        "16-the-machine-that-interviews-the-expert.md",
        "Margaret Mead",
        "developing structured ethnographic interviewing in *Coming of Age in Samoa* (1928) and the methodological work that followed — the disciplined elicitation of tacit knowledge from a domain expert who is, in this case, a culture",
        "an LLM-guided multi-agent interview that elicits expert causal knowledge in 45 minutes",
        "Who was Margaret Mead, and how does her structured ethnographic interviewing — the disciplined elicitation of cultural knowledge from informants who couldn't articulate it directly — connect to the multi-agent LLM interview architecture (Interviewer, Consistency, Equivalence, Bias-Watch) the chapter specifies? Keep it to three paragraphs. End with the single most surprising thing about her career or ideas.",
        "Margaret Mead",
        "Ask it to explain *participant observation* in plain language, as if you've never read anthropology",
        "Ask it to compare Mead's structured field-interview protocol to the four-agent role split in the chapter",
        'Add a constraint: "Answer as if you\'re writing the system prompt for the Interviewer agent"',
    ),
    (
        "17-resolving-the-graph.md",
        "Bruno de Finetti",
        "founding subjective Bayesianism in the 1930s — the formal account of how a coherent probabilistic agent updates beliefs given evidence, which is exactly what discovery algorithms (PC, GES, NOTEARS, FCI) operationalize",
        "running causal-discovery algorithms on data and reconciling their output with expert structure",
        "Who was Bruno de Finetti, and how does his subjective Bayesian framework — particularly his exchangeability theorem — connect to the chapter's argument that resolving a CPDAG requires reconciling expert priors with data-driven discovery algorithms like PC, GES, and NOTEARS? Keep it to three paragraphs. End with the single most surprising thing about his career or ideas.",
        "Bruno de Finetti",
        "Ask it to explain *exchangeability* in plain language, as if you've never seen a Bayesian textbook",
        "Ask it to compare de Finetti's expert-prior-plus-data framework to the three-step expert-vs-algorithm resolution protocol in this chapter",
        'Add a constraint: "Answer as if you\'re writing the documentation for a CPDAG resolution tool"',
    ),
    (
        "18-from-graph-to-decision.md",
        "Prasanta Chandra Mahalanobis",
        "founding the Indian Statistical Institute in 1931 and using statistical models to drive the 1950s Indian Five-Year Plans — operationalizing a graph-to-decision pipeline at the scale of a national economy",
        "parameterizing the validated graph and ranking interventions by Expected Value under budget constraints",
        "Who was Prasanta Chandra Mahalanobis, and how does his work using statistical-economic models to drive the Indian Five-Year Plans — translating quantified relationships into policy choices under hard resource constraints — connect to the chapter's pipeline from a parameterized causal graph through EV-ranked interventions to a budget-constrained portfolio? Keep it to three paragraphs. End with the single most surprising thing about his career or ideas.",
        "Prasanta Chandra Mahalanobis",
        "Ask it to explain the *Mahalanobis distance* in plain language, as if you've never seen a multivariate statistics textbook",
        "Ask it to compare Mahalanobis's planning-model approach to the modern budget-constrained-knapsack step in this chapter",
        'Add a constraint: "Answer as if you\'re writing the policy memo that accompanies an EV-ranked portfolio"',
    ),
    (
        "19-the-causal-brain-executive-report.md",
        "Marie Neurath",
        "designing the Isotype picture-language for public communication of statistical and policy claims through the 1930s and 1940s — the foundational case that decision-grade visualization is itself a craft, not decoration",
        "the four-part executive report and decision-focused visualization",
        "Who was Marie Neurath, and how does her Isotype work — the disciplined design of statistical visualizations that communicate uncertain quantitative claims to non-specialist audiences — connect to the chapter's must-do / must-never-do rules for decision-focused visualization in a Causal Brain Executive Report? Keep it to three paragraphs. End with the single most surprising thing about her career or ideas.",
        "Marie Neurath",
        "Ask it to explain the *Isotype* approach in plain language, as if you've never read information design",
        "Ask it to compare Neurath's editorial discipline (what to include, what to leave out) to the four-part report structure in this chapter",
        'Add a constraint: "Answer as if you\'re reviewing a draft visualization against the must-never-do list"',
    ),
    (
        "20-keeping-the-model-alive.md",
        "Gregory Bateson",
        "writing *Steps to an Ecology of Mind* (1972) on feedback, learning, and what it takes for a system to remain *alive* — adaptive to a changing environment rather than calcified into the conditions it was built for",
        "DecisionOps: keeping the Living Model adaptive over its operational life",
        "Who was Gregory Bateson, and how does his work on feedback, learning, and *the difference that makes a difference* connect to the chapter's three modes of Living Model decay (parametric drift, structural drift, mechanism failure) and the four-stage feedback loop that keeps the model honest? Keep it to three paragraphs. End with the single most surprising thing about his career or ideas.",
        "Gregory Bateson",
        "Ask it to explain Bateson's *deutero-learning* (learning to learn) in plain language, as if you've never read cybernetics",
        "Ask it to compare Bateson's account of adaptive systems to the DecisionOps disciplines in this chapter",
        'Add a constraint: "Answer as if you\'re writing the on-call runbook for a Living Model that just fired its drift detector"',
    ),
]


BLOCK = """
---

## AI Wayback Machine

The ideas in this chapter didn't appear from nowhere. **{name}** was {framing} decades before most people had heard of {concept}. Here's a prompt to find out more — and then make it better.

**Run this:**

```
{prompt}
```

→ Search **"{search}"** on Wikipedia after you run this. See what the model got right, got wrong, or left out.

**Now make the prompt better.** Try one of these:

- {v1}
- {v2}
- {v3}

What changes? What gets better? What gets worse?
"""


def main():
    seen_names = set()
    for entry in ENTRIES:
        filename, name, framing, concept, prompt, search, v1, v2, v3 = entry
        if name in seen_names:
            print(f"!!! DUPLICATE figure: {name}")
        seen_names.add(name)
        path = CH / filename
        text = path.read_text()
        if "## AI Wayback Machine" in text:
            print(f"  SKIP (already has Wayback): {filename}")
            continue
        # Append after the existing LLM Exercise block — i.e. at end of file.
        block = BLOCK.format(
            name=name, framing=framing, concept=concept,
            prompt=prompt, search=search,
            v1=v1, v2=v2, v3=v3,
        )
        new_text = text.rstrip() + "\n" + block + "\n"
        path.write_text(new_text)
        print(f"  appended Wayback ({name}) to {filename}")
    print(f"\nfigures included: {len(seen_names)} unique")


if __name__ == "__main__":
    main()
