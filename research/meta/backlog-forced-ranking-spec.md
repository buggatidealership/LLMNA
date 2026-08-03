# Backlog forced-ranking (Option B) — spec + kill criteria

**Operator decision 2026-08-03:** *"let's do B for now as a test."* Chosen over Option A (time-based auto-expiry) and Option C (status quo manual purges).

---

## §1 — Why B and not A, in one paragraph

A time-based expiry would have **killed our single best item this month.** The FX-sensitivity to-do sat 33 days stale — dead under any expiry rule — and it named the exact gap that opened on 2026-08-01, when Japan began intervening and MURATA's guidance turned out to lean on the yen. The macro-tripwires item sat 35 days and named yen-reversal risk *before it arrived*.

**Age measures attention, not value — and attention is precisely the faculty that is failing.** So the mechanism must force a *comparison* ("which 30 of these 75?"), which produces information, rather than consult a *clock* ("is this 30 days old?"), which does not.

**Consequence, stated as a hard design rule: AGE CARRIES ZERO WEIGHT IN THE SCORE.** Not a small weight. Zero. The moment age enters the ranking, B degrades into A wearing a ranking's clothes, and the FX-class casualty returns.

## §2 — The mechanism

| | |
|---|---|
| **Cadence** | Weekly (Mondays, alongside the existing wake) |
| **Cut size** | **30** (configurable). Current open list: 75 → roughly a 2.5:1 cut |
| **Who proposes** | Me — computed, not felt |
| **Who decides** | The operator. He sees the *cut*, not all 75 |
| **What happens to the rest** | **PARKED, not deleted** — moved to a `## Parked` section with the date and the reason |
| **Reversal** | One line. A parked item can be pulled back at any time by anyone |

**Parking is deliberately cheap to undo and deliberately visible.** An item that gets proposed, cut, revived and cut again is telling us something no clock ever would.

## §3 — The score (what actually earns a place)

Four components, none of them age:

| Component | Max | What it measures | Computable? |
|---|---|---|---|
| **CALENDAR** | 40 | A dated external trigger inside the next 30 days, or a `[DUE]`/`[CAL]` tag | yes |
| **POSITION** | 25 | Names a held position — i.e. real money is exposed to it | yes |
| **PRIORITY** | 20 | P0=20 / P1=14 / P2=6 / P3=2 | yes |
| **LIVE RELEVANCE** | 15 | Referenced by a corpus file touched in the last 14 days | yes |

**CALENDAR is weighted highest on purpose.** The one thing a backlog genuinely cannot recover from is missing a dated event — a print, a disclosure window, a regulatory date. Everything else can slip a week without loss.

### The P0 rule — and the flag that matters more than the rule

**P0 items are never parked.** A P0 that fails to make the cut on merit is a contradiction: we said it must happen and then ranked it below thirty other things.

So it is force-included **and flagged**. That flag — *"this P0 would not have made the cut"* — is the most useful output the whole mechanism produces, because it is the harness telling the operator, in writing, that a stated priority is not a real one. Currently there are three P0s and two have been overdue for more than a week.

## §4 — Kill criteria (pre-registered 2026-08-03, before any data)

| Signal | Verdict |
|---|---|
| **Two consecutive weekly cuts skipped** | B is dead. Revert to C and say so. This is B's most likely failure mode — the cut becomes a chore. |
| **Cut list >80% identical week-over-week for 3 weeks** | The ranking is re-sorting, not deciding. Retire or re-weight. |
| **Nothing is ever revived from Parked in 60 days** | Parking is deletion with extra steps. Simplify to deletion and stop pretending. |
| **🔴 A parked item has to be revived because reality forced it** | **The score is wrong in the FX-class direction.** Log it, name which component missed it, re-weight. This is the criterion that matters — it is the direct descendant of the counter-example that killed Option A. |

**Blind-check (Principle #51):**

```
Blind-check: distinguishes "this item earns a slot" from "this item is merely familiar"
· reads on calendar proximity, held-name mention, priority tag, recent corpus reference
· GOES BLIND IF an item's value has no textual footprint — a genuinely novel research
  direction nobody has written about yet scores 0 on LIVE RELEVANCE and 0 on POSITION
  by construction, so the ranking systematically favours work already under way over
  work not yet started. The mechanism cannot see an unstarted good idea, and its
  silence about one is not evidence there isn't one.
```

## §5 — Honest limits

1. **I propose the ranking, and I am the party that let the list rot.** The operator's override is the only real check, which means the mechanism is only as good as his willingness to look at the cut. If he rubber-stamps, B is theatre.
2. **The score can be gamed by me** — adding a held-name mention or a `[DUE]` tag to an item's title would lift it. Not currently a risk, recorded so it is not a surprise later.
3. **A 2.5:1 cut is aggressive for a first test.** Chosen deliberately: a gentle cut would not generate enough signal to evaluate the mechanism. If it proves too aggressive the cut size rises before the mechanism is abandoned.
