#!/usr/bin/env python3
"""EDGAR client for the LLMNA research OS (built 2026-07-16).

SEC EDGAR has NO API key. Access requirements (SEC fair-access policy):
  1. Declared User-Agent with contact info  -> UA below
  2. Rate limit <= 10 req/s                 -> MIN_INTERVAL throttle
  3. Hosts: data.sec.gov (structured JSON), efts.sec.gov (full-text search),
     www.sec.gov/Archives (raw documents)

Usage (import or CLI):
  python3 edgar_client.py submissions 1046179          # TSMC recent filings
  python3 edgar_client.py facts 1046179                # XBRL company-facts
  python3 edgar_client.py fts "HBM4 capacity" --forms 6-K
  python3 edgar_client.py doc <archives-url>           # fetch one document
"""
import json, sys, time, urllib.request

UA = "LLMNA-personal-research alistairjdb@gmail.com"
MIN_INTERVAL = 0.15  # seconds between requests (~6.7 req/s < SEC's 10/s cap)
_last = [0.0]

# CIK map for tracked names (zero-padded to 10 digits at call time)
CIKS = {
    "TSM": 1046179, "SKHY": 2120882, "MU": 723125, "NVDA": 1045810,
    "ASML": 937966, "SNDK": 2023554, "ALAB": 1736946, "NET": 1477333,
    "ACMR": 1680062, "CRCL": 1876042, "NBIS": 1898627, "IBM": 51143,
}

def _get(url, binary=False):
    wait = MIN_INTERVAL - (time.time() - _last[0])
    if wait > 0:
        time.sleep(wait)
    req = urllib.request.Request(url, headers={
        "User-Agent": UA,
        "Accept-Encoding": "gzip, deflate",
        "Host": url.split("/")[2],
    })
    _last[0] = time.time()
    import gzip
    with urllib.request.urlopen(req, timeout=30) as r:
        raw = r.read()
        if r.headers.get("Content-Encoding") == "gzip":
            raw = gzip.decompress(raw)
        return raw if binary else raw.decode("utf-8", errors="replace")

def submissions(cik):
    """Recent filings index for a CIK (data.sec.gov)."""
    return json.loads(_get(f"https://data.sec.gov/submissions/CIK{int(cik):010d}.json"))

def companyfacts(cik):
    """All XBRL facts for a CIK (filing-grade numbers)."""
    return json.loads(_get(f"https://data.sec.gov/api/xbrl/companyfacts/CIK{int(cik):010d}.json"))

def fts(query, forms=None):
    """EDGAR full-text search (efts.sec.gov, same endpoint the UI calls).
    forms: optional comma-separated form filter, e.g. '6-K,8-K'."""
    from urllib.parse import quote
    url = f"https://efts.sec.gov/LATEST/search-index?q={quote(chr(34) + query + chr(34))}"
    if forms:
        url += f"&forms={quote(forms)}"
    return json.loads(_get(url))

def doc(url):
    """Fetch a raw filing document from www.sec.gov/Archives."""
    assert url.startswith("https://www.sec.gov/Archives/"), "Archives URLs only"
    return _get(url)

def recent_filings(cik, form=None, n=10):
    s = submissions(cik)
    r = s["filings"]["recent"]
    out = []
    for i in range(len(r["accessionNumber"])):
        if form and r["form"][i] != form:
            continue
        acc = r["accessionNumber"][i].replace("-", "")
        out.append({
            "form": r["form"][i], "filed": r["filingDate"][i],
            "accession": r["accessionNumber"][i],
            "primaryDoc": r["primaryDocument"][i],
            "url": f"https://www.sec.gov/Archives/edgar/data/{int(cik)}/{acc}/{r['primaryDocument'][i]}",
        })
        if len(out) >= n:
            break
    return out

if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else "help"
    if cmd == "submissions":
        cik = CIKS.get(sys.argv[2], sys.argv[2])
        for f in recent_filings(cik, form=(sys.argv[3] if len(sys.argv) > 3 else None)):
            print(f"{f['filed']}  {f['form']:8s}  {f['url']}")
    elif cmd == "facts":
        cik = CIKS.get(sys.argv[2], sys.argv[2])
        d = companyfacts(cik)
        print(d["entityName"], "| fact groups:", ", ".join(list(d.get("facts", {}).keys())))
    elif cmd == "doc":
        print(doc(sys.argv[2])[:3000])
    else:
        print(__doc__)
