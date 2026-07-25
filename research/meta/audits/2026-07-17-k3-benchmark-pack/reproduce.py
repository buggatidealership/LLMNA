#!/usr/bin/env python3
"""
LLMNA benchmark-audit reproducibility pack — frozen baseline 2026-07-18
Audited commit: d816abf1664d23a50a1927b8a6f3365c8a6939e7 (main, 2026-07-17T22:05:42Z)

USAGE (path-independent, offline — no network needed):
  python3 reproduce.py --repo /path/to/LLMNA-checkout --pack /path/to/llmna-audit-pack

  --repo   git checkout of buggatidealership/LLMNA (baseline: pinned to the commit above)
  --pack   this pack's folder (reads prices from <pack>/prices; expectations from embedded constants)

Outputs: regenerated CSVs written to ./audit-repro-out/ under the CURRENT working directory
(frozen pack files are never touched). Diff them against the pack's CSVs for receipt verification.

Expected headline outputs (see MANIFEST.txt):
  Brier 0.1978 / 0.2500 / 0.1844 / 0.1000 | TEST2 12W/7L/1T mean +1.03pp |
  TEST3 means -3.63% / -1.25% / -2.26% | 0 late registrations
Deterministic: bootstraps seeded (42 / 7).
"""
import csv, re, subprocess, math, random, statistics, os, sys, argparse
import datetime as dt
from pathlib import Path

EXPECTED_HEAD = "d816abf1664d23a50a1927b8a6f3365c8a6939e7"

ap = argparse.ArgumentParser()
ap.add_argument('--repo', required=True, help="path to the LLMNA git checkout")
ap.add_argument('--pack', required=True, help="path to this audit pack (contains prices/)")
ap.add_argument('--out', default='./audit-repro-out', help="where regenerated CSVs go (default: ./audit-repro-out)")
a = ap.parse_args()
root, PACK = Path(a.repo), Path(a.pack)
OUT = Path(a.out); OUT.mkdir(parents=True, exist_ok=True)
if not (root/'research/predictions/calibration-ledger.csv').exists():
    sys.exit(f"FATAL: {root} does not look like the LLMNA repo (missing research/predictions/calibration-ledger.csv)")
if not (PACK/'prices/NVDA.csv').exists():
    sys.exit(f"FATAL: {PACK} does not look like the audit pack (missing prices/NVDA.csv)")

def sh(args, cwd=root):
    return subprocess.run(args, capture_output=True, text=True, cwd=cwd).stdout.strip()

# ================= STEP 0 — SYNC =================
head_full = sh(['git','log','-1','--format=%H'])
head = sh(['git','log','-1','--format=%H %cI'])
ncommits = sh(['git','rev-list','--count','HEAD'])
match = "MATCH (audited baseline)" if head_full == EXPECTED_HEAD else ("AHEAD/BEHIND vs baseline — deltas are vs the frozen numbers below" if head_full else "UNKNOWN")
print(f"STEP 0 | repo HEAD = {head} | commits = {ncommits}")
print(f"STEP 0 | baseline  = {EXPECTED_HEAD} 2026-07-17T22:05:42Z | {match}")

# ================= REGISTRATION INTEGRITY =================
def git_first(rel):
    d = sh(['git','log','--diff-filter=A','--follow','--format=%cI','--',rel]).split('\n')
    return d[-1] if d and d[0] else None
def git_all(rel):
    return sh(['git','log','--follow','--format=%cI','--',rel]).split('\n')

pred = sorted((root/'research/predictions').glob('2026-*.md'))
EDIT_NOTES = {
 '2026-06-03-AVGO-Q2FY26.md':'addendum ~8h post-print, 11min pre-grade-commit; registered numbers UNCHANGED (P=70 kept)',
 '2026-06-12-KIOXIA-VLSI-symposium-pre-registration.md':'Day3-4 monitoring append during multi-day event; registered numbers unchanged',
 '2026-07-02-AI-supplychain-earnings-program.md':'ASMPT P2 slot added; umbrella file',
 '2026-07-02-KIOXIA-Q1FY27-earnings-prediction.md':'TrendForce note appended pre-resolution (print Aug-7); numbers unchanged',
 '2026-07-02-SAMSUNG-Q2-prelim-earnings-prediction.md':'SUPERSEDED banner added eve of print; duplicate-registration disambiguation — PROCESS FLAG',
 '2026-07-02-SAMSUNG-Q2-prelim-prediction.md':'4 pre-print commits incl. consensus-vintage addenda; canonical file; numbers registered Jul-2',
 '2026-07-02-SNDK-Q4FY26-earnings-prediction.md':'TrendForce note appended pre-resolution (print Aug-5); numbers unchanged'}
