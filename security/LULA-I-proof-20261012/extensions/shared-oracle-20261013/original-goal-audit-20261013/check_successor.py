"""Pin the manually reviewed live-index successor without rewriting old audit."""
from pathlib import Path
import hashlib
import json

HERE=Path(__file__).resolve().parent
X=HERE.parent
BASE=X/'root-docs-before-query-resource'
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
names=['PROOF.md','OPEN.md','REQUIREMENT-MAP.md','HANDOFF.md','SECURITY-CRITERION.md']
text={n:(X/n).read_text(encoding='utf-8') for n in names}
old=json.loads((HERE/'AUDIT.json').read_text(encoding='utf-8'))
old_audit={
    'AUDIT.md':'77c2ed3fc963cb23a9418129f945c4ee712b70344e051cba6603319753c1f0b5',
    'AUDIT.json':'bc53dde4bdf7c4f1ecaf01e48f1ce2ae943a4f310f5a0bc68436622b0dfddf45',
    'audit.py':'833977e21cd1f7b3d58b15304c22effa3a5933e478e8b9df3e444107e027d336'}
assert all(sha(HERE/n)==h for n,h in old_audit.items())
accepted=['CLASSICAL-RO-THEOREM.md','QUANTUM-RO-THEOREM.md',
          'QUANTUM-EVENT-SPECIFIC-THEOREM.md','bounds.py','bounds-event-specific.py',
          'root-checks/bounds-QH64/bounds.json','root-checks/bounds-QH128/bounds.json',
          'root-checks/refined-Qq32/bounds.json','root-checks/refined-Qq64/bounds.json']
assert all(sha(X/n)==old['input_pins'][n] for n in accepted)
checks={
    'F1_no_crossing': ('## 6. Original tiny-failure gates' in text['PROOF.md']
      and 'at least6243/N' in text['PROOF.md']
      and 'statements about sufficient bounds' in text['PROOF.md']
      and 'not adversarial success lower bounds' in text['PROOF.md']),
    'F3_successor_gate': ('remaining coverage/composition gate stays open' not in text['PROOF.md']
      and 'complete coverage/composition successor is proved in Sections 5a–5b' in text['PROOF.md']
      and 'without altering their review hashes' in text['PROOF.md']),
    'F4_extra_mechanization': ('fully mechanized Rust/compiler/channel theorem is additional assurance' in text['PROOF.md']
      and 'checked compiler refinement is extra assurance' in text['REQUIREMENT-MAP.md']
      and 'Exact manual source/game verification and reduction programs are required' in text['PROOF.md']),
    'F8_optional_source_attack': ('not an original proof deliverable or a new completion prerequisite' in text['PROOF.md']
      and 'not an original proof deliverable or a category-certification prerequisite' in text['SECURITY-CRITERION.md']
      and '**OPEN — active next source boundary.**' not in text['HANDOFF.md']
      and 'probability audit is ongoing' not in text['HANDOFF.md']),
    'generic_reductions_remain_open': ('still-requested keyed PRF and addressed PRE/SPR/TCR challenge programs' in text['OPEN.md']
      and 'remain OPEN' in text['OPEN.md']
      and 'Generic primitive challenge programs/resources and actual level/category certification remain original unresolved obligations' in text['REQUIREMENT-MAP.md']),
    'category_capacity_remain_open': ('certified signing capacities are not established' in text['PROOF.md']
      and 'not certified work factors' in text['PROOF.md']
      and '**OPEN 2 — certified level/category and capacity.**' in text['OPEN.md']),
    'public_cache_remains_open': ('Public cache bytes require an auxiliary-view simulation' in text['OPEN.md']
      and 'Public cache-byte interface needs an auxiliary-view simulation' in text['REQUIREMENT-MAP.md']
      and 'broader public-cache and corrupt-cache demands remain distinct' in text['PROOF.md']),
    'prior_audit_unchanged':True,
    'accepted_theorems_and_existing_numerics_unchanged':True,
}
outcome='PASS_ORIGINAL_SCOPE_NO_CROSSING_AND_SUCCESSOR_INDEX' if all(checks.values()) else 'PARTIAL_SUCCESSOR_CONTRADICTION_REMAINS'
record={'outcome':outcome,'manual_review':'All five current live-index files read; checks pin identified statements, not substitute a new theorem proof.',
        'checks':checks,'baseline_pins':{n:sha(BASE/n) for n in names},
        'successor_pins':{n:sha(X/n) for n in names},'preserved_old_audit_pins':old_audit,
        'accepted_artifacts_unchanged':{n:sha(X/n) for n in accepted},
        'check_script_sha256':sha(Path(__file__)),
        'certification':'NOT_ESTABLISHED; original goal remains active'}
(HERE/'SUCCESSOR-CHECK.json').write_text(json.dumps(record,indent=2)+'\n',encoding='utf-8')
lines=['# Original-goal audit: live-index successor check','',
       '**'+outcome+'** — Five successor index documents read completely. This checks incorporation of the original audit, not a new complete security proof. Old audit files, accepted model theorem hashes and previously checked numerical outputs are unchanged.','',
       '| Finding/obligation | Checked result |','|---|---|']
for k,v in checks.items(): lines.append(f'| {k} | {"PASS" if v else "PARTIAL"} |')
lines += ['',
 '**PROVED — F1.** Section6 gives exact no-crossing of the supplied sufficient probability envelopes. It keeps the distinction between failed sufficient gates and actual attacks; constant-success1/2 query crossings are separately labelled and do not replace category certification.','',
 '**PROVED — F3.** Live PROOF index now directs readers to the proved finite-QROM successor instead of declaring its coverage/composition gate open. Reviewed historical artifacts retain their exact old hashes.','',
 '**PROVED — F4.** Exact manual source/game correspondence and reduction programs remain required. Fully checked Rust/compiler/channel refinement is expressly additional assurance. This does not weaken the original generic-program or category requirements.','',
 '**PROVED — F8 scope.** Source-valid operational attack/skeleton work is labelled optional and unpromoted, with no review acceptance credited to the failed lane. It is not an original deliverable or a prerequisite for category certification.','',
 '**OPEN — actual remaining obligations.** Explicit memoized shared-oracle-compatible private challenge programs/resources; selected-address PRE/SPR/TCR challenge embedding and extraction costs; public payload-only auxiliary-view simulation; adequate level/category resource comparison and certified signing capacity. Arbitrary corrupt-cache transparency remains refuted for pinned code.','',
 '**OPEN — final certification.** Not established. The original goal remains active.']
if not checks['F8_optional_source_attack']:
    lines += ['', '**PARTIAL — actionable inconsistency.** HANDOFF.md still calls the operational signature-skeleton lane the active next source boundary and/or says its narrow probability audit is ongoing. The ending already makes the lane optional. Replace the stale live paragraphs with historical unpromoted status and completed narrow abstract review before accepting F8 fully.']
(HERE/'SUCCESSOR-CHECK.md').write_text('\n'.join(lines)+'\n',encoding='utf-8')
print(json.dumps({'outcome':outcome,'checks':checks}))
