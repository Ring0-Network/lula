from pathlib import Path
import hashlib,json,re,subprocess
E=Path(__file__).resolve().parent
source=E/'DigestProjection.lean'
text=source.read_text()
assert not re.search(r'\b(sorry|admit|native_decide|axiom)\b',text)
linux='/mnt/c/'+str(source).replace('C:\\','').replace('\\','/')
cmd=['wsl','-d','Ubuntu-24.04','--cd','/root/jolt-lean-20261001/mathlib','--','/usr/bin/env','PATH=/root/jolt-lean-20261001/lean-4.28.0-linux/bin:/usr/bin:/bin','/root/jolt-lean-20261001/lean-4.28.0-linux/bin/lake','env','lean',linux]
p=subprocess.run(cmd,capture_output=True,text=True,encoding='utf8')
log=p.stdout+p.stderr
(E/'DigestProjection.log').write_text(log,encoding='utf8')
assert p.returncode==0,log
sets=re.findall(r'depends on axioms: \[([^\]]*)\]',log)
assert len(sets)==3,log
axioms=[set(x.strip() for x in s.split(',') if x.strip()) for s in sets]
assert all(s <= {'propext','Classical.choice','Quot.sound'} for s in axioms)
record={'status':'PASS_THREE_DIGEST_PROJECTION_HELPERS','source_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),'log_sha256':hashlib.sha256((E/'DigestProjection.log').read_bytes()).hexdigest(),'command':cmd,'exit_code':p.returncode,'checked_declarations':3,'axiom_sets':[sorted(s) for s in axioms],'toolchain':'Pinned Lean4.28.0, existing Mathlib checkout','scope':'Bit-function prefix projection and two source-position slices; not SHA hardness, source refinement, or full signature theorem','new_source_game_checked_declarations':0}
(E/'PROJECTION-CHECK.json').write_text(json.dumps(record,indent=2)+'\n',encoding='utf8')
print(json.dumps(record,indent=2))
