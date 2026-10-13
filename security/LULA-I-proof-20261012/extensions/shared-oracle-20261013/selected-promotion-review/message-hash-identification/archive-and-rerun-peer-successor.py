import hashlib
from pathlib import Path
HERE=Path(__file__).resolve().parent
X=HERE.parents[1]
PEER=X/'outside-field-check/message-hash-identification'
SCRIPT=PEER/'controls.py'
assert hashlib.sha256(SCRIPT.read_bytes()).hexdigest()=='8b982db26e6ab041b3dfcfbe31a38d409e3d059b31a80671acb1eed6b615dd7b'
code=SCRIPT.read_bytes().decode('utf-8')
start=code.index('# A second separation')
end=code.index('# Fresh nonce',start)
old=code[:start]+code[end:]
old=''.join(line for line in old.splitlines(keepends=True) if "'two_nonce_" not in line)
recovered=hashlib.sha256(old.encode('utf-8')).hexdigest()=='aad568f06c0ab13d3ba23de8e3bd1238885bf1065bbd50fd5b07a23256e2ef53'
if recovered:
    ARCHIVE=HERE/'peer-controls-historical-aad568.py'
    ARCHIVE.write_bytes(old.encode('utf-8'))
DEST=HERE/'peer-rerun-successor'
DEST.mkdir(exist_ok=True)
needle="out = HERE / 'CONTROL-RESULTS.json'"
assert code.count(needle)==1
redirected=code.replace(needle,"out = REVIEW_DEST / 'CONTROL-RESULTS.json'")
exec(compile(redirected,str(SCRIPT),'exec'),{'__file__':str(SCRIPT),'REVIEW_DEST':DEST})
assert (DEST/'CONTROL-RESULTS.json').read_bytes()==(PEER/'CONTROL-RESULTS.json').read_bytes()
print('SUCCESSOR_BYTE_IDENTICAL_EXIT0; historical_source_recovered='+str(recovered))
