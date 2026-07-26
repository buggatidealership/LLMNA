# 2026-07-26 — NEW SESSIONS LAND 669 COMMITS BEHIND: stale-base-branch diagnosis

**Origin:** operator report 2026-07-26 ~09:20 UTC — *"it seems like when I create a new session it ends up landing on an outdated version of the repo."* Diagnosed from repo data, not inference. Every figure below is computed; commands are reproducible.

## Verdict

**New sessions branch from `claude/first-test-new-repo-wxedu9`, which has been frozen at `344962f` (2026-07-06 16:06 UTC, the LLMNA-migration commit) ever since. `main` carries 669 commits after it.**

## What is NOT the cause (ruled out first)

- **Push path / git proxy.** GitHub `main` = `769fdbc` = this session's local HEAD, byte-identical. Pushes land correctly. The `http://127.0.0.1:41729/git/...` proxy is not caching stale state.
- **A protected/diverged default branch.** `main` is the default and is current.

## Evidence chain (computed)

| Check | Result |
|---|---|
| GitHub `main` tip vs local HEAD | both `769fdbc` — in sync |
| `claude/first-test-new-repo-wxedu9` tip | `344962f`, **2026-07-06** — unmoved for 20 days |
| `main` commits after `344962f` | **669** |
| Newest session branch `claude/new-session-drppai`, oldest own commit `80708ca` (07-23) | parent = **`344962f`** → started 669 behind |
| Other `claude/*` branches created 07-12, 07-16 (×2), 07-19 | all fork from **`344962f`** → base is pinned to the stale branch, NOT to `main`-at-container-start |
| That session's own sync commit `671e2da` (07-25 22:39) | *"merge origin/main into claude/new-session-drppai (668 commits behind -> live state)"* — the affected session states the gap itself |
| `344962f` ancestor of `main`? | **YES** → updating that branch to `main` is a fast-forward, not a history rewrite |

Reproduce:
```
git merge-base --is-ancestor origin/claude/first-test-new-repo-wxedu9 origin/main   # exit 0
git rev-list --count 344962f..origin/main                                           # 669
git log -1 --format=%P $(git rev-list --reverse origin/main..origin/claude/new-session-drppai | head -1)
```

## Realised cost — this is not hypothetical, it fired twice

1. **The harness was declared dead on false evidence.** The stale session graded a *"17-day dead window Jul-7 → Jul-23, zero autonomous commits, CronList empty"* as **FAIL-infrastructure, "largest gap in harness history."** `main` has **587 commits** in that window — every single day, 13–58/day (`git log --since=2026-07-07 --until=2026-07-24 origin/main`). Retracted by that session in `4d18537` once it merged. **The clone stopped on 07-06, so the absence of commits after 07-06 was an artifact of the checkout, read as a fact about the world.**
2. **The over-constraint audit ran 668 behind.** Per `2a11a27`: of four HIGH-tier hook fixes the operator authorised, **three were withdrawn on live re-measure** — including retiring `structural-output` + `llm-native-priming`, which *"would have overridden the operator's 2026-07-06 keep-both decision and destroyed a running experiment 12 days before its 08-06 adjudication."* **A stale base nearly caused a Rule #19 HIGH-tier deletion of live enforcement on operator authorisation obtained under false premises.**
3. **Duplicated work.** That session ran an Opus-5-vs-Fable-5 deep dive on 07-25 (`bdd5e75`); this session ran its own on `main` the same day (`a6cf7ab`).
4. **Re-grading already-graded predictions** — Samsung prelim / ASML / TSMC / NBIS T+30 re-graded in `e256184`, all already resolved on `main`.

## Stranded work — 18 non-merge commits on `claude/new-session-drppai`, NOT on `main`

Includes material worth recovering: a MURATA stale-position-weight correction (`3faac1c`); `da04101` *"session-start: surface branch position before anything else"* — **a hook fix for this exact bug**; a SUMCO Q2 component-level pre-registration lock (`2275462`); a Jul-25 morning-brief ingest (`aeb813e`) whose subject references *"Korea-US $950B memory deals ANNOUNCED"* — **⚠️ UNVERIFIED: that figure is read from an unmerged commit SUBJECT LINE only; it is not grounded in any file on `main`, no source was checked by this session, and it must be verified before any cascade or restatement.**

## Corrections to existing harness state

- **`meta/day-state.md` "Operating mode note (2026-07-06 EVE) — SINGLE-SESSION MODE" is STALE and now actively misleading.** It asserts *"this session is the ONLY live thread"* and that *"any main-branch commit NOT from this session = a platform Routine firing or an anomaly to investigate."* At least two sessions are concurrently live (the other committed `766d09d` at 2026-07-26 09:06 UTC). That note's provenance rule would misclassify a sibling session's commits as anomalies.
- The 07-23 `W11 WAKE-AUDIT-3` "FAIL-infrastructure, 3rd instance / 17-day dead window" finding is **VOID** — it is measurement error from the stale checkout, already retracted at source (`4d18537`). It must not be counted as a wake-infrastructure failure instance if it reaches `main`.

## Fix

1. **Durable (operator-side, the actual fix):** point the session/environment config at `main` rather than `claude/first-test-new-repo-wxedu9`. Same repo-selector class as the pending Routines fix in the standing browser checklist.
2. **Mitigation (agent-side, safe):** fast-forward `claude/first-test-new-repo-wxedu9` → `main`. Verified fast-forward (ancestor check above), so no history rewrite and no Rule #19 exposure; reversible to `344962f`, recorded here. Then a new session branching from it starts current even before (1) lands.
3. **Recovery:** triage + merge the 18 stranded commits — deferred while that session is active (last commit 14 min before this diagnosis); merging under a live writer risks conflicts on files it is actively editing.
4. **Prevention:** `da04101` (session-start surfaces branch position) should reach `main` — a session that is told at turn 1 "you are N commits behind" cannot spend two days reasoning on a dead snapshot.

## Generalisable lesson (candidate — goes to lessons.md at N=2)

**Absence of data in a checkout is not evidence of absence in the world.** Both realised failures share one shape: the session read the *edge of its own clone* as a *fact about the repository* — no commits after 07-06 became "the harness died"; hook state at 07-06 became "these hooks are unnecessary." Same family as B65 (context-fluency) and L39 (*"unreachable ≠ fabricated"*): a retrieval boundary mistaken for a substantive finding. **Mechanical guard: any claim of the form "X stopped / nothing happened / this is inert" must first establish that the observer could have seen X had it occurred** — for repo claims that means printing the branch position before the conclusion, which is precisely what `da04101` implements.
