from pathlib import Path
import subprocess, json, hashlib
BASE=Path(__file__).resolve().parent
LINUX='/mnt/c/Users/angel/Desktop/paper/PAPERS/LUGEL/research/lula22/security/LULA-I-proof-20261012/formal'
cmd=['wsl','-d','Ubuntu-24.04','--','bash','-lc',
 'cd /root/jolt-lean-20261001/mathlib && env PATH=/root/jolt-lean-20261001/lean-4.28.0-linux/bin:/usr/bin:/bin /root/jolt-lean-20261001/lean-4.28.0-linux/bin/lake env lean '+LINUX+'/LulaLemmas.lean']
p=subprocess.run(cmd,text=True,encoding='utf-8',capture_output=True,timeout=120)
(BASE/'lean-local.log').write_text(p.stdout+p.stderr,encoding='utf-8')
rec={'command':cmd,'exit_code':p.returncode,'source_sha256':hashlib.sha256((BASE/'LulaLemmas.lean').read_bytes()).hexdigest(),'stdout':p.stdout,'stderr':p.stderr}
(BASE/'lean-local.json').write_text(json.dumps(rec,indent=2),encoding='utf-8')
print(json.dumps(rec,indent=2))
