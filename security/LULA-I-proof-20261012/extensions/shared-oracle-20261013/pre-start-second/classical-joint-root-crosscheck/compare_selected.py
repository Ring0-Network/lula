"""Exact comparison to authorized selected input after own dataset save."""
from pathlib import Path
from fractions import Fraction as F
import hashlib,json
import mpmath as mp
E=Path(__file__).resolve().parent;X=E.parent.parent
read=lambda p:json.loads(p.read_text(encoding='utf-8'))
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
own=read(E/'OWN-JOINT-NUMERICS.json')
selected_path=X/'selected-promotion-review/joint-classical-review/JOINT-NUMERICS.json'
selected=read(selected_path)
pair=lambda p:F(*map(int,p))
exact_checks=0;display_checks=0
with mp.workdps(700):
 for r in selected['rows']:
  o=next(t for t in own['rows'] if (t['q_exponent'],t['QH_exponent'])==(r['log2_q'],r['log2_Q']))
  for key,oldkey in [('uncapped_lower','lower_rational'),('uncapped_upper','upper_rational'),('capped_lower','capped_lower_rational'),('capped_upper','capped_upper_rational'),('old_minus_new_uncapped_exact','old_minus_new_uncapped_linear')]:
   assert pair(o[key])==pair(r[oldkey]),(r['log2_q'],r['log2_Q'],key)
   exact_checks+=1
  a=mp.mpf(o['own_numeric_probability']);b=mp.mpf(r['joint_probability_display'])
  assert abs(a-b)/max(a,b)<mp.mpf('1e-57')
  display_checks+=1
 for r in selected['half_success_crossings']:
  o=next(t for t in own['half_success_crossings'] if t['q_exponent']==r['log2_q'])
  assert (o['Q_pass'],o['Q_fail'])==(r['Q_pass'],r['Q_fail'])
  exact_checks+=2
  for k,sourcekey in [('pass_interval','pass_interval'),('fail_interval','fail_interval')]:
   assert pair(o[k][0])==pair(r[sourcekey]['lower_rational'])
   assert pair(o[k][1])==pair(r[sourcekey]['upper_rational'])
   exact_checks+=2
  assert pair(o['pass_margin'])==pair(r['pass_margin_lower'])
  assert pair(o['fail_margin'])==pair(r['fail_margin_lower'])
  exact_checks+=2
review=read(X/'selected-promotion-review/joint-classical-review/FINAL-SUBJECT-REVIEW.json')
assert review['subject_sha256']==own['subject_sha256']==sha(X/'CLASSICAL-JOINT-RO-THEOREM.md')
assert all(review['checks'].values()) and not review['whole_goal_complete']
for group in ('preserved_artifacts','numerical_input_pins'):
 for name,h in review[group].items():
  path=Path(name) if Path(name).is_absolute() else X/name
  assert sha(path)==h,name
assert len(own['rows'])==24 and len(selected['rows'])==16
assert all(pair(r['capped_lower'])==pair(r['capped_upper'])==F(1) for r in own['rows'] if r['QH_exponent']==128)
out={'status':'PASS_SELECTED16_EXACT_SCALAR_ROWS_8CROSSINGS_PLUS_OWN_REQUIRED_QH128_ROWS',
 'own_first_sha256':sha(E/'INDEPENDENT-FIRST.md'),'own_calculator_sha256':sha(E/'independent_joint_bounds.py'),
 'own_data_sha256':sha(E/'OWN-JOINT-NUMERICS.json'),'selected_data_sha256':sha(selected_path),
 'selected_final_review_sha256':sha(X/'selected-promotion-review/joint-classical-review/FINAL-SUBJECT-REVIEW.json'),
 'subject_sha256':sha(X/'CLASSICAL-JOINT-RO-THEOREM.md'),'script_sha256':sha(Path(__file__)),
 'exact_Fraction_equalities':exact_checks,'display_probability_checks':display_checks,
 'display_relative_tolerance':'1e-57','own_moment_precision':620,'own_stability_precision':760,
 'own_rows':24,'selected_rows':16,'required_QH128_rows':8,'QH128_all_exact_cap1':True,
 'half_success_crossings':8,'new_root_joint_calculator_read':False,
 'inherited_pF_interval_premise_explicit':True,'own_affine_and_exhaustion_derivation':True,
 'new_source_game_declarations':0,'whole_goal_complete':False,'category':'not established'}
(E/'SELECTED-COMPARISON.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps(out))
