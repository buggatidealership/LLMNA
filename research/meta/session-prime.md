# Session Prime — Force-Read Manifest (Cold Session Start)

**What this is:** the deterministic baseline that every fresh session loads into context before any analytical work. Hook-injected via `~/.claude/session-prime-hook.py` on `SessionStart` (NOT on `SessionStart:resume`). User-articulated rationale 2026-06-12 verbatim: *"included on the … pushes a new session to read all the components of the ledger that are crucial for the continuous and fluid learnings … the session is slower, and I get slower replies than fast replies, but with more accuracy."*

**What this is NOT:** a replacement for `INDEX.md` (which is the lazy retrieval entry point). INDEX.md says "where to look"; this file says "what you MUST have in mind right now."

**Architectural relationship to other defenses (cross-session-anchoring stack):**
- **Per-prompt:** `llm-native-priming-hook.py` injects discipline checklist (item 8 = B45 regime priors)
- **Per-session-cold:** THIS file injects via `session-prime-hook.py`
- **Per-orientation:** `CLAUDE.md` TL;DR banner (passive instruction)
- **Post-hoc:** Stop hooks catch revert patterns
- **Audit:** 2026-07-12 effectiveness check; 2026-09-12 cohort recalibration

## Cap rules (load-bearing — without these the file degrades)

- **Size budget:** hard cap 500 lines / 30,000 chars (hook MAX_INJECT_CHARS). Soft target 250-400 lines. Over 500 lines → forced demotion at monthly audit
- **What goes in:**
  1. ACTIVE CANDIDATE biases (full one-paragraph each) — see §2
  2. CONFIRMED biases still actively binding on current outputs (one-line + correction, not archived) — see §2
  3. Lessons L(n-4) through L(n) (rolling 5 most recent verified lessons only — no placeholders)
  4. Critical Rules 1-N (numbered list only, full text in CLAUDE.md) — keep current with CLAUDE.md
  5. The current regime read (one paragraph; the B45 baseline) — see §1
  6. Active TC clusters (one-line each; PARKED clusters stay out)
  7. Held cohort (current positions, one-line each; re-date on every monthly audit)
  8. Pending predictions whose resolution window has NOT yet passed
  9. Upcoming recalibrations / audits within the next 90 days (past-due items get removed on monthly audit)
