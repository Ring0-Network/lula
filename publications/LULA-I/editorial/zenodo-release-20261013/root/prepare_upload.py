"""Prepare only the privacy-reviewed paper/source pair for the requested Zenodo upload."""
from pathlib import Path
import hashlib,json,re,shutil,zipfile,importlib.util
P=Path(__file__).resolve().parents[3];E=Path(__file__).resolve().parent;B=E.parent/'baseline';R=P/'release'
OUT=P/'zenodo-upload';OUT.mkdir(exist_ok=True)
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
description="LULA I separates hash-based signing from its reusable cache. The paper specifies honest-restoration agreement, a conditional rollback-security transfer, and the memory and recovery tradeoffs. Full reference-signer security remains open.\n\nRing0 Labs\nangel@r-0.org\nPublished by Lugel Labs"
(OUT/'description.txt').write_text(description+'\n',encoding='utf8')
metadata={'title':'LULA I: Rollback-Resilient Hash-Based Signatures with Cache-Accelerated Signing',
          'resource_type':'Publication / Preprint','creators':[{'name':'Gonzalez, Luis Ángel','affiliation':'Ring0 Labs'}],
          'publisher':'Lugel Labs','contact':'angel@r-0.org','description':description,
          'keywords':['Hash-based signatures','Rollback','Caching','WOTS+C','FORS+C'],
          'language':'English','license':'Creative Commons Attribution4.0 International',
          'project_repository':'https://github.com/Ring0-Network/lula',
          'planned_files':['LULA-I.pdf','LULA-I-source.zip'],
          'upload_state':'NOT_UPLOADED_BROWSER_CONTROL_RUNTIME_FAILED'}
(OUT/'metadata.json').write_text(json.dumps(metadata,indent=2,ensure_ascii=False)+'\n',encoding='utf8')
public=['LULA-I.tex','references.bib','operating-model.tex','stability-results.tex',
        'comparison-results.tex','replay-results.tex','LULA-I.bbl']
helper=R/'code/models/cache_memory_tradeoff.py'
readme='''LULA I editable manuscript and analytical cache illustration.

Build: pdflatex -interaction=nonstopmode -halt-on-error LULA-I.tex;
bibtex LULA-I; then pdflatex twice. Requires llncs/splncs04, CM-Super,
algorithm2e, TikZ, placeins, booktabs and hyperref. Both figures are vector TikZ.
The author contact is intentional. No machine inventory, telemetry, private
research notes, benchmark logs, keys or cache files are included.

Optional: python -I -B cache_memory_tradeoff.py (mpmath1.3.0) reproduces
the analytical height illustration. It creates no signatures or measurements.
Its figures are FORS component-model exponents, not full-security guarantees.
The evaluated construction's complete reference-signer bound remains open.
'''
with zipfile.ZipFile(P/'LULA-I-source.zip','w',zipfile.ZIP_DEFLATED) as z:
    for name in public:z.write(P/name,name)
    z.write(helper,'cache_memory_tradeoff.py')
    z.writestr('README.txt',readme)
shutil.copy2(P/'LULA-I.pdf',OUT/'LULA-I.pdf')
shutil.copy2(P/'LULA-I-source.zip',OUT/'LULA-I-source.zip')
privacy=re.compile(r'Intel|Core Ultra|255U|Windows 11|C:\\Users\\|/Users/|RA36|R6A|evidence[- ]manifest|public deposit to.?do|TODO',re.I)
with zipfile.ZipFile(OUT/'LULA-I-source.zip') as z:
    assert len(z.namelist())==9
    for name in z.namelist():
        assert Path(name).name==name
        assert not privacy.search(z.read(name).decode('utf8')),name

# Refresh the local reproduction archive as well, but it is NOT an upload file:
# its retained research records include machine details the author excludes here.
old={line.split('  ',1)[1]:line.split('  ',1)[0] for line in (B/'EVIDENCE-MANIFEST.sha256').read_text().splitlines()}
assert all(sha(R/rel)==pin for rel,pin in old.items()),'Unexpected preexisting evidence change'
evidence=sorted(set(old)|{'code/models/cache_memory_tradeoff.py'})
(R/'EVIDENCE-MANIFEST.sha256').write_text(''.join(f'{sha(R/rel)}  {rel}\n' for rel in evidence),encoding='utf8')
spec=importlib.util.spec_from_file_location('manifest',R/'check_manifest.py');m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
paths=sorted(m.shipped_paths()-{'MANIFEST.sha256'})
(R/'MANIFEST.sha256').write_text(''.join(f'{sha(R/rel)}  {rel}\n' for rel in paths),encoding='utf8')
m.main()
with zipfile.ZipFile(P/'LULA-I-release.zip','w',zipfile.ZIP_DEFLATED,compresslevel=9) as z:
    for rel in sorted(m.shipped_paths()):z.write(R/rel,rel)
record={'status':'READY_LOCAL_PRIVACY_REVIEWED_PAPER_SOURCE_PAIR_ZENODO_UPLOAD_PENDING',
        'upload_files':{name:{'bytes':(OUT/name).stat().st_size,'sha256':sha(OUT/name)} for name in metadata['planned_files']},
        'source_members':public+['cache_memory_tradeoff.py','README.txt'],
        'raw_research_archive_selected_for_upload':False,
        'all_preexisting_research_evidence_unchanged':True,
        'new_evidence_file':'code/models/cache_memory_tradeoff.py',
        'crypto_source_unchanged':sha(R/'code/lula1/src/lib.rs')=='ac8e67f05af68dd8e1291c5909847f74103903fb7ffa2c70f500c6ec48f14210',
        'repository_anonymous_status':'404; neutral requested project link, no availability claim',
        'publication_performed':False}
(E/'UPLOAD-FILES.json').write_text(json.dumps(record,indent=2)+'\n',encoding='utf8')
(P/'DELIVERABLES.json').write_text(json.dumps(record,indent=2)+'\n',encoding='utf8')
print(json.dumps(record))
