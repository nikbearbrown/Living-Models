# Enrichment + Cleanup Log

Run: 2026-05-04 — living-models

## What changed

### Build infrastructure added at the book root

`bash build.sh` now produces both `output/living-models.epub` and `output/living-models.html`. EPUB chapter splits land cleanly on all 23 H1s (frontmatter, intro, 20 content chapters, back matter).

Files added: `metadata.yaml`, `styles/kindle.css`, `styles/kindle-book.css`, `build.sh` (executable).

### Pass 3 — 20 portrait stubs inserted

Wayback Machine sections were authored in a prior pass with all subjects already validated against the no-post-2000-alive rule. This pass added the spec-format portrait stubs (alt text + italic caption, `images/{slug}.jpg` path) between each section's contextualizing paragraph and its `**Run this:**` block.

| Ch | Subject | Era |
|---|---|---|
| 1 | John Snow (1813–1858) | c. 1850s |
| 2 | Trygve Haavelmo (1911–1999) | c. 1950s |
| 3 | Konrad Zuse (1910–1995) | c. 1940s |
| 4 | Frank Knight (1885–1972) | c. 1930s |
| 5 | Karl Pearson (1857–1936) | c. 1890s |
| 6 | Sewall Wright (1889–1988) | c. 1920s |
| 7 | Bertrand Russell (1872–1970) | c. 1910s |
| 8 | Gertrude Cox (1900–1978) | c. 1940s |
| 9 | Charles Sanders Peirce (1839–1914) | c. 1890s |
| 10 | Jerome Cornfield (1912–1979) | c. 1960s |
| 11 | Janet Lane-Claypon (1877–1967) | c. 1920s |
| 12 | Esther Boserup (1910–1999) | c. 1960s |
| 13 | Kenneth Boulding (1910–1993) | c. 1950s |
| 14 | Michael Polanyi (1891–1976) | c. 1950s |
| 15 | Amos Tversky (1937–1996) | c. 1980s |
| 16 | Margaret Mead (1901–1978) | c. 1930s |
| 17 | Bruno de Finetti (1906–1985) | c. 1950s |
| 18 | Prasanta Chandra Mahalanobis (1893–1972) | c. 1950s |
| 19 | Marie Neurath (1898–1986) | c. 1940s |
| 20 | Gregory Bateson (1904–1980) | c. 1960s |

None overlap the existing botspeak / branding-and-ai / computational-skepticism-for-ai Wayback rosters.

### Pass 1 — 28 tables rendered

Distribution: Ch 1 (3), Ch 3 (3), Ch 4 (2), Ch 6 (1), Ch 8 (1), Ch 9 (3), Ch 11 (3), Ch 12 (2), Ch 14 (3), Ch 15 (2), Ch 18 (2), Ch 19 (3). Each table populated from the comment description plus chapter context: $P(Y \mid X)$ vs. $P(Y \mid do(X))$ comparison (Ch 1), the 3×3 latency audit (Ch 3), the heat-map collapse register (Ch 4), the abduction-action-prediction worked counterfactual (Ch 9), the SUTVA / JTPA audit (Ch 11), six-barrier KEBN diagnostic (Ch 14), kind-vs-wicked elicitation posture (Ch 15), the knapsack variants (Ch 18), the recommendation quality rubric and narration must-do/must-never (Ch 19).

## Per-chapter results

