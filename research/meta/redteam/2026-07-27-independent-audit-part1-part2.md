<!-- Independent external audit, commissioned 2026-07-27 (commit 679db78,
     "Fresh-session verification commission: two layers, absence over presence").
     Authored by a fresh session with no prior context on this corpus.
     Method constraint imposed by the commission: repository artifacts are NOT
     evidence for the claims they contain. Every Part-1 number was recomputed
     from primary/independent sources or from git directly.
     The audit itself changed nothing in the repository; this file is the
     first and only write, made afterwards at operator instruction. -->

# LLMNA — independent audit, 2026-07-27

Two parts: (1) adjudication of eleven asserted claims, recomputed from underlying data rather
than from repository artifacts; (2) structural absences.

**Nothing in the repository was changed.** Final working tree: one modified file,
`research/meta/hook-fire-log.md` (+6 lines), written by the repo's own telemetry hooks reacting
to my reads. My audit branch was never pushed. Verified by `git status --porcelain` throughout.

Labels used: **VERIFIED** = read, executed, or computed by me or a delegated agent against a
primary/independent source. **INFERRED** = reasoned, not measured. **UNCERTAIN** = flagged, not
resolved.

---

## PART 0 — Where I was standing

Both defects the commission warned about were present.

**Defect 1 — the repository arrives SHALLOW.**
`git rev-parse --is-shallow-repository` → `true`. Every commit count, root-commit count and
ordinal position in claim 1 is *unobtainable and silently wrong* in this state: a shallow clone
reports a truncated history with a fabricated boundary, and `git rev-list --count` answers
confidently anyway. I ran `git fetch --unshallow` before counting anything. Claim 1 is
checkable — but only after a step the claim does not mention, and a session that skipped it
would have produced wrong numbers with no error.

**Defect 2 — `main` was not where the claim said, and moved twice during the audit.**

| time (UTC) | `origin/main` | what landed |
|---|---|---|
| 2026-07-27 08:41:10 | `4e0e199` | "Fix the retrieval spine: CI had been red on every commit, unread" |
| 2026-07-27 08:52:27 | `679db78` | "Fresh-session verification commission" — the commit that commissioned this audit |
| 2026-07-27 09:09:25 | `55afe58` | "chore: hook-fire-log telemetry" |

At audit start `origin/main` was `679db78`; mid-audit it advanced to `55afe58`. Divergence
`origin/main...HEAD` was `0 0` at start. `4e0e199` is an ancestor of main, not its head — it was
head for **11 minutes 17 seconds**.

Consequence worth noting: two of the three commits above are hook telemetry or commission
scaffolding, not research. The head of `main` moves on its own while a session runs, which means
any count-based metric over `main` (including the "curation ratio") is measuring a moving target
that partly consists of its own instrumentation.

---

## PART 1 — The eleven claims

| # | Claim | Verdict |
|---|---|---|
| 1 | main HEAD `4e0e199`; 1538 commits; 2 roots; `344962f` = 826th | **SPLIT** — 3 of 4 hold; head is stale by 1–3 commits |
| 2 | 2 branches; it2e0w +21 commits / 26 non-telemetry files, unmerged | **CONFIRMED** — one material omission |
| 3 | Link-check passes on `4e0e199`, failed on every preceding commit for weeks | **CONFIRMED, understated** |
| 4 | Brent settled $96.78 on 07-24, above the $95 gate; "$90.47" was WTI-class | **CONFIRMED** — "WTI-class" needs qualifying |
| 5 | KOSPI −5.72%, SKH −8.34%, Samsung −7.59% on 07-24; 07-27 open +0.60% @09:06 KST | **SPLIT — (a)(b)(c) CONFIRMED, (d) REFUTED** |
| 6 | USDKRW FELL 1.09% on 07-24 — won strengthened as foreigners net-sold | **CONFIRMED on the number, framing REFUTED** |
| 7 | 10Y +~16bp over five sessions to 07-23; no FRED 07-24 obs at 07-27 00:30Z | **CONFIRMED** — reading-dependent |
| 8 | IBM +0.43% TRUE, NOW −3.69% FALSE; 11-leg Brier 0.1344 | **CONFIRMED exactly** — baseline is not |
| 9 | IBM's −25.21% day was 07-14, a pre-warning, not the 07-22 reaction | **CONFIRMED in full** |
| 10 | Korean single-stock leveraged-ETF measure effective 07-31, moved from 08-05 | **CONFIRMED** — direction is *restrictive* |
| 11 | Regime weights H1 60 / H2 12 / H3 28, unchanged by the 07-27 reading | **CONFIRMED** |

### Claim 1 — SPLIT

