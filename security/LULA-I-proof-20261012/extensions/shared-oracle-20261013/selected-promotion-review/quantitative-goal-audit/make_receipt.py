import hashlib,json
from pathlib import Path
HERE=Path(__file__).resolve().parent
X=HERE.parents[1]
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
num=json.loads((HERE/'NUMERICS.json').read_text(encoding='utf-8'))
for n,h in num['current_pins'].items():assert sha(X/n)==h,n
assert sha(HERE/'INDEPENDENT-FIRST.md')=='b70fe2a09a802d4ee08c2111e7f8cfaf25865b5c04c6aadaa5274c416e062381'
assert len(num['verified_crossings'])==32
assert sha(X.parents[1]/'OBJECTIVE.txt')==num['original_objective_sha256']
release=X.parents[3]/'publications/LULA-I/release/code/lula1/src/lib.rs'
assert sha(release)=='ac8e67f05af68dd8e1291c5909847f74103903fb7ffa2c70f500c6ec48f14210'
out={
 'status':'SOURCE_FIRST_QUANTITATIVE_GOAL_ADEQUACY_AUDIT_COMPLETE_SCOPED',
 'own_pins':{n:sha(HERE/n) for n in ('INDEPENDENT-FIRST.md','LOSS-ADEQUACY-ADDENDUM.md',
      'RESOURCE-MODEL-OBLIGATION.md','audit_numeric.py','NUMERICS.json','NUMERICS.md',
      'resource_ratios.py','RESOURCE-RATIOS.json','nist-security-criteria.html','make_receipt.py')},
 'current_source_pins':num['current_pins'],
 'original_objective_path':str(X.parents[1]/'OBJECTIVE.txt'),
 'original_objective_sha256':num['original_objective_sha256'],
 'release_source_path':str(release),'release_source_sha256':sha(release),
 'primary':{'url':'https://csrc.nist.gov/Projects/Post-Quantum-Cryptography/Post-Quantum-Cryptography-Standardization/Evaluation-Criteria/Security-%28Evaluation-Criteria%29',
     'anchors':'4.A.4-5','access_date':'2026-10-13','page_updated':'2026-08-05','cached_html_sha256':sha(HERE/'nist-security-criteria.html')},
 'checks':{n:True for n in ('original_security_objective_read_not_publication_prompt_substituted',
     'sourcefirst_saved_before_new_targetonly_activation_peer_reads',
     'current_later_successors_resolve_old_legal_interface_OPEN_rows',
     'false_original_premises_classified_not_missing_lemmas',
     'literal_small_failure_gate_refuted_for_supplied_formula_not_security_impossibility',
     'independent_binomial_exp_log1p_arithmetic_q38_q40_q41',
     'all32_original_rational_pass_fail_certificates_checked',
     'all32_adjacent_crossings_independently_reevaluated_260digits',
     'exhaustion_enclosure_below_all_endpoint_margins',
     'dominant_terms_q_and_Q_budgets_separated',
     'fresh_official_NIST_category_and_signing_query_scope_read',
     'full_search_vs_half_success_reference_normalization_distinguished',
     'required_ratios_not_observed_gate_costs_or_arbitrary_attack_lower_bounds',
     'ordinary_ITSR_2pow544_and_hidden_254UD_residual_budgets_explicit',
     'concrete_quantitative_resource_interface_bridge_missing',
     'no_optional_filtered_attack_retried','no_source_manuscript_core_scalar_or_prior_receipt_edits')},
 'precision_decimal_digits':260,'verified_crossings':32,
 'next_scientific_obligation':'Lawful complete-resource quantitative primitive applicability and probability-budget feasibility, plus explicit query-to-AES gate/depth/success bridge; then assess analytic parameter repair',
 'actual_fixed_h_hardness':'NOT_ESTABLISHED','category_or_capacity_certificate':False,
 'new_source_game_checked_declarations':0,'whole_goal_complete':False,
}
p=HERE/'REVIEW-RECEIPT.json';p.write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8');print('PASS',sha(p))