00-frontmatter.md — 0 tables, 0 figures, no Wayback (front matter)
00-introduction.md — 0 tables, 0 figures, no Wayback (intro)
01-the-dashboard-that-lied.md — 3 tables, 0 figures, Wayback: stub inserted (John Snow)
02-the-map-that-doesnt-move.md — 0 tables, 0 figures, Wayback: stub inserted (Trygve Haavelmo)
03-what-we-mean-when-we-say-realtime.md — 3 tables, 0 figures, Wayback: stub inserted (Konrad Zuse)
04-risk-is-two-numbers-not-one.md — 2 tables, 0 figures, Wayback: stub inserted (Frank Knight)
05-pearls-ladder.md — 0 tables, 0 figures, Wayback: stub inserted (Karl Pearson)
06-graphs-that-think.md — 1 table, 0 figures, Wayback: stub inserted (Sewall Wright)
07-the-equivalence-problem.md — 0 tables, 0 figures, Wayback: stub inserted (Bertrand Russell)
08-estimating-effects.md — 1 table, 0 figures, Wayback: stub inserted (Gertrude Cox)
09-the-counterfactual.md — 3 tables, 0 figures, Wayback: stub inserted (Charles Sanders Peirce)
10-confounders-colliders-and-the-limits-of-observational-data.md — 0 tables, 0 figures, Wayback: stub inserted (Jerome Cornfield)
11-treatments.md — 3 tables, 0 figures, Wayback: stub inserted (Janet Lane-Claypon)
12-the-plumbers-objection.md — 2 tables, 0 figures, Wayback: stub inserted (Esther Boserup)
13-the-living-model-defined.md — 0 tables, 0 figures, Wayback: stub inserted (Kenneth Boulding)
14-the-expert-in-the-room.md — 3 tables, 0 figures, Wayback: stub inserted (Michael Polanyi)
15-how-experts-get-causation-wrong.md — 2 tables, 0 figures, Wayback: stub inserted (Amos Tversky)
16-the-machine-that-interviews-the-expert.md — 0 tables, 0 figures, Wayback: stub inserted (Margaret Mead)
17-resolving-the-graph.md — 0 tables, 0 figures, Wayback: stub inserted (Bruno de Finetti)
18-from-graph-to-decision.md — 2 tables, 0 figures, Wayback: stub inserted (Prasanta Chandra Mahalanobis)
19-the-causal-brain-executive-report.md — 3 tables, 0 figures, Wayback: stub inserted (Marie Neurath)
20-keeping-the-model-alive.md — 0 tables, 0 figures, Wayback: stub inserted (Gregory Bateson)
99-back-matter.md — 0 tables, 0 figures, no Wayback (back matter)

## Summary

Total chapters processed: 23
Total tables rendered: 28
Total figures generated (SVG+PNG pairs): 0 *(deferred — see Action items)*
Total Wayback Machine portrait stubs inserted: 20
Total Wayback Machine subject replacements: 0 (subjects authored under the rule already)

## Action items

### 1. Pass 2 — 56 IMAGE/FIGURE/DIAGRAM figures (deferred)

The book has 56 `<!-- → [IMAGE: ... ] -->`, `<!-- → [FIGURE: ... ] -->`, and `<!-- → [DIAGRAM: ... ] -->` comments distributed across 13 chapters. Concentration: Ch 17 (11), Ch 11 (7), Ch 14 (6), Ch 4 (6), Ch 3 (5), Ch 19 (3), Ch 12 (3), Ch 1 (3), Ch 6 (4), Ch 8 (2), Ch 9 (2), Ch 15 (2), Ch 18 (2). Chapter prose currently references zero-byte `.jpg` placeholders for these figures — they will render as broken images in the EPUB until generated.

### 2. Generate 20 Wayback portrait .jpg files

The Wayback Machine sections reference these AI-redrawn portrait files (none currently on disk):

`john-snow.jpg`, `trygve-haavelmo.jpg`, `konrad-zuse.jpg`, `frank-knight.jpg`, `karl-pearson.jpg`, `sewall-wright.jpg`, `bertrand-russell.jpg`, `gertrude-cox.jpg`, `charles-sanders-peirce.jpg`, `jerome-cornfield.jpg`, `janet-lane-claypon.jpg`, `esther-boserup.jpg`, `kenneth-boulding.jpg`, `michael-polanyi.jpg`, `amos-tversky.jpg`, `margaret-mead.jpg`, `bruno-de-finetti.jpg`, `prasanta-chandra-mahalanobis.jpg`, `marie-neurath.jpg`, `gregory-bateson.jpg`.

### 3. Add a cover image

`build.sh` looks for `cover.jpg` at the book root for KDP upload (1600×2560 JPEG).

### 4. INFOGRAPHIC / CHART comments out of literal Pass-2 scope

The book has 4 `[INFOGRAPHIC: ... ]` and 13 `[CHART: ... ]` comments — out of scope per the spec's literal Pass-2 token list. Chapters 1, 3, 4, 8, 11, 12, 14, 17, 18, 19 carry them. If the intent is to render these too, expand the token list and re-run.

## Build commands

```
cd books/living-models
./build.sh
```

Outputs land in `output/`: `living-models.epub`, `living-models.html`, and `combined.md` (archival concatenated source).
