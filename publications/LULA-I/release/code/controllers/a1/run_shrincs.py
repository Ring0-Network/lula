"""SHRINCS author-C (B32 parameters) cells, serial, logical CPU 10. Starts after run_campaign.py has finished.
Uses the state file generated once by `build/shrincs-c-b32.exe prepare` (vectors/shrincs-c.state)."""
import json, random, subprocess, sys, time
from pathlib import Path

from release_paths import CODE, RELEASE, campaign, results, build
C = campaign('a1', rerun=True)
RESULTS = results('a1')
BUILD = build()
(C / 'raw').mkdir(parents=True, exist_ok=True)
(C / 'vectors').mkdir(parents=True, exist_ok=True)
RAW = C / 'raw'
RUNNER = Path(__file__).with_name('bounded_run.py')
EXE = BUILD / 'shrincs-c-b32.exe'
STATE = C / 'vectors' / 'shrincs-c.state'
CPU = 10
SEED = 20261013

def load_pct():
    try:
        out = subprocess.run(['powershell', '-NoProfile', '-Command',
                              '(Get-CimInstance Win32_Processor | Measure-Object LoadPercentage -Average).Average'],
                             capture_output=True, text=True, timeout=30).stdout.strip()
        return float(out)
    except Exception:
        return None

def run(prefix, scenario, n, reps, tag, timeout=1800):
    out = RAW / f'{prefix}.csv'
    vec = RAW / f'{prefix}.vec.json'
    argv = [str(EXE), 'run', 'x', str(STATE), scenario, str(n), str(reps), str(out), str(vec)]
    b = load_pct()
    subprocess.run([sys.executable, '-B', str(RUNNER), '--cpu', str(CPU), '--timeout', str(timeout),
                    '--prefix', str(RAW / f'job-{prefix}'), '--cwd', str(C)] + argv,
                   stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    a = load_pct()
    with open(RAW / 'load-records.jsonl', 'a') as f:
        f.write(json.dumps({'prefix': prefix, 'tag': tag, 'load_before': b, 'load_after': a, 'argv': argv}) + '\n')

def main():
    while not ((RAW / 'campaign-DONE.txt').exists() or (RAW / 'campaign-ABORT.txt').exists()):
        time.sleep(30)
    rng = random.Random(SEED)
    cells = []
    for m in (32, 1024, 65536):
        cells.append(('shrincsC-stateful', 'prepared', m, 200))
        cells.append(('shrincsC-fallback', 'fallback', m, 20))
        cells.append(('shrincsC-silent-rollback', 'restored', m, 100))
        cells.append(('shrincsC-detected-loss', 'missing', m, 10))
    rng.shuffle(cells)
    (RAW / 'shrincs-order.json').write_text(json.dumps({'seed': SEED, 'order': cells}, indent=1))
    for name, sc, m, reps in cells:
        run(f'{name}-{m}', sc, m, reps, name)
    # fresh process, first stateful signature after loading the state file: 10 separate processes at 32 B
    for i in range(10):
        run(f'shrincsC-fresh-32-{i}', 'prepared', 32, 1, 'shrincsC-fresh')
    (RAW / 'shrincs-DONE.txt').write_text(time.strftime('%Y-%m-%dT%H:%M:%S'))

if __name__ == '__main__':
    main()
