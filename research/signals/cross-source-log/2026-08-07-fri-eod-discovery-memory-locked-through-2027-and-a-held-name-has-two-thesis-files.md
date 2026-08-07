# 2026-08-07 FRI EOD — DISCOVERY: memory is pre-sold through 2027, SK Hynix commits $38B — and the held name it lands on has TWO thesis files

**Run:** EOD CONDITIONAL SYNTHESIS Routine, FULL PATH. One Leg-B unanchored discovery agent (company- and segment-agnostic, breadth-at-search/filter-at-digest).
**Segment classification (Rule #6 / Principle #29):** memory-and-storage (items 1–2), networking/advanced-packaging (3–4), infrastructure-financing + power-and-cooling (5–6).
**Status:** 🟢 **BOTH VERIFIERS RETURNED — see §7 (item 5) and §8 (item 2). In BOTH cases the load-bearing leg broke, and in BOTH cases the commissioning prompt had pre-registered that leg as the one to attack.** Cascade still deferred per §4.

---

## TL;DR

Memory output for all of 2027 is reportedly pre-allocated with **Apple unable to secure a fourth DRAM supplier**; SK Hynix approved **~$38B for two new fabs today**. But the discovery's most useful output is not a market signal — **the L60 prior-read check found that a held position has two live thesis files, and the one the corpus mostly points at is not the one with the recent work.**

---

## 1. THE DISCOVERY ITEMS

| # | Mechanism | Tier | Status |
|---|---|---|---|
| 1 | **2027 DRAM/HBM output fully pre-allocated** — Samsung/SKH/Micron finished 2027 allocation talks early; **Apple reportedly failed to line up a 4th DRAM supplier** | T2/T3 (Digitimes-lineage) | plausible, not verified |
| 2 | **SK Hynix board approves KRW 54.3T (~$38B)** — Yongin "Y2" DRAM 35.2T + Cheongju "M17" NAND 19.1T; Yongin cluster timeline reportedly pulled **2045 → 2033** | 🟢 **CONFIRMED-T1 on the money; 🔴 the "2045→2033" is a 6-WEEK-OLD RECYCLE** — see §8 |
| 3 | **FCC drafting ban on Chinese optical transceivers** — hits Zhongji Innolight (27% global share, 62% of Q1-26 revenue from US); Coherent/AOI/Lumentum rallied same day | T1/T2 Reuters-lineage | directional |
| 4 | **Japan tightens advanced-packaging tool licensing to China** | 🔴 **T3, Chinese financial press ONLY** | **NOT CONFIRMED — see §3** |
| 5 | **AI data-centre CMBS spreads widening**; 2 of last 3 deals repriced wider; "hyperscaler bond coverage ratios ~5× (Feb) → below 2× (Jul)" | 🟢 spreads CONFIRMED; 🔴 **the "5×→2×" is a METRIC CONFLATION** — see §7 |
| 6 | **AI's spiky power draw physically degrading DC equipment** — some storage systems replaced after weeks | T2 Bloomberg, single-source | registered, not actioned |

**The agent's own strongest-disconfirming pick was [5]**, and it picked correctly: it is market-priced rather than vendor-reported, and its framing ("supply of debt is the risk, not defaults") makes it a cost-of-capital signal rather than a distress signal. That distinction is exactly the kind that gets flattened in transmission, which is why it went to a verifier.

---

## 2. 🟢 THE L60 CHECK EARNED ITS KEEP ON ITS FIRST SCHEDULED RUN

L60 was codified this morning: *before an external attribution enters an artifact, grep for our own prior read.* Run here as a matter of course, and it changed two readings:

**(a) The SK Hynix CEO "worst year in the industry's history" quote is ALREADY OURS.** The agent correctly flagged it as **not fresh (2026-07-10)** — and the corpus goes further: it was ingested **2026-07-12**, routed, and put through a **substance-validation run** (`2026-07-12-sun-eve-kwak-substance-validation-blockF.md`), then cascaded into `companies/SKHY/thesis.md`. **Item [1]'s "corroborating" quote is our own month-old datum arriving back as if it were support.** Treating it as independent corroboration would have double-counted a single source — the precise shape of the error the whole exercise exists to stop.

**(b) The data-centre debt theme is not new either.** `2026-07-23-thu-ai-brief-intake-1p65T-debt-...md` already carries a read on the financing stack. **Item [5] is a continuation with a fresh market-priced datum, not a discovery.** Registered as such.

**⇒ Two of six items were partially already-held.** Neither was wrong; both would have been over-weighted as new. **The check cost one grep.**

---

## 3. 🔴 ITEM [4] IS NOT ENTERING THE CORPUS

Japan/advanced-packaging licensing is sourced **only** to Chinese financial press (Eastmoney, 163.com, both 2026-08-03). The agent tried and failed to corroborate via METI, Reuters or Nikkei and **flagged it itself as the translation/attribution-garble pattern**.

**That is the same shape as this morning's refuted Korean "next-gen AI chip supply delay"** — single-language press, no primary source, a mechanism that would be very convenient if true. **Two instances in one day.** Logged here, cascaded nowhere, and if it is real a primary source will appear.

---

## 4. 🔴 THE STRUCTURAL FINDING — A HELD POSITION HAS TWO LIVE THESIS FILES

Surfaced only because the L60 check made me look up where SK Hynix knowledge actually lives before cascading into it.

| | `companies/HYNIX/` | `companies/SKHY/` |
|---|---|---|
| thesis.md size | **334 KB** | 89 KB |
| header "Last updated" | 2026-06-12 | 2026-07-11 |
| most recent dated entry | **2026-07-28** | 2026-07-27 |
| inbound references from the rest of the corpus | **183** | **22** |
| `INDEX.md` points to | ✅ this one | — |
| Position implication carried | **`HOLD (SKHY 37 ADS)`** | **`HOLD (37 ADS)`** |

🔴 **Both files carry position implications for the SAME live position — 37 ADS.** This is not a held/exited split and not two instruments: `HYNIX/thesis.md` line 21 states the SKHY position explicitly. **Both were written to within one day of each other in late July. Neither is canonical.**

**Why this matters more than it looks:** a Rule #10 cascade lands in whichever folder the session happens to pick. **The corpus points 183:22 at `HYNIX/`, while `holdings.md` names the position `SKHY`** — so the retrieval gradient and the position record point at different files. Work done in one is invisible from the other.

**Classification: L53 (retrieval-drawer error) at the FOLDER level, on a live position.** L53 governs a name filed under the wrong theme being functionally invisible; this is a name filed under two folders, where the more-referenced one is not the one named in holdings.

⚠️ **I first read this as "duplicate folders = defect," then checked whether it was a deliberate GDR-vs-ADS distinction — it is not, and the check is what established that.** Recording the sequence because the wrong read was the intuitive one.

**NOT resolved tonight.** Merging or retiring a 334 KB thesis file touches live position records and is **Rule #19 MEDIUM-to-HIGH** — it is booked for the operator, not executed at EOD by the party that found it.

**Blind-check (#51):** *distinguishes "one canonical thesis per position" from "two files that each look complete" · reads on the count of `companies/*/thesis.md` files carrying a Position-implication line for the same holdings row · **goes blind if** a folder stops being written to but keeps its inbound references, which makes it look retired while still being the retrieval target.*

---

## 5. WHAT THE AGENT LOOKED FOR AND DID NOT FIND (recorded — a negative result is information)

- No fresh (≤36h) EU capital/regulatory item — the 7-gigafactory tender is **8 days stale**, excluded.
- No fresh China-side regulatory response beyond stock reaction — MOFCOM draft consultation is FT-sourced ~07-21/22, **excluded as stale-recycle**.
- **No genuine demand-destruction or efficiency-compression signal in the window.** Worth stating plainly: the U8/B47 falsifier side produced nothing today.
- No FERC compliance filing yet against the ~2026-08-17 deadline from the June 18 order — **flagged for a dedicated sweep on/after 08-17.**

---

## 6. POSITION IMPLICATION

**Position implication: 🔴 NO ACTION** — no size change on any name — **the two items that could bear on a held position are both still under verification, one of the six is single-language and refused entry, and two were partially already in the corpus.** Weights held **H1 60 / H2 11 / H3 29**. Any sizing decision remains operator-gated regardless.

**Rule #10 cascade: DEFERRED, deliberately.** The correct target file for SK Hynix is ambiguous (§4), and cascading into the wrong one would be worse than not cascading — it would create a record that looks complete and is not. **Cascade executes once the verifiers return AND the folder question is resolved by the operator.**

**Signal density (Rule #14):** items 1–2 are same-segment (memory-and-storage) same-direction as the 2026-07-12 Kwak cluster — but per §2(a) that is the *same source lineage*, not a third independent signal. **No TC promotion. N is not incremented on a datum we already hold.**

---

## 7. 🔴 VERIFIER RETURN — ITEM [5]: THE HEADLINE NUMBER IS A METRIC CONFLATION, AND THE STORY IS TWO STORIES

**Verdicts, per claim, not per item:**

| claim | verdict |
|---|---|
| Data-centre CMBS risk premiums widened over 12 months | 🟢 **CONFIRMED-FRESH** — Bloomberg 2026-08-06 verbatim, independently corroborated by IFR and GlobalCapital (T2) |
| Two of last three such deals repriced wider | 🟢 **CONFIRMED-FRESH** — CyrusOne (KKR-backed) and QTS (Blackstone-backed) named |
| **"Hyperscaler bond coverage ratios ~5× (Feb) → below 2× (Jul)"** | 🔴 **PARTIAL — number real, attribution and framing WRONG** |
| Bloomberg framing "supply is the risk, not defaults" | ⚠️ **UNVERIFIED** — article body paywalled; directionally consistent with Slok and Morgan Stanley but **not attributable to Bloomberg** |

### 7.1 The metric was the whole question, and the pre-registered suspicion was correct

**It is BID-TO-COVER at issuance — how many dollars of orders per dollar of bonds sold. It is NOT interest coverage.** Apollo's own footnote settles it: *"A cover ratio of 3x… means the deal received orders equal to three times the amount being sold."*

**Actual hyperscaler interest coverage, for scale:** Meta **59.6× LTM**, Microsoft **~52.7× TTM**, Amazon **~61.5×**. **Read as interest coverage, the claim would be wrong by roughly 30×** — and would have said the largest balance sheets on earth were approaching distress.

🔴 **This is the third "correct number, wrong basis" of the day** — after the KR-wake open-vs-session error and the "SOX crash" that was −1.40%. **L58 is now at 8 specimens in 6 days.** The commissioning prompt named this leg as *"the one to attack"* and asked for the metric to be identified precisely. **Pre-registering the suspicion is what converted a plausible bear datum into a caught error.**

### 7.2 Source attribution was also wrong, and the number is stale

Sourced to **Apollo / Torsten Slok, 2026-07-15** — **not** Bloomberg 2026-08-06. By the 6th it was **three weeks old**. 🔴 **Textbook B40 stale-recycle, second instance today** (after the Japan packaging item in §3).

### 7.3 🔴 CONTRADICTED THE SAME DAY, BY THE SAME OUTLET

**Alphabet priced $25B on 2026-08-06 with ~$115B of orders = 4.6× cover**, its 40-year tranche tightening from ~155bp IPT to **130bp**. Bloomberg ran the bearish CMBS piece and this on the **same date**. **Any claim that cover ratios are "below 2×" as a CURRENT state is contradicted by the same publication on the same day.**

Reconstructed series (bid-to-cover): Alphabet 02-10 **>5.0×** · Amazon 03-10 **~3.4×** · Amazon 07-07 peak 2.5× → **final 1.64×** · Alphabet 08-06 **4.6×**.
⚠️ **The July "below 2×" is a FINAL book after banks trimmed spreads** (orders fell $62B→$41B as pricing tightened); peak was 2.5×. **Whether the series uses peak or final books consistently could not be verified — so the endpoint is a BAND (1.6–2.5×), not a point.** That is a basis question inside the corrected number.

### 7.4 The counter-evidence is substantial and is recorded, not buried

QTS — **the same issuer cited as evidence of stress** — moved its June ABS from 195bp guidance to **145bp**, tranches >3× subscribed. Data-centre ABS spreads hit **four-year tights in Feb 2026**, so the 12-month window in claim 1 **starts near a spread low, which mechanically flatters "risk premiums have broadly risen."** Green Street: top-rated data-centre ABS tightened **60bp in two weeks** (2026-05-01). Morgan Stanley (08-06) says July ABS pricing was "largely stable despite weakness in corporate credit" and calls compute *structurally undersupplied over the medium term*. **And no reported data-centre CMBS/ABS delinquency, default or loss anywhere in 2026.**

### 7.5 What survives — the defensible version

🟡 **Real but narrow: the PRICE of new AI-linked debt is repricing at the margin, concentrated in repeat issuance and long tenors. Nothing has impaired.** The stress is in *execution*, not *credit*.

**Defensible restatement, replacing the version in §1:** *"Bid-to-cover on hyperscaler IG issuance fell from ~5× (Feb 2026) to ~1.6–2.5× on Amazon's 07-07 deal (Apollo/Slok, 07-15), before recovering to 4.6× on Alphabet's 08-06 deal."*

🔴 **DO NOT let this cascade into solvency.** Interest coverage is 50–60× and Moody's — in the same late-July note warning on AI capex — still calls these balance sheets *"among the strongest in the world."*

### 7.6 🔴 A NEW FAILURE MODE, AT THE AGENT LAYER

**The two halves were never one story.** Claims 1–2 are **data-centre CMBS**; claim 3 is **hyperscaler IG corporate bonds** — *different asset class, three weeks apart, different source*. **Neither original source made the connection. The bundling happened in the digest.**

That is not B40 (stale source) and not L58 (wrong basis) — it is **a synthesis layer inventing a relationship between two true facts.** The Bloomberg piece and the Apollo chart are each defensible; the compound claim is not, and it is *more* persuasive than either part because it appears to have two legs.

**Registered as a CANDIDATE agent-layer failure mode: DIGEST-FUSION — a summarising agent joins two separately-true items into one claim neither source supports.** N=1. Its detector is cheap: **when a claim has two halves, check whether one source carries both.** Not codified as a bias yet; N=2 required.

### 7.7 Position implication — UNCHANGED

**Position implication: 🔴 NO ACTION** — no size change on any name — **the disconfirming item survives only in its narrow form (price of new debt, not ability to service it), it was contradicted by a 4.6× print the same day, and the version that would have mattered was a metric error.** Weights held **H1 60 / H2 11 / H3 29**. **H2 is NOT re-weighted on this**: a financing-cost signal that reverses within a day is not demand destruction.

---

## 8. 🔴 VERIFIER RETURN — ITEM [2]: THE MONEY IS REAL AND T1. THE HEADLINE IS SIX WEEKS OLD.

| claim | verdict |
|---|---|
| Board approved **KRW 54.3T** for Yongin Y2 + Cheongju M17, 2026-08-07 | 🟢 **CONFIRMED-T1** |
| Construction starts 2027; first cleanrooms 2028–2029 | 🟢 **CONFIRMED-T1** |
| **"Yongin cluster pulled 2045 → 2033, a 12-year acceleration"** | 🔴 **CONFIRMED-STALE-RECYCLE — real, but announced 2026-06-29** |

### 8.1 The money reconciles exactly

**35조 2,246억 (Y2, DRAM/HBM) + 19조 1,000억 (M17, NAND) = 54조 3,246억.** Computed, not assumed — no discrepancy. DART template fields quoted verbatim across multiple Korean outlets: **29.19% and 15.83% of consolidated equity**, disbursement to **2031-10-31** and **2031-04-30**.

**Dates, and the distinction that matters:** groundbreaking **Jul 2027 (Y2) / Feb 2027 (M17)**; **first** cleanroom **Jun 2029 (Y2) / Dec 2028 (M17)**. 🔴 **No mass-production or wafer-out date was disclosed for either fab.** Anyone deriving "SK Hynix output up in 2029" from this is inferring. **NOT ESTABLISHED — the gap stays open.**

🔴 **AND 54.3T IS THE SHELL, NOT THE FAB.** Seoul Economic Daily (08-07) puts total investment including equipment at **">150 trillion won"** — modelling 54.3T as the all-in cost understates by roughly **3×**. ⚠️ **Single-source; flagged UNVERIFIED-SINGLE-SOURCE and not used as a figure.** It is recorded because the *direction* of the error is what matters: the headline number is the smaller one.

### 8.2 The load-bearing claim is a de-dating artifact — and the transmission path is mechanical

SK hynix's own Korean release, 2026-08-07:

> 「당초 2045년으로 예정했던 용인 반도체 클러스터 완공 시점을 12년 앞당겨 2033년까지 4기 팹 건설을 마친다는 목표를 **세운 바 있다**.」

**`-ㄴ 바 있다` is Korean's explicit retrospective construction — "has previously done."** Not 세웠다 (set) and not 세운다 (sets). The company's own English release matches: *"**previously set** a goal."* **Origin: the SK hynix newsroom explainer of 2026-06-29**, announced at a government event alongside the 1,100조 mega-project plan.

🟢 **THE TRANSMISSION FAILURE IS SPECIFIC AND CHECKABLE: the retrospective marker survived in the Korean wires and was DROPPED in the English and aggregator versions.** Korea Herald renders it "has brought forward its target… to 2033" with no temporal marker; ZDNet Korea's Korean coverage of the same board resolution **doesn't mention 2045/2033 at all.** That is the exact path by which a June announcement arrived in tonight's digest as August news.

**⇒ Any thesis increment dated 2026-08-07 on the acceleration must be re-dated to 06-29 or dropped.**

### 8.3 What is genuinely new tonight, stated separately

🟢 **NEW:** the board resolution itself (a legally-operative act) · exact KRW amounts and equity ratios · the named fabs Y2/M17 · groundbreaking and first-cleanroom dates · floor areas · **M17 as a dedicated large-scale NAND fab — genuine product-mix information** · a quarterly dividend of KRW 375/share plus a further shareholder-return package flagged for September.
🔴 **NOT NEW (all 2026-06-29):** 2045→2033 · Yongin 600조 · Cheongju 100조 · the 1,100조 aggregate · the four-fab structure.

**The clean summary: 08-07 is the first concrete tranche of a 06-29 announcement. The money and the dates are new. The strategy and the acceleration are not.**

### 8.4 The falsification pass returned substance — and it is not about SK Hynix

No evidence contradicts the resolution or the figures. The evidence against runs on **feasibility**, and it lands on a third party:

🔴 **The Yongin cluster needs 6 GW. 2.8 GW is secured. The remaining 3.2 GW depends on transmission and substation work for which detailed implementation plans do not yet exist** (구체적 이행 방안 미수립). The 400조 southwest cluster competes for **the same grid and water**, and the enabling special act is not assured (한국일보, 06-29, on the day of the acceleration announcement: 「특별법은 글쎄...」).

**⇒ The 2033 target is a jointly-announced government-industry target contingent on Korean state infrastructure delivery — NOT a unilateral SK Hynix capital-allocation decision.** Treating it as company-controlled is the framing error underneath the freshness error.

🟢 **A near-term falsifiable checkpoint exists and is cheap:** **Y1's first cleanroom, February 2027.** That validates or breaks the acceleration story six years before 2033 does.

⚠️ **Market context, recorded without adjectives per B45:** SK Hynix fell ~**41.5% in July 2026**, then reversed violently into early August. **Announcing 54.3T of new supply into an active oversupply debate is itself part of the bear case**, and the disclosure's own boilerplate ("실제 투자금액은… 변경될 수 있다") plus management's "capacity expansion based on confirmed demand, executed flexibly" mean **the 54.3T is not irrevocable.** That cuts both ways.

### 8.5 🟢 TWO FOR TWO ON PRE-REGISTRATION — THE METHOD FINDING OF THE NIGHT

Both commissioning prompts named, in advance, the single leg most likely to be wrong:
- Item [5]: *"Claim 3 is the one to attack… identify the metric precisely."* → **it was a metric conflation.**
- Item [2]: *"This is the claim I would most likely be wrong about, and it is the one carrying the most analytical weight."* → **it was a six-week-old recycle.**

**In both cases the surrounding facts were solid and the headline was the broken part.** A verifier pointed at everything equally would likely have confirmed the money, confirmed the spreads, and passed the headline through — because the headline is the part that *sounds* like the finding.

**Registered as a method upgrade: name the suspect leg in the commissioning prompt, not just the claim set.** N=2, same night, independent domains.

🔴 **B40 tally for 2026-08-07: FOUR stale-recycle or de-dating instances in one day** — the refuted Korean supply-delay attribution (morning), the Japan packaging item (§3), the Apollo cover ratio (§7.2), and the 2045→2033 (§8.2). **That is not four coincidences; it is what the aggregation layer does, and today is the first day the harness caught all four before any of them cascaded.**

### 8.6 Position implication — UNCHANGED, and now for a stated reason

**Position implication: 🔴 NO ACTION** — no size change on any name — **the capex is real, T1 and directionally supportive of the existing binding-constraint read, but it is the execution of a plan already in the corpus since June; the one genuinely new analytical item (M17 as a dedicated NAND fab) does not move a tier on its own; and the correct thesis file to cascade into remains ambiguous per §4.** Weights held **H1 60 / H2 11 / H3 29**.

**Ties to macro:** confirms the 2026-08-07 binding-constraint read (memory/HBM supply-gated, B45 regime) **without adding new information to it** — a supplier funding a previously-announced expansion is consistent with the constraint, not evidence of a change in it. **The genuine open question the verifier surfaced is not SK Hynix's willingness to spend but Korea's ability to deliver 3.2 GW**, which belongs in the bottleneck ledger rather than in a thesis tier.
