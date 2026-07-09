# GOOD-MORNING PROTOCOL — user-triggered daily wake (codified 2026-07-09, user directive)

**Trigger:** the user writes **"good morning"** (bare, any language variant) — optionally with WSJ screenshots attached.
**Design intent (user, 2026-07-09):** until the platform routines are fixed (browser item 0) — and possibly instead of them — the user himself is the scheduler: one phrase each morning fires everything the KR/JP wake + catch-up would have done. The phrase is the routine.

## Execution order (all steps, every time)
1. **Sync:** `git fetch origin main && git checkout main && git pull` — repo is the only memory.
2. **Catch-up sweep:** read `meta/day-state.md` docket; execute anything overdue — pending grades (grading-log Pending rows), unresolved self check-ins, data-gap reconfirms (e.g., exact closes), catalyst-clock events that resolved overnight. This step FIRST — the freshest scan is worthless if yesterday's grades are dangling.
3. **Two-leg scan (Workflow #10), region = KR/JP + overnight-global**, timed off the actual trigger hour: Leg A portfolio-anchored + Leg B unanchored discovery, both Opus, in parallel, past-24h window, named source roster, T-tiers, artifacts to cross-source-log.
4. **Leg C — WSJ ingest (if screenshots attached):** see §Leg C below. Runs in the MAIN LOOP (no subagent needed for the headline layer).
5. **Tier-2 auto-fire** per the lifted gate for anything crossing trigger criteria; ≤2 Opus baseline + escalation conditions per day-state; every fire → ledger, same commit.
6. **Cascades per Critical Rule #10** (theses/TC/candidates/day-state/registers) + heartbeat-log line ("user good-morning wake") — one commit, pushed.
7. **Reply:** compact synthesis — tape table, keystone verdicts, Leg B delta, Leg C delta, catalyst clock next-72h. Materiality gate governs push-notification framing.

## §Leg C — WSJ screenshot ingest (the user's third channel, added 2026-07-09)
- **What it is:** user's WSJ subscription — headline screenshots of Top Stories / Markets / Tech / U.S. / World / Economy sections. This is a CURATED WESTERN EDITORIAL CONTAINER — exactly the attention-function Leg B borrows from editors, but delivered through the user's paywall (solves the systematic 403/paywall blocks on our side; WSJ/FT-class hosts refuse our proxy).
- **Tier discipline:** screenshot headlines = **T2 headline-layer** (publisher T1-class, but headline ≠ article body — do NOT book numbers from a headline; article-level claims need a WebSearch corroboration pass or explicit headline-only flag).
- **Processing:** (a) extract every investing-relevant headline; (b) classify per the channel-coverage model (segment | region | direction); (c) route: held-name/thesis items → Tier-2 verify if threshold-crossing; known-thread items → thread updates (dedup vs Twitter channel — WSJ and FinTwit often carry the same story a day apart, B40 check both directions); complement items (macro/FX/energy/geopolitics/non-AI) → absence-question register + day-state; (d) ONE ingest artifact per morning batch in cross-source-log with a routing table.
- **Channel-model note:** WSJ screenshots are the COMPLEMENT-heavy channel (macro/rates/FX/geopolitics/cross-sector M&A) — they attack the user's own FinTwit shape. The histogram tags both channels separately (source-type: twitter-relay vs wsj-headline).
- **Value calibration (from the 2026-07-09 pilot batch of 20):** highest-yield sections for this book = Markets (incl. Commodities/Currencies), Tech, World/Economy. Heard-on-the-Street pieces are analyst-grade context (T2 named-publisher opinion) — flag as HOTS, never as consensus.

## Relationship to the platform routines
Routines (once repo-fixed) automate the SAME spec at fixed clock times with no user action. The good-morning path stays valid permanently as (a) the manual override, (b) the WSJ-attachment channel (screenshots can't ride a routine), (c) the fallback when routines fail. If both fire the same morning, the second run is a cheap catch-up (docket already clean → it degrades to Leg C + increments only).

## Fluidity metadata
Codified 2026-07-09 (user articulation). Falsifier: if 14 days of good-mornings produce Leg C routing tables where <20% of routed items ever touch a thread/thesis/register, the WSJ layer is decorative — trim to Markets+Tech sections only. Re-eval at the 2026-08-09 channel-model audit.
