# MARKET-STATE LOG — computed state vectors (spec: market-state-function-spec.md)

**Born:** 2026-07-08 (P1 first run). Compute: `research/meta/market-state-compute.py` (#43b — arithmetic only, interpretation separate). Sourcing: HYBRID (user decision 2026-07-08) — templated pull-agent tape + user screenshots; env-network-policy upgrade path documented in spec.

---

## 2026-07-08 — vector #1 (SEED RUN — mixed-session data, see hygiene notes)

**Inputs:** 16 names, 7 cohorts; user tape (T2-user) + session-verified artifacts. ⚠️ Hygiene: sessions MIXED (some 07-07 closes, some 07-08, some premarket — e.g., Cloudflare +8.6 is 07-07 close on the Scotiabank upgrade); single-member cohorts are placeholders; NOT yet a clean same-session snapshot. The vector's structure is right; the inputs mature with the pull-agent roster.

**Computed output (verbatim from script):**
```
cohort              n   mean%     min     max
ccl-scarcity        3    2.60    1.00    5.00  low=ITEQ high=EliteMaterial
energy              1    1.00
eu-infra            1   -8.87
jp-components       3   -3.80   -5.00   -2.00  low=Disco high=MURATA
memory              5   -5.17   -6.25   -3.50  low=Samsung high=Kioxia
software            1    8.60
us-compute          2   -4.25   -7.00   -1.50  low=SpaceX high=NVDA

breadth: 5/16 up (31%)
cross-cohort dispersion: 17.47pp (software +8.60 vs eu-infra -8.87)
DIVERGENCE FLAG: ccl-scarcity (+2.60) opposite-signed vs tape mean (-2.33)
DIVERGENCE FLAG: energy (+1.00) opposite-signed vs tape mean (-2.33)
DIVERGENCE FLAG: software (+8.60) opposite-signed vs tape mean (-2.33)
```

**Regime read (interpretation layer, my model):** R2 AI-complex derisk ~0.40 / R5 whisper-treadmill ~0.25 (L27 1/2 + Samsung T+48h fade) / R4 intra-AI rotation (growth→scarcity variant) ~0.20 (the CCL flag is its computed signature) / R3 broad risk-off ~0.05 (energy green + 07-07 breadth data cut against) / others ~0.10. Flip conditions per spec §3.

**Divergence ledger entries (born today):**
1. PRIMARY-vs-SECONDARY: SKH ADR book heavily oversubscribed (~1,000 institutions, T2 etoday) vs SKH −5.68% on pricing day (T2-user) — resolves at tonight's NY pricing (second-cut tells pre-registered in HYNIX thesis).
2. STRUCTURAL-BID-vs-COHORT-BETA: ccl-scarcity +2.60 mean on a 31%-breadth tape (computed above) — TC-16; 3-session persistence rule pre-registered.
3. FUNDAMENTAL-vs-REACTION: Samsung record-OP beat → cumulative −6.2/−6.5% (computed 07-08 AM) — L27 tick #1.