late = 0
with open(OUT/'registration_integrity.csv','w',newline='') as f:
    w = csv.writer(f); w.writerow(['file','event_date','first_commit','verdict','post_event_commits','post_event_edit_assessment'])
    for p in pred:
        rel = str(p.relative_to(root)); m = re.match(r'(2026-\d\d-\d\d)-', p.name)
        ev = m.group(1) if m else '?'; fc = git_first(rel)
        ok = 'GRADE' in p.name or (fc and fc[:10] <= ev)
        if not ok: late += 1; print(f"  LATE REGISTRATION: {p.name} event={ev} first_commit={fc}")
        later = [c for c in git_all(rel) if c[:10] > ev]
        w.writerow([p.name, ev, fc, 'OK (grade file — post-event by design)' if 'GRADE' in p.name else ('OK' if ok else 'LATE'), len(later), EDIT_NOTES.get(p.name,'')])
print(f"INTEGRITY | {len(pred)} prediction artifacts checked | late registrations: {late}")

# ================= TEST 1 — CALIBRATION vs CHANCE =================
df = list(csv.DictReader(open(root/'research/predictions/calibration-ledger.csv')))
def P(r):
    try: return float(r['claimed_p'])/100
    except: return None
binary = [r for r in df if r['outcome'] in ('TRUE','FALSE') and P(r) is not None]
mixed  = [r for r in df if r['outcome'] == 'MIXED' and P(r) is not None]
parrot = [r for r in binary if re.search(r'consensus|guide|whisper|beat', r['component'])]
def brier(rows, f): return sum((f(r)-(1 if r['outcome']=='TRUE' else 0))**2 for r in rows)/len(rows)
base = sum(1 for r in binary if r['outcome']=='TRUE')/len(binary)
print(f"\nTEST 1 | binary n={len(binary)} (MIXED n={len(mixed)} excluded from primary)")
print(f"  Brier system    {brier(binary,P):.4f}")
print(f"  Brier coin      {brier(binary,lambda r:0.5):.4f}")
print(f"  Brier base-rate {brier(binary,lambda r:base):.4f}  (base={base:.3f})")
print(f"  Brier parrot P=.80 (n={len(parrot)}) {brier(parrot,lambda r:0.8):.4f} | system on same rows {brier(parrot,P):.4f}")

def boot(rows, fA, fB, n=10000, seed=42):
    rng = random.Random(seed); idx = list(range(len(rows))); d = []
    for _ in range(n):
        s = [rows[rng.choice(idx)] for _ in idx]
        d.append(brier(s,fA)-brier(s,fB))
    d.sort(); return sum(d)/n, d[int(.025*n)], d[int(.975*n)], sum(1 for x in d if x<0)/n
for name, rows, fB in [("vs coin", binary, lambda r:0.5), ("vs base", binary, lambda r:base), ("vs parrot", parrot, lambda r:0.8)]:
    m,lo,hi,pb = boot(rows,P,fB)
    print(f"  bootstrap {name}: D={m:+.4f} 95%CI[{lo:+.4f},{hi:+.4f}] P(sys better)={pb:.3f}")
print("  calibration curve (binary):")
for lo,hi in [(0,.3),(.3,.5),(.5,.7),(.7,.9),(.9,1.01)]:
    br = [r for r in binary if lo <= P(r) < hi]
    if br:
        rf = sum(1 for r in br if r['outcome']=='TRUE')/len(br)
        print(f"    [{lo:.1f},{min(hi,1.0):.1f}) n={len(br):2d} claimed={sum(P(r) for r in br)/len(br):.3f} realized={rf:.3f} SE={math.sqrt(rf*(1-rf)/len(br)):.3f}")

