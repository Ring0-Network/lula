"""Only arithmetic for stated conditional search/property models, not a security proof."""
import json, math, hashlib
from pathlib import Path
numeric_path=Path(__file__).resolve().parent.parent/'numerics'/'bounds.json'
numeric=json.loads(numeric_path.read_text(encoding='utf-8'))
rows=[]
for item in numeric['rows']:
    qs=item['log2_signatures']
    b=item['FORS_binomial_bits']
    for e in [32,40,60,64]:
        Q=2**e
        rows.append({'signing_exponent':qs,'input_fors_per_try_bits':b,
                     'quantum_queries_exponent':e,
                     'plain_grover_query_work_exponent':b/2,
                     'conditional_average_search_log2_upper':math.log2(8)+2*math.log2(Q+1)-b,
                     'conditional_average_search_clipped_log2_upper':min(0,math.log2(8)+2*math.log2(Q+1)-b),
                     'ideal_sm_tcr_log2_upper':math.log2(32*(Q+.5)**2+16*Q*Q)-128,
                     'status':'COMPUTED ARITHMETIC, ASSUMED MODEL, NOT LULA I BOUND'})
out={'numeric_input_sha256':hashlib.sha256(numeric_path.read_bytes()).hexdigest(),
     'numeric_input_scope':numeric['formula_scope'],
     'sm_tcr_coefficient_bits':math.log2(48),
     'sm_tcr_constant_success_query_exponent_loss':math.log2(48)/2,
     'single_ideal_tcr_Q_exponent_for_upper_2minus64':(128-64-math.log2(48))/2,
     'rows':rows,
     'no_certified_quantum_signing_limit':True}
Path(__file__).with_name('quantum-arithmetic.json').write_text(json.dumps(out,indent=2),encoding='utf-8')
print(json.dumps(out,indent=2))
