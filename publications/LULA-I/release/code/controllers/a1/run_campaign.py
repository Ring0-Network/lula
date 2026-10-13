"""Serial benchmark campaign for the LULA I comparison. One job at a time through bounded_run.py (logical CPU 10,
BelowNormal, 2.75 GiB, timeout). Waits for the LULA I cache preparation to finish first. Cell order is shuffled with a
recorded seed. Machine load (Win32 LoadPercentage) is sampled before and after every job."""
import json, os, random, subprocess, sys, time
from pathlib import Path

from release_paths import CODE, RELEASE, campaign, results, build
C = campaign('a1', rerun=True)
RESULTS = results('a1')
BUILD = build()
(C / 'raw').mkdir(parents=True, exist_ok=True)
(C / 'vectors').mkdir(parents=True, exist_ok=True)
RAW = C / 'raw'
RUNNER = Path(__file__).with_name('bounded_run.py')
RA = BUILD / 'lula1_driver_original.exe'
SL = BUILD / 'slhdsa_ossl.exe'
CACHE = C / 'vectors' / 'lula1.cache'
CPU = 10
SEED = 20261012
LOG = RAW / 'campaign-order.json'

def load_pct():
    try:
        out = subprocess.run(['powershell', '-NoProfile', '-Command',
                              '(Get-CimInstance Win32_Processor | Measure-Object LoadPercentage -Average).Average'],
                             capture_output=True, text=True, timeout=30).stdout.strip()
        return float(out)
    except Exception:
        return None

def run(prefix, argv, timeout):
    before = load_pct()
    cmd = [sys.executable, '-B', str(RUNNER), '--cpu', str(CPU), '--timeout', str(timeout),
           '--prefix', str(RAW / prefix), '--cwd', str(C)] + [str(a) for a in argv]
    t = time.time()
    subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    after = load_pct()
    rec = {'prefix': prefix, 'load_before': before, 'load_after': after, 'wall_s_outer': round(time.time() - t, 2),
           'argv': [str(a) for a in argv]}
    with open(RAW / 'load-records.jsonl', 'a') as f:
        f.write(json.dumps(rec) + '\n')
    return rec

def wait_prepare():
    while subprocess.run(['tasklist', '/FI', 'IMAGENAME eq lula1_driver_original.exe'], capture_output=True, text=True).stdout.count('lula1_driver_original.exe'):
        time.sleep(15)

def main():
    wait_prepare()
    if not CACHE.exists():
        (RAW / 'campaign-ABORT.txt').write_text('preparation finished without a cache file; see lula1-full-prepare.*\n')
        return
    rng = random.Random(SEED)
    cells = []
    for m in (32, 1024, 65536):
        cells.append(('slh128f', m, [SL, 'SLH-DSA-SHA2-128f', m, 1000, RAW / f'slh128f-{m}.csv'], 600))
        cells.append(('slh128s', m, [SL, 'SLH-DSA-SHA2-128s', m, 100, RAW / f'slh128s-{m}.csv'], 1800))
        cells.append(('lula1-hot', m, [RA, 'run', 'lula1', CACHE, 'prepared', m, 1000, RAW / f'lula1-hot-{m}.csv',
                                       RAW / f'lula1-hot-{m}.vec.txt'], 1800))
    rng.shuffle(cells)
    order = [{'cell': c[0], 'msg': c[1]} for c in cells]
    # fresh-process first signature with the persisted cache: 10 separate processes, 32 B, 1 signature each
    fresh = [('lula1-fresh', 32, [RA, 'run', 'lula1', CACHE, 'fresh', 32, 1, RAW / f'lula1-fresh-32-{i}.csv',
                                   RAW / f'lula1-fresh-32-{i}.vec.txt'], 900) for i in range(10)]
    LOG.write_text(json.dumps({'seed': SEED, 'hot_order': order, 'fresh_runs': len(fresh)}, indent=1))
    for name, m, argv, to in cells:
        run(f'job-{name}-{m}', argv, to)
    for i, (name, m, argv, to) in enumerate(fresh):
        run(f'job-{name}-{m}-{i}', argv, to)
    # total cache loss: 2 signatures in one process, N = 1 process (about 12 min each if nothing re-warms)
    run('job-lula1-missing-32', [RA, 'run', 'lula1', CACHE, 'missing', 32, 2, RAW / 'lula1-missing-32.csv',
                                 RAW / 'lula1-missing-32.vec.txt'], 7200)
    (RAW / 'campaign-DONE.txt').write_text(time.strftime('%Y-%m-%dT%H:%M:%S'))

if __name__ == '__main__':
    main()
