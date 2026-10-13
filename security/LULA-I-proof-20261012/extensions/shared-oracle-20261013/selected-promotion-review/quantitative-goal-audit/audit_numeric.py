import hashlib
import json
from math import comb
from pathlib import Path
import mpmath as mp
HERE=Path(__file__).resolve().parent
X=HERE.parents[1]
mp.mp.dps=260
N=mp.mpf(2)**128
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def bits(v):return float(-mp.log(v,2))
def raw(v):return mp.nstr(v,65)
def pf(q):
    B=mp.mpf(2)**41;t=mp.mpf(512)
    return mp.fsum([(-1)**j*comb(17,j)*mp.exp(q*mp.log1p(-(1-(1-1/t)**j)/B)) for j in range(18)])/t
def evaluate(q,Q,p):
    Q=mp.mpf(Q);q=mp.mpf(q)
    classical={
        'private_and_source_linear':(6*Q+3*q+6243)/N,
        'pair_collision':(q*Q+q*(q-1)/2+q)/(N*N),
        'coverage_search':(Q+1)*p,
    }
    M=N*N-N
    D=min(1,q*(mp.sqrt((Q+q+1)/M)+(Q+q+1)/(2*M)))
    A=min(1,D+8*(Q+2)**2*(p+1/N+q/(N*N)))
    c=min(1,(2*Q+mp.sqrt(q))**2/N+(2*(Q+2)/mp.sqrt(N)+mp.sqrt(A))**2)
    h=min(1,(2*Q+mp.sqrt(3017))**2/N)
    g=min(1,8*(Q+3218)**2/N)
    d7=min(1,8*(Q+6)**2/N)
    delta=min(1,2*Q/mp.sqrt(N)+(2*q+2)/N)
    b=min(1,(2*q+2)/N);e=min(1,c+h+g+d7)
    cons=min(1,1/N+delta+c+h+g+d7)
    event=min(1,1/N+(2*Q/mp.sqrt(N)+mp.sqrt(min(1,b+e)))**2)
    return {'classical':min(1,mp.fsum(classical.values())),
        'classical_components':classical,'quantum_D':D,'quantum_A':A,
        'quantum_C':c,'quantum_H':h,'quantum_G':g,'quantum_D7':d7,
        'quantum_private_distance':delta,'quantum_ideal_union':e,
        'quantum_conservative':cons,'quantum_event':event,'quantum_best':min(cons,event)}
data=[]
P={k:pf(1<<k) for k in (24,30,38,40,41,44,50,64)}
for k in (38,40,41):
    for a in (32,64):
        values=evaluate(1<<k,1<<a,P[k])
        flat={}
        for n,v in values.items():
            if isinstance(v,dict):
                flat[n]={j:{'probability':raw(w),'probability_exponent':bits(w)} for j,w in v.items()}
            else:flat[n]={'probability':raw(v),'probability_exponent':bits(v)}
        data.append({'log2_q':k,'log2_Q':a,'pF_exponent':bits(P[k]),**flat})
thresholds=json.loads((X/'query-resource-independent/THRESHOLDS.json').read_text(encoding='utf-8'))
assert len(thresholds['rows'])==32
cross=[]
for r in thresholds['rows']:
    k=r['log2_q'];model=r['model'];lo=int(r['Q_pass']);hi=int(r['Q_fail'])
    assert hi==lo+1
    lv=evaluate(1<<k,lo,P[k])[model];hv=evaluate(1<<k,hi,P[k])[model]
    assert lv<=mp.mpf(1)/2<hv,(k,model,raw(lv),raw(hv))
    assert min(mp.mpf(1)/2-lv,hv-mp.mpf(1)/2)>mp.power(2,k-4096)
    for bound,expected in ((r['pass_bound'],'PASS'),(r['fail_bound'],'FAIL')):
        l,u=bound['lower_rational'],bound['upper_rational']
        assert int(l[0])*int(u[1])<=int(u[0])*int(l[1])
        if expected=='PASS':assert 2*int(u[0])<=int(u[1])
        else:assert 2*int(l[0])>int(l[1])
    cross.append({'log2_q':k,'model':model,'Q_pass':str(lo),'Q_fail':str(hi),
                  'log2_Q_pass':float(mp.log(lo,2)),'pass_margin':raw(mp.mpf(1)/2-lv),'fail_margin':raw(hv-mp.mpf(1)/2)})
pins={n:sha(X/n) for n in ('PROOF.md','OPEN.md','TERM-TABLE.md','REQUIREMENT-MAP.md','SECURITY-CRITERION.md',
    'CLASSICAL-RO-THEOREM.md','QUANTUM-RO-THEOREM.md','QUANTUM-EVENT-SPECIFIC-THEOREM.md',
    'FIXED-H-COMPOSITION-WITH-UD-PRE.md','query-resource-independent/THRESHOLDS.json',
    'query-resource-independent/CROSSCHECK.json','bounds.py','bounds-event-specific.py')}
out={'status':'COMPUTED_SOURCE_FIRST_ADEQUACY_AUDIT','precision_decimal_digits':260,
     'pF_method':'Independent finite alternating binomial expectation, exp/log1p,17 real leaves plus zero filter',
     'exhaustion':'Only omitted from display approximation; certified 0<=q*(511/512)^(2^32)<=q*2^-4096, below all endpoint margins; original rational crossings retain it.',
     'current_pins':pins,'original_objective_sha256':sha(X.parents[1]/'OBJECTIVE.txt'),
     'script_sha256':sha(Path(__file__)),'rows':data,'verified_crossings':cross,
     'security_level_category':'NOT_ESTABLISHED','new_source_game_checked_declarations':0,'whole_goal_complete':False}
(HERE/'NUMERICS.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
lines=['# Independent source-model adequacy arithmetic','',
 '| log2 q | log2 Q | pF exponent | classical total exponent | QROM conservative exponent | QROM refined exponent | best exponent |',
 '|---:|---:|---:|---:|---:|---:|---:|']
for r in data:
    lines.append('| '+ ' | '.join(str(v) for v in (r['log2_q'],r['log2_Q'],round(r['pF_exponent'],9),*[round(r[n]['probability_exponent'],9) for n in ('classical','quantum_conservative','quantum_event','quantum_best')]))+' |')
lines.extend(['','32 original rational adjacent crossings passed exact endpoint certificate checks and an independent260-digit formula reevaluation. Probability exponents are not security bits.'])
(HERE/'NUMERICS.md').write_text('\n'.join(lines)+'\n',encoding='utf-8')
print('PASS',len(cross),'crossings',sha(HERE/'NUMERICS.json'))
print('\n'.join(lines))
