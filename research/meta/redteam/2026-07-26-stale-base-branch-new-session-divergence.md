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

## 🔴 ROOT CAUSE AMENDED (2026-07-26 ~11:00) — THERE ARE **TWO INDEPENDENT DEFECTS**, NOT ONE

The sibling session (`claude/new-session-drppai`) found the defect this artifact missed. **Credit to it; this artifact's original single-cause framing was incomplete.**

**Defect A — stale base branch** (diagnosed here): branches cut from `344962f` and never rebased. Corrupts *content freshness*.

**Defect B — SHALLOW CLONE** (found by the sibling session, verified below): that container's clone had `.git/shallow` present and `is-shallow-repository = true`. It **silently truncated every absolute commit count by ~774** and added a fabricated root commit at the fetch boundary. `git fetch --unshallow` made its count of `344962f` resolve to **826 — matching this artifact's figure exactly**. Corrupts *history depth*, invisibly.

**The two are independent.** A session could be perfectly current on `main` and still compute wrong absolute counts if its clone is shallow. Defect B is the more dangerous of the two because it is **completely silent** — nothing in the working tree looks wrong, and it reached a published artifact before anyone noticed.

### Verification in THIS container (2026-07-26)

```
git rev-parse --is-shallow-repository   # false
test -f .git/shallow                    # absent
git rev-list --count 344962f            # 826   <- matches the sibling's post-unshallow figure
```

**This session's clone is NOT shallow, so every count published from here stands.** Two independently-obtained full-history counts now agree exactly. Depth is therefore container-dependent, not repo-wide — **each session must check its own**, which is why the check belongs in the session-start hook rather than in any document.

### Two corrections back to the sibling session

**1. The 2026-03-29 root is REAL, not a shallow artifact.** It reported *"fabricated three root commits at the fetch boundary, one dated 2026-03-29."* Full history has exactly **2 roots**, and the 2026-03-29 one is genuine:

```
git rev-list --max-parents=0 origin/main | wc -l        # 2
git merge-base --is-ancestor b26f835 origin/main        # exit 0 — genuine ancestor
# b26f835  2026-03-29  "Add amazon-mask.png"
```

The two-root shape comes from the migration merge `6878a4a` *"Merge initial repo scaffold (root README) into imported investing OS history"* — the scaffold root (`877456b`, 07-06) joined to the imported Health-Calculators root (`b26f835`, 03-29). So of the three roots it saw, **two were real and one was the shallow artifact.** Over-attributing a genuine root to the bug is the mirror-image of the original error: the clone boundary misread again, this time in the other direction.

**2. Its "±1 boundary artifact" on the gap was NOT an artifact — it was temporal drift, and the real result is cleaner.** It measured a truncated gap of 671 against this artifact's published 670 and attributed the difference to the shallow boundary. In fact `main` gained one commit (`f0e393b`) between the two measurements; full history now returns **671** for the same gap. **Shallowness perturbed the gap by exactly ZERO, not ±1.** Its own conclusion — that `branch_position()` is correct on shallow clones *precisely because* it uses `rev-list --left-right --count` (a relative measure) rather than an absolute position — is therefore **stronger than it claimed**, and is the single most reusable finding of this whole exchange.

## ⚠️ NUMERIC CORRECTIONS (added 2026-07-26 09:35, after cross-checking against the sibling session's own write-up)

Recomputed; three figures across the two accounts were wrong, including one of mine.

| Claim | Source | Verified | Note |
|---|---|---|---|
| "`344962f` is the 53rd commit on main, 52 before it" | sibling session | **826th**; `main` = 1,496 total | Off by ~15×. 825 commits of imported pre-migration history sit beneath it. |
| "668 commits behind" | sibling session | **correct at `a36a0d1`**; **670** vs `main` now | Not a constant — recompute, never quote. A quoted staleness figure is itself a staleness bug. |
| "576 commits in the dead window" | sibling session | **false precision** — same window returns 583/613/616/629 depending on author-vs-commit date and bounds | Robust form: **all 17 days Jul-07→Jul-23 had commits.** |
| "587 commits in that window" | **this artifact, originally** | same false-precision problem | **My own error, same class.** Replaced with the day-count form above. |
| "fast-forward the stale branch" (as a general fix) | **this artifact, originally** | only **2 of 10** `claude/*` branches are pure ancestors | **My own over-generalisation.** Only `claude/first-test-new-repo-wxedu9` and `claude/good-morning-rjaji6` are FF-able; the other five 07-06-rooted branches each carry one own commit and need a merge. |

**Both sessions independently produced false-precision commit counts about the harness's own history while diagnosing a bug about false beliefs regarding the harness's own history.** That is #43b clause 3f / B65 (context-fluency) firing on the diagnosis of a staleness bug — logged as a specimen, not a coincidence.

## 🔴 The fix is stranded behind the bug

`da04101` (*"session-start: surface branch position before anything else"*) is on `claude/new-session-drppai`, **not on `main`**. A new session cut from `344962f` does not get it. It must not be described as "live" until merged — it currently protects only the one branch that least needs it.

## Fix

1. **Durable (operator-side, the actual fix):** point the session/environment config at `main` rather than `claude/first-test-new-repo-wxedu9`. Same repo-selector class as the pending Routines fix in the standing browser checklist.
2. **Mitigation (agent-side, safe):** fast-forward `claude/first-test-new-repo-wxedu9` → `main`. Verified fast-forward (ancestor check above), so no history rewrite and no Rule #19 exposure; reversible to `344962f`, recorded here. Then a new session branching from it starts current even before (1) lands.
3. **Recovery:** triage + merge the 18 stranded commits — deferred while that session is active (last commit 14 min before this diagnosis); merging under a live writer risks conflicts on files it is actively editing.
4. **Prevention:** `da04101` (session-start surfaces branch position) should reach `main` — a session that is told at turn 1 "you are N commits behind" cannot spend two days reasoning on a dead snapshot.

## Generalisable lesson (candidate — goes to lessons.md at N=2)

**Absence of data in a checkout is not evidence of absence in the world.** Both realised failures share one shape: the session read the *edge of its own clone* as a *fact about the repository* — no commits after 07-06 became "the harness died"; hook state at 07-06 became "these hooks are unnecessary." Same family as B65 (context-fluency) and L39 (*"unreachable ≠ fabricated"*): a retrieval boundary mistaken for a substantive finding. **Mechanical guard: any claim of the form "X stopped / nothing happened / this is inert" must first establish that the observer could have seen X had it occurred** — for repo claims that means printing the branch position before the conclusion, which is precisely what `da04101` implements.
