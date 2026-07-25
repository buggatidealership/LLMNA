# 2026-07-17 FRI — IBM W9 DEEP-DIVE: WSJ inside story + filing-grade 8-K + computed cohort tape (docketed 2026-07-16; executes the 4-question pre-registration)

**WORKFLOW: #9 MACRO-FIRST (wraps #1 INGEST of WSJ "The Inside Story of IBM's Shocking Profit Warning," Gardizy/Glazer/Thomas, read 2026-07-17 via 10 user screenshots, T2 journalist-sourced)**
**Builds on (does not repeat):** `2026-07-14-tue-ibm-warning-enterprise-memory-pullforward.md` (mechanism T1, pull-forward corroboration table, Mythos cyber referent, SKHY/NOW cascades — all already booked).
**Fact layer this pass:** 8-K Ex-99.1/99.2 full text via edgar_client (accession 0000051143-26-000070, T1) + cohort tape computed from FMP EOD (facts-first: no press numbers used for prices).

---

## Step 0-1 — Layer first-principles (enterprise-IT budget layer, date-anchored 2026-07-17)

The binding constraint in enterprise IT right now is not demand and not technology — it is **input-cost inflation crowding a fixed budget**. Memory/server/storage prices are rising at supercycle rates (house book: DRAM contract +58-63% Q2, Jefferies Q3 +40-50% QoQ, 64GB RDIMM ~2× in two quarters — all per the Jul-14 artifact §2, T2), while IT budgets were set months ago (Cohn, T2). A CIO with a fixed envelope facing rising hardware prices has exactly four moves: (1) front-run price increases NOW (pull forward), (2) defer everything deferrable, (3) cannibalize other lines (software/consulting/projects), (4) escalate for more budget. June 2026 = moves 1+2+3 executing simultaneously, and IBM's 8-K is the first T1 issuer-level documentation of the whole triple.

## Step 2 — Filing-grade metrics (8-K Ex-99.1, T1 🟢 — completes the headline set from Jul-14)

| Metric | Q2-26 prelim | Note |
|---|---|---|
| Revenue | $17.2B, +1% | vs consensus ~$17.86B (Jul-14 artifact) |
| Software | +5% | below plan; Transaction Processing (Z-attached) named |
| Consulting | flat (+1% cc) | signings still growing, GenAI-led |
| Infrastructure | −7% | Z shortfall; **Distributed Infra +37% = best in reported history, ~$500M backlog exiting Q** |
| GPM | GAAP 57.7% (−100bp); op 59.4% (−70bp) | mix shift away from Z/TP software |
| PTI margin | GAAP 14.4% (−90bp); **op 19.2% (+30bp)** | productivity offset — profit engine intact |
| EPS | GAAP $2.27 (−2%); **op $2.93 (+5%)** | this "profit warning" grew operating EPS |
| FCF YTD | $4.8B (op cash $7.8B) | |
| z17 | ~130% program-to-program vs z16; 85% of installed MIPs maintaining/growing | install base NOT churning |
| New (not in Jul-14 artifact) | **Lightwell**: $5B commitment, open-source-vulnerability clearinghouse launched post-Mythos, GA Jul-8, adopters = BofA/BNY/Citi/GS/JPM/Mastercard/MS/RBC/State Street/Visa/WFC; **Anderon**: DoC LOI, first pure-play quantum wafer foundry, $1B CHIPS + $1B IBM cash, >$10B quantum over 5 yrs | IBM monetizing the SAME cyber churn that hurt its Q — and doubling down on quantum capex |

**The arithmetic tell 🟢:** the −25.2% day (computed: $290.23→$217.07, FMP) removed ~$65-70B of market cap (~919M diluted shares, recall-hedge on sharecount) on a quarter where revenue GREW and operating EPS rose +5%. The market did not price a quarter; it priced Saha's question (WSJ/LinkedIn, T2): *"can a 115-year-old enterprise company lead the agentic era, or merely survive it?"* — a permanent-relevance repricing, exactly the shape of the user's structural-shift hypothesis.

