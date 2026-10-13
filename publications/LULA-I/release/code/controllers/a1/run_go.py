"""Go adapter cells (third-party hashsig Go code, QPC timer patch): shrincs-go and KN4036. Serial, logical CPU 10, after
run_shrincs.py has finished. GOMAXPROCS=1 is set for every job."""
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
EXE = BUILD / 'hashsig_driver.exe'
CPU = 10
SEED = 20261014
os.environ['GOMAXPROCS'] = '1'

def load_pct():
    try:
        out = subprocess.run(['powershell', '-NoProfile', '-Command',
                              '(Get-CimInstance Win32_Processor | Measure-Object LoadPercentage -Average).Average'],
                             capture_output=True, text=True, timeout=30).stdout.strip()
        return float(out)
    except Exception:
        return None

def run(prefix, kind, scenario, n, reps, timeout):
    out, vec = RAW / f'{prefix}.csv', RAW / f'{prefix}.vec.json'
    argv = [str(EXE), 'bench', kind, str(C / 'vectors' / f'go-{kind}.json'), scenario, str(n), str(reps), str(out), str(vec)]
    b = load_pct()
    subprocess.run([sys.executable, '-B', str(RUNNER), '--cpu', str(CPU), '--timeout', str(timeout),
                    '--prefix', str(RAW / f'job-{prefix}'), '--cwd', str(C)] + argv,
                   stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    a = load_pct()
    with open(RAW / 'load-records.jsonl', 'a') as f:
        f.write(json.dumps({'prefix': prefix, 'load_before': b, 'load_after': a, 'argv': argv}) + chr(10))

def main():
    while not (RAW / 'shrincs-DONE.txt').exists():
        time.sleep(30)
    rng = random.Random(SEED)
    cells = []
    for m in (32, 1024, 65536):
        cells.append(('shrincsGo-stateful', 'shrincs', 'prepared', m, 200, 900))
        cells.append(('shrincsGo-fallback', 'shrincs', 'fallback', m, 10, 1800))
        cells.append(('kn4036-prepared', 'kn4036', 'prepared', m, 12, 3600))
    rng.shuffle(cells)
    (RAW / 'go-order.json').write_text(json.dumps({'seed': SEED, 'order': cells}, indent=1))
    for name, kind, sc, m, reps, to in cells:
        run(f'{name}-{m}', kind, sc, m, reps, to)
    for i in range(3):
        run(f'kn4036-fresh-32-{i}', 'kn4036', 'fresh', 32, 1, 900)
    run('kn4036-missing-32', 'kn4036', 'missing', 32, 2, 1800)
    (RAW / 'go-DONE.txt').write_text(time.strftime('%Y-%m-%dT%H:%M:%S'))

if __name__ == '__main__':
    main()
