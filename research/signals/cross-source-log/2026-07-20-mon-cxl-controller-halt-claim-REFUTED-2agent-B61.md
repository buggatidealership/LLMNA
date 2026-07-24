# 2026-07-20 MON — CXL-controller "Big Three halted proprietary development" claim → REFUTED by 2 independent agents (likely a conflation/LLM-generated input, B61 instance); the real landscape finding: the note OMITS Astera Labs (the actual CXL leader) and the market is pre-revenue to 2027-28

**WORKFLOW: INGEST → resolves REFUTED (Rule #16, 2 Opus agents parallel: halt-claim verify + beneficiary-map). Source = user-shared note + image ("Promoting CXL Could Destabilize DRAM — The Cannibalization Dilemma"), tone = confident investment thesis. Verdict: foundational premise UNSUPPORTED-to-CONTRADICTED. NO POSITION ACTION. NO cascade to held theses (premise refuted). Value retained: the CXL landscape map + a caught bad-input instance.**

## The premise is REFUTED (both agents, independent sourcing incl. today-dated)
Claim: "the memory Big Three (Samsung/SK Hynix/Micron) have HALTED / SCRAPPED proprietary CXL controller development" because a finished integrated CXL module would cannibalize their DIMM cash cow.
- **Both agents found the OPPOSITE**, searching the full Korean corpus (thelec/ZDNet Korea/ETNews/TheBell/Sedaily) + DigiTimes/TrendForce with native terms (자기잠식/카니발라이제이션):
  - **Samsung** — actively racing to mass-produce CXL 3.2; CMM-D roadmap live (2.0 samples, 3.1 → 2027). Source dated **2026-07-20** (Sedaily, T3). NOT halted.
  - **SK Hynix** — moving TOWARD in-house controllers (chiplet/FOWLP, TSMC-built, AsicLand ~₩31.1bn design contract through mid-2026). (TrendForce 2025-02-19 T2/T3.) The opposite of exiting.
  - **Micron** — no halt found (weakest leg, T4).
- **"Cannibalization" rationale: NOT FOUND in any outlet, either language.** The real reported "CXL dilemma" (ZDNet 2025-06-26) is technology-ready-but-market-immature (demand-TIMING), a different thing.
- **LIKELY ORIGIN OF THE ERROR (agent-2 catch):** TrendForce's 2026-01-19 "memory giants map 2025-26 EXIT STRATEGY amid supply crunch" piece is about legacy **DDR4 / MLC-NAND exit**, NOT CXL-controller exit → the note appears to have CONFLATED that headline with CXL. This is the fingerprint of a plausible-but-fabricated synthesis.
- **My-model P(premise false): ~85%.** Residual ~15%: a genuine, very-recent (<48h) halt not yet indexed (thelec.kr was 403-blocked to the agents). Falsifier: a primary KR trade-press or IR confirmation of an actual Big-Three CXL-controller-design exit. Until then → treat as REFUTED.
- **B61 INSTANCE (LLM-generated / fabricated-input failure mode):** confident, internally-coherent, structurally-plausible investment note whose load-bearing premise has no traceable source — exactly what B61 + Rule #16 verification exist to catch. Caught pre-cascade; zero thesis contamination. (Companion to the KR/Meritz misattribution catch earlier today — +21%=BofA-not-Meritz — a run of input-provenance defects this session.)

## What SURVIVES as a genuine finding (the note's own framing was also incomplete even if the premise held)
**Joint-state CXL-controller landscape (fabless/merchant) — the note named only Montage+Marvell and OMITTED the leader:**
| Name | CXL product | Position | CXL-purity of equity | Tier |
|---|---|---|---|---|
| **Astera Labs (ALAB)** | Leo CXL Smart Memory Controllers (3rd-gen sampling; KV-cache-offload win ships 2027) | **SemiAnalysis ranks #1 — "first to CXL memory pooling, ahead of Marvell/Rambus/Microchip/Montage"**; live on Azure M-series | LOW purity — Leo CXL is a minority of a Scorpio/Aries-dominated business (Q1 FY26 rev $308.4M +93% YoY) | 🟢 (T2/T3 SemiAnalysis) |
| **Marvell (MRVL)** | Structera CXL + XConn switch ($540M acq closed 2026-02-10) | broadest disaggregated-memory-connectivity portfolio; Samsung Pangea v2 partner | VERY LOW — XConn CXL ~$100M FY28 vs custom-ASIC ~$1.5B→$4B+; CXL = rounding error next to Trainium/optical | 🟢 |
| **Montage (688008.SS / HK dual-list)** | MXC CXL 3.1 (sampling since 2025-09) | core moat = DDR5 RCD/MRCD-MDB (1 of 2 global suppliers); CXL is small forward optionality | LOW-MED — CXL a sliver of the ~19%-of-interconnect line; 2025 rev +49.9% driven by RCD not CXL | 🟡 |
| Rambus (RMBS) | CXL 2.0/3.0 controller IP (licensing, not merchant Si) | complementary, not a shipped-chip competitor | LOW | 🟡 |
| Microchip (MCHP) | XpressConnect CXL retimer | signal-conditioning layer, not the controller | VERY LOW | 🟡 |
| Panmnesia | CXL 3.2 fusion switch (sampling 2H26) | KR startup, private | NOT PUBLICLY INVESTABLE | 🔴 |

**Adoption-timeline reality (material, not decorative):** 2026 = samples/qualification/early-design-win; **real volume 2027-2028** (CXL Consortium's own target; Samsung DELAYED CMM-D mass production to 2027; AMD EPYC Venice sampling pushed past Sept-2026). ">90% of servers CXL-CAPABLE" is a hardware-readiness stat, NOT deployed-pooling adoption. CXL memory-controller-IC TAM ~$70.8M (2026) → ~$312.6M (2031), 34.6% CAGR (Mordor, small-firm est., directional). B45 note: the multi-year TAM shift is real and possibly under-modeled, but near-term 2026 P&L impact for EVERY name here is small — "wide open market" overstates magnitude-NOW vs magnitude-eventually.

## Parallel hypotheses on the input itself (my model)
- **H1 fabricated/LLM-generated note w/ conflated premise (~65%)** — coherent prose, no traceable source, matches the TrendForce DDR4/NAND-exit conflation fingerprint (B61).
- **H2 real-but-garbled human take (~20%)** — someone misread the exit-strategy story + editorialized a cannibalization rationale.
- **H3 genuine very-recent scoop not yet indexed (~15%)** — the residual; would need primary confirmation.

## Cascades
- `watchlist/candidates.md` — **Astera Labs (ALAB)** added as CXL-memory-pooling LEADER candidate (surfaced as the note's omission, genuine Leg-B-style discovery — NOT off the false premise), with the low-purity + pre-revenue-to-2027 caveats. Montage noted as RCD-moat name (CXL = optionality). MRVL: CXL immaterial to its (untracked-folder) story — no action.
- `meta/day-state.md` — B61 refutation logged.
- No held-thesis cascade (premise refuted; the memory book is unaffected — if anything "Big Three building in-house CXL + protecting DIMMs" is mildly supply-discipline-consistent, but I will NOT lean on a refuted-premise note).

**Position implication: NO ACTION — the input's driver premise (Big Three exited CXL controllers) is REFUTED (~85% false, B61 fabricated-input class); the bullish "Montage+Marvell" conclusion loses its stated cause AND omits the actual leader (Astera Labs), AND the market is pre-revenue to 2027-28. Only genuine takeaway: ALAB logged as the CXL-pooling leader to WATCH (low near-term purity, long-run optionality) — no sizing. 🔴 SPECULATIVE (input refuted).**

---
**2026-07-20 ROUND-2 REFINEMENT (forward-pointer, no silent edit):** a more-detailed version of this claim arrived; re-verification (2 more agents) shows the Round-1 "~85% false, B61 fabricated" framing was OVER-STRONG. The STRUCTURAL CORE (fabless supply CXL controllers; Big Three's shipping modules use them; in-house never shipped) is TRUE but a multi-year STATUS QUO; the "new July-2026 wholesale-halt decision" framing stays UNVERIFIED (~70%), built on real kernels (Primemas exists; SK Hynix's ASICLAND CXL design contract really was terminated 06-26) over-generalized + dressed with unsupported specifics (PIM reassignment, Samsung roadmap removal, LPDDR pivot). Full consolidated 3-layer verdict + self-correction: `2026-07-20-mon-cxl-halt-ROUND2-consolidated-3layer-verdict-selfcorrection.md`.
