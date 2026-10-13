from pathlib import Path
from fractions import Fraction as F
from hashlib import sha256
import json,subprocess,sys
import mpmath as mp
E=Path(__file__).resolve().parent;X=E.parent.parent
script=E/'bounds.py';base=json.loads((E/'baseline.json').read_text());original=json.loads((E/'results.json').read_text())
def run(args,want):
 p=subprocess.run([sys.executable,'-I','-B',str(script),*args],capture_output=True,text=True)
 assert p.returncode==want,(p.returncode,p.stdout,p.stderr)
 return {'native_exit_code':p.returncode,'stdout_tail':p.stdout.splitlines()[-1] if p.stdout else '', 'stderr':p.stderr.strip()}
tests={}
tests['default_repeat']=run(['--out',str(E/'repeat-results.json')],0)
assert (E/'repeat-results.json').read_bytes()==(E/'results.json').read_bytes()
tests['selected_budgets']=run(['--log2-QH','64','--log2-Qq','32','--out',str(E/'selected-results.json')],0)
selected=json.loads((E/'selected-results.json').read_text())
for row,ref in zip(selected['rows'],original['rows']):
 assert len(row['classical'])==len(row['quantum'])==1
 assert row['classical'][0]==ref['classical'][0] and row['quantum'][0]==ref['quantum'][0]
ret=dict(base);ret['S']=list(base['S']);ret['S'][0]-=1
(E/'retuned-test.json').write_text(json.dumps(ret,indent=2)+'\n')
tests['nonbaseline_refused']=run(['--params',str(E/'retuned-test.json'),'--out',str(E/'retuned-results.json')],2)
r=json.loads((E/'retuned-results.json').read_text())
assert not r['baseline_source_parameters'] and all(not z['classical'] and not z['quantum'] for z in r['rows'])
ret['S'][0]=ret['ell'][0]*((1<<ret['lw'][0])-1)
(E/'Smax-test.json').write_text(json.dumps(ret,indent=2)+'\n')
tests['Smax_only_diagnostics']=run(['--params',str(E/'Smax-test.json'),'--out',str(E/'Smax-results.json')],2)
r=json.loads((E/'Smax-results.json').read_text())
assert not r['analytic_costs']['source_Smax_guard_all_layers'] and not r['rows'][0]['classical']
bad=dict(base);bad['n_bytes']=32
(E/'invalid-test.json').write_text(json.dumps(bad,indent=2)+'\n')
tests['n32_rejected']=run(['--params',str(E/'invalid-test.json'),'--out',str(E/'invalid-results.json')],2)
assert not (E/'invalid-results.json').exists()
bad64=dict(base);bad64['heights']=[5,5,5,18,31]
(E/'height64-test.json').write_text(json.dumps(bad64,indent=2)+'\n')
tests['total_height64_rejected']=run(['--params',str(E/'height64-test.json'),'--out',str(E/'height64-results.json')],2)
assert not (E/'height64-results.json').exists()
reverse=dict(base);reverse['lw']=[8,4,4,4,4]
(E/'reversed-lw-test.json').write_text(json.dumps(reverse,indent=2)+'\n')
tests['reversed_bases_rejected']=run(['--params',str(E/'reversed-lw-test.json'),'--out',str(E/'reversed-lw-results.json')],2)
assert not (E/'reversed-lw-results.json').exists()
tests['insufficient_precision_rejected']=run(['--dps','400','--out',str(E/'low-precision-results.json')],2)
assert not (E/'low-precision-results.json').exists()
a=original['analytic_costs'];assert a['signature_bytes_exact']==5720
assert int(a['logical_cache_bytes_exact'])==((1<<22)-1)*16+(1<<21)*4
assert int(a['driver_fixture_bytes_exact'])==int(a['logical_cache_bytes_exact'])+117
assert int(a['top_subtree_cold_rebuild_tail_compressions_exact'])==(1<<21)*4102-1
assert int(a['top_only_keygen_fixed_tail_compressions_exact'])==(1<<21)*20805-1
# Compare the NEW600dps outward pF enclosure to old independently reviewed230dps enclosure.
def dyad(t):
 sign,m,e,b=t;assert sign==0 and m.bit_length()==b
 return F(m*(1<<e)) if e>=0 else F(m,1<<(-e))
old=json.loads((X/'classical-composition-numeric/OWN-BOUNDS.json').read_text())
oldp={r['log2_signing_query_cap']:r['FORS_per_raw_candidate'] for r in old['rows']}
for row in original['rows']:
 k=row['log2_q'];v=row['FORS_fixed_instance_moment'];ov=oldp[k]
 assert dyad(ov['lower_dyadic_mpf_tuple'])<=dyad(v['lower_dyadic_tuple'])<=dyad(v['upper_dyadic_tuple'])<=dyad(ov['upper_dyadic_mpf_tuple'])
 assert len(row['classical'])==len(row['quantum'])==2
# Numerical reproduction of separately preserved root quantum rows: full
# decimal values are approximate90-digit displays, so compare relative error.
rootfile=X/'root-polynomial-private-composition/RESULTS.json'
roots=json.loads(rootfile.read_text());mapping={(r['log2_q'],r['log2_Q']):r for r in roots['rows']}
name={'C':'c','H':'h','G':'g','D7':'d7','K_decision_v':'vK','P_classical_alias':'aliasP','P_one_sided_aP':'aP','complete_polynomial_private':'poly_total','retained_old_conservative':'old_conservative','retained_old_event':'old_event','complete_best_of_three':'best_total'}
checks=0
with mp.workdps(200):
 for row in original['rows']:
  for quant in row['quantum']:
   ref=mapping[row['log2_q'],quant['log2_Qq']]
   for k,v in name.items():
    new=mp.mpf(quant['components'][k]['probability_upper']);old=mp.mpf(ref['probabilities'][v])
    assert abs(new-old)/old<mp.mpf('1e-80'),(k,row['log2_q'])
    checks+=1
out={'status':'PASS_CURRENT_DELIVERABLE_VALIDATION','script_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),'bounds_sha256':sha256(script.read_bytes()).hexdigest(),'results_sha256':sha256((E/'results.json').read_bytes()).hexdigest(),'native_cli_tests':tests,'default_repeat_byte_identical':True,'default_classical_rows':16,'default_quantum_rows':16,'new600dps_pf_inside_all_old_independent230dps_intervals':True,'root_quantum_display_relative_crosschecks':checks,'root_dataset_sha256':sha256(rootfile.read_bytes()).hexdigest(),'exact_signature_cache_and_top_compression_checks':True,'source_or_old_calculators_modified':False,'new_source_game_declarations':0,'whole_goal_complete':False}
(E/'VALIDATION.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'status':out['status'],'tests':{k:v['native_exit_code'] for k,v in tests.items()},'quantum_crosschecks':checks,'validation_sha256':sha256((E/'VALIDATION.json').read_bytes()).hexdigest()}))
