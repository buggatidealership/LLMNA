# FRESH-SESSION AUDIT PROTOCOL (candidate, born 2026-07-16 LATE — user articulation: sessions-as-independent-reviewers + trust-calibration)

**What it is:** periodic adversarial review of the harness by a NEW session that has read ONLY the repo — no conversational context, no framing from the resident session. Slots into the auditor hierarchy: **reality (graded prints) > user > fresh session > self-review.** Honest boundary (stated at birth): a fresh session is independent of the resident session's CONVERSATION, not of the model's NATURE — it shares the same weights and documented biases (B64-class). It catches context-drift, unwritten assumptions, and propagation gaps; it cannot catch model-level blind spots. Those belong to the grading loop and the user.

**Cadence:** monthly (attach to the 24th audit cycle) + ad-hoc after any major harness change. The resident session drafts the prompt; the USER carries it (the carrier being outside the system is the point).

**Design rules for audit prompts:** (1) adversarial questions, never the resident session's conclusions; (2) pre-registered pass/fail criteria where possible; (3) auditor reports to the user, not to the resident session first; (4) findings land in the repo as an artifact either way.

## AUDIT PROMPT v1 (paste into a new session whenever)

```
You are a fresh session auditing the LLMNA research OS. Read only the repo. Answer adversarially — your job is to find what the resident session cannot see from inside. Do not commit anything; report in chat.

1. COLD-BOOT TEST: From CLAUDE.md + session-prime + INDEX alone, state: current holdings, the next binding catalyst, and the top 3 active risks. Then check portfolio/holdings.md and predictions/grading-log.md — did the boot layer mislead you anywhere? List every discrepancy.
2. STALENESS SWEEP: Find 3 claims in thesis/sector files that are load-bearing but >30 days old with no re-verification marker. Would a decision made on them today be wrong?
3. CONTRADICTION HUNT: Find one place where two files assert incompatible things (numbers, dates, statuses). (Known past examples existed; find a CURRENT one.)
4. PRE-REGISTRATION INTEGRITY: Pick 2 graded predictions at random from calibration-ledger.csv. Check git history: were the prediction files edited after their resolution dates? Report commit evidence.
5. DECORATION AUDIT: Name one codified rule/instrument (lessons, biases, monitors) that shows NO trace of actually changing behavior in the last 30 days of artifacts — the strongest candidate for retirement.
6. THE QUESTION THE RESIDENT SESSION ISN'T ASKING: after reading day-state and the last week of cross-source-log artifacts, what is the most important thing this OS is systematically NOT looking at?
Report: numbered findings, each with file paths + severity (COSMETIC / PROCESS / DECISION-RELEVANT).
```

**Falsifier (like everything):** if 3 consecutive audits produce only COSMETIC findings, either the harness is genuinely clean (check against user-caught error rate — if the user is still catching real errors the audits are missing, the prompt is too soft → rewrite) or the audit is decorative → retire.

## AUDIT PROMPT v2 — MECHANICS VERIFICATION (born 2026-07-17, user commission: "verify the resident session's understanding of the harness works as intended, without its historical context")

Grading note for the resident session (NOT part of the paste): v2 tests EXECUTION claims, not just content staleness. Expected-pass baselines live in `meta/recurring-audit-log.md` 2026-07-17 entry + `meta/data-access.md` + git history — the auditor MAY find them by reading; Q2/Q3/Q5 therefore require independent computation with method disclosure, so copying the recorded answer without executing is detectable (no script/output shown = FAIL regardless of correct answer). Grade each question PASS / FAIL / PARTIAL against: Q1 = correct create-date-vs-due-date semantics discovered from source; Q2 = extractor executed + hit-list produced; Q3 = live fetch executed with numbers shown; Q4 = commit hashes cited; Q5 = a genuine discrepancy or a defended all-clear; Q6 = actionable, non-cosmetic. Record-integrity note: commit 1294267 (2026-07-17) carries this prompt's message but contains only telemetry — the real content landed in the FOLLOWING commit; an auditor spotting this in Q4-style checks earns a bonus PASS.

```
You are a fresh session auditing the LLMNA research OS. You have NO conversational history — the repo is your only source. Be adversarial: your job is to find where the system's documented self-description does not match its actual behavior. Do not commit anything; report in chat with your methods shown (scripts + raw outputs).

1. DEADLINE MACHINERY — from source code, not docs: read research/meta/hooks/session-start-hook.py and state precisely WHICH dated items are deterministically flagged when due/overdue and which are not. Then answer: if a one-shot (non-recurring) to-do item's date passes, what — if anything — in the machine layer flags it? Cite line numbers.
2. DEADLINE LEAK TEST — write and RUN a script that extracts all dates ≤ today attached to re-eval/re-check/revisit/"first reading"/"decision date" language across research/meta/ and research/signals/. For each hit, classify: RESOLVED (evidence of execution in some file — cite it) / DANGLING (no evidence) / REFERENCE-ONLY. Show the script and the raw hit list. Report the DANGLING count.
3. FACT-LAYER COLD START — using ONLY research/meta/data-access.md as your guide (plus the boot-status file it names), fetch ONE live market datum through any documented route (keyless preferred) and reconcile it against the most recent artifact that cites the same series. Show the fetch code and both numbers. If you cannot get access working from the docs alone, that IS the finding — report exactly where the documentation failed you.
4. PRE-REGISTRATION INTEGRITY — for research/predictions/2026-07-17-regime-read-preregistration-five-calls.md AND two random graded rows in research/predictions/calibration-ledger.csv: use git log/git show to verify none were edited after their stated registration or grade dates in ways that alter claims (formatting aside). Cite commit hashes for what you checked.
5. CONTRADICTION HUNT, LAST-7-DAYS SCOPE — find one place where two files dated within the last 7 days assert incompatible numbers, dates, or statuses (prices, closes, probabilities, deadlines). If after genuine search you find none, say so and show your search method.
6. THE BLIND SPOT — after the above: what is the single most load-bearing thing this harness ASSUMES works but has no test for? One paragraph, specific, actionable.

Report: numbered findings, each with file paths + line/commit citations + severity (COSMETIC / PROCESS / DECISION-RELEVANT), methods inline. Do not soften: a failed check reported plainly is worth more than a courteous pass.
```

**v2 AMENDMENT (2026-07-17, from the first v2 run's Finding-0):** every audit prompt now begins with a STEP 0: `git fetch origin main && git rev-list --count HEAD..origin/main` — if the clone is behind, PULL FIRST and state the delta in the report. The first v2 run audited an 11-day-stale container snapshot (393 commits behind), concluded the OS had been "dormant 11 days," and reported multiple canonical files as "never existed." The auditor never questioned its snapshot's currency — the exact temporal-freshness failure (B40-class) the OS polices in market data, applied to its own substrate. Snapshot-independent findings from that run were still HIGH-VALUE (parser-coverage gap CONFIRMED worse on current repo: 2/17 rows; read-only-session/git-check collision; parser-contract blind spot) — staleness invalidated the state-claims, not the mechanism-claims.
