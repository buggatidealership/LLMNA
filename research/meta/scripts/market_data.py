#!/usr/bin/env python3
"""
market_data.py — API fetch layer for the good-morning wake (built 2026-07-11 per protocol §API layer).

SECURITY (binding, protocol §API layer NEVER-ECHO discipline):
  - Keys are read from environment variables ONLY (durable route) with a container-local
    scratchpad fallback (pre-burned paste-then-rotate route). Key values are NEVER printed,
    logged, or included in error messages. All diagnostics mask to key name + present/absent.
  - Keys NEVER enter this repo. This file contains no secrets by construction.

KEYS (set in the Claude environment settings, browser):
  FINNHUB_API_KEY   — US quotes, earnings calendar, news        (finnhub.io must be allowlisted)
  EODHD_API_TOKEN   — TSE/KRX closes, indices, FX               (eodhd.com allowlisted)
  DART_API_KEY      — Korea filings                             (opendart.fss.or.kr allowlisted)
  EDINET_API_KEY    — Japan filings                             (api.edinet-fss.go.jp allowlisted)
  FRED_API_KEY      — US macro series                           (api.stlouisfed.org allowlisted)

Usage: python3 research/meta/scripts/market_data.py status          (which keys/hosts are live)
       python3 research/meta/scripts/market_data.py quote AAPL      (Finnhub US quote)
       python3 research/meta/scripts/market_data.py eod 3436.TSE    (EODHD close: SUMCO)
Wake integration: `status` runs at each wake; any live key upgrades that data class from
web-chase to API pull; missing/blocked keys fall back silently to the web-chase path.
"""
import os, sys, json, glob, urllib.request, urllib.error

KEY_SPECS = {
    "FINNHUB_API_KEY": ("finnhub.io", "US quotes + earnings calendar + news"),
    "EODHD_API_TOKEN": ("eodhd.com", "TSE/KRX closes, indices, FX"),
    "DART_API_KEY": ("opendart.fss.or.kr", "Korea filings (T1)"),
    "EDINET_API_KEY": ("api.edinet-fss.go.jp", "Japan filings (T1)"),
    "FRED_API_KEY": ("api.stlouisfed.org", "US macro series"),
}
SCRATCH_FALLBACK = {"FINNHUB_API_KEY": "finnhub_candidate"}  # pre-burned pasted keys, container-local


def _scratchpad_dir():
    hits = glob.glob("/tmp/claude-*/*/*/scratchpad/keys")
    return hits[0] if hits else None


def get_key(name):
    """Env first; scratchpad pre-burned fallback second. Returns value or None. Never print the return."""
    v = os.environ.get(name)
    if v:
        return v.strip()
    sd = _scratchpad_dir()
    fb = SCRATCH_FALLBACK.get(name)
    if sd and fb and os.path.exists(os.path.join(sd, fb)):
        return open(os.path.join(sd, fb)).read().strip()
    return None


def _get(url, timeout=15):
    """Fetch URL. On ANY error, report without the URL (it may embed a key)."""
    try:
        with urllib.request.urlopen(url, timeout=timeout) as r:
            return r.read().decode(), None
    except urllib.error.HTTPError as e:
        return None, f"HTTP {e.code}"
    except Exception as e:
        return None, type(e).__name__


def status():
    print("KEY STATUS (values masked by construction):")
    for name, (host, purpose) in KEY_SPECS.items():
        src = "env" if os.environ.get(name) else ("scratchpad" if get_key(name) else None)
        if not src:
            print(f"  {name}: ABSENT — {purpose}")
            continue
        # reachability probe with the real key, output masked
        if name == "FINNHUB_API_KEY":
            body, err = _get(f"https://finnhub.io/api/v1/quote?symbol=AAPL&token={get_key(name)}")
        elif name == "EODHD_API_TOKEN":
            body, err = _get(f"https://eodhd.com/api/eod/AAPL.US?api_token={get_key(name)}&fmt=json&limit=1")
        elif name == "FRED_API_KEY":
            body, err = _get(f"https://api.stlouisfed.org/fred/series?series_id=DGS10&api_key={get_key(name)}&file_type=json")
        else:
            body, err = None, "no-probe-defined"
        blocked = err or ("denied" in (body or "").lower()[:200])
        print(f"  {name}: present ({src}) — {'LIVE' if body and not blocked else f'BLOCKED/{err or 'denied'}'} — {purpose}")


def quote(symbol):
    k = get_key("FINNHUB_API_KEY")
    if not k:
        print("FINNHUB_API_KEY absent"); return 1
    body, err = _get(f"https://finnhub.io/api/v1/quote?symbol={symbol}&token={k}")
    if err or not body:
        print(f"blocked/error: {err}"); return 1
    d = json.loads(body)
    print(json.dumps({"symbol": symbol, "current": d.get("c"), "prev_close": d.get("pc"),
                      "day_high": d.get("h"), "day_low": d.get("l")}))
    return 0


def eod(symbol):
    k = get_key("EODHD_API_TOKEN")
    if not k:
        print("EODHD_API_TOKEN absent"); return 1
    body, err = _get(f"https://eodhd.com/api/eod/{symbol}?api_token={k}&fmt=json&limit=2")
    if err or not body:
        print(f"blocked/error: {err}"); return 1
    print(body[:500])
    return 0


if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else "status"
    if cmd == "status":
        status()
    elif cmd == "quote" and len(sys.argv) > 2:
        sys.exit(quote(sys.argv[2]))
    elif cmd == "eod" and len(sys.argv) > 2:
        sys.exit(eod(sys.argv[2]))
    else:
        print(__doc__)
