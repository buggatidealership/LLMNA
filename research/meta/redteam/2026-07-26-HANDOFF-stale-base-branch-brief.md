# HANDOFF BRIEF — stale base branches (self-contained; written 2026-07-26 to be forwarded to any other session)

**Read this before acting on anything else in this repo.** It is written to be read by a session that may itself be stale.

---

## STEP 0 — CHECK YOUR OWN POSITION BEFORE YOU READ THE REST

You may be reading this on a 20-day-old tree. Run this first:

```bash
git fetch origin main --quiet
git rev-list --left-right --count origin/main...HEAD   # "<behind> <ahead>"
git log -1 --format='%h %ad %s' --date=iso HEAD
```

If the **behind** number is not 0, **stop and merge `origin/main` before forming any conclusion about the harness.** Everything below explains why that instruction is not bureaucratic.

---

## THE FACT

Session branches are cut from a **pinned old base and never rebased**. Six branches share the identical root:

```
344962f83ab9f485491fd15b665c24ae44518bce
2026-07-06 16:06:57 +0000
"Remove accidentally committed __pycache__ from compile check; add .gitignore"
```

`main` is at 1,496 commits total; **670 of them land after that root** (as of 2026-07-26 09:28 UTC).

**The clone is not broken.** `344962f` is a genuine `origin/main` ancestor (`git merge-base --is-ancestor` exits 0). GitHub `main` matches a current session's HEAD byte-for-byte. Nothing is corrupted — the branch simply never moves forward.

---

## ⚠️ THREE CORRECTIONS TO THE EARLIER WRITE-UP (fix these before relying on it)

The first account of this, produced on `claude/new-session-drppai`, got the mechanism right and three numbers wrong. All three are recomputed here.

**1. `344962f` is NOT "the 53rd commit on main with 52 before it."** It is the **826th**:

```bash
git rev-list --count 344962f     # 826
git rev-list --count origin/main # 1496
```

825 commits of imported Health-Calculators history sit beneath it — the pre-migration corpus. The "53rd" figure understates the repo's depth by roughly 15×. **This matters most to the session that designed the original harness:** the migration preserved the full history; your work is underneath that root, not absent from it.

**2. "668 behind" is not a constant — it was correct at its measurement point and is already wrong.** It was measured against `a36a0d1`; `main` has moved twice since.

```bash
git rev-list --count 344962f..a36a0d1    # 668  (their measurement)
git rev-list --count 344962f..origin/main # 670 (now)
```

**Never quote this number. Recompute it.** A quoted staleness figure is itself a staleness bug.

**3. The "576 commits in the dead window" figure is false precision — do not cite it.** Depending on author-date vs commit-date and bound inclusivity, the same window returns 583 / 613 / 616 / 629. The robust, filter-independent statement is:

> **Every single one of the 17 days from 2026-07-07 to 2026-07-23 had commits on `main`.** (`git log --format=%ad --date=short origin/main | awk '$1>="2026-07-07" && $1<="2026-07-23"' | sort -u | wc -l` → 17)

That is enough to destroy the "dead window" finding without needing an exact count.

---

## WHAT IT ACTUALLY COST — twice, both already realised

**1. The harness was graded dead on evidence that was its own branch age.** A session graded a *"17-day dead window Jul-7 → Jul-23, zero autonomous commits, CronList empty"* as `FAIL-infrastructure`, *"largest gap in harness history."* Its branch root was 07-06 and its first work was 07-23 — the "17 days" was the age of the root, reflected back. Retracted at source (`4d18537`).

**2. A stale audit nearly deleted live enforcement.** The over-constraint audit ran 668 behind. Of four HIGH-tier hook fixes the operator authorised, **three were withdrawn on live re-measure** (`2a11a27`) — including retiring `structural-output` + `llm-native-priming`, which would have overridden the operator's 2026-07-06 keep-both decision and destroyed a running experiment 12 days before its 2026-08-06 adjudication. **Operator authorisation was obtained on a false picture. That is the failure mode to carry forward, not the individual fixes.**

