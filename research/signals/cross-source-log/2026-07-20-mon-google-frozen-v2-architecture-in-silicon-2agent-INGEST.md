# 2026-07-20 MON — Google "Frozen v2": Gemini ARCHITECTURE-in-silicon inference chip (The Information scoop, same-day) → 2-agent verified INGEST. Real, dated TODAY, but SINGLE-SOURCED (5+ outlets = one leak redistributed) and 2028-horizon research-stage. User's "bakes the weights" framing = the ABANDONED predecessor project inside the same story, not a garble. NO POSITION ACTION.

**WORKFLOW: INGEST (Rule #16, 2 Opus agents parallel: news-item hunter + landscape/feasibility). Source = user voice relay ("Taalas-like chips baking model weights into silicon, news today"). Temporal freshness explicitly enforced (Rule #12): every claim below date-anchored; CNBC timestamp verified from article JSON-LD via curl after WebFetch 403 (retrieval-infra fix, working as designed).**

## What is VERIFIED (dated today)
| Claim | Detail | Source / tier |
|---|---|---|
| **The story is real, published TODAY** | The Information scoop; CNBC pickup timestamped 2026-07-20T14:00:10Z (JSON-LD, curl-verified); Bloomberg + 5 more same-day | T3 scoop, T2 pickups |
| **"Frozen v2"** (internal codename) | Inference chip embedding **parts of Gemini's ARCHITECTURE** into silicon; weights remain updatable; reported 6-10x tokens per unit power vs latest TPUs; deployment target as early as 2028; COMPLEMENTARY to TPU line, no mass-production commitment | All via The Information |
| **The predecessor "Frozen" (v1) was the WEIGHTS-hardwired version** | Reportedly led by Jeff Dean; burning model weights themselves into silicon — literally Taalas-class — **ABANDONED** in favor of the architecture-only v2 (weights swappable, chip survives Gemini versions sharing the backbone) | Via The Information relay |
| **Motive** | Internal Google Cloud compute shortage limiting enterprise wins | Via The Information |
| **Google response** | Hedge, not confirmation: teams experiment; not every project ships | T2 pickups |
| Alphabet stock moved up on the report | "pops"/"gain" headlines; magnitude not pinned this session | T2 |

## SOURCE STRUCTURE WARNING (Critical Rule #6 — why this stays cross-source-log, NOT triangulation)
5+ outlets same-day is **convergence of DISTRIBUTION, not of independent reporting** — every one cites The Information. Single-sourced until the original text or a second outlet with its own reporting confirms. The Information's track record on Google silicon is decent (T3-with-history) but the load-bearing specifics (6-10x, 2028, Jeff-Dean-led v1) are one leak deep.

## Landscape verified (agent 2, date-anchored)
- **Taalas (private): REAL, no Google link.** Founder Ljubisa Bajic (ex-Tenstorrent); $169M latest round, total over $219M; **HC1 demo chip launched 2026-02-19** — Llama 3.1 8B hardwired, ~14-17k tok/s company-reported, 815mm² TSMC N6; HC2 (20B-param class) targeted end-2026. No independent benchmarks. Its answer to model turnover = cheap fast re-tape-outs (~$30M/chip claimed), not field updates.
- **Etched (private):** exited stealth **2026-06-30** — $800M raised, $1B FORWARD contracts, working A0 silicon, racks targeted summer 2026. Sohu = transformer-ARCHITECTURE-specialized (weights updatable) — the same category as Frozen v2. No independent benchmarks, no delivered revenue.
- **Google TPU state:** Ironwood (v7) in deployment (192GB HBM3E, 7.2TB/s — announced 2025-11, historical). **Broadcom = Ironwood co-designer, agreement reportedly through 2031** (JPR). **TPU v8 (~late 2027) SPLITS: "Sunfish" training (Broadcom) / "Zebrafish" inference (MEDIATEK) on TSMC 2nm** — Broadcom's inference exclusivity was already narrowing BEFORE Frozen v2; Frozen v2's designer is unreported.

## First-principles read (analysis, both agents + my synthesis)
1. **Why v1 died and v2 lives:** fab lead time (6-18mo+) vs frontier-weight turnover (weeks-months) makes weight-hardwiring structurally unfit for frontier models; architecture turns over slower than weights → locking the backbone while keeping weights swappable is the rational point on the specialization curve. Weight-hardwiring stays viable only for long-lived high-volume models (embeddings/speech/ranking) — Taalas's actual niche.
2. **Memory read-through (ties to the serving-substrate row):** architecture-ASICs remove NONE of the weight/KV memory traffic that weight-hardwiring would; and even Taalas-class chips leave **KV-cache + activations fully HBM/DRAM-bound**, scaling with context and concurrency. Every point on the specialization curve CONVERGES on KV-cache as the surviving memory bottleneck — directionally consistent with the serving-substrate-memory row (`sector/bottlenecks.md`, N=5 this morning via Nvidia CMX). Cross-segment read-through (chip-and-foundry → memory-and-storage) → noted, NOT counted as a new N (Rule #6 segment discipline).
3. **Custom-ASIC narrative (NVDA bear leg):** consistent with the existing trajectory (hyperscaler silicon diversification), adds a NEW SPECIES (model-family-specialized ASIC) rather than a new magnitude — 2028 horizon, research-stage, hedged by Google itself. No NVDA falsifier fires.
4. **AVGO watch-item (the sharpest read-through):** two same-direction data points now on file — Zebrafish inference going to MediaTek at v8, and Frozen v2's designer unreported — of Google diversifying inference silicon away from the Broadcom co-design franchise at the margin, against a co-design agreement reportedly through 2031. Registered as a WATCH, not a thesis change (AVGO not held; single-sourced).

## Parallel hypotheses on the story itself (my model)
- **H1 (~70%): accurate leak of a real research-stage program** — consistent with Google's compute-shortage motive, the v1-to-v2 pivot logic is engineering-plausible, and Google's non-denial fits.
- **H2 (~20%): real program, details garbled in the leak** (the 6-10x figure and 2028 date are exactly the kind of specifics that mutate in single-source relays).
- **H3 (~10%): strategic/positioning leak** overstating maturity (timed against Nvidia narrative or for cloud-customer reassurance) — the "stock pops" outcome is consistent but not probative.

## Cascades (this commit)
- `companies/NVDA/thesis.md` + `companies/AVGO/thesis.md` — back-refs (custom-ASIC species note; AVGO inference-diversification watch).
- `sector/bottlenecks.md` serving-substrate row — one-line note: specialization-curve convergence on KV-cache.
- `watchlist/candidates.md` — Etched + Taalas added as private-tracker-class names (architecture-ASIC and weights-ASIC category leaders respectively).
- `meta/day-state.md` — logged.

**Position implication: NO ACTION — single-sourced (one leak, redistributed), research-stage, 2028-horizon, company-hedged; NVDA custom-ASIC bear leg gains a species not a magnitude; AVGO gains a registered watch-item (inference-design diversification: Zebrafish/MediaTek + Frozen-designer-unknown vs co-design agreement through 2031); serving-substrate row directionally reinforced via the KV-cache-survives argument (analysis, not a counted source). Falsifier-watch: The Information original text or independent second reporting → upgrade; Google official confirmation or TPU-roadmap integration → re-run with thesis weight. 🟡 DIRECTIONAL (event real and dated; specifics single-sourced).**

---
## ADDENDUM (2026-07-20 EVE, ~1h post-booking) — PRIMARY-TEXT FRAGMENTS obtained (user screenshot of The Information's original article)
The user supplied a screenshot of The Information's own article text (the exact input the CXL Round-3 lesson identified as the tie-breaker class). **Specifics upgrade from relay-fidelity to primary-text-fidelity; source-COUNT unchanged (still one outlet → stays cross-source-log).** What the primary text adds/confirms:
1. **The mechanism, stated for the first time (new):** general chips (TPUs/GPUs) "must make a lot of time-consuming decisions as they interact with whichever model they're running — whereas Frozen v2 would have some of the decisions for Google's Gemini models BUILT IN, reducing the number of steps the chip must take and **the amount of data it has to move around**." → the claimed 6-10x is control/dispatch elimination + data-movement reduction, per-model-family. Note for the C4/KV-cache read: the primary text claims data-movement reduction as part of the gain — the reduction plausibly targets instruction/weight-path traffic; KV-cache remains state that must move regardless (my analysis, unchanged but now with the primary mechanism on record to test against).
2. **"PROJECTED to be 6 to 10 times more efficient"** — the primary word is *projected*: internal target, not measurement. Hedge the figure accordingly everywhere it's cited.
3. **Architecture-lock confirmed verbatim:** "usable for later generations of Gemini AI models only if they are based on the same underlying model architecture in use when it was designed"; **weights-updatable confirmed verbatim** ("updating the model to take advantage of new model weights").
4. **Complementary-not-replacement confirmed verbatim** ("a new branch of homegrown chips... rather than to replace the TPU"); **latency angle (new):** faster query response "potentially enabling new AI applications."
5. Sourcing anthropology: "one of the people said" (plural insiders) — a multi-insider leak inside one outlet.
**Hypothesis reweight (my model):** H1 accurate-leak ~70→80% (primary phrasing now visible; relay-garble room shrank), H2 garbled-details ~20→10%, H3 positioning-leak ~10% unchanged. Verdict/action unchanged: single-outlet, research-stage, NO POSITION ACTION. 🟡