- **"main HEAD is 4e0e199" — FALSE as of audit.** See Part 0. True for 11 minutes.
- **"1538 commits total" — TRUE at `4e0e199`** (`git rev-list --count 4e0e199` = 1538). Now 1540.
- **"Exactly 2 root commits" — CONFIRMED.** `877456b` (2026-07-06, "Initialize repository with
  README") and `b26f835` (2026-03-29, "Add amazon-mask.png"). A genuine two-root graft.
- **"`344962f` is the 826th" — CONFIRMED, and robustly.** Position 826 under *all four* orderings
  tested (default rev-list, `--topo-order`, `--date-order`, `--author-date-order`), and
  `git rev-list --count 344962f` = 826 independently. Convention note: under `--first-parent`
  it is the 8th of 47. The claim holds under every natural reading.
- `344962f` = "Remove accidentally committed `__pycache__` from compile check; add .gitignore",
  2026-07-06 16:06:57Z. It is also the base of PR #1 and the head of the repo's *former* default
  branch — see Part 2, F3.

### Claim 2 — CONFIRMED, with one material omission

VERIFIED: exactly 2 branches on GitHub (`main`, `claude/harness-accounting-audit-it2e0w`) —
confirmed twice, via API and `git ls-remote --heads`. My own audit branch is local-only.

- **+21 commits** — VERIFIED. And `git cherry origin/main <branch>` returns 21 `+` and zero `-`:
  no commit's patch-id is already in main, so it is unmerged *and* not silently cherry-picked.
- **26 non-telemetry files** — VERIFIED. 27 files differ from the merge-base; exactly one
  (`research/meta/hook-fire-log.md`) is hook telemetry. 27 − 1 = 26.

**Omission that matters:** the branch is also **126 commits BEHIND** main. "21 ahead, unmerged"
invites a merge; "21 ahead / 126 behind" is a stale branch whose merge is a conflict exercise.
The claim states only the flattering half. Concretely, this branch holds
`research/meta/computed-counts.py` + `computed-counts.md` — the count-recompute instrument — and
neither exists on main (verified: `git ls-tree origin/main research/meta/ | grep -c computed` = 0).
The tool built to stop the header-count drift has been stranded off main for 21 commits.

### Claim 3 — CONFIRMED, and the claim understates it

VERIFIED against GitHub Actions run history (1,285 runs, all 1,229 `main` runs enumerated).

- Passes on `4e0e199`: run **#1283**, 2026-07-27T08:41:14Z, `success`. Also green on the two
  subsequent commits (#1284, #1285).
- **Red streak on `main`: runs #17 → #1282 = 1,212 runs, 1,211 `failure` + 1 `cancelled`, zero
  successes**, from 2026-07-06T18:15:45Z to 2026-07-27T08:19:03Z = **20 days 14h 25m ≈ 2.94 weeks**.
- Main's only greens were runs #1 and #4–#16, all inside the repo's first **2h 10m 53s**. The
  workflow was broken by the fifth item of the very audit that created it, and was red for
  **99.6% of its lifetime**.
- The failure was stable and specific: `check-internal-links.py` fails on any `research/...`
  reference that resolves to nothing and is not in `.github/link-check-baseline.txt`. The
  baseline was last touched 2026-07-06 and then not for 20 days. Representative failing output
  (run #1281): `NEW BROKEN (6)` listing dangling paths in `day-state.md`,
  `subagent-cost-yield-ledger.md`, `todo.md`, `candidates.md`.

**One precision correction:** read as "every preceding commit *on main*", TRUE. Read as "every
preceding run anywhere", FALSE — there were feature-branch greens, most recently run #1239
(`claude/new-session-drppai`, 2026-07-25T22:21:29Z).

### Claim 4 — CONFIRMED; "WTI-class" needs qualifying

VERIFIED. Brent front-month (ICE Sep-2026) **settled $96.78** on 2026-07-24 — three independent
sources: Rigzone carrying the Bloomberg wire ("Brent for September settlement dropped 3.9% to
close at $96.78"), a Barchart back-solve from the next session's change, and InvestingLive. The
session **low was $95.40**, also above the gate, so the $95 gate held on every basis that day.
No T1 obtained — ICE, CME and EIA pages returned no usable price data.

**On "$90.47 was WTI-class and wrong":** the *wrong* half is solid — $90.47 cannot be a
front-month Brent print on 07-24 (it is $4.93 below Brent's session low). Two qualifications:

1. It is **not the WTI settle either.** WTI Sep-2026 settled **$89.31** (MT Newswires; range
   $87.68–92.83). $90.47 is TradingEconomics' WTI **continuation-series** reference close —
   verified by back-solve: 90.47 × 0.9178 = 83.03, their 07-27 value. So "WTI-class" is right
   about provenance and wrong about it being a settle.
2. **Second-month Brent (Oct-2026) settled $91.68 on 07-24 with a session low of $90.32.** So
   $90.47 sits inside *deferred Brent's* range that same day. "Not a Brent print" is true only
   for the front month.

**A live trap for anyone re-checking this:** Investing.com's "Brent Oil" historical table shows
**91.68** for 07-24 because that page had rolled to the October contract on 07-26. In a
backwardated curve (Sep–Oct ≈ $5.10) a re-check via that page returns a Brent figure ~$5 too
low, which would appear to *confirm* the original error.

### Claim 5 — SPLIT. (a)(b)(c) CONFIRMED; (d) REFUTED

**(a)(b)(c) — CONFIRMED to the exact won**, across multiple independent Korean-language domestic
outlets, each arithmetically self-consistent:

| | prior close | 07-24 close | change |
|---|---|---|---|
| KOSPI | 7,096.89 | 6,690.62 | −406.27 = **−5.72%** |
| SK Hynix (000660) | ₩1,919,000 | ₩1,759,000 | −160,000 = **−8.34%** |
| Samsung Elec (005930) | ₩270,000 | ₩249,500 | −20,500 = **−7.59%** |

Context VERIFIED: foreign net selling **−₩3,282.8bn** (institutions −1,951.3bn, retail
+5,178.3bn); sell-side sidecar triggered ~11:23; the 23rd sidecar since 2026-05-27. Sourcing
caveat: no T1 exchange feed was obtained (Naver blocked, KRX portal not reached) — this is
multi-source T2 corroboration, not exchange-of-record.

**(d) — REFUTED, and the refutation propagates.**

| measure of the 07-27 KOSPI "open" | level | vs Friday | retraces Friday's 406.27 pts |
|---|---|---|---|
| corpus §1.1 "open-tick" (EODHD real-time @00:06Z) | 6,730.91 | **+0.60%** | **9.9%** |
| **actual 09:00 opening auction** (KR press ×4) | 6,806.27 | **+1.73%** | **28.5%** |
| **actual 09:06 KST print** (Hankyung, exact timestamp) | 6,764.53 | +1.10% | 18.2% |
| full-day close (session now over) | 6,755.75 | +0.97% | 16.0% |
| intraday low | 6,557.39 | −1.99% | −32.8% |

The corpus figure matches **neither** the open nor the 09:06 print. Hankyung carries the exact
09:06 timestamp: `코스피는 전 거래일보다 0.74% 오른 6764.53`. The actual open was **+1.73%** and
was the day's high — the index *faded* from the open (+1.73% → +0.74% @09:06 → +0.23% @09:12),
whereas the artifact describes the level as having "improved from +0.60% to +1.22%."

**Why this matters beyond a decimal.** The artifact's stated primary read is *"(a) The bounce is
weak — this is the primary read… today's open retraces only 9.9% / 8.1% / 24.4%."* Measured at
the real open those retracements are **28.5% / 34.4% / 36.6%** — off by **2.87× / 4.23× / 1.50×**.
The "weak bounce" conclusion is an artifact of measuring six minutes into a fade and calling it
the open.

**And the same file already contains the right numbers.** §6.4 gives SK Hynix open ₩1,814,000
(+3.1%) and Samsung ₩257,000 (+3.0%) from the Korean press. §1.1 gives ₩1,772,000 (+0.74%) and
₩254,500 (+2.00%) from the vendor API. The two tables are never reconciled — and §1.1's wrong
numbers are labelled **"T1-machine"** while §6.4's correct numbers are labelled **"T2"**. See
Part 2, F1 and F2.

**Full 07-27 session, now closed** (materially changes the read): KOSPI closed **6,755.75,
+0.97%**, having traded **−1.99%** intraday; it recovered only **16%** of Friday's loss. SK Hynix
+3.24%, Samsung +1.80%, KOSDAQ +2.22%.

### Claim 6 — number CONFIRMED; the framing is REFUTED

**The number is exactly right on one convention.** 24-hour/UTC bar: 1,475.63 → 1,459.57 =
−1.0884% = **−1.09%**. The won strengthened. No sign flip, no per-unit inversion.

**But on the Seoul onshore convention the day was flat.** 15:30 KST closes: 1,466.8 → 1,466.6 =
**−0.01%** (−0.2 won). Roughly half the ~16-won move occurred in the *night session after the
KOSPI had closed*, on US–Iran de-escalation headlines. Reconstructed: 07-23 Seoul close 1,466.8 →
overnight rebound to ~1,475 → 07-24 Seoul close 1,466.6 (flat) → night close 1,458.5.

So "the won strengthened **on the day** foreigners net-sold", read as one intraday phenomenon,
is not supported: **during the selloff hours the won was flat.** The big won-strength session was
Thursday 07-23 (−0.90%), a day of foreign *buying*.

**Two further corrections to any "explained" reading:**
- It was **not** dollar weakness. DXY was **+0.02%** on 07-24 and **+0.7% on the week** — its best
  week since mid-June. The move was KRW-idiosyncratic.
- The actual mechanism resolves the paradox: SK Hynix's **~$26.5bn ADR conversion** into won
  (≈ one full day of total KRW spot turnover), plus **offshore unwinding of short-KRW equity
  hedges** — foreigners exiting *hedged* Korean equity must buy KRW back to close forwards. Foreign
  equity selling therefore generated won *demand*. No BOK intervention found.

### Claim 7 — CONFIRMED, reading-dependent

VERIFIED, three T1 sources agreeing to the basis point (FRED DGS10, Treasury par curve, Fed H.15
— noting these share one lineage, so this is corroboration of transmission, not three
independent measurements):

`07-16 4.57 · 07-17 4.55 · 07-20 4.60 · 07-21 4.63 · 07-22 4.67 · 07-23 4.71 · 07-24 4.69`

- **07-17 → 07-23 = +16bp** (five closes). **07-16 → 07-23 = +14bp** (five session changes).
  The claim lands exactly on the first reading and within 2bp on the stricter one. Worth stating
  that the number is reading-dependent.
- **No FRED 07-24 observation at 2026-07-27 00:30Z — CONFIRMED by interval-bracketing.** FRED's
  page carried `Updated: Jul 24, 2026 3:17 PM CDT` and `Next Release Date: Jul 27, 2026`; FRED
  does not update DGS10 on weekends; 00:30Z Monday falls strictly inside that window. Independently,
  the series still ends `2026-07-23,4.71`. The absence is **normal, not an anomaly** — H.15 carries
  the prior business day, so DGS10 inherits a one-business-day lag; Treasury published 4.69
  same-day on its own site. The literal instant is not re-observable; the bracketing leaves no
  room for a 07-24 observation to have existed and vanished.

**A near-miss worth recording:** the first fetch of Treasury's HTML `TextView` page returned 4.58
for 07-23 — a **column-misalignment error** (it read the 7-Year column), 13bp low, which would
have flipped this finding. The machine-readable CSV endpoint gave 4.71. Wide HTML tables are a
live extraction hazard for exactly this class of check.

### Claim 8 — CONFIRMED exactly; the baseline it is compared against is not

I recomputed from the registered probabilities and the independently verified outcomes:

```
print legs (9)     Brier = 0.101822  → 0.1018   claimed 0.1018   ✓   9/9 directional
reaction legs (2)  Brier = 0.281250  → 0.2812   claimed 0.2812   ✓   1/2
full slate (11)    Brier = 0.134445  → 0.1344   claimed 0.1344   ✓  10/11
```

Both reaction legs VERIFIED against market data: IBM $205.77 → $206.65 = **+0.4277% → +0.43%**
(TRUE at p=0.55); NOW $95.46 → $91.94 = **−3.6874% → −3.69%** (FALSE at p=0.60). Direction check
passes on the one leg where it matters: N-4's p=0.40 is the probability of the event that did
*not* occur, so (0.40−0)² is correct.

**Three caveats, none of which touch the arithmetic:**

1. **The convention was genuinely pre-registered — I checked this against git rather than
   trusting it.** NOW's after-hours reaction was **+3.7%/+4.75%** and it *opened* 07-23 **+4.76%
   at $100.01** before reversing to close $91.94. Graded on the gap or AH, the sign is POSITIVE
   and the leg is TRUE. The close-to-close convention was in the repo at commit `9f00944`,
   2026-07-22 05:41:43Z — **~14 hours before the after-market print**. The fork was pre-resolved.
   Credit: this is clean.
2. **IBM's +0.43% was a low-information event.** The Q2 numbers had been pre-released on 07-14;
   CNBC records the 07-22 figures as "in line with the figures released a week ago." A directional
   call on an empty catalyst is closer to a coin flip than the grade implies.
3. **The "vs coinflip 0.25" comparison inflates the result about fivefold.** The slate's outcome
   base rate is 0.818 and the house's own class base rate (BR-1 robust) is 0.828. Computed:

```
coinflip p=0.50                Brier 0.2500   BSS vs system = +0.4622
class base rate p=0.828        Brier 0.1489   BSS vs system = +0.0962   ← the honest figure
in-sample climatology 0.818    Brier 0.1488
event-clustered (3 events,
  not 11 draws)                system 0.1526  vs climatology 0.1488  → WORSE
P(a do-nothing base-rate forecaster beats 0.25 | true rate 0.828, n=11) = 0.89
```

   The repository's own program document forbids precisely this comparison — *"beating base-rate
   Brier by imitation is a FAIL by construction"*, and amendment OCT-5 requires *"per-class frozen
   nulls (no pooled base)"*. The reporting layer publishes the baseline the program layer
   prohibits. Separately, the ledger-wide edge over climatology is **+0.0023 against the system's
   own stated detection floor of 0.0806 — 35× below it**, and the program says a Brier verdict
   *"is claimed ONLY if realized n clears the floor."*

   To be fair in both directions: a Murphy decomposition over the clean 32-row forecast
   population gives **RESOLUTION = +0.0768** (positive, RES/UNC = 0.504). The forecasts do carry
   real information — this is not base-rate imitation. The defect is in what gets *reported*, not
   in whether there is signal.

### Claim 9 — CONFIRMED in full

The most extraordinary claim in the list, and it survives every test I could construct.

VERIFIED across three independent price sources agreeing to the cent: **2026-07-14 (a Tuesday),
IBM closed $217.07 vs $290.23 — −25.2076% → −25.21%**, on volume **67.44M vs 5.02M** the prior
session (13×). The **largest single-day decline in IBM's recorded history**, exceeding Black
Monday 1987's −22.96%; ~$67bn erased. Heavy T2 coverage (Bespoke, CNBC, Forbes, CNN, Bloomberg).

Every alternative explanation tested and refuted: not cumulative (peak-to-trough 07-07 → 07-22 is
a *different* number, −32.8%); not a split (`adjclose == close` throughout; last split 1999); not
a bad tick (the level persisted at ~$205–219 afterwards); not a different security or scale.

**The reaction to the 07-22 print was +0.43% on 07-23** — a different event eight sessions later.

**The "pre-warning" characterisation is confirmed at T1:** SEC 8-K accession
`0000051143-26-000070`, filed 2026-07-14, acceptance **07:01:52 ET — pre-market**, Items 2.02 /
7.01 / 9.01. Exhibit 99.1 (CEO letter) disclosed preliminary Q2 revenue $17.2B, Infrastructure
−7%, results "below our expectations" and "disappointing," citing a Z shortfall, clients shifting
capex "toward servers, storage, and memory purchases to secure supply-constrained infrastructure,"
and "numerous large deals failed to close." Guidance was *deferred* to the 07-22 call, not revised.

### Claim 10 — CONFIRMED on both legs; the direction is *restrictive*

VERIFIED at T1 from the FSC's own releases.

- **Effective 2026-07-31** — the 기본예탁금 (basic deposit) for single-stock leveraged/inverse
  ETFs **and ETNs** rises **₩10m → ₩30m**, and 대용증권 (substitute securities) no longer count,
  so the full ₩30m must be **cash**. Applies to new *and* additional purchases, and to
  overseas-listed equivalents. FSC verbatim: *"7.31일부터는 현금으로만 3천만원을 넘게 보유한
  경우에만 단일종목 레버리지 상품(국내상장 및 해외상장)을 매수할 수 있게 된다."*
- **The acceleration is evidenced in the FSC's own words.** The 07-16 parent release scheduled
  the deposit hike for *"8.5일경"* and the cash-only rule for *"8.19일경"*; the 07-24 release
  states both are *"조기에 시행"* — implemented earlier than planned.

**Three precision notes:**
1. The original was **"8.5일경" — "around August 5"**, a soft target explicitly pegged to
   brokerages' IT readiness, not a hard statutory date. "Originally announced 2026-08-05" is fair
   but firmer than the source.
2. The acceleration **bundled two separate dates into one**: Aug 5 *and* Aug 19 both became
   Jul 31. "08-05 → 07-31" captures only the headline leg; the cash-only rule jumped 19 days.
3. **Direction: this RESTRICTS.** Both a permit and a restrict event exist in 2026 and they are
   months apart — the enabling 시행령 took effect **2026-04-28** and KRX listed the first 18
   products on **2026-05-27**; the product then went **₩4.4tn → ₩11.9tn in 50 days**, reaching
   ~38% of all ETF trading value, which is what triggered the curb (new listings suspended,
   marketing banned, deposits raised). If any artifact reads 07-31 as a permissive/bullish launch
   event, it is inverted.

**Adjacent-date trap:** the 괴리율 (divergence-rate) tightening 3% → 2% remains **2026-08-19** and
was *not* accelerated. That is the likeliest date to be confused with this one.

### Claim 11 — CONFIRMED

The 07-27 artifact states the weights twice and explicitly declines to move them: *"NO RE-WEIGHT.
H1 60 / H2 12 / H3 28 stand"* (addendum #8, dated 2026-07-24). The escalation trigger
("foreign net-sell persisting ≥3 KR sessions → H3 to ~35") was at session 1 of 3, so no re-weight
was owed.

Scope note stated plainly: unlike claims 4–10, these weights are a **self-declared internal state
variable** tagged "(my model)", not an external observable. The repository is legitimately the
source of record for its own state. I verified *that the state is as claimed*, not that the
weights are correct — the latter is not falsifiable from outside.

One consistency check that does bear on it: 07-27 closed with foreign net selling of roughly
₩2.9–3.1tn (sources differ on scope), which makes Monday session 2 of the ≥3 needed. The trigger
count advances; the threshold is still unmet. Consistent.

---


## PART 2 — What is absent

### The shape of the gap

This system's *detectors* are unusually good. The shallow-clone-invariant branch check, the wake
atomicity rule, the parser's self-reported coverage line, the probe-tagging channel, the
three-way-redundant `hooksPath` re-arming, the twin-print GRADER GUARD, the blind-adversary
commissioning protocol — better than most production engineering. `instrument-commissioning.md`
independently names survivorship bias, self-coded outcomes, resolution-timing selection,
equal-weight-vs-stakes and regime-tailwind confounds, and records the system's own
adjustment-alpha as **negative**. Very little here is naive.

The absences cluster at the two ends the framework does not reach, and they share one shape.

**The framework commissions the middle and neither end.** Its own A2 boundary defines an
instrument as something with a read function whose output feeds a named gate — which captures the
tripwires, parsers, base-rate classes and quotas. It does not capture:

- **the first hop** — the world→corpus boundary, where numbers are fetched and typed in. No market
  data feed has an instrument block, birth hypothesis, falsifying observable, or kill criterion.
  Yet a vendor feed satisfies the A2 test perfectly: if it silently returned wrong output for 30
  days, everything downstream would break unnoticed.
- **the last hop** — the corpus→human boundary, where a finding either reaches someone or does
  not. Every detector here writes to a channel. Nothing measures whether the channel has a reader.

Enforcement is concentrated in the middle, and in one *form*: of 19 hook scripts, **15 are Stop
hooks** inspecting the shape of prose already written. One is PreToolUse, matched to `Bash` only.
One is UserPromptSubmit (an injection, not a check). **There is no hook on `WebFetch`, `WebSearch`,
`Read`, `Write` or `Edit`** — none at the moment data enters, none at the moment a number is
written into a file. Both recent errors entered at exactly those two unguarded boundaries.

---

### F1 — There is no tape of record. This is the root finding.

**Absent:** any canonical, machine-readable store of market observations — a table of
`(instrument_id, exchange, date, session, field, value, currency, basis, source_url, source_tier,
fetch_timestamp)`. VERIFIED: grepping every script in `meta/tools/` and `meta/scripts/` for
`open(...,'w')` / `to_csv` / `json.dump` / `sqlite` / `INSERT` returns **zero persistence calls**.
The fetch layer prints to stdout; a human or model transcribes into prose; every subsequent use
re-types it. `market-state-compute.py` reads its inputs from **stdin**.

The anti-fabrication hook — the only numeric guard — is a **bag-of-numbers existence test**. It
extracts a numeric token, checks a ±350-char window for any citation-or-hedge pattern, then runs
`grep -r -F -l` for the bare string across `research/`. `rc=0 → GROUNDED`. It reads one token and
never looks at the surrounding words. It therefore structurally cannot check instrument, date,
frame, units, session, or arithmetic — and because it asks only "does this string exist
*somewhere*", **a propagated error becomes more grounded with every copy.**

Its detection coverage is also narrower than advertised. VERIFIED by execution: `$145`, `$1.5bn`
and `5 GWh` **do not match** its patterns at all (bare currency without a magnitude word escapes;
only `5 GW` matches). Patches for these were designed and verified by the repo's own 2026-07-21
redteam and **never applied** — the selftest still reports the pre-patch 22 checks.

**What it would catch — and did not.** Six instances of "right magnitude, wrong binding" in roughly
six weeks. Two were known. **Four are new and were uncaught until this audit:**

1. **The KR/JP crash is dated one day wrong in 13 places, including four held-name theses.**
   `companies/HYNIX/thesis.md:399` reads *"Tue Jun 24 Asia open KOSPI −9.99% … SK Hynix −12%"*.
   2026-06-24 was a **Wednesday**; the event was Tue **2026-06-23**. Four independent confirmations,
   including the repo's *own* other artifact
   (`2026-06-24-pm-subagent-hynix-nasdaq-ads-offering-verification.md:146` dates it June 23) and its
   own price pack. Propagated to `HYNIX`, `KIOXIA`, `SUMCO`, `MURATA` theses and 9 more files.
   **Materiality high:** the line is the basis of an "ENTRY OPPORTUNITY" read on a Core position —
   and correcting the date **inverts the causal story**. The corpus tells a "US Monday → Asia
   Tuesday" transmission tale; correctly dated, US and Asia fell in the *same* session and **Asia
   led**. Corpus-wide the weekday checker found **57 mismatches in 314 weekday+date pairs (18%)**.
2. **A percentage that contradicts the two prices printed beside it.** `| MRVL | $307.86 | $279.04
   | −8.82% |` — true value **−9.36%**. The mechanism is diagnostic: `307.86 − 279.04 = $28.82`;
   the *dollar* delta was transcribed into the *percent* field and the leading digit lost. And
   `"8.82"` is a **suffix of `"28.82"`**, walking straight through the substring hole the hook's own
   docstring documents as "structurally unprotected". Cited to a real source — cited-and-real while
   contradicting its own row. Propagated to 5 files; at `MRVL/thesis.md:75` it is load-bearing for a
   falsifier verdict.
3. **A correction that never cascaded — 18 surviving occurrences.** `MRVL/thesis.md:58` records a
   self-correction of a false *"MRVL +8.23%"*. The false figure still stands in 18 places: 11 in its
   origin file (labelled *"T2 VERIFIED / HIGH CONFIDENCE"*), 5 feeding a MU beat-probability pack,
   and `HYNIX/thesis.md:556` where it supports *"NET DOUBLY-BULLISH structural day"* → **HOLD
   10.13% Core**. MRVL closed **−9.36%** that day; no June 2026 session was +8.23%. **The correction
   itself introduced a new date error** — it attributes the figure to "Friday Jun 20", and
   2026-06-20 was a **Saturday** (06-19 was Juneteenth).
4. **The one machine-readable price table is misdated by a day for Korea.** `000660_KS.csv` and
   `005930_KS.csv` each contain **8 Sunday rows and 0 Friday rows**; the 14 non-Korean files have
   clean Mon–Fri distributions. The KR series is shifted `true = CSV + 1 day`, validated against
   four corpus anchors. So the sole structured price store is wrong for the most important region in
   the held book, carries impossible weekend rows, has no source/fetch_timestamp column — and is
   **excluded from hook grounding anyway** by `--exclude-dir=audits`.

**What the Brent miss cost, traced.** The corrupted object was a *pre-registered trigger*: *"Brent
settle <$95 → H3 gate un-breach review."* The false premise propagated through ≥5 files including
three separate lines of `day-state.md` — the clock a fresh session reads — and into the scope of a
live P1 todo item. Had the operator acted on it, the H3 gate would have been un-breached and
macro-risk posture relaxed **into FOMC 07-28/29 and the 07-29 SK Hynix print**, the latter being the
pre-registered adjudicator for a conditional ADD on a Core position. The corrupted trigger sat one
to two sessions ahead of the position action gated on it, and the error ran in the dangerous
direction: it made a live, escalating oil shock look like it was de-escalating.

**The remediation is still incomplete.** VERIFIED: four uncorrected `$90.47` residues survive today
with no strikethrough — `day-state.md:51`, `day-state.md:63` (**two of that file's three H3 lines
still assert the falsified premise**, three lines below a correction block that *was* applied),
`todo.md:130` (a live P1 item whose scope is *defined* by the false premise), and the 07-25 EOD
artifact.

**Honest base rate:** six instances in six weeks. **Every catch was human or human-directed
re-verification. Zero were mechanical.** Detection rate on this class is currently 0%.

---

### F2 — The tier ladder conflates *authority* with *machine-readability*, and is an uncontrolled vocabulary

The sharpest single finding, because the tier system is load-bearing on every claim in the corpus
and it inverted the evidence in the one place I checked.

In the 07-27 artifact, §1.1's **wrong** open figures are labelled **"T1-machine"** (EODHD vendor
API). §6.4's **correct** open figures are labelled **"T2"** (Naver Finance / Korean press relaying
the KRX auction print). The tier system rated the wrong number *above* the right one — because "T1"
is being used to mean *came from an API* rather than *is the authority for this measurement*. For an
opening-auction print the exchange and its domestic tape **are** the authority; a vendor feed is a
convenience. No rule anywhere expresses that ordering.

The vocabulary is also uncontrolled. VERIFIED census: 6,135 uses of `T1`, 5,802 of `T2`, plus at
least 20 ad-hoc suffixed variants coined in flight — `T1-TRADE`, `T1-adjacent`, `T1-vendor`,
`T1-verified`, `T1-confirmed`, `T1-via`, `T1-equivalent`, `T1-filing`, `T1-derived`, `T2-DERIVED`,
`T2-press`, `T2-user`, `T2-CN`, `T0-MARK`, `T3-TRANSIENT`… **`T1-machine` appears in exactly one
file** — invented for that artifact. And `source-reliability.md` is organised as `## T2 —
Primary-tier` / `## T3 — Specialist trade press` / `## T4 — Aggregators`, i.e. **there is no T1
section at all**, and no canonical definition of the ladder anywhere.

**What is absent is not the tier idea — it is a second, orthogonal axis.** Tier answers *how much do
I trust this source*. It cannot answer *what exactly was measured*. Brent settle vs last vs
continuation vs second-month; KOSPI opening auction vs a tick six minutes in; USDKRW 24h-UTC bar vs
Seoul 15:30 onshore close; equity close-to-close vs after-hours; 10Y constant-maturity vs
on-the-run. **Every one of those distinctions bit within the last two weeks, and every pair sits at
the same tier.** Two numbers can both be honestly T1 and not be comparable.

Principle **#39 CANDIDATE** is the nearest existing thing (`T0-MARK` / `T1-TRADE` / `T2-DERIVED` /
`T3-TRANSIENT`) and covers exactly one axis — settle-vs-last-vs-derived-vs-thin. CANDIDATE at N=1
since 2026-06-26, unenforced. Nothing defines Brent-vs-WTI, front-vs-deferred month,
index-vs-futures, or adjusted-vs-unadjusted close.

**Cost of the miss, measured:** the artifact's stated primary read — "the bounce is weak" — rests on
retracements of 9.9% / 8.1% / 24.4% that are really **28.5% / 34.4% / 36.6%**, wrong by 2.87× /
4.23× / 1.50×. A second-source reconciliation on any figure entering an analytical read would have
caught it *in the same file, from data already in that file*.

**Compounding:** the artifact then declared *"✅ NEW CAPABILITY CONFIRMED: EODHD `/api/real-time`
does serve KRX same-day intraday quotes during KR hours"* — on a **single observation, with no
cross-check against an independent tape** — and wrote that conclusion into `meta/data-access.md`,
the canonical fact-layer registry, explicitly overriding the prior note. A capability was promoted
to canon by the very reading that was wrong. **There is no commissioning gate for a data source.**

---

### F3 — No wire carries any automated signal to a human or a session

**Absent:** any path by which CI status, test results, or job health reaches the operator or a
future session. VERIFIED by exhaustive negative: grepping every hook (`.py` and `.sh`) for
`github.?actions | workflow_run | gh run | gh api | /actions/ | check[_-]suite | link-check | CI
status` returns **zero hits**. The session-start briefing surfaces to-dos, pending grades, stale
tiers, cost-yield and branch divergence. It surfaces **none** of: CI status, test pass/fail, hook
error counts, whether scheduled jobs ran, missing API keys, or whether the previous session ended
cleanly.

**What it cost — measured exactly.** The link-check workflow was green for **2h 10m 53s** and red
for **20 days 14h 25m** — **99.6% of its lifetime**, 1,212 consecutive failing runs on `main`. The
fixing commit says it: *"CI had been red on every commit, **unread**."* Never a detection failure.
The detector worked perfectly 1,212 times and printed into a log with no reader.

Meanwhile the thing it guarded did rot: 29 pre-existing broken references sit in the baseline, and
failing runs listed dangling paths in `day-state.md`, `todo.md`, `candidates.md` and
`subagent-cost-yield-ledger.md` — the retrieval spine degrading while the guard shouted into a void.

---

### F4 — 241 test assertions that nothing runs, bound to the wrong file

VERIFIED. Four test files, 1,471 lines, encoding hard-won adversarial knowledge: 21 git-guard
bypass probes, 12 adjacency false-positive probes, 10 tier-gate probes, 200 corpus assertions.
Measured when I ran them: **241/243 pass** (the 198/200 claim reproduces exactly; both failures are
assertions coupled to mutable `todo.md` prose, already self-diagnosed).

**Nothing invokes them.** No `pytest.ini`, `conftest.py`, `Makefile`, `tox.ini`, `noxfile.py`,
`pyproject.toml` or `package.json` exists anywhere. Neither workflow mentions tests; no git hook
does; no Stop hook does. A grep across `.github/`, `.claude/`, hooks, tools and scripts returns
exactly one hit and it is a code comment.

**Worse, the registration assertions point at the wrong file.**
`test_framework_codifications.py:43` binds `HOOKS_SETTINGS` to
`research/meta/hooks/settings.json` — a **stale mirror** holding 18 entries all pointing at
`~/.claude/*`, missing `git-guard` and `session-prime-cascade` — **not** the live
`.claude/settings.json`. So its registration checks would pass even if a hook were deleted from the
live config, and they "confirm" `stop-hook-git-check.sh`, which is not registered there at all. Its
structure checks are substring tests (`"sys.exit(2)" in content`) — presence, not behaviour.

**What it would catch:** a future edit reopening a patched bypass. The tests that guard the guards
are unguarded, and aimed at a decoy. They are documentation wearing the costume of enforcement —
precisely the distinction this repository's founding philosophy rests on ("instructions are choices;
hooks are enforced"). The unlearned corollary: **a check with no runner is also just an
instruction.**

---

### F5 — The one out-of-container notification channel is stale at both ends

The `recurring-audit-reminder` workflow is genuinely well built — it uploads an artifact and
creates/updates real GitHub Issues. Credit: it is the only mechanism here producing durable,
human-addressable output outside the container, and it has never failed.

But VERIFIED: it has run **twice in its entire existence** (2026-07-13, 2026-07-20), and **both runs
executed on the stale default branch** — `head_branch: claude/first-test-new-repo-wxedu9`,
`head_sha: 344962f`, a **2026-07-06** commit. Scheduled workflows run on the default branch, which
was only repointed to `main` on 2026-07-22. So both reminders computed due-date verdicts from a
`todo.md` snapshot 7 and 14 days stale — **and reported `success` both times.**

The delivered output is frozen and unread:

- Issue **#2**, created 2026-07-13: *"Weekly competitive-product surveillance — **DUE SOON (in 2
  day(s))**"*, due 2026-07-15. **Still OPEN. 12 days past due.**
- Issue **#3**, created 2026-07-20: *"PRUNING DISCIPLINE monthly pass — **DUE SOON (in 4 day(s))**"*,
  due 2026-07-24. **Still OPEN. 3 days past due.**

The urgency label is stamped at creation and never re-evaluated, so both will read "DUE SOON"
forever. **Nothing reads Issues back into a session.** The reminder lands, correctly, where the only
actor capable of acting on it never looks — the link-check failure displaced one hop: a *successful*
delivery to an unmonitored inbox.

Today (Monday 2026-07-27) the 09:00Z run had not appeared as of ~09:35Z; historically it fires ~3h
late, so this is **UNCERTAIN, not a confirmed miss.**

**The decay it did not prevent:** VERIFIED from `todo.md` — 80 open items, **54 stamped in the
past**, median **18.5 days** overdue, 15 items **>30 days** overdue, oldest **67 days**. Plus 233
tier entries flagged stale against Principle #37's 30-day rule.

---

### F6 — The fire log is write-only: precision is instrumented, recall is not

**Absent:** any mechanism that could detect a hook which *stopped firing when it should have*.
VERIFIED: 19 hooks append to `hook-fire-log.md`; **no live hook reads it.** A fire log yields
precision and can never yield recall. Only **2 of 19** hooks embed a `--selftest`
(`anti-fabrication`, 22 checks; `session-prime-cascade`, 21 fixtures) — both pass when run by hand,
and **nothing automatically invokes either.** Zero `--selftest` references in any workflow, cron, or
Routine. Of 18 scheduled Routines, none performs a hook health check.

**The paradigm case is in the record and nobody drew the general conclusion.**
`session-prime-cascade-hook.py` v1 shipped 2026-07-12 requiring an `#45 —` ID-dash adjacency no
real house header contains. **Zero fires were possible from the moment it shipped**; found two days
later by manual diagnosis. A hook that *cannot* fire is indistinguishable, in this architecture,
from a hook with *nothing to catch*.

**The documented verification protocol is itself the blind instrument.**
`DURABLE-ACTIVATION.md:38-44` says: count the hook `.py` files (`# expect 19`) and `tail -5` the
fire log for recent fires — *"if hooks are firing per hook-fire-log.md, durability is confirmed."*
Both steps are broken. The count now returns **20** (a shared library was added 07-24), so it reads
as drift when nothing is wrong. And of the last 100 log records, **69 are `session-prime-hook` and
16 are `git-guard`** (85%), so `tail -5` shows those two regardless. **The protocol would report
"durability confirmed" with all 15 Stop hooks dead.**

**Fire counts, probe-tagged test fires excluded:** session-prime 685, git-guard 322, macro-anchor
152, structural-output 149, anti-fabrication 21, session-prime-cascade 5, four hooks 1 each — and
**zero live fires ever** for `segment-trajectory`, `bypass-route`, `bottoms-up`, `antifragility-mn`,
`cascade-enforcement`, `analyst-pt-context`, `borrowed-vs-firstprinciples`. Two of the zeros
(`session-start`, `llm-native-priming`) **contain no logging code at all**, so their zero is
uninformative — they are certainly running. And **11 of the 15 Stop hooks only gained logging on
2026-07-24**, so their observability window is **3 days, not 45**. The fire log **cannot yet
distinguish inert from dead** for most of the layer.

Note also that session-prime's 685 fires are mostly nothing: **668 are no-ops** (637 `resume` + 31
`compact`). It actually injected **16 times in 45 days**.

