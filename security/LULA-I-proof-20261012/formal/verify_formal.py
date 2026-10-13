from pathlib import Path
import json, re, hashlib
BASE=Path(__file__).resolve().parent
local=json.loads((BASE/'lean-local.json').read_text())
remote=json.loads((BASE/'axle-check.json').read_text())
aristotle=json.loads((BASE/'aristotle-independent-recheck.json').read_text())
ar_local=json.loads((BASE/'aristotle-local-check.json').read_text())
environment=json.loads((BASE/'ENVIRONMENT.json').read_text())
axioms={}
for line in local['stdout'].splitlines():
    m=re.fullmatch(r"'([^']+)' depends on axioms: \[(.*)\]",line)
    if m: axioms[m[1]]=[x.strip() for x in m[2].split(',') if x.strip()]
    m=re.fullmatch(r"'([^']+)' does not depend on any axioms",line)
    if m: axioms[m[1]]=[]
allowed={'propext','Classical.choice','Quot.sound'}
assert len(axioms)==7
assert all(set(a)<=allowed for a in axioms.values())
assert local['exit_code']==0 and not local['stderr']
assert local['source_sha256']==hashlib.sha256((BASE/'LulaLemmas.lean').read_bytes()).hexdigest()
assert remote['okay'] and not remote['lean_messages']['errors']
transmitted=(BASE/'LulaLemmas.lean').read_text(encoding='utf-8')
assert remote['content'].rstrip('\n')==transmitted.rstrip('\n')
assert remote['source_sha256']==hashlib.sha256(transmitted.encode()).hexdigest()
assert aristotle['check']['okay'] and aristotle['statement_comparison']['okay']
assert ar_local['exit_code']==0 and 'sorryAx' not in ar_local['stdout']
assert ar_local['source_sha256']==hashlib.sha256((BASE/'IndependentLulaLocal.lean').read_bytes()).hexdigest()
assert environment['easycrypt_final']['checked_without_diagnostics']
for f in list(BASE.glob('*.lean'))+list(BASE.glob('*.ec')):
    body=f.read_text(encoding='utf-8')
    assert not re.search(r'\b(?:sorry|native_decide|admit)\b|^\s*axiom\b',body,re.M), f
for f,digest in environment['source_hashes'].items():
    assert hashlib.sha256((BASE/f).read_bytes()).hexdigest()==digest, f
rec={'status':'PASS_SCOPED_FORMAL_CHECKS_FULL_SECURITY_OPEN',
     'lean_declarations':axioms,'aristotle_project':'8088c406-8395-494b-a4d4-7f8642dc0bc8',
     'aristotle_checked':'exact returned source with AXLE check and statement comparator; narrow local adaptation separately checked',
     'easycrypt_lemmas':['consistent_equivalence','abort_or_reference','successful_response'],
     'easycrypt_scope':'abstract guarded wrapper, not real corruption handling or security reduction',
     'K':'UNCHECKED', 'complete_EUF_CMA':'OPEN','QROM':'OPEN','certified_quantum_signing_limit':None,
     'source_hash_note':'local/source inventory hashes are actual file bytes; remote hashes are UTF-8 text transmitted, normalized LF by Python read_text',
     'readme':'FORMAL_REPORT.md','quantum_report':'QUANTUM.md'}
(BASE/'FORMAL_STATUS.json').write_text(json.dumps(rec,indent=2),encoding='utf-8')
manifest={str(f.relative_to(BASE)):hashlib.sha256(f.read_bytes()).hexdigest() for f in BASE.rglob('*') if f.is_file() and f.name!='SHA256SUMS.json'}
(BASE/'SHA256SUMS.json').write_text(json.dumps(manifest,indent=2),encoding='utf-8')
print(json.dumps(rec,indent=2))
