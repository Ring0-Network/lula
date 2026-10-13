"""Exact selector-factor counterexample and source coordinate/resource ledger."""
from fractions import Fraction as F
from pathlib import Path
import hashlib,json
OUT=Path(__file__).resolve().parent
# One active cut, four padded ranks; square-root success and error both1/4.
L=4
bbar=F(1,64)
delta=F(1,4)
source_success=F(1,4)
correct=L*bbar+2*delta*F(1,4)+delta**2
wrong=L*bbar+2*delta*F(1,8)+delta**2
assert correct==source_success and wrong==F(3,16)<source_success
A=2**41+2**36+2**31+2**26
w=480*A+4080*2**21
u=32*A+16*2**21
k=448*A+4064*2**21
f=2**41*17*512
assert k==w-u==1016949404336128
assert u+f==19212937084272640
assert w+f==20229886488608768
assert 2**54<w+f<2**55
rows=[]
for qexp in [24,30,38,40,41,44,50,64]:
    q=2**qexp
    rows.append({'q_exp':qexp,
                 'hot_private_distinct_cap':min(u+f,1+2181038080+q*12816),
                 'cold_private_distinct_cap':min(u+f,1+2181038080+q*33567232),
                 'honest_hot_public_plus254':2**21*(19505+2**32)-1+q*(82090+5*2**32)+3224+254,
                 'honest_cold_public_plus254':2**21*(19505+2**32)-1+q*(8560574463+82090+6*2**32)+3224+254})
out={'status':'PASS_EXACT_SELECTOR_CROSS_TERM_COUNTEREXAMPLE_AND_SOURCE_RESOURCE_LEDGER',
     'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
     'D_W':w,'D_W_position_zero':u,'D_cut':k,'D_F':f,'D_H':w+f,'pad':2**55,
     'missing_sqrt_L_counterexample':{'L':L,'D_cut':1,'bbar':str(bbar),'delta':str(delta),
             'actual_source_success':str(source_success),'correct_envelope':str(correct),
             'incorrect_cross_term_envelope':str(wrong)},
     'q_source_resource_rows':rows,
     'coherent_handle_calls':'Q selected plus Q outside =2Q total',
     'selected_classical_final_calls_max':1,
     'finite_outside_table':'V_b=sum_{ell=0}^b256^ell;32V_b data bytes;O(V_b*(b+32)) lookup gates per coherent outside call',
     'not_checked':'Quantum source-prefix/vector/simulator theorem and conventional challenge equivalence.'}
(OUT/'QPRE-Algebra-Control.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf8')
print(json.dumps({'status':out['status'],'D_cut':k,'source_q_rows':len(rows),'wrong_bound':str(wrong),'correct_bound':str(correct)}))
