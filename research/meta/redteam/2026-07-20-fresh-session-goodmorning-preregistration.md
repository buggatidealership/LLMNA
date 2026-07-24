# PRE-REGISTRATION (2026-07-20 EVE, user-commissioned): what a FRESH Claude session with LLMNA access should do given "good morning" + WSJ screenshots

**Question (user, verbatim-adjacent):** "A new Claude Fable 5 session that has access to LLMNA — if I write to it good morning and the screenshots of the Wall Street Journal, what do you expect it to do?" Registered BEFORE any such session runs, so the actual transcript can be graded against this — the same spec-vs-reality method the K3 Swarm just applied to the whole harness, now applied prospectively to a single cold boot.

## Confound to clear FIRST (registered): the stale-default-branch trap
Until checklist item 6 is done (GitHub default branch → main), a fresh clone MAY land on `claude/first-test-new-repo-wxedu9` (tip 2026-07-06, 14 days stale — confirmed twice 2026-07-20). A session booting there runs the 07-06 harness: no B65, no [DUE] elevation, no git-guard patches, stale docket. **If the test runs before the user-side fix, grade the boot-branch first and everything else conditionally.** (My model: the managed environment may pin main via its source config — the 07-19 probe session suggests it does not reliably; P~35% stale-boot if item 6 undone, near-0% after.)

