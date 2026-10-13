import hashlib, json
from pathlib import Path

HERE = Path(__file__).resolve().parent
BASE = HERE.parent.parent
def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()
subjects = {
    'chain-pre-independent/outside-simulator/INDEPENDENT-DERIVATION.md': '5555569b844c8a30ee5d58bdca9121e84a45fe5dd62474d0f0fb64df5c009680',
    'chain-pre-independent/outside-simulator/CLARIFICATION.md': '4e0ae20f94a1af80b5a86cd14bab4b8873589a62f4c15eb519757bf3e64f01c7',
    'chain-pre-independent/outside-simulator/ROUTES-CLARIFICATION.md': '383dc9c6b0de9417fe44ca6c66dc69874143aba970b98511df745e256461ede4',
    'outside-field-check/first-independent-derivation.md': 'c6b1b31b95100e10d484e06ba839d2b36d2e1393d18add5e7710d6bf52364a69',
    'outside-field-check/SECOND-READER.json': '331f0e648cdf7bc5b3496f4ab4e151071f2bd64cc488b0d6e26bdd2dab820dbf'
}
for name, expected in subjects.items():
    assert sha(BASE / name) == expected, name
review = {'verdict': 'ACCEPT_SCOPED_MANUAL_B_ONLY_REPLACEMENT',
          'own_first_saved_before_peer_read': True,
          'own_first_sha256': sha(HERE / 'INDEPENDENT-DERIVATION.md'),
          'peer_subjects': subjects,
          'review_sha256': sha(HERE / 'PEER-REVIEW.md'),
          'scope': 'B-only bounded-query success equality; inherited source call caps; no conventional SHA identification',
          'new_resource_metric': 'gate-record emission vs serialized indexed wire-label bitwork distinguished'}
(HERE / 'PEER-REVIEW.json').write_text(json.dumps(review, indent=2) + '\n', encoding='utf-8')
results = json.loads((HERE / 'CONTROL-RESULTS.json').read_text(encoding='utf-8'))
assert results['status'] == 'COMPUTED_EXACT_FINITE_CONTROLS_NOT_FULL_SOURCE_PROOF'
assert results['one_query_full_Choi_equal'] is True
assert results['whole_postC_row_joint_output_law_equal'] is True
files = ['INDEPENDENT-DERIVATION.md', 'CLARIFICATION.md', 'control.py', 'CONTROL-RESULTS.json', 'PEER-REVIEW.md', 'PEER-REVIEW.json', 'finalize.py']
provenance = {'packet': 'ADDITIONAL_OUTSIDE_SIMULATOR_REVIEW_AND_CONTROLS',
    'ready_for_additional_review': True, 'ready_for_promotion': False,
    'already_promoted_original_subject_sha256': '939f4c5fc75e4f8be5dbbb56d45dd8a70f9d6c839e03625776ca271691df7c9e',
    'already_promoted_original_second_reader_sha256': subjects['outside-field-check/SECOND-READER.json'],
    'own_control_exit': 0, 'own_control_status': results['status'],
    'new_clarification_control_peer_read': 'PENDING; not claimed accepted by original receipt',
    'files': {f: sha(HERE / f) for f in files},
    'write_boundary': 'chain-pre-adapter/outside-simulator only',
    'prior_pins_unchanged': True}
(HERE / 'PROVENANCE.json').write_text(json.dumps(provenance, indent=2) + '\n', encoding='utf-8')
print(json.dumps({'provenance_sha256': sha(HERE / 'PROVENANCE.json'), 'review_sha256': sha(HERE / 'PEER-REVIEW.md'), 'control_status': results['status']}))
