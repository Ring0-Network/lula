"""Record an already authorized, independently reviewed intervening paper cut.
Reads the publication files; never edits them or the cryptographic source.
"""
from pathlib import Path
import hashlib,json
X=Path(__file__).resolve().parent.parent
P=X.parents[3]/'publications/LULA-I'
Z=P/'editorial/zenodo-release-20261013'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
prior=json.loads((X/'AUTHORIZED-EDITORIAL-DELTA-PUBLICATION-FINAL-20261013.json').read_text())
peer=json.loads((Z/'technical/POSTEDIT-REVIEW.json').read_text())
upload=json.loads((Z/'root/UPLOAD-FILES.json').read_text())
assert peer['verdict']=='ACCEPT_SCOPED_POSTEDIT_MANUSCRIPT_AND_SCRIPT'
assert peer['unresolved_findings']==0
assert sha(P/'release/code/lula1/src/lib.rs')=='ac8e67f05af68dd8e1291c5909847f74103903fb7ffa2c70f500c6ec48f14210'
expected={'LULA-I.tex':'7aab775544100ba0336d8539aaf13622e3a840981f3c567ca56f19fdc2a009bf',
 'LULA-I.pdf':'b036d61139ce8bc3d5cc0715e6e6b5e2174c80218c39d70e7bf6c5fa6cf48156',
 'stability-results.tex':'c9c1855c24f1d418ad53d4cef74d36a385145fd39644871687516ddcbe68e802'}
changes={n:{'before':prior['paper_changes'][n]['after'],'after':sha(P/n)} for n in expected}
assert all(changes[n]['after']==h for n,h in expected.items())
assert peer['subject_pins']['LULA-I.tex']==expected['LULA-I.tex']
assert peer['subject_pins']['stability-results.tex']==expected['stability-results.tex']
assert upload['upload_files']['LULA-I.pdf']['sha256']==expected['LULA-I.pdf']
patches=X/'root-parameter-uniform-classical/PRIOR-AUTHORIZED-PUBLICATION-CUT.json'
record={'status':'RECORD_OF_PRIOR_AUTHORIZED_EDITORIAL_CHANGES_NOT_NEW_PROOF_EDITS',
 'authorization':'User explicitly requested GitHub link after conclusion, removal of private hardware/OS identifiers, and 72MiB cache versus memory/security analysis before Zenodo upload.',
 'already_completed_deltas':['repository link','32GiB-only hardware sentence','guarded analytical 36MiB illustration and cache/parameter distinction'],
 'paper_changes':changes,'review_path':str(Z/'technical/POSTEDIT-REVIEW.json'),
 'review_sha256':sha(Z/'technical/POSTEDIT-REVIEW.json'),
 'upload_files_record_sha256':sha(Z/'root/UPLOAD-FILES.json'),
 'current_proof_turn_manuscript_or_crypto_edits':0,'remote_publication_performed':False}
assert not patches.exists(),'Do not overwrite provenance'
patches.write_text(json.dumps(record,indent=2)+'\n',encoding='utf8')
delta=X/'AUTHORIZED-EDITORIAL-DELTA-ZENODO-20261013.json'
assert not delta.exists(),'Do not overwrite prior editorial delta'
delta.write_text(json.dumps({'authorization':record['authorization'],'patches_path':str(patches),
 'patches_sha256':sha(patches),'paper_changes':changes},indent=2)+'\n',encoding='utf8')
print(json.dumps({'status':record['status'],'delta_sha256':sha(delta),'paper_changes_recorded':3,'new_paper_edits':0}))
