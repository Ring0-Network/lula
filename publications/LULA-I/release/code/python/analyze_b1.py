"""Analyze the stability campaign b1 (see PROTOCOL.md). Reads raw/*.csv, raw/*.process.json, raw/sampler.csv.
Writes results/stability_by_job.csv, results/stability_by_cell.csv and results/STABILITY-FINDINGS.md.
The header of the findings file says STATUS: COMPLETE only if raw/campaign-DONE.txt exists."""
import csv, datetime as dt, json, math, re, statistics
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
S = ROOT / 'data/b1'
RAW, RES = S / 'raw', ROOT / 'recomputed/b1'
RES.mkdir(parents=True, exist_ok=True)

def parse_utc(x):
    return dt.datetime.fromisoformat(x.replace('Z', '+00:00')) if x.endswith('Z') else dt.datetime.fromisoformat(x)

def nr(v, q):
    s = sorted(v)
    return s[max(0, math.ceil(q * len(s)) - 1)]

def med(v):
    return statistics.median(v)

# sampler
samples = []
try:
    with open(RAW / 'sampler.csv', encoding='ascii', errors='ignore') as f:
        next(f)
        for ln in f:
            p = ln.rstrip('\n').split(',', 5)
            try:
                samples.append((parse_utc(p[0]), float(p[1]), float(p[2]), float(p[3]), float(p[4] or 0)))
            except Exception:
                pass
except FileNotFoundError:
    pass
samples.sort()

def sampler_stats(t0, t1):
    rows = [r for r in samples if t0 <= r[0] <= t1]
    if not rows:
        return None
    n = len(rows)
    return {'rows': n, 'total_mean': sum(r[1] for r in rows) / n, 'c10_mean': sum(r[2] for r in rows) / n,
            'c11_mean': sum(r[3] for r in rows) / n, 'c11_max': max(r[3] for r in rows),
            'freq10_mean': sum(r[4] for r in rows) / n}

jobs = []
for pj in sorted(RAW.glob('*.process.json')):
    name = pj.name[:-len('.process.json')]
    m = re.match(r'^b(\d+)-(lula)-k(\d)-(\d+)$', name) or re.match(r'^b(\d+)-(slh128[fs])-(\d+)$', name)
    w = re.match(r'^w(\d+)-(fresh)-(\d+)$', name) or re.match(r'^w(\d+)-(cacheloss)$', name)
    if not (m or w):
        continue
    meta = json.loads(pj.read_text())
    csvp = RAW / f'{name}.csv'
    if meta.get('status') != 'completed' or meta.get('exit_code') != 0 or not csvp.exists():
        jobs.append({'job': name, 'status': meta.get('status'), 'exit': meta.get('exit_code')})
        continue
    if m:
        block = int(m.group(1)); alg = m.group(2)
        key = int(m.group(3)) if alg == 'lula' else 0
        msg = int(m.group(4)) if alg == 'lula' else int(m.group(3))
    else:
        block = int(w.group(1)); alg = w.group(2); key = 1; msg = 32
    ops = defaultdict(list)
    with open(csvp, encoding='utf-8') as f:
        for r in csv.DictReader(f):
            op = r.get('operation'); ns = r.get('ns', r.get('elapsed_ns'))
            if op in ('sign', 'verify', 'fixture_load') and ns not in (None, ''):
                ops[op].append(int(ns))
    t0, t1 = parse_utc(meta['start_utc']), parse_utc(meta['end_utc'])
    ss = sampler_stats(t0, t1)
    contaminated = ss is None or ss['rows'] < 3 or ss['c11_mean'] > 15 or ss['total_mean'] > 45
    jobs.append({'job': name, 'status': 'completed', 'exit': 0, 'block': block, 'alg': alg, 'key': key, 'msg': msg,
                 'start': meta['start_utc'], 'end': meta['end_utc'], 'wall_s': round(meta.get('wall_seconds', 0), 2),
                 'ops': dict(ops), 'sampler': ss, 'contaminated': contaminated,
                 'peak_ws': meta.get('peak_working_set_bytes')})

def stats(v):
    return {'N': len(v), 'min': min(v) / 1e6, 'median': med(v) / 1e6, 'p95': nr(v, .95) / 1e6, 'p99': nr(v, .99) / 1e6,
            'max': max(v) / 1e6}