**A real silent death is already in the log, and only negative-logging found it.** Line 281:
`2026-07-06 16:24:00Z session-prime-hook event= injected=False`. An **empty `source` field** from
the harness made the calibration injection silently never fire on those cold starts — the code
comment calls it *"the worst failure mode"*. **Existence proof that the stdin-schema-drift class is
real, not theoretical** — and the only reason it was visible is that this one hook logs its
negatives. No other hook does.

**Why this compounds now:** fire-log counts are the declared substrate for the **2026-08-06**
structural-output keep/retire decision. **UNCERTAIN:** during one read-only session the log recorded
5 `git-guard BLOCK` lines while only one command was observably blocked — a possible 5:1
logged-to-observed ratio that should be resolved before those counts adjudicate anything.

**The only canary that exists ran once, by hand.** The 2026-07-24 `probe=1` sweep *was* a
synthetic-fixture canary and *did* prove the block+log path for 5 hooks. Nothing schedules it. It is
already written, and `LLMNA_PROBE=1` already keeps it out of metric numerators.

---

### F7 — The enforcement layer is dead-by-exemption, and systematically blind on the turns that modify it

This is v1's failure mode wearing different clothes, and it is the finding I would rank second
overall.

VERIFIED by loading each hook's real trigger and exemption patterns and matching against 230 real
corpus samples:

| hook | trigger hits | surviving exemptions | suppressed |
|---|---|---|---|
| nth-order-cascade | 134 | **4** | 97% |
| bypass-route | 109 | **6** | 94% |
| bottoms-up | 71 | **3** | 96% |
| reasoning-tagging | 86 | **0** | **100%** |
| borrowed-vs-firstprinciples | 18 | **0** | **100%** |
| analyst-pt-context | 8 | **1** | 88% |

The triggers match real text abundantly. **The exemption layer then discards 88–100% of it.**
~600 exemption patterns guard ~15 trigger sets, matched `IGNORECASE | DOTALL` over the **whole
message** — so one occurrence anywhere in a 5,000-word turn voids the hook.

**Proven by execution: a single token disables most of the layer at once.**

| token | hooks exempted (of 11 tested) |
|---|---|
| the bare word **`hook`** | **10 / 11** |
| a `.py` filename | **10 / 11** |
| `settings.json` | **10 / 11** |
| `principle #2` | **10 / 11** |
| the plural `hooks` | 4 / 11 |

The singular/plural asymmetry is a **drafting inconsistency, not a design** — four hooks use
`\bhook(s)?\b`, seven use singular-only `\bhook\b`.

**Measured accidental-exemption rate: 27.6% of day-state analytical blocks and 40.7% of
`research/*.md` files over 800 chars contain at least one universal-escape token.** Ordinary
analytical output lands in an exemption routinely; no adversarial intent required.

**And the structural consequence is the part nobody asked about: the enforcement layer is
systematically blind on exactly the turns that modify the enforcement layer.** Any turn discussing
the harness escapes essentially the entire Stop layer simultaneously. Live demonstration: this week,
`structural-output` and `macro-anchor` have fired **0 times** after 38 and 27 fires the previous
week — because every turn in a hook-focused session is exempt. **Including this audit.** The
sessions that change the safety machinery are the sessions that run without it.

**Is the exemption rate measured anywhere? No.** No hook logs an exemption-skip; only fires are
logged. Precision is instrumented, recall is not — the exact asymmetry that let v1 hide.

---

### F8 — 18 of 19 hooks fail open; 17 of 19 fail open *silently*; one field kills all 15

**Absent:** any stdin-schema validation, version pin, or assertion that a field a hook depends on
actually exists.

All 15 Stop hooks depend on exactly two stdin fields (`stop_hook_active`, `transcript_path`) plus
two transcript-JSONL shapes (`message.role`, and content items shaped `{"type":"text","text":…}`).
VERIFIED by execution in a hermetic sandbox:

- **`transcript_path` renamed or removed → all 15 Stop hooks exit 0 silently, simultaneously.** No
  fallback, no log, no stderr. **A single field rename upstream ends all Stop enforcement with no
  trace.** Confirmed: 0 of 18 hooks log when the field is missing or the transcript unreadable.
- **Content item type renamed** (`"text"` → `"output_text"`) → empty parts → exit 0 silently across
  all 15.
- Only `stop_hook_active` breaking would be *noticed*, because hooks would re-fire in a loop.

**The Rule #7 enforcer can die permanently and look like a clean session.**
`anti-fabrication-hook.py:564-573` wraps `main()` in `except Exception: sys.exit(0)` with the
comment *"Fail-open: an unexpected bug in this hook must never block work."* VERIFIED: exit **0**,
**0 bytes of stderr**, **no log line**. Only 3 of 19 hooks wrap `main()` at all; only 2 of 19 log
their exception path. No `timeout` key is set anywhere, so a killed hook is a silent, unlogged,
non-blocking error.

There is also a **stale-text enforcement** bug: `get_last_assistant_message` returns `""` only after
exhausting its loop, so when the final assistant message is tool-use-only the hooks silently walk
**backwards** and enforce against an older, already-adjudicated message.

**One documented-as-live hook is not registered where the docs say.** `research/CLAUDE.md`
describes `stop-hook-git-check.sh` as a live Stop hook; it appears **only** in the stale mirror
`research/meta/hooks/settings.json`, not in `.claude/settings.json`. **UNCERTAIN and worth
resolving:** separate evidence indicates a platform-managed copy at `~/.claude/` *is* wired via
`launcher-settings.json`, in which case enforcement is live but **outside version control and
outside the test suite** — the one enforcement mechanism the repo can neither test nor audit. Either
way the documentation and the project config disagree.

