# INTU — Intuit Inc. · FACTS

**Raw numerical facts only. No interpretation.** (House rule: interpretation lives in `interpretations.md`, the read in `thesis.md`.)

**Folder opened:** 2026-08-08 (portfolio-addition discovery pass). No prior coverage — the corpus had **zero** files on Intuit before this date (grep-verified 2026-08-08; the 47 files matching "intuit" are all "Intuitive Surgical" / "counterintuitive").

Fiscal year ends **31 July**. FY2026 therefore ENDED 2026-07-31 and is unreported as of this file's creation.

---

## 1. Market data (🟢 HARD)

| Item | Value | Source / date |
|---|---|---|
| Close 2026-08-07 | **$325.25** (adjusted) | EODHD `/api/eod/INTU.US`, fetched 2026-08-08 |
| 52-week high | **$740.68** (2025-08-08) | same series |
| 52-week low | **$253.95** (2026-06-25) | same series |
| Off 52w high | **−56.1%** | computed |
| Off 52w low | **+28.1%** | computed |
| YTD 2026 (from 2025-12-31 close) | **−50.4%** | computed |
| Implied diluted shares | **~279.3M** (= 9M FY26 net income $4,203M ÷ EPS $15.05) | computed from EDGAR |
| Implied market cap | **~$90.8B** | computed |
| 50-day MA / 200-day MA | $291.17 / $455.46 | computed |
| Annualised vol, trailing 60d | **65.9%** (vs 47.3% trailing 12m) | computed |
| Max drawdown, trailing 12m | **−65.7%** | computed |

Exchange: **Nasdaq (INTU)**. US large cap — DeGiro-accessible from Germany (standard US universe).

## 2. Filing-grade financials — SEC EDGAR XBRL (🟢 HARD)

Pulled from `data.sec.gov/api/xbrl/companyconcept/CIK0000896878/...` on 2026-08-08. All $M.

### Nine months FY26 (2025-08-01 → 2026-04-30) vs prior-year nine months

| Line | 9M FY26 | 9M FY25 | Δ |
|---|---|---|---|
| Revenue | 17,094 | 15,000 | **+14.0%** |
| Operating income | 5,409 | 4,584 | **+18.0%** |
| Net income | 4,203 | 3,488 | **+20.5%** |
| GAAP diluted EPS | $15.05 | $12.33 | **+22.1%** |
| Operating cash flow | 7,507 | 5,826 | **+28.9%** |
| Share-based comp | 1,549 | 1,478 | +4.8% |
| Buybacks | 3,341 | 2,026 | **+64.9%** |
| Operating margin | 31.6% | 30.6% | +1.1pp |
| SBC as % of revenue | 9.1% | 9.9% | −0.8pp |

### Quarterly revenue (EDGAR period rows)

| Quarter | Revenue | Prior year | Δ |
|---|---|---|---|
| Q1 FY26 (Aug–Oct 2025) | 3,885 | 3,283 | +18.3% |
| Q2 FY26 (Nov 2025–Jan 2026) | 4,651 | 3,963 | +17.4% |
| Q3 FY26 (Feb–Apr 2026) | 8,558 | 7,754 | +10.4% |

TTM revenue through 2026-04-30 = **$20,925M** (Q4 FY25 3,831 + 3,885 + 4,651 + 8,558).
⚠️ Note for future sessions: a naive "sum the last four ~90-day rows" TTM helper **double-counts** Intuit's tax quarter and returns ~$24.8B. Intuit's Q3 is ~4× Q1 in size; always build TTM from explicit period rows. (Caught and discarded 2026-08-08.)

### Full-year history

| FY (ends 31 Jul) | Revenue | Op income | Net income | GAAP dil. EPS | Op cash flow |
|---|---|---|---|---|---|
| FY2025 | 18,831 | 4,923 | 3,869 | $13.67 | 6,207 |
| FY2024 | — | — | — | — | 4,884 |

### Diluted weighted-average share count (10-K)

| FYE | Shares | Δ |
|---|---|---|
| 2019-07-31 | 264.0M | — |
| 2021-07-31 | 273.0M | +3.4% |
| 2022-07-31 | 284.0M | +4.0% |
| 2023-07-31 | 283.0M | −0.4% |
| 2024-07-31 | 284.0M | +0.4% |
| 2025-07-31 | 283.0M | −0.4% |

Share count **flat for four years** despite ~9% of revenue in SBC — buybacks fully offset dilution.

## 3. FY26 guidance as raised at the Q3 print (🟢 HARD — primary source)

