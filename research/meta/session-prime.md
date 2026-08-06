# Session Prime — Force-Read Manifest (Cold Session Start)

**What this is:** the deterministic baseline that every fresh session loads into context before any analytical work. Hook-injected via `~/.claude/session-prime-hook.py` on `SessionStart` (NOT on `SessionStart:resume`). User-articulated rationale 2026-06-12 verbatim: *"included on the … pushes a new session to read all the components of the ledger that are crucial for the continuous and fluid learnings … the session is slower, and I get slower replies than fast replies, but with more accuracy."*

**What this is NOT:** a replacement for `INDEX.md` (which is the lazy retrieval entry point). INDEX.md says "where to look"; this file says "what you MUST have in mind right now."

**Architectural relationship to other defenses (cross-session-anchoring stack):**
- **Per-prompt:** `llm-native-priming-hook.py` injects discipline checklist (item 8 = B45 regime priors)
- **Per-session-cold:** THIS file injects via `session-prime-hook.py`
- **Per-orientation:** `CLAUDE.md` TL;DR banner (passive instruction)
- **Post-hoc:** Stop hooks catch revert patterns
- **Audit:** 2026-07-12 effectiveness check; 2026-09-12 cohort recalibration

## 🔴 2026-08-04 — THIS FILE WAS SILENTLY OVER ITS OWN CAP, AND NOTHING SAID SO

**Measured today while adding L55/L56: the file was 30,347 chars against the hook's `MAX_INJECT_CHARS=30000`.** It had been **347 chars over**, so **everything past char 30,000 was being silently dropped at every cold-start injection** — the tail (a PC-20/21/22 pattern line) was in the file, in git, readable by anyone who opened it, and **never reaching the session it exists to prime.**

**The failure mode is the cap's, not the content's:** it truncates instead of failing. 1 char over and 5,000 over behave identically, and the only symptom is content that quietly stops arriving. **Nothing measures the file against the cap** — the hook enforces it at read time and never reports it.

**Fixed by pruning, not by raising the cap:** dropped §9c's 07-07 batch narrative (3,269 → 380 ch; its principles live in `CLAUDE.md` + `methodology.md`) and applied §3's own **rolling-5** rule, which had drifted to 6.