with open(OUT/'test1_binary_rows.csv','w',newline='') as f:
    w = csv.writer(f)
    w.writerow(['include','exclude_reason','date_graded','prediction_id','ticker','component','claimed_p','outcome','layer_failed','parrot_row','notes'])
    for r in binary:
        w.writerow(['YES','',r['date_graded'],r['prediction_id'],r['ticker'],r['component'],r['claimed_p'],r['outcome'],r['layer_failed'],'YES' if r in parrot else '',r['notes']])
    for r in mixed:
        w.writerow(['NO','MIXED outcome — excluded from primary (binary-only) run; scored as 0.5 in sensitivity run',r['date_graded'],r['prediction_id'],r['ticker'],r['component'],r['claimed_p'],r['outcome'],r['layer_failed'],'YES' if r in parrot else '',r['notes']])

# ================= TEST 2 — POINT ESTIMATES vs STREET =================
ROWS2 = [
 ("NVDA","revenue",81.6,82.0,78.8,"pred-file table"),("NVDA","eps",1.88,1.87,1.77,"pred-file table"),
 ("NVDA","gm%",75.4,74.9,74.5,"pred-file table"),("NVDA","datacenter",75.2,81.0,None,"—"),
 ("NVDA","q2-guide",91.0,88.5,86.0,"pred-file: street 85-87 mid"),("MOD","revenue",954.4,940,920.7,"grade-file"),
 ("MOD","eps",1.71,1.55,1.57,"grade-file (repo=range mid)"),("MOD","cs-margin%",20.0,18.7,None,"—"),
 ("MOD","blended-margin%",15.3,13.8,None,"—"),("SNOW","product-rev",1.330,1.275,1.265,"grade-file"),
 ("SNOW","nrr%",126,124,None,"—"),("MRVL","revenue",2.418,2.470,2.410,"grade-file"),
 ("MRVL","eps",0.80,0.82,0.795,"grade-file: consensus 0.79-0.80"),("MRVL","dc-yoy%",27,44.5,None,"—"),
 ("MRVL","q2-guide",2.700,2.65,2.60,"pred-file street-INFERENCE (soft)"),("HPE","revenue",10.7,9.95,9.77,"grade-file"),
 ("HPE","eps",0.79,0.57,0.53,"grade-file"),("HPE","ai-backlog",5.9,8.0,None,"—"),
 ("AVGO","revenue",22.187,22.5,22.08,"pred-file (repo=band mid)"),("AVGO","eps",2.44,2.50,2.39,"pred-file (repo=band mid)"),
 ("AVGO","q3-guide",29.4,23.4,None,"—"),("MU","q4-guide",50.0,40.0,40.0,"street≈repo range (NO independent edge)"),
 ("005930","op",89.4,92,84.58,"FnGuide via pred-file addendum"),("005930","revenue",171,178,None,"—"),
 ("ASML","revenue",9.3,8.95,9.04,"pred-file: LSEG consensus"),("ASML","eps",7.59,8.20,8.00,"pred-file: ~7.98-8.03"),
 ("TSMC","revenue",39.62,40.1,38.1,"pred-file"),("TSMC","eps",4.31,3.90,3.80,"pred-file: ~US$3.8")]
w=l=t=u=0; deltas=[]
with open(OUT/'test2_point_estimates.csv','w',newline='') as f:
    wr = csv.writer(f)
    wr.writerow(['ticker','metric','actual','repo_estimate','street','street_source','repo_abs_err_pct','street_abs_err_pct','verdict','error_delta_pp(street-repo)'])
    for tk,m,act,rp,st,src in ROWS2:
        re_ = abs(rp-act)/act*100
        if st is None:
            u += 1; wr.writerow([tk,m,act,rp,'',src,f'{re_:.2f}','','UNSOURCED-STREET','']); continue
        se = abs(st-act)/act*100
        v = "REPO" if re_<se-0.05 else ("STREET" if se<re_-0.05 else "TIE")
        w,l,t = w+(v=="REPO"), l+(v=="STREET"), t+(v=="TIE")
        deltas.append(se-re_)
        wr.writerow([tk,m,act,rp,st,src,f'{re_:.2f}',f'{se:.2f}',v,f'{se-re_:+.2f}'])
rng = random.Random(7); boots = sorted(sum(rng.choice(deltas) for _ in deltas)/len(deltas) for _ in range(10000))
print(f"\nTEST 2 | sourced rows={w+l+t} unsourced-street={u} | REPO {w} / STREET {l} / TIE {t}")
print(f"  win-rate ex-tie {w}/{w+l} | mean D {statistics.mean(deltas):+.2f}pp | median {statistics.median(deltas):+.2f}pp")
print(f"  bootstrap meanD 95%CI [{boots[250]:+.2f},{boots[9750]:+.2f}] P(D>0)={sum(1 for b in boots if b>0)/10000:.3f}")