---

### F9 — All consistency enforcement is between files. None is within a file.

**Absent:** any check that an artifact is consistent with *itself*. VERIFIED: the
cascade-enforcement hook's docstring scopes it to inter-file back-references (artifact →
`companies/{TICKER}/thesis.md`), and it has **zero live fires ever**. Grepping hooks and tests for
`intra-file | within-document | self-consistency | internal consistency` returns **nothing**.

**What it would catch:** the KOSPI error, immediately, from data already in the file. The 07-27
artifact contains §1.1 (SKH open ₩1,772,000 / +0.74%) and §6.4 (SKH **open ₩1,814,000 / +3.1%**) —
two values for the same instrument, field and session, ~100 lines apart, never reconciled. All the
cascade machinery points outward; the error was inward.

The general form is cheap: for any row carrying `(prior, current, pct)`, assert
`|pct − (current/prior − 1)| ≤ 0.05pp`. That single check also fires on the MRVL −8.82% error — and
the repository already has the rule as prose, BOUNDARY RULE #43b: *"if a claim could in principle be
settled by arithmetic … it MUST be computed."* A principle with no enforcer.

---

### F10 — Corrections are events, not transactions

**Absent:** any instrument that, when a numeric claim is struck, requires every surviving instance
to be corrected or explicitly exempted **in the same commit**.

VERIFIED: the Brent correction left **4 uncorrected residues**, two in the file a fresh session
reads at wake, one the scope of a live P1 item. The MRVL `+8.23%` correction left **18 uncorrected
occurrences**, several load-bearing for a HOLD on a 10.13% Core position — and that correction
introduced a fresh date error of its own.

The system has rich machinery (Critical Rule #10, `tier-cascade-log.md`, a hook) for propagating
*new* information **forward**. It has nothing for propagating a *retraction* **backward**. Given
that grounding is string-existence, an uncorrected residue is not merely stale — it actively
**re-grounds the retracted number** for any future claim that repeats it.

---

### F11 — A growing write-only region of the corpus that no retrieval path reaches

**Absent:** any inbound-reachability check. The link-check workflow validates that references
*resolve outward*. Nothing validates that a file is *referenced inward*.

VERIFIED, computed over the whole corpus: **154 of 872 files (17.7%) are never referenced by any
other file.** Excluding legitimate scaffolding (`__pycache__`, benchmark fixtures, hook scripts
reached via settings, git hooks): **102 substantive markdown files, 595 KB, median 4.2 KB** — real
artifacts, not stubs. `INDEX.md`, the declared "single-file retrieval entry point", directly reaches
**43 of 872 files (4.9%)**.

The stated architecture is *"Write into the hierarchy…; read through the references (INDEX, tags,
cross-links)"*, and the retrieval-first protocol directs sessions to prefer INDEX over grep. For 12%
of the corpus that read path does not exist.

**What this already costs:**

- `predictions/2026-07-25-SUMCO-Q2CY2026-component-level-pre-registration.md` — a **19 KB live
  pre-registration**, orphaned, and VERIFIED **absent from `grading-log.md`**. Its own header says
  *"A prediction file with the wrong resolution date is a grading hazard; that is the primary reason
  this v2 exists"* — and it is now invisible to the only mechanism that surfaces pending grades. It
  resolves 2026-08-06.
- `companies/IBM/facts.md` — the file holding the corrected `−25.21%` tape. Orphaned.
- `companies/SMCI/` — **all four files** orphaned. An entire company folder unreachable.

Research paid for in subagent tokens becomes invisible to every future session, silently, while the
corpus grows ~10 artifacts a day.

---

### F12 — The grading denominator has holes no mechanism can see

The bookkeeping is clean where measurable — VERIFIED: **zero** deletions from
`research/predictions/` in 1,539 commits; **zero** post-registration probability edits; the
twin-print registration body byte-identical across all four revisions. Credit: genuine integrity.

**But four registration files are orphans, never referenced in `grading-log.md`** — the only file the
pending-grade parser reads. The consequential one:
`2026-07-17-regime-read-preregistration-five-calls.md` — **five calls with explicit
probabilities**, whose own line 22 commits that *"each call grades at its resolution date into
calibration-ledger.csv."* VERIFIED: **zero ledger rows reference that slate.** Calls #2 (P~80) and
#3 (P~70) resolved on the **same 2026-07-22 events** that resolved the twin-print slate. The
twin-print slate was graded within six hours and its 0.1018 became the headline. The registration
pointing at the same two events **was never scored at all.**

**INFERRED, flagged:** call #2 at P~80 asserted *"crowding, not displacement, is the live
mechanism"*; the twin-print grade concluded the opposite (*"L33 SPLIT = hardware-displacement not
software-squeeze"*). It plausibly resolved FALSE or MIXED at P~80 — the single largest Brier
contribution in the corpus (0.64 if FALSE). I found no evidence of concealment and the append-only
history is fully consistent with neglect. But the asymmetry runs one way: **the flattering
registration of that event pair was graded same-day; the unflattering one was never graded.**

The forcing mechanism exists and is miscalibrated in both directions. VERIFIED by running the
parser: coverage is exactly **"9 of 18"**, honestly self-reported. Of the 3 rows surfaced as PENDING
GRADES, **only 1 is real** — the skip test matches the literal `"✅ GRADED"`, and two fully-graded
rows are tagged `"✅ FULLY GRADED"` and `"T+30 GRADED-FINAL"`, so an inserted word defeats the match.
**Signal-to-noise 1:3, structurally and recurringly** — which trains the operator to discount the
alert, and is how the one genuine overdue item (Samsung, 4 days) survives in plain sight. Separately,
one prediction carries the resolution date `late-Jul→Aug-13 (date TBC)`; the parser requires an ISO
date, so it is **permanently invisible — it will not surface when Aug-13 passes either.**

---

### F13 — The reported baseline is one the system's own program forbids, at an n its own floor rejects

See claim 8. In brief: the published comparator "coinflip 0.25" inflates the skill score roughly
fivefold against the honest comparator (class base rate 0.828 → BSS +0.096, not +0.462). On an
event-clustered basis — 3 events, not 11 independent draws — the system scores **0.1526 vs
climatology's 0.1488, i.e. worse**. The program document itself states *"beating base-rate Brier by
imitation is a FAIL by construction"* and amendment OCT-5 requires *"per-class frozen nulls (no
pooled base)"*. And the ledger-wide edge over climatology is **+0.0023 against the system's own
detection floor of 0.0806 — 35× below it**, where the program says a verdict *"is claimed ONLY if
realized n clears the floor."*

**What is absent** is not the analysis — the program layer specifies all of it. What is absent is any
check that the **reporting layer obeys the program layer**. Headline numbers and their comparators
are written by hand into artifacts, and nothing reconciles them against the spec that governs them.

In fairness: a Murphy decomposition over the clean 32-row population gives **RESOLUTION = +0.0768**
(positive, RES/UNC = 0.504) — the forecasts carry real information. The system is also
**systematically under-confident by 18.2pp** (mean stated P 0.631 vs realized 0.813; the 0.50–0.70
buckets resolved **12/12 TRUE**), independently confirming the program's own diagnosis that the
defect is timid, undersized deviation rather than bad deviation.

---

### F14 — The ledger only grows, and the mandatory read set now exceeds the context window

VERIFIED by git replay across 1,539 commits: **143 additions : 0 retirements.** `RETIRED` /
`DEPRECATED` / `REVOKED` / `DEMOTED` / `ARCHIVED` score **exactly zero** in all five canonical
files. Even retirement *decisions* are append-only: **PC-10** carries the written verdict *"VERDICT:
RETIRE from pattern register"*, dated 2026-06-24, and 33 days later still occupies its lines and
still loads. `research/CLAUDE.md:27` states the rule — *"Codifications that go INERT for 30 days get
retired or promoted to hooks"* — and **no hook implements it.**

**36 of 55 CANDIDATEs (65%) are past their own stated gate**, median 16 days overdue, max 33, ~500
cumulative codification-days. Three sit above their own promotion thresholds and were not promoted
at the audit that named them.

**Quantitative consequence:** the mandatory boot-order read set totals roughly **7,448 lines / 975k
chars / ~244k tokens ≈ 122% of a 200k context window.** *(Estimated at chars÷4, not a tokenizer —
approximate, but the direction is not in doubt.)* **The boot order cannot be complied with**, so
*which* codifications actually condition a given session is non-deterministic. The one capped
channel, `session-prime.md`, sits at **29,683 of 30,000 chars — 317 chars of headroom** — has grown
3.08× in 40 days, and breached the cap twice on 2026-07-17 with the truncation branch firing and
silently dropping the ledger tail. Meanwhile the pruning task is defined against the *line* cap
(245/500 = 49%, apparent slack), not the *char* cap that overflowed.

The repository diagnoses this itself, precisely — `todo.md:384`: *"the harness is engineered to
ACCRETE… **There is an accrete cadence but no matching PRUNE cadence**"*; `todo.md:357`: *"ossified
text that's never actually applied = **the most likely OS-degradation pathway**"*;
`instrument-commissioning.md:17`: *"**birth without a death-condition is how registries bloat.**"*
The diagnosis is complete. The instrument is absent.

**A self-referential instance:** `session-start-hook.py:480` hardcodes a banner printed every session
advertising *"re-eval 2026-07-15"* — 12 days past. The harness spends context every session
announcing an expired deadline.

---

### F15 — Nothing records what happened to the money

**Absent:** any record of realized fills, and therefore any possibility of grading a *decision*
rather than a *forecast*.

VERIFIED from `portfolio/holdings.md`: **four full exits with unknown fills** — SKH (16 GDR), SNDK
(9 sh), NBIS (30 sh), KIOXIA (~€10k, *"closure date/proceeds UNCONFIRMED"*). The file records this
as *"SKH/SNDK/NBIS realized fills remain UNKNOWN — the audit gap from 2026-07-05 stands"* and
classifies it *"for the trade log; not blocking."*

**That classification is the finding.** The gap is filed as **bookkeeping**; nobody asked what it
means **epistemically**. The learning loop is Predict → Grade → Lesson → Bias → Principle → Hook,
and every stage operates on *forecast accuracy*. Without fills there is no observable for *decision
quality* — a different quantity. A well-calibrated forecast that arrives after the fill, or that
nobody trades on, has a good Brier score and zero consequence.

This is explicitly **not** an argument about who decides sizing — that is the operator's, fixed, and
not what I am auditing. It is that the system does not **collect the evidence** that would let it
learn from decisions at all.

Related and VERIFIED: `portfolio/changes.md` carries **4 PLANNED + 1 PENDING against 1 EXECUTED**,
with intents from 2026-05-25 (HDS €10,000; STM €5,000) and 2026-06-02 (SELL TE; a full rotation)
still unresolved **63 and 55 days later**. Nothing forces a PLANNED action to become EXECUTED or
CANCELLED — the same open-ended-state failure as an ungraded prediction, on the money side. The
corpus does creditably link each change to the artifact that drove it (`Linked: …`), so the forward
half of decision provenance exists. The backward half does not.

---

### F16 — The one instrument aimed at decision quality is half-built and its verdicts are noise

`portfolio/override-counterfactual-ledger.csv` is exactly the right instrument: five rows recording
where the operator overrode the harness, with an ex-post verdict. Real credit for existing. It is
also unfed and unsound:

- **`T7`, `T30`, `T90` are empty on every row.** The fields designed to measure *when* an override
  was right were never populated.
- **The comparison column is literally named `price_now_20260717`** — a hardcoded date. Every
  verdict is frozen at one arbitrary timestamp, now 10 days stale.
- **I re-priced all five rows at the 07-24 close. No verdict label flips — and that is the least
  important thing.** The skipped interval contains **two sign reversals the ledger never saw**:
  SKHY closed **above** its 173.45 entry on 07-14 (193.92) and 07-15 (176.46) — the verdict would
  have read VINDICATED, not UNDERWATER — and NBIS closed above its event price on 07-21, 22 and 23.
  Weekly magnitudes move 3–6 points; intra-window swings reach 13. **A single-timestamp verdict on a
  two-to-four-week-old trade in this tape is an artifact of the sampling date, not a conclusion** —
  and with SK Hynix reporting 07-28 and SanDisk 08-05 at a ~25% implied move, every row will be
  re-shocked within nine days.
- **Three data-integrity defects.** SK Hynix's `−15.8%` is computed off a *different base price*
  than the one in its own `price_at_event` column — reproduced exactly:
  `(1,842,000 − 2,187,000)/2,187,000 = −15.775%`, using the 07-02 close while recording the 07-01
  close. True figure **−28.0%**; direction survives by luck, not method. The NBIS event is dated
  **2026-07-03, a day US markets were closed** (Independence Day observed); 213.02 is the 07-06
  close. And SK Hynix's "07-17" price is a **07-16** print — KRX had no 07-17 session.
- **Most consequentially, rows 2 and 5 are not independent.** They are one SK Hynix round trip: the
  operator exited the ordinary on 07-01 at ₩2,560,000, then on 07-10 re-entered the same economic
  exposure via the ADR at 173.45 × 10 × 1,505.91 ≈ **₩2,612,000 share-equivalent — 2.0% ABOVE the
  exit price — while the underlying was 14.8% cheaper.** The gate the override bypassed had blocked
  exactly this: the ADR premium at fill was **+19.8%**, not marginally over the 5% gate, and has
  since widened to **+29.5%** (so the ADR's apparently mild −10.9% versus the ordinary's −19.3% is
  *entirely premium expansion*, masking a deteriorating basis). The ledger scores this as one win
  and one loss. It is a single self-cancelling error, which makes the aggregate override scorecard
  **biased upward by construction.**

**Absent:** a rule that an override's unit of analysis is the *round trip in an exposure*, not the
individual ticket — plus the horizon columns the schema already declares.

---

### F17 — There is no market calendar or session clock

**Absent, VERIFIED by search:** no `market_calendar`, `trading_calendar`, `exchange_calendar`,
`is_trading_day`, `session_close` or `market_hours` anywhere in the repository.

Almost every dating and session error in this audit traces to that one absence: 57 weekday/date
mismatches (18% of pairs); the Korean price series shifted a day with Sunday rows; an event dated to
a US market holiday; a "Friday EOD" artifact filed under a Saturday; a correction attributing a
figure to a Saturday; settle-vs-after-hours-vs-close ambiguity on 79% of price legs; a 09:06 tick
labelled an opening auction; FRED's publication lag mistaken for missing data.

A single authority answering *is this a session for this exchange, and what are its open/close
timestamps* would mechanically kill an entire error family. **The cheapest high-yield instrument on
this list.**

Associated exposure, VERIFIED: **only 6 of 29 price/reaction legs (20.7%) pre-state their
measurement convention, and 0 of 29 name a data source of record.** The twin-print slate survived the
ServiceNow +4.75%/−3.69% fork because its author happened to write "close" twice, 14 hours before the
print. That was care on one file, not a mechanism — the other 23 legs are exposed, and on any of
them both signs are arguable at grade time.

---

### F18 — Out-of-git state fails silently, including the entire fact layer

VERIFIED: **all 8 API keys** (`FINNHUB`, `EODHD`, `FRED`, `DART`, `EDINET`, `FMP`, `ALPHAVANTAGE`,
`ECOS`) are **absent** in this container. `setup.sh` correctly detected this and wrote it to
`/tmp/llmna-boot-status.txt` — which **nothing reads**, is now 4 days stale, and asserts `BEHIND
origin/main: 0 commits` at a commit four days old. A file whose purpose is to prevent a stale-clone
misdiagnosis would now cause one.

