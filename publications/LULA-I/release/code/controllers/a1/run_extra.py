"""Extra cells, logical CPU 10, after run_go.py: KN-3952 reconstruction (hot, 3 sizes, + 3 fresh processes), SHRINCS author-C
exhaustion transition (3 processes), LULA I old-snapshot branches (two processes loading the same snapshot file, one after
the other signing overlapping messages; byte equality is checked by compare_snapshot.py)."""
import json, random, shutil, subprocess, sys, time
from pathlib import Path

from release_paths import CODE, RELEASE, campaign, results, build
C = campaign('a1', rerun=True)
RESULTS = results('a1')
BUILD = build()
(C / 'raw').mkdir(parents=True, exist_ok=True)
(C / 'vectors').mkdir(parents=True, exist_ok=True)
RAW, RUNNER = C / 'raw', Path(__file__).with_name('bounded_run.py')
CPU, SEED = 10, 20261015

def load_pct():
    try:
        out = subprocess.run(['powershell', '-NoProfile', '-Command',
                              '(Get-CimInstance Win32_Processor | Measure-Object LoadPercentage -Average).Average'],
                             capture_output=True, text=True, timeout=30).stdout.strip()
        return float(out)
    except Exception:
        return None

def run(prefix, argv, timeout):
    b = load_pct()
    subprocess.run([sys.executable, '-B', str(RUNNER), '--cpu', str(CPU), '--timeout', str(timeout),
                    '--prefix', str(RAW / f'job-{prefix}'), '--cwd', str(C)] + [str(a) for a in argv],
                   stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    with open(RAW / 'load-records.jsonl', 'a') as f:
        f.write(json.dumps({'prefix': prefix, 'load_before': b, 'load_after': load_pct(), 'argv': [str(a) for a in argv]}) + '\n')

def main():
    while not (RAW / 'go-DONE.txt').exists():
        time.sleep(30)
    rng = random.Random(SEED)
    KN, ST = BUILD / 'kn3952.exe', C / 'vectors' / 'kn3952.state'
    cells = [(m, 20 if m < 65536 else 12) for m in (32, 1024, 65536)]
    rng.shuffle(cells)
    for m, reps in cells:
        run(f'kn3952-recon-hot-{m}', [KN, 'run', 'x', ST, 'hot', m, reps, RAW / f'kn3952-recon-hot-{m}.csv',
                                      RAW / f'kn3952-recon-hot-{m}.vec.json'], 3600)
    for i in range(3):
        run(f'kn3952-recon-fresh-32-{i}', [KN, 'run', 'x', ST, 'fresh', 32, 1, RAW / f'kn3952-recon-fresh-32-{i}.csv',
                                           RAW / f'kn3952-recon-fresh-32-{i}.vec.json'], 900)
    EX, SS = BUILD / 'shrincs-c-b32-ex.exe', C / 'vectors' / 'shrincs-c.state'
    for i in range(3):
        run(f'shrincsC-exhaustion-{i}', [EX, 'run', 'x', SS, 'exhaustion', 32, 8, RAW / f'shrincsC-exhaustion-{i}.csv',
                                         RAW / f'shrincsC-exhaustion-{i}.vec.json'], 900)
    SNAP = BUILD / 'lula1_snapshot.exe'
    CACHE = C / 'vectors' / 'lula1.cache'
    if CACHE.exists():
        s0 = C / 'vectors' / 'lula1.snapshot0'
        if not s0.exists():
            shutil.copyfile(CACHE, s0)
        run('lula1-snapA', [SNAP, 'snap', CACHE, 0, 100, 32, RAW / 'lula1-snapA-32.txt'], 1800)
        run('lula1-snapB', [SNAP, 'snap', s0, 0, 200, 32, RAW / 'lula1-snapB-32.txt'], 1800)
        run('lula1-snapA-1k', [SNAP, 'snap', CACHE, 0, 50, 1024, RAW / 'lula1-snapA-1024.txt'], 1800)
        run('lula1-snapB-1k', [SNAP, 'snap', s0, 0, 100, 1024, RAW / 'lula1-snapB-1024.txt'], 1800)
    (RAW / 'extra-DONE.txt').write_text(time.strftime('%Y-%m-%dT%H:%M:%S'))

if __name__ == '__main__':
    main()