with open(RES / 'stability_by_job.csv', 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['job', 'alg', 'key', 'msg', 'block', 'op', 'N', 'min_ms', 'median_ms', 'p95_ms', 'p99_ms', 'max_ms', 'wall_s',
                'sampler_rows', 'total_mean', 'c10_mean', 'c11_mean', 'c11_max', 'freq10_mean', 'contaminated'])
    for j in jobs:
        if j.get('status') != 'completed':
            w.writerow([j['job'], '', '', '', '', 'FAILED/INCOMPLETE:' + str(j.get('status')) + ':' + str(j.get('exit'))])
            continue
        ss = j['sampler'] or {}
        for op, v in j['ops'].items():
            st = stats(v)
            w.writerow([j['job'], j['alg'], j['key'], j['msg'], j['block'], op, st['N'], f"{st['min']:.4f}", f"{st['median']:.4f}",
                        f"{st['p95']:.4f}", f"{st['p99']:.4f}", f"{st['max']:.4f}", j['wall_s'], ss.get('rows'),
                        f"{ss.get('total_mean', 0):.1f}", f"{ss.get('c10_mean', 0):.1f}", f"{ss.get('c11_mean', 0):.1f}",
                        f"{ss.get('c11_max', 0):.0f}", f"{ss.get('freq10_mean', 0):.0f}", j['contaminated']])

# cells: pooled over blocks (and keys for LULA)
cells = defaultdict(list)
for j in jobs:
    if j.get('status') != 'completed' or j['alg'] in ('fresh', 'cacheloss'):
        continue
    for op in ('sign', 'verify'):
        if op in j['ops']:
            cells[(j['alg'], j['msg'], op)].append(j)

rows = []
for (alg, msg, op), js in sorted(cells.items()):
    clean = [j for j in js if not j['contaminated']]
    bmeds = [med(j['ops'][op]) / 1e6 for j in clean]
    allm = [med(j['ops'][op]) / 1e6 for j in js]
    pooled = [x for j in clean for x in j['ops'][op]]
    verdict = 'inconclusive'
    spread = cv = ratio = None
    if len(clean) >= 4:
        mean = sum(bmeds) / len(bmeds)
        spread = (max(bmeds) - min(bmeds)) / mean
        cv = statistics.pstdev(bmeds) / mean
        ratio = max((nr(j['ops'][op], .99) / med(j['ops'][op])) for j in clean)
        verdict = 'stable' if (spread <= 0.05 and ratio <= 3.0) else 'unstable'
    keyeff = ''
    if alg == 'lula' and clean:
        k1 = [med(j['ops'][op]) / 1e6 for j in clean if j['key'] == 1]
        k2 = [med(j['ops'][op]) / 1e6 for j in clean if j['key'] == 2]
        if k1 and k2:
            keyeff = f"{abs(med(k1) - med(k2)) / ((med(k1) + med(k2)) / 2):.3f}"
    pst = stats(pooled) if pooled else None
    rows.append({'alg': alg, 'msg': msg, 'op': op, 'blocks_total': len(js), 'blocks_clean': len(clean), 'verdict': verdict,
                 'block_median_min': min(bmeds) if bmeds else None, 'block_median_max': max(bmeds) if bmeds else None,
                 'spread': spread, 'cv': cv, 'p99_over_median_max': ratio, 'key_effect': keyeff, 'pooled': pst,
                 'all_block_median_range': (min(allm), max(allm)) if allm else None})

with open(RES / 'stability_by_cell.csv', 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['alg', 'msg', 'op', 'blocks_total', 'blocks_clean', 'verdict', 'block_median_min_ms', 'block_median_max_ms',
                'spread_over_mean', 'cv_block_medians', 'max_p99_over_median', 'key_effect', 'pooledN', 'pooled_median_ms',
                'pooled_p95_ms', 'pooled_p99_ms', 'pooled_max_ms'])
    for r in rows:
        p = r['pooled'] or {}
        fm = lambda x, d=4: '' if x is None else f'{x:.{d}f}'
        w.writerow([r['alg'], r['msg'], r['op'], r['blocks_total'], r['blocks_clean'], r['verdict'], fm(r['block_median_min']),
                    fm(r['block_median_max']), fm(r['spread'], 3), fm(r['cv'], 3), fm(r['p99_over_median_max'], 2),
                    r['key_effect'], p.get('N', ''), fm(p.get('median')), fm(p.get('p95')), fm(p.get('p99')), fm(p.get('max'))])

# fresh / cache loss
fresh = [j for j in jobs if j.get('status') == 'completed' and j['alg'] == 'fresh' and not j['contaminated']]
loss = [j for j in jobs if j.get('status') == 'completed' and j['alg'] == 'cacheloss']
done = (RAW / 'campaign-DONE.txt').exists()
gate = []
try:
    gate = [json.loads(x) for x in open(RAW / 'gate.jsonl')]
