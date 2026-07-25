# 2026-07-15 EVE — Micron & Samsung HBF posture (user question; 1 Opus agent, EN+KR+JP)

**WORKFLOW: TRIANGULATE.** User: do Micron and Samsung have HBF (or NAND-integration equivalents) on their roadmaps? House had only 2 camps on file (SanDisk+SKH alliance / Kioxia proprietary). Answer: the map is FOUR postures.

## The four-posture map

| Player | HBF posture | Evidence (quoted where load-bearing) | Tier |
|---|---|---|---|
| SanDisk + SK Hynix | Alliance, OCP standard founders | On file: T1 PR 2026-02-25; samples H2-26, devices early-27 | T1 |
| Kioxia | Proprietary track + Nvidia GPU-direct flash | On file (Jun-28 head-to-head) | T2 |
| **Samsung** | **THIRD CAMP — own HBF, early stage, posture AMBIGUOUS** | KR exclusive (fnnews 2025-10-01, 단독): "삼성전자는 자체 HBF 제품 개발을 위한 개념 설계 등 초기 단계에 착수" (= began early-stage concept design for its OWN HBF). TrendForce 2025-11-11: "SK hynix, Samsung, and SanDisk Bet on HBF." Tooling corroboration: Hanmi Semiconductor building a TC bonder for HBF (MTN 2026-05-26). Contradictory standards signals: some coverage says Samsung signed an MOU with SanDisk; the KR exclusive + others frame it as proprietary. NOT a confirmed OCP-workstream member (workstream lists only SanDisk+SKH as founders). No dated samples/MP. | T2 KR-primary; posture unresolved — re-triangulation flagged |
| **Micron** | **FOURTH POSTURE — ABSTAINER: no HBF, betting CXL+QLC instead** | No product/roadmap/membership found; CEO capex narrative all DRAM/HBM (2026-07-11 coverage); TrendForce/Tom's: "no direct involvement in the high-bandwidth flash technology." Its answer to the same demand = 6600 ION 245TB QLC eSSD + CZ122/CZ120 CXL expanders + SOCAMM2. One EETimes-lineage line claims a proprietary Micron track — single-source, no primary, graded LOW/likely lazy grouping | T2 (absence + adjacents) |

**My interpretation (labeled):** Micron is making a deliberate architecture bet — that CXL-DRAM tiering plus ultra-high-capacity QLC covers KV-cache/weights offload without a new stacked-flash form factor. Samsung is doing the classic hedge: cooperate-on-spec signals while building proprietary, with all three enablers in-house (#1 NAND share, HBM franchise, packaging) — lowest integration friction, latest start.

## Samsung's SHIPPING answer today (not HBF)
CMM-D CXL family (MD220 256GB) + the June-2026 KV-cache-offload whitepaper (4× MD220 = 1TB pool; a 512GB DRAM config fails where the 1TB CXL pool holds — Samsung's own numbers, T1 whitepaper) + PM1763 PCIe 6.0 eSSD (MP 2026-07-08). My read: complementary tiers — CXL now, HBF later; Samsung is the only player positioned across all three tiers.

## Competitive read (my model)
- OCP standard WINS → Micron most exposed (no product, no seat); Samsung fast-follows into a spec whose interface terms rivals set; SNDK/SKH moat holds.
- FRAGMENTS (now 3 HBF builders + ambiguous Samsung) → Samsung + Kioxia benefit; the SanDisk "standard-setter moat" from the Jun-28 keep-verdict THINS — fragmentation risk is no longer only Kioxia's "Betamax" problem, it cuts at the alliance too. Micron unaffected either way — its bet is the category underperforms vs CXL+QLC.
- H1 (P~45%, my model): OCP standard prevails, Samsung ultimately joins-and-ships within it (the MOU signals are the tell). H2 (P~35%): dual-standard KR-vs-alliance fragmentation into 2027. H3 (P~20%): Micron's abstention proves right — CXL+QLC absorbs the workload, HBF stays niche.

## Cascades
- `watchlist/HBF-trajectory-monitor.md`: Gate-1 ("standard fragments" reversal trigger) gains named watch items — Samsung OCP membership yes/no + Samsung sample date + FMS Aug-26 posture reveals.
- `companies/SNDK/thesis.md`: moat-read nuance — standard-setter premium now carries a quantified third-camp risk; keep-verdict UNCHANGED (Samsung is ~a year behind, undated), hinge unchanged.
- Open re-triangulation items: Samsung OCP membership (contradictory), Micron FMS/ISSCC commentary (none found), Samsung sample timeline (undated).

**Position implication: NO ACTION — held names untouched (SKHY sits inside the winning-alliance leg either way in H1/H2); SNDK keep-verdict intact with the moat premium marked one notch less certain; watchlist reads for the Jul-31/Aug-5 NAND prints unchanged.** 🟡
