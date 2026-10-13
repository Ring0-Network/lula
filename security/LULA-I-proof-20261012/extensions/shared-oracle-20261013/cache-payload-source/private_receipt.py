from hashlib import sha256
from pathlib import Path
import json

here = Path(__file__).resolve().parent
author = here.parent / 'private-challenge-program'
files = {
    'original_author_candidate': author / 'INDEPENDENT_DERIVATION.md',
    'corrected_author_successor': author / 'SUCCESSOR.md',
    'successor_provenance': author / 'SUCCESSOR-PROVENANCE.json',
    'original_gap_review': here / 'PRIVATE-CHALLENGE-REVIEW.md',
    'corrected_successor_review': here / 'PRIVATE-CHALLENGE-SUCCESSOR-REVIEW.md',
    'author_arithmetic_script': author / 'check_counts.py',
    'exact_copied_arithmetic_script': here / 'private_challenge_check_counts_copy.py',
    'reader_rerun_results': here / 'COUNT-CHECKS.json',
    'easycrypt_source': author / 'AdapterCounts.ec',
    'easycrypt_receipt': author / 'EASYCRYPT-CHECK.json',
    'easycrypt_log': author / 'easycrypt-check.log',
}
addendum = here / 'PRIVATE-CHALLENGE-FINAL-PIN-ADDENDUM.md'
if addendum.exists():
    files['final_pin_addendum'] = addendum
    files['final_author_successor'] = author / 'FINAL-SUCCESSOR.md'
    files['final_provenance'] = author / 'FINAL-PROVENANCE.json'
hashes = {name: {'path': str(path), 'sha256': sha256(path.read_bytes()).hexdigest()}
          for name, path in files.items()}
prov = json.loads(files['successor_provenance'].read_text(encoding='utf-8'))
assert prov['original_sha256'] == hashes['original_author_candidate']['sha256']
assert prov['successor_sha256'] == hashes['corrected_author_successor']['sha256']
assert hashes['author_arithmetic_script']['sha256'] == hashes['exact_copied_arithmetic_script']['sha256']
ec = json.loads(files['easycrypt_receipt'].read_text(encoding='utf-8'))
assert ec['exit_code'] == 0
assert ec['source_sha256'] == hashes['easycrypt_source']['sha256']
assert ec['log_sha256'] == hashes['easycrypt_log']['sha256']
res = json.loads(files['reader_rerun_results'].read_text(encoding='utf-8'))
assert res['script_sha256'] == hashes['exact_copied_arithmetic_script']['sha256']
assert len(res['q_columns']) == 8
current = hashes['corrected_author_successor']['sha256']
initial_reviewed = 'd5ed7d17dd8f7a2c5de76374a6894c6743b1b6b9205b10fe736237758f485336'
if current != initial_reviewed:
    assert addendum.exists() and current in addendum.read_text(encoding='utf-8')
if addendum.exists():
    final = json.loads(files['final_provenance'].read_text(encoding='utf-8'))
    assert final['reviewed_successor_sha256'] == current
    assert final['final_successor_sha256'] == hashes['final_author_successor']['sha256']
    assert final['final_successor_sha256'] in addendum.read_text(encoding='utf-8')
receipt = {
    'verdict': 'ACCEPT_MANUAL_JOINT_ACCESS_ROM_ADAPTER_IDENTITIES_AND_RESOURCE_CAPS',
    'scope': 'classical source-relative joint Raw/private ROM challenge; no conventional-PRF or Rust-refinement claim',
    'original_review_preserved': True,
    'eight_q_rows_reexecuted': True,
    'toy_worlds_reexecuted': res['toy_comparison_worlds'],
    'easycrypt_checked_declarations': len(ec['declarations']),
    'files': hashes,
}
(here / 'PRIVATE-CHALLENGE-REVIEW.json').write_text(json.dumps(receipt, indent=2) + '\n', encoding='utf-8')
print(receipt['verdict'])