**Blind-check (#51):** distinguishes *"session-prime is priming the session"* from *"session-prime's tail is being cut off"* · reads on `len(file)` vs `MAX_INJECT_CHARS` · **goes blind if** the cap is enforced somewhere the file's authors never look — which is exactly what happened; it is enforced inside the hook at read time, and no writer, commit or audit compares the two numbers. **A limit that is only checked by the thing consuming it is invisible to the thing producing it.**

**Booked:** add a length assertion to the pre-commit checks so this fails loudly at write time rather than silently at read time.

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
- **B64** (CANDIDATE N=1, origin 2026-07-13, user-flagged) — Model-affinity contamination: Claude-family models reportedly favor NOW in pick-a-stock settings; house NOW thesis cites Anthropic T1 material = closed-loop risk. Any NOW decision package: adversarial pass mandatory, Anthropic-sourced validation corroborating-only, case must survive with Anthropic evidence removed.

## §3. RECENT LESSONS (rolling 5; all recent = CANDIDATE)

- **L59 CANDIDATE (2026-08-06): A CORRECT CALL FROM A REFUTED MECHANISM IS A REASONING MISS.** SNDK R-4 (beat-both → negative close) HIT at **P=0.35** — but its registered justification was *"consensus sits above the guide, so an in-range print is a miss."* **The print was NOT in range**: it cleared consensus by 8–15% and guided +17.7% QoQ, and fell anyway. **Premise false, conclusion landed.** Score outcome and mechanism SEPARATELY; **never update the P on a mechanism the event refuted** — a long-odds hit strengthens a disproved chain *harder* than an ordinary one. Binding: **no direction leg ships without a stated mechanism.** Companion refuted same session at N=2: SNDK R-2 over-called magnitude (−8.00%) while DDOG R-5 under-called it (−19.03%) at identical P and threshold ⇒ **magnitude is NOISY, not biased**; keep it separate from B45 (directional) or a correction factor gets applied to noise.
- **L58 (2026-08-05): BASIS MISMATCH — every number carries what it was measured AGAINST, and no two numbers may be compared until their bases match.** Basis = reference point, date, category, season, window, denominator (incl. day count) — **and tense**. Generalises and SUPERSEDES L42-b. Enforcement is **CONSTRUCTIVE** (a BASIS column in every comparison table), not filtering. Five specimens in four days: AMD −8.8% off a close that had risen +7.00%; SNDK −5.40% attributed to a print 30 min later; SPCX −13.61% off a +9.43% close; "printed" written of an event 2.9h away; and the SNDK R-2 grade, where the registered baseline made it a MISS and the other available baseline would have made it a HIT.
- **L57 (2026-08-05): A BEAT-HISTORY BASE RATE MEASURES THE GUIDANCE GAP, NOT THE COMPANY.** A streak of beats is a fact about how conservatively management guided, not about how the business performs. **Check whether the gap is still open before using the streak** — DDOG's bar-jump was the company removing its own sandbag, not the street re-rating it.
- **L56 (2026-08-04): AN "ANOMALOUS AND UNRESOLVED" FIGURE IN A PREDICTION FILE IS A DEFECT, NOT A DISCLOSURE.** ¥874.1bn ÷ ¥869bn (the **NET** guide) = +0.6% — a net figure crossed against an operating-profit guide; the "anomaly" was the arithmetic signature of the cross. **Scale-check every carried bar against the entity's other published lines — one division.** Name the basis on every profit line.
- **L53 CANDIDATE (N=2 → N=3, MPWR + MURATA 07-31; RECURRED 2026-08-06): THE RETRIEVAL-DRAWER ERROR** — a name filed under the wrong theme is functionally invisible even when it is in the corpus and correctly described. **Retained out of rolling order because it recurred today**: I re-derived the beat-and-fall pattern as new when `predictions/2026-08-05-DDOG-...md:301` already carried it, in a file I had written 18 hours earlier. Governs DECAY of a correct OLD classification (B60 governs framing of NEW data). Instrument: at each monthly audit re-derive every held/watchlist name's primary drawer from its LATEST reported segment mix.

_Numbering: L17/L18 tombstoned; full list `predictions/lessons.md` + `meta/tags.md`._
_§3 curation: 07-31 L27+L28, 08-02 L40 removed; **08-06 L54 + L55 curated out** (canonical in `predictions/lessons.md`; L55's B45-at-intake content is carried by B45 itself in §2); L53 retained beyond rolling-5 on same-day recurrence._

## §4. CRITICAL RULES (full text in `CLAUDE.md`; orientation list)

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
13b. **BLIND-CHECK ON EVERY DETECTOR (#51, 2026-08-01)** — every falsifier / falsification condition / kill criterion / re-eval trigger / hook repair criterion carries one line: `distinguishes [X] from [Y] · reads on [quantity] · **goes blind if [channel shift]**`. In a fluid-outcome domain the outcome NEVER grades the instrument, so this is the only ex-ante grade there is. The load-bearing clause is "goes blind if" — a LATERAL question (*what else produces this same reading?*), answerable without foreknowing the channel. STANDARD not METHOD: destination constrained, route free. Specimens: KIOXIA unfireable · capex-line blind when MSFT moved $132.5bn into leases · macro-anchor-hook's repair criterion unmeasurable from its own log. **VERIFIED BY MEASUREMENT:** `meta/tools/blind_check_audit.py` → `meta/blind-check-ledger.md`. Baseline 08-02 **0/155**; thresholds pre-registered; re-eval 08-24; **<80% = hook it or retire it.**
14. Signal density detection — every cross-source-log file MUST run same-segment same-direction lookup; promote to triangulation at N≥3
15. Macro-first, research-anchored — articulate layer first-principles with date anchor; tag claims research-verified vs recall-based; tie micro to macro; surface contradictions before concluding (B46)
16. Always run verification subagents immediately on external data with thesis/sizing implications — Opus 4.8, parallel, N=2-4, never ask; log to `meta/subagent-cost-yield-ledger.md`
17. Ensemble high-stakes calls — sizing-consequential binary/numeric decisions get N=3-5 independent samples; report MODE + SPREAD (spread IS the signal; 3/5 = state the uncertainty). Not routine work.
18. Standing dissent mandate — on any thesis conclusion, sizing decision, or user framing, generate the strongest FALSIFYING case BEFORE concluding; if none exists, say so explicitly. Non-optional; suppresses confirmation-of-harness-state + sycophancy. Per-conclusion obligation (distinct from Rule #8 periodic + Leg B search-layer).
19. Destructive-change governance (`meta/destructive-change-governance.md`) — HIGH tier (delete LIVE enforcement/active Routine/protected path; >3-file delete) = operator pre-approval FIRST; CATASTROPHIC (history rewrite/force-push, repo wipe) = explicit VERBATIM operator instruction only; inferred/relayed never qualifies. Enforced: pre-commit F4 + pre-push hook (verified 07-19); tokens only after approval.

## §5. ACTIVE TRIANGULATION CLUSTERS (orientation only; `signals/triangulation.md` quick-index is CANONICAL for N)

- **TC-1** Memory tightness multi-tier (memory-and-storage) [ACTIVE N=22+; 60-yr WSTS trend-break + Jun-22 cohort-wide ATH cluster-state event]
- **TC-2** AI capex on credit + state budgets (infrastructure-IaaS) [ACTIVE N=7]
- **TC-3** DC-ceiling + EM-migration (power-and-cooling) [ACTIVE N=9; $130B/75+ projects blocked Q1'26]
- **TC-4** Anthropic enterprise-trust drift (model-and-foundation-lab) [ACTIVE N=12 + acute-phase transition (Jun-13 90-min shutdown)]
- **TC-5** CoPoS / glass-core packaging firming (advanced-packaging) [ACTIVE N=8]
- **TC-6** MLCC AI-server tier bifurcation [ACTIVE N=6] · **TC-7** InP geopolitical bottleneck [N=4] · **TC-8** token consumption [maintained]
- **TC-10** Model-layer sovereignty + export control [ACTIVE N=9 + NBIS UK proof case] · **TC-11** chip-import patent enforcement [CANDIDATE N=1]
- **TC-12** DRAM>HBM margin inversion [ACTIVE N=5] · **TC-13** AI power-infrastructure bottleneck cascade [ACTIVE N=7+] · **TC-14** YMTC westward NAND qualification [ACTIVE N=3, promoted 2026-07-05 — bear-vector watch on KIOXIA/SNDK consumer mix]


## §6. HELD COHORT (`portfolio/holdings.md` is canonical — re-verify on every screenshot; refreshed 07-12)

**3 held names (all DeGiro):**
1. MURATA 336sh (MUR1) — ~20,6% at the 07-05 baseline (BEP €53,67; Q1 FY27 print 2026-07-31, L22/L27 test)
2. SUMCO 626sh (S3X) — ~17,9% at the 07-05 baseline (BEP €22,31; Q2 pre-registered `predictions/2026-07-11-SUMCO-Q2-FY2026-preregistration.md`, print 2026-08-06)
3. SKHY 37 ADS @ $173.45 (2026-07-10, ~6.0% at entry, computed) — bought at +19.7% ADR premium over Seoul ordinary (ABOVE the pre-stated ≤~5% gate, user override, both being graded); regular-way tape opens 2026-07-13; premium template + read ladder in `companies/SKHY/thesis.md`
+ Cash ~€53.1k after SKHY entry (per thesis entry facts) — governed by `portfolio/risk-envelope.md` v4 (capital ladder: floor €160k inviolable at total-wealth level; rungs gated on graded evidence).

**⚠️ PRINCIPAL CONTEXT (booked 2026-07-11/12 — read `meta/user-source-profile.md` before any sizing talk):** purpose/capital-ladder/fluidity-rule/PF-register (PF-1 ⚠️FALSIFIED-AS-DOCTRINE 07-17→override-ledger adjudicates; Rule #8 stands); NO position cap (Q7); inputs are an evolving function — do NOT ossify single utterances. Standing directive 2026-07-12: if user input is required, ASK (queue: `meta/principal-questions.md`).

**⚠️ 2026-07-05 STATE CHANGE (read before ANY position talk):** SKH 16 GDR + SNDK 9sh + KIOXIA ~€10k(N26) FULL-EXITED ~Jul-1/2 by user — EMOTIONAL exits, NOT falsifier fires, disclosed 2026-07-05; NBIS exited Jul-3. All four theses intact → watchlist-reference. Conversion-layer lesson in `predictions/lessons.md` (2026-07-05): sizing must track REVEALED drawdown tolerance; re-entries only via fresh envelope-gated decision packages. Do NOT propose redeployment before the risk envelope exists.

**🔴 EXITED (do NOT reference as held — watchlist-reference only):** MRVL (full exit 2026-06-27, was 8.0%), DDOG (sold 2026-06-22), NOW (sold 2026-06-22), ARM/AGC/Hirano/MongoDB (exited Jun rotation).

_holdings.md is authoritative. This list caused a held-vs-sold error 2026-06-27 when stale — keep it synced on every portfolio screenshot._

## §7. PENDING PREDICTIONS (canonical ledger = `predictions/grading-log.md`; read its NOT-CANONICAL row tags)

- **SUMCO Q2 FY2026 pre-registration (print 2026-08-06):** canonical = `predictions/2026-07-11-SUMCO-Q2-FY2026-preregistration.md` (rev/OP/net bands + 5 guidance-language P's + three-outcome table).
- **SKHY gate-vs-override grading LIVE:** premium template runs at every close from Jul-13 (`companies/SKHY/thesis.md` — anchors: WI +15.6% / entry +19.3-19.7% / gate ≤~5%); one-way fungibility + TSMC-ADR ~+21% precedent booked 2026-07-12.
- **NBIS T+30 GRADED-FINAL 2026-07-22**: H3-exceeded price / CONFOUNDED mechanism → B48/R2 UNGRADEABLE (5 idiosyncratic catalysts incl. NVDA 9.3% 13G T1); B48 stays N=0; L40 CANDIDATE. Artifact in cross-source-log 07-22.
- **Earnings board (2026-07-02 program):** TSMC Q2 call Jul-16 (June monthly Jul-13), ASML Jul-15, NOW Jul-22 (IR-pinned 2026-07-12), SK Hynix Jul-29 (T1-pinned 07-13; GP-bridge first run + pre-registered miss-isn't-bearish ladder in SKHY thesis), MURATA Jul-31, Samsung full Jul-30 (IR-pinned 2026-07-12), SNDK Aug-5 + Investor Day Aug-13, KIOXIA Aug-07, SUMCO Aug-06.
- **CXMT IPO:** price Jul-15 / subscription Jul-16 — adjudicates the Nanya-deep-dive capacity-mix conflict + Nanya trigger (b).
- **GRADE debt: NONE** — the long-carried "MU 3-layer backfill owed" was PHANTOM (full grade existed since 07-06; row+prose synced 07-20). Samsung Q2 prelim GRADE completed Jul-7/8.


## §7.5 — DURABLE CARRY-OVERS (was the 07-14 session deltas; pruned 07-31, note at end)

- **Funding-node tell #11** (asset-level distribution) — 3 axes (#9 lending / #10 issuance / #11 asset); node NOT fired; weights 40/40/20.
- **#45** event-anchored re-evals; **B64** binding on NOW re-entry. **Hindsight-gate** (meth. candidate 07-15): 5 tests before any miss→lesson booking; loss function declared at registration.
- **#48 CANDIDATE EARNINGS-SEQUENCE READ-THROUGH:** don't act on a scheduled print (priced by arrival) — reconstruct from already-reported adjacent/upstream names (calendar = dependency graph). Caveat: illuminates only the leg whose upstream already printed; ask if that leg is the BINDING uncertainty.
- **#49 CANDIDATE OPERATOR-INTENT / MISSED-LOOP MANDATE:** extract directional intent not literal words; surface the higher-value loop the instruction skips (red-teams the QUESTION; #18 red-teams the conclusion).
- **FACT LAYER: read `meta/data-access.md` BEFORE fetching any market/filing data** (keyed APIs NEVER-ECHO + keyless clients at `meta/tools/`; facts-first wake order #43b/3e).
- **L34 (N=2): harness claims need same-turn source reads; harness CODE changes need an independent verifier before reported applied.**

_Pruned 07-31 (cap, §0): 07-14 macro snapshot, SKHY GP-bridge gate, enterprise-memory bullet, ASML/TSMC grade note — all resolved, canonical elsewhere._

## §8. UPCOMING RECALIBRATIONS / AUDITS (refreshed 2026-07-12; next 90 days)

- **2026-08-06** — Structural-output normalized-metric decision (fires ÷ commits) + SUMCO print
- **2026-08-11** — Prompt-library re-eval (`meta/prompt-library.md` falsifier: unused = decorative)
- **2026-08-12** — session-prime-cascade-hook falsifier check (hook built 2026-07-12)
- **2026-09-11/12** — Question-generation asymptote falsifier + constraint-differential quarterly sweep + B45 cohort quarterly recalibration
- **2026-10-11** — Worldview quarterly revision + end-demand-durability model re-eval
- **PAST-DUE (canonical in `meta/todo.md`, surfaced by session-start): #37/#16 (07-15), monthly audit (07-24, P0), #17/#18 (07-27), BOTTLENECK-FORECAST (06-04).**

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

### §9c — 2026-07-07 codification batch — **PRUNED 2026-08-04 to fit the 30,000-char injection cap.** Principles #43 configuration-over-capability / #43b COMPUTE-INSTEAD-OF-NARRATE / #44 detection-over-prediction are all carried in `CLAUDE.md`'s loop header and `meta/methodology.md`; the batch narrative added no orientation value the IDs don't. Full text: `meta/methodology.md`.

## §10. ARCHITECTURE NOTE — how this file gets maintained

Per Critical Rule #13 cascade discipline: every commit adding a new bias/lesson/principle/rule/TC cluster MUST update this file in the same changeset — ENFORCED by `session-prime-cascade-hook.py` (v2 ID-set-diff rebuild 07-14; live catch 2026-07-19 on #47). Monthly audit continues.

**Curation rule location:** §0 above (codified 2026-06-24). The curation rule is embedded in this file rather than a separate file because the rules that govern injection ARE themselves part of what the session needs to know cold.

## §11. FALSIFIER FOR THIS FILE ITSELF

If a 30-day audit shows that having session-prime loaded produced ZERO measurable reduction in the bias-recurrence rate (e.g., I still flag +7-10% single-day moves as "extreme" without referencing B45 baseline), then the file is decorative noise and should be retired (along with the hook). Detectability: grep transcripts 2026-06-12 → 2026-07-12 for magnitude-categorizing language WITHOUT B45 reference. POSITIVE = <2 instances; NEGATIVE = ≥3 instances → retire OR refine selection rules.

**Extended falsifier (added 2026-06-24):** if monthly audit produces zero demotions + zero additions for 3 consecutive cycles, the curation rule is working but the file is not evolving — check whether the OS has stagnated or the curation rule is too aggressive.

- **PC-20/21/22 (07-20/21):** PC-20 export-control DESIGN-AROUND (~50%, re-eval 08-20) · PC-21 listing/monetization wave (proceeds-use tell; ~45%, re-test 08-13) · PC-22 AI-LEVERAGE OPACITY MIGRATION (credit+insurance+sovereign channels → private/opaque structures; BIS-complement; re-eval 08-21). All CANDIDATES — track, don't cite as priors.