So the entire fact layer registered in `data-access.md` is credential-less and no channel carries
that fact to a session. A session could reasonably conclude a data source is *broken* when it is
merely *unauthenticated* — or quietly fall back to press and pre-training.

**A new, undocumented hole:** `origin/HEAD` does not resolve in this repository.
`stop-hook-git-check.sh` falls back to `upstream="origin/HEAD"` for branches with no remote
counterpart; the `rev-list` then fails, `|| unpushed=0` swallows it, and the check passes. Proven
end-to-end on a never-pushed branch carrying one real commit: **exit 0 with unpushed work present.**
The same failure silently empties the signature check. (Network failure during push *is* correctly
caught.) Separately confirmed: the blanket `stop_hook_active` guard means an identical dirty tree
returns exit 2 or exit 0 depending only on whether some *other* Stop hook blocked first — **one
block by any of 15 Stop hooks disarms git enforcement for the next Stop.** That one is already known
and P0-tracked.

---

### Incidental: the git-guard's false-positive rate on read-only work is ~100%

Not a structural absence, and its governing policy is out of scope — but measured, so recorded. The
guard blocked **6 of 6** commands in one read-only audit session, and blocked two of mine: once
reading `2>/dev/null` as *"truncating redirect (>) onto an enforcement/protected file"*, and once
matching a bypass flag that appeared **inside the prose of this report** as I wrote it to a
scratchpad path outside the repo. Root cause for the config-key class is identifiable: the check
scans the raw command string rather than the echo/heredoc-stripped view that the adjacent check
correctly uses, and does not gate on being inside a git repo. The redirect FP class is documented as
fixed; it is not. Note also two spelling variants of the same block reason in the log — reason-string
drift will silently split any count keyed on those strings.

---

### What I checked and found genuinely sound

Reporting these because an accurate map matters more than a long charge sheet.

- **Deletion and retro-edit integrity: clean.** Zero deletions from `research/predictions/` in 1,539
  commits; zero probabilities edited at or after a resolution date. Every removed line traced.
- **The ServiceNow convention was genuinely pre-registered** — in the repo 14 hours before the
  after-market print. Verified against git, not taken on trust.
- **The twin-print GRADER GUARD** pre-emptively blocked the exact stale-recycle defect that would
  have faked leg G-1. Written before the print. Genuinely good integrity engineering.
- **`HYNIX/facts.md` on the ADR raise is exemplary** — reconciles $26,507,100,000 against
  177,900,000 ADSs at $149.00 and 17,790,000 common shares at a 1:10 ratio, cites the 6-K, and
  records that house pre-estimates were +5.6%/+9.8% high. **One of my own subagents got this wrong**,
  conflating the common-share count with the ADS count to derive $2.65bn. The corpus was right and
  my agent was not. Recorded because it is the same error class this audit is about, and the corpus
  is the party that got it right.
- **Repo-root resolution is correct and dynamic in all 19 hooks** — no stale-path class remains.
- **`session-prime-cascade-hook` v2 genuinely fixed v1** — 5 live fires, 21/21 fixtures pass.
- **`anti-fabrication`'s three-valued grounding** (GROUNDED / FABRICATED / INCONCLUSIVE, a 15s shared
  budget, and *logged* INCONCLUSIVE rather than a false fire) is the most careful code in the layer.
- **`hook_fire_log.py`** is a clean never-raises helper with newline-injection defence,
  probe-tagging, and metric-safe rotation. **`install.sh` correctly ABORTs** when project settings
  are active.
- **`git hooksPath` is the best-defended thing here** — redundantly re-armed by three independent
  mechanisms.
- **`session-start-hook.py`'s `branch_position()` is exemplary** and is the intellectual template
  for what the rest of the layer needs: it reasons about shallow-clone invariants, corrects two of
  its own earlier false claims in the docstring, pre-registers a falsifier, runs first, and states a
  recall-aware test — *"prove it by asserting the LIVE line is present, not merely that no alarm
  ran."*
- **B17 exists.** I hypothesised that a system with 65 biases about the AI's failure modes would have
  none about the operator's inputs. Wrong: B17 "User-deference bias" is exactly that, carrying the
  operator's own instruction to be doubted. Unenforced by any hook, but not unimagined.
- **The wake atomicity rule** — *"a wake COUNTS only if its terminal commit+push landed"* — is sound:
  absence-of-commit as the durable record, remote git as ground truth.
- **The commissioning framework** anticipates most of the attacks in this audit. **The gap is not
  that this system lacks the right ideas. It is that the ideas live in the spec layer and the
  reporting and enforcement layers do not obey them** — and, repeatedly, that patches were designed,
  verified, and never applied.

---

### If I had to rank

By (probability of silent failure) × (cost when it bites):

1. **F1** — no tape of record. Six instances in six weeks, mechanical detection rate 0%, one
   corrupting a pre-registered trigger two sessions ahead of a position gate.
2. **F7 / F8** — the enforcement layer is dead-by-exemption (88–100% suppression; one bare word
   voids 10 of 11 hooks) and one unvalidated stdin field silently kills all 15 Stop hooks. Both are
   invisible to every instrument the system has.
3. **F2** — tier conflates authority with machine-readability; no measurement-convention axis exists.
4. **F10** — corrections don't propagate, and under string-existence grounding an uncorrected residue
   actively re-grounds the retracted number.
5. **F3 / F4 / F5 / F6** — the delivery and recall family. Detectors that work perfectly into
   channels with no reader; a verification protocol that would certify a dead layer as healthy.
6. **F17** — no market calendar. Cheapest fix on the list; kills a whole error family.
7. **F12 / F13** — denominator holes, and a reported baseline the program layer forbids.
8. **F11** — 12% of the corpus unreachable, including a live pre-registration.
9. **F15 / F16** — no realized-outcome evidence; the one decision-quality instrument unfed and its
   verdicts sampling artifacts.
10. **F14 / F18** — monotonic ledger exceeding the context window; out-of-git state failing silently.

Two changes would cover a surprising amount of this, and both are assembly rather than invention.
**One:** a briefing section that reads what the system already produces and already discards — last
CI conclusion, test exit code, open `recurring-audit` issues, fire-log error counts, boot-status
freshness, API-key presence. **Two:** schedule the `probe=1` canary sweep that already exists and
already ran once by hand — it converts the enforcement layer from precision-only to
precision-plus-recall, and would have caught the v1 dead hook in a day instead of two.


---

### F19 — Nothing validates a citation, and the hook's incentive gradient rewards inventing one

**This is the single most consequential defect found.** I verified it myself rather than relying on an agent.

`research/meta/hooks/anti-fabrication-hook.py` line 76, inside `CITATION_PATTERNS` — the list of things that count as satisfying the anti-fabrication check:

```python
CITATION_PATTERNS = [
    r"https?://\S+",                       # URLs
```

**Any URL-shaped string satisfies the hook. There is zero validation — no fetch, no format check, nothing.**
So a fabricated URL is not merely undetected; it is a *perfect bypass*. It converts a message the hook
would block into one it passes. The gradient actively rewards inventing a citation over hedging an
uncited number — the opposite of the intent of Critical Rule #7, which this hook exists to enforce.

**VERIFIED, and it has already happened at scale.** Across the ten `2026-06-25-pm-subagent-*`
artifacts, 317 URLs were checked: 247 live, **32 hard 404s**, 30 access-blocked. The 404s are not
randomly distributed — which is what rules out ordinary link rot:

| artifact | URLs | 404 | dead % |
|---|---|---|---|
| subagent-1 — HBM 3-condition cycle-escape | 16 | **11** | **69%** |
| subagent-3 — CXMT capacity / DDR6 | 9 | **8** | **89%** |
| subagent-4 — NAND 4-vector structural growth | 14 | **9** | **64%** |
| subagent-10 — TrendForce 800V HVDC | 72 | 0 | 0% |
| subagent-7 / -8 / -9 | 32 / 38 / 38 | 0 | 0% |

Same date, same corpus age, same repo. Seven of ten have 0–5% dead links; three have 64–89%. Age
cannot explain that.

**The decisive item, which I confirmed exists in the corpus:**
`https://arxiv.org/abs/2507.HCAttention`, at
`signals/cross-source-log/2026-06-25-pm-subagent-1-...:173`. arXiv identifiers are `YYMM.NNNNN`.
**That string is not a syntactically valid arXiv ID — it could never have resolved.** It was invented.

The rest share one signature: a plausible path synthesized from the claim itself. All confirmed
present in the corpus by my own grep:

```
research/.../subagent-1:176   https://www.morganstanley.com/research/hbm-pricing-power-2026
research/.../subagent-3:172   https://www.smee.com.cn/euv-roadmap-2029
research/.../subagent-3:166   https://www.trendforce.com/datatrack/cxmt-2026
research/.../subagent-4:206   https://www.citi.com/research/vera-rubin-cmx-tb-estimate
                              https://www.goldmansachs.com/insights/articles/micron-q3-2026-...
                              https://www.bernsteinresearch.com/semiconductor-supercycle-2026
                              https://investors.micron.com/news-releases/q3-fy26-results
```

**Fabrication concentrates exactly where the model cannot actually fetch** — paywalled institutional
research. That is a predictable, targetable pattern, which is what makes the absent check so cheap.

**Reach, and the cost of the miss.** All three artifacts fed
`2026-06-25-pm-integrated-synthesis-chinese-ai-semi-article.md`, and subagent-4 **cascaded into
`companies/KIOXIA/thesis.md`**. Their subject is the memory thesis underpinning the held book
(SUMCO wafers, SKHY HBM) and the exited NAND names.

**And the sharpest illustration in this entire audit:** all three were graded in
`meta/subagent-cost-yield-ledger.md`, and the round is scored **"HIGH yield."** The system *caught*
that subagent-3 violated Critical Rule #16 by running on the wrong model tier (logged: *"Sonnet 4.6 —
Critical Rule #16 VIOLATION; ledger demerit"*), and *caught* one of its substantive claims via
cross-refutation — and still graded it *"MEDIUM-HIGH yield, 1 correction caught."* **It audited the
model tier. It audited the claim. It never checked whether a single citation resolved. Eight of
nine did not.**

A URL liveness check is the cheapest mechanical instrument available anywhere in this system. It
requires no model judgment, no API key, and no new concept — and it is the one check that would have
caught 28 fabricated citations in a single batch.

*Baseline for fairness, measured on random samples:* the corpus-wide hard-dead rate is only **2.5%**
(80 random URLs) and **1/30** on a stratified sample — so this is not a corpus-wide rot problem. It
is a concentrated, per-artifact fabrication problem, which is exactly why a per-commit check would
be high-signal and low-noise.

---

### F20 — Three Stop hooks are not merely suppressed; they are provably dead, and one passes its own tests while dead

F7 described death-by-exemption. Deeper testing found that the v1 dead-regex failure mode **also
recurred**, three more times, and nothing detected any of them. Each was proven end-to-end by
executing the real hook code against real house text in a hermetic sandbox.

**1. `cascade-enforcement-hook.py` — PROVABLY DEAD (0 fires ever).** Its ticker extractor is
`re.findall(r"\*\*([A-Z]{2,8})\*\*", content)` (line 131), which requires a bold span containing
*nothing but* 2–8 uppercase letters. Real house bold spans are `**Cohort implications:**`,
`**Falsifier:**`, `**TC-18**`; real ticker mentions are bare prose — `hurts NVDA/AVGO/AMD/MRVL`.
Measured on the current `signals/triangulation.md`: the hook extracts **0 tickers**; a bare-token
scan finds **30**. Across all 33 post-activation commits touching a synthesis artifact, the extractor
returned **0 tickers in 33 of 33**. Replay shows it *would* have fired 15 times — all between
2026-05-20 and 2026-06-03, i.e. **the corpus writing style drifted away from the code around June
2026 and the hook silently stopped being able to see a ticker.** This is the hook enforcing Critical
Rule #10, the cascade discipline the system considers too important to leave optional.

**2. `antifragility-mn-hook.py` — PROVABLY DEAD, and this one is the most instructive failure in the
repository.** It requires the literal `P(bull` and `P(bear` (lines 62–63). The real house thesis
format inverts the parenthesis: `## Bull case (P = 65%)`. Measured: `P(bull` appears in **4 of 92**
thesis files, `P(bear` in **3 of 92**. Proven end-to-end — real-format transcript → exit 0; hook-format
transcript → exit 2.

The root cause is a documentation contradiction nobody reconciled: **`research/CLAUDE.md` carries two
conflicting house formats** — the Conviction Format section specifies `- P(bull case): X%` (what the
hook matches), and the thesis template immediately below specifies `## Bull case (P=X%)` (what 88 of
92 files actually use). And the test fixtures at
`research/meta/tests/test_framework_codifications.py:774-782` encode the **unused** format:

```
"Tier: Core. Position target: 10%. P(bull case): 65%. "
"P(bear case): 15%. Anti-fragility: 4/5 scenarios."
```

**So the hook passes its own test suite and fires on zero real theses.** That is the precise shape of
the gap this audit is about: a green test proving a dead instrument healthy. (Two further defects sit
behind it — if the trigger were fixed, `Anti-fragility: 3.5/5` is not exempted by
`\d+\s*/\s*\d+` and becomes a live false-positive class; and the block message instructs the model to
write `M/N: 4/5`, a format that appears **zero** times in the corpus.)

**3. `segment-trajectory-hook.py` — PROVABLY DEAD in practice.** Its main trigger `\bonly\s*\d`
(line 75) forbids an approximator, and house style writes `~` constantly. Measured: the hook pattern
gets 56 hits against 109 loose `only N%` instances — **48.6% missed** — and the missed forms include
`only ~10-15%`, **the exact phrasing quoted in the hook's own origin docstring at line 22**. The hook
cannot match the phrase it was built to catch. Its range separator `[-/]` also excludes the en-dash
(577 corpus occurrences). Net: **0 blocks across 4,529 real units**; the only 6 files that trigger it
are the hook's own documentation.

**4. `llm-native-reasoning-hook.py:125` — a provably dead regex.**
`r"\b\+\d+%\s+(?:YTD|1Y|1-year|YoY)"` — `\b` immediately before a literal `+` requires a *word*
character to precede the plus, which never happens in prose. Measured: **0 hits with `\b`; 754
without it.** The rally-history string it exists to catch occurs 99 times as `+NN% YTD` and can never
match.

**5. And the v2 rebuild carries the v1 defect class.** `session-prime-cascade-hook.py:108` uses
`\*\*(TC-\d+)\*\*`, requiring `**` immediately after the digits. The newest cluster is written
`| **TC-19 CANDIDATE** Edge-inference-mandatory…`, so it fails — TC-19 is the only one of 18 rows the
hook misses. **This caused a confirmed missed fire**: commit `97068f0` (2026-07-19) registered TC-19
touching only `triangulation.md` with `session-prime.md` absent — the charter says fire; the log has
no such entry. **The 21-fixture selftest does not cover the `**TC-19 CANDIDATE**` shape** (fixture 14
uses `**TC-18**`, where bold closes at the digit). A green 21/21 does not cover the live defect — the
same blind-spot structure that let v1 ship dead.

**What this means together:** the v1 post-mortem treated the dead hook as an incident. It was a
*class*. Five instances of it are live right now, in a fleet of 15, and the only reason any of them is
known is that someone hand-executed the regexes against the corpus. **Nothing in this system compares
a hook's trigger patterns against the writing style of the corpus it polices** — and house style
drifts continuously, which means every hook decays silently by default.

