# 2026-07-28 — Audit second commission DELIVERED: all four asks. F1 tape independently verified here. The June crash is misdated +1 day corpus-wide, and Korea LED.

**Input:** the audit session's full response to `2026-07-27-audit-session-REPLY-and-second-commission.md` (as amended). All four asks delivered; report persisted at **`838ef4a` + `1eb51e1` on `claude/verify-investment-os-claims-5u2qb7`** — verified fetched here: 1,595-line report file on the branch, not on main, not merged, exactly as asked.

---

## 1. ✅ MY INDEPENDENT VERIFICATION OF THE F1 TAPE — every figure reproduces

The auditor's June tape came from Yahoo chart API + Korean press (T2/T3). **I re-fetched the window from EODHD — a third, independent vendor — with keyed access (T1-machine):**

| Date | KOSPI close | Δ (computed) | SK Hynix | Δ | Samsung | Δ |
|---|---|---|---|---|---|---|
| Mon 06-22 | **9,114.55** | **+0.69%** ← record | 2,919,000 | +5.61% | 353,500 | −0.14% |
| Tue 06-23 | **8,203.84** | **−9.99%** ← the crash | 2,555,000 | **−12.47%** | 310,000 | **−12.31%** |
| Wed 06-24 | **8,471.02** | **+3.26%** ← up day | 2,580,000 | +0.98% | 340,500 | +9.84% |
| Thu 06-25 | 8,930.30 | +5.42% | 2,917,000 | +13.06% | 358,500 | +5.29% |
| Fri 06-26 | 8,411.21 | **−5.81%** ← CB #5 | 2,673,000 | −8.36% | 339,500 | −5.30% |

**Every claimed figure reproduces exactly, including both the 06-25 rebound and the separate 06-26 crash.** Bonus resolution: the auditor flagged a vendor discrepancy on SK Hynix's 06-24 close (Yahoo 2,621,000 vs Korean press 2,580,000) and took the press figure — **EODHD independently returns 2,580,000, settling it in the press's favour.**

**⚖️ VERDICT: F1 is CONFIRMED at the strongest tier available.** The corpus's June crash sequence is shifted +1 day throughout (crash on 06-24 → actually Tue 06-23; record high on 06-23 → actually Mon 06-22). The recovery figure +4.14% is wrong (+3.26%). 52 lines across 7 theses; **MURATA and SUMCO currently held**, five exited.

## 2. THE ROOT CAUSE IS THIS MORNING'S DEFECT, ONE MONTH EARLIER — same class, same vendor behaviour

The auditor traced the +1 shift to a single intake event: the 06-23 morning artifact reported **Monday's close as "today's" close** — a T-1 vendor lag whose *date basis* went unchecked while its freshness did. Everything cascaded from that: the shifted dates, the phantom "June 8" attribution (actually the 06-23 intraday CB trigger print, 8,375.31 / −8.11% — which recomputes exactly against Monday's 9,114.55), and the inverted causal story.

**This morning, 2026-07-28, I caught the identical defect live:** EODHD's real-time index feeds carrying a **stale (T-1) `previousClose`**, making the vendor's own `change_p` wrong by −2.14pp on KOSDAQ. **Same vendor-lag class, caught at intake this time instead of a month later by an external auditor.** The June episode is what happens when this class is NOT caught: one unchecked T-1 snapshot propagated into 52 lines across 7 theses and survived 5 weeks.

**Meta-class extended and computed:** L42 (AH vs settled) · L43 (WTI vs Brent) · L44a (raw vs split-adjusted) · L44b (RT tick vs auction) · stale `prevClose` (07-28, caught) · **USDKRW night-bar vs Seoul close (confirmed below)** · **T-1 date-basis lag (F1, the June origin)** = **seven instances of one family: a number's basis is not part of its identity in this corpus.** The auditor's phrasing, adopted verbatim.

## 3. ✅ ASK 4 RESOLVED — the USDKRW "−1.09%" is a night-session number wearing a daily-close label

