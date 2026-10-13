"""New source polynomial-private QROM candidate; old calculators immutable."""
from pathlib import Path
import hashlib,json,importlib.util
import mpmath as mp
E=Path(__file__).resolve().parent;X=E.parent
source=X.parents[1]/'numerics/bounds.py'
spec=importlib.util.spec_from_file_location('frozen_pf',source)
mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod)
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
rows=[]
with mp.workdps(230):
 N=mp.mpf(1<<128);M=N*N-N;cap=lambda x:min(mp.mpf(1),x)
 for logq in (24,30,38,40,41,44,50,64):
  q=1<<logq
  pf=mod.fors_moment(q,41,9,18,dps=230)
  positive=mod.fors_positive(q,41,9,18,dps=230)
  assert abs(-mp.log(pf,2)-positive['bits'])<mp.mpf('1e-10')
  for logQ in (32,64):
   Q=1<<logQ
   D=cap(q*(mp.sqrt(mp.mpf(Q+q+1)/M)+mp.mpf(Q+q+1)/(2*M)))
   A=cap(D+8*(Q+2)**2*(pf+1/N+mp.mpf(q)/(N*N)))
   c=cap((2*Q+mp.sqrt(q))**2/N+(2*(Q+2)/mp.sqrt(N)+mp.sqrt(A))**2)
   h=cap((2*Q+mp.sqrt(3017))**2/N)
   g=cap(8*(Q+3218)**2/N);d7=cap(8*(Q+6)**2/N)
   e=cap(c+h+g+d7)
   v=cap(mp.mpf(4*Q*Q)/(N-4*Q*Q)) if 4*Q*Q<N else mp.mpf(1)
   t=cap((2*Q+mp.sqrt(min(N,2*q+2)))**2/N)
   ap=cap(v+t)
   poly=cap(1/N+v+ap+e)
   oldprivate=cap(mp.mpf(2*Q)/mp.sqrt(N)+mp.mpf(2*q+2)/N)
   old=cap(1/N+oldprivate+c+h+g+d7)
   event=cap(1/N+(mp.mpf(2*Q)/mp.sqrt(N)+mp.sqrt(cap(mp.mpf(2*q+2)/N+e)))**2)
   terms={'pF':pf,'vK':v,'aliasP':t,'aP':ap,'c':c,'h':h,'g':g,'d7':d7,
          'ideal_union':e,'poly_total':poly,'old_conservative':old,'old_event':event,
          'best_total':min(poly,old,event)}
   rows.append({'log2_q':logq,'log2_Q':logQ,
    'probabilities':{n:mp.nstr(x,90) for n,x in terms.items()},
    'exponents':{n:float(-mp.log(x,2)) if x else None for n,x in terms.items()},
    'new_wins_minimum':poly<min(old,event),'category':'not established'})
pins={n:sha(X/n) for n in ('QUANTUM-POLYNOMIAL-PRIVATE-COMPOSITION.md',
 'SOURCE-PRIVATE-K-POLYNOMIAL-QROM.md','SOURCE-PRIVATE-P-POLYNOMIAL-QROM.md',
 'QUANTUM-RO-THEOREM.md','QUANTUM-EVENT-SPECIFIC-THEOREM.md')}
out={'status':'COMPUTED_FROM_MANUAL_SOURCE_SUCCESSOR_PENDING_INDEPENDENT_FULL_REVIEW',
 'script_sha256':sha(Path(__file__)),'frozen_pf_calculator_sha256':sha(source),
 'input_pins':pins,'mpmath':mp.__version__,'dps':230,'rows':rows,
 'old_source_calculators_changed':False,'whole_goal_complete':False}
(E/'RESULTS.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf8')
print(json.dumps({'rows':len(rows),'q40_Q32':next(r['exponents'] for r in rows if r['log2_q']==40 and r['log2_Q']==32),
 'new_stronger_rows':sum(r['new_wins_minimum'] for r in rows),'category':'not established'}))
