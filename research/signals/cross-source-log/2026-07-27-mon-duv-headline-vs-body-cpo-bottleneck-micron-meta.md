# 2026-07-27 LATE — The DUV article REFUTES ITS OWN HEADLINE (primary text in hand) + a new CPO supply-constraint map + Micron×Meta capacity paper

**WORKFLOW: INGEST. Critical Rule #16 verification fired (2 parallel agents, Korean/Chinese native-language). Escorted-instrument discipline. NO POSITION ACTION (user-gated, Rule #8).**

**Input:** 4 operator screenshots + 2 links. Screenshots give me **primary article text**, which is a tier above everything in the earlier aggregator batch — this is the actual reporting, not a summary of it.

---

## 1. 🎯 THE DUV STORY: the headline and the body say opposite things, and the body is the reporting

**Headline (screenshot 2):** *"**Exclusive** — China Starts **Mass-Producing** Homegrown DUV Chipmaking Tools, An Advance for Local Chip Industry."* Custom art credited "Mike Sullivan," consistent with the outlet attribution my verification agent reached independently (T2 — I am not asserting the masthead from styling alone).

**Body of the same article (screenshot 1), verbatim:**

> *"**Much still has to be done before the Chinese-made equipment is deemed a success.** Moving the Chinese DUV machines onto mass-production lines could take **many months or longer** as chipmakers test their accuracy, reliability and compatibility with other equipment… which **still trail ASML's products in performance and build quality**, the two people said."*
>
> *"The Chinese DUV uses mostly domestic components, though **some key parts come from Japan**… **Delays from local suppliers have held back production this year**, they added."*
>
> *"**ASML therefore faces little immediate threat.** But rising domestic output could gradually erode its market position in the country, particularly if tighter Western restrictions accelerate Chinese chipmakers' shift to local equipment."*

### 1.1 The ambiguity that does all the work — "mass production" of WHAT?

**The headline means the TOOLS are being manufactured. The body says the tools are NOT YET on mass-production LINES** — and getting there "could take many months or longer," pending accuracy, reliability and compatibility qualification.

Those are two different claims separated by a full qualification cycle:

| Reading | Claim | Status per the body |
|---|---|---|
| **"Mass-producing the tools"** | Yuliangsheng is manufacturing DUV units at volume | ⚠️ ~5 units in 2026 against ASML's ~130 immersion/yr — pilot scale at best, and **"delays from local suppliers have held back production this year"** |
| **"Tools in mass production"** | Chinese fabs are running production wafers on them | ❌ **Explicitly NOT yet** — "many months or longer" |

**This is the same defect family the desk has booked four times this week (L42/L43/L44): a term deployed without its basis named.** "Mass production" without specifying *of the tool* versus *with the tool* is the lithography equivalent of a price without its settle/spot basis. My verification agent independently judged "mass production" overstated and preferred TechPowerUp's *"Begins **Limited** Production"* framing — **the primary text now confirms that judgment from the source's own reporting.**

### 1.2 ⚠️ The article's own conclusion is "ASML faces little immediate threat" — and ASML fell 6-8%

**The market traded the headline; the body says the opposite.** This is not a hindsight observation — the disconfirming sentence is *in the same article*, four paragraphs down, sourced to the same two people.

**Three readings held in parallel (my model, weights mine):**
- **H1 (P~55%) — Headline-driven de-rating, body under-read.** The move prices the *category* announcement, not the reported substance. Consistent with the body's own "little immediate threat."
- **H2 (P~30%) — Correct duration re-rating.** The market is not pricing 5 tools; it is repricing ASML's China terminal share on the *direction*, which the body explicitly endorses ("could gradually erode its market position").
- **H3 (P~15%) — Coincident cause.** The move belongs mostly to the same session's broad rotation out of AI infrastructure (Intel −7.9% on a beat, AMD −7.3%, Micron −5%), with the DUV story as narrative attachment.

**H1 and H2 are not exclusive** — a duration re-rating triggered by a headline can be directionally right and magnitudinally wrong. **No position implication: ASML is in the universe table but has no thesis folder in this corpus, and this desk holds nothing in lithography equipment.** Logged as a mechanism observation.