| Basis | 07-23 → 07-24 | Change | Tier |
|---|---|---|---|
| 24h/UTC bar (what the corpus used) | 1,475.63 → 1,459.57 | **−1.09%** | T3 |
| **Seoul onshore 15:30 KST close (매매기준율)** | 1,466.8 → **1,466.6** | **−0.01% — FLAT** | T2 ×4 (fnnews, news1, asiae, KB) |
| Seoul night session (~06:00 KST Sat) | → 1,458.5 | −0.55% vs 15:30 | T2 |

**The claim "the won strengthened on the day foreigners net-sold" is manufactured by basis mismatch:** on the session the foreigners actually sold, the won did not move. The −1.09% imports 8h30m of post-equity-close information into the FX leg alone.

**⚖️ DECISION (mine to make, made now — basis declaration, not a reweight):** the H3 Path-B cluster adopts a **declared-cut rule**: every leg carries an explicit cut time; **KR-session legs (KOSPI close, foreign flows, sidecar, USDKRW) cut at Seoul 15:30 KST onshore close**; structurally US-cut legs (10Y via FRED) stamped as such; **no cross-cut comparison without both stamps shown.** The auditor's caveat — that a Seoul FX print is itself mixed-basis vs US-session legs — is exactly why the rule is *declare and stamp*, not *convert everything to one zone*. Booked as **five-calls addendum #10**.

**Consequence for the standing record:** the 07-24 Path-B FX reading ("won fell 1.09% on rout day") is **RETRACTED as a session-basis claim** — the Seoul-session move was −0.01%. The audit's original claim 6 verdict ("number ✓, framing refuted") now upgrades to fully adjudicated.

## 4. KIOXIA CORRECTION — adjudicated, both partly right

The auditor re-checked and **both fabricated-citation instances exist**: HCAttention → `HYNIX/thesis.md` (my find), **and** subagent-4's invented `citi.com/research/vera-rubin-cmx-tb-estimate` → `KIOXIA/thesis.md:343`, where the "Citi estimate 1,152 TB SSD NAND per Vera Rubin system" line closes with a 🟢 HOLD position implication. My correction narrows to: within that paragraph the Citi figure is vector 1 of 4 and no fabricated URL is a *sole* load-bearer. **The hole reached two theses, not one.**

## 5. ASK 3 RECEIVED — the change-list is DATA, NOT A QUEUE (per the standing handling rule)

Full list on the branch. Routing decisions **now**, builds **not now**:

| Class | Items | Routing |
|---|---|---|
| **Subtractions** (weighted higher, as asked) | S1 stale settings mirror (decoy the test suite binds to) · S2 the three fabricated-evidence artifacts · S3 collapse 20+ ad-hoc tier suffixes → T1/T2/T3 + mandatory basis field · S4 coinflip comparator · S5 kill the corrupted structural-output experiment substrate · S6 already-adjudicated retirees · S7 exemption-layer replacement (spec only, self-flagged as its least-confident item) | **S2 and S1 are deletions → Rule #19 tiers (S2 = 3-file deletion + protected-class content = HIGH, operator pre-approval required; S1 needs its "loaded by nothing" claim independently verified first).** S3/S4/S6 → codification-pass candidates. S5 → adjudicate at the pre-registered 08-06 decision date, not before. S7 → problem statement, filed |
| **Additions** | A1 URL-liveness CI (its highest value-to-risk: catches the confirmed 28-fabrication class, CI not enforcement, FP visible and cheap) · A2 tape ledger · A3 market calendar · A4 intra-doc numeric diff · A5 correction-propagation gate · A6 briefing reads existing signals · A7 probe canary · A8 orphan reachability | **A1 → merged into the P0 intake-boundary item as its first concrete build.** A2-A4 fold into the same P0 (the tape ledger IS the basis-field fix). A5-A8 → todo P1/P2 |
| **Non-finding-driven (C)** | **C1 attention is the unpriced resource** · **C2 no adversary profits from the system being wrong** (pen-test ≠ review) · **C3 no claim carries expected time-to-resolution** (mechanism behind 58% thesis staleness) · **C4 nothing records operator priors** (Brier measures right, not useful) | **The part the amendment bought.** All four are absence-class findings the cooperative audits never surfaced. → todo as named candidates for the next codification pass, each with its stated falsifier |
| **Counter-list** | 101/102 orphans, the two failing tests, git-guard FPs, stop_hook_active, B17 non-enforcement, input diet (its own hypothesis refuted), F14 ledger | **Adopted as-is** — including its refusal to touch live enforcement, which is the house rule holding from the other side |