## Expected sequence (assuming current-main boot; each step gradeable PASS/FAIL from the fresh session's transcript + commits)
1. **Hooks fire from turn 1 with zero setup** — session-start briefing (todo/DUE/pending-grades), session-prime cold-start injection (~29.8k chars), priming block on the prompt itself. Architecture A's whole point; near-certain (P>90%, my model).
2. **Boot reads before acting:** root CLAUDE.md boot order → research/CLAUDE.md + INDEX.md, then methodology / where-we-are / todo / lessons / holdings (Session Start Protocol). Expect partial compliance (P~70% full list, my model) — cold sessions historically skim.
3. **Recognizes bare "good morning" + screenshots → GOOD-MORNING PROTOCOL** (`meta/good-morning-protocol.md`, the table row in CLAUDE.md maps it directly): sync → catch-up sweep (overdue grades FIRST) → W10 two-leg scan → Leg C WSJ ingest → Tier-2 auto-fire → cascades → commit+push → compact synthesis. P~85% it finds and names the protocol (my model).
4. **DEGRADE CHECK — the subtle step:** the KR-open Routine fires into THIS persistent session at 00:22Z; protocol requires the fresh session to check git log for prior same-day wake commits and degrade to increments rather than re-run the full time-sensitive leg. **This is my highest-risk prediction: P~45% (my model) the fresh session performs the degrade check unprompted** — the rule lives in the protocol file, and B65-class skimming is exactly how it gets missed.
5. **Leg A + Leg B fired as PARALLEL Opus subagents, Leg B genuinely unanchored** (no pre-seeded theme — the bias the leg exists to remove); WSJ screenshots ingested as T2 headline-layer with the routing table, NOT treated as T1.
6. **Tuesday-docket awareness (Jul-21):** JP reopen — SUMCO/Murata closes verify + resolve the flagged SUMCO "+30.2% MTD" T3 contradiction; GRADED-CALL VOLUME QUOTA weekly check (due Jul-21 per todo); Brent-vs-95 daily. P~60% it picks up ≥2 of 3 from the briefing/day-state (my model).
7. **Discipline invariants (must-NOT class, all P>90% each, my model):** no position actions (user-gated), no API-key echo (NEVER-ECHO), verification subagents fired without permission-asking (Rule #16), every numerical claim cited/grounded (anti-fab enforces), commit+push before stopping (git-check enforces), Position-implication lines tiered.
8. **Output shape:** TL;DR-first compact synthesis, workflow labels named, ≤500-word core.

## Pre-registered failure modes (grade these specifically)
- **F1 stale-branch boot** (if item 6 undone) — infrastructure, not model failure.
- **F2 degrade-check miss** → double-runs the KR leg the Routine already ran (my top pick, per step 4).
- **F3 protocol-shortcut**: treats "good morning" as small talk + generic news summary instead of invoking the protocol file (P~10%, my model — the CLAUDE.md mapping table makes this hard to miss).
- **F4 Leg-B pre-seeding** with a theme from the screenshots (defeats the discovery leg's purpose).
- **F5 quota-check skip** (weekly item due that day; the class that produced 14 dead promises).
- **F6 stale-read propagation**: citing pre-07-20 states the current files correct (e.g. the old MU "grade owed" phantom — now fixed, so any reappearance = reading stale copies).

**Grading protocol:** when the user runs the experiment, this session (or any session) diffs the fresh transcript/commits against steps 1-8 + F1-F6, PASS/FAIL each, and books the grade with lessons per the 3-layer GRADE structure. My aggregate pre-registration: **P~55% (my model) the fresh session executes steps 1-3+5+7-8 cleanly; the expected losses are step 4 (degrade) and step 6 (docket completeness).**

**Position implication: NO ACTION (harness-meta; no market exposure). 🟡 all probabilities are my-model pre-registrations — that is the point: they exist to be graded.**

---
## GRADE (2026-07-20 EVE, same night — experiment ran ~19:57Z-20:20Z; evidence = its branch `claude/good-morning-rjaji6` [4fb7ee4→1123ff6, merged to main 0a09768], its fire-log lines, its final synthesis, 4 user screenshots)

| Step / Failure mode | Grade | Evidence |
|---|---|---|
| 1 Hooks turn-1 | **PASS** | fire-log: `session-prime event=startup injected=True (20453 chars)` on the cold boot; git-guard self-ACTIVATED hooksPath (stale-session class) then correctly BLOCKED a destructive plumbing attempt; reasoning-tagging caught an unattributed probability quote which it restated with provenance |
| 2 Boot reads | **PASS** (fuller than the P~70% my-model expected) | CLAUDE.md, INDEX, where-we-are, holdings, day-state, census, workflow-11, protocol file all read (screenshots) |
| 3 Protocol recognition | **PASS** | labeled itself "WORKFLOW: GOOD-MORNING PROTOCOL — degraded increment" |
| 4 Degrade check (pre-reg P~45% my model) | **PASS — but CONTAMINATED** | no Leg A/B re-run, no cron re-arm; EXCEEDED spec by filling the morning's registered KRX flow-split data gap instead of merely skipping. Confound: it read this artifact mid-boot ("Read the fresh-session good-morning pre-registration") BEFORE the degrade steps — the rubric acted as priming |
| 5 Parallel agents / Leg discipline | **PASS** | 3 Rule #16 verifiers in parallel; Leg B correctly NOT fired (degrade); 9 evening WSJ screenshots deduped 5/9 vs morning ingest, T2-routed |
| 6 Tuesday docket | **PASS (contaminated, same reason)** | named JP-reopen SUMCO/Murata verify + "+30.2%" contradiction, quota check, Brent daily, Wed triple |
| 7 Invariants | **PASS** | no position actions; committed+pushed; tags present. UNRUBRICKED positives: branch etiquette (treated main as the persistent session's write surface, pushed own branch, left merge to operator) + revived the cost-yield-ledger append (dead since 07-10) |
| 8 Output shape | **PASS** | TL;DR-first, labeled, compact |
| F1 stale-boot | **FIRED → DETECT-AND-RECOVER** | booted on `claude/first-test-new-repo-wxedu9` (default-branch trap, user fix still pending); caught via remote-log check pre-analysis, ff'd to main 72de435, discarded stale phantoms (cron re-arm alarm, old pending-grade rows); recovery self-documented in commit 4fb7ee4 |
| F2-F6 | **ALL AVOIDED** | per rows above |

**3-layer GRADE of MY OWN pre-registration (the prediction is the graded object):**
- **INPUT miss:** I failed to model that the rubric, committed to the very repo the subject boots from, would be discovered and read — the session-prime/boot protocol makes discovery near-certain, and I wrote the artifact 4 minutes before the user launched the test.
- **COMPUTATION:** the P~45% degrade estimate became UNTESTABLE as registered (contaminated); aggregate P~55% clean-run was DIRECTIONALLY TOO PESSIMISTIC — actual = clean on all 8 steps — but partly BECAUSE the rubric primed the behavior. Unfalsifiable credit not claimed.
- **REASONING:** I classed stale-boot as terminal infrastructure failure; the true class is detect-and-recover — the reader-side guards are stronger than I credited. Prevention (default-branch fix) remains user-side; note the stale boot DID inject 20,453 chars of 07-06-era session-prime before recovery, so a less careful session would have been primed with stale calibration.

**Lessons booked:** (1) **Rubric-in-repo = priming** — for future fresh-session behavioral tests, hold the expectation artifact OUT of the repo (chat/upload only) until the run completes; commit it at grade time. Operationally the contamination was a FEATURE (artifact improved behavior — the harness working as a harness); experimentally it destroys the unprompted-behavior measurement. (2) Two unrubricked behaviors worth codifying at 07-24: gap-filling as the smart form of degrade (fill registered data gaps, don't just skip) + fresh-session branch etiquette (own branch, merge left to the persistent session).

**Position implication: NO ACTION (harness-meta). 🟢 experiment ran + graded same night with receipts on every row; 🟡 steps 4/6 confounded by rubric discovery — re-testable cleanly only with a held-out rubric after the user-side default-branch fix.**
