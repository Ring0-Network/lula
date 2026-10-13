from pathlib import Path
from fractions import Fraction as F
from math import isqrt
from hashlib import sha256
import json
E=Path(__file__).resolve().parent;X=E.parent.parent
new=json.loads((E/'NEW-CERTIFICATES.json').read_text())
old_path=X/'query-resource-independent'/'THRESHOLDS.json'
old=json.loads(old_path.read_text());manifest=json.loads((X/'query-resource-independent'/'SHA256SUMS.json').read_text())
assert sha256(old_path.read_bytes()).hexdigest()==next(r['sha256'] for r in manifest if r['name']=='THRESHOLDS.json')
oldmap={(r['log2_q'],r['model']):int(r['Q_pass']) for r in old['rows']}
newmap={(r['log2_q'],r['model']):int(r['Q_pass']) for r in new['rows']}
mapname={'conservative':'quantum_conservative','event':'quantum_event'}
for (k,model),a in newmap.items():
 if model in mapname:assert a==oldmap[k,mapname[model]]
N=1<<128;precision=384;den=1<<precision
# Independent expanded-form endpoint evaluator. Single scalar endpoint chooses
# all low or all high values; every quantity is positive/isotone.
def sqrt_round(x,upper):
 t=isqrt((x.numerator<<(2*precision))//x.denominator);a=F(t,den)
 assert a*a<=x<F((t+1)*(t+1),den*den)
 return F(t+1,den) if upper and a*a!=x else a
def evaluation(k,Q,pf,upper):
 q=1<<k
 D=min(F(1),q*(sqrt_round(F(Q+q+1,N*N-N),upper)+F(Q+q+1,2*(N*N-N))))
 A=min(F(1),D+8*(Q+2)**2*(pf+F(1,N)+F(q,N*N)))
 sq=sqrt_round(F(q),upper);sa=sqrt_round(A,upper);sh=sqrt_round(F(3017),upper)
 c=min(F(1),F(4*Q*Q+q,N)+F(4*Q,N)*sq+F(4*(Q+2)**2,N)+F(4*(Q+2),1<<64)*sa+A)
 h=min(F(1),F(4*Q*Q+3017,N)+F(4*Q,N)*sh)
 g=min(F(1),F(8*(Q+3218)**2,N));d=min(F(1),F(8*(Q+6)**2,N))
 pub=c+h+g+d;e=min(F(1),pub)
 con=min(F(1),F(1,N)+min(F(1),F(2*Q,1<<64)+F(2*q+2,N))+pub)
 a=F(2*Q,1<<64);be=min(F(1),min(F(1),F(2*q+2,N))+e)
 event=min(F(1),F(1,N)+a*a+2*a*sqrt_round(be,upper)+be)
 v=min(F(1),F(4*Q*Q,N-4*Q*Q)) if 4*Q*Q<N else F(1)
 C=min(N,2*q+2)
 t=min(F(1),F(4*Q*Q+C,N)+F(4*Q,N)*sqrt_round(F(C),upper))
 poly=min(F(1),F(1,N)+v+min(F(1),v+t)+e)
 return {'conservative':con,'event':event,'polynomial':poly,'best':min(con,event,poly)}
comparisons=[];certs=0;max_ratio=F(0)
for row in new['rows']:
 k=row['log2_q'];m=row['model']
 pf=new['FORS_enclosures'][str(k)]['enclosure']
 lo,hi=(F(int(z[0]),int(z[1])) for z in pf)
 for which in ('pass','fail'):
  Q=int(row['Q_'+which]);l=evaluation(k,Q,lo,False)[m];u=evaluation(k,Q,hi,True)[m]
  assert l<=u
  if which=='pass':assert u<=F(1,2)
  else:assert l>F(1,2)
  certs+=1
  margin=F(1,2)-u if which=='pass' else l-F(1,2)
  assert margin>0
  max_ratio=max(max_ratio,(u-l)/margin)
for k in (24,30,38,40,41,44,50,64):
 o=oldmap[k,'quantum_best'];p=newmap[k,'best']
 assert p>=o
 comparisons.append({'log2_q':k,'old_best_Q_pass':str(o),'new_best_Q_pass':str(p),'additional_sufficient_raw_queries':str(p-o),'winning_new_component':[m for m in ('conservative','event','polynomial') if newmap[k,m]==p]})
assert max_ratio<F(1,1<<200)
r={'status':'PASS_INDEPENDENT_EXPANDED_FORM_AND_OLD_COMPARISON','script_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),'new_certificate_sha256':sha256((E/'NEW-CERTIFICATES.json').read_bytes()).hexdigest(),'old_threshold_sha256':sha256(old_path.read_bytes()).hexdigest(),'old_threshold_read_after_new_certificate_saved':True,'root_new_results_read':False,'expanded_formula_precision_bits':precision,'endpoint_checks':certs,'old_individual_conservative_event_thresholds_all_match':True,'max_interval_width_over_endpoint_margin':str(max_ratio),'max_ratio_less_than_2_to_minus_200':True,'comparisons':comparisons,'new_source_game_declarations':0,'whole_goal_complete':False}
(E/'INDEPENDENT-CROSSCHECK.json').write_text(json.dumps(r,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'checks':certs,'comparisons':comparisons,'crosscheck_sha256':sha256((E/'INDEPENDENT-CROSSCHECK.json').read_bytes()).hexdigest()}))