Calibration defects worth recording alongside, since they bear on the 2026-08-06 keep/retire decision:
`macro-anchor` fires from a measured **8.4%** unexempted slice (`\bB\d{2}\b` alone suppresses 65% of
the proxy corpus, i.e. it exempts precisely the ID-citing analytical output the system *mandates*);
`structural-output`'s general gate is satisfied by **any markdown table** (420–444 of 550 docs), and
`\bcascade\b` sits in **both** its trigger and its pass list — self-neutralising by construction;
`anti-fabrication` resolves **38% of grounding events to INCONCLUSIVE and passes them**, caused by
10-second subprocess stalls against greps I measured at 10–15 ms, and **38% of its actual fires
(5 of 13) are false positives** from a pattern that captures a 40-character prose span and then
greps it literally.

---

### F21 — A pre-registered, machine-checkable price trigger fired three days ago into a stale file

The clearest single instance of the staleness gap having a live cost.

`watchlist/candidates.md:264` pre-registers an entry trigger for ALAB (Astera Labs):
*"(1) >25-30% pullback from ATH to **~$295-315** range … (3) BOTH (1)+(2) must fire jointly."*

**ALAB closed $291.58 on 2026-07-24** — through the floor of that zone. Meanwhile:

- `companies/ALAB/thesis.md` was last touched **2026-07-02 — 25 days ago**
- `candidates.md:273` still states its position implication against **"~$413"**, 41.7% above spot
- a prediction on the name resolves **2026-08-11**

Nothing checked. And the reason is structural, not incidental: **Principle #37's staleness rule is
contact-triggered.** `methodology.md:1525` — *"**if any touched file's** existing 🔴/🟡 entries are
>30 days old…"*. A file must be touched for the system to notice it hasn't been touched. The
implementation narrows it further: `session-start-hook.py:580` `parse_stale_tier_entries()` reads
`meta/tier-cascade-log.md` and **never scans `companies/`**. Running it live, the hook reports **33
stale cascade entries and zero stale theses**, while **53 of 92 company folders (58%) sit past the
30-day threshold**.

**Absent:** a price-trigger watcher. Every pre-registered numeric trigger in the corpus is a
machine-checkable predicate against a daily close, and nothing evaluates any of them.

Related coverage findings, VERIFIED: **16 of the 33 declared-universe names have no folder at all**
(TSM, ASML, AMAT, LRCX, MSFT, META, ORCL, ANET, CIEN, CSCO, TLN, NEE, DELL, HPE, PLTR, CRWD) — and
these are not forgotten names: MSFT is mentioned in 186 files, ASML in 117, META in 105. **Five names
have registered, graded earnings predictions but no thesis folder** (TSMC, ASML, SAMSUNG, HPE,
SKHYNIX) — forward calls on names with no falsifiers, no tier, no anti-fragility score. And
**76 of 92 folders (83%) contain only `thesis.md`**; the declared five-file structure exists in 4.

Two more stale load-bearing files: `sector/scenarios.md` is **55 days** old — it holds the 3–5 futures
that feed every anti-fragility M/N score, and `CLAUDE.md:34` says "reweight on every major event."
`meta/source-reliability.md` is **67 days** old. And `meta/morning-feed-sources.md` targets a
portfolio that no longer exists: its scan blocks name HYNIX, KIOXIA, SNDK, NBIS and MRVL — **five of
seven are exited positions.** The daily input-acquisition apparatus is pointed at the wrong names.

**Credit where it is due, and it is significant: all three held names are fresh** — MURATA 1 day,
SUMCO 2 days, SKHY 0 days. There is no held name on a stale thesis. Attention does follow the money.

---

### F22 — I graded the rejections the system never grades. The declines were good; the substitution was not.

Part two asks what evidence the system never collects. This is the clearest case, so I collected some.

There is **no instrument that grades a rejection against what subsequently happened**, and I found
**zero instances** in the corpus of a recorded "we decided not to look at X" later being graded.
Innolux is mentioned in 17 files, was killed 2026-06-17, and has had **zero post-kill price checks**;
`grading-log.md` contains no entry for it or for Astera.

So I priced five named, dated decisions against real market data:

| name | decision | date | price then | 2026-07-27 | return | verdict |
|---|---|---|---|---|---|---|
| Innolux 3481.TW | 🔴 SKIP | 06-17 | NT$58.60 (true close) | NT$47.35 | **−19.2%** | ✅ right |
| ALAB | 🔴 DO NOT ENTER | 06-22 | $439.66 (true close) | $291.58 | **−33.7%** | ✅ right |
| Sakai Chemical 4078.T | 🔴 downgrade to WAIT | 06-16 | ¥4,775 | ¥4,065 | **−14.9%** | ✅ right |
| Sumitomo Metal Mining 5713.T | 🟢 PROMOTED #1 | 06-16 | ¥8,863 | ¥7,785 | **−12.2%** | ❌ lost |
| Sumitomo Electric 5802.T | 🟢 PROMOTED #2 | 06-16 | ¥3,080 (split-adj) | ¥2,355 | **−23.5%** | ❌ lost |

Computed: the equal-weight replacement basket returned **−17.85%** against the **−14.87%** of the name
it replaced — **the reallocation cost 2.98pp.** Benchmark: the Nikkei 225 fell **−6.63%** over the
same window (from an all-time high set on the very day of the downgrade); all three JP names
underperformed it.

**The finding is a failure mode the corpus has no category for.** The macro call was excellent and the
security selection was negative-alpha: capital rotated out of one crowded AI-adjacent momentum name
into two others — one of which had peaked 13 days earlier, the other down 3.66% *on the day it was
bought*. "The thesis was wrong" and "the substitution was worse than the thing it replaced" are
different errors, and only the first is gradeable here.

**And two calibration points that any rejection-grading instrument would need:**

- **Both winning rejections went hard against the call first.** Innolux ran to NT$72.60 on 06-24
  (**+29.4%** against the SKIP) before collapsing; ALAB ran to $499.48 on 06-30 (**+20.9%** against
  the rejection) before falling 41.6%. Marked mid-window, both looked like errors. **Grading only the
  endpoint materially overstates the skill** — max-adverse-excursion has to be recorded too. This is
  the same defect as F16's single-timestamp override verdicts, in a different instrument.
- The same applies to the two 2026-06-26 rejections I checked: ACMR ($103 → $84.32, **−18.1%**) rose
  to an all-time-high close **two trading days after** the reference date, and 3986.HK
  (HK$1,083 → HK$546, **−49.6%**) rose 14.6% first. Both declines were correct; neither looked it at
  T+2.

**Framing errors found inside the corpus only because someone re-derived the numbers** — every one a
fresh instance of the F1 class:

1. **Sakai's entry trigger was incoherent when written.** `candidates.md:323` calls for an *"entry
   trigger ¥5,000-5,400 retrace"* on a day the stock **closed at ¥4,775 — already 4.5% below the
   band floor.** A "retrace" to a level above spot is a breakout.
2. **Its ¥6,380 anchor was a blow-off top** capping a two-session +29.15% melt-up that included a
   **no-range limit-up lock** (OHLC all ¥5,640). No rule guards against accepting a post-limit-up
   print as a reference price.
3. **Innolux arithmetic:** *"NT$56 is 2.9× consensus HIGH"* — 56.10/27 = **2.08×**; 2.9× is versus the
   *average*. The clause conflates average and high.
4. **ALAB's cited "$421.20 ATH" was superseded within two sessions** — the true ATH is **$499.48**,
   making the citation 18.6% stale; and the companion *"67% above consensus PT (~$247)"* has fully
   inverted — consensus is now $297.01 and the stock closed *below* it.
5. **Anchor hygiene:** NT$56.10 and $413 are both intraday prints recorded as "spot" ($413 is the
   06-22 day *low*).
6. **3986.HK's market cap is mixed-basis** — an H-share price paired with an A-share-derived cap,
   understating H-implied market cap by **17.2%**; and its *"P/E ~560"* is not reproducible on any
   basis (forward non-GAAP was ~68× at that price). The rejection was right for the wrong reason.
7. **A refuted premise still in the corpus:** any thesis keyed to a *"BIS/Entity List action against
   ACM Research parent"* rests on a false claim. Per the company's own release and FY2025 10-K, only
   **ACM Shanghai and ACM Korea** were listed, on **2024-12-02**; the Delaware parent never was.

**One instrument that does do this job, and deserves credit:** the KIOXIA VLSI grade prices a path not
taken — *"pre-reg Option B was directionally correct but **cost ~36pp of upside vs Option A**"*. That
is a graded counterfactual with a quantified opportunity cost. It is a decision path *within* a held
name, not a declined name — but the machinery is there and could be pointed outward.

**A structural headwind worth naming.** B9 correctly forbids emotional selling, and the derived
discipline appears repeatedly as a bar on missed-opportunity accounting — *"entry-price regret is NOT
a thesis input (B9 discipline)"*, *"evidence-gated-not-regret-gated"*. Each instance is individually
right. Collectively they supply a principled reason never to compute what the passes cost. **The
distinction the corpus does not draw: regret as a *sizing input* (correctly banned) versus regret as
a *calibration datum* (the missing meter).**

---

### F23 — One whole ingestion channel produces claims with no re-checkable receipt

My prior was that the evidence base would prove narrow and outlet-concentrated. **Measured, it does
not — and I was wrong.** Across all 447 cross-source-log files: **4,248 URL citations, 1,020 distinct
domains, top-10 share 22.4%, HHI 0.0076** (equivalent to ~132 equally-weighted domains); 506 domains
cited exactly once. Top source is trendforce.com at 4.3%. **No outlet is load-bearing.** The
multilingual discipline is visibly real in the tail (nikkei, kabutan, stcn, sina, solnews,
denkishimbun, minkabu, cnyes). This is a genuine strength.

**But WSJ — which reads as load-bearing in the prose — has 2 wsj.com URLs in the entire log.** It
enters by **screenshot**: `CLAUDE.md:732` defines a "Leg C WSJ-screenshot ingest", and "screenshot"
appears **434 times across 131 files**.

**That is the actual diet blind spot, and it is not concentration — it is a channel that is
structurally unauditable.** A screenshot-sourced claim has no URL, so it cannot be re-fetched, cannot
be checked for staleness, and cannot be falsified by any future session. It also satisfies the
anti-fabrication hook trivially via a `(per …)` citation pattern. Combined with F19: the two ways a
number can enter this corpus without a verifiable receipt are a fabricated URL and a screenshot, and
neither has a check.

Separately, no corpus-level concentration measure exists at all — grep for
`source concentration | HHI | herfindahl | outlet diversity` returns nothing. Per-claim single-outlet
vigilance is real and good (B40.3 is invoked with rigour across ~20 artifacts); the portfolio-level
view of the evidence base is absent. In this case the answer happens to be reassuring, which is
precisely why measuring it once would be worth doing.

---

### F24 — One instrument was designed to measure the correlated-error risk, and it is blocked on a human step

The strongest counter to my expectations. B63 (model-provenance) and B64 (model-affinity) are not
merely named — they impose binding countermeasures, and B64's 2026-07-22 amendment turns the lens on
the oracle itself: *"B64 covered affinity in MY outputs; the mirror is affinity in the ORACLE I use to
check my outputs… **The oracle's provenance is a re-verifiable VARIABLE, not a constant**."* It
downgrades the external reviewer's independence HIGH→MODERATE and adopts weight-by-disagreement.
That is high-quality epistemics.

