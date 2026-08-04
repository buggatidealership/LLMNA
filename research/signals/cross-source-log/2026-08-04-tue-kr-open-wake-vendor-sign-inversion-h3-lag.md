# 2026-08-04 (Tue) — KR-OPEN WAKE: the vendor told me KOSPI was −3.26%; it was +1.96%. And the H3 dashboard is reading last week.

**Workflow:** KR-OPEN WAKE (scheduled Routine) — time-sensitive leg only. Full 3-leg scan / prose-deadline sweep / quota check reserved for the operator's "good morning."
**Sync:** clean, not BEHIND. No prior operator wake today. Full leg.
**Reading:** ~09:24 KST (00:24 UTC). **All prices INTRA-SESSION — not a session result until settlement (L42-b).**

---

## TL;DR

🔴 **The EODHD index `previousClose` defect REPRODUCED, and this time it inverted a sign.** The vendor reported **KOSPI −3.26%**. Against the true prior close it is **+1.96%** — a **5.22pp error across zero**. Caught only because verifying `prevClose` against our own T1 record before use is now standing practice.

🟢 **The memory complex is bouncing.** SK Hynix **+3.70%**, Samsung **+1.46%**, SEMCO **+4.49%**, KOSDAQ **+3.75%** (corrected).

🔴 **Five of six H3 instruments are ≥4 days stale — median lag 4 days, Brent 8.** The H3 two-path check, run daily, is structurally blind to anything that happened after 07-31. **No weight moved, because nothing could be seen.**

---

## §1 — 🔴 THE VENDOR DEFECT REPRODUCED, WITH A SIGN INVERSION

| KOSPI | value |
|---|---|
| vendor `previousClose` | **6,595.45** ← this is the **07-31** close, one session stale |
| TRUE prior close (our T1 record for 08-03) | **6,257.45** |
| last (~09:24 KST) | 6,380.32 |
| **vendor `change_p`** | **−3.26%** ← WRONG |
| **TRUE change** | **+1.96%** |
| **error** | **5.22pp — SIGN INVERTED** |

| KOSDAQ | value |
|---|---|
| vendor `previousClose` | 719.76 ← also the 07-31 close |
| TRUE prior close | 737.35 |
| vendor `change_p` / TRUE | **+6.29%** / **+3.75%** — 2.54pp error |

**All four single-stock `previousClose` values were CLEAN** (Samsung 239,500 ✓ · SK Hynix 1,567,000 ✓ · SEMCO 1,181,000 ✓ · Hanmi 202,500 ✓). The defect is **INDEX-ONLY**, exactly as the standing note says: *on INDEX symbols, trust only `close`.*

**It did NOT reproduce on 08-03 and HAS today ⇒ intermittent, not permanent.** Yesterday I recorded the non-reproduction as *"non-reproduction, not a fix"* — that caution was correct and is now vindicated. **An intermittent defect is more dangerous than a permanent one**, because a single clean session invites you to stop checking.

**What this would have cost.** The wake's headline read would have been *"KOSPI down another 3.3%, the decline is continuing"* when the index is in fact **up 2%** and the memory complex is **bouncing**. Every downstream inference — H1/H2/H3 weights, the ETF-divergence test, the flush-repair status — would have been built on an inverted sign.

```
Blind-check on the verification step itself: distinguishes "vendor field is right" from
"vendor field is stale" · reads on prevClose vs our own T1 record for the prior session
· GOES BLIND IF our own prior-session record is missing or wrong — the check is a
  comparison against the corpus, so it inherits the corpus's errors and cannot run at
  all on a name whose prior close we never booked. It is not vendor-independent.
```

## §2 — 🟢 The memory complex is bouncing (corrected figures)

| Name | lev-ETF underlying? | 08-03 close | now (~09:24) | 2-day net |
|---|---|---|---|---|
| Samsung Electronics | **yes** | −8.76% | **+1.46%** | −7.43% |
| SK Hynix | **yes** | −8.79% | **+3.70%** | −5.42% |
| Hanmi Semiconductor | no | −5.59% | +0.49% | −5.13% |
| Samsung Electro-Mechanics | no | +3.42% | **+4.49%** | **+8.06%** |
| **KOSPI** *(corrected)* | — | −5.12% | **+1.96%** | −3.26% |
| **KOSDAQ** *(corrected)* | — | +2.44% | **+3.75%** | **+6.28%** |

