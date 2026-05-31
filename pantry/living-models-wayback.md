# Wayback Image Prompts — Living Models

Text-to-image prompts generated from the AI Wayback Machine sections in `chapters/`.
Each prompt is anchored to the historical figure named in the chapter section.

```python
living_models = [
    # chapters/01-the-dashboard-that-lied.md — John Snow
    "John Snow (circa 1854, British physician and epidemiology pioneer) - Victorian physician with sideburns, London cholera map and pump notes nearby, historically plausible editorial portrait, face-centered composition, period-appropriate clothing and workspace, accurate to known public portraits or photographs when available, no text, no watermark",
    # chapters/02-the-map-that-doesnt-move.md — Trygve Haavelmo
    "Trygve Haavelmo (circa 1944, Norwegian econometrician) - middle-aged man with short hair, formal suit, econometric equations nearby, historically plausible editorial portrait, face-centered composition, period-appropriate clothing and workspace, accurate to known public portraits or photographs when available, no text, no watermark",
    # chapters/03-what-we-mean-when-we-say-realtime.md — Konrad Zuse
    "Konrad Zuse (circa 1941, German computer pioneer) - young man in suit, mechanical computer components nearby, historically plausible editorial portrait, face-centered composition, period-appropriate clothing and workspace, accurate to known public portraits or photographs when available, no text, no watermark",
    # chapters/04-risk-is-two-numbers-not-one.md — Frank Knight
    "Frank Knight (circa 1921, American economist) - middle-aged man with glasses, uncertainty and risk notes nearby, historically plausible editorial portrait, face-centered composition, period-appropriate clothing and workspace, accurate to known public portraits or photographs when available, no text, no watermark",
    # chapters/05-pearls-ladder.md — Karl Pearson
    "Karl Pearson (circa 1900, British statistician) - middle-aged man with mustache, biometric tables and distribution curves nearby, historically plausible editorial portrait, face-centered composition, period-appropriate clothing and workspace, accurate to known public portraits or photographs when available, no text, no watermark",
    # chapters/06-graphs-that-think.md — Sewall Wright
    "Sewall Wright (circa 1934, American geneticist) - middle-aged man with glasses, path diagrams nearby, historically plausible editorial portrait, face-centered composition, period-appropriate clothing and workspace, accurate to known public portraits or photographs when available, no text, no watermark",
    # chapters/07-the-equivalence-problem.md — Bertrand Russell
    "Bertrand Russell (circa 1910, British philosopher and logician) - middle-aged man with sharp features, formal suit, logic manuscripts nearby, historically plausible editorial portrait, face-centered composition, period-appropriate clothing and workspace, accurate to known public portraits or photographs when available, no text, no watermark",
    # chapters/08-estimating-effects.md — Gertrude Cox
    "Gertrude Cox (circa 1950, American statistician) - middle-aged woman with short hair, statistical design tables nearby, historically plausible editorial portrait, face-centered composition, period-appropriate clothing and workspace, accurate to known public portraits or photographs when available, no text, no watermark",
    # chapters/09-the-counterfactual.md — Charles Sanders Peirce
    "Charles Sanders Peirce (circa 1890, American philosopher and logician) - older man with beard, pragmatism and logic manuscripts nearby, historically plausible editorial portrait, face-centered composition, period-appropriate clothing and workspace, accurate to known public portraits or photographs when available, no text, no watermark",
    # chapters/10-confounders-colliders-and-the-limits-of-observational-data.md — Jerome Cornfield
    "Jerome Cornfield (circa 1959, American statistician) - middle-aged man with glasses, epidemiology tables nearby, historically plausible editorial portrait, face-centered composition, period-appropriate clothing and workspace, accurate to known public portraits or photographs when available, no text, no watermark",
    # chapters/11-treatments.md — Janet Lane-Claypon
    "Janet Lane-Claypon (circa 1926, British physician and epidemiologist) - woman physician in early twentieth-century dress, patient records nearby, historically plausible editorial portrait, face-centered composition, period-appropriate clothing and workspace, accurate to known public portraits or photographs when available, no text, no watermark",
    # chapters/12-the-plumbers-objection.md — Esther Boserup
    "Esther Boserup (circa 1965, Danish economist) - middle-aged woman with short hair, agricultural development notes nearby, historically plausible editorial portrait, face-centered composition, period-appropriate clothing and workspace, accurate to known public portraits or photographs when available, no text, no watermark",
    # chapters/13-the-living-model-defined.md — Kenneth Boulding
    "Kenneth Boulding (circa 1956, British-American economist and systems thinker) - middle-aged man with glasses, systems diagrams nearby, historically plausible editorial portrait, face-centered composition, period-appropriate clothing and workspace, accurate to known public portraits or photographs when available, no text, no watermark",
    # chapters/14-the-expert-in-the-room.md — Michael Polanyi
    "Michael Polanyi (circa 1958, Hungarian-British polymath) - middle-aged man with receding hair, tacit knowledge manuscripts nearby, historically plausible editorial portrait, face-centered composition, period-appropriate clothing and workspace, accurate to known public portraits or photographs when available, no text, no watermark",
    # chapters/15-how-experts-get-causation-wrong.md — Amos Tversky
    "Amos Tversky (circa 1974, Israeli cognitive psychologist) - middle-aged man with dark hair, judgment and bias notes nearby, historically plausible editorial portrait, face-centered composition, period-appropriate clothing and workspace, accurate to known public portraits or photographs when available, no text, no watermark",
    # chapters/16-the-machine-that-interviews-the-expert.md — Margaret Mead
    "Margaret Mead (circa 1935, American cultural anthropologist) - young woman with short hair, field notebooks nearby, historically plausible editorial portrait, face-centered composition, period-appropriate clothing and workspace, accurate to known public portraits or photographs when available, no text, no watermark",
    # chapters/17-resolving-the-graph.md — Bruno de Finetti
    "Bruno de Finetti (circa 1937, Italian probabilist) - middle-aged man in suit, subjective probability notes nearby, historically plausible editorial portrait, face-centered composition, period-appropriate clothing and workspace, accurate to known public portraits or photographs when available, no text, no watermark",
    # chapters/18-from-graph-to-decision.md — Prasanta Chandra Mahalanobis
    "Prasanta Chandra Mahalanobis (circa 1930, Indian statistician) - South Asian man with mustache and round glasses, survey statistics charts nearby, historically plausible editorial portrait, face-centered composition, period-appropriate clothing and workspace, accurate to known public portraits or photographs when available, no text, no watermark",
    # chapters/19-the-causal-brain-executive-report.md — Marie Neurath
    "Marie Neurath (circa 1940, German-British information designer) - middle-aged woman with short hair, pictogram sheets nearby, historically plausible editorial portrait, face-centered composition, period-appropriate clothing and workspace, accurate to known public portraits or photographs when available, no text, no watermark",
    # chapters/20-keeping-the-model-alive.md — Gregory Bateson
    "Gregory Bateson (circa 1972, British anthropologist and systems thinker) - middle-aged man with beard, ecology of mind notes nearby, historically plausible editorial portrait, face-centered composition, period-appropriate clothing and workspace, accurate to known public portraits or photographs when available, no text, no watermark",
]
```
