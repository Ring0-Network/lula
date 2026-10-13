from pathlib import Path
import json, subprocess, hashlib
BASE=Path(__file__).resolve().parent
if (BASE/'check.json').exists():
    attempts=BASE/'attempts';attempts.mkdir(exist_ok=True)
    index=len(list(attempts.glob('attempt-*.json')))+1
    (attempts/f'attempt-{index:03}.json').write_bytes((BASE/'check.json').read_bytes())
LINUX='/mnt/c/Users/angel/Desktop/paper/PAPERS/LUGEL/research/lula22/security/LULA-I-proof-20261012/extensions/shared-oracle-20261013/formal-tree'
cmd=['wsl','-d','Ubuntu-24.04','--','bash','-lc','cd /root/jolt-lean-20261001/mathlib && env PATH=/root/jolt-lean-20261001/lean-4.28.0-linux/bin:/usr/bin:/bin /root/jolt-lean-20261001/lean-4.28.0-linux/bin/lake env lean '+LINUX+'/AddressedMerkle.lean']
p=subprocess.run(cmd,text=True,encoding='utf-8',capture_output=True,timeout=120)
(BASE/'check.log').write_text(p.stdout+p.stderr,encoding='utf-8')
record={'command':cmd,'exit_code':p.returncode,'stdout':p.stdout,'stderr':p.stderr,'source_sha256':hashlib.sha256((BASE/'AddressedMerkle.lean').read_bytes()).hexdigest()}
(BASE/'check.json').write_text(json.dumps(record,indent=2),encoding='utf-8')
print(json.dumps(record,indent=2))
raise SystemExit(p.returncode)