Source: Intuit Q3 FY26 press release, **2026-05-20** ([businesswire](https://www.businesswire.com/news/home/20260520628538/en/Intuit-Reports-Strong-Third-Quarter-Results-and-Raises-Full-Year-Revenue-Guidance)).

| Metric | FY26 guide | Growth |
|---|---|---|
| Revenue | **$21.341–21.374B** | ~13–14% |
| GAAP diluted EPS | **$15.79–15.84** | ~16% |
| Non-GAAP diluted EPS | **$23.80–23.85** | ~18% |

⚠️ The GAAP EPS guide **includes** restructuring charges of **$300–340M**, "largely recognized in its fourth fiscal quarter ending July 31, 2026." Restructuring expense in the 9M FY26 10-Q was **$0** — the whole charge lands in the Q4 print.

### Segment detail, Q3 FY26 (same primary source)

| Segment / line | Q3 revenue | Q3 growth | FY26 guide |
|---|---|---|---|
| Global Business Solutions | $3.3B | **+15%** | ~16% (raised) |
| — Online Ecosystem | $2.5B | **+19%** | — |
| — QuickBooks Online Accounting | — | **+22%** | — |
| — Online Services | — | +15% (+$160M) | — |
| Consumer (TurboTax) | $5.3B | +8% | ~10% (raised) |
| Credit Karma | $631M | +15% | ~19% |
| ProTax | $278M | flat | ~4% |

QuickBooks Online Accounting growth attributed by the company to *"the interrelated factors of higher effective prices, customer growth, and mix-shift."*
Online Services growth composition: **money offerings +$107M, payroll offerings +$55M.**
TurboTax Live customers guided **+38%**; TurboTax filers starting in Credit Karma **+54%**.

### Restructuring
Company is **"reducing its full-time workforce by 17 percent."** Charge $300–340M.

### Segment reorganisation
Per the Q3 FY26 10-Q: effective **2025-08-01**, Intuit **combined Consumer, Credit Karma and ProTax into a single Consumer segment**; prior-year comparatives recast. ⚠️ Relevant to any falsifier written against segment-level disclosure — the reporting basis has already changed once inside this fiscal year.

### TurboTax guidance trim (🟡 DIRECTIONAL — press, not primary)
FY26 TurboTax revenue trimmed to **$5.277–5.282B** from **$5.305–5.330B** (a cut of ~$28–48M, ~0.6%); total IRS filings expected down ~30bp for the season.

## 4. Dated catalysts (🟢 HARD)

| Date | Event |
|---|---|
| **2026-08-25** (after close) | **Q4 + full-year FY26 results, and first FY27 guidance.** Carries the $300–340M restructuring charge. |
| **2026-09-17** | **Investor Day.** |

Source: [Intuit IR, 2026-07-30](https://investors.intuit.com/news-events/press-releases/detail/1318/intuit-to-announce-fourth-quarter-and-full-year-fiscal-2026-results-on-aug-25-investor-day-set-for-sep-17).

⚠️ **UNVERIFIED — do not use:** a secondary aggregation surfaced "preliminary FY2027 guidance of 11–12% revenue growth." It is **not** in the Q3 FY26 press release and could not be traced to a primary source. Treated as absent. FY27 guidance is expected at the Aug-25 print.

## 5. Computed valuation at $325.25 (computed 2026-08-08)

| Metric | Value |
|---|---|
| P/E on FY26 GAAP guide midpoint ($15.82) | **20.6×** |
| P/E on FY26 GAAP ex-restructuring (~$16.72) | 19.5× |
| P/E on FY26 non-GAAP guide midpoint ($23.83) | **13.7×** |
| Est. FY26 operating cash flow | ~$7.89B |
| Est. FY26 free cash flow (capex ~$300M) | ~$7.59B |
| **FCF yield** | **~8.4%** |
| Annualised buyback pace (9M × 4/3) | ~$4.46B = **4.9% of market cap/yr** |

### Reverse-DCF — what the price implies
10% discount rate, FCF growth fading linearly to terminal over 10 years:

| Starting FCF growth | Terminal growth implied by $325.25 |
|---|---|
| 12% | **−3.6%** in perpetuity |
| 10% | **−2.5%** in perpetuity |
| 8% | **−1.4%** in perpetuity |

## 6. Correlation to the held book (computed 2026-08-08)

Daily returns, 250 observations, 2025-08-08 → 2026-08-07 (EODHD adjusted closes):

| | INTU | NVDA | PLTR | AMZN | LLY | S&P 500 |
|---|---|---|---|---|---|---|
| **INTU** | 1.00 | **0.01** | 0.31 | 0.08 | 0.04 | 0.07 |
| NVDA | 0.01 | 1.00 | 0.33 | 0.31 | −0.04 | 0.66 |
| PLTR | 0.31 | 0.33 | 1.00 | 0.24 | −0.05 | 0.42 |
| AMZN | 0.08 | 0.31 | 0.24 | 1.00 | 0.03 | 0.55 |
| LLY | 0.04 | −0.04 | −0.05 | 0.03 | 1.00 | 0.13 |

- Average correlation of INTU to the four holdings: **+0.11**
- Average **pairwise correlation inside the existing four-name book: +0.14** — i.e. the held book is already less internally correlated than a "three-quarters one trade" description implies. Recorded because it **weakens** a diversification argument, not because it supports one.
- Equal-weight book annualised vol **25.5%**; adding 10/15/20% INTU moves it to 24.4 / 24.3 / 24.3%. **Diversification benefit ≈ 1pp. Small.**

## 7. Trailing returns for reference (same series)

| Name | Close 2026-08-07 | YTD 2026 | 12m | ann. vol | max DD 12m |
|---|---|---|---|---|---|
| INTU | 325.25 | −50.4% | −56.1% | 47.3% | −65.7% |
| NVDA | 223.96 | +20.2% | +22.7% | 36.6% | −20.2% |
| PLTR | 172.01 | −3.2% | −8.0% | 60.3% | −48.2% |
| AMZN | 274.48 | +18.9% | +23.3% | 34.4% | −21.7% |
| LLY | 1,185.71 | +10.7% | +90.9% | 35.6% | −23.2% |
| S&P 500 | 7,757.64 | +13.3% | +21.4% | 12.9% | −9.1% |
