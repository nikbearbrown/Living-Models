#!/usr/bin/env python3
"""Pass 3 — insert portrait stubs in all 20 Wayback Machine sections of
living-models/chapters/. Subjects are already validated (all pre-2001 dead OR
foundational pre-2001 work). The insertion goes between the contextualizing
paragraph and the `**Run this:**` block, per the spec.
"""
import re
from pathlib import Path

ROOT = Path(__file__).parent
CH = ROOT / "chapters"

# (filename, full_name, era, source_type, image_type, jpg_filename)
SUBJECTS = [
    ("01-the-dashboard-that-lied.md",                                 "John Snow",                       "c. 1850s",  "photograph", "portrait", "john-snow.jpg"),
    ("02-the-map-that-doesnt-move.md",                                "Trygve Haavelmo",                 "c. 1950s",  "photograph", "portrait", "trygve-haavelmo.jpg"),
    ("03-what-we-mean-when-we-say-realtime.md",                       "Konrad Zuse",                     "c. 1940s",  "photograph", "portrait", "konrad-zuse.jpg"),
    ("04-risk-is-two-numbers-not-one.md",                             "Frank Knight",                    "c. 1930s",  "photograph", "portrait", "frank-knight.jpg"),
    ("05-pearls-ladder.md",                                           "Karl Pearson",                    "c. 1890s",  "photograph", "portrait", "karl-pearson.jpg"),
    ("06-graphs-that-think.md",                                       "Sewall Wright",                   "c. 1920s",  "photograph", "portrait", "sewall-wright.jpg"),
    ("07-the-equivalence-problem.md",                                 "Bertrand Russell",                "c. 1910s",  "photograph", "portrait", "bertrand-russell.jpg"),
    ("08-estimating-effects.md",                                      "Gertrude Cox",                    "c. 1940s",  "photograph", "portrait", "gertrude-cox.jpg"),
    ("09-the-counterfactual.md",                                      "Charles Sanders Peirce",          "c. 1890s",  "photograph", "portrait", "charles-sanders-peirce.jpg"),
    ("10-confounders-colliders-and-the-limits-of-observational-data.md", "Jerome Cornfield",             "c. 1960s",  "photograph", "portrait", "jerome-cornfield.jpg"),
    ("11-treatments.md",                                              "Janet Lane-Claypon",              "c. 1920s",  "photograph", "portrait", "janet-lane-claypon.jpg"),
    ("12-the-plumbers-objection.md",                                  "Esther Boserup",                  "c. 1960s",  "photograph", "portrait", "esther-boserup.jpg"),
    ("13-the-living-model-defined.md",                                "Kenneth Boulding",                "c. 1950s",  "photograph", "portrait", "kenneth-boulding.jpg"),
    ("14-the-expert-in-the-room.md",                                  "Michael Polanyi",                 "c. 1950s",  "photograph", "portrait", "michael-polanyi.jpg"),
    ("15-how-experts-get-causation-wrong.md",                         "Amos Tversky",                    "c. 1980s",  "photograph", "portrait", "amos-tversky.jpg"),
    ("16-the-machine-that-interviews-the-expert.md",                  "Margaret Mead",                   "c. 1930s",  "photograph", "portrait", "margaret-mead.jpg"),
    ("17-resolving-the-graph.md",                                     "Bruno de Finetti",                "c. 1950s",  "photograph", "portrait", "bruno-de-finetti.jpg"),
    ("18-from-graph-to-decision.md",                                  "Prasanta Chandra Mahalanobis",    "c. 1950s",  "photograph", "portrait", "prasanta-chandra-mahalanobis.jpg"),
    ("19-the-causal-brain-executive-report.md",                       "Marie Neurath",                   "c. 1940s",  "photograph", "portrait", "marie-neurath.jpg"),
    ("20-keeping-the-model-alive.md",                                 "Gregory Bateson",                 "c. 1960s",  "photograph", "portrait", "gregory-bateson.jpg"),
]


def insert_stub(filename, name, era, src_type, img_type, jpg_filename):
    path = CH / filename
    text = path.read_text()
    # Find the section header.
    header_idx = text.find("## AI Wayback Machine")
    if header_idx == -1:
        print(f"!!! no Wayback section in {filename}")
        return False
    # Find "**Run this:**" after the header — the contextualizing paragraph ends just before it.
    run_idx = text.find("**Run this:**", header_idx)
    if run_idx == -1:
        print(f"!!! no Run this block in {filename}")
        return False
    # Skip if a portrait stub is already present in the section.
    section_text = text[header_idx:run_idx]
    if re.search(r'!\[' + re.escape(name), section_text):
        print(f"  SKIP (stub already present): {filename}")
        return False
    stub = (
        f"![{name}, {era}. AI-generated {img_type} based on a public domain {src_type} (Wikimedia Commons).]"
        f"(images/{jpg_filename})\n"
        f"*{name}, {era}. AI-generated {img_type} based on a public domain {src_type}.*\n\n"
    )
    # Insert stub before the "**Run this:**" line, with proper spacing.
    before = text[:run_idx].rstrip() + "\n\n" + stub
    after = text[run_idx:]
    path.write_text(before + after)
    print(f"  inserted stub for {name} in {filename}")
    return True


def main():
    inserted = 0
    for entry in SUBJECTS:
        if insert_stub(*entry):
            inserted += 1
    print(f"\ntotal stubs inserted: {inserted}")


if __name__ == "__main__":
    main()
