from pathlib import Path
import hashlib,json,re
B=Path(__file__).resolve().parent;P=B.parents[2]
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
scope=json.loads((B/'READ-SCOPE.json').read_text(encoding='utf-8'))
expected_current={**scope['manuscript_pins'],
 'LULA-I.tex':'3ef61931c2feb57e05ae28171a693801c131a9b1edee59956e477384985d27c8',
 'stability-results.tex':'7bf5af933b82d89dab647d784d07598276c0c56693dc795001e4da1aec9671b7'}
for n,h in scope['manuscript_pins'].items():
    assert sha(B/'baseline'/n)==h,('frozen baseline changed',n)
    assert sha(P/n)==expected_current[n],('unreviewed current successor',n)
closure=[]
def visit(n):
    if n in closure:return
    closure.append(n)
    text=(P/n).read_text(encoding='utf-8')
    for inc in re.findall(r'\\input\{([^}]+)\}',text):visit(inc if inc.endswith('.tex') else inc+'.tex')
visit('LULA-I.tex')
assert set(closure)==set(['LULA-I.tex','operating-model.tex','stability-results.tex','comparison-results.tex'])
text='\n'.join((P/n).read_text(encoding='utf-8') for n in closure)
abstract=(P/'LULA-I.tex').read_text(encoding='utf-8').split(r'\begin{abstract}',1)[1].split(r'\keywords',1)[0]
assert len(abstract.split())==94
labels=set(re.findall(r'\\label\{([^}]+)\}',text))
refs={x.strip() for group in re.findall(r'\\(?:Cref|ref|eqref)\{([^}]+)\}',text) for x in group.split(',')}
citations={x.strip() for group in re.findall(r'\\cite(?:\[[^\]]*\])?\{([^}]+)\}',text) for x in group.split(',')}
bib={x.strip() for x in re.findall(r'@\w+\{([^,]+),',(P/'references.bib').read_text(encoding='utf-8'))}
assert not refs-labels and not citations-bib
retired=re.findall(r'RA36|evidence[- ]manifest|evidence cutoff|public deposit|TODO|CC BY',text,re.I)
assert not retired
findings=[dict(id='W01',severity='MINOR',file='LULA-I.tex',line=51,
    quote='A resource that appears unused in every restored execution may nevertheless have been exposed in another branch.',
    rewrite='A resource that appears unused after restoration may already have been exposed in another branch.',
    protected=['apparent unused status','possible exposure on another branch','permanent adversarial observations'],
    action='RECOMMENDED_LOCAL_EXPRESSION_ONLY'),
 dict(id='W02',severity='MINOR',file='LULA-I.tex',line=55,
    quote='The intended use objective is $2^{40}$ signing queries across all branches, conditional on a still-unestablished full reference-signer bound.',
    rewrite='The intended use objective is $2^{40}$ signing queries across all branches, conditional on a full reference-signer bound that has not yet been established.',
    protected=['2^40 is conditional use objective','all branches','full reference bound unestablished'],
    action='OPTIONAL_LOCAL_REGISTER_POLISH'),
 dict(id='W03',severity='MINOR',file='stability-results.tex',line=23,
    quote='Cache availability has a larger effect on first-use latency than on signature size.',
    rewrite='Under the honest-cache model, cache availability affects first-use latency but leaves serialized signature size unchanged.',
    protected=['honest cache interface','terminating returned signatures','all measured values and individual-observation limitations'],
    action='RECOMMENDED_LOCAL_PRECISION_ONLY')]
for f in findings:
    line=(B/'baseline'/f['file']).read_text(encoding='utf-8').splitlines()[f['line']-1]
    assert f['quote'] in line,f['id']
    assert f['rewrite'] in (P/f['file']).read_text(encoding='utf-8').splitlines()[f['line']-1]
    f['source_sha256']=sha(B/'baseline'/f['file']);f['applied_by_root']=True
    f['reviewer_applied']=False
