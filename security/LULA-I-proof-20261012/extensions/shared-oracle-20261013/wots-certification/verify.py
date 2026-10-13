from pathlib import Path
import json,re,hashlib,subprocess
BASE=Path(__file__).resolve().parent
source=BASE/'ChainEvidence.lean'
body=source.read_text(encoding='utf-8')
assert not re.search(r'\b(?:sorry|admit|native_decide)\b|^\s*axiom\b',body,re.M)
check=json.loads((BASE/'check.json').read_text(encoding='utf-8'))
assert check['exit_code']==0 and not check['stderr'] and 'error' not in check['stdout'] and 'warning' not in check['stdout']
assert check['source_sha256']==hashlib.sha256(source.read_bytes()).hexdigest()
axioms={}
for line in check['stdout'].splitlines():
    m=re.fullmatch(r"'([^']+)' depends on axioms: \[(.*)\]",line)
    if m:axioms[m[1]]=[a.strip() for a in m[2].split(',') if a.strip()]
    m=re.fullmatch(r"'([^']+)' does not depend on any axioms",line)
    if m:axioms[m[1]]=[]
assert len(axioms)==8 and all(set(a)<={'propext','Classical.choice','Quot.sound'} for a in axioms.values())
pattern=re.compile(r'(?ms)^(theorem\s+(\w+).*?) :=(?: by\n|\n)(.*?)(?=^\S|\Z)')
statements=[{'name':name,'signature':signature} for signature,name,proof in pattern.findall(body)]
assert len(statements)==8
sp=BASE/'STATEMENTS.json'
if sp.exists():assert json.loads(sp.read_text(encoding='utf-8'))['declarations']==statements,'Declaration changed'
else:sp.write_text(json.dumps({'declarations':statements,'source_sha256':check['source_sha256'],'scope':'Exact declarations; proof bodies are in checked source'},indent=2),encoding='utf-8')
library=Path(r'C:\Users\angel\Desktop\paper\PAPERS\LUGEL\research\lula22\publications\LULA-I\release\code\lula1\src\lib.rs')
pin='ac8e67f05af68dd8e1291c5909847f74103903fb7ffa2c70f500c6ec48f14210'
assert hashlib.sha256(library.read_bytes()).hexdigest()==pin
cmd=['wsl','-d','Ubuntu-24.04','--','bash','-lc','/root/jolt-lean-20261001/lean-4.28.0-linux/bin/lean --version; git -C /root/jolt-lean-20261001/mathlib rev-parse HEAD; sha256sum /root/jolt-lean-20261001/lean-4.28.0-linux/bin/lean /root/jolt-lean-20261001/mathlib/lake-manifest.json']
p=subprocess.run(cmd,text=True,encoding='utf-8',capture_output=True,timeout=120)
assert p.returncode==0
for pintext in ['4.28.0','8f9d9cff6bd728b17a24e163c9402775d9e6a365','3e0d0d3d801675359f2d4cf9815bfdb417b20b92fdd9d48b3b14c95bbae28bbf','a89b59a9c917d113c32b931cc82a6b919d50be80ec1a701612f571bcd34f245a']:assert pintext in p.stdout
binding={'library':str(library),'sha256':pin,'source_anchors':{'wots': [202,278],'verification':[720,729]},'scope':'Manual exact source binding, not verified extraction','pin_command':cmd,'pin_exit_code':p.returncode,'pin_stdout':p.stdout,'pin_stderr':p.stderr}
(BASE/'SOURCE_BINDING.json').write_text(json.dumps(binding,indent=2),encoding='utf-8')
status={'status':'MANUAL_COMPLETE_WOTS_EVIDENCE_SPLIT_WITH_CHECKED_COMPONENTS','declarations':axioms,'source_sha256':check['source_sha256'],'quantitative_primitive_embedding':'OPEN','unexposed_key_reduction':'OPEN','complete_EUF_CMA':'OPEN','QROM':'OPEN','mechanized_scope':'Labelled suffix merger, raw-input injection, last-step preimage dataflow, fixed-sum antichain; not whole WOTS algorithm/source refinement'}
(BASE/'STATUS.json').write_text(json.dumps(status,indent=2),encoding='utf-8')
manifest={str(f.relative_to(BASE)):hashlib.sha256(f.read_bytes()).hexdigest() for f in BASE.rglob('*') if f.is_file() and f.name!='SHA256SUMS.json'}
(BASE/'SHA256SUMS.json').write_text(json.dumps(manifest,indent=2),encoding='utf-8')
print(json.dumps({'status':status['status'],'checked_declarations':len(axioms),'quantitative_embedding':'OPEN'},indent=2))
