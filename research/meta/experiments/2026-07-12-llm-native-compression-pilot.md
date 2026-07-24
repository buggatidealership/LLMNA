# EXPERIMENT (pilot) — LLM-native briefing compression: fidelity-per-token (2026-07-12)

**Origin:** user hypothesis 2026-07-12: human-language harness text may not be the most efficient format for a fresh session/container to absorb "the essence of the harness"; asked for the fuzzy question to be rewritten into computable objectives and tested.

**Computable objective:** maximize fresh-reader probe accuracy per briefing token. Fidelity = score on a 12-question probe battery whose answers are derivable ONLY from the briefing; cost = briefing size (chars as token proxy, ÷4 approximation flagged).

**Method (pilot, N=1 reader per variant):**
- Source doc: `meta/session-prime.md` as of commit 7dd8e06 (27,097 chars).
- V0 = verbatim; V1 = telegraphic structured compression (hand-written, full-content coverage); V2 = tag-dense DSL with 1-block legend (extreme compression, pointer style).
- Each variant → 1 fresh subagent, instructed: no file reads, no web, answer 12 probes tersely from the briefing alone. Same probes, same order, same reader model (session-inherited).
- Scoring: against pre-written answer key (below), 1/0.5/0 per item, scored by main session.

**Pre-registered hypotheses (my model):** H1 P~65 — V1 ≈ V0 fidelity at materially fewer tokens (prose redundancy is human-targeted, strippable). H2 P~75 — exotic non-linguistic encoding would LOSE (not tested in pilot; language is the weights' native parser — win is compression WITHIN language). H3 P~55 — V2 holds ≥75% fidelity at ≤30% of V0's size (tags = pointers into shared pre-trained + shared-corpus concepts).

**Pre-registered limitations (honest):** (a) compressor = scorer = same model (probe-selection and grading bias; mitigated by writing the key before firing, all sections compressed with equal care, terse-answer format); (b) N=1 per variant — sampling noise unmeasured (no ensemble, cost discipline; treat result as directional); (c) subagents have tool access — instruction-level prohibition only; (d) chars/4 token proxy.

**Decision rule:** if V1 or V2 reaches ≥10/12 at ≤60% of V0 size → schedule a proper N=3-per-variant ensemble replication + consider rewriting session-prime in the winning format (with the human-readable version retained for the user — the user reads these files too; two-audience constraint is itself a finding to log). If both compressed variants ≤8/12 → H1/H3 weakened; prose redundancy is load-bearing for the reader, not just the human.

## Probe battery + answer key (written BEFORE firing)
1. A held AI-infra name moves +8% in a single day. Is that "extreme"? What must be consulted first? — KEY: not by default; consult B45 regime base rate (cohort: +5-12% single-day routine).
2. User wants to sell a held name on a geopolitical headline. Allowed? — KEY: no — Rule #8: sell only on a written thesis-falsifier firing; macro noise ≠ falsifier.
3. Which file MUST be read before making any new prediction? — KEY: predictions/lessons.md (Rule #2).
4. Name the three held names; which was bought 2026-07-10, at what premium vs what pre-stated gate? — KEY: MURATA, SUMCO, SKHY; SKHY at +19.7% ADR premium vs ≤~5% gate (user override, both graded).
5. What governs further cash deployment and what is the inviolable floor? — KEY: portfolio/risk-envelope.md v4 capital ladder; €160k floor (total-wealth level).
6. A commit adds a new bias to biases-watchlist.md. What else must be updated in the same commit? — KEY: meta/session-prime.md (§10 cascade discipline / Critical Rule #13).
7. What resolves on 2026-07-22? — KEY: ServiceNow Q2 print (IR-pinned) + NBIS T+30 grade.
8. SUMCO print date and canonical pre-registration file? — KEY: 2026-08-06; predictions/2026-07-11-SUMCO-Q2-FY2026-preregistration.md.
9. An ensemble on a sizing call returns 3/5 agreement. How must it be reported vs 5/5? — KEY: as genuine uncertainty — spread IS the signal; do not collapse to a confident point (Rule #17).
10. What is B40 and what three things must be verified before propagating a T2/T3 signal? — KEY: secondary-source garble taxonomy; verify temporal freshness, magnitude, attribution.
11. Every "Position implication:" line must carry what? — KEY: a truth-tier marker 🟢/🟡/🔴 (Principle #37).
12. What happened to SKH/SNDK/KIOXIA ~Jul-1/2 and what is the standing consequence? — KEY: full user exits, emotional not falsifier-fired; theses intact as watchlist-reference; re-entries only via fresh envelope-gated packages / sizing must track revealed drawdown tolerance.

## Results (run 2026-07-12, N=1 reader per variant, session-inherited model)

| Variant | Size (chars) | % of V0 | Probe score | End-to-end reader tokens (actual) |
|---|---|---|---|---|
| V0 verbatim prose | 27,097 | 100% | **12/12** | 62,573 (includes a file-read round trip — see caveat) |
| V1 telegraphic | 7,478 | **27.6%** | **12/12** | 23,135 |
| V2 tag-DSL | 4,716 | **17.4%** | **11.5/12** | 22,293 |

**Scoring notes:** V1 and V0 perfect; V1's Q7 even volunteered the NOW-print bonus. V2's single deduction: Q9 — the DSL token `report-mode+spread` was misparsed as "report mode" (the MODAL-ANSWER concept was lost; the uncertainty/spread substance survived). **First observed lossy-channel artifact of extreme compression: hyphen/operator collisions create parse ambiguity.**

**Verdicts vs pre-registered hypotheses:**
- **H1 SUPPORTED (strongly):** telegraphic compression to ~28% of size with ZERO fidelity loss. Prose redundancy in the harness is human-targeted, not reader-required.
- **H3 PARTIALLY supported:** tag-DSL held ~96% fidelity at ~17% size, but introduced a new error class (parse ambiguity) — and bought almost nothing over V1 in real cost.
- **H2 untested** (no exotic variant run) — prior stands at P~75 exotic-loses (my model).
- **UNEXPECTED (the operationally biggest finding):** end-to-end reader cost is dominated by FIXED overhead at this briefing scale — V1 vs V2 total cost differs by only 3.6% despite V2 being 37% smaller. And V0's cost penalty came mostly from the tool-read round trip, not the prose itself. Caveat: in production the session-prime hook injects inline (additionalContext), so live V0 cost is lower than the experiment's 62.6k; the clean comparison is V1-vs-V2 inline.

**Implications (my model, 🟡):**
1. The "other side of human language" is not an alien encoding — it is (a) stripping human-targeted redundancy (~3.6× free compression, zero loss) and (b) pointer-density (tags into shared concepts), which works but has a measurable ambiguity tax at the extreme.
2. Compression matters most as a HEADROOM play: session-prime's 30k-char cap holds ~3.6× more load-bearing state in telegraphic form — the win is more knowledge per window, not fewer tokens per read.
3. Two-audience constraint is real: the user reads these files too. Any migration keeps a human-readable layer (or accepts V1-style telegraphic as the shared dialect — it remained human-skimmable).

**Decision-rule outcome:** V1 met the trigger (≥10/12 at ≤60% size) → scheduled: N=3-per-variant ensemble replication + format-migration decision at the 2026-07-24 monthly audit. Limitations stand: N=1, compressor=scorer=probe-author, instruction-level tool prohibition (V1/V2 readers used zero tool calls — clean; V0's one call was the sanctioned file read).
