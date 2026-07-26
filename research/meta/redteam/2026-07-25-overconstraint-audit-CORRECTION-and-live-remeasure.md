# Overconstraint audit — CORRECTION + live re-measure

**Date:** 2026-07-25
**Status:** supersedes the findings issued earlier this session
**Scope note:** the four fixed rules (no leverage; sizing belongs to the operator;
keys never enter the repo; Rule #19 governance) were out of audit scope and stayed
untouched. Nothing below proposes changing any of them.

---

## 0. Why this document exists

The audit was measured against a working tree **668 commits behind `origin/main`**.
Every conclusion drawn from it inherited that defect. After merging live state
(`671e2da`) and re-measuring, **3 of 4 HIGH-tier fixes I had proposed — and which
the operator authorised — turned out to be wrong.** They were not executed.

This session produced **five** misdiagnoses from the one root cause:

| # | Claim | Reality on live state |
|---|---|---|
| 1 | WAKE-AUDIT-4 = `FAIL-infrastructure` | 576 commits across the 17 "dead" days; harness fine |
| 2 | F1: self-check layer stopped, 0 audits | 23 entries; 9 of 20 checks ran (format my grep missed) |
| 3 | F2: Rule #11 falsifier fired, 38 HOLD : 1 ENTER | 753 lines, 25.0% genuine action; falsifier NOT met |
| 4 | 5 Stop hooks lack recursion guards | all 15 have `stop_hook_active` |
| 5 | `WORKFLOW_LABELS` self-triggers on mandated headers | 1 genuine fire in the entire log |

**The pattern is the finding.** Five independent errors, one cause, all in the
direction of "the system is broken" — a stale tree makes a working harness look
dead, because absence of recent activity is indistinguishable from absence of
records. Fixed durably: `session-start-hook.py` now reports branch position first
(`da04101`).

---

## 0a. The mechanism — verified 2026-07-26 (corrects my first explanation)

I originally told the operator the cause was *"the repo default branch is not
`main`, so default clones land weeks stale."* **That was wrong.** I asserted it
without checking. Recorded here because the wrong mechanism points at a fix that
would not have worked.

**What actually happens: session branches are cut from a pinned old base and never
rebased.** The clone is correct; the root simply never moves.

This session's branch, `claude/new-session-drppai`, was rooted at:

```
344962f83ab9f485491fd15b665c24ae44518bce
2026-07-06 16:06:57 +0000
"Remove accidentally committed __pycache__ from compile check; add .gitignore"
```

`git merge-base --is-ancestor 344962f origin/main` → **true**. It is a genuine
`main` commit — main's 53rd (52 before it, 668 after). Not an orphan, not a fork.
Just old.

**Systemic, not a one-off.** Sibling branches at time of measurement:

| Branch | Root date | Root | Behind `main` |
|---|---|---|---|
| `claude/api-edgar-smoke-test-qad0n9` | 2026-07-06 | `344962f` | 668 |
| `claude/api-edgar-smoke-test-yzvoo9` | 2026-07-06 | `344962f` | 668 |
| `claude/api-key-smoke-test-lbzc7y` | 2026-07-06 | `344962f` | 668 |
| `claude/file-deletion-git-rules-v7fi3q` | 2026-07-06 | `344962f` | 668 |
| `claude/first-test-new-repo-wxedu9` | 2026-07-06 | `344962f` | 668 |
| `claude/harness-optimization-goals-mqkcyx` | 2026-07-06 | `344962f` | 668 |
| `claude/git-enforcement-audit-fui966` | 2026-07-19 | `fbac203` | 191 |
| `claude/good-morning-rjaji6` | 2026-07-20 | `1123ff6` | 139 |
| `claude/harness-accounting-audit-it2e0w` | 2026-07-22 | `10c7b10` | 79 |

**Six branches share the identical 07-06 root.** Note which names appear:
`git-enforcement-audit`, `harness-accounting-audit`, `harness-optimization-goals`
— the branches most likely to *audit the harness* are among the stale ones. Any
audit run from them inherits the same defect this document exists to correct.

**The 17-day number was never evidence.** My branch root is 2026-07-06; this
session's first work landed 2026-07-23. I graded that window a `FAIL-infrastructure`
"17-day dead window." It was the **age of the branch root** — 576 commits landed on
`main` in those days and the tree could not see one of them. The figure I cited as
proof of failure was the branch's own age reflected back.

**Scope limit of the fix.** `branch_position()` makes staleness visible at session
start. It does **not** stop branches being cut from stale bases — that cause sits
upstream of this repo and is still open. Six branches are sitting stale right now.

---

## 1. Disposition of the four authorised fixes

| # | Proposed fix | Disposition |
|---|---|---|
| 1 | Add recursion guards to 5 unguarded Stop hooks | **WITHDRAWN — already present** on all 15 live Stop hooks |
| 2 | Rule #7 case (b) + citation co-occurrence in anti-fabrication | **STANDS** — see §3; already booked as an overdue P0 |
| 3 | Retire `structural-output` + `llm-native-priming` | **WITHDRAWN — would have overridden a live operator decision** |
| 4 | Delete the `WORKFLOW_LABELS` short-circuit | **WITHDRAWN — not worth a HIGH-tier change** |

**On #3 — the one that would have done real damage.** I cited a retirement
pre-authorised for 2026-07-01. The operator superseded it five days later:

> `recurring-audit-log.md:552` — *"USER DECISION 2026-07-06: KEEP BOTH hooks;
> extend 30 days with normalized metric = weekly fires ÷ weekly main-branch
> commits. Extended close: 2026-08-06."*

Retiring them on 07-25 would have destroyed a running experiment 12 days before
its adjudication date. Worse, `G-28`'s numerator reclassification has already
flipped the expected read to **FALLING → keep**. I was one authorised step away
from deleting live enforcement the operator had explicitly chosen to keep, on the
strength of a superseded note.

**On #4.** The short-circuit is real (`nth-order-cascade-hook.py:187`) and does
bypass the causal-verb + anchor requirement — but *not* the exemption check, and
the hook has fired **twice ever, one of those a test probe**. Deleting live
enforcement (Rule #19 HIGH) to remove a cost that measures ~1 fire is a bad trade.
Left in place.

---

## 2. Where the cost actually is — measured, not assumed

Fires per hook across the whole log:

| Hook | Fires | Share |
|---|---|---|
| `structural-output` | 169 | 49% |
| `macro-anchor` | 152 | 44% |
| `anti-fabrication` | 11 | 3% |
| all 12 others combined | 14 | 4% |

**93% of all enforcement cost sits in two hooks.** My audit had ranked neither
first. The 12 hooks I spent most of the audit on account for 4% of fires between
them — that mis-ranking is itself a finding about how the audit was conducted:
I read code and reasoned about what *would* be costly instead of reading the fire
log, which had the answer all along.

### `macro-anchor-hook` — 152 fires, one reason, ~5/day, every day

Single reason string across all 152: `missing macro-anchor / research-tag /
tie-together`. Sustained 3-8/day for the entire logged period.

The trigger is `TICKER + position-marker + >800 chars`, where
`TICKER_PATTERN = r"\b[A-Z]{2,5}(?:\.[A-Z]{1,3})?\b"` — any 2-5 letter uppercase
run. In a repo whose working vocabulary is `HBM`, `TSE`, `JPY`, `P0`, `TC-19`,
`INDEX`, `HOLD`, that matches nearly every message. Position markers include bare
`\bthesis\b` and `\bsizing\b`.

**I did not change it, and I want to be explicit about why.** The hook carries its
own pre-registered repair criterion at line 68 — *"If false-positive rate >30% →
tighten exemption list"* — which would authorise tightening. But:

> **The FP rate is not measurable from the instrument.** `hook-fire-log.md` records
> the fire reason, never the message that caused it. So the criterion that governs
> this hook's repair cannot be evaluated with the data the hook collects.

That is the deeper finding: **a pre-registered kill/repair criterion that its own
instrument cannot feed is not a criterion, it's a decoration.** It has sat
un-adjudicable through two scheduled reviews (06-24, 07-12).

⚠️ **Flagged as uncertain:** I genuinely do not know whether these 152 fires are
false positives. The exemption list is broad and case-insensitive (`hook`, `.py`,
`methodology`, `codification`), so harness-meta chatter should already be exempt —
which argues the fires may be *legitimate* catches on real research output that
omitted a tier tag. Reading the code cannot settle it. Recommend logging a
120-char message excerpt per fire for two weeks, then adjudicating on evidence.
That is a change to a LIVE-enforcement file, so it is yours to approve, not mine
to take.

### `structural-output-hook` — 169 fires, accelerating

120 `structural-markers-missing` / 42 `position-implication-tier-missing`. Rate is
climbing sharply: **27 fires on 07-23, 12 on 07-24.** Flagging because it feeds the
08-06 decision and an accelerating denominator-free count could distort that read.
No action taken — this hook is under the operator's explicit keep-until-08-06
decision.

---

## 3. The one fix that survived re-measurement

`anti-fabrication-hook` fires are few (11) but the needles show genuine garbling:

```
'Q4 2026**. The $6'      <- needle spans a bold-close and a sentence boundary
'2028 chip'              <- not a financial figure at all
'914 wafers'  '4.707%'   '$750B' (x2)
```

Consistent with the `(?:Q[1-4]|FY\d{2,4}).{0,40}[\$€£]\s*\d` pattern capturing
across markdown table cells. Rule #7 case (b) — *"computed from a number you cited
earlier in the same message"* — is still not implemented.

This is a **repair of a defective matcher, not a retirement**, and it is already
booked and overdue in the harness's own backlog (P0 07-24: `G-21` sub-200-char
floor, `G-22` bare-currency, `G-29` per-needle skip-reason logging). `G-29` would
also supply exactly the per-fire diagnostics `macro-anchor` is missing.

**Not executed in this session.** It is the correct next change, but it touches a
LIVE Stop hook, and having just had 3 of 4 authorisations turn out to rest on stale
measurements, spending the fourth on momentum would be the same mistake again.

---

## 4. What I changed

One thing, `da04101`: `session-start-hook.py` now prints branch position before
anything else, tiered (live / routine-drift note / stop-work alarm at ≥25 behind).
Rule #19 **LOW** — creates an advisory check, disables no enforcement. Tiered on
purpose: an alarm firing on every ordinary 1-2 commit drift would decay into
exactly the macro-anchor pathology diagnosed above. Falsifier and 2026-08-25
re-eval in the docstring. Verified across 668/25/24/2/0-behind plus no-origin and
garbage-output cases.

I also applied `# secretscan-ok` to `market_data.py:33` after reading the file and
confirming the flagged line maps an env-var *name* to a scratchpad *filename* and
holds no key value. Used the documented remedy rather than bypassing the scanner.

---

## 5. Honest residual

- **The audit's ranking was wrong before its findings were.** I ranked by reading
  code; the fire log had the true distribution and I reached it last. Any future
  overconstraint audit should open with the fire log.
- **I cannot tell you whether the harness is overconstrained.** 93% of enforcement
  cost sits in two hooks whose false-positive rates are unmeasurable with current
  instrumentation. The honest answer is *not yet determinable*, and the instrument
  gap is the thing to fix first.
- **Direction of error worth noting:** all five misdiagnoses ran toward "the system
  is broken." A stale tree biases specifically that way. If a future audit reports
  widespread harness failure, check branch position before believing it.
- **Unverified:** live holdings carry **three** positions (MURATA, SUMCO, and SKHY
  37 ADS bought 2026-07-10). My audit reasoning assumed two throughout. I have not
  re-checked which conclusions that touched.
- **Still open, unrelated to the audit:** `MURATA/thesis.md:427` reads *"User's
  12.4% position is appropriately sized"* — canonical was 20,6% at the 07-07 mark.
  `origin/main` never fixed it. The right repair points at `portfolio/holdings.md`
  rather than hard-coding any number.