(B/'FINDINGS.json').write_text(json.dumps(findings,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
coverage={}
for skill,files in scope['skill_pins'].items():
    root=Path('C:/Users/angel/.agents/skills')/skill
    coverage[skill]=[dict(path=str(root/n).replace('\\','/'),sha256=h,status='READ_IN_FULL') for n,h in files.items()]
    for f in coverage[skill]:assert sha(Path(f['path']))==f['sha256']
assert len(coverage['writing-skill'])==103 and len(coverage['phd-paper-review'])==25
paper=[dict(file=n,sha256=sha(P/n),baseline_sha256=sha(B/'baseline'/n),lines=len((P/n).read_text(encoding='utf-8').splitlines()),status='BASELINE_READ_IN_FULL_CURRENT_ALLOWLIST_DIFF_REVIEWED') for n in scope['manuscript_pins']]
# Root is sole editor: prove that exactly the three recommended substitutions plus
# two explicitly notified technical presentation substitutions explain the successor.
main=(B/'baseline/LULA-I.tex').read_text(encoding='utf-8')
for f in findings:
    if f['file']=='LULA-I.tex':main=main.replace(f['quote'],f['rewrite'])
main=main.replace('Reconstruct WOTS public key by completing each chain',
    'Reconstruct the WOTS public key $P_j$ by completing each chain')
main=main.replace(r'\mathsf{RootFromPath}(j,t_j,q_j,\mathsf{WotsPK},\mathsf{path}_j)',
    r'\mathsf{RootFromPath}(j,t_j,q_j,P_j,\mathsf{path}_j)')
main=main.replace(r'{FORS and four\\online layers}',r'{FORS, lower trees,\\and chain signing}')
assert main==(P/'LULA-I.tex').read_text(encoding='utf-8'),'main allowlist incomplete'
stability=(B/'baseline/stability-results.tex').read_text(encoding='utf-8')
f=findings[2];stability=stability.replace(f['quote'],f['rewrite'])
assert stability==(P/'stability-results.tex').read_text(encoding='utf-8')
oldtext='\n'.join((B/'baseline'/n).read_text(encoding='utf-8') for n in closure)
assert re.findall(r'\d+(?:[,.]\d+)*',oldtext)==re.findall(r'\d+(?:[,.]\d+)*',text)
for env in ['table','lemma','theorem','proof','equation','align']:
    pat=r'\\begin\{'+env+r'\}.*?\\end\{'+env+r'\}'
    assert re.findall(pat,oldtext,re.S)==re.findall(pat,text,re.S),env
oldabstract=(B/'baseline/LULA-I.tex').read_text(encoding='utf-8').split(r'\begin{abstract}',1)[1].split(r'\keywords',1)[0]
assert oldabstract==abstract
note='I named it LULA because I felt like it. Sorry, friends---I need to have some fun sometimes.'
assert note in text and note in oldtext
out=dict(outcome='COMPLETE_WITHIN_SCOPE_READ_ONLY_PROSE_REVIEW',skill_coverage=coverage,
    writing_nodes=95,writing_assets=7,phd_nodes=24,skills_entrypoints=2,paper_coverage=paper,
    recursive_article_include_closure=closure,
    figures_tables_algorithms_theorems_and_proofs_read=True,
    article_environment_counts={env:len(re.findall(r'\\begin\{'+env+r'\}',text)) for env in ['algorithm','figure','table','lemma','theorem','proof']},
    scientific_claims_independently_proved_in_this_review=False,experiment_data_rerun=False,
    Li_example=dict(path='C:/Users/angel/Desktop/paper/PAPERS/references/pdfs/li_crypto2025/li_crypto2025.tex',
      access='Title and section hierarchy, introduction/contributions lines92–190, efficiency/performance lines1297–1318; structure/register comparison only, not full Li mathematics review.'),
    external_research_access=[dict(url='https://arxiv.org/html/2410.16107v2',access='Abstract and opening methods/results returned by live primary HTML opening.'),
      dict(url='https://arxiv.org/html/2603.18161v1',access='Abstract and selected grammar-editing passages returned by primary HTML find. Preprint; not whole-paper replication.')],
    findings=dict(CRITICAL=0,MAJOR=0,MINOR=3),current_unresolved_findings=dict(CRITICAL=0,MAJOR=0,MINOR=0),no_AI_authorship_inference=True,
    manual_checks=['All32 structural-pattern categories considered with keep-when counterinterpretations.',
      'All8 PhD writing dimensions assessed; source claims and limits matched across abstract/introduction/theorem/results/conclusion.',
      'Each proposed exact quote matched to current frozen source line; rewrite conditions recorded.',
      'Root presentation-only verifier P_j and diagram edits manually reviewed; theorem/proof/table/equation/align bodies,numeric strings,abstract and Note identical.'],
    automated_checks=dict(abstract_whitespace_words=94,missing_reference_targets=sorted(refs-labels),
      unknown_citation_keys=sorted(citations-bib),cited_keys=len(citations),bibliography_source_records=len(bib),retired_workflow_matches=retired,
      frozen_baselines_unchanged=True,current_successor_exact_patch_allowlist_passed=True,
      numeric_strings_math_theorems_proofs_tables_abstract_Note_preserved=True),
    unperformed=['No manuscript edit','No TeX compile','No PDF render review','No URL/bibliography fact-check','No new mathematical proof or model-checker execution','No benchmark rerun','No publication/upload'],
    open_author_questions=[],recommendations_applied_by_root=True,reviewer_edited_manuscript=False,
    root_is_sole_editor=True,whole_security_proof_goal_complete=False)
(B/'COVERAGE.json').write_text(json.dumps(out,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
lines=['# Read coverage','','95 writing reference nodes,7 writing assets,24 PhD reference nodes and2 entrypoints read in full. The following inventory is actual reading coverage, not a claim that each node produced a defect.','']
for skill,files in coverage.items():
    lines+=['## '+skill,'','|Path|SHA256|Status|','|---|---|---|']
    for f in files:lines.append(f"|{f['path']}|{f['sha256']}|READ_IN_FULL|")
lines+=['','## Article','','Recursive closure: '+', '.join(closure)+'.','',
 'The main515lines and every included line were read, including captions, equations,algorithms,proofs and appendix. Bibliography source and academic structure were read; inactive replay source is empty. The Li example and external research access limits are explicit in COVERAGE.json.']
(B/'COVERAGE.md').write_text('\n'.join(lines)+'\n',encoding='utf-8')
receipt=dict(outcome=out['outcome'],review_sha256=sha(B/'REVIEW.md'),findings_sha256=sha(B/'FINDINGS.json'),coverage_sha256=sha(B/'COVERAGE.json'),
    baseline_pins=scope['manuscript_pins'],current_document_pins=expected_current,counts=out['findings'],current_unresolved_counts=out['current_unresolved_findings'],checks=out['automated_checks'],recommendations_applied_by_root=True,
    root_is_sole_editor=True,whole_security_proof_goal_complete=False)
(B/'REVIEW-RECEIPT.json').write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf-8')
print(json.dumps(dict(outcome=out['outcome'],counts=out['findings'],skill_files=128,abstract_words=94,
    recursive_includes=closure,missing_refs=sorted(refs-labels),unknown_citations=sorted(citations-bib),
    receipt_sha256=sha(B/'REVIEW-RECEIPT.json'),reviewer_edited_manuscript=False)))
