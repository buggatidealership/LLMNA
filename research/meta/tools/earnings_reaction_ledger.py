#!/usr/bin/env python3
"""
EARNINGS REACTION LEDGER — reusable instrument (born 2026-07-31).

Purpose: for any cohort of names in any earnings cycle, compute the
DIVERGENCE between the after-hours knee-jerk (FLOW) and the next settled
session (CONSIDERED READ), with a cohort control so the divergence is not
just market beta wearing a costume.

Design rules baked in (do not remove):
  * Closes come from machine routes and are cross-verified across >=2 vendors.
    Finnhub /quote is the primary US route (unmetered at tier); FMP
    /stable/historical-price-eod/full is the history route; EODHD is the
    third-vendor check and is QUOTA-LIMITED (20/day).
  * NEVER read an EODHD same-day EOD row (documented stale-print defect,
    data-access.md 2026-07-28/29). Ask it only for rows <= T-1.
  * NEVER use FMP `changePercent` as a daily return. Empirically verified
    2026-07-31: FMP's field is (close-open)/open, NOT close-vs-prior-close.
    Always recompute close-to-close yourself.
  * After-hours prints are NOT retrievable retroactively from any free
    route. They must be supplied by hand with a PRICE ANCHOR and a SOURCE,
    and they are a RANGE across the evening, not a point. The schema forces
    ah_low/ah_high so the range cannot be silently collapsed to a point.
  * Every reaction is reported both RAW and COHORT-ADJUSTED (excess vs the
    same-day mean of cohort members that were NOT reacting to their own
    print that session). The raw number alone manufactures fake regularities.

Usage:
    python3 earnings_reaction_ledger.py            # runs the 2026-07 cycle
    (edit CYCLE below for the next quarter; the code does not change)
"""
import os, json, time, urllib.request, datetime, statistics

# ---------------------------------------------------------------- config
CYCLE = {
    "label": "2026-Q2 hyperscaler cycle",
    "window": ("2026-07-17", "2026-07-31"),
    # ticker -> print date, session ("amc"/"bmo"), base date (prior regular
    # close), T+24h session, T+48h session (None if not yet available)
    "prints": {
        "GOOGL": dict(print_date="2026-07-22", hour="amc", base="2026-07-22",
                      t24="2026-07-23", t48="2026-07-24"),
        "MSFT":  dict(print_date="2026-07-29", hour="amc", base="2026-07-29",
                      t24="2026-07-30", t48="2026-07-31"),
        "META":  dict(print_date="2026-07-29", hour="amc", base="2026-07-29",
                      t24="2026-07-30", t48="2026-07-31"),
        "AMZN":  dict(print_date="2026-07-30", hour="amc", base="2026-07-30",
                      t24="2026-07-31", t48=None),
        "AAPL":  dict(print_date="2026-07-30", hour="amc", base="2026-07-30",
                      t24="2026-07-31", t48=None),
    },
    # HAND-ENTERED, because no free route serves historical extended-hours.
    # pct = the best price-anchored point; lo/hi = the observed evening range.
    # Every entry needs a source string. No source -> leave it None -> the
    # ledger prints DATA GAP rather than inventing a number.
    "after_hours": {
        "GOOGL": dict(pct=-4.90, lo=-7.0, hi=-4.90,
                      src="T2 Yahoo Finance AH snapshot 'drops nearly 5%' / 'down 4.9%'; CNBC 'fell as much as 7%'"),
        "MSFT":  dict(pct=+8.88, lo=+3.0, hi=+8.88,
                      src="corpus anchor +8.88% (day-state 07-29); T2 Phemex $422.30 = +8.13%; T2 Yahoo early snapshot '+3%'"),
        "META":  dict(pct=-7.45, lo=-9.0, hi=-7.45,
                      src="corpus anchor -7.45% (reward-function-map 07-30); T2 Phemex 'fell ~8%'; T2 'almost 9%'"),
        "AMZN":  dict(pct=+7.41, lo=+7.41, hi=+10.0,
                      src="corpus $252.95 = +7.41% (lessons.md, price-anchored); T2 Motley Fool 'over 8%'; T2 Benzinga '+9.5%'; T2 TradingKey '10%'"),
        "AAPL":  dict(pct=-7.00, lo=-7.8, hi=-6.0,
                      src="T2 Yahoo headline 'drops 7% after-hours'; T2 Benzinga 'as much as 6%'; corpus band -6% to -7.8%"),
    },
}