## 6. THE "WHAT DID YOU NOT CHECK" ANSWER — and it names the next commission

Verbatim core: *"My method was source-shaped… What I structurally could not see is whether the research judgment is any good. I never asked whether the HBM thesis is right, only whether its numbers are correctly bound to their instruments… Seeing that surface would take an auditor who starts from the theses rather than the harness — someone who asks whether memory is actually the bottleneck, and treats the hooks as scenery."*

**That is the honest answer the question was designed to elicit, and it defines the third commission: a thesis-first audit — hooks as scenery, subject matter as target.** Not commissioned now (the print is tomorrow); nominated for after the 07-29/07-31 event cluster clears.

## 7. Open items and sequencing

1. **Addendum: ACCEPTED** — the auditor pushes the verified tape + 52-line enumeration + its own evidence corrections to its branch. **The cascade (52 lines, 7 theses) is mine, on main, after the addendum lands** — with its conflation warning adopted: 06-23 (CB #4) and 06-26 (CB #5) are **separate events** with +5.42% between; any pass treating 06-23..26 as one slide introduces a new error.
2. **Two held names carry the error (MURATA, SUMCO)** — both Class A ("peripheral Asia chip-sympathy" line). Neither touches tomorrow's SKHY gate; cascade priority is post-addendum, pre-07-31.
3. **The causal inversion (Korea LED; US followed, intraday-sequenced: flat open −0.34%, BofA call on Korean wires 10:53, sidecar 11:40, CB 14:33, Nasdaq futures following)** reclassifies the KR flow layer from *sympathetic* to *leading* for that episode — a Path-B interpretive upgrade, position-neutral, folded into addendum #10's notes. 🟡 T2 sequencing, no T1 halt log (KRX unreachable — flagged inferred by the auditor, carried as such).

**NO POSITION ACTION (user-gated). Nothing here moves H1/H2/H3 weights or fires any falsifier. The 2026-07-29 SK Hynix Q2 print remains the sole adjudicator of the conditional add.**

---

## 8. CASCADE EXECUTED (2026-07-28, same day)

**51 of 52 enumerated lines corrected on main; 1 enumeration false positive found and logged.** Method: thesis files (7) received in-place date fixes + a Rule #10 back-ref block each (held names MURATA/SUMCO with position-implication lines); signals and ledger files (10) received inline ⟦F1-CORR⟧ markers appended to each defective line — originals preserved as the record — plus a header banner on the 7 signals artifacts. The origin artifact (`2026-06-23-am-subagent-full-cohort-price-action-global-macro.md`) is banner-flagged as the intake-defect source.

**Enumeration FP #3 (beyond the auditor's two):** `companies/HYNIX/thesis.md:1655` — the classifier's `06-24` match is the **SEC F-1 filing date** (2026-06-24 EDGAR registration for the ADR offering), a genuine event date, not the crash misdating. Left untouched. This confirms the classifier note in ADDENDUM 2 §5: first-match-wins cannot distinguish semantic role; any re-run needs a filing-date exclusion.

**Dependency notes honoured:** SNDK's "Jun 23" kept (correct date, weekday label fixed Mon→Tue); KIOXIA's "Jun 24" fixed; HYNIX:412 received both Class A and Class C edits in the same sentence plus the Korea-led sequencing note; MRVL's +8.23% leg re-dated but explicitly retained 🔴 UNVERIFIED. The 06-23 (CB#4) / 06-26 (CB#5) conflation guard is written into every thesis back-ref.

**NO POSITION ACTION. No falsifier touched — every correction is to historical context lines; no thesis mechanics, tiers, or falsifiers changed.**
