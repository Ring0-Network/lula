from pathlib import Path
from hashlib import sha256
import json

here = Path(__file__).resolve().parent
x = here.parent
index_path = x / 'PAYLOAD-PRIVATE-CURRENT-INDEX.json'
index = json.loads(index_path.read_text(encoding='utf-8'))
promotion_path = x / 'PAYLOAD-PRIVATE-PROMOTION.json'
promotion = json.loads(promotion_path.read_text(encoding='utf-8'))
docs = {name: sha256((x / name).read_bytes()).hexdigest() for name in index['documents']}
assert docs == index['documents']
for name, digest in promotion['new_artifacts'].items():
    assert sha256((x / name).read_bytes()).hexdigest() == digest
for receipt_name, digest in promotion['review_receipts'].items():
    receipt_path = x / receipt_name
    assert sha256(receipt_path.read_bytes()).hexdigest() == digest
    receipt = json.loads(receipt_path.read_text(encoding='utf-8'))
    for entry in receipt['files'].values():
        assert sha256(Path(entry['path']).read_bytes()).hexdigest() == entry['sha256']
result = {
    'verdict': 'ACCEPT_CORRECTED_PAYLOAD_PRIVATE_CURRENT_INDEX',
    'all_five_status_repairs_and_two_precision_repairs_closed': True,
    'payload_aware_internal_adapters_accepted': True,
    'same_sufficient_bounds_not_advantage_equality': True,
    'category_capacity_and_conventional_generic_obligations_still_open': True,
    'documents': docs,
    'promoted_artifacts': promotion['new_artifacts'],
    'prior_review_receipts': promotion['review_receipts'],
    'current_index_sha256': sha256(index_path.read_bytes()).hexdigest(),
    'preserved_promotion_sha256': sha256(promotion_path.read_bytes()).hexdigest(),
    'initial_integration_review_sha256': sha256((here / 'INTEGRATION-REVIEW.md').read_bytes()).hexdigest(),
    'initial_integration_receipt_sha256': sha256((here / 'INTEGRATION-REVIEW.json').read_bytes()).hexdigest(),
    'final_review_sha256': sha256((here / 'INTEGRATION-FINAL-REVIEW.md').read_bytes()).hexdigest(),
}
(here / 'INTEGRATION-FINAL-REVIEW.json').write_text(json.dumps(result, indent=2) + '\n', encoding='utf-8')
print(result['verdict'])
