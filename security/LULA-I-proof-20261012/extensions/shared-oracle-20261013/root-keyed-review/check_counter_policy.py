"""Run the four synthetic counter-policy helpers under the pinned kernel.

The helpers do not prove source security or published-definition compatibility.
"""
from pathlib import Path
import hashlib, json, re, subprocess

P=Path(__file__).resolve().parent
source=P/'CounterPolicy.lean'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
text=source.read_text(encoding='utf8')
assert not re.search(r'\bsorry\b|\bnative_decide\b|^\s*axiom\s',text,re.M)
cmd=['wsl','-d','Ubuntu-24.04','--cd','/root/jolt-lean-20261001/mathlib','--',
     '/usr/bin/env','PATH=/root/jolt-lean-20261001/lean-4.28.0-linux/bin:/usr/bin:/bin',
     '/root/jolt-lean-20261001/lean-4.28.0-linux/bin/lake','env','lean',
     '/mnt/c/Users/angel/Desktop/paper/PAPERS/LUGEL/research/lula22/security/LULA-I-proof-20261012/extensions/shared-oracle-20261013/root-keyed-review/CounterPolicy.lean']
r=subprocess.run(cmd,capture_output=True,text=True,timeout=60)
log=P/'CounterPolicy.log'
log.write_text(r.stdout+r.stderr,encoding='utf8')
assert r.returncode==0,r.stdout+r.stderr
names=['both_policies_accepted','canonical_policy_collision',
       'later_policy_no_changed_base_collision','no_finite_factor_from_zero_success']
axioms={}
for name in names:
    full='LulaCounterPolicy.'+name
    m=re.search(re.escape("'"+full+"'")+r' depends on axioms: \[([^\]]*)\]',r.stdout)
    if m:
        aset=sorted(s.strip() for s in m.group(1).split(',') if s.strip())
    else:
        assert "'"+full+"' does not depend on any axioms" in r.stdout,full
        aset=[]
    assert set(aset)<={'propext','Classical.choice','Quot.sound'}
    axioms[full]=aset
receipt={'status':'PASS_FOUR_SYNTHETIC_COUNTER_POLICY_HELPERS',
         'source_sha256':sha(source),'log_sha256':sha(log),'command':cmd,
         'exit_code':r.returncode,'toolchain':'Lean 4.28.0; existing WSL Ubuntu-24.04 Mathlib checkout',
         'checked_declarations':4,'axioms':axioms,'custom_axioms':0,'admissions':0,
         'source_security_checked_declarations':0,
         'scope':'A two-base abstract selection-policy countermodel; no actual LULA predicate, hash hardness or source attack.'}
(P/'COUNTER-POLICY-CHECK.json').write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf8')
print(json.dumps({'status':receipt['status'],'declarations':4,'axioms':axioms}))
