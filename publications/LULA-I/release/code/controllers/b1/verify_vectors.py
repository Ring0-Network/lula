"""Replay the LULA I vectors of campaign b1 through the independent verifier and compare bytes across states.
Writes results/independent-check.txt. Groups by (pk_root, msg): every group must hold a single signature."""
import subprocess, sys, collections
from pathlib import Path

from release_paths import CODE, RELEASE, campaign, results, build
S = campaign('b1', rerun=False)
RESULTS = results('b1')
BUILD = build()
V = CODE / 'verifier' / 'verify_lula.py'
SPEC = '18,9,1;5:4:0:240:0|5:4:0:240:0|5:4:0:240:0|5:4:0:240:0|21:8:0:2040:1'
tmp = RESULTS / 'kat-for-independent-check'
tmp.mkdir(exist_ok=True)
out, groups = [], collections.defaultdict(set)
files = sorted(p for p in (S / 'raw').glob('*.vec.txt') if 'slh' not in p.name)
for vec in files:
    lines = vec.read_text().splitlines()
    d = {l.split()[0]: l.split()[1] for l in lines if len(l.split()) == 2}
    groups[(d['pk_root'], d['msg'])].add(d['sig'])
    kat = tmp / ('vectors_' + vec.name.replace('.vec.txt', '') + '.txt')
    kat.write_text('# campaign replay; params LULA I spec ' + SPEC + '\n' + '\n'.join(lines) + '\n')
    r = subprocess.run([sys.executable, '-I', '-B', str(V), str(kat)], capture_output=True, text=True)
    out.append(f'{vec.name}: exit={r.returncode} {r.stdout.strip()} {r.stderr.strip()[:200]}')
ok = sum(1 for l in out if ': exit=0' in l)
out.append(f'verifier passed {ok}/{len(files)} vector files')
for (root, msg), sigs in groups.items():
    out.append(f'byte equality: key {root[:8]} msg {msg[-8:]}: {len(sigs)} distinct signature(s)')
(RESULTS / 'independent-check.txt').write_text('\n'.join(out) + '\n')
print('\n'.join(out[-8:]))
