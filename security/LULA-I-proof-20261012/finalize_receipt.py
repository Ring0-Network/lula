from pathlib import Path
import hashlib, json

D = Path(__file__).resolve().parent
def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()
checks = json.loads((D / 'VALIDATION.json').read_text())
formal = json.loads((D / 'formal' / 'FORMAL_STATUS.json').read_text())
original = json.loads((D / 'numerics' / 'bounds.json').read_text())
rerun = json.loads((D / 'results' / 'bounds.json').read_text())
assert original == rerun, 'Root entry-point replay differs'
assert formal['complete_EUF_CMA'] == 'OPEN' and formal['QROM'] == 'OPEN'
assert formal['certified_quantum_signing_limit'] is None
assert len(formal['lean_declarations']) == 7 and len(formal['easycrypt_lemmas']) == 3
for row in json.loads((D / 'BASELINE.json').read_text()):
    assert sha(Path(row['path'])) == row['sha256'], 'Protected file changed'
names = ['PROOF.md','bounds.py','TERM-TABLE.md','OPEN.md','README.md','HANDOFF.md','OBJECTIVE.txt','BASELINE.json','VALIDATION.json',
         'code-review/INDEPENDENT_CODE_GAME.md','code-review/SOURCE_AND_COUNTS.json','code-review/SECOND_READER.md','code-review/ROOT_PROOF_REVIEW.md',
         'numerics/bounds.py','numerics/bounds.json','numerics/ROOT_NUMERIC_REVIEW.md','numerics/ORIGINAL_CROSSCHECK.json',
         'formal/FORMAL_REPORT.md','formal/FORMAL_STATUS.json','formal/QUANTUM.md','formal/LulaLemmas.lean','formal/CacheModel.ec','formal/CacheSemantics.k']
receipt = {'outcome':'SCOPED_PROOFS_AND_COMPUTATIONS_DELIVERED_FULL_SECURITY_OPEN',
           'full_EUF_CMA':'not established','full_QROM':'not established','certified_classical_signing_limit':None,'certified_quantum_signing_limit':None,
           'source_and_manuscript_unchanged':True,'root_numeric_replay_matches_independent_output':True,
           'Lean_checked_declarations':7,'Aristotle_independent_antichain_rechecked':True,'EasyCrypt_checked_lemmas':3,'K':'UNCHECKED',
           'review_corrections_applied':['total-versus-partial oracle wording','actual prepared setup PRF invocation bound','round quantum exponent from unrounded numeric value'],
           'files':[{'path':name,'bytes':(D / name).stat().st_size,'sha256':sha(D / name)} for name in names]}
(D / 'DELIVERY.json').write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf-8')
print(json.dumps({key:value for key,value in receipt.items() if key != 'files'},indent=2))
