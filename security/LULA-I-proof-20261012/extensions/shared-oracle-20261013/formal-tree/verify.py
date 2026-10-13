from pathlib import Path
import json,re,hashlib,subprocess
BASE=Path(__file__).resolve().parent
source=BASE/'AddressedMerkle.lean'
body=source.read_text(encoding='utf-8')
assert not re.search(r'\b(?:sorry|admit|native_decide)\b|^\s*axiom\b',body,re.M)
local=json.loads((BASE/'check.json').read_text(encoding='utf-8'))
assert local['exit_code']==0 and not local['stderr'] and 'error' not in local['stdout'] and 'warning' not in local['stdout']
assert local['source_sha256']==hashlib.sha256(source.read_bytes()).hexdigest()
axioms={}
for line in local['stdout'].splitlines():
    match=re.fullmatch(r"'([^']+)' depends on axioms: \[(.*)\]",line)
    if match: axioms[match[1]]=[x.strip() for x in match[2].split(',') if x.strip()]
assert len(axioms)==5
assert all(set(x)<={'propext','Classical.choice','Quot.sound'} for x in axioms.values())
remote=json.loads((BASE/'axle.json').read_text(encoding='utf-8'))
assert remote['check']['okay'] and remote['statement_comparison']['okay']
assert not remote['check']['lean_messages']['errors']
assert remote['check']['content'].rstrip('\n')==body.rstrip('\n')
assert remote['transmitted_source_sha256']==hashlib.sha256(body.encode()).hexdigest()
assert remote['statement_only_sha256']==hashlib.sha256((BASE/'STATEMENTS.json').read_bytes()).hexdigest()
binding=json.loads((BASE/'SOURCE_BINDING.json').read_text(encoding='utf-8'))
assert hashlib.sha256(Path(binding['library']).read_bytes()).hexdigest()==binding['library_sha256']
pin_cmd=['wsl','-d','Ubuntu-24.04','--','bash','-lc','/root/jolt-lean-20261001/lean-4.28.0-linux/bin/lean --version; git -C /root/jolt-lean-20261001/mathlib rev-parse HEAD; sha256sum /root/jolt-lean-20261001/lean-4.28.0-linux/bin/lean /root/jolt-lean-20261001/mathlib/lake-manifest.json']
pin=subprocess.run(pin_cmd,text=True,encoding='utf-8',capture_output=True,timeout=120)
assert pin.returncode==0
for text in ['4.28.0','8f9d9cff6bd728b17a24e163c9402775d9e6a365','3e0d0d3d801675359f2d4cf9815bfdb417b20b92fdd9d48b3b14c95bbae28bbf','a89b59a9c917d113c32b931cc82a6b919d50be80ec1a701612f571bcd34f245a']:
    assert text in pin.stdout
record={'status':'PROVED_SCOPED_ADDRESSED_MERKLE_EXTRACTION','declarations':axioms,
        'source_sha256':local['source_sha256'],'axiom_allowlist':['propext','Classical.choice','Quot.sound'],
        'exact_statement_comparison':'PASS_AXLE','source_binding':'MANUAL_NO_RUST_REFINEMENT_PROOF',
        'challenge_embedding':'OPEN','complete_security_bound':'OPEN','pin_command':pin_cmd,'pin_exit_code':pin.returncode,'pin_stdout':pin.stdout,'pin_stderr':pin.stderr}
(BASE/'STATUS.json').write_text(json.dumps(record,indent=2),encoding='utf-8')
manifest={str(f.relative_to(BASE)):hashlib.sha256(f.read_bytes()).hexdigest() for f in BASE.rglob('*') if f.is_file() and f.name!='SHA256SUMS.json'}
(BASE/'SHA256SUMS.json').write_text(json.dumps(manifest,indent=2),encoding='utf-8')
print(json.dumps({'status':record['status'],'declarations':list(axioms),'source_sha256':local['source_sha256'],'challenge_embedding':'OPEN'},indent=2))