### 1.3 What this does to SKHY falsifier #3 — nothing, and it slightly *weakens* the adverse leg

Falsifier #3's capacity leg treats domestic DUV as loosening the tooling constraint that bounds CXMT. **The primary text says the tools are months from production lines, trail ASML on performance and build quality, still depend on Japanese parts, and were themselves delayed by local supplier problems this year.** That is a **slower** relief-valve path than the aggregator framing implied.

**Falsifier #3 remains NOT FIRED**, and the adverse leg is now dated later than it looked twelve hours ago. The tightened Tier-1 AI-qualification wording (NVIDIA/AMD, HBM-class) is untouched.

## 2. 🆕 CPO SUPPLY CONSTRAINTS — a bottleneck map for a layer this corpus tracks thinly

**Source: TrendForce, July 2026 (screenshot 3). 🟡 T2 — vendor research, qualitative; no unit counts, no dates, no capacity figures.** Reported as-is; the absence of numbers is itself the reason it cannot yet drive a call.

| Component | Primary bottleneck | Key constraint | Near-term outlook |
|---|---|---|---|
| **Optical Engine** | Integrates lasers, modulators, photodetectors and optical coupling — highly complex manufacturing | High yield requirements + thermal management limit pace of capacity expansion | Mass-production capacity remains limited; rapid expansion difficult |
| **SiPh** | High-precision optical coupling + advanced packaging | Tight foundry **and backend packaging** capacity | Long build-out cycles; limited near-term supply flexibility |
| **Advanced Packaging** | Close integration of switch ASIC + optical engines + high-speed electrical circuits; **TSMC's COUPE process critically enabling** | **AI chips and HPC processors compete for the SAME 2.5D/3D advanced-packaging capacity** | Packaging resources constrained; competition intensifying |

### 2.1 The line that matters, and it is a cross-link this corpus already has

**"AI chips and HPC processors compete for the same 2.5D/3D advanced packaging capacity."** CPO is not an independent supply story — **it is a second claimant on the CoWoS-class capacity the AI-accelerator thesis already depends on.** Every CPO switch built consumes advanced-packaging substrate that an accelerator would otherwise take.

**Cross-link to TC-7 (InP geopolitical bottleneck + JP rent migration, ACTIVE):** optical engines integrate **lasers** — the InP-substrate layer TC-7 already tracks. CPO scaling is a demand multiplier on exactly that constrained substrate. **This is the first datum connecting the CPO switch layer to the InP cluster in this corpus.**

### 2.2 Bypass-route read (Critical Rule #9 — mandatory on any binding-constraint claim)

The consensus answer to "CPO is packaging-constrained" is *buy the packaging supplier*. The bypass question is what integrators do when CPO capacity fails their timeline: **the fallback is pluggable optics / linear-drive (LPO) retention** — staying on the incumbent architecture longer rather than waiting for CPO allocation. That makes near-term CPO scarcity a **transition-delay** story, not a demand-destruction story, and it means the loser is the CPO-exclusive supplier, not the optics chain as a whole. Named consequence: **connector/optical-module incumbents retain volume longer than a CPO-transition timeline implies.**

