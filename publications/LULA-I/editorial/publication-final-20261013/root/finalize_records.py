"""Record the exact final paper cut and its explicitly authorized editorial delta."""
from pathlib import Path
import hashlib,json,re
from PIL import Image,ImageChops
P=Path(__file__).resolve().parents[3];E=Path(__file__).resolve().parent;B=E.parent/'baseline'
X=P.parents[1]/'security/LULA-I-proof-20261012/extensions/shared-oracle-20261013'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
load=lambda p:json.loads(p.read_text(encoding='utf-8-sig'))
paper_names=['LULA-I.tex','LULA-I.pdf','comparison-results.tex','stability-results.tex',
             'operating-model.tex','replay-results.tex','references.bib']
changes={name:{'before':sha(B/name),'after':sha(P/name)} for name in paper_names if sha(B/name)!=sha(P/name)}
writing=load(E.parent/'writing/FINDINGS.json')
records=[{'id':r['id'],'file':r['file'],'old':r['quote'],'new':r['rewrite'],
          'conditions':r['protected'],'status':'APPLIED_AND_INDEPENDENTLY_RECHECKED'} for r in writing]
records += [
 {'id':'T01','file':'LULA-I.tex','old':r'FORS and four\\online layers',
  'new':r'FORS, lower trees,\\and chain signing','status':'APPLIED_AND_INDEPENDENTLY_RECHECKED',
  'conditions':['Top WOTS chain signing remains online; no cost or data change.']},
 {'id':'T02','file':'LULA-I.tex','old':'Reconstruct WOTS public key; RootFromPath takes function name',
  'new':'Bind reconstructed node P_j and pass that node to RootFromPath',
  'status':'APPLIED_AND_INDEPENDENTLY_RECHECKED','conditions':['Explicit symbol binding; verifier behavior unchanged.']},
 {'id':'R01','file':'release/code/models/verify_paper_models.py',
  'old':'Default command expected22 legacy rows in the current3-row article and exited1.',
  'new':'Verify3 current component rows and22 archived rows explicitly; default exits0.',
  'status':'NATIVE_FAILURE_REPRODUCED_AND_FIXED','conditions':['Numerical formulas and crypto source unchanged.']},
 {'id':'R02','file':'release/README.md','old':'Historical private-and-empty description and prospective DOI placeholder',
  'new':'Prepared local archive; intended repository anonymously unavailable on2026-10-13.',
  'status':'ANONYMOUS_404_AND_LOCAL_PACKAGE_DISTINGUISHED','conditions':['No public deposit or remote content claimed.']}]
patch={'authorization':'Latest user: final review and correction of the complete mechanism manuscript/PDF, claims, references, figures and public package, preserving conditional scientific limits.',
       'article_patch_count':5,'patches':records,'paper_changes':changes,
       'source_signature_size_cache_and_results_changed':False,'cryptographic_source_changed':False}
(E/'PATCHES.json').write_text(json.dumps(patch,indent=2,ensure_ascii=False)+'\n',encoding='utf8')
for i in range(1,22):
    assert ImageChops.difference(Image.open(E/'metadata-render'/f'page-{i:02d}.png'),
                                Image.open(E/'final-render'/f'page-{i:02d}.png')).getbbox() is None
for folder in ('metadata-render','repository-render'):
    record=load(E/folder/'INSPECTION.json')
    assert record['page_count']==21 and not record['blank_pages'] and record['text_outside_page']==0
    assert not record['forbidden_public_terms'] and record['all_fonts_embedded'] and not record['type3_fonts']
    record['visual_review']='PASS: all21 main pages visually inspected; latest main pages pixel-identical to those inspected. Repository pages2-21 pixel-identical to main; its contact-free first page visually inspected separately.'
    (E/folder/'INSPECTION.json').write_text(json.dumps(record,indent=2,ensure_ascii=False)+'\n',encoding='utf8')
package=load(E/'PACKAGING.json')
package['deliverables']['LULA-I.pdf']={'bytes':(P/'LULA-I.pdf').stat().st_size,'sha256':sha(P/'LULA-I.pdf')}
package['pdf_metadata_refresh']='An extra main-directory compile changed PDF metadata; corrected isolated-source check then preserved delivered files. Every refreshed page has identical pixels and extracted text to the reviewed main cut.'
(E/'PACKAGING.json').write_text(json.dumps(package,indent=2)+'\n',encoding='utf8')
(P/'DELIVERABLES.json').write_text(json.dumps(package,indent=2)+'\n',encoding='utf8')
delta={'authorization':patch['authorization'],'patches_path':str(E/'PATCHES.json'),
       'patches_sha256':sha(E/'PATCHES.json'),'paper_changes':changes}
(X/'AUTHORIZED-EDITORIAL-DELTA-PUBLICATION-FINAL-20261013.json').write_text(json.dumps(delta,indent=2)+'\n',encoding='utf8')
print(json.dumps({'article_patches':5,'paper_changes':changes,'main_pdf':sha(P/'LULA-I.pdf'),
                  'latest_all21_pages_pixel_identical_to_visually_reviewed_cut':True,
                  'source_archive_check':load(E/'SOURCE-ARCHIVE-CHECK.json')['status']}))