UA = {"User-Agent": "Mozilla/5.0 (LLMNA earnings-reaction-ledger)"}


def _get(url):
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.loads(r.read())


def fetch_fmp_eod(ticker, start, end):
    k = os.environ["FMP_API_KEY"]                      # NEVER-ECHO
    d = _get("https://financialmodelingprep.com/stable/historical-price-eod/full"
             f"?symbol={ticker}&from={start}&to={end}&apikey={k}")
    rows = d if isinstance(d, list) else d.get("historical", [])
    # deliberately DROP changePercent: wrong basis (close-open)/open
    return {r["date"]: {kk: r[kk] for kk in ("open", "high", "low", "close")}
            for r in rows}


def fetch_finnhub_quote(ticker):
    k = os.environ["FINNHUB_API_KEY"]                  # NEVER-ECHO
    d = _get(f"https://finnhub.io/api/v1/quote?symbol={ticker}&token={k}")
    return dict(close=d.get("c"), prev_close=d.get("pc"), open=d.get("o"),
                high=d.get("h"), low=d.get("l"),
                ts_utc=datetime.datetime.fromtimestamp(
                    d.get("t", 0), datetime.timezone.utc).isoformat())


def fetch_eodhd_eod(ticker, start, end, today):
    """Third-vendor check. Refuses to return the same-day row (vendor defect)."""
    k = os.environ["EODHD_API_TOKEN"]                  # NEVER-ECHO
    d = _get(f"https://eodhd.com/api/eod/{ticker}.US?from={start}&to={end}"
             f"&api_token={k}&fmt=json")
    return {r["date"]: {kk: r[kk] for kk in ("open", "high", "low", "close")}
            for r in d if r["date"] != today}          # <-- the defect guard


def pct(a, b):
    return None if (a is None or b in (None, 0)) else (a / b - 1.0) * 100.0


def build(cycle, use_eodhd_check=True):
    start, end = cycle["window"]
    today = datetime.date.today().isoformat()
    tickers = list(cycle["prints"])
    eod, quotes, xcheck = {}, {}, {}
    for t in tickers:
        eod[t] = fetch_fmp_eod(t, start, end); time.sleep(0.4)
        quotes[t] = fetch_finnhub_quote(t);    time.sleep(0.4)
    if use_eodhd_check:
        for t in tickers:
            try:
                xcheck[t] = fetch_eodhd_eod(t, start, end, today)
            except Exception as e:
                xcheck[t] = {"_err": repr(e)[:120]}
            time.sleep(0.4)

    # --- vendor agreement audit ------------------------------------------
    audit = []
    for t in tickers:
        q = quotes[t]
        for d, row in sorted(eod[t].items()):
            if t in xcheck and d in xcheck[t]:
                if abs(xcheck[t][d]["close"] - row["close"]) > 0.005:
                    audit.append(f"{t} {d}: FMP {row['close']} vs EODHD {xcheck[t][d]['close']}")
        # Finnhub live quote vs FMP latest two rows
        ds = sorted(eod[t])
        if ds and q["close"] and abs(q["close"] - eod[t][ds[-1]]["close"]) > 0.005:
            audit.append(f"{t} latest: Finnhub {q['close']} vs FMP {eod[t][ds[-1]]['close']}")

    # --- close-to-close returns for every session ------------------------
    ret = {}
    for t in tickers:
        ds = sorted(eod[t]); ret[t] = {}
        for i in range(1, len(ds)):
            ret[t][ds[i]] = pct(eod[t][ds[i]]["close"], eod[t][ds[i-1]]["close"])

    # --- cohort control: mean of names NOT reacting to their own print ----
    reacting = {}   # session -> set of tickers whose reaction that session is
    for t, p in cycle["prints"].items():
        for d in (p["t24"], p["t48"]):
            if d:
                reacting.setdefault(d, set()).add(t)

    def control(session, exclude):
        peers = [ret[x][session] for x in tickers
                 if x != exclude and x not in reacting.get(session, set())
                 and ret[x].get(session) is not None]
        return statistics.fmean(peers) if peers else None, [
            x for x in tickers if x != exclude
            and x not in reacting.get(session, set()) and ret[x].get(session) is not None]

    # --- the ledger -------------------------------------------------------
    out = []
    for t, p in cycle["prints"].items():
        base_px = eod[t][p["base"]]["close"]
        d24 = pct(eod[t][p["t24"]]["close"], base_px) if p["t24"] in eod[t] else None
        d48 = pct(eod[t][p["t48"]]["close"], base_px) if p["t48"] and p["t48"] in eod[t] else None
        ah = cycle["after_hours"].get(t) or {}
        c = ah.get("pct")
        ctrl, ctrl_names = control(p["t24"], t)
        d24_adj = None if (d24 is None or ctrl is None) else d24 - ctrl
        out.append(dict(
            ticker=t, print_date=p["print_date"], hour=p["hour"],
            base_date=p["base"], base_close=base_px,
            ah_pct=c, ah_lo=ah.get("lo"), ah_hi=ah.get("hi"), ah_src=ah.get("src"),
            t24_date=p["t24"], t24_close=eod[t][p["t24"]]["close"] if p["t24"] in eod[t] else None,
            t24_pct=d24,
            t48_date=p["t48"], t48_pct=d48,
            t24_high=eod[t][p["t24"]]["high"] if p["t24"] in eod[t] else None,
            t24_low=eod[t][p["t24"]]["low"] if p["t24"] in eod[t] else None,
            control_pct=ctrl, control_names=ctrl_names,
            t24_excess=d24_adj,
            divergence_raw=None if (d24 is None or c is None) else d24 - c,
            divergence_adj=None if (d24_adj is None or c is None) else d24_adj - c,
            divergence_raw_lo=None if (d24 is None or ah.get("hi") is None) else d24 - ah["hi"],
            divergence_raw_hi=None if (d24 is None or ah.get("lo") is None) else d24 - ah["lo"],
        ))
    return out, audit, quotes


