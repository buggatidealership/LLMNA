#!/usr/bin/env python3
"""TWSE / TPEx open-data client for the LLMNA research OS (built 2026-07-16).

NO API key. Public JSON endpoints:
  - openapi.twse.com.tw  (TWSE main board: EMC 2383, Nanya 2408, TSMC 2330)
  - www.tpex.org.tw/openapi (TPEx/OTC board: TUC 6274)

Usage (CLI):
  python3 twse_client.py quote 2383 2408 2330     # daily close from all-market file
  python3 twse_client.py monthly 2383             # monthly revenue (上市公司每月營業收入)
  python3 twse_client.py tpex 6274                # TPEx daily close
"""
import json, sys, time, urllib.request

UA = "LLMNA-personal-research alistairjdb@gmail.com"
MIN_INTERVAL = 0.5
_last = [0.0]

TRACKED = {"2330": "TSMC", "2383": "Elite Material (CCL)", "2408": "Nanya (DRAM tell)",
           "6274": "TUC (TPEx, CCL)", "3532": "Formosa Sumco", "6488": "GlobalWafers (TPEx)"}

def _get(url, retries=2):
    wait = MIN_INTERVAL - (time.time() - _last[0])
    if wait > 0:
        time.sleep(wait)
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "application/json"})
    _last[0] = time.time()
    for attempt in range(retries + 1):
        try:
            with urllib.request.urlopen(req, timeout=30) as r:
                return json.loads(r.read().decode("utf-8"))
        except Exception:
            if attempt == retries:
                raise
            time.sleep(1.5)  # TPEx occasionally drops chunked reads (IncompleteRead) — retry heals it

def twse_daily_all():
    """All TWSE-listed daily OHLCV (previous/most recent close file)."""
    return _get("https://openapi.twse.com.tw/v1/exchangeReport/STOCK_DAY_ALL")

def twse_quotes(codes):
    data = twse_daily_all()
    want = set(codes)
    return [row for row in data if row.get("Code") in want]

def twse_monthly_revenue(codes=None):
    """Monthly revenue of listed companies (上市公司每月營業收入彙總表)."""
    data = _get("https://openapi.twse.com.tw/v1/opendata/t187ap05_L")
    if codes:
        want = set(codes)
        data = [r for r in data if r.get("公司代號") in want or r.get("Code") in want]
    return data

def tpex_daily(codes=None):
    """TPEx (OTC) daily quotes."""
    data = _get("https://www.tpex.org.tw/openapi/v1/tpex_mainboard_daily_close_quotes")
    if codes:
        want = set(codes)
        data = [r for r in data if r.get("SecuritiesCompanyCode") in want or r.get("Code") in want]
    return data

if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else "help"
    if cmd == "quote":
        for row in twse_quotes(sys.argv[2:]):
            print(json.dumps(row, ensure_ascii=False))
    elif cmd == "monthly":
        for row in twse_monthly_revenue(sys.argv[2:] or None)[:5]:
            print(json.dumps(row, ensure_ascii=False))
    elif cmd == "tpex":
        for row in tpex_daily(sys.argv[2:] or None):
            print(json.dumps(row, ensure_ascii=False))
    else:
        print(__doc__)
