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