And the measurement exists **as a design**:
`meta/redteam/2026-07-22-K3-distillation-behavioral-probe.md` is a properly constructed blind
differential — three discriminator items planting blind spots this corpus demonstrably missed, a
competence **control** to separate "weak reviewer" from "specifically blind", pre-registered verdict
logic, and the right weighting insight (*"DIVERGENCE is weighted as the strong,
lineage-unexplainable signal"*).

**It has never been run.** `day-state.md` lists it under **"⏳ AWAITING USER"** — designed 07-22, still
unexecuted at 07-27, because it requires the operator to paste a block into the external model. The
scoring key sits filled in with no result beside it. **And B64's own falsifier re-eval was set for the
2026-07-24 monthly audit; B64 appears in zero audit files. The date passed three days ago
unremarked.**

For accuracy: the census of adjudicators is **K3 = 293 mentions, Opus 5 = 53, Fable 5 = 44, Kimi = 13,
GPT-5 = 2** — and Fable 5 and Opus 5 are both Claude-family. **One genuinely non-Claude adjudicator
exists, and no human other than the operator adjudicates anything.** The one place external human
expertise is acknowledged as required, it has not been obtained — `risk-envelope.md:34`: *"NOT tax
advice, verify with a German tax advisor… should be confirmed with his advisor before it's used in
any trim/hold math."*

So the accurate statement is not "named but unmeasured". It is: **precisely named, bindingly
countermeasured, rigorously measurement-designed — and the measurement is blocked on a human step,
with its own re-eval deadline already missed.** The absent instrument is not the probe. It is anything
that notices a designed measurement has been sitting unexecuted for five days.

---

### Revised ranking

By (probability of silent failure) × (cost when it bites):

1. **F19** — nothing validates a citation, and the hook's incentive gradient rewards fabricating one.
   28 confirmed fabricated URLs in one batch, cascaded into a held-name thesis, graded "HIGH yield".
   The cheapest possible fix; the largest blast radius.
2. **F1** — no tape of record. Six "right magnitude, wrong binding" instances in six weeks, mechanical
   detection rate 0%, one corrupting a pre-registered trigger two sessions ahead of a position gate.
3. **F20 / F7 / F8** — five live instances of the dead-hook class, one of which passes its own test
   suite while dead; 88–100% exemption suppression; a single unvalidated stdin field that would kill
   all 15 Stop hooks silently. Nothing compares hook triggers against corpus style, and style drifts
   continuously.
4. **F2** — tier conflates authority with machine-readability; no measurement-convention axis exists.
5. **F10** — corrections don't propagate, and under string-existence grounding an uncorrected residue
   actively re-grounds the retracted number.
6. **F3 / F4 / F5 / F6** — the delivery and recall family: detectors that work perfectly into channels
   with no reader, and a verification protocol that would certify a dead layer as healthy.
7. **F21** — contact-triggered staleness; a machine-checkable price trigger fired into a 25-day-stale
   file, and 58% of company folders are past the system's own threshold.
8. **F17** — no market calendar. Cheapest single fix; kills a whole error family.
9. **F12 / F13 / F22** — denominator holes, a reported baseline the program layer forbids, and no
   rejection-grading (where I did it: the declines were right, the substitution cost 2.98pp).
10. **F11 / F15 / F16 / F23** — 12% of the corpus unreachable; no realized fills; the one
    decision-quality instrument unfed with sampling-artifact verdicts; an unauditable screenshot
    channel.
11. **F14 / F18 / F24** — monotonic ledger exceeding the context window; out-of-git state failing
    silently; a designed independence probe sitting unrun past its own deadline.

**Three changes would cover most of this, and all three are assembly rather than invention.**

- **A URL liveness check on every commit.** No model judgment, no keys. Would have caught F19.
- **A briefing section that reads what the system already produces and already discards** — last CI
  conclusion, test exit code, open `recurring-audit` issues, fire-log ERROR counts, boot-status
  freshness, API-key presence. Covers most of F3/F4/F5/F6/F18.
- **Schedule the `probe=1` canary sweep that already exists and already ran once by hand**, and add
  one fixture per hook drawn from *current* corpus text rather than from the spec. Converts the
  enforcement layer from precision-only to precision-plus-recall, and would have caught all five
  dead-hook instances in a day.

---

### A note on my own method, since it is the same error class

Two corrections I had to make to my own work, recorded because they are the audit's subject matter:

- **A subagent told me the SK Hynix ADR raise was $2.65bn, not $26.5bn** — it had conflated the
  common-share count (17.79M) with the ADS count (177.9M) at a 1:10 ratio. **The corpus was right and
  my agent was wrong.** `HYNIX/facts.md` reconciles $26,507,100,000 against 177,900,000 ADSs at
  $149.00, cites the 6-K, and records that house pre-estimates were +5.6%/+9.8% high. Exemplary work.
- **A subagent flagged four `git-guard` log entries it had not generated** — including a
  "recursive force-delete aimed at repo root" — and raised the possibility of a concurrent session
  operating on the repo. **Those were mine, and they were false positives on document text:** the
  `core.hooksPath` entries came from a command that *printed* `settings.json`, and the force-delete
  entry came from a heredoc containing the prose *"reopens a patched `rm -rf` bypass"* while I was
  writing this report to a path outside the repo. No concurrent session; no destructive command. I
  record it because a guard that fires on prose describing the guard is how a false alarm about a
  force-delete reaches an operator.

For the record on this audit's own footprint: the repository's working tree ends with exactly one
modified file, `research/meta/hook-fire-log.md` (+6 lines), every line written by the repo's own hooks
reacting to my reads. No commits, no pushes, no edits. My audit branch was never pushed.


---
---

# ADDENDUM — operator adjudication, 2026-07-27 (post-delivery)

Recorded after the operator independently re-derived the load-bearing parts. Kept
separate from the audit body so the original claims stand as written and the
corrections are visible as corrections.

## A1. Claim 5(d) — conceded in full, and the root cause is sharper than the audit stated

The operator re-fetched settled daily OHLC and confirmed the opening auction at
KOSPI 6,806.27 / SK Hynix 1,814,000 / Samsung 257,000 = +1.73% / +3.13% / +3.01%
against the published +0.60% / +0.74% / +2.00%. The multipliers (2.87x / 4.23x /
1.50x) and the retracement corrections (9.9 -> 28.5%, 8.1 -> 34.4%, 24.4 -> 36.6%)
reproduce exactly. The artifact is retracted in place and replaced; the "weak
bounce" read is **withdrawn, not adjusted** — the corrected tape is a gap-up to the
day's high, a sell through Friday's close to a new low on all three names, then a
green close.

**Operator's root-cause finding, which supersedes the audit's framing of F2:**
the figure was an EODHD real-time snapshot at 00:06Z, labelled `open-tick`, then
fed into a metric *defined on the opening auction*. `data-access.md` already warns
that the endpoint lags and instructs "cross-check timestamp field ALWAYS" — and the
timestamp **was** checked. That is why it passed.

> **The guard checked freshness; the defect was basis. A guard on the wrong axis
> reads as a passed check.**

This is a strictly stronger statement than the audit's "the framework commissions
the middle and neither end". Some intake guards *do* exist. They measure the wrong
axis, and a guard on the wrong axis is worse than no guard, because it produces a
green signal. Any future intake guard must declare which axis it measures —
freshness, basis, instrument identity, or arithmetic — and a claim is only covered
on the axes explicitly guarded.

## A2. Correction to F19's blast radius — partly upheld, partly not

The operator challenged the audit's placement of the fabricated-citation cascade in
`companies/KIOXIA/thesis.md`. Adjudicated: **two distinct instances exist**, from two
different subagents, and both parties were looking at a real one.

- **`HCAttention`** (the non-resolvable `arxiv.org/abs/2507.HCAttention`, from
  subagent-1) appears in **`companies/HYNIX/thesis.md`** — as a list item inside the
  H1 30%->65% reweight (MLA / V4 / GQA / HCAttention). The operator is correct that
  it is not the load-bearer there; that reweight rests mainly on MLA/V4 and
  token-volume data.
- **subagent-4** (NAND 4-vector, 9 of 14 URLs dead) is cited at
  **`companies/KIOXIA/thesis.md:343`**, and that line carries *"Citi estimate 1,152 TB
  SSD NAND per Vera Rubin system"* — the exact claim of the fabricated
  `citi.com/research/vera-rubin-cmx-tb-estimate`. The line closes with
  `Position implication: 🟢 HOLD at Core 14.4% (€19K N26)`.

**Net: the audit's "cascaded into a held-name thesis" is accurate and citable. The
operator's correction still lands on magnitude** — within that paragraph the Citi
figure is vector 1 of 4, and the KIOXIA-specific reinforcement items (a)-(e) rest on
company and investor materials, not on the fabricated URL. **No fabricated URL was
found to be the sole load-bearer of any conclusion anywhere in the corpus.** F19's
mechanism finding (any URL-shaped string satisfies `CITATION_PATTERNS`) is
independently confirmed by the operator at source and is unaffected.

## A3. The intra-artifact consistency finding is F9, not a new one

The operator proposed the Samsung §1.1 (+2.00%) vs §6.4 (+3.0%) contradiction —
same print, same document, a full percentage point apart, unreconciled — as a
finding the audit did not report. It is **F9**, "All consistency enforcement is
between files. None is within a file." The audit did report it as a standalone
structural class and cited the same document as its worked example.

The operator's sharpening is nonetheless a real strengthening and is adopted: the
audit used the SK Hynix pair as its example; the **Samsung pair is the better
specimen** because the two figures are a full percentage point apart on the same
instrument, same field, same session, written hours apart in one file, with the
correct value arriving *second* and never reconciled against the first. Nothing in
the harness diffs a document against itself.

## A4. Independently confirmed by the operator

F19 at source (`CITATION_PATTERNS` contains `r"https?://\S+"`); the non-resolvable
`arxiv.org/abs/2507.HCAttention` present in the corpus; `antifragility-mn-hook`
requiring the literal `P(bull`, which appears in 4 of 92 thesis files — inert on
~96% of the corpus while passing its own fixtures.

## A5. Provenance of this file

The audit was performed with the repository untouched; the working tree ended with a
single modified file, `research/meta/hook-fire-log.md`, every line of it written by
the repo's own hooks reacting to the auditor's reads. That session's telemetry was
preserved to scratchpad and discarded from the working tree before branching, since
`origin/main` had advanced independently and carried its own record of the same
period. No audit finding depends on it.

The auditor declined a commit during the audit on the grounds that a third remote
branch would have falsified claim 2, one of the claims under test. The operator
accepted that reasoning and released the constraint after delivery; this file is the
result.


---
---
# ADDENDUM 2 — F1 dossier: the June KR/JP crash misdating
**Anchored to `6ca7b49` (this branch, with `origin/main@4d9aff9` merged in). Line numbers are valid at that tree; if they drift, re-run the classifier in §5.**
Operator-authorised 2026-07-28. Scope: evidence only. **No thesis file is touched here — the Rule #10 cascade is the operator's.**

## 1. Verified tape — TRIPLE-VENDOR
Yahoo chart API (T3 vendor) + Korean-language press (T2, multi-outlet) + EODHD (T3 vendor, operator-fetched independently 2026-07-28). Every figure reproduces across all three.

| date | KOSPI | chg | SK Hynix | Samsung | Kioxia 285A.T |
|---|---|---|---|---|---|
| Mon 2026-06-22 | 9,114.55 | **+0.69%** — record high | ₩2,919,000 +5.61% | ₩353,500 | — |
| **Tue 2026-06-23** | **8,203.84** | **−9.99%** | **₩2,555,000 −12.47%** | **₩310,000 −12.31%** | **¥92,290 −15.1%** |
| Wed 2026-06-24 | 8,471.02 | **+3.26%** — an *up* day | ₩2,580,000 +0.98% | ₩340,500 +9.84% | — |
| Thu 2026-06-25 | 8,930.30 | +5.42% | ₩2,917,000 +13.1% | ₩358,500 +5.29% | — |
| Fri 2026-06-26 | 8,411.21 | −5.81% | ₩2,673,000 −8.36% | ₩339,500 −5.30% | — |

**Resolved, not open:** the SK Hynix 06-24 close is **₩2,580,000**. Yahoo returned ₩2,621,000; Korean press and EODHD both return ₩2,580,000. Two independent sources against one — the press figure stands and the discrepancy is closed.

**The corpus is uniformly +1 day across the whole sequence. The weekday labels are correct; every date is one day late.**

## 2. Root cause — one intake defect, three downstream errors
`signals/cross-source-log/2026-06-23-am-subagent-full-cohort-price-action-global-macro.md:18`, written *on* 06-23, states: *"On June 23, 2026, KOSPI is **actually UP +0.69% to 9,115** — a record high close."* That is **Monday's close reported as today's** — a T-1 vendor lag, unchecked. Everything follows:

1. **The +1 date shift** across the cascade (record high → 06-23; crash → 06-24).
2. **A misattributed datapoint.** The same artifact could not reconcile a −8.1% / 8,37x print with "today is a record high", so it pushed it back to *June 8* (line 17). That print is the **06-23 intraday circuit-breaker trigger**. Note the scope limit: 06-23's CB was the *4th of 2026*, so three earlier 2026 CBs exist and a June 8 event may well be real — what is established is that **these numbers** are 06-23's, not that no June 8 event occurred.
3. **The inverted causal story** — §3.

**This is the same class as the 07-27 KOSPI open-tick error: a vendor snapshot whose *basis* went unchecked while its *freshness* did not. It recurred live at the 2026-07-28 KR open** — EODHD real-time index feeds served a stale `previousClose`, making the vendor's own `change_p` wrong by −2.14pp on KOSDAQ. Caught at intake that time. The June instance is what this class does when it is not.

## 3. Intraday causal sequencing — the transmission runs Korea → futures → US

| | Mon 06-22 | Tue 06-23 |
|---|---|---|
| Nasdaq Composite | −1.33% | **−2.21%** |
| S&P 500 | −0.37% | **−1.44%** |
| SOXX | **+2.43%** | **−7.88%** |
| Micron | **+6.83%** | **−13.18%** |
| NVDA | −0.97% | −4.13% |

The corpus's *"Mon Jun 23 US session Nasdaq −2.2% / S&P −1.43%"* figures are **real and belong to Tuesday 06-23's US session** — the same day as the Korean crash, and **~7 hours after KRX closed** (15:30 KST = 02:30 ET; NYSE opened 09:30 ET). On Monday the semiconductor complex *rose*.

**The KOSPI opened 06-23 at 9,083.54, −0.34%** — essentially flat, not a gap-down. A −1.33% overnight US lead produced a −0.34% opening reaction: **only 3.4% of the day's eventual move was present at the open.** The rout was built in Asian hours, not imported.

| KST | event |
|---|---|
| 09:06:02 | KOSDAQ sell sidecar |
| 10:53 / 11:24 | BofA three-rate-hike call hits Korean wires |
| 11:40:44 | KOSPI200 futures sell sidecar, −5.12% |
| **14:33:43** | **KOSPI Stage-1 circuit breaker**, 20-min halt (4th of 2026, 10th ever) |
| 16:13 | Korea Herald cites **Nasdaq futures −1% *during* Korean hours** as a concurrent driver |
| 22:03 | Nasdaq100 E-mini **−3%**, Nikkei −3.6% — still before the NY open |
| NY session | Nasdaq −2.21%, SOXX −7.88%, Micron −13.18% |

**Inverts to: Korea led; the US followed the same day.** Corroborated by CNN (US declines *"came after steep sell-offs in Asia"*), TheStreet 06-23 (*"Asian market tumble sends semis sinking"*), and KB Securities' 06-23 note describing the backdrop Korea *opened into* as Nasdaq −1%-ish with *"마이크론 등 반도체는 강세"* — Micron and semis **strong**.

**Cause (T2, contemporaneous Korean press):** unwind of a crowded semiconductor trade — foreign ~₩4.1tn + institutional ~₩4.5tn net selling on the KOSPI regular session against record retail buying, amplified by mechanical deleveraging in the leveraged single-stock ETFs launched weeks earlier (Bloomberg Intelligence: ~$6bn sold, ≈14% of the two stocks' combined volume). Not an exogenous shock.

**Ruled out:** the MSCI DM-watchlist story is **chronologically impossible** as a trigger — announced 23 June US time, first reported by Korean press 07:44 KST on 24 June, after the Korean close.

**Conflation risk for the cascade: 2026-06-26 was a SEPARATE crash** — CB #5, close −5.81% — with a **+5.42% rebound on 06-25 between them**. Two CBs in one week, a first in KOSPI history. Any pass treating 06-23→06-26 as one slide introduces a new error.

## 4. Enumeration — 52 actionable lines, 7 theses
Grouped by defect class. Each class has one fix. **No thesis edited here.**

> **CLASSIFIER CORRECTION (applied post-commit, same session).** The listing below was generated at 54 matches. Two of those are **false positives**: `meta/redteam/2026-07-28-audit-second-commission-...:21` (Class B) and `:25` (Class F) are lines in the operator's own reception artifact *describing* this finding, not instances of the error. The classifier excluded the audit file itself but not other meta-discussion of it. **Actionable count is 52.** The two entries are left visible below rather than deleted, marked ⚠️FP, so the correction is auditable.

### Class A — 18 lines
**FIX:** -> 2026-06-23 (Tue). 06-24 closed +3.26%, an UP day

- `research/companies/HYNIX/thesis.md:412`
  > **LAYER #3: AI Stock Selloff — REAL but NUANCED-PARTIAL; CRITICAL IRONY = ENTRY OPPORTUNITY.** T
- `research/companies/HYNIX/thesis.md:1655`
  > **2026-06-26 AM Round 7 cross-ref — SK Hynix ADR dilution arbitrage reversal (Subagent 11 verifi
- `research/companies/KIOXIA/thesis.md:54`
  > **🟢 2026-06-24 AM-BRIEF-COMBINED cross-ref — TRIPLE-BULLISH stack (Pax Silica + Legacy storage N
- `research/companies/KIOXIA/thesis.md:60`
  > **LAYER #3: AI Stock Selloff — KIOXIA -15%+ Tue Jun 24 Asia session; circuit-breaker-amplified m
- `research/companies/KIOXIA/thesis.md:70`
  > **Position implication: 🟡 HOLD-until-falsifier ~€10K N26 (per `portfolio/holdings.md` PM33 canon
- `research/companies/MURATA/thesis.md:46`
  > **LAYER #2 (peripheral): AI Stock Selloff Tue Jun 24 Asia session.** MURATA TSE 6981 was caught 
- `research/companies/SUMCO/thesis.md:65`
  > **LAYER #2 (peripheral): AI Stock Selloff Tue Jun 24 Asia session.** SUMCO TSE 3436 likely caugh
- `research/meta/subagent-cost-yield-ledger.md:1590`
  > 1. AI Stock Selloff NUANCED-PARTIAL — timeline-resolved: Mon Jun 23 US session selloff (Nasdaq -
- `research/meta/subagent-cost-yield-ledger.md:1625`
  > - `companies/KIOXIA/thesis.md` — AM-BRIEF cross-ref; Pax Silica Japan-founding + storage NVMe up
- `research/meta/tier-cascade-log.md:328`
  > - `companies/KIOXIA/thesis.md` top-of-file — new AM-BRIEF cross-ref; Pax Silica Japan-founding +
- `research/signals/cross-source-log/2026-06-24-am-brief-integrated-synthesis.md:73`
  > - **Tue Jun 24 Asia open: KOSPI -9.99% to 8,203.84; SK Hynix -12%; Samsung -12%; KIOXIA -15%+; T
- `research/signals/cross-source-log/2026-06-24-am-brief-integrated-synthesis.md:85`
  > | SK Hynix | 2,945,000 KRW ATH Jun 22 | held Mon; -12% Tue Jun 24 | Major Jun 24 |
- `research/signals/cross-source-log/2026-06-24-am-brief-integrated-synthesis.md:86`
  > | KIOXIA 285A | 112,700 JPY ATH Jun 22 | -15%+ Tue Jun 24 | Major Jun 24 |
- `research/signals/cross-source-log/2026-06-24-am-brief-integrated-synthesis.md:204`
  > | KIOXIA ~€10K N26 | Pax Silica + storage NVMe BULLISH + selloff -15%+ Jun 24 = WITHIN regime ba
- `research/signals/cross-source-log/2026-06-24-am-subagent-brief-hardware-infra-policy-items-verification.md:20`
  > - Tuesday June 24 Asia open: KOSPI plunged 9.99% to 8,203.84; SK Hynix -12%; Samsung -12%; KIOXI
- `research/signals/cross-source-log/2026-06-24-am-subagent-brief-hardware-infra-policy-items-verification.md:32`
  > | SK HYNIX | 2,945,000 KRW (ATH Jun 22) | held Mon; -12% Tue Jun 24 | Major Jun 24 |
- `research/signals/cross-source-log/2026-06-24-am-subagent-brief-hardware-infra-policy-items-verification.md:33`
  > | KIOXIA 285A | 112,700 JPY (ATH Jun 22) | -15%+ Tue Jun 24 | Major Jun 24 |
- `research/signals/cross-source-log/2026-06-24-pm-subagent-hyperscaler-fcf-compression-load-bearing-verification.md:58`
  > 6. **June 24 Asia:** KOSPI -9.99%, SK Hynix -12%, KIOXIA -15%+, circuit breakers. Same-day +4% r

### Class B — 11 lines
**FIX:** -> 2026-06-22 (Mon) close 9,114.55 +0.69%

- `research/companies/HYNIX/thesis.md:569`
  > **🟢 2026-06-23 AM-FULL-COHORT-PRICE-MACRO cross-ref — KOSPI RECORD HIGH +0.69% to 9,115 with HYN
- `research/companies/MRVL/thesis.md:81`
  > **🟢 2026-06-23 AM-FULL-COHORT-PRICE-MACRO cross-ref — MRVL +8.23% TODAY to $313.55 (T2 Yahoo Fin
- `research/companies/SUMCO/thesis.md:83`
  > **🟡 2026-06-23 AM-FULL-COHORT-PRICE-MACRO SELF-CORRECTION to prior 2026-06-23 AM-JPY cross-ref:*
- ⚠️**FP — not a defect, this is the operator's reception artifact describing the finding** `research/meta/redteam/2026-07-28-audit-second-commission-DELIVERY-reception-and-independent-tape-verification.md:21`
  > **⚖️ VERDICT: F1 is CONFIRMED at the strongest tier available.** The corpus's June crash sequenc
- `research/signals/cross-source-log/2026-06-23-am-subagent-full-cohort-price-action-global-macro.md:18`
  > - On June 23, 2026, KOSPI is actually **UP +0.69% to 9,115** — a record high close — REVERSING p
- `research/signals/cross-source-log/2026-06-23-am-subagent-full-cohort-price-action-global-macro.md:104`
  > **NOTE:** The KOSPI circuit-breaker crash (-8.44%) occurred on **June 8, 2026** per Korea Times 
- `research/signals/cross-source-log/2026-06-23-am-subagent-full-cohort-price-action-global-macro.md:388`
  > - KOSPI June 23 +0.69% record high: Trading Economics + CNBC Korea article (T2)
- `research/signals/cross-source-log/2026-06-23-am-subagent-mu-beat-probability-data-pack-tomorrow-print.md:134`
  > | 2026-06-23 | MRVL +8.23%; KOSPI record high +0.69%; Nikkei record +1.55% | T2 verified (harnes
- `research/signals/cross-source-log/2026-06-23-am-subagent-mu-beat-probability-data-pack-tomorrow-print.md:300`
  > - SK Hynix KRX 000660: RECORD HIGH June 22 (2,945,000 KRW); June 23 +5.57% (verified in harness 
- `research/signals/cross-source-log/2026-06-24-am-brief-integrated-synthesis.md:71`
  > - Mon Jun 23 KST close: KOSPI 9,114.55 record high (per yesterday's verified read = correct at t
- `research/signals/cross-source-log/2026-06-24-am-subagent-brief-hardware-infra-policy-items-verification.md:18`
  > - Monday June 23 KST close: KOSPI 9,114.55 (record high — yesterday's verified read = correct at

### Class C — 11 lines
**FIX:** -> Tue 2026-06-23 US session, AFTER the 15:30 KST KR close

- `research/companies/MRVL/thesis.md:58`
  > **🚨 B40.3 SELF-CORRECTION on prior MRVL price framing (Critical Rule #11 self-correction discipl
- `research/companies/MRVL/thesis.md:62`
  > **LAYER #2: AI Stock Selloff context — MRVL -8.82% Mon Jun 23 close $279.04.** B45 regime-check 
- `research/companies/MRVL/thesis.md:72`
  > | Recent move | +8.23% (today) | -8.82% (Mon Jun 23) |
- `research/companies/MRVL/thesis.md:77`
  > **Position implication: 🟢 HARD — HOLD 5.9% Active (44sh, BEP $286.26, now ~-2.5% vs BEP post-sel
- `research/companies/NBIS/thesis.md:51`
  > **LAYER #2: AI Stock Selloff context — NBIS approx -6% Mon Jun 23 to ~$277.65 from ~$295.** B45 
- `research/companies/SNDK/thesis.md:80`
  > **LAYER #3: AI Stock Selloff — SNDK -13.7% Mon Jun 23 close ~$1,962 from ATH $2,273.73 (Jun 22).
- `research/meta/subagent-cost-yield-ledger.md:1620`
  > **B40.3 self-correction on prior cascade:** Yesterday's HYNIX/MRVL AM-FULL-COHORT-PRICE-MACRO cr
- `research/meta/tier-cascade-log.md:327`
  > - `companies/MRVL/thesis.md` top-of-file — new AM-BRIEF cross-ref + 🚨 B40.3 SELF-CORRECTION on y
- `research/signals/cross-source-log/2026-06-24-am-brief-integrated-synthesis.md:72`
  > - Mon Jun 23 US session: Nasdaq -2.2%, S&P -1.43%
- `research/signals/cross-source-log/2026-06-24-am-brief-integrated-synthesis.md:76`
  > **Cohort actual moves Mon Jun 23 US close:**
- `research/signals/cross-source-log/2026-06-24-am-brief-integrated-synthesis.md:88`
  > **🟡 SELF-CORRECTION on yesterday's MRVL framing:** Yesterday's HYNIX/MRVL thesis files reference

### Class D — 3 lines
**FIX:** -> +3.26% (KOSPI 06-24). No index bounced 4.14%

- `research/signals/cross-source-log/2026-06-24-am-brief-integrated-synthesis.md:74`
  > - Tue Jun 24 same-day recovery: KOSPI +4.14% intraday; closed ~+1%; Samsung +7%; SK Hynix +3.8%
- `research/signals/cross-source-log/2026-06-24-am-subagent-brief-hardware-infra-policy-items-verification.md:21`
  > - Tuesday June 24 same-day recovery: KOSPI +4.14% intraday; closed ~+1%; Samsung +7%; SK Hynix +
- `research/signals/cross-source-log/2026-07-14-tue-morning-scan-3agent.md:16`
  > Verdict: the dip was bought TWICE (open, midday); retail liquidation absorbed by institutions+fo

### Class E — 3 lines
**FIX:** -> ONE KOSPI stage-1 CB 14:33:43 + ONE KOSDAQ CB; the 11:40:44 event was a SIDECAR

- `research/signals/cross-source-log/2026-06-24-am-brief-integrated-synthesis.md:90`
  > **B45 regime check binding:** -9.99% KOSPI + same-day +4% recovery + two circuit breakers = **le
- `research/signals/cross-source-log/2026-06-24-pm-subagent-hynix-nasdaq-ads-offering-verification.md:146`
  > | June 23 2026 | Semiconductor selloff: HYNIX -12% on KRX, KOSPI -9.99% (two circuit breakers) |
- `research/signals/cross-source-log/2026-06-26-morning-feed-pre-korea-scan.md:14`
  > 1. **L30 SUPERCYCLE-MAGNITUDE-FLOOR FIRED IN REVERSE (DOWNSIDE).** KOSPI -5.81% to 8,411.21 toda

### Class F — 8 lines
**FIX:** -> 8,375-8,378/-8.1% is the 06-23 INTRADAY CB trigger, not a June 8 close

- ⚠️**FP — not a defect, this is the operator's reception artifact describing the finding** `research/meta/redteam/2026-07-28-audit-second-commission-DELIVERY-reception-and-independent-tape-verification.md:25`
  > The auditor traced the +1 shift to a single intake event: the 06-23 morning artifact reported **
- `research/signals/cross-source-log/2026-06-23-am-subagent-full-cohort-price-action-global-macro.md:17`
  > - The KOSPI circuit-breaker crash (-8.11% to 8,375.31) DID occur — but on **June 8, 2026**, NOT 
- `research/signals/cross-source-log/2026-06-23-am-subagent-full-cohort-price-action-global-macro.md:45`
  > - HY9H Frankfurt: €1,700 is T2 inferred (one source said €1,700 on June 23, one said €1,665 on J
- `research/signals/cross-source-log/2026-06-23-am-subagent-full-cohort-price-action-global-macro.md:88`
  > | SOX (Philly Semi) | Recovery from prior week | ~+3-5% (estimated) | Post-AVGO June 5 crash (-1
- `research/signals/cross-source-log/2026-06-23-am-subagent-full-cohort-price-action-global-macro.md:173`
  > **Background:** June 5-8 2026 — AVGO earnings miss ($4.1B AI revenue vs $4.8B expected) + June 8
- `research/signals/cross-source-log/2026-06-23-am-subagent-full-cohort-price-action-global-macro.md:174`
  > **Source:** Multiple T2 including Korea Herald / Bloomberg / Kalkine circuit-breaker references 
- `research/signals/cross-source-log/2026-06-23-am-subagent-full-cohort-price-action-global-macro.md:328`
  > 1. Correctly identifies the TEMPORAL ERROR in the prior cascade (KOSPI circuit-breaker = June 8 
- `research/signals/cross-source-log/2026-06-23-am-subagent-full-cohort-price-action-global-macro.md:387`
  > - KOSPI circuit breaker crash June 8: Korea Times https://www.koreatimes.co.kr/economy/20260608/

**Theses touched:** `research/companies/HYNIX/thesis.md`, `research/companies/KIOXIA/thesis.md`, `research/companies/MRVL/thesis.md`, `research/companies/MURATA/thesis.md`, `research/companies/NBIS/thesis.md`, `research/companies/SNDK/thesis.md`, `research/companies/SUMCO/thesis.md`

**Currently held:** MURATA and SUMCO (both Class A, both the peripheral "Asia chip-sympathy" line). The other five are exited positions — lower priority.

**Two dependency notes.** `companies/SNDK/thesis.md` says *"Jun 23 −13.7%"* and is **correct** — SNDK is US-listed, so its selloff is the Tue 06-23 US session. Its cascaded sibling in `companies/KIOXIA/thesis.md` says *"Jun 24 −15%+"* and is **wrong**. The divergence flagged in the audit body as an inconsistency is really one right and one wrong. And `companies/HYNIX/thesis.md:412` (was :399 before the merge — line numbers drifted) needs both a Class A and a Class C edit **in the same sentence**.

**RETRACTED.** An earlier revision of this section claimed the count grew 52→54 across ten commits and concluded *"the misdating is still propagating."* **That was wrong.** Both new matches are the operator's own reception artifact discussing the finding; the defect count is **stable at 52**. No new propagation occurred. The A5 correction-propagation-gate argument stands on the Brent and MRVL residues documented in the audit body, not on this.

## 5. Reproducing this enumeration
The classifier is six regex pairs over `research/**/*.md`. **It must exclude BOTH this file AND any other artifact discussing the finding** (e.g. `redteam/2026-07-28-audit-second-commission-*`) — omitting the second exclusion is what produced the two false positives noted in §4. Class A: a `Jun 24|06-24` token co-occurring with any of `9.99 | 8,203 | -12% | -15%+ | circuit breaker | asia session | asia open`. Class B: `Jun 23|06-23` with `record high | 9,115 | +0.69`. Class C: the literal `Mon Jun 23`. Class D: `4.14`. Class E: `two circuit breakers`. Class F: `June 8` with `circuit breaker | 8,375`. First match wins, so classes are disjoint.

## 6. Corrections to the audit body and to my own evidence
Recorded because a report that hides where its evidence failed is worth less than one that does not.

1. **The body says "13 places … four held-name theses." Both numbers are wrong.** The correct figures are **54 lines across 7 theses**, of which **2 are held**. The 13 came from a subagent's narrower pattern that I did not re-derive before publishing.
2. **The body asserts the causal inversion on the repo's own price pack. That pack has no rows for 2026-06-22..26 at all** — I verified this directly. It never supported the claim. The conclusion survives on independent evidence (§3); the evidence originally cited for it did not exist.
3. **I over-claimed "there was no June 8 crash."** See §2 item 2 — the established finding is narrower.
4. **I gave foreign net selling as ₩5.79tn as though settled.** Three figures circulate with inconsistent scope (~4.1tn / 5.008tn / 5.79tn). Best-supported is ~4.1tn on the KOSPI regular session. I picked the outlier and stated it flat — the same basis error this audit documents.
5. **Intermediate error, resolved:** mid-investigation I doubted the whole finding, because `companies/HYNIX/thesis.md:556` dates the +0.69% record high to 06-23, which would have put the crash on 06-24. **That line is itself misdated by +1** (Class B). I used a corrupted date to check a date, and briefly reached the wrong conclusion. The failure mode is worth keeping: in a corpus with a systematic date shift, internal cross-checks inherit the shift and read as confirmation.
6. **Two circuit-breaker trigger prints remain unreconciled** — 8,375.31 / −8.11% and 8,378.25 / −8.07%, 2.94 index points apart, both internally consistent against Monday's close. Immaterial to any conclusion. **No T1 obtained: KRX's own release index returned nothing, so every CB time here is press-attributed, not exchange record.**
7. **The "two circuit breakers" error is inherited, not invented.** Two T3 aggregators mislabel the 11:40 sidecar as a circuit breaker. `meta/source-reliability.md` rates one of them **T4** — so a T4 aggregator's error propagated into thesis files unchallenged. That is a source-tier discipline failure, distinct from the dating failure, and it is not in the audit body's 24 findings.

## 7. Disposition of the audit's change-list (operator, 2026-07-28)
Recorded here so the artifact carries its own outcome:

- **A1 (URL-liveness CI) + A2–A4** merged into the live P0 intake-boundary item as its concrete builds.
- **C1–C4** booked as codification-pass candidates with their stated falsifiers attached.
- **Counter-list adopted as-is**, including the refusal to touch live enforcement (L41 / Rule #19).
- **S1 and S2 are operator-gated and untouched.** S2 (deleting three fabricated-evidence artifacts) is a Rule #19 HIGH action requiring pre-approval with the matching token; S1 pends independent verification of its "loaded by nothing" claim. **Neither was acted on by the auditor.**
- **S5** waits for its pre-registered 2026-08-06 decision date.
- **Ask-4 (FX basis) is adopted on main** as five-calls addendum #10: every Path-B leg carries an explicit cut time, KR legs at the Seoul 15:30 KST onshore close (매매기준율), US-cut legs stamped as such, no cross-cut comparison without both stamps, unstampable legs DATA-GAPPED rather than substituted. The 07-24 "won fell 1.09%" reading is retracted as a session-basis claim.
