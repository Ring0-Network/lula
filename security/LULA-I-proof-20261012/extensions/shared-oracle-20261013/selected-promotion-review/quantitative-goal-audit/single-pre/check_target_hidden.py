from pathlib import Path
from fractions import Fraction as F
import hashlib,json
HERE=Path(__file__).resolve().parent
X=HERE.parents[2]
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
assert (HERE/'root_quantitative.py').read_bytes()==(X/'root-target-only-ud/quantitative.py').read_bytes()
assert (HERE/'QUANTITATIVE-RESULTS.json').read_bytes()==(X/'root-target-only-ud/QUANTITATIVE-RESULTS.json').read_bytes()
data=json.loads((HERE/'QUANTITATIVE-RESULTS.json').read_text(encoding='utf-8'))
N=1<<128;K=sum(1<<h for h in (41,36,31,26))
AH=32*K*105+16*(1<<21)*(254*255//2)
DH=480*K+4080*(1<<21)+(1<<41)*17*512
assert (AH,DH)==(7628143271608320,20229886488608768)
mu=F(2*N-1,N*N);slope=F(12*AH,1<<64)
def values(qa):
 r=qa+1;pre=min(F(1),(2*r+1)**2*mu)
 return pre,DH*pre,slope*r
assert len(data['rows'])==32
observed=set()
for row in data['rows']:
 qa=int(row['QA']);q=1<<row['log2_q'];pre,ps,us=values(qa)
 assert qa==1<<row['log2_QA']
 assert int(row['effective_Q'])==qa+1
 for name,value in (('PRE',pre),('PRE_source',ps),('UD_source',us)):
  assert F(int(row[name+'_numerator']),int(row[name+'_denominator']))==value
 assert F(row['hidden_component_cap'])==min(F(1),ps+us)==1
 hm=82090+5*(1<<32) if row['mode']=='prepared' else 8560574463+82090+6*(1<<32)
 assert int(row['outside_query_cap'])==qa+(1<<21)*(19505+(1<<32))-1+q*hm+3224+254
 observed.add((row['log2_q'],row['mode'],row['log2_QA']))
assert len(observed)==32
for t in data['constant_probability_crossings']:
 a,b=t['QA_pass'],t['QA_fail'];assert b==a+1
 av=sum(values(a)[1:]);bv=sum(values(b)[1:]);target=F(t['target'])
 assert av==F(t['pass_value']) and bv==F(t['fail_value'])
 assert av<=target<bv
assert [(r['QA_pass'],r['QA_fail']) for r in data['constant_probability_crossings']]==[(99,100),(200,201)]
out={'status':'PASS_INDEPENDENT_EXACT32_COMPONENT_ROWS_AND_ADJACENT_GATES',
 'root_copy_result_identical':True,'rows':32,'D_H':DH,'sum_A_r':AH,
 'half_success_QA_crossing':[99,100],'uncapped_sum_one_crossing':[200,201],
 'root_script_sha256':sha(HERE/'root_quantitative.py'),'result_sha256':sha(HERE/'QUANTITATIVE-RESULTS.json'),
 'checker_sha256':sha(Path(__file__)),'whole_goal_complete':False}
p=HERE/'TARGET-HIDDEN-NUMERIC-CHECK.json';p.write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8');print('PASS',sha(p))