## Computed cohort tape (FMP EOD, market-netted: SPY +0.35% Jul-14, +0.2% cum; QQQ +1.1%/−0.8% — moves below are idiosyncratic) 🟢

| Ticker | Jul-14 (day 1) | Jul-13→16 cum | Read |
|---|---|---|---|
| IBM | −25.21% | −24.53% | no dead-cat inside window (Jul-17 +3.7% pre-open per user widget, T3) |
| DELL | +7.12% | −8.37% | day-1 beneficiary → full round-trip in the Jul-15/16 global memory rout (confound: BOK-day semis crash, house artifact Jul-16) |
| HPE | +4.91% | −4.46% | same round-trip |
| NTAP | +6.48% | −2.59% | same |
| MU | +4.92% | −8.94% | rallied on the letter, sold with the global memory rout |
| CRWD | **+12.14%** | **+8.43%** | the ONLY durable winners: cybersecurity |
| PANW | +6.84% | +7.17% | held gains through the rout |
| NOW | −5.76% | **−6.52%** | did NOT recover — market singling out large-deal enterprise software into Jul-22 |
| CSCO | −1.81% | −8.04% | deferrable-infra casualty, kept bleeding |
| ORCL | −2.74% | −5.53% | |
| CRM | −2.14% | +0.85% | SaaS displacement fear did NOT stick |
| WDAY | −3.49% | +0.39% | same |
| SNOW | +2.71% | +0.51% | consumption-model spared |
| ACN | −2.86% | +4.40% | consulting fear faded fastest |

Day-1 the market traded Krishna's letter line-by-line (long what clients bought, short what they deferred/cannibalized). By Jul-16 the surviving trades are: **cyber up, deferrable-hardware/infra down, NOW down, seat-SaaS forgiven.** That last column IS the market's current answer to displacement-vs-crowding: crowding, concentrated on big-ticket lumpy vendors.

## WSJ inside-story layer (T2 — what the filing cannot show)

- Board debated pre-announce vs wait; Krishna chose disclosure ("Arvind took it upon himself… 'I don't want to surprise them'" — Cohn). Governance read: no smoldering accounting issue; an execution+environment miss surfaced voluntarily.
- **Board tolerance is explicitly finite: "an impatient Wall Street is unlikely to tolerate two or three more quarters of underperformance" (people familiar with board discussions). Board meets again late July.** Activist/breakup vulnerability confirmed by people familiar. Don Bilson (Gordon Haskett): execution stigma now attaches to Krishna.
- Mechanism paragraph matches the letter: AI-infra (memory) + cybersecurity concerns **displacing hardware spend** — WSJ explicitly contrasts with CRM/WDAY/SNOW-style AI-replaces-software fear. Distinct failure modes; the tape (above) confirms the market agrees.
- Customer structure: financial services + retailers; over-reliance on large accounts with lumpy, pushable deals; leadership discussing diversifying to midsize customers (= admission the revenue base is deferral-fragile).
- Daniel Morgan (Synovus): customers treat IBM as discretionary — "we don't need to upgrade to the new mainframe right now."
- Market cap now <$200B vs AVGO $1.8T / AMD $800B ("once seen as small suppliers to giants like IBM").

## The four pre-registered questions (docketed 2026-07-16, day-state)

**Q1 — Segment attribution: ANSWERED at filing grade 🟢.** The miss is a **mainframe-complex event**: Infrastructure −7% (Z collapse masked by Distributed +37%) + the Z-attached Transaction Processing software stack (why Software +5% still "missed plan"). Consulting flat = secondary. This is NOT an AI-displaces-IBM-software print. Within-segment split (Z vs Distributed vs TP) at the Jul-22 full report grades this final.

**Q2 — Displacement vs reallocation vs pause: filing evidence says REALLOCATION + PAUSE, not displacement 🟡.** For reallocation: clients bought MORE infrastructure (Distributed +37%, $500M backlog) while deferring Z — budget moved sideways inside hardware, front-running prices. For pause: "numerous large deals failed to close on the timelines we expected" + 85% MIPs maintained/growing = deferral, not loss. Against displacement: Red Hat accelerated to 11%, GenAI-led signings growth, software +5%. **Jul-22 discriminators (pre-registered): (a) consulting bookings/backlog level; (b) whether June's slipped Z deals closed in July (management commentary); (c) FY guide shape (maintained >5% cc = pause; cut = worse); (d) TP software attach commentary.**

