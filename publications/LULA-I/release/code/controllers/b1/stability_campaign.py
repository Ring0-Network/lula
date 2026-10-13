"""Stability campaign b1 controller. Strictly serial, logical CPU 10, BelowNormal, 2.75 GiB (bounded_run.py).
Requires the sampler (code/controllers/b1/sampler.py) to be running and vectors/lula1-key2.cache to exist (prepared on logical 8).
See PROTOCOL.md. Its gate log records passes, each twentieth populated failure, and gate timeouts: raw/gate.jsonl, raw/b*-*.process.json (every job)."""
import csv, datetime as dt, json, random, subprocess, sys, time
from pathlib import Path

from release_paths import CODE, RELEASE, campaign, results, build
S = campaign('b1', rerun=True)
RESULTS = results('b1')
BUILD = build()
(S / 'raw').mkdir(parents=True, exist_ok=True)
(S / 'vectors').mkdir(parents=True, exist_ok=True)
RAW = S / 'raw'
RUNNER = Path(__file__).with_name('bounded_run.py')
CACHE1 = RELEASE / 'reruns' / 'a1' / 'vectors' / 'lula1.cache'
CACHE2 = S / 'vectors' / 'lula1-key2.cache'
RA = BUILD / 'lula1_driver_original.exe'      # key 1 (original fixture)
RAK = BUILD / 'lula1_driver_seeded.exe'      # key 2 loads its seed from the fixture file
SL = BUILD / 'slhdsa_ossl.exe'
CPU, SEED = 10, 20261012
BLOCKS, GAP_S, GATE_WAIT_S = 6, 180, 25 * 60
THR = dict(total=30.0, c10=8.0, c11=8.0)

def now():
    return dt.datetime.now(dt.timezone.utc)

def sampler_rows(seconds):
    rows = []
    try:
        with open(RAW / 'sampler.csv', encoding='ascii', errors='ignore') as f:
            lines = f.readlines()[-60:]
    except FileNotFoundError:
        return rows
    cut = now() - dt.timedelta(seconds=seconds)
    for ln in lines[1:]:
        p = ln.strip().split(',')
        try:
            t = dt.datetime.fromisoformat(p[0].replace('Z', '+00:00'))
            if t >= cut:
                rows.append((t, float(p[1]), float(p[2]), float(p[3])))
        except Exception:
            continue
    return rows

def gate(label):
    t0 = time.time(); tries = 0
    while True:
        rows = sampler_rows(20)
        if len(rows) >= 3:
            m = [sum(r[i] for r in rows) / len(rows) for i in (1, 2, 3)]
            ok = m[0] <= THR['total'] and m[1] <= THR['c10'] and m[2] <= THR['c11']
            tries += 1
            if ok or tries % 20 == 0:
                with open(RAW / 'gate.jsonl', 'a') as f:
                    f.write(json.dumps({'utc': now().isoformat(), 'job': label, 'pass': ok, 'total': round(m[0], 1),
                                        'c10': round(m[1], 1), 'c11': round(m[2], 1), 'rows': len(rows),
                                        'waited_s': round(time.time() - t0)}) + '\n')
            if ok:
                return True
        if time.time() - t0 > GATE_WAIT_S:
            with open(RAW / 'gate.jsonl', 'a') as f:
                f.write(json.dumps({'utc': now().isoformat(), 'job': label, 'pass': False, 'gate_timeout': True}) + '\n')
            return False
        time.sleep(3)

def run(prefix, argv, timeout):
    if not gate(prefix):
        return None
    subprocess.run([sys.executable, '-B', str(RUNNER), '--cpu', str(CPU), '--timeout', str(timeout),
                    '--prefix', str(RAW / prefix), '--cwd', str(S)] + [str(a) for a in argv],
                   stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    return True

def lula(prefix, key, scenario, msg, reps, timeout):
    exe, cache = (RA, CACHE1) if key == 1 else (RAK, CACHE2)
    return run(prefix, [exe, 'run', 'lula1', cache, scenario, msg, reps, RAW / f'{prefix}.csv', RAW / f'{prefix}.vec.txt'], timeout)

def main():
    while not CACHE2.exists():
        time.sleep(30)
    # key 2 preparation must have exited
    while subprocess.run(['tasklist', '/FI', 'IMAGENAME eq lula1_driver_seeded.exe'], capture_output=True, text=True).stdout.count('lula1_driver_seeded.exe'):
        time.sleep(20)
    (RAW / 'campaign-START.txt').write_text(now().isoformat())
    for b in range(1, BLOCKS + 1):
        key = 1 if b % 2 else 2
        jobs = []
        for m in (32, 1024, 65536):
            jobs.append(('lula', f'b{b}-lula-k{key}-{m}', m))
            jobs.append(('f', f'b{b}-slh128f-{m}', m))
            jobs.append(('s', f'b{b}-slh128s-{m}', m))
        random.Random(SEED + b).shuffle(jobs)
        (RAW / f'b{b}-order.json').write_text(json.dumps({'seed': SEED + b, 'key': key, 'order': [j[1] for j in jobs]}))
        for kind, prefix, m in jobs:
            if kind == 'lula':
                lula(prefix, key, 'prepared', m, 1000, 1800)
            elif kind == 'f':
                run(prefix, [SL, 'SLH-DSA-SHA2-128f', m, 1000, RAW / f'{prefix}.csv'], 900)
            else:
                run(prefix, [SL, 'SLH-DSA-SHA2-128s', m, 200, RAW / f'{prefix}.csv'], 1800)
        time.sleep(GAP_S)
    for w in range(1, 4):                       # fresh-process series and one independent cache-loss process per window
        for i in range(5):
            lula(f'w{w}-fresh-{i}', 1, 'fresh', 32, 1, 900)
        lula(f'w{w}-cacheloss', 1, 'missing', 32, 1, 2400)
        time.sleep(GAP_S)
    (RAW / 'campaign-DONE.txt').write_text(now().isoformat())
    (RAW / 'sampler.stop').write_text('stop')

if __name__ == '__main__':
    main()
