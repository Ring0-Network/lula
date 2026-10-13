from pathlib import Path
from hashlib import sha256
import json
here = Path(__file__).resolve().parent
files = {
    'prior_independent_source_derivation': here / 'INDEPENDENT_DERIVATION.md',
    'reviewed_author_candidate': here.parent / 'cache-payload-math/INDEPENDENT_DERIVATION.md',
    'independent_second_reading': here / 'SECOND_READER.md',
    'layout_factorization_control': here / 'control.py',
    'control_results': here / 'CONTROL-RESULTS.json',
    'pinned_library': here.parents[4] / 'publications/LULA-I/release/code/lula1/src/lib.rs',
    'private_fixture_serializer': here.parents[4] / 'publications/LULA-I/release/code/lula1/src/bin/lula1_driver_original.rs',
}
data = {
    'verdict': 'ACCEPT_MANUAL_EXACT_PUBLIC_LOGICAL_PAYLOAD_EXTENSION_WITH_UNCHANGED_FINITE_MODEL_BOUNDS',
    'subject': '75,497,456-byte top logical nodes and canonical counters; no seed/context/work buffers',
    'source_first': True,
    'new_sibling_candidate_opened_after_own_derivation_saved': True,
    'reviewed_entire_author_candidate': True,
    'full_crypto_execution_or_cache_generation': False,
    'efficient_pk_plus_oracle_simulator_established': False,
    'fixed_sha_or_category_established': False,
    'files': {name: {'path': str(path), 'sha256': sha256(path.read_bytes()).hexdigest()}
              for name, path in files.items()},
}
assert data['files']['pinned_library']['sha256'] == 'ac8e67f05af68dd8e1291c5909847f74103903fb7ffa2c70f500c6ec48f14210'
(here / 'REVIEW.json').write_text(json.dumps(data, indent=2) + '\n', encoding='utf-8')
print(data['verdict'])