**Q3 — the "temporary" claim: GRADED. Attribution correction first: the quote is Gary COHN, vice chairman, CNBC Jul-15 (T1-said) — not chairman Krishna** (Krishna is chairman+CEO; user relay drift, WSJ confirms Cohn). Substance: **partially true, and the true part is not the reassuring part 🟡.** The June *pull-forward spike* is temporary by construction (once supply is secured, the panic-buy stops — TD Synnex's "modest pull-forward," MS's borrowed-2027-demand caveat). But the *budget squeeze* driving it is priced off memory tightness the house book carries through 2027 (TC-18 revealed-preference cluster N=6; HPE itself: elevated memory prices "well into 2027," Jul-14 artifact §2). A one-quarter reprioritization admits reversal; a 6-quarter input-cost regime does not. Cohn's own CNBC framing concedes the structural half: "companies are now starting to question the return on investment" — budget-composition questioning is exactly what does NOT resolve in a quarter. **User's instinct ("that's probably not the case") = SUPPORTED on the squeeze, with one precision: the mechanism is memory-inflation crowding, not AI-obsolescence of IBM's stack.** Grade the claim itself at the Jul-22 guide: maintained-FY = Cohn vindicated near-term; cut = "temporary" was IR smoothing.

**Q4 — What does IBM sell, and is it obsolete or smaller? (the user's core question)** FY25 base: $67.5B revenue, Software ~$30B (WSJ, T2); rough splits Consulting ~$20B / Infrastructure ~$15B (recall-based estimate — pin at Jul-22).
| Line | What it actually is | Verdict |
|---|---|---|
| Transaction Processing (in Software) | Mainframe-attached annuity — the software toll on Z capacity (banks/retail core systems) | **Smaller, not obsolete, but CAPACITY-LINKED**: the attach means every deferred Z upgrade bleeds software too — highest-margin dollars with single-point-of-failure exposure to the Z cycle |
| Red Hat / hybrid-cloud (in Software) | Open-source infra software layer | Growing (11%, accelerating) — the agentic-era relevance case lives here + Lightwell |
| Consulting | People-led integration, GenAI signings billions (book) | Not obsolete; **margin-fragile in an agentic era** (Krishna himself: AI replaces ~half the work in many workflows — that is his OWN consulting labor model) |
| Z / mainframe (Infrastructure) | Cyclical hardware with the industry's stickiest install base (85% MIPs retained) | **Structurally smaller share of client budgets** as AI-infra takes the growth dollar; deferrable at will, as June proved |
| Distributed Infra (Power/Storage) | Generic-ish servers/storage | Just printed +37% — sells INTO the front-run |
| Quantum (Anderon, $10B/5yr) | Optionality; now with $1B public co-funding | The board-sanctioned "next era" bet — also a capex drag while Wall Street's patience is 2-3 quarters |

**Net answer 🟡: not obsolete — mispositioned in TIME.** ~60% of the P&L (TP + Z + Consulting) monetizes *yesterday's* enterprise stack with deferrable, lumpy, large-account revenue — precisely the profile that a multi-quarter input-cost squeeze keeps hitting. The growth assets (Red Hat, Lightwell, quantum) are real but too small to carry $17B quarters yet. "Smaller place, with a fat annuity tail and finite board patience" is the honest one-line answer.

## Step 3 — pattern matches (named, per W9 quality bar)

- **TC-18 coherence (NOT a formal N+1):** clients front-running price increases with quarterly capex = spot-level revealed preference; TC-18 proper requires committed capital ahead of delivery (LTAs/prepay). Dell's 3-5yr customer supply lockups (Jul-14 §2) remain the cluster-grade instance; IBM's letter is corroborating context at the spot layer.
- **Anomaly-register thread continuation ("AI's cost climbing the customer stack," born Jul-14):** N+1 at the GOVERNANCE layer — the cost squeeze has now consumed a mega-cap board's agenda, an activist setup, and a CEO's tenure risk. Consumers → enterprises → security budgets → boardrooms in 96 hours.
- **B45 regime check:** a −25% single-day on a Dow blue chip is NOT "routine regime volatility" — it is the largest one-day drop in IBM history per WSJ (T2; our computed −25.2% vs Black Monday's −23.7%, Jul-14 artifact) — regime priors do not normalize this; it is a genuine tail event.
- **Value-migration lens (user directive Jul-16):** the screen candidate this generates — *second-order casualties of memory inflation with deferrable revenue* (CSCO −8% cum, enterprise-refresh names) vs *durable beneficiaries the market under-holds* (cyber kept +7-8% while everything round-tripped). Feed to the value-migration screen first run (post-Jul-29).

## Step 4 — house-book contact + dissent

**Rule #18 strongest counter-case (against "structural shift not priced in"):** operating EPS +5%, op-PTI margin +30bp, FCF on plan, z17 install base retained at 85%, Distributed backlog $500M, and the stock already surrendered a quarter of its value in a day — at <$200B / ~14× FCF-ish (recall-hedge) the market may have OVER-priced a timing miss as a relevance crisis; Cohn's reversion scenario ("go back to reinvesting in proven enterprise infrastructure") is IBM-bullish if memory normalizes in 2027 and deferred Z deals close. This counter fails ONLY if the squeeze persists ≥2 more quarters — which is exactly what the house memory book (through-2027 tightness) predicts. So the honest posture: the DIRECTION of the user's hypothesis is supported, but the cheap expression is not shorting IBM after −25%; it is (a) owning the input-cost winners we already own, (b) watching the casualty cohort for the REPEAT prints the market still models as one-offs.

**Hindsight gate — MISS-OF-OMISSION logged (lesson candidate, cascaded to lessons.md):** every input for pre-naming the casualty leg existed in the house book BEFORE Jul-14: Dell +17% PowerEdge repricing (March), HPE "well into 2027" + reprice-existing-orders, Gartner software-trim/DC-systems +55.8% split, 32-40wk memory lead times. We cascaded memory-price BENEFICIARIES for months and never walked the second-order question "whose fixed-budget customers get crowded, and which vendor P&L reports it first?" The 2025 agentic→inference→memory→Micron chain the user asked to replicate has a casualty mirror-image, and it was computable in June. B21 (first-order anchoring) instance at the cascade layer.

## Jul-22 TRIPLE-adjudication checklist (pre-registered, 5PM ET call; NOW print same day)

1. IBM FY guide: maintained >5% cc (pause confirmed) / cut (structural) — the single highest-information bit.
2. Consulting bookings + backlog level (Q2 discriminator).
3. Z deal-closure commentary — did June's slipped deals close in July?
4. Segment split: Z vs Distributed vs TP software attach (grades Q1 final).
5. Memory-cost commentary: does IBM guide its OWN COGS inflation (Distributed margin) — the squeeze arriving on the vendor side?
6. Mythos/cyber-spend language on the call (the Krishna "how much do I need to spend" quote was T2 single-sourced — confirm/kill).
7. NOW same day: budget-reallocation/deal-slippage language = mechanism BROAD; in-line+reaffirm = IBM-idiosyncratic (pre-registered Jul-14, unchanged).

**Files cascaded (Rule #10, same commit):** `companies/IBM/thesis.md` + `facts.md` (CREATED), `companies/NOW/thesis.md`, `companies/HYNIX/thesis.md`, `companies/MU/thesis.md`, `predictions/lessons.md` (L33 candidate), `meta/day-state.md`, `INDEX.md`.

**Position implication: NO ACTION on IBM (not held, no entry package — post-crash entry would be regret-chasing a falling-knife narrative against finite board patience; re-look ONLY at the Jul-22 print with the checklist above). HOLD SKHY/held memory book — this artifact is a demand-side T1 confirmation of pricing power WITH the borrowed-2027-demand discount already booked. NOW: WAIT unchanged into Jul-22.** 🟡