**The ETF-divergence test, second reading:** ETF underlyings bounce **+2.58%** mean vs non-ETF Hanmi **+0.49%** — a **+2.09pp spread**, now in the *opposite* direction to yesterday's −2.09pp.

🟡 **Hedged deliberately.** This is *consistent* with mechanical selling having exhausted in the two names it was concentrated in. It is **equally consistent with plain beta** — they fell more, so they bounce more. **A symmetric spread on both legs is exactly what beta produces.** N=1 session, intra-session, and I have now been wrong once on this hypothesis by measuring it the wrong way. **The real test is tomorrow: the FSC single-stock leveraged-ETF rules take effect 2026-08-05.**

**KOSDAQ +6.28% over two sessions vs KOSPI −3.26%** keeps the large-vs-small split wide and pointing the same way: this remains a large-cap-memory event, not a Korean risk event.

## §3 — 🔴 THE H3 DASHBOARD IS READING LAST WEEK

Applying last night's booked rule — *stamp the observation date and the lag, never just the value*:

| Instrument | latest | obs date | **lag** |
|---|---|---|---|
| UST 10Y | 4.75% | 2026-07-31 | **4d** ⚠ |
| UST 2Y | 4.28% | 2026-07-31 | **4d** ⚠ |
| 10y breakeven | 2.27% | 2026-08-03 | 1d |
| HY OAS | 2.84% | 2026-07-30 | **5d** ⚠ |
| JPY/USD | 159.16 | 2026-07-31 | **4d** ⚠ |
| Brent spot | 91.82 | 2026-07-27 | **8d** ⚠ |

**Five of six are ≥4 days stale. Median lag 4 days.**

🔴 **This is a structural finding about the Routine, not about today's data.** The KR-OPEN WAKE runs daily and its H3 two-path check is specified against instruments with a 4–8 day publication lag. **It is therefore incapable, by construction, of detecting an escalation inside the window it exists to monitor.** Yesterday's error — marking H3 "flat" off a stale 10Y — was not carelessness; it was the *designed behaviour* of this instrument set.

**Weights HELD at H1 62 / H2 5 / H3 33.** Not "no change because nothing moved" — **no change because nothing could be seen.** Those are different statements and only the second one is true this morning.

**Booked as a to-do:** the H3 daily check needs at least one same-day instrument (futures, a live quote route) or it should be downgraded from a daily leg to a weekly one and stop pretending to be a monitor.

**Standing gaps, unchanged:** Brent — L43 holds, FRED serves **spot**, the retired gate was a **settle**; cannot adjudicate either way. Non-Brent dashboard (Dubai EFS / JKM / war-risk / Hormuz transits) — **NOT REACHABLE**; the escalation review still cannot run.

## §4 — Owed, and not invented

- **투자자별 close-basis flows for 08-04** — not available intra-session. Yesterday's arrived via the evening sweep (retail **+₩4.65조** buying against foreign+institutional **−₩4.77조**); today's will need the same route.
- **반대매매 07-31 and 08-03 prints** — still owed.
- **MOF cumulative August intervention total** — window runs to 08-07; MOF publishes on a quarterly lag, so **no August aggregate exists yet**. Only the 07-30 start is confirmed.
- **KOSPI200 futures basis / overnight CME-EUREX gap** — the two best pre-open predictors, both still dark. Standing instrument gap, unchanged since it was first recorded.

## §5 — What this wake changes

**Nothing fires. No position action (user-gated).**

| | |
|---|---|
| H1 / H2 / H3 | **62 / 5 / 33 — HELD, because the instruments cannot see past 07-31** |
| Memory complex | **bouncing**; KOSPI +1.96%, SK Hynix +3.70% intra-session |
| ETF-divergence hypothesis | second reading, **opposite sign**, fully confounded with beta — **08-05 is the test** |
| MURATA / SUMCO | unchanged from last night's FX correction; **yen 159.16 as of 07-31 (4d stale)**, MOF window open to 08-07, SUMCO interim 08-06 |
| Vendor trust | **index fields intermittently corrupt — the verification step is load-bearing and must not be dropped after a clean session** |
