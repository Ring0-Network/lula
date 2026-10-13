"""Hash-pinned successor wording/equation check; read-only peer subjects."""
import hashlib, json
from pathlib import Path
HERE=Path(__file__).resolve().parent
BASE=HERE.parent
old=(BASE/'QUANTUM-COVERAGE-DRAFT.md').read_bytes()
new=(BASE/'QUANTUM-COVERAGE-THEOREM.md').read_bytes()
old_hash=hashlib.sha256(old).hexdigest()
new_hash=hashlib.sha256(new).hexdigest()
assert old_hash=='990aeb1067f9ac12235ef3982bc9d3d132cffeab5e704a7d0865a69d77e0c0ce'
assert new_hash=='24a031417b42ba03d266c638a4c3f94dae8887ffd8cf13f584b21387e6d01217'
o=old.decode('utf-8'); n=new.decode('utf-8')
math_old=[line.strip() for line in o.splitlines() if line.startswith('    ')]
math_new=[line.strip() for line in n.splitlines() if line.startswith('    ')]
assert math_old==math_new
for text in (
 'Each new-message reprogramming instruction, including a sampled collision with an old namespace, is followed by one whole-row read that updates the namespace-keyed cache.',
 'Later repeats use the latest cached row for their unchanged U and need no additional read.',
 'The BASE outer function is sampled independently of T_q before adaptive selection.',
 'The selected response can be biased by adaptive quantum search.',
 'reviewed event-only independent advice',
 'This identity is used only after the source-to-programmed-game bridge is justified.',
 'the two enlarged views must not be merged',
 'Full-forgery common-game composition requires its separate review.'
): assert text in n,text
result={'status':'PASS_HASH_PINNED_SUCCESSOR_CHECK', 'immutable_draft_sha256':old_hash,
        'successor_sha256':new_hash,'all_indented_equation_lines_unchanged':True,
        'equation_line_count':len(math_old),'clarifications_present':True,
        'full_forgery_composition_gate_retained':True}
(HERE/'SUCCESSOR-CHECK.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result,indent=2))
