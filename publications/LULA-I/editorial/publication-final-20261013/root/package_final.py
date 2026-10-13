"""Refresh only the local public delivery archives after the final article review."""
from pathlib import Path
import hashlib,importlib.util,json,shutil,zipfile

P=Path(__file__).resolve().parents[3];E=Path(__file__).resolve().parent;R=P/'release'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
B=E.parent/'baseline'
for name in ('MANIFEST.sha256','EVIDENCE-MANIFEST.sha256'):
    target=B/('release-'+name)
    if not target.exists():shutil.copy2(R/name,target)
old={line.split('  ',1)[1]:line.split('  ',1)[0] for line in (B/'release-EVIDENCE-MANIFEST.sha256').read_text(encoding='utf8').splitlines()}
changes={rel:{'before':pin,'after':sha(R/rel)} for rel,pin in old.items() if sha(R/rel)!=pin}
assert set(changes)=={'README.md','code/models/verify_paper_models.py'},changes
assert sha(R/'code/lula1/src/lib.rs')=='ac8e67f05af68dd8e1291c5909847f74103903fb7ffa2c70f500c6ec48f14210'
(R/'EVIDENCE-MANIFEST.sha256').write_text(''.join(f'{sha(R/rel)}  {rel}\n' for rel in sorted(old)),encoding='utf8')
spec=importlib.util.spec_from_file_location('public_manifest',R/'check_manifest.py')
manifest=importlib.util.module_from_spec(spec);spec.loader.exec_module(manifest)
paths=sorted(manifest.shipped_paths()-{'MANIFEST.sha256'})
(R/'MANIFEST.sha256').write_text(''.join(f'{sha(R/rel)}  {rel}\n' for rel in paths),encoding='utf8')
manifest.main()

public=['LULA-I.tex','references.bib','operating-model.tex','stability-results.tex',
        'comparison-results.tex','replay-results.tex','LULA-I.bbl','SUBMISSION_METADATA.json']
readme='''LULA I editable mechanism-paper source.

Build with pdflatex -interaction=nonstopmode -halt-on-error LULA-I.tex,
bibtex LULA-I, and two further pdflatex passes. Dependencies: llncs,
splncs04, CM-Super, algorithm2e, TikZ, placeins, booktabs and hyperref.
Both construction diagrams are vector TikZ figures in the TeX source.

Use the contact-bearing LULA-I.pdf delivered beside this archive for the
prepared ePrint submission. This source contains the same author contact.
The separate reproducibility archive has an intentionally contact-free
repository paper copy. No ePrint submission or public deposit is claimed.
The paper studies the mechanism and its conditional rollback transfer;
it does not establish full reference-signer or category-1 security.
'''
with zipfile.ZipFile(P/'LULA-I-source.zip','w',zipfile.ZIP_DEFLATED) as z:
    for name in public:z.write(P/name,name)
    z.writestr('README.txt',readme)
with zipfile.ZipFile(P/'LULA-I-release.zip','w',zipfile.ZIP_DEFLATED,compresslevel=9) as z:
    for rel in sorted(manifest.shipped_paths()):z.write(R/rel,rel)
with zipfile.ZipFile(P/'LULA-I-release.zip') as z:
    expected=manifest.shipped_paths()
    assert set(z.namelist())==expected
    assert all(hashlib.sha256(z.read(rel)).hexdigest()==sha(R/rel) for rel in expected)
    assert not any(part in {'private','__pycache__','target','.git','recomputed'} for rel in z.namelist() for part in Path(rel).parts)
    assert not any(Path(rel).suffix in {'.log','.aux','.out','.blg'} for rel in z.namelist())
records={name:{'bytes':(P/name).stat().st_size,'sha256':sha(P/name)} for name in ['LULA-I.pdf','LULA-I.tex','LULA-I-source.zip','LULA-I-release.zip','SUBMISSION_METADATA.json']}
result={'status':'PACKAGED_LOCAL_MECHANISM_PREPRINT_NO_REMOTE_PUBLICATION',
        'deliverables':records,'source_members':public+['README.txt'],
        'release_file_count':len(expected),'evidence_changes':changes,
        'all_other_preexisting_evidence_file_hashes_unchanged':True,
        'archive_file_bytes_match_manifest':True,'private_build_and_generated_scratch_excluded':True,
        'cryptographic_source_unchanged':True,
        'main_submission_pdf_has_author_contact':True,
        'repository_pdf_intentionally_contact_free':True,
        'public_repository_anonymous_access':'404; deposit not established',
        'full_security_goal_complete':False}
(E/'PACKAGING.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf8')
(P/'DELIVERABLES.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf8')
print(json.dumps({'status':result['status'],'release_files':len(expected),'archives':{n:records[n] for n in ('LULA-I-source.zip','LULA-I-release.zip')}}))
