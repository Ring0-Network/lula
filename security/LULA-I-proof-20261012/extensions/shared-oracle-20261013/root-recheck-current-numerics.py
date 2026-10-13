"""Root reexecution against the independently saved classical interval dataset.

Only the historical quantum-status assertion is adapted; mathematical classical
comparisons are reused verbatim. No peer result or calculator is overwritten.
"""
from pathlib import Path
import hashlib
import json
import subprocess
import sys

X=Path(__file__).resolve().parent
src=X/'classical-composition-numeric'
out=X/'root-current-classical-recheck'
out.mkdir(exist_ok=True)
original=(src/'crosscheck_root.py').read_bytes()
s=original.decode('utf8')
old='assert row["quantum_total"] is None and row["quantum_status"] == "OPEN_NO_QROM_REDUCTION"'
new='assert row["quantum_category1_status"] == "NOT_ESTABLISHED_NO_CERTIFIED_CAPACITY"'
assert s.count(old)==1
s=s.replace(old,new)
s=s.replace('"comparison_order":"Independent OWN-BOUNDS.json was saved first; root result files were then read.",','"comparison_order":"Root reexecution against the peer dataset saved independently before original root results; mathematical checks unchanged.",')
(out/'crosscheck_root.py').write_text(s,encoding='utf8')
own=(src/'OWN-BOUNDS.json').read_bytes()
(out/'OWN-BOUNDS.json').write_bytes(own)
provenance={
 'original_independent_data_sha256':hashlib.sha256(own).hexdigest(),
 'original_crosscheck_source_sha256':hashlib.sha256(original).hexdigest(),
 'adapted_crosscheck_sha256':hashlib.sha256((out/'crosscheck_root.py').read_bytes()).hexdigest(),
 'adaptation':'Historical quantum-total-null status assertion replaced by current category-unestablished assertion; classical mathematical comparisons unchanged.',
 'independence':'This run is by root using a previously independent peer dataset, not a new blind derivation.'}
(out/'PROVENANCE.json').write_text(json.dumps(provenance,indent=2)+'\n',encoding='utf8')
p=subprocess.run([sys.executable,'-I','-B',str(out/'crosscheck_root.py')],capture_output=True,text=True)
(out/'RUN.json').write_text(json.dumps({'exit_code':p.returncode,'stdout':p.stdout,'stderr':p.stderr},indent=2)+'\n',encoding='utf8')
assert p.returncode==0, p.stderr
print('PASS_16_CURRENT_CLASSICAL_ROWS_AGAINST_SAVED_INDEPENDENT_INTERVAL_DATA')
