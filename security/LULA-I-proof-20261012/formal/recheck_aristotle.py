from pathlib import Path
import tarfile, json, asyncio, dataclasses, hashlib, subprocess
from axle import AxleClient
BASE=Path(__file__).resolve().parent

async def main():
    with tarfile.open(BASE/'aristotle-returned','r:gz') as archive:
        src=[m for m in archive if m.isfile() and m.name.endswith('/IndependentLula.lean')]
        if len(src)!=1: raise ValueError('Ambiguous Lean source')
        body=archive.extractfile(src[0]).read().decode('utf-8')
    (BASE/'IndependentLula.lean').write_text(body,encoding='utf-8')
    formal='''import Mathlib
namespace IndependentLula
theorem fixed_sum_antichain {x y : List Nat}
 (hle : List.Forall₂ (· ≤ ·) x y) (hs : x.sum = y.sum) : x = y := by sorry
end IndependentLula
'''
    client=AxleClient(base_timeout_seconds=150,max_concurrency=1)
    try:
        chk=await client.check(content=body,environment='lean-4.28.0',ignore_imports=False,timeout_seconds=120)
        compare=await client.verify_proof(formal_statement=formal,content=body,environment='lean-4.28.0',ignore_imports=False,timeout_seconds=120)
        rec={'check':dataclasses.asdict(chk),'statement_comparison':dataclasses.asdict(compare),
             'source_sha256':hashlib.sha256(body.encode()).hexdigest(),
             'statement_template_contains_placeholder_only_for_comparator':True}
        (BASE/'aristotle-independent-recheck.json').write_text(json.dumps(rec,indent=2),encoding='utf-8')
        print(json.dumps(rec,indent=2))
    finally: await client.close()
    narrow=body.replace('import Mathlib\n','import Mathlib.Data.List.Forall2\nimport Mathlib.Data.List.TakeDrop\n',1).replace('exact le_rfl','exact Nat.le_refl _')
    local=BASE/'IndependentLulaLocal.lean'
    local.write_text(narrow,encoding='utf-8')
    linux='/mnt/c/Users/angel/Desktop/paper/PAPERS/LUGEL/research/lula22/security/LULA-I-proof-20261012/formal/IndependentLulaLocal.lean'
    cmd=['wsl','-d','Ubuntu-24.04','--','bash','-lc','cd /root/jolt-lean-20261001/mathlib && env PATH=/root/jolt-lean-20261001/lean-4.28.0-linux/bin:/usr/bin:/bin /root/jolt-lean-20261001/lean-4.28.0-linux/bin/lake env lean '+linux]
    p=subprocess.run(cmd,text=True,encoding='utf-8',capture_output=True,timeout=120)
    (BASE/'aristotle-local-check.json').write_text(json.dumps({'command':cmd,'exit_code':p.returncode,'stdout':p.stdout,'stderr':p.stderr,'source_sha256':hashlib.sha256(local.read_bytes()).hexdigest(),'local_changes':['aggregate import replaced by compiled narrow imports','generic le_rfl replaced by Nat.le_refl _; statement unchanged']},indent=2),encoding='utf-8')
    print('Independent local exit:',p.returncode,p.stdout,p.stderr)
if __name__=='__main__': asyncio.run(main())