except FileNotFoundError:
    pass
timeouts = sum(1 for g in gate if g.get('gate_timeout'))
failed = [j['job'] for j in jobs if j.get('status') != 'completed']
cont = [j['job'] for j in jobs if j.get('status') == 'completed' and j['contaminated']]

L = []
L.append(f"STATUS: {'COMPLETE' if done else 'PARTIAL (campaign still running or interrupted)'}")
L.append('')
L.append('# Stability findings, campaign b1')
L.append('')
L.append(f"Generated {(RAW / 'campaign-DONE.txt').read_text().strip()}. Protocol: `PROTOCOL.md` (including Amendment 1). "
         'Times are elapsed milliseconds unless stated; the maximum is the maximum observed latency, not a bound.')
L.append('')
L.append(f"Jobs completed: {sum(1 for j in jobs if j.get('status') == 'completed')}; failed or incomplete: {len(failed)}; "
         f"contaminated (kept, flagged, excluded from verdicts): {len(cont)}; gate timeouts: {timeouts}.")
if failed:
    L.append('Failed/incomplete jobs: ' + ', '.join(failed))
if cont:
    L.append('Contaminated jobs: ' + ', '.join(cont))
L.append('')
L.append('## Per-cell stability (blocks pooled; LULA I uses two keys, 3 blocks each)')
L.append('')
L.append('| Cell | Op | Clean blocks / total | Verdict | Block medians min–max (ms) | Spread/mean | Max p99/median | Key effect | Pooled N | Pooled median / p95 / p99 / max (ms) |')
L.append('|---|---|---|---|---|---|---|---|---|---|')
names = {'lula': 'LULA I prepared', 'slh128f': 'SLH-DSA-128f', 'slh128s': 'SLH-DSA-128s'}
for r in rows:
    p = r['pooled'] or {}
    lab = f"{names[r['alg']]} {r['msg']} B"
    bm = f"{r['block_median_min']:.3f}–{r['block_median_max']:.3f}" if r['block_median_min'] is not None else 'n/a'
    sp = f"{100 * r['spread']:.1f} %" if r['spread'] is not None else 'n/a'
    rt = f"{r['p99_over_median_max']:.2f}" if r['p99_over_median_max'] is not None else 'n/a'
    pooled = f"{p['median']:.3f} / {p['p95']:.3f} / {p['p99']:.3f} / {p['max']:.3f}" if p else 'n/a'
    L.append(f"| {lab} | {r['op']} | {r['blocks_clean']}/{r['blocks_total']} | {r['verdict']} | {bm} | {sp} | {rt} | {r['key_effect'] or 'n/a'} | {p.get('N', '')} | {pooled} |")
L.append('')
L.append('## Fresh process and cache loss (LULA I key 1, 32 B)')
L.append('')
if fresh:
    lo = [j['ops']['fixture_load'][0] / 1e9 for j in fresh if 'fixture_load' in j['ops']]
    fs = [j['ops']['sign'][0] / 1e9 for j in fresh if 'sign' in j['ops']]
    pair = [a + b for a, b in zip(lo, fs)]
    L.append(f"- Fresh process, clean jobs N = {len(fresh)} (windows: {sorted({j['block'] for j in fresh})}): load median {med(lo):.3f} s "
             f"(range {min(lo):.3f}–{max(lo):.3f}); first sign median {med(fs) * 1000:.3f} ms; paired load plus first sign median {med(pair):.3f} s "
             f"(range {min(pair):.3f}–{max(pair):.3f}).")
else:
    L.append('- Fresh process: no clean job yet.')
if loss:
    ls = [(j['block'], j['ops']['sign'][0] / 1e9, j['contaminated']) for j in loss if 'sign' in j['ops']]
    L.append('- Cache loss, one first signature per independent process: ' + '; '.join(f"window {b}: {s:.3f} s{' (contaminated)' if c else ''}" for b, s, c in ls)
             + '. Each value is a single observation; three observations do not support a distribution estimate.')
else:
    L.append('- Cache loss: no completed process yet.')
L.append('')
L.append('## Reading this file')
L.append('- *stable* / *unstable* / *inconclusive* are defined in `PROTOCOL.md`; a cell is judged on uncontaminated blocks only.')
L.append('- *Key effect* is |median(key 1 blocks) − median(key 2 blocks)| over their mean, LULA I only.')
L.append('- Nothing here is a worst-case guarantee, a security-normalized ranking, or a statement about other machines.')
(RES / 'STABILITY-FINDINGS.md').write_text('\n'.join(L) + '\n', encoding='utf-8')
print('\n'.join(L[:12]))
