from pathlib import Path
from hashlib import sha256
import json

here = Path(__file__).resolve().parent
x = here.parent
docs = ('PROOF.md','OPEN.md','TERM-TABLE.md','REQUIREMENT-MAP.md','HANDOFF.md','SECURITY-CRITERION.md')
promotion = json.loads((x / 'PAYLOAD-PRIVATE-PROMOTION.json').read_text(encoding='utf-8'))
pins = {name: sha256((x / name).read_bytes()).hexdigest() for name in docs}
for name, digest in pins.items():
    assert promotion['documents'][name] == digest
for name, digest in promotion['new_artifacts'].items():
    assert sha256((x / name).read_bytes()).hexdigest() == digest
result = {
    'verdict': 'NEEDS_CURRENT_STATUS_RECONCILIATION',
    'scientific_interface_and_probability_scope_accepted': True,
    'numeric_or_source_change_required': False,
    'documents': pins,
    'promoted_artifacts': promotion['new_artifacts'],
    'promotion_sha256': sha256((x / 'PAYLOAD-PRIVATE-PROMOTION.json').read_bytes()).hexdigest(),
    'review_sha256': sha256((here / 'INTEGRATION-REVIEW.md').read_bytes()).hexdigest(),
    'source_private_reviews_preserved': True,
}
(here / 'INTEGRATION-REVIEW.json').write_text(json.dumps(result, indent=2) + '\n', encoding='utf-8')
print(result['verdict'])
