"""Read-only scoped post-edit review; outputs only beside this file."""
from pathlib import Path
import difflib,hashlib,json,re,subprocess,sys
import mpmath as mp
P=Path(r'C:\Users\angel\Desktop\paper\PAPERS\LUGEL\research\lula22\publications\LULA-I')
O=Path(__file__).parent
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
old=P/'editorial/publication-final-20261013/root/source-archive-build'
assert sha(old/'LULA-I.tex')=='3ef61931c2feb57e05ae28171a693801c131a9b1edee59956e477384985d27c8'
assert sha(old/'stability-results.tex')=='7bf5af933b82d89dab647d784d07598276c0c56693dc795001e4da1aec9671b7'
assert sha(P/'LULA-I.tex')=='7aab775544100ba0336d8539aaf13622e3a840981f3c567ca56f19fdc2a009bf'
a=(old/'LULA-I.tex').read_text(encoding='utf8');b=(P/'LULA-I.tex').read_text(encoding='utf8')
sa=(old/'stability-results.tex').read_text(encoding='utf8');sb=(P/'stability-results.tex').read_text(encoding='utf8')
diff=''.join(difflib.unified_diff(a.splitlines(True),b.splitlines(True),fromfile='accepted-pre-edit/LULA-I.tex',tofile='current/LULA-I.tex'))
diff+=''.join(difflib.unified_diff(sa.splitlines(True),sb.splitlines(True),fromfile='accepted-pre-edit/stability-results.tex',tofile='current/stability-results.tex'))
(O/'POSTEDIT-DIFF.txt').write_text(diff,encoding='utf8')
def env(text,name):return re.findall(r'\\begin\{'+name+r'\}.*?\\end\{'+name+r'\}',text,re.S)
for e in ['abstract','lemma','theorem','proof','algorithm','table']:
    assert env(a,e)==env(b,e),e
assert a[a.index(r'\paragraph{Note:}'):]==b[b.index(r'\paragraph{Note:}'):]
for f in ['operating-model.tex','comparison-results.tex','references.bib']:
    assert (P/f).read_bytes()==(old/f).read_bytes(),f
assert env(sa,'table')==env(sb,'table')
# The original article differs only by parameter-scope clarification, new
# subsection, and the requested neutral repository line.
newsection=re.search(r'\\subsection\{Less cache memory and the security claim\}.*?(?=\\section\{Signature format)',b,re.S)[0]
without=b.replace(newsection,'\n\n\n')
paramold=a.splitlines()[129];paramnew=b.splitlines()[129]
without=without.replace(paramnew,paramold).replace('Project repository: \\url{https://github.com/Ring0-Network/lula}.\n\n','')
assert [x for x in without.splitlines() if x.strip()]==[x for x in a.splitlines() if x.strip()]
assert '64$ MiB minus 16 bytes' in newsection and '$8$ MiB' in newsection
assert 'unevaluated component calculation, not a full-security bound' in newsection
assert 'still materializes the temporary tree' in newsection
assert 'intermediate cache policies are not implemented or measured here' in newsection
assert 'omitting the retained top cache' in newsection
live='\n'.join((P/f).read_text(encoding='utf8') for f in ['LULA-I.tex','stability-results.tex','operating-model.tex','comparison-results.tex'])
assert not re.search(r'Intel|Core Ultra|255U|Windows 11|processor model|operating system',live,re.I)
assert '32 GiB of RAM' in sb and 'physical core was not isolated' in sb
script=P/'release/code/models/cache_memory_tradeoff.py'
run=subprocess.run([sys.executable,'-I','-B',str(script)],capture_output=True,text=True)
assert run.returncode==0,run.stderr
public=json.loads(run.stdout)
ind=json.loads((O/'HEIGHT-ILLUSTRATION.json').read_text())
assert public['status']=='ANALYTICAL_ILLUSTRATION_ONLY' and not public['new_measurements'] and not public['full_security_bound_established']
for pub,own in zip(public['rows'],ind['rows'][:2]):
    with mp.workdps(200):assert abs(mp.mpf(pub['FORS_per_candidate_exponent'])-mp.mpf(own['binomial']['negative_log2_p_raw']))<mp.mpf('1e-77')
    cnt=next(x for x in ind['counts'] if x['top_height']==pub['top_height'])
    assert pub['retained_cache_bytes']==cnt['cache_payload_bytes'] and pub['signature_bytes']==cnt['signature_bytes']
    assert pub['node_payload_bytes']==cnt['node_bytes'] and pub['counter_payload_bytes']==cnt['counter_bytes']
    assert str(pub['display'])==own['binomial']['display']
assert sha(P/'release/code/lula1/src/lib.rs')=='ac8e67f05af68dd8e1291c5909847f74103903fb7ffa2c70f500c6ec48f14210'
checks=dict(status='ACCEPT_SCOPED_POSTEDIT_MANUSCRIPT_AND_ANALYTICAL_SCRIPT',subject_pins={f:sha(P/f) for f in ['LULA-I.tex','stability-results.tex','operating-model.tex','comparison-results.tex','references.bib','release/code/models/cache_memory_tradeoff.py','release/code/lula1/src/lib.rs']},baseline_pins={f:sha(old/f) for f in ['LULA-I.tex','stability-results.tex']},unchanged=['abstract','all lemma/theorem/proof environments','all five algorithms','all six tables and measured numbers','operating model','comparison results','bibliography','final Note'],permitted_main_changes=['evaluated versus analytical parameter qualification','new sec:memorytradeoff','neutral repository line after conclusions'],stability_changes=['exact model and OS omitted; 32 GiB RAM/pinning/non-isolation retained; all other text unchanged'],public_script_command=dict(argv=[sys.executable,'-I','-B',str(script)],exit_code=run.returncode,result=public),independent_height_data_sha256=sha(O/'HEIGHT-ILLUSTRATION.json'),manual_diff_sha256=sha(O/'POSTEDIT-DIFF.txt'),new_measurements=False,signing_or_benchmark_runs=0,reviewer_root_file_edits=0,upload_scope_under_review='intent: updated PDF and editable source ZIP only; no raw-data reproducibility ZIP',remote_upload_performed_by_reviewer=False,full_signature_security_established=False,whole_goal_complete=False)
(O/'POSTEDIT-CHECKS.json').write_text(json.dumps(checks,indent=2)+'\n',encoding='utf8')
print(json.dumps(dict(status=checks['status'],postedit_checks_sha256=sha(O/'POSTEDIT-CHECKS.json'),public_script_sha256=sha(script),manual_diff_sha256=sha(O/'POSTEDIT-DIFF.txt')),indent=2))
