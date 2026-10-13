from pathlib import Path
import json,hashlib,subprocess,re
BASE=Path(__file__).resolve().parent
SRC=BASE/'ChainEvidence.lean'
source=SRC.read_bytes()
LINUX='/mnt/c/Users/angel/Desktop/paper/PAPERS/LUGEL/research/lula22/security/LULA-I-proof-20261012/extensions/shared-oracle-20261013/wots-certification/ChainEvidence.lean'
cmd=['wsl','-d','Ubuntu-24.04','--','bash','-lc','cd /root/jolt-lean-20261001/mathlib && env PATH=/root/jolt-lean-20261001/lean-4.28.0-linux/bin:/usr/bin:/bin /root/jolt-lean-20261001/lean-4.28.0-linux/bin/lake env lean '+LINUX]
p=subprocess.run(cmd,text=True,encoding='utf-8',capture_output=True,timeout=120)
assert SRC.read_bytes()==source,'Source changed during checking'
record={'command':cmd,'exit_code':p.returncode,'stdout':p.stdout,'stderr':p.stderr,'source_sha256':hashlib.sha256(source).hexdigest()}
if (BASE/'check.json').exists():
    history=BASE/'attempts';history.mkdir(exist_ok=True)
    (history/f'attempt-{len(list(history.glob("*.json")))+1:03}.json').write_bytes((BASE/'check.json').read_bytes())
(BASE/'check.json').write_text(json.dumps(record,indent=2),encoding='utf-8')
(BASE/'check.log').write_text(p.stdout+p.stderr,encoding='utf-8')
print(json.dumps(record,indent=2))
raise SystemExit(p.returncode)
