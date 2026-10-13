"""Verify byte-preserved research payload without running proof/crypto scripts."""
from pathlib import Path
import hashlib,json,re,sys
R=Path(__file__).resolve().parents[1]
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
manifest=json.loads((R/'snapshot/SOURCE-COPY-MANIFEST.json').read_text(encoding='utf8'))
seen=set()
for item in manifest['files']:
    rel=item['repository_path'];p=(R/rel).resolve()
    assert p.is_relative_to(R.resolve()) and rel not in seen
    seen.add(rel)
    assert item['source_sha256']==item['copy_sha256']==sha(p),rel
    assert p.stat().st_size==item['bytes'],rel
assert len(seen)==manifest['copied_files']
src=R/'publications/LULA-I/release/code/lula1/src/lib.rs'
assert sha(src)=='ac8e67f05af68dd8e1291c5909847f74103903fb7ffa2c70f500c6ec48f14210'
paper=R/'publications/LULA-I/LULA-I.pdf'
assert sha(paper)=='b036d61139ce8bc3d5cc0715e6e6b5e2174c80218c39d70e7bf6c5fa6cf48156'
x=R/'security/LULA-I-proof-20261012/extensions/shared-oracle-20261013'
assert (x/'UNIFORM-CLASSICAL-PROMOTION.json').is_file() and (x/'VALIDATION.json').is_file()
print(json.dumps({'status':'PASS_RECORDED_SNAPSHOT_BYTES','payload_files':len(seen),'payload_bytes':sum(i['bytes'] for i in manifest['files']),'paper_sha256':sha(paper),'crypto_source_sha256':sha(src),'proof_or_benchmark_runs':0,'portable_historical_proof_reproduction_claim':False}))
