import hashlib,json
from pathlib import Path
import mpmath as mp
HERE=Path(__file__).resolve().parent
mp.mp.dps=120
p=json.loads((HERE/'NUMERICS.json').read_text(encoding='utf-8'))
rows=[]
for r in p['verified_crossings']:
    if r['log2_q'] not in (38,40,41) or r['model'] not in ('classical','quantum_best'):continue
    a=128 if r['model']=='classical' else 64
    Q=mp.mpf(r['Q_pass']);coef=mp.mpf(1)/2 if a==128 else mp.pi/8
    rows.append({'log2_q':r['log2_q'],'model':r['model'],'Q_pass':r['Q_pass'],
       'log2_Q_pass':float(mp.log(Q,2)),
       'benchmark_deficit_bits':float(a-mp.log(Q,2)),
       'required_hash_per_reference_unit_ratio_full_search':mp.nstr(mp.power(2,a)/Q,45),
       'ideal_success_half_reference_coefficient':mp.nstr(coef,45),
       'required_ratio_ideal_success_half':mp.nstr(coef*mp.power(2,a)/Q,45),
       'meaning':'Required assumed lower resource cost per hash relative to one reference-test unit, under a valid all-attacks black-box resource translation; not an observed cost or category result'})
out={'status':'COMPUTED_REQUIRED_RESOURCE_RATIOS_ONLY','success_ceiling':'1/2',
 'numeric_input_sha256':hashlib.sha256((HERE/'NUMERICS.json').read_bytes()).hexdigest(),
 'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'rows':rows,
 'quantum_half_reference':'Asymptotic ideal unique-target Grover count (pi/8)*sqrtN for success1/2, not an AES circuit estimate',
 'quantum_half_depth_or_parallelism_included':False,'actual_hash_cost_lower_bound_established':False,
 'category_certified':False,'whole_goal_complete':False}
(HERE/'RESOURCE-RATIOS.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
for r in rows:print(r['log2_q'],r['model'],r['benchmark_deficit_bits'],r['required_hash_per_reference_unit_ratio_full_search'],r['required_ratio_ideal_success_half'])