# ================= TEST 3 — ECONOMIC VALUE vs BENCHMARK =================
def load(fp): return {r['Date'][:10]: float(r['Close']) for r in csv.DictReader(open(fp))}
tickmap={"NVDA":"NVDA","MOD":"MOD","SNOW":"SNOW","MRVL":"MRVL","HPE":"HPE","AVGO":"AVGO","MU":"MU",
         "NBIS":"NBIS","ASML":"ASML","TSM":"TSM","SOXX":"SOXX","QQQ":"QQQ","005930.KS":"005930_KS"}
px = {t: load(PACK/'prices'/f'{o}.csv') for t,o in tickmap.items()}
def coa(t,d):
    ks = sorted(k for k in px[t] if k>=d); return (ks[0],px[t][ks[0]]) if ks else (None,None)
def cob(t,d):
    ks = sorted(k for k in px[t] if k<=d); return (ks[-1],px[t][ks[-1]]) if ks else (None,None)
TRADES = [("NVDA","2026-05-20","NVDA Q1 beat call"),("MOD","2026-05-26","MOD Q4 beat call"),
          ("SNOW","2026-05-27","SNOW Q1 beat call"),("MRVL","2026-05-27","MRVL Q1 beat call"),
          ("HPE","2026-05-29","HPE Q2 beat call"),("AVGO","2026-06-03","AVGO Q2 beat + T+24h +11-13% stance"),
          ("MU","2026-06-23","MU beat-modal call (day before print)"),("NBIS","2026-06-19","NBIS inclusion-reaction pre-registration"),
          ("005930.KS","2026-07-02","Samsung prelim OP-beat call"),("ASML","2026-07-02","ASML Q2 call"),
          ("TSM","2026-07-02","TSMC Q2 call")]
res=[]
print("\nTEST 3 | rule: LONG at registration close -> +30d close, equal weight; SOXX/QQQ matched windows")
with open(OUT/'test3_trade_windows.csv','w',newline='') as f:
    wr = csv.writer(f)
    wr.writerow(['ticker','registration_date','direction','entry_date','entry_close','exit_date','exit_close','days_held','truncated','trade_ret_pct','soxx_ret_pct','qqq_ret_pct','beats_soxx','note'])
    for tk,d,note in TRADES:
        ed,ep = coa(tk,d)
        xd0 = (dt.date.fromisoformat(ed)+dt.timedelta(days=30)).isoformat()
        xd,xp = cob(tk,xd0)
        r  = (xp/ep-1)*100
        rs = (cob("SOXX",xd)[1]/coa("SOXX",d)[1]-1)*100
        rq = (cob("QQQ",xd)[1]/coa("QQQ",d)[1]-1)*100
        nd = (dt.date.fromisoformat(xd)-dt.date.fromisoformat(ed)).days
        res.append((r,rs,rq))
        wr.writerow([tk,d,'LONG',ed,f'{ep:.2f}',xd,f'{xp:.2f}',nd,'YES' if nd<28 else '',f'{r:+.2f}',f'{rs:+.2f}',f'{rq:+.2f}','YES' if r>rs else 'NO',note])
        print(f"  {tk:10s} {ed}@{ep:>9.2f} -> {xd}@{xp:>9.2f}  {r:+6.2f}% | SOXX {rs:+6.2f}% | QQQ {rq:+6.2f}%")
print(f"  MEAN {statistics.mean(x[0] for x in res):+.2f}% | SOXX {statistics.mean(x[1] for x in res):+.2f}% | QQQ {statistics.mean(x[2] for x in res):+.2f}% | beats SOXX {sum(1 for x in res if x[0]>x[1])}/{len(res)}")
print("  coverage: 11/22 registration artifacts (50%) — no extrapolation (audit rule)")

print("\nTEST 4 | see pack test4_selection_integrity.md (static evidence; 83% confirmed / 71% incl-ambiguous)")
print("TEST 5 | see pack test5_overrides.csv (4/4 exposure-reducing overrides vindicated; SKHY -11.2%)")
print(f"\nDONE — regenerated CSVs in {OUT.resolve()} — diff against pack for receipt verification")