- **What stays out:** archived biases (CONFIRMED + >60 days inert), stale lessons (>90 days no application), placeholder lessons with no content, inactive TC clusters (PARKED), full thesis bodies (use `INDEX.md` to retrieve), past-due audit dates, resolved/expired prediction stubs
- **Promotion/demotion:** on each codification commit (Critical Rule #13), update THIS file in the same commit. On monthly audit (24th of each month), demote items that meet INERT criteria per the curation rule below

## §0. CURATION RULE (codified 2026-06-24 — governs what stays in and when it leaves)

**Purpose:** keep session-prime small enough to be useful and large enough to matter. The hook injects the entire file; every line costs cold-start context. Ballast that doesn't change cold-session calibration is waste.

### Inclusion criteria (entry must satisfy ALL three)

| Criterion | Test |
|---|---|
| **Recency** | Added or updated in last 90 days OR re-verified as still-binding this cycle |
| **Load-bearing** | If removed, cold-session calibration would measurably worsen (e.g., B45 without §1 → pre-training magnitude error resurfaces) |
| **Non-redundant** | Not already enforced by a LIVE hook — hooks are deterministic; this file is supplemental priming for anything that lacks a hook |

### Demotion triggers (any one fires → remove or move entry to its canonical file)

| Trigger | Action |
|---|---|
| Bias promoted to CONFIRMED + inert >60 days | Remove from §2; canonical home is `biases-watchlist.md` |
| Lesson >90 days since last visible application | Remove from §3; canonical home is `predictions/lessons.md` |
| Lesson is a placeholder "(placeholder — verify...)" | Remove immediately; never allow into inject |
| Critical Rule added to CLAUDE.md but missing here | ADD within same commit (critical rule #13 cascade) |
| Prediction resolution window has passed | Remove from §7 within 7 days; grade it via GRADE workflow |
| Audit date is in the past | Remove from §8 at next monthly audit |
| TC cluster status is PARKED | Remove from §5; canonical home is `signals/triangulation.md` |
| File exceeds 450 lines (early-warning threshold) | Force demotion pass at monthly audit BEFORE 500-line hard cap |

### Monthly audit integration (codified 2026-06-24)

Session-prime is reviewed on the **24th of each month** as part of the monthly consolidated audit. Steps:

1. **Measure** file size in chars + lines; log % of cap
2. **Audit §2** (biases): verify each bias is still CANDIDATE or actively-binding CONFIRMED; demote inerts
3. **Audit §3** (lessons): verify rolling-5 is current; remove placeholders; check all lessons are referenced ≥1 time in last 90 days
4. **Audit §4** (critical rules): cross-check against CLAUDE.md for any rules added since last audit; add missing one-liners
5. **Audit §5** (TC clusters): verify each is still ACTIVE N≥3; remove PARKEDs
6. **Audit §6** (held cohort): re-date to current session; note any position changes since last audit date
7. **Audit §7** (pending predictions): remove any whose resolution window passed; flag for GRADE workflow
8. **Audit §8** (recalibrations): remove past dates; add any new items due in next 90 days
9. **Log findings** in `meta/recurring-audit-log.md` with chars/% of cap, demotion count, additions, and next audit date

---

## §1. CURRENT REGIME (B45 baseline — load-bearing for magnitude reads)

**Regime:** structural-demand AI-supercycle through at least 2027 per `sector/where-we-are.md` 8-tier memory-shortage convergence ledger. Empirical 15-name AI-infrastructure basket Jan 2025 → Jun 12 2026 (subagent-verified, full data at `signals/cross-source-log/2026-06-12-pre-training-magnitude-conservatism-calibration.md`):

- 6 of 15 names returned >+200% (extreme outliers); 6 of 15 returned +100-200% (category outliers)
- Most under-modeled vs naive pre-training prior: MU +1,044%, NBIS +1,528%, SK Hynix +799%, Kioxia +5,480%
- Single-day moves of +5-12% across cohort are ROUTINE (multiple times per week)
- Tail under-modeled by ~5-8× vs pre-training prior

**Pre-training is mis-calibrated here. Before flagging any return or single-day move as "extreme" / "elevated" / "exhaustion-signaling" / "above expectation" / "stretched" / "priced-to-perfection", check this regime base rate.** Quarterly recalibration 2026-09-12.

## §2. ACTIVE BIASES (CANDIDATE biases + CONFIRMED biases still binding on current outputs)

- **B40** (CONFIRMED VERIFIED-HIGH-CONFIDENCE) — Secondary-source garble taxonomy (3 sub-types). B40.1 stale-recycle (N=9+), B40.2 magnitude-inflation (CONFIRMED N=3), B40.3 attribution-garbling (CONFIRMED N=2). Verify temporal freshness + magnitude + attribution before propagating any T2/T3 signal. Stays here because hook enforcement not yet built; manual discipline required.
- **B44** (CANDIDATE N=3, origin 2026-06-11) — Chat-summary discipline drift from file-level discipline. File-level work applies T1/T2/T3 tagging / N-th order / native-language / hedge labels correctly; chat summary collapses to prose. Mirror file-level discipline in chat summaries.
- **B45** (CANDIDATE N=1, origin 2026-06-12) — Pre-training magnitude conservatism in structural-demand regimes. Tail under-modeled by ~5-8×. See §1 above for active priors. Companion to B26 + B28: B45 is the MAGNITUDE-layer error in the structural-anchoring family.
- **B62** (CANDIDATE N=1, origin 2026-06-15; RENUMBERED from B47 on 2026-07-06 — B47 was already taken by efficiency-driven demand destruction in `biases-watchlist.md`) — Pre-training lead-time conservatism: estimates of gov/regulatory lead-times are wrong by 2-10×. Overstates fast-track gov action; understates regulated EU processes. Every gate-timing estimate gets retroactively case-calibrated. See §9b.
- **B60** (CANDIDATE N=1, origin 2026-07-01) — Portfolio-anchored ingest bias: discovery legs must stay unanchored to held names.
- **B61** (CANDIDATE N=1, origin 2026-07-03) — LLM-generated bottleneck fiction as an input class: unsourced single-company monopoly-bottleneck theses from social sources get the full mechanism gauntlet regardless of sharer track record.

## §3. RECENT LESSONS (rolling 5 — refreshed 2026-07-06 harness audit; current tail L30, all recent = CANDIDATE)

- **L26** — Multi-decade trend-line break = structural-regime-confirmation framework (60-year DRAM ASP rupture origin; N=2 watch: MLCC / NAND / CoWoS).
- **L27** — Beat-Consensus-As-Regime-Test: per-quarter beat-or-miss across the semi cohort = primary regime-validation mechanism (first empirical test = MU Q3 FY26 print 2026-06-24; N=2 watch: HYNIX Q2 + MURATA Q1 FY27 late-Jul).
- **L28** — Jevons/efficiency-fear misread: "efficiency reduces demand" keeps losing to volume growth (N=3 flavors incl. enterprise rate-limiting).
- **L29** — LLM-native inference as the analytical anchor, not sell-side aggregation (user methodological preference 2026-06-25).
- **L30** — Supercycle base rates dominate pre-supercycle band priors on cohort ATH events (KIOXIA VLSI grade origin).

_Correction note (2026-07-06): this section previously claimed "L24 removed; tail is L25" — WRONG on both counts: L24 exists in lessons.md as a real lesson (mid-cap structural-inflection ATH-break, TY case) and the tail is L30. Numbering gap: L17/L18 carry tombstones (no lesson text). Full list: `predictions/lessons.md` + `meta/tags.md`._

## §4. CRITICAL RULES (full text in `CLAUDE.md` — numbered list here for orientation)

1. Never mix facts and interpretations (separate files)
2. Never PREDICT without reading lessons.md first
3. Never claim "consensus thinks X" without naming source
4. Always run TRACE on cross-domain events
5. Always update `bottlenecks.md` last_review on BOTTLENECK-FORECAST
6. Single article never overrides triangulated signal + segment-classify before triangulating
7. NEVER FABRICATE NUMBERS (enforced by `anti-fabrication-hook.py`)
8. Never sell on macro headwind without thesis falsification
9. Always apply bypass-route thinking on any binding constraint
10. Always cascade cross-source synthesis to per-thesis files (enforced by `cascade-enforcement-hook.py`)
11. Always close thesis update with explicit `Position implication:` line + auto-execute default + self-correct visibly
12. Always verify temporal freshness before cascading T2/T3 signals (B40)
13. Codification trigger — chat-only output MUST be persisted to file when contradicting / position-relevant / methodological / user-corrected / N≥2 recurring
14. Signal density detection — every cross-source-log file MUST run same-segment same-direction lookup; promote to triangulation at N≥3
15. Macro-first, research-anchored discipline — before position-relevant output: articulate layer first-principles with date anchor; tag claims research-verified vs recall-based; tie micro details to macro thesis; surface macro-vs-micro contradictions before concluding (B46 origin 2026-06-12)
16. Always run verification subagents immediately on any external data with thesis/sizing implications — model = Opus 4.8, parallel firing, N=2-4, never ask permission; log to `meta/subagent-cost-yield-ledger.md` (instrumentation added 2026-06-19)
17. Ensemble high-stakes calls — for any binary/numeric decision with sizing consequence (prediction GRADEs, binary-catalyst outcomes, TRIM/EXIT/ENTER on a Core position, tier-gating P-weights), run N=3-5 independent Opus 4.8 samples and report MODE + SPREAD; spread is the signal (5/5 = high-conviction; 3/5 = state uncertainty, don't collapse to false-confident point). Scope: sizing-consequential only, NOT routine. (added 2026-06-27)
18. Standing dissent mandate — on any thesis conclusion, sizing decision, or user framing, generate the strongest FALSIFYING case BEFORE concluding; if none exists, say so explicitly. Non-optional; suppresses confirmation-of-harness-state + sycophancy. Per-conclusion obligation (distinct from Rule #8 periodic + Leg B search-layer). (added 2026-06-27)

## §5. ACTIVE TRIANGULATION CLUSTERS (refreshed 2026-07-06 harness audit; quick-index in `signals/triangulation.md` is CANONICAL for N — this list is orientation only)

- **TC-1** Memory tightness multi-tier (memory-and-storage) [ACTIVE N=22+; 60-yr WSTS trend-break + Jun-22 cohort-wide ATH cluster-state event]
- **TC-2** AI capex on credit + state budgets (infrastructure-IaaS) [ACTIVE N=7]
- **TC-3** DC-ceiling + EM-migration (power-and-cooling) [ACTIVE N=9; $130B/75+ projects blocked Q1'26]
- **TC-4** Anthropic enterprise-trust drift (model-and-foundation-lab) [ACTIVE N=12 + acute-phase transition (Jun-13 90-min shutdown)]
- **TC-5** CoPoS / glass-core packaging firming (advanced-packaging) [ACTIVE N=8]
- **TC-6** MLCC AI-server tier bifurcation [ACTIVE N=6] · **TC-7** InP geopolitical bottleneck [N=4] · **TC-8** token consumption [maintained]
- **TC-10** Model-layer sovereignty + export control [ACTIVE N=9 + NBIS UK proof case] · **TC-11** chip-import patent enforcement [CANDIDATE N=1]
- **TC-12** DRAM>HBM margin inversion [ACTIVE N=5] · **TC-13** AI power-infrastructure bottleneck cascade [ACTIVE N=7+] · **TC-14** YMTC westward NAND qualification [ACTIVE N=3, promoted 2026-07-05 — bear-vector watch on KIOXIA/SNDK consumer mix]

_Prior version of this section carried N-counts 2-4× stale (e.g. TC-4 listed N=3 vs actual N=12) and omitted TC-10..14 entirely — corrected 2026-07-06._

## §6. HELD COHORT (per `portfolio/holdings.md` — REFRESHED 2026-07-05 EVE screenshots; FRESH-START baseline; DeGiro €95.406,73 = the whole book, N26 = bank only)

**2 held names (both DeGiro); re-verify at session start against holdings.md:**
1. MURATA 336sh (MUR1) — €19.656,00 — **20,6%** (BEP €53,67; Q1 FY27 print ~late July, L22 test)
2. SUMCO 626sh (S3X) — €17.058,50 — **17,9%** (BEP €22,31; wafer-hike thesis materializing)
+ Cash €58.692,23 — **61,5%** — LOCKED until `portfolio/risk-envelope.md` exists; ALAB/BE intents SUPERSEDED.

**⚠️ 2026-07-05 STATE CHANGE (read before ANY position talk):** SKH 16 GDR + SNDK 9sh + KIOXIA ~€10k(N26) FULL-EXITED ~Jul-1/2 by user — EMOTIONAL exits, NOT falsifier fires, disclosed 2026-07-05; NBIS exited Jul-3. All four theses intact → watchlist-reference. Conversion-layer lesson in `predictions/lessons.md` (2026-07-05): sizing must track REVEALED drawdown tolerance; re-entries only via fresh envelope-gated decision packages. Do NOT propose redeployment before the risk envelope exists.

**🔴 EXITED (do NOT reference as held — watchlist-reference only):** MRVL (full exit 2026-06-27, was 8.0%), DDOG (sold 2026-06-22), NOW (sold 2026-06-22), ARM/AGC/Hirano/MongoDB (exited Jun rotation).

_holdings.md is authoritative. This list caused a held-vs-sold error 2026-06-27 when stale — keep it synced on every portfolio screenshot._

## §7. PENDING PREDICTIONS (refreshed 2026-07-06 harness audit; canonical ledger = `predictions/grading-log.md` — read its NOT-CANONICAL row tags)

- **Samsung Q2 prelim — resolves ~2026-07-07 (KEYSTONE):** canonical file = `predictions/2026-07-02-SAMSUNG-Q2-prelim-prediction.md` (rev pt ₩178tn / OP pt ₩92tn vs cons ₩84.98tn). ⚠️ A superseded duplicate file exists — grade ONLY the canonical one.
- **NBIS Nasdaq-100 inclusion grades:** T+15 ~2026-07-07, T+30 ~2026-07-22 (primary adjudicator). T+5 (due 2026-06-27) NOT yet run — backfill with the T+15 grade. Position exited 07-03; grades still resolve.
- **10-name earnings prediction board (registered 2026-07-02):** TSMC Jul-16 (checkpoint Jul-10), ASML Jul-15, SK Hynix ~Jul-29, MURATA Jul-31, SNDK late-Jul/Aug, KIOXIA Aug-07, ALAB Aug-11, SUMCO Aug-12, BE ~Jul-30.
- **Overdue GRADE debt:** MU Q3 FY26 (resolved 2026-06-24) was never formally ledgered/3-layer-graded — backfill owed.

_Prior version claimed "no active pending predictions as of 2026-06-24" — corrected 2026-07-06; the KIOXIA VLSI grade it referenced was completed 2026-06-26 (L30)._

## §8. UPCOMING RECALIBRATIONS / AUDITS (next 90 days from 2026-06-24)

- **2026-06-25** — Supply chain graph reconstruction (H1 capability application, monthly recurring)
- **2026-06-26** — Two-bracket LLM-native experiment week-3 check
- **2026-06-27** — Adversarial bear-case stress-test on held cohort (use B45-corrected base rates)
- ~~2026-07-01~~ **RESOLVED 2026-07-06** — Two-bracket 30-day close: volume-confounded raw read; user decision KEEP BOTH → extended close **2026-08-06** with normalized metric (fires ÷ weekly commits); see CLAUDE.md hook entry + todo.md
- **2026-07-04 (OVERDUE)** — BOTTLENECK-FORECAST monthly (Layer-3 power gap flagged per `sector/unbypassable-layers.md`; last_review still 2026-06-04)
- **2026-07-11** — Codification rule + signal-density-detection 30-day net-positive check
- **2026-07-12** — B45 priming-bracket effectiveness check (30-day audit) + session-prime maintenance discipline check
- **2026-07-15** — Principle #37 first re-eval (N=20 cascade events gate)
- **2026-07-24** — Monthly consolidated audit (next cycle)
- **2026-07-31** — SNDK Q2 FY27 print + L17 candidate test
- **2026-09-12** — B45 cohort base-rate quarterly recalibration

## §9. TRUTH-TIER TAGGING + SCOPED-CASCADE RULE (Principle #37 CANDIDATE — ADDED 2026-06-15, load-bearing for every analytical output)

**The convention (memorize for first turn):** every load-bearing claim carries a marker.
- **🟢 HARD** — T1 receipt (filing, IR, gov data, court record, contract). Citation URL REQUIRED.
- **🟡 DIRECTIONAL** — T2 source-tier (trade press, sell-side, forecaster) OR my-model with explicit `(my model)` + Bayesian P.
- **🔴 SPECULATIVE / IN-FEAR** — Hypothesis, candidate, pre-registered H1-H4, single-source unverified.
- **STALE** — Auto-flag on 🔴/🟡 entries no cascade-event >30 days.

**Position implication enforcement:** every `Position implication:` line MUST carry a 🟢/🟡/🔴 marker on the same line or directly above. Hook-level enforcement: `research/meta/hooks/structural-output-hook.py` is LIVE via project-level `.claude/settings.json` (Architecture A, since 2026-06-26) — the old "pending `cp` to `~/.claude/`" activation instruction is obsolete and must NOT be followed (`~/.claude/settings.json` is intentionally unused; copying would risk double-firing).

**The scoped-cascade rule (load-bearing — when new data lands):**

1. **Tag intake** — tier the new datapoint 🟢/🟡/🔴 BEFORE it enters any log file
2. **Touch detection** — identify which existing 🔴/🟡 claims this datapoint INTERSECTS (grep / search; usually 1-3 files: 1 thesis + 1 TC entry + 1 cross-source-log + sometimes a watchlist row)
3. **Scoped propagation** — update tier on touched claims IN THE SAME COMMIT; append entry to `meta/tier-cascade-log.md` recording: trigger source, intake tier, files touched with tier-moves, files NOT touched (confirms scope), stale flags fired, commit SHA. **UNTOUCHED FILES STAY UNTOUCHED — do NOT blanket-sweep.** (User explicit 2026-06-15: "if a piece of data does not touch anything specifically, no need to update.")
4. **Stale check** — log auto-flags 🔴/🟡 entries >30d untouched; surfaced in next SessionStart briefing

**Integration:** Principle #37 is the structural resolution of Critical Rule #15 (research-vs-recall T1/T2/T3) — the source-tier becomes a propagating marker. Critical Rule #11 (`Position implication:`) now requires tier marker. Critical Rule #10 (cascade cross-source synthesis) operates tier-by-tier rather than file-by-file but BOTH still required in same commit.

**Cascade log:** `meta/tier-cascade-log.md` (append-only audit trail). First entry 2026-06-15 = meta-entry / file birth.

**Status:** 🟡 CANDIDATE (Principle #37 born at directional pending 30-day operational test). Promotion gate: N=20 cascade events successfully logged without drift. First re-eval 2026-07-15.

### §9b — Principle #38 CANDIDATE — Lead-Lag Variable Framework (added 2026-06-15 PM2)

Every tracking variable in a thesis / cluster / candidate file must be tagged **LEAD** (acts BEFORE the market-moving event) or **LAG** (confirms AFTER) — explicitly. Default is LAG because LAG signals naturally surface from research-verified sources (filings / earnings / press releases); LEAD requires deliberate alt-data sourcing. Without the tag, sizing decisions get made on LAG variables and capture only consensus-level alpha.

For every gate / falsifier / monitoring variable: build BOTH lead-indicator stack (verified URL + accessibility tier + native-lang + historically-calibrated lead-time) AND lag-indicator stack (explicit "do not chase" tagging). Plus convex-hull / lateral check per LLM-native priming item 3.

**B47 candidate** listed in §2 above. First application: `companies/NBIS/tracking-variables.md`. Next application N=2: any TC cluster's tracking variables (TC-1 / TC-6 / TC-10 most likely given active cascade rate).

### §9c — 2026-07-07 codification batch (Principles #43/#43b/#44 candidates + B63 — load-bearing operating changes)

- **#43 Configuration Over Capability:** latent capability ≠ deployed behavior; sampling defaults anchor to training-distribution patterns (English sources, linear prose, human-time estimates). Operator-surfaced affordances = HIGH-VALUE codification triggers. Monthly-audit standing question: *"what capability exists but is not deployed by default?"*
- **#43b — COMPUTE INSTEAD OF NARRATE (deployed behavior, not a suggestion):** for ANY quantitative task (envelope/band math, P/L decomposition, correlations, prediction bands, count metrics, calibration aggregation) EXECUTE the computation via Bash/python FIRST, then explain. Prose smooths errors; computation surfaces mismatches, and the mismatch is information. First run (2026-07-07): 2 tasks → 3 catches (impossible cross-position FX residuals; git history-graft trap in `--first-parent`; miscounted hook-fire series narrated as fact). Deterministic tool: `meta/structural-output-metric.py` (the 2026-08-06 hook-experiment adjudicator). Also in priming-hook item 10.
- **#44 Detection Over Prediction:** revenue-model emergence is unforecastable ex-ante, detectable early — instrument for it (pricing-transition metrics); under model-uncertainty own the substrate every candidate model consumes; the Cisco warning: substrate pricing power is ERA-BOUND → buildout-maturation falsifiers (coding-deceleration tripwire, capex guides) outrank technology-substitution falsifiers in firing order.
- **B63 model-provenance bias:** the analyst is an Anthropic model — ALL Anthropic/lab-favorable conclusions get mandatory adversarial treatment (never bank lab-sourced ARR; third-party evidence for rankings; explicit Rule #18 falsifier run).
- Anthropomorphic-default bias (named class, inside #43b): pre-training imports human constraints that don't bind the model — human time estimates, single-threaded plans, essay-instead-of-computation. Sweep for these at the affordance review.
- **AGENT-PRIMITIVES CAPABILITY MAP (docs-verified + executed-tested 2026-07-08; #43 N+1 — user-surfaced):** (1) Subagents here are NOT fire-and-forget: a completed agent is **RESUMABLE via SendMessage with context intact** — EXECUTED-VERIFIED 2026-07-08 (docs-sweep agent resumed post-completion, answered from prior context in ~8s, zero re-searches). USE for follow-up questions to verification agents instead of re-firing fresh ones (cost saver). Docs' "cannot be resumed" claim is FALSE for this runtime; session-scoped only. (2) Docs (T1 code.claude.com 2026-07-08): subagent roles CAN carry `enable persistent memory` frontmatter (accumulates across invocations) — but memory lives at ~/.claude/projects/ which does NOT survive cloud-container recycling; the harness's git-versioned files remain the superior durable memory for us. (3) Agent teams (team lead + named teammates w/ own contexts, shared task list, inter-agent messaging) EXIST but are experimental, CLI-only (`CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1`, tmux/iTerm2) — NOT available in cloud sessions. Team lead = the main session, not an agent type.

## §10. ARCHITECTURE NOTE — how this file gets maintained

Per Critical Rule #13 codification cascade discipline (updated 2026-06-12): every commit that adds a new bias / lesson / principle / critical rule / triangulation cluster MUST also update this file in the same commit. The `cascade-enforcement-hook.py` does not currently check for session-prime updates — manual enforcement until N≥2 skips trigger building `~/.claude/session-prime-cascade-hook.py`. Audit at 2026-07-12 + monthly thereafter: if codifications happened but session-prime wasn't updated, the maintenance discipline is broken and needs hook-enforcement.

**Curation rule location:** §0 above (codified 2026-06-24). The curation rule is embedded in this file rather than a separate file because the rules that govern injection ARE themselves part of what the session needs to know cold.

## §11. FALSIFIER FOR THIS FILE ITSELF

If a 30-day audit shows that having session-prime loaded produced ZERO measurable reduction in the bias-recurrence rate (e.g., I still flag +7-10% single-day moves as "extreme" without referencing B45 baseline), then the file is decorative noise and should be retired (along with the hook). Detectability: grep transcripts 2026-06-12 → 2026-07-12 for magnitude-categorizing language WITHOUT B45 reference. POSITIVE = <2 instances; NEGATIVE = ≥3 instances → retire OR refine selection rules.

**Extended falsifier (added 2026-06-24):** if monthly audit produces zero demotions + zero additions for 3 consecutive cycles, the curation rule is working but the file is not evolving — check whether the OS has stagnated or the curation rule is too aggressive.