**Routing decision, stated so the skip is auditable (Rule #14):** logged to `sector/bottlenecks.md` as a constraint-map row with the packaging-contention link. **NOT promoted to a triangulation cluster and NOT cascaded to per-name theses** — a qualitative vendor table with no numbers, no dates and no capacity figures does not clear the bar for a thesis change on any held name, and the corpus holds no CPO-primary position. The TC-7 cross-link is recorded as a note, not an instance count.

## 3. 🟡 MICRON × META WHITE PAPER — a demand-side capacity argument, verification in flight

Circulating via @jukan05 (X, T3 relay of a T1-vendor primary). Reported: joint **Micron × Meta** white paper running **SparkBench (DCPerf suite)** across two SKUs differing in memory capacity — **38.75× speedup at Stage 2** under standard query load where the lower-capacity SKU spills shuffle data to SSD, and **5.96×** under a 3× workload where the bottleneck shifts to re-reads. Stated conclusion: **memory capacity is the decisive performance factor for Spark**; insufficient DRAM causes order-of-magnitude slowdowns from disk I/O.

**Why I routed it rather than skipping it:** if it holds, this is a **NON-AI demand argument for DRAM capacity per server** — data-analytics workloads independently driving capacity, separate from the HBM/AI leg. That matters because the corpus's memory thesis leans heavily on AI demand; an independent commodity-DRAM demand driver is a diversification of the thesis's support, not a restatement of it.

**⚠️ Tier discipline: Micron is an interested party.** A Micron-authored white paper is T1 for *what it says* and vendor-marketing for *why it says it*. The figures are being verified against the document itself before any use. **Not cascaded pending return.**

## 4. ⬜ NOT ROUTED — `$INTC × $SKHY`

A social post (@jukan05) reading **"$INTC X $SKHY ? 👀"** with an INTC quote card ($91.67, −0.70%) and no accompanying claim. **That is speculation with zero asserted content — there is nothing to verify beyond whether any real reporting exists, which the agent carries as a secondary check.** Logged as not-routed. Noting it only because Intel fell 7.9% on a beat the same week and a genuine Intel–SK Hynix item would touch a held name.

## 5. VERIFICATION IN FLIGHT

| Agent | Scope | Why it matters |
|---|---|---|
| A ✅ **RETURNED — see §7** | **Samsung "Chinese chips" for China mobile** — WHICH chips (memory vs logic vs analog)? Is Samsung the buyer? Volume/status? + INTC-SKHY substance check | If it is CXMT **memory**, a Samsung purchase would be extraordinary and would bear on falsifier #3's Tier-1 leg. Agent instructed to weigh the strong prior that a category other than memory is more likely, and to report "the headline is broader than the substance" if that is what it finds |
| B | **asiae.co.kr 2026-07-27 SK Group ↔ SK Hynix article** (Korean primary) + **Micron×Meta white paper** figures/conclusion | A governance or capital-structure event at SK Hynix's parent, **two days before the print that is this desk's pre-registered decision gate**, is directly position-relevant | ✅ **RETURNED — see §6** |

## Position

**NO POSITION ACTION (user-gated, Rule #8). No falsifier fired.** The DUV primary text **weakens** the adverse leg of falsifier #3 relative to the aggregator framing — the relief valve is dated later, not earlier. The CPO map is a bottleneck-layer observation with no held-name exposure. The Micron paper and both Korean items are pending.

**The 2026-07-29 SK Hynix Q2 print remains the sole adjudicator of the conditional €3-5k SKHY add.**

---

# 6. ✅ AGENT B RETURNED — both items corrected the framing they were handed

## 6.1 The asiae article is a REAL-ESTATE story. All four of my candidate hypotheses were wrong.

Fetched and read in full (403 on WebFetch; retrieved with a browser user-agent, HTTP 200 — **the article itself, not a reconstruction**).

**Headline:** `[단독]SK하이닉스, 서울 한복판에 거점 세운다...강남 르메르디앙 호텔 자리에 사옥 건립 추진` — *"[Exclusive] SK Hynix to establish a base in the heart of Seoul… pushing to build an office building on the former Le Méridien Hotel site in Gangnam."* 아시아경제, 이민우, filed 2026-07-27 17:07 KST, revised 21:50. **T2 — single-outlet exclusive, explicitly anonymous sourcing** (*"27일 재계와 투자금융(IB) 업계 등에 따르면"*), no company confirmation.

**I offered the agent four candidate hypotheses — governance restructuring, NVIDIA-related, capital allocation, Q2-print-tied — and told it not to assume any. NONE is correct.** SK Inc's stake is not mentioned; SK스퀘어 is not mentioned once; there is no 지배구조 개편, no merger, no stake transfer. **If the operator's "SK group ↔ SK hynix" heading carried a hypothesis that a holdco action had landed, this article does not support it.**

**Substance:** SK Group is pursuing acquisition/development of the former Le Méridien site in Gangnam-gu for an SK Hynix office building — a change from the earlier plan to house SK Hynix's Seoul office inside 서린빌딩 (group HQ, Jongno-gu). Framing is symbolic: ~1km from Gangnam Station where Samsung's buildings cluster, on sloped ground so a new building would *"look down on Samsung Town."*

**Scale — and it settles the materiality question (computed):** the only price anchor is the **2021 whole-site purchase of ~KRW 700bn ≈ $480m** at USDKRW 1,459.57 (corpus 07-24 close) — and that figure is **stale, pre-development, and a different perimeter**. For reference from today's other work: **CXMT's IPO raise (~$8.6bn) is 17.9× the entire 2021 site price.** This is not a capital-allocation event of thesis-relevant size.

**⚠️ The one genuinely open variable, and the article says so itself:** *"SK그룹이 해당 사업에 참여하는 구체적인 방식은 향후 거래의 핵심 변수"* — **which entity pays is undetermined.** Landowner is 대신자산신탁, developer 넥스플랜, via 비120 PFV; SK could buy the land directly, buy PFV equity, or forward-purchase (선매입). **If SK Hynix itself funds a trophy Gangnam HQ ahead of a capex-heavy cycle, that reads differently to minority holders than SK Inc or a PFV holding it with SK Hynix as tenant.** *(That framing is the agent's inference and mine — it is NOT in the article. Do not price it either way.)*

**And a softer corroborating account exists:** inews24 reports SK Hynix reviewing **multiple** Gangnam candidate sites with **location and method not decided** — materially weaker than the exclusive's framing. 🟡 T2, read via search summary only, host not fetchable here.

**⚖️ Verdict: headline noise around the decision gate, not gate input. Nothing here bears on the 2026-07-29 Q2 print.**

## 6.2 The Micron×Meta paper is real — and the number that circulated is 13.7× the number the paper stands behind

**Primary PDF downloaded and read end-to-end (8pp).** *"LPDDR for General-Purpose and AI Workloads in Large-Scale Data Center Deployments."* Genuinely co-authored — 5 named Micron authors, **4 named Meta hardware-systems engineers** — but **published and controlled by Micron** (Micron branding, PDF Author metadata, doc code CCM004-1681249710-11889). No corresponding Meta engineering-blog post found.

**⚠️ FRESHNESS CATCH #4 in two days: the paper is dated 2026-07-16, not ~07-26.** PDF CreationDate 2026-07-16 14:54 UTC; revision stamp *"Rev A 07/2026"*; companion Micron blog 07-20. What circulated on 07-26 was **secondary press**, not the paper. The X relay presented a ten-day-old vendor document as current.

### The correction that matters — the experiment is not what the relay implied

| | SKU1 | SKU2 |
|---|---|---|
| Memory | **512GB/socket LPDDR5X** | **256GB/socket LPDDR5X** |
| Speed | 6400 MT/s | **8533 MT/s** |
| Rank | 4 | 2 |

**Both SKUs are LPDDR5X.** This is LPDDR-vs-LPDDR at two capacities — **not LPDDR vs conventional DRAM**, which is how a casual read frames it. And the higher-capacity SKU is the **slower** one (4-rank stacking caps signalling rate).

**⚠️ The paper's stated isolation claim is overstated.** It says the systems are *"otherwise identical… isolating memory capacity as the primary performance variable"* — but **data rate differs by 33% (computed) and rank differs.** Directionally a spill cliff dwarfs a 33% rate delta, so the finding survives; the *claim of isolation* does not.

### The figures — confirmed, and scoped

| Metric | Value | Scope |
|---|---|---|
| **38.75×** | ✅ confirmed | **Stage 2 ONLY, standard query load** — the shuffle-heavy stage where SKU2 spills to SSD |
| **5.96×** | ✅ confirmed | **Stage 1 ONLY, 3× load** — scan stage, OS page cache too small |
| **2.82× / 3.45×** | ✅ | **END-TO-END QPH**, standard / 3× load — *the paper's own Key Takeaways headline: "2x to 3x throughput improvement"* |
| **0.96×** | ✅ | Stage 1, standard load — **the smaller, faster SKU WINS this stage** |

**Reading the 38.75× as the result overstates the paper's own headline by 13.7× (computed).** This is a **capacity cliff, not a capacity gradient** — and the near-miss is the point: I quoted 38.75× in §3 above as *reported* and explicitly did **not** cascade it pending verification. **That discipline is what stopped a 13.7× scope error from entering a thesis.** Same family as L42/L43/L44 — a number without its basis, here the basis being **scope** (one stage vs end-to-end).

**Axis check (agent grepped the full text): zero occurrences of "CXL", "tier" or "tiering."** The argument is **capacity-per-socket within LPDDR5X**, and the forward pitch is explicit — Micron's 256GB SOCAMM2 enabling up to 2TB LPDDR5X per socket.

### Is it a demand-side argument or vendor marketing? Both, honestly

**For:** SparkBench is classified in the paper itself as **GPC (general-purpose compute), not AI** — so it does argue a **non-AI analytics workload independently demands more DRAM per socket**. The benchmark is Meta's own open-source **DCPerf**, which Meta uses for platform selection and procurement, with Meta engineers as named co-authors — meaningfully better than a pure vendor bench. And the effect is a genuine **discontinuity at the 256→512GB/socket boundary**, the kind of threshold that moves DRAM content per server rather than preference.

**Against:** n=2 SKUs, one workload family, headline carried by a single stage; the confound above; the Spark spill cliff is **well-known, not a discovery**, and the paper never tests whether tuning or partition sizing narrows it — so it cannot distinguish *"workloads need more DRAM"* from *"this untuned configuration needed more DRAM."* Purpose is to sell LPDDR5X and SOCAMM2.

**⚖️ Net: supporting colour for the view that non-AI datacentre workloads add to DRAM capacity demand — NOT evidence that moves a position on its own.** A vendor document containing a real measurement with hyperscaler co-authors. 🟡

## 6.3 Cost-yield

**Agent B: HIGH on task 2, MEDIUM-HIGH on task 1.** Task 1 refuted all four hypotheses I supplied rather than force-fitting one — the correct behaviour and the reason the hypotheses were offered as candidates. Task 2 corrected the date by ten days, corrected the experiment's design (LPDDR-vs-LPDDR, not LPDDR-vs-DDR5), scoped the headline figure to one stage against a 13.7× end-to-end gap, and surfaced that the paper's own isolation claim is overstated. **It also retained the primary PDF and HTML locally rather than reporting from memory.**

---

# 7. ✅ AGENT A RETURNED — the Samsung story is real, the CXMT attribution is not, and I made a bad routing call on Intel×SK Hynix

## 7.1 The Samsung item: category confirmed as MEMORY, supplier attribution INVENTED downstream

**Original: 아시아타임즈 (Asia Time)**, minor Seoul business daily, 이하영, **2026-07-27 14:15 KST**. Headline `[단독] 삼성전자의 역발상…'중국칩'으로 현지 모바일 시장 뚫는다`. The English title the operator has is an accurate translation; 단독 = exclusive.

**I told the agent not to generalise "Chinese chips" into "Chinese memory" unless the source did. It does.** String-verified counts in the Korean body:

| Term | Occurrences |
|---|---|
| **D램 (DRAM)** | **7** |
| CXMT / 长鑫 / 창신 | **0** |
| YMTC, UNISOC, SMIC, 낸드, LPDDR, AP/모뎀/PMIC, 파운드리 | **0 each** |

Load-bearing sentence: *"삼성전자는 **중국산 저가 모바일 D램 등 현지 반도체(외주 칩)** 채택을 통해…"* — Chinese-made **low-cost mobile DRAM** as an outsourced BOM input.

### 🔴 The finding: "CXMT" was added by aggregators, and the chain is traceable

| Step | Outlet | What it added |
|---|---|---|
| 1 | **Asia Time (KR)**, 07-27 14:15 | "중국산 저가 D램" — **no supplier named** [T2] |
| 2 | IT之家 (CN) | added the spec **"LPDDR5X"** — not in the Korean [T3] |
| 3 | **快科技/MyDrivers (CN)**, 19:43 | added **长鑫存储 (CXMT)** outright: 「三星手机要用长鑫内存！」 [T3] |
| 4 | Sina Finance | syndicated MyDrivers [T3] |
| 5 | wccftech (EN) | headline says CXMT; **body concedes "the report doesn't explicitly mention CXMT"**; self-rates **35% "Questionable"** [T3] |
| 6 | TechNode (EN) | most disciplined: *"did **not specify which** Chinese memory suppliers"* [T3] |

**Every downstream claim naming CXMT is inferred, not read.** It is a *reasonable* inference — CXMT is the only Chinese firm mass-producing JEDEC-certified LPDDR5X — but it is not what the source says. **This is F19's cousin: not a fabricated citation, but a fabricated specificity, accreting across a relay chain until an unnamed supplier becomes a named one.**

### ⛔ My prior was structurally wrong, and the correction matters

I briefed the agent that "Samsung is itself the world's largest DRAM maker — a Samsung purchase of a rival's DRAM would be extraordinary." **That is wrong at the division level.** This is **Samsung MX (Mobile eXperience), not Samsung DS** — separate P&Ls. **MX already routinely buys third-party DRAM from SK Hynix and Micron for Galaxy handsets; second-sourcing is standard practice.** MX buying non-Samsung DRAM is not extraordinary at all. What would be novel is *the supplier's identity* — precisely the fact the article withholds.

**The motive is credible even where the fact is not.** Q2 2026 MX/Networks loss estimates: Hana ₩200bn, Samsung Securities ₩584.1bn, Eugene ₩1tn, iM ₩800bn; Samsung Securities cut FY26 MX operating profit from **+₩3.41tn to −₩5.841tn**. A division under that duress plausibly reviews cost-down options.

### Status and sourcing — both weak

**Status: 유력하게 검토 중 — "strongly under review." Pre-decision.** Not shipping, not qualified, not sampling; **no supplier contact of any kind is described.** Products: **Galaxy A series** (mid/low tier), **China domestic only**, **zero volumes, zero dates, zero contract value.**

**Sourcing: 「27일 반도체 업계에 따르면」** — the weakest form of Korean trade-press attribution: no named source, no source count, no company. **Samsung's own response, quoted in the article: 「확인이 되지 않는다」 — "this cannot be confirmed."** A soft deflection, materially weaker than a 사실무근 ("groundless") denial — **it neither supports nor kills the story.** The only named human is a **KIET economist saying Apple and Samsung "could consider"** adopting Chinese DRAM — an outside economist speculating on plausibility, **not a source confirming a fact.** Zero independent corroboration; no Korean major has matched it.

**⚠️ Timing worth pricing:** this published **on the exact day of CXMT's STAR-Market debut**. The article never mentions CXMT or the IPO. MyDrivers itself flags the risk: 「不排除带有为三星营造有利舆论的宣传色彩」 — PR colouring favourable to Samsung cannot be excluded.

### ⚖️ Does this constitute Tier-1 qualification for CXMT? **NO.**

**Four reasons, and the economic one is the sharpest:**
1. **There is no qualification event.** "검토 중" is *considering*. No sample, no evaluation, no named counterparty. **You cannot have Tier-1 qualification without a named Tier-2 party.**
2. **CXMT is not in the source.** A CXMT thesis here stacks an unsourced claim on a downstream inference.
3. **Volume is immaterial even if true.** Samsung holds **0.1–0.6%** of China (the article says 0.6%, unsourced; IDC via two relays says 0.1%). Full conversion of China-market Galaxy A is low-single-digit millions of units — noise against a company that just raised $8.6bn and signed a ~$3bn Tencent DRAM deal.
4. **The stated economic premise may be inverted.** Two relays report **CXMT pricing DDR5 ABOVE Samsung** and refusing Huawei's discount demands — which is what my own agent 1 verified this afternoon. **If Chinese DRAM isn't cheap, the article's "저가/low-cost" rationale collapses.**

**And the better-evidenced version of this trade already exists: Apple.** Digitimes (06-29) — Apple seeking approval for CXMT DRAM; 9to5Mac/MacRumors (07-08) — Apple **actually testing/qualifying** CXMT chips. Named parties, a stated regulatory pathway, progression through qualification stages. **If the CXMT Tier-1 question is to be tracked, Apple is the instance. Samsung is not.**

**File as: unconfirmed single-source signal that Chinese mobile DRAM has entered a Tier-1 OEM's cost-reduction option set.** Directionally consistent with the CXMT thesis, **evidentially far too thin to move anything.** SKHY falsifier #3's tightened Tier-1 AI-customer leg is untouched — this is client-tier and pre-decision.

## 7.2 ⛔ I WAS WRONG TO NOT-ROUTE `$INTC × $SKHY` — real, multi-outlet reporting underlies it

In §4 above I logged the social post as *"speculation with zero asserted content"* and did not route it. **That was a bad routing call.** I judged the *relay* rather than checking whether anything underlay it. There is a substantial July 2026 story with **two distinct and conflicting claims**:

| Claim | Source | Tier | Status |
|---|---|---|---|
| **A — ACQUISITION:** SK hynix in talks to **buy** Intel's Ohio One campus (~1,000 acres, 8-fab capacity, ~$100bn full build-out) for **US front-end memory production within five years** | Korea JoongAng Daily "Exclusive", **07-22** | T2, anonymous | **Reported** |
| **B — THE DENIAL:** SK hynix **Korea Exchange filing**: *"has not pursued or decided to acquire Intel's Ohio site and fab"* — while continuing to review investment/acquisition opportunities generally. Shares fell ~4%, then pared | **KRX regulatory filing, 07-22** | **T1** | **Acquisition form is DEAD** |
| **C — OPERATING PARTNERSHIP:** Intel seeking a partner to help **run** Ohio, not sell it; SK hynix among candidates *"rather than buy the operation outright."* **"The two companies have not yet engaged in formal negotiations."** A person close to Intel called the interest **"very early."** Intel declined comment; SK hynix did not respond | Semafor "Exclusive", **07-22** | T2, anonymous | **LIVE but embryonic** |
| **D — INTEL'S OWN WORDS:** Lip-Bu Tan, Q2 call **07-23** — memory is a significant supply constraint and AI bottleneck; Intel working with all three major memory vendors as a top priority; **volunteered the ex-SK hynix CEO (Lee Seok-hee) hire while discussing memory plans**. Did **NOT** confirm any SK hynix arrangement | Intel prepared remarks | **T1** | Linkage to SKH is **third-party inference — do not rely** |

**Separate and more concrete workstream:** SK hynix is **testing HBM integration with Intel's EMIB 2.5D packaging** [T3, TrendForce]. Intel has precedent for external capital while retaining control (Brookfield SCIP, Arizona 2022, up to $30bn, 51/49).

**Why this is genuinely position-relevant, two days before the print:** a US front-end memory fab — whether by acquisition or operating partnership — is a **capex commitment of real scale** on a name whose Q2 guidance this desk is about to read as a pre-registered decision gate. **Capex/capital-allocation commentary on Wednesday's call now has a specific thing to listen for.**

**Correct characterisation: an early-stage, twice-reported, once-partially-denied talks story — materially more than "pure speculation," materially less than a transaction.**

## 7.3 The lesson, and it is mine not the agent's

**A low-tier relay can point at a high-tier story. The tier of the relay is not the tier of the underlying.** I dismissed a T3 social post because the *post* asserted nothing — but "$INTC X $SKHY? 👀" was a pointer, and behind it sat a T1 regulatory filing and two independent exclusives. **The correct test is not "what does this source assert?" but "does anything underlie it?"** — and that costs one search.

This is the mirror image of the same day's other failure mode: the Samsung item shows a relay chain *inventing* specificity that was not in the source, while the Intel item shows me *discarding* a relay that pointed at more than it said. **Both are relay-tier errors; they run in opposite directions.** Booked to `predictions/lessons.md` as CANDIDATE L45.

## 7.4 Cost-yield

**Agent A: HIGH / FRAMING-ERROR-CAUGHT ×2.** It traced a six-step attribution chain to show CXMT was inserted downstream, corrected my structurally wrong MX-vs-DS prior, and — most valuably — **refuted the expected answer I had written into its own prompt** on Intel×SK Hynix. A verification agent that overturns the commissioner's stated expectation is the highest-value return class this ledger tracks.
