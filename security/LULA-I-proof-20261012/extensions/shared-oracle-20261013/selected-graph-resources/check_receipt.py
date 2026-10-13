from pathlib import Path
import json,hashlib
HERE=Path(__file__).resolve().parent
r=json.loads((HERE/'REVIEW-RECEIPT.json').read_text())
for category,base in [('subject_pins',HERE.parent),('own_pins',HERE)]:
    for name,pin in r[category].items():
        assert hashlib.sha256((base/name).read_bytes()).hexdigest()==pin,(category,name)
initial=json.loads((HERE/'INDEPENDENT-MANIFEST.json').read_text())
for name,pin in initial['files'].items():
    assert hashlib.sha256((HERE/name).read_bytes()).hexdigest()==pin,('initial',name)
print(json.dumps({'outcome':'PASS_CURRENT_SUBJECT_AND_INDEPENDENT_RECEIPT_PINS',
                  'subject_files':len(r['subject_pins']),'own_review_files':len(r['own_pins']),
                  'initial_files':len(initial['files'])}))