def implied_price(base_close, claimed_pct):
    """Discrepancy forensics: what price does a disputed % imply, and is it
    inside the session's range (=> intraday tick) or outside (=> other cause)?"""
    return base_close * (1 + claimed_pct / 100.0)


def report(rows, audit, quotes):
    print(f"# EARNINGS REACTION LEDGER — {CYCLE['label']}")
    print(f"# built_utc {datetime.datetime.now(datetime.timezone.utc).isoformat()}")
    print(f"# vendor-disagreement rows: {len(audit)}")
    for a in audit:
        print("  !!", a)
    hdr = ("TKR  print       base       base$    AH%      T24%     T48%    "
           "ctrl%   excess%  div_raw  div_adj")
    print(hdr); print("-" * len(hdr))
    f = lambda v: "   n/a " if v is None else f"{v:7.2f}"
    for r in rows:
        print(f"{r['ticker']:<5}{r['print_date']} {r['base_date']} "
              f"{r['base_close']:8.2f} {f(r['ah_pct'])} {f(r['t24_pct'])} "
              f"{f(r['t48_pct'])} {f(r['control_pct'])} {f(r['t24_excess'])} "
              f"{f(r['divergence_raw'])} {f(r['divergence_adj'])}")
    print("\n# SIGN TEST (AH vs T+24h opposite sign?)")
    for r in rows:
        if r["ah_pct"] is None or r["t24_pct"] is None:
            print(f"  {r['ticker']}: DATA GAP"); continue
        print(f"  {r['ticker']}: {'OPPOSITE — AH was FLOW not information' if r['ah_pct']*r['t24_pct'] < 0 else 'same sign'}")
    print("\n# COMMON-DIRECTION TEST")
    for key, lab in (("divergence_raw", "RAW"), ("divergence_adj", "COHORT-ADJUSTED")):
        v = [r[key] for r in rows if r[key] is not None]
        if not v: continue
        print(f"  {lab}: n={len(v)} pos={sum(1 for x in v if x>0)} neg={sum(1 for x in v if x<0)} "
              f"mean={statistics.fmean(v):+.2f}pp  -> "
              f"{'DIRECTIONAL' if abs(sum(1 for x in v if x>0)-len(v)/2)==len(v)/2 else 'MIXED (no regularity)'}")
    print("\n# RANKED BY |divergence| (cohort-adjusted)")
    for r in sorted([x for x in rows if x["divergence_adj"] is not None],
                    key=lambda x: -abs(x["divergence_adj"])):
        print(f"  {r['ticker']:<6}{r['divergence_adj']:+.2f}pp   (raw {r['divergence_raw']:+.2f}pp)")


if __name__ == "__main__":
    rows, audit, quotes = build(CYCLE)
    report(rows, audit, quotes)
