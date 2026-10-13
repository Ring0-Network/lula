"""Replay the signatures of this campaign through the independent Python verifier of the publication
(`code/verifier/verify_lula.py`, written from SPEC.md, not from the Rust
code). Input: raw/lula1-*.vec.txt written by lula1_driver_original (pk_seed, pk_root, msg, sig of replicate 0). Output:
results/independent-check.txt. The verifier checks: signature verifies; one flipped message bit rejects; one flipped signature
byte rejects."""
import subprocess, sys
from pathlib import Path

from release_paths import CODE, RELEASE, campaign, results, build
C = campaign('a1', rerun=False)
RESULTS = results('a1')
BUILD = build()
V = CODE / 'verifier' / 'verify_lula.py'
SPEC = '18,9,1;5:4:0:240:0|5:4:0:240:0|5:4:0:240:0|5:4:0:240:0|21:8:0:2040:1'
tmp = RESULTS / 'kat-for-independent-check'
tmp.mkdir(exist_ok=True)
out = []
for vec in sorted((C / 'raw').glob('lula1-*.vec.txt')):
    lines = vec.read_text().splitlines()
    kat = tmp / ('vectors_' + vec.stem.replace('.vec', '') + '.txt')
    kat.write_text('# campaign replay; params LULA I spec ' + SPEC + '\n' + '\n'.join(lines) + '\n')
    r = subprocess.run([sys.executable, '-I', '-B', str(V), str(kat)], capture_output=True, text=True)
    out.append(f'{vec.name}: exit={r.returncode} {r.stdout.strip()} {r.stderr.strip()[:200]}')
(RESULTS / 'independent-check.txt').write_text('\n'.join(out) + '\n')
print('\n'.join(out))
