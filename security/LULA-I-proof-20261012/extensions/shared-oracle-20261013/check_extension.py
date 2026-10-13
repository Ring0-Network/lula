"""Checks the extension without modifying the frozen security packet or paper."""
from pathlib import Path
import hashlib
import json
import subprocess
import sys

X = Path(__file__).resolve().parent
S = X.parents[1]
P = S.parents[1] / 'publications/LULA-I'
sha = lambda f: hashlib.sha256(f.read_bytes()).hexdigest()
BASE = X / 'PRESERVATION-BASELINE.json'

def snapshot():
    frozen = {str(f.relative_to(S)): sha(f) for f in S.rglob('*')
              if f.is_file() and not f.is_relative_to(S / 'extensions')}
    paper = {n: sha(P / n) for n in ['LULA-I.tex', 'LULA-I.pdf', 'comparison-results.tex',
             'stability-results.tex', 'operating-model.tex', 'replay-results.tex', 'references.bib']}
    crypto = {str(f['path']): sha(Path(f['path'])) for f in json.loads((S / 'BASELINE.json').read_text())
              if str(f['path']).endswith('lib.rs')}
    return {'frozen_packet': frozen, 'current_paper': paper, 'crypto': crypto}

if sys.argv[1] == 'baseline':
    assert not BASE.exists(), 'Do not replace an existing baseline'
    BASE.write_text(json.dumps(snapshot(), indent=2) + '\n', encoding='utf8')
    print('CURRENT_EXTENSION_PRESERVATION_BASELINE_SAVED')
elif sys.argv[1] == 'preservation':
    expected = json.loads(BASE.read_text(encoding='utf8'))
    actual = snapshot()
    assert actual['frozen_packet'] == expected['frozen_packet'], 'Frozen security packet changed'
    assert actual['crypto'] == expected['crypto'], 'Cryptographic source changed'
    paper_expected = dict(expected['current_paper'])
    editorial_paths = [X / 'AUTHORIZED-EDITORIAL-DELTA.json',
                       X / 'AUTHORIZED-EDITORIAL-DELTA-20261013.json',
                       X / 'AUTHORIZED-EDITORIAL-DELTA-PUBLICATION-FINAL-20261013.json',
                       X / 'AUTHORIZED-EDITORIAL-DELTA-ZENODO-20261013.json']
    for editorial_path in editorial_paths:
        if not editorial_path.exists():
            continue
        editorial = json.loads(editorial_path.read_text(encoding='utf8'))
        assert sha(Path(editorial['patches_path'])) == editorial['patches_sha256']
        for name, change in editorial['paper_changes'].items():
            assert name in paper_expected and paper_expected[name] == change['before']
            paper_expected[name] = change['after']
    assert actual['current_paper'] == paper_expected, 'Unrecorded manuscript drift'
    old = json.loads((S / 'BASELINE.json').read_text())
    for item in old:
        if item['path'].endswith('lib.rs'):
            assert sha(Path(item['path'])) == item['sha256']
    record = {'status': 'PASS_FROZEN_PACKET_CRYPTO_PRESERVED_AND_AUTHORIZED_PAPER_CUT',
              'frozen_files': len(actual['frozen_packet']), 'crypto_pins_match_old_packet': True,
              'original_extension_baseline_retained': True,
              'intervening_editorial_deltas': [str(path) for path in editorial_paths if path.exists()],
              'historical_paper_cut': 'Old BASELINE.json predates authorized editorial work; not current paper baseline.'}
    (X / 'PRESERVATION.json').write_text(json.dumps(record, indent=2) + '\n', encoding='utf8')
    print(json.dumps(record))
else:
    raise ValueError(sys.argv[1])
