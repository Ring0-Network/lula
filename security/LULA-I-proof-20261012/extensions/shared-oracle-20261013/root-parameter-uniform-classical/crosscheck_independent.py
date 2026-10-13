"""Independent exact rational checks of the saved uniform numerical rows."""
from pathlib import Path
from fractions import Fraction as F
import hashlib,importlib.util,json
HERE=Path(__file__).resolve().parent;X=HERE.parent
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
spec=importlib.util.spec_from_file_location('root_uniform',HERE/'uniform_bounds.py')
m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
path=X/'pre-start-second/uniform-classical-numerics-20261014/OWN-UNIFORM-NUMERICS.json'
data=json.loads(path.read_text())
assert data['script_sha256']==sha(path.parent/'evaluate.py')
assert data['first_sha256']==sha(path.parent/'INDEPENDENT-FIRST.md')
assert data['source_sha256']==m.SOURCE_SHA
assert data['baseline_regression']['rows']==24
assert len(data['baseline_regression']['half_success_crossings'])==8
def dyadic(t):
 sign,man,exp,bits=t
 assert not sign and (not man or man.bit_length()==bits)
 return F(man<<exp) if exp>=0 else F(man,1<<-exp)
rows=0;pf_checks=0;N=1<<128
for rec in data['parameter_records']:
 p=rec['parameters'];layers=p['layers']
 params={'n_bytes':16,'a':p['a'],'r':p['k']-1,
  'heights':[l['h'] for l in layers],'ell':[l['ell'] for l in layers],'S':[l['S'] for l in layers]}
 m.guarded(params);g=rec['derived']
 for row in rec['rows']:
  q=1<<row['q_exponent'];Q=1<<row['Q_exponent']
  root=m.evaluate(params,q,Q)
  assert root['C']==g['C_p'] and root['H']==g['H_fin'] and root['G']==g['G_fin']
  assert root['signature_bytes']==g['signature_bytes']
  assert int(row['linear_numerator'])==3*Q+2*q+root['C']
  assert int(row['pair_numerator'])==q*Q+q*(q-1)//2+q
  lo,hi=map(dyadic,row['pF_interval_dyadic']);assert 0<lo<=hi<=F(1,1<<p['a'])
  # The moment enclosure need only intersect this mathematically proved upper.
  assert lo<=m.positive_upper(q,params);pf_checks+=1
  outlo,outhi=(F(int(a),int(b)) for a,b in row['capped_interval_rational'])
  assert 0<=outlo<=outhi<=1
  # Dropping exhaustion lower-bounds U; its proven dyadic upper upper-bounds U.
  certain=F(3*Q+2*q+root['C'],N)+F(q*Q+q*(q-1)//2+q,N*N)+(Q+1)*lo
  finite_upper=F(q,1<<min(2048,1<<(32-p['a'])))
  loose=F(3*Q+2*q+root['C'],N)+F(q*Q+q*(q-1)//2+q,N*N)+(Q+1)*hi+finite_upper
  assert outlo<=min(F(1),loose) and outhi>=min(F(1),certain)
  if row['Q_exponent']==128:assert outlo==outhi==1
  rows+=1
for fname in ('BASELINE-CERTIFICATES.json','HEIGHT63-CERTIFICATES.json'):
 r=json.loads((HERE/fname).read_text())
 assert r['script_sha256']==sha(HERE/'uniform_bounds.py') and r['theorem_sha256']==sha(m.THEOREM)
 for v in r['rows']:
  fresh=m.evaluate(r['parameters'],int(v['q']),int(v['Q']))
  assert all(v[k]==val for k,val in fresh.items())
 if fname.startswith('HEIGHT63'):
  assert all(v['sufficient_at_success_half'] for v in r['rows'] if v['log2_Q']==125)
  assert all(v['capped_upper']['numerator']==v['capped_upper']['denominator'] for v in r['rows'] if v['log2_Q']==128)
assert rows==144 and pf_checks==144
record={'status':'PASS144_INDEPENDENT_UNIFORM_ROWS_AND48_ROOT_POSITIVE_CERTIFICATES',
 'subject_sha256':sha(m.THEOREM),'independent_data_sha256':sha(path),
 'independent_script_sha256':sha(path.parent/'evaluate.py'),'root_script_sha256':sha(HERE/'uniform_bounds.py'),
 'check_script_sha256':sha(Path(__file__)),'independent_rows_checked':rows,'positive_moment_checks':pf_checks,
 'root_exact_certificate_rows_checked':48,'baseline_old_rows_preserved':24,'baseline_old_crossings_preserved':8,
 'new_source_or_manuscript_edits':0,'QROM_retuning_established':False,
 'original_128_category_minimal_repair':'not established','whole_goal_complete':False}
(HERE/'ROOT-CROSSCHECK.json').write_text(json.dumps(record,indent=2)+'\n',encoding='utf8')
print(json.dumps(record))