**Direction of error is not random.** Absence of recent records is indistinguishable from absence of activity, so a stale tree produces false *"the system is dead / this is inert / this can be retired"* findings and never false *"everything is fine."* **It biases specifically toward destructive recommendations.** Note which branches carry the 07-06 root: `git-enforcement-audit`, `harness-accounting-audit`, `harness-optimization-goals` — the branches most likely to audit the harness are the ones structurally guaranteed to audit a fossil.

---

## 🔴 THE THING THAT MOST NEEDS SAYING

**The fix for this bug is stranded behind this bug.**

`da04101` — *"session-start: surface branch position before anything else"* — makes staleness visible at turn 1. It lives on `claude/new-session-drppai` and **is not on `main`**. A new session cut from `344962f` therefore does **not** get it. Describing that fix as "live" is wrong until it is merged to `main`; it protects exactly one branch, the one that least needs it.

**Until it is on `main`, Step 0 of this document is the only protection that exists, and it is manual.**

---

## CURRENT BRANCH STATE (computed 2026-07-26)

| Branch | Root | Fast-forwardable? |
|---|---|---|
| `claude/first-test-new-repo-wxedu9` | `344962f` (07-06) | ✅ pure ancestor — safe FF |
| `claude/good-morning-rjaji6` | 07-20 | ✅ pure ancestor — safe FF |
| `claude/api-edgar-smoke-test-qad0n9` | `344962f` (07-06) | ❌ 1 own commit |
| `claude/api-edgar-smoke-test-yzvoo9` | `344962f` (07-06) | ❌ 1 own commit |
| `claude/api-key-smoke-test-lbzc7y` | `344962f` (07-06) | ❌ 1 own commit |
| `claude/file-deletion-git-rules-v7fi3q` | `344962f` (07-06) | ❌ 1 own commit |
| `claude/harness-optimization-goals-mqkcyx` | `344962f` (07-06) | ❌ 1 own commit |
| `claude/git-enforcement-audit-fui966` | 07-19 | ❌ 1 own commit |
| `claude/harness-accounting-audit-it2e0w` | 07-22 | ❌ 21 own commits |
| `claude/new-session-drppai` | merged to live | ❌ 20 own commits |

**Correction to my own earlier advice:** I previously said "fast-forward the stale branch" as though it were general. It is clean for **one** of the six 07-06-rooted branches. The other five each carry a commit of their own, so they need a merge, not a fast-forward — and they may belong to sessions still using them.

---

## STANDING REQUIREMENT (operator directive, 2026-07-26)

> **New sessions must always get the most up-to-date state of the repo.**

Three layers, in order of durability:

1. **Upstream (the real fix, operator-side, outside this repo):** whatever cuts session branches must cut them from current `main`. No in-repo change can fix this — both affected sessions confirmed it is upstream of the repository.
2. **In-repo (merge `da04101` to `main`):** every session then learns its position at turn 1. Makes staleness *visible*; does not prevent it.
3. **Behavioural (applies immediately, needs no infrastructure):** **any claim of the form "X stopped / nothing happened / this is inert / this can be retired" must first establish that the observer could have seen X had it occurred.** For repo claims that means printing branch position before stating the conclusion. This is the generalisation of L39 (*"unreachable ≠ fabricated"*) from the retrieval layer to the version-control layer.

---

## IF YOU ARE THE SESSION THAT DESIGNED THE ORIGINAL HARNESS

The three things most likely to be wrong in your current picture:

1. **Your history is intact.** 825 commits sit beneath `344962f`, including the pre-migration Health-Calculators corpus. If your tree suggests otherwise, that is your branch root, not the repo.
2. **Any "this hook/rule is inert, retire it" conclusion you hold is suspect if reached on a stale tree** — that is the exact error class above, and it points one way: toward deletion. Re-measure against live `main` before recommending any removal. Critical Rule #19 governs deletions of live enforcement; authorisation obtained on stale evidence does not count as authorisation.
3. **The hook counts and fire-log figures you carry may be from the 07-06 snapshot.** Recompute from the live fire log rather than reading them from your tree.

Full diagnosis with the ruled-out hypotheses: `research/meta/redteam/2026-07-26-stale-base-branch-new-session-divergence.md` (on `main`).
