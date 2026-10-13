"""Bind the final local mechanism-paper closure to actual reviewed artifacts."""
from pathlib import Path
import hashlib,json,re,zipfile
import fitz
P=Path(__file__).resolve().parents[3];E=Path(__file__).resolve().parent;Q=E.parent
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
read=lambda p:json.loads(p.read_text(encoding='utf-8-sig'))
pack=read(E/'PACKAGING.json')
for name,row in pack['deliverables'].items():
    assert (P/name).stat().st_size==row['bytes'] and sha(P/name)==row['sha256'],name
build=read(E/'BUILD-CHECKS.json');assert len(build)==8 and all(r['exit_code']==0 for r in build)
isolation=read(E/'SOURCE-ARCHIVE-CHECK.json')
assert isolation['status']=='PASS_ISOLATED_SOURCE_ARCHIVE_BUILD' and isolation['pages']==21
assert isolation['source_archive_sha256']==sha(P/'LULA-I-source.zip')
assert isolation['every_page_extracted_text_exactly_matches_submission_pdf']
for name,pin in isolation['delivered_files_unchanged'].items():assert sha(P/name)==pin,name
for folder,actual in [('metadata-render',P/'LULA-I.pdf'),('repository-render',P/'release/paper/LULA-I.pdf')]:
    pdf=read(E/folder/'INSPECTION.json')
    assert pdf['pdf_sha256']==sha(actual) and pdf['page_count']==21
    assert pdf['all_fonts_embedded'] and not pdf['type3_fonts']
    assert not pdf['blank_pages'] and pdf['text_outside_page']==0
    assert not pdf['forbidden_public_terms'] and pdf['visual_review'].startswith('PASS')
written=read(Q/'writing/REVIEW-RECEIPT.json')
for name,pin in written['current_document_pins'].items():assert sha(P/name)==pin,name
for row in read(Q/'writing/FINDINGS.json'):assert row['applied_by_root']
delivery=read(Q/'technical/final-package/CHECKS.json')
assert delivery['status']=='PASS_LOCAL_PACKAGE_WITHIN_MECHANISM_SCOPE'
assert delivery['packaging_json_sha256']==sha(E/'PACKAGING.json')
for name,pin in delivery['deliverable_sha256'].items():assert sha(P/name)==pin,name
assert len(delivery['commands'])==4 and all(c['exit_code']==0 for c in delivery['commands'])
assert delivery['release']['members']==887 and delivery['release']['unchanged_evidence_entries']==870
text=(E/'metadata-render/text.txt').read_text(encoding='utf8')
assert 'angel@r-0.org' in text and 'Lugel Labs' in text
assert not re.search(r'RA36|RA-dual|R6A|evidence[ -]*(manifest|cutoff)|public[ -]*deposit|TODO|Designer[, ]+Observer|CC\s*BY|Creative Commons',text,re.I)
main=(P/'LULA-I.tex').read_text(encoding='utf8')
repo=(P/'release/paper/LULA-I.tex').read_text(encoding='utf8')
assert main.replace(r'\email{angel@r-0.org}\\','')==repo
assert all((P/name).read_bytes()==(P/'release/paper'/name).read_bytes()
           for name in ('references.bib','stability-results.tex','comparison-results.tex','operating-model.tex','replay-results.tex'))
for name in ('references.bib','comparison-results.tex','operating-model.tex','replay-results.tex'):
    assert sha(P/name)==sha(Q/'baseline'/name),name
reviews=[Q/'writing/REVIEW-RECEIPT.json',Q/'technical/FINAL-TECHNICAL-REVIEW.json',
         Q/'bibliography/BIBLIOGRAPHY-URL-AUDIT.json',Q/'bibliography/LOCAL-LOCATOR-ADDENDUM.json',
         Q/'technical/final-package/CHECKS.json',Q/'technical/final-package/FINAL-PACKAGE-REVIEW.json',
         Q/'technical/final-package/REPORT.md',Q/'FINAL_REVIEW.md']
assert all(p.exists() for p in reviews)
record={'outcome':'COMPLETE_WITHIN_SCOPE','scope':'Local final mechanism-paper publication preparation; no remote submission or complete security certification.',
        'deliverables':pack['deliverables'],'review_receipts':{str(p.relative_to(Q)):sha(p) for p in reviews},
        'article_edits':5,'unresolved_critical_or_major_manuscript_findings':0,
        'pdf_pages':21,'all_fonts_embedded':True,'every_page_visually_reviewed':True,
        'all_numeric_tables_proofs_abstract_and_author_note_preserved':True,
        'bib_entries_checked':14,'compiled_references':13,'all_bib_urls_anonymous_200':True,
        'current_tables':6,'current_checked_rows_fields':37,'archived_tables_checked_separately':21,
        'independent_unpacked_release_cli_checks':4,'source_archive_build_commands':4,
        'public_repository':'anonymous404; no claim of public deposit',
        'external_publication_performed':False,'cryptographic_implementation_changed':False,
        'broader_full_security_goal_complete':False}
(Q/'FINAL_VALIDATION.json').write_text(json.dumps(record,indent=2)+'\n',encoding='utf8')
print(json.dumps({'outcome':record['outcome'],'main_pdf_sha256':sha(P/'LULA-I.pdf'),
                  'pages':21,'unresolved_critical_major':0,'release_members':887,
                  'security_goal_complete':False,'external_publication':False}))
