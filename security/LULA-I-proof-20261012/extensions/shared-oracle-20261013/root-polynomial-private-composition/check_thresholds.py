from pathlib import Path
from fractions import Fraction as F
import importlib.util,hashlib,json
import mpmath as mp
E=Path(__file__).resolve().parent;X=E.parent
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
certpath=X/'outside-field-check/polynomial-query-thresholds/NEW-CERTIFICATES.json'
cert=json.loads(certpath.read_text(encoding='utf8'))
for name,digest in cert['pins'].items():assert sha(X/name)==digest,name
source=X.parents[1]/'numerics/bounds.py'
spec=importlib.util.spec_from_file_location('frozen_pf',source)
mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod)
f=lambda pair:F(*map(int,pair))
checks=[]
with mp.workdps(260):
 N=mp.mpf(1<<128);M=N*N-N;cap=lambda x:min(mp.mpf(1),x)
 for logq in (24,30,38,40,41,44,50,64):
  q=1<<logq;pf=mod.fors_moment(q,41,9,18,dps=260)
  def values(Q):
   D=cap(q*(mp.sqrt(mp.mpf(Q+q+1)/M)+mp.mpf(Q+q+1)/(2*M)))
   A=cap(D+8*(Q+2)**2*(pf+1/N+mp.mpf(q)/(N*N)))
   c=cap((2*Q+mp.sqrt(q))**2/N+(2*(Q+2)/mp.sqrt(N)+mp.sqrt(A))**2)
   h=cap((2*Q+mp.sqrt(3017))**2/N)
   g=cap(8*(Q+3218)**2/N);d=cap(8*(Q+6)**2/N)
   union=cap(c+h+g+d)
   v=cap(mp.mpf(4*Q*Q)/(N-4*Q*Q)) if 4*Q*Q<N else mp.mpf(1)
   alias=cap((2*Q+mp.sqrt(min(N,2*q+2)))**2/N)
   poly=cap(1/N+v+cap(v+alias)+union)
   conservative=cap(1/N+cap(2*mp.mpf(Q)/mp.sqrt(N)+mp.mpf(2*q+2)/N)+c+h+g+d)
   event=cap(1/N+(2*mp.mpf(Q)/mp.sqrt(N)+mp.sqrt(cap(mp.mpf(2*q+2)/N+union)))**2)
   return {'conservative':conservative,'event':event,'polynomial':poly,'best':min(poly,conservative,event)}
  for row in [r for r in cert['rows'] if r['log2_q']==logq]:
   lo,hi=int(row['Q_pass']),int(row['Q_fail']);model=row['model']
   assert hi==lo+1
   assert f(row['pass_interval']['upper'])<=F(1,2)<f(row['fail_interval']['lower'])
   # Primary certificate intervals have exact Fraction endpoints; independent
   # floating evaluation must land inside them with a generous 1e-220 tolerance.
   for Q,key in ((lo,'pass_interval'),(hi,'fail_interval')):
    value=values(Q)[model]
    interval=row[key]
    lower=f(interval['lower']);upper=f(interval['upper'])
    lm=mp.mpf(lower.numerator)/lower.denominator;um=mp.mpf(upper.numerator)/upper.denominator
    assert lm-mp.mpf('1e-220')<=value<=um+mp.mpf('1e-220')
    assert (value<=mp.mpf('0.5'))==(key=='pass_interval')
   checks.append({'log2_q':logq,'model':model,'Q_pass':str(lo),'Q_fail':str(hi)})
assert len(checks)==32
out={'status':'PASS_32_NEW_COMPLETE_ENVELOPE_ADJACENT_PAIRS_64_ENDPOINTS',
 'script_sha256':sha(Path(__file__)),'certificate_sha256':sha(certpath),
 'subject_sha256':sha(X/'QUANTUM-POLYNOMIAL-PRIVATE-COMPOSITION.md'),
 'frozen_pf_calculator_sha256':sha(source),'dps':260,'rows':checks,
 'exact_rational_gate_checks':64,'independent_high_precision_evaluations':64,
 'scope':'Root numeric confirmation of independent outward certificates; not a new kernel proof or category claim'}
(E/'THRESHOLD-CROSSCHECK.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf8')
print(json.dumps({'pairs':32,'endpoints':64,'status':out['status']}))
