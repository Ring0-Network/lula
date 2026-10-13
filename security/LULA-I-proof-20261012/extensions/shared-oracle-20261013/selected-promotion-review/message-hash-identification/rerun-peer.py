import hashlib
from pathlib import Path
HERE=Path(__file__).resolve().parent
X=HERE.parents[1]
PEER=X/'outside-field-check/message-hash-identification'
SCRIPT=PEER/'controls.py'
assert hashlib.sha256((PEER/'INDEPENDENT-FIRST.md').read_bytes()).hexdigest()=='b07700807df0f78be2272afd7a5372044603b92697b3760afaa8cdfac5a3a1df'
assert hashlib.sha256(SCRIPT.read_bytes()).hexdigest()=='aad568f06c0ab13d3ba23de8e3bd1238885bf1065bbd50fd5b07a23256e2ef53'
DEST=HERE/'peer-rerun'
DEST.mkdir(exist_ok=True)
code=SCRIPT.read_text(encoding='utf-8')
needle="out = HERE / 'CONTROL-RESULTS.json'"
assert code.count(needle)==1
code=code.replace(needle,"out = REVIEW_DEST / 'CONTROL-RESULTS.json'")
exec(compile(code,str(SCRIPT),'exec'),{'__file__':str(SCRIPT),'REVIEW_DEST':DEST})
assert (DEST/'CONTROL-RESULTS.json').read_bytes()==(PEER/'CONTROL-RESULTS.json').read_bytes()
print('PEER_CONTROL_BYTE_IDENTICAL; no peer files edited')
