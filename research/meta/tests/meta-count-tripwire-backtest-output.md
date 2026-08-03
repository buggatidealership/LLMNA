# Meta-count tripwire — pre-ship backtest OUTPUT (committed receipt)

Run 2026-08-03 at ship time. Committed because the circulated "0 FPs across
108,883 corpus sentences" figure was UNRECEIPTED (dual-review finding #3) —
the spec requires reproduction, not citation. This file is the receipt.

```
==========================================================================
META-COUNT TRIPWIRE — PRE-SHIP BACKTEST (reproduced, not cited)
==========================================================================

GATE 1 — origin trigger shape must be CAUGHT
  fixture : 'The hook fired 6 times today.'
  today's true fire count (computed) : 4
  verdict : block   -> PASS
  NOTE: the ORIGINAL 2026-07-20 sentence was never committed verbatim
        (the adjudication records the claim, not the string). This is the
        canonical SHAPE — third person, precise count, past window, no
        in-turn computation — not a byte-exact replay of the incident.

GATE 2 — false positives on REAL committed meta-statements
  candidate population (harness-noun + past-window in one sentence):
    total harvested        : 285
    dated (replayable)     : 148
    undated (window unrecoverable, EXCLUDED from the rate) : 137
  blocks on dated candidates : 1
  FP rate                    : 1/148  = 0.14 per 20  (gate: <= 1.00 per 20)

==========================================================================
GATE 1 (catches origin shape) : PASS
GATE 2 (<=1 FP per 20)        : PASS
SHIP DECISION                 : CLEARED
==========================================================================
```

## Honest reading of the single remaining block

`1/148` is an **upper bound on the live FP rate, not a measurement of it.** The
one blocked sentence is from `meta/redteam/2026-07-20-self-trust-K3-adjudication.md`
and reads *"11 of 23 commits today are telemetry"* — written **mid-day** on
07-20, when 23 commits existed. Replayed against the full-day count (58) it
looks like a mismatch. The live hook, evaluating at the moment the sentence was
written, would have computed 23 and passed.

**So the backtest cannot distinguish "the hook was wrong" from "the day wasn't
over yet."** Intra-day claims replayed against end-of-day totals are structurally
unfair to the hook, and I am recording that as a limitation of the TEST rather
than quietly banking the favourable read.

## What the v1 → v2 gate actually caught

v1 (bag-of-features: count ANYWHERE + noun ANYWHERE + window ANYWHERE) scored
**2.30 FP per 20 — a 2.3× gate failure — and would have shipped without this
backtest.** Every FP had one root cause: the number was scavenged from elsewhere
in the sentence (`Rule #19 HIGH` → 19, `$29.4B` → 29, `20:17Z EOD fire` → 20,
`§8 B40.x discipline fires today` → 8). v2 binds the number to the counted noun
via explicit claim phrases. Lower recall, correct trade for a tripwire.

The second v2 block was **the tripwire firing on the write-up of the very
incident it was built from** — the dual-review artifact quotes *"the hook fired
three times today"* verbatim. Fixed with an inline-quote exemption: a claim
wholly inside quote marks is someone else's sentence, not this turn's assertion.
