from pathlib import Path
import hashlib, json

HERE = Path(__file__).resolve().parent
BASE = HERE.parent.parent
ROOT = BASE.parents[3]
def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()
source = ROOT / 'publications/LULA-I/release/code/lula1/src/lib.rs'
assert sha(source) == 'ac8e67f05af68dd8e1291c5909847f74103903fb7ffa2c70f500c6ec48f14210'
assert sha(BASE / 'PRIVATE-REDUCTION-PROGRAMS.md') == 'feff3d899edcb0b675970eaf915c221d837a47ab7357828758f0f0a40c923f89'
assert sha(HERE / 'INDEPENDENT-DERIVATION.md') == '6c44c1b3cce9cc5438f333031258b1c392069a171b1c6358e6354af6d9aab1af'
result = json.loads((HERE / 'CONTROL-RESULTS.json').read_text(encoding='utf-8'))
assert result['source_sha256'] == sha(HERE / 'control.py')
assert result['status'] == 'COMPUTED_EXACT_INTERFACE_CONTROLS_NOT_FULL_SOURCE_PROOF'
assert result['full_source_facing_transcript_law_checked']
files = ['INDEPENDENT-DERIVATION.md','control.py','CONTROL-RESULTS.json','finalize.py']
packet = {
    'scope': 'EXACT_ORDINARY_PUBLIC_FIXED_H_PRIVATE_PRF_ADAPTERS',
    'own_first_saved_before_peer_read': True,
    'manual_status': 'OWN_DERIVATION_SAVED_INDEPENDENT_PEER_REVIEW_PENDING',
    'hardness_status': 'ASSUMED_PARTICULAR_PRIVATE_FAMILIES',
    'own_control_exit': 0,
    'source_sha256': sha(source),
    'inherited_counts_sha256': sha(BASE / 'PRIVATE-REDUCTION-PROGRAMS.md'),
    'files': {f:sha(HERE/f) for f in files},
    'identities': ['SrcReal_h->SrcFideal_h = ordinary AdvPRF(f,BK)',
                   'SrcFideal_h->SrcFJideal_h = ordinary AdvPRF(g,BP)'],
    'private_output_bytes': 16,
    'raw_sideoracle': False,
    'public_hash': 'ONE_FIXED_KNOWN_FULL256_ALGORITHM_COMPUTED_LOCALLY',
    'public_seed_zero_excluded': False,
    'prekey_source_seed_withheld': True,
    'quantum_private_query_requirement': 'classical only; PQ distinguisher allowed',
    'limits': ['No fixed-SHA PRF hardness proof', 'No externalRO numerical transfer',
               'No ideal-private fixed-h PRE/TCR/final forgery theorem',
               'No kernel/native-Rust/category certification'],
    'write_boundary': 'chain-pre-adapter/public-h-private only'
}
(HERE / 'PROVENANCE.json').write_text(json.dumps(packet, indent=2)+'\n', encoding='utf-8')
print(json.dumps({'provenance_sha256':sha(HERE/'PROVENANCE.json'),
                  'subject_sha256':sha(HERE/'INDEPENDENT-DERIVATION.md'),
                  'control_result_sha256':sha(HERE/'CONTROL-RESULTS.json')}))
