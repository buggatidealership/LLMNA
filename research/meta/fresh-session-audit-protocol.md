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
