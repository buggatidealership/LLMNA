# 2026-07-27 MON — NVIDIA×SK partnership claim (Jensen/Ed Ludlow Bloomberg): entity disambiguation + tape

**WORKFLOW: INGEST (Critical Rule #16 verification fired immediately, 2 parallel agents). Escorted-instrument discipline. NO POSITION ACTION (user-gated, Rule #8).**

**Operator input (2026-07-27):** watched a Jensen Huang / Ed Ludlow (Bloomberg) video in which Huang discussed a partnership between NVIDIA and **"SK Group"** — operator unsure of the exact entity, thought possibly a Korean telecom. Observed the shares "going up the last few days," not back to an all-time high set around **1999–2001**. Asked for an **unbiased** check on the partnership and whether it merits portfolio consideration.

⚠️ **Framing hazard named up front: "SK Group" is a chaebol, not a listed instrument.** SK Inc, SK Square, SK Telecom and SK Hynix are separate listings with materially different exposure. Resolving an ambiguous group name to a specific ticker by plausibility is the same error class as the 2026-07-24 WTI/Brent conflation booked this morning (L43): right story, wrong instrument. The entity is therefore treated as an open question and settled on evidence, not assumption.

---

## 1. DETERMINISTIC TAPE (orchestrator-fetched, EODHD, no agent, no recall)

Closes, and daily moves **computed** from adjacent closes. KOSPI reference from the same source (`KS11.INDX`), per this morning's KR-open artifact.

| Date | KOSPI | **SK Telecom** 017670 | rel. | SK Square 402340 | SK Inc 034730 |
|---|---|---|---|---|---|
| 2026-07-22 | +0.74% | **+10.58%** | **+9.8pp** | −1.84% | +4.70% |
| 2026-07-23 | +4.40% | **+5.74%** | +1.3pp | −0.73% | +4.97% |
| 2026-07-24 | **−5.72%** | **+0.50%** | **+6.2pp** | **−9.17%** | −3.82% |
| 2026-07-27 (live) | +1.22% | **−2.10%** | **−3.3pp** | −1.17% | −1.11% |

**Levels:** SK Telecom ₩85,100 (07-21) → **₩100,000 (07-24 close)** → ₩97,900 (07-27). ADR **SKM**: $31.95 (07-21) → **$35.67 (07-24)**, i.e. +6.23% / +3.71% / +1.34% across 07-22/23/24 — the move confirms in USD, so it is not an FX artifact.

**Computed:** over 07-21 → 07-24, **SK Telecom +17.51% vs KOSPI −0.85% = +18.4pp relative**.

### What the tape establishes

**(a) The operator's "going up" observation is TRUE — and specific to SK TELECOM.** On the same three sessions SK Square fell and SK Inc round-tripped. **This is not a group-wide move.**

**(b) The Friday signature is the strongest datum here.** On 2026-07-24 the KOSPI fell 5.72% — the "검은 금요일" rout in which foreigners net-sold ~₩3.28조 and SK Hynix fell 8.34% — and **SK Telecom closed UP 0.50%**, +6.2pp relative. A name holding green through a broad rout of that size is an **idiosyncratic-event signature**: something name-specific was being priced, independent of the market.

**(c) ⚠️ But it is already fading.** Today SK Telecom is **−2.10% while the KOSPI is +1.22%** — **−3.3pp relative**, the first negative-relative session of the sequence, and it comes on the bounce. A durable re-rating on a major new partnership would not normally underperform a recovering tape the very next session. Two readings, neither confirmed: (i) event-driven pop beginning to fade / profit-taking; (ii) ordinary consolidation after +17.5% in three sessions. **Note also the 07-24 close of exactly ₩100,000** — a round number that may be acting as resistance. 🟡 DIRECTIONAL.

**(d) Group-level test FAILS.** If this were an *SK Group*–level deal, the holdco (SK Inc) should carry it. SK Inc rose 07-22/23 with the tape and then fell 3.82% on Friday — it did **not** hold green when SK Telecom did. **The evidence points to an SK TELECOM–specific catalyst, not a group transaction.** This directly qualifies the operator's "SK Group" framing. 🟡 DIRECTIONAL.

**Entity verdict (my model, on the tape alone, pending the press leg): SK TELECOM (017670.KS / ADR SKM), high confidence.** Corroborated independently by the operator's 1999–2001 ATH detail — SK Telecom was a dot-com-era Korean mega-cap; **SK Square cannot match that clue, having been spun off only in 2021.**

---

## 2. ⚠️ THE PRIOR THE OPERATOR DOES NOT HAVE IN VIEW — an NVIDIA relationship is ALREADY ON FILE

This is the single most important context item, and it reframes the question.

Per `signals/cross-source-log/2026-07-24-fri-skm-deep-dive-3agent.md` (3-agent deep dive run **three days ago**, at the operator's own request):

- **SK Telecom already operates the "Haein" cluster — >1,000× NVIDIA B200**, the largest domestic GPUaaS in Korea, on SKT's own Petasus AI Cloud virtualisation, with a Japan PoC as first international market (T1/T2).
- SKM has been **watchlist P3 since 2026-06-17** ("Korean sovereign AI cornerstone").
- The 07-24 dive verdict: **REMAIN WATCHLIST P3 — do NOT promote; entry-frame RESET.**

**So the question is NOT "is there an NVIDIA–SKT relationship" — there demonstrably is. The question is whether Jensen's remarks describe something NEW and materially larger than the Haein arrangement already booked, or are commentary on / a re-report of the existing one.** That is a B40 temporal-freshness question, and it is the load-bearing discriminator for whether anything changes. The verification leg was tasked with exactly this distinction.

### The 07-24 dive's own conclusion, which any new evidence must clear

> *"SKM is the **right listed vehicle for exactly one thesis** — Korea sovereign-AI infrastructure execution — and the **wrong vehicle for the desk's core thesis** (AI-memory/supply-chain: that's SK Square/direct memory names, and the book already holds SKHY)."*

The dive judged the AI leg **largely priced** (+80% YTD at the time) and the dividend leg **half-refuted**, scoring **LOW anti-fragility for this book**: wins only in sovereign-execution scenarios, loses in AI-capex-compression *and* telecom-regulatory scenarios.

### Registered re-look triggers from that dive (pre-registered, not invented now)

1. **Aug-2026 down-select result** — survive = narrative intact; cut = KILL the candidate.
2. **Q2 print 2026-08-11** — AIDC run-rate + any AIX/model-licensing breakout line (the platform-vs-landlord tell).
3. Breach-litigation resolution (fine appeal + class actions) bounding a ~₩2.3T-ceiling liability tail.
4. **Any AIX revenue acceleration >30%/yr** — would genuinely challenge the landlord frame.

**A new NVIDIA partnership is NOT among the pre-registered triggers.** Whether it should be added is a live question — but adding a trigger *after* seeing a price move, to justify re-opening a candidate that was closed three days ago, is exactly the shape of post-hoc rationalisation the pre-registration discipline exists to prevent. Flagged explicitly so the decision is made consciously rather than by drift.

---

## 3. PORTFOLIO-OVERLAP CHECK (Rule #10 relevance, before any sizing conversation)

The book already holds **SKHY (37 ADS, SK Hynix ADR)**. SK Hynix is an SK Group affiliate. If the operator's interest is "get exposure to SK Group's AI position," **that exposure already exists in the book via the memory leg** — the 07-24 dive said so directly ("the book already holds SKHY"). Adding SK Telecom would not be adding SK-Group exposure; it would be adding a *different* thesis — Korean sovereign-AI infrastructure execution — which the dive assessed and declined three days ago.

**NO POSITION ACTION. No falsifier fired on any held name.** Wed **2026-07-29 SK Hynix Q2** remains the sole adjudicator of the conditional €3-5k SKHY add; the KR leveraged-ETF measure lands **2026-07-31**.

---

## 4. VERIFICATION LEG 1 RETURNED — the partnership is REAL, and three qualifiers matter more than the headline

| Claim | Verdict | Evidence |
|---|---|---|
| Huang/Ed Ludlow Bloomberg interview exists, discusses an SK partnership | ✅ **VERIFIED** | [Bloomberg video, 2026-07-25](https://www.bloomberg.com/news/videos/2026-07-25/nvidia-s-jensen-huang-on-south-korea-s-golden-age-sk-hynix-group-partnership) — T1 outlet |
| NVIDIA × SK "$500B+" partnership announced | ✅ **VERIFIED** | Stated 2026-07-24 in San Francisco after Huang met Korean President Lee Jae-myung; [NVIDIA newsroom](https://nvidianews.nvidia.com/news/sk-group-and-nvidia-expand-strategic-partnership-across-ai-factories-and-next-generation-memory) PR 2026-07-25 + [서울경제](https://www.sedaily.com/article/20071800), [뉴시스](https://www.newsis.com/view/NISX20260725_0003722948) |
| **It is a signed LOI — NON-BINDING** | ✅ **VERIFIED** | 서울경제 headline uses the term explicitly: *"SK, 엔비디아와 5000억불 AI인프라 구축 **LOI**"* (의향서) |
| Counterparty = **SK Telecom (AI factories) + SK Hynix (HBM)** — two entities, not one | ✅ **VERIFIED** | [CNBC](https://www.cnbc.com/2026/07/25/nvidia-locks-down-memory-from-sk-hynix-as-part-of-500-billion-ai-deal.html), SK hynix newsroom, Korean 이투데이/서울경제 both name SK텔레콤 + SK하이닉스 |
| "Wholly new deal" | ❌ **REFUTED** | Escalation/formalisation of a [2026-06-08 NVIDIA–SK Telecom announcement](https://nvidianews.nvidia.com/news/sk-telecom-ai-infrastructure) |
| SKT's headline 2GW figure | ⚠️ **COMPANY SELF-CORRECTED** | [SK Telecom Form 6-K, SEC EDGAR](https://www.sec.gov/Archives/edgar/data/0001015650/000119312526260621/d109398d6k.htm) — T1 regulatory: 2GW is a **long-term ceiling**, not the 2027 facility's size |
| Verbatim Huang quote | **DATA-GAPPED** | Bloomberg paywall; only paraphrases retrieved. DART filing for the LOI also not located — SEC 6-K is the closest regulatory-grade document |

**Three qualifiers that do the work:**
1. **Non-binding LOI.** The house already discounts LOI-grade commitments — the 07-22 WSJ steelman turned on exactly this ("the marquee 900k wafers/mo Stargate number is a non-binding LOI/MOU"). Same treatment applies here; consistency demands it.
2. **$500B is a rolled-up figure** spanning at least two separate workstreams across two entities, not a single contract value.
3. **The company has already walked back its own headline number once**, in a regulatory filing.

## 5. 🎯 THE TIMING — the entire move was PRE-announcement, and the news session is NEGATIVE

**Computed sequence:**
- KRX 07-24 session closed 15:30 KST = **06:30 UTC**. Huang spoke 2026-07-24 in San Francisco — earliest plausible ~16:00 UTC. **The Korean market closed ~9.5 hours BEFORE the statement.** PR dated 07-25 (Saturday); 07-25/26 KRX closed.
- ⇒ **The first KRX session able to price this announcement is TODAY, Monday 2026-07-27.**

| Window | SK Telecom | KOSPI | Relative |
|---|---|---|---|
| **PRE-announcement** 07-21 → 07-24 | **+17.51%** | −0.85% | **+18.4pp** |
| **POST-announcement** 07-24 → 07-27 (live) | **−2.10%** | +1.22% | **−3.3pp** |

**The whole +17.5% run happened before the news was public.** Friday's +0.50% against a −5.72% rout — the idiosyncratic signature flagged in §1(b) — was **anticipation, not reaction**: the Korean President's US trip and NVIDIA meeting were scheduled and public.

**And the first session that can price the actual announcement is down, and down relative to a bouncing market.** That is a **buy-the-rumour-sell-the-fact** signature. 🟡 DIRECTIONAL (one partial session; the full-day close is the real read).

**This is the same reaction-function flip the desk has measured four times in six days** — IBM cut guidance and rose; NOW, GOOGL and TXN each beat/raised and fell; Disco posted a record H1 and fell 12.27% the next session (`2026-07-25-fri-eod-reaction-leg-grade-legb-kr-etf-crackdown.md`, Principle #48/#49). **A fifth instance, on a different continent, on a partnership rather than an earnings print** — which widens the pattern beyond earnings reactions. Registered as a candidate extension of the reflexivity read, not yet promoted: one partial session is not a close, and an alternative reading (ordinary consolidation after +17.5% in three sessions) is not excluded.

## 6. WHAT THIS ACTUALLY MEANS FOR THIS BOOK — the SK Hynix leg, not the SK Telecom leg

The operator asked about adding SK Telecom. **The materially more important fact is the other counterparty.**

**NVIDIA has signed an LOI locking HBM3E/HBM4 supply and co-development with SK Hynix — and the book holds SKHY (37 ADS).** This lands **two days before the 2026-07-29 SK Hynix Q2 print**, which is the pre-registered *sole adjudicator* of the conditional €3-5k SKHY add (demand ✅ confirmed / reaction-function ⚠️ flipping, per five-calls addendum #8).

**Directional read on the held position: mildly supportive, and explicitly NOT a falsifier event.** It is demand-side corroboration of the HBM thesis from the single most important customer. But it is **LOI-grade**, so it must not be weighted as a contract; and it arrives into a tape that has just punished four consecutive good-news prints. **It does not resolve the add gate — the Jul-29 print still does, and specifically the LTA prepayment/duration disclosure and the GP-bridge sign test.**

**On SK Telecom as an addition:** the 07-24 dive's verdict survives this news intact. The dive judged the AI leg *already priced*; this announcement is an escalation of a relationship the dive already counted (the >1,000× B200 Haein cluster), it is non-binding, the company has walked back its own headline figure, and the market's first chance to price it produced a negative relative session. **None of the four pre-registered re-look triggers has fired.** 🟡

**NO POSITION ACTION (user-gated, Rule #8). No falsifier fired on any held name.**
