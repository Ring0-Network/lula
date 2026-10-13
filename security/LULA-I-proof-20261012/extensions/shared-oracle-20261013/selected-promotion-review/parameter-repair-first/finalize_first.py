from pathlib import Path
import hashlib,json
B=Path(__file__).resolve().parent;X=B.parents[1]
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
goals=[Path('C:/Users/angel/.codex/attachments/032bcc59-5956-41c6-88fb-1d3d3779005f/pasted-text-1.txt'),
       Path('C:/Users/angel/.codex/attachments/7ca7dd75-961c-425a-94a2-2bc006720d14/pasted-text-1.txt')]
assert sha(goals[0])=='655c5344c76c16d6e22d15ab169847385154a147dd28d0d31f1bbe86b465ee2f'
assert sha(goals[1])=='ccdcfbc8b10de3d10546573ea9d92c0f906b182dcb34ba2eb100225bb206a1e8'
assert goals[0].read_text(encoding='utf-8').strip().splitlines()==goals[1].read_text(encoding='utf-8').strip().splitlines()
assert sha(B/'INDEPENDENT-FIRST.md')=='869736c449aaff9ed24eb68e352fcff46bad784be4085b013c70c6db0ab7f842'
source=Path('C:/Users/angel/Desktop/paper/PAPERS/LUGEL/research/lula22/publications/LULA-I/release/code/lula1/src/lib.rs')
assert sha(source)=='ac8e67f05af68dd8e1291c5909847f74103903fb7ffa2c70f500c6ec48f14210'
preserve={'CLASSICAL-RO-THEOREM.md':'3ff8d3c0457ce0525a5af416472f7188e75e20c52cc06d2220b4273a1db752fe',
 'bounds.py':'2e0849d60bde394397ef917d667d8a547c910868b571157d6a26f8140eb338cd',
 'bounds-event-specific.py':'4f06f80befae967479a582fb644d4d24bcb40b9051324709f529abcf683a8a81'}
for n,h in preserve.items():assert sha(X/n)==h,n
data=json.loads((B/'ANALYTIC-CONTROLS.json').read_text(encoding='utf-8'))
assert data['exit_code']==0 and len(data['rows'])==7 and data['invalid_geometry_cases']==6
assert data['rows'][0]['top_row_failure_union_exact_power_two_upper_exponent']==-5741859
checks={k:True for k in ['both_full_original_goals_read','original_goal_n16_and_allowed_list_preserved',
 'blind_first_before_new_peer_or_root_repair_read','three_literal_query_resource_interpretations_distinguished',
 'no_parameter_invariant_bound_vacuity_to_impossibility_inference',
 'source_u64_and_u32_shift_address_digest_guards_checked','ell_z_lfull_and_forced_zero_injectivity_checked',
 'fixed_tail_buffer_guard_checked','new_H_G_and_joint_constant_computed_not_old_counts_reused',
 'serialized_bytes_cache_payload_and_compression_formulas_derived',
 'meaningful_completion_gate_not_aborting_game_vacuity','finite_counter_counts_not_actual_unconditional_runtime',
 'three_smallest_metrics_explicit','n_extension_named_separately_not_adopted','source_and_old_scalars_preserved']}
files=['INDEPENDENT-FIRST.md','COMPLETENESS-AND-COST-CLARIFICATION.md','analytic_controls.py','ANALYTIC-CONTROLS.json','ALTERNATIVES.md','finalize_first.py']
out=dict(status='SOURCE_FIRST_T3_ANALYTIC_FRONTIER_FULL_REPAIR_CERTIFICATE_OPEN',
 subject_sha256=sha(B/'INDEPENDENT-FIRST.md'),checks=checks,
 own_artifacts={str((B/n).relative_to(X)).replace('\\','/'):sha(B/n) for n in files},
 original_goal_pins={str(p).replace('\\','/'):sha(p) for p in goals},
 preserved_artifacts={**preserve,str(source).replace('\\','/'):sha(source)},
 finite_controls=dict(toy_coefficients_and_antichains=data['toy_coefficient_antichain_cases'],invalid_geometry_cases=6,
     analytic_alternatives=7,exit_code=0,source_or_signing_execution=False),
 smallest_open_obligation='Fix work/success/depth and meaningful completion criterion; then prove tighter parameter-uniform private/message/QROM composition or universal raw-to-AES attack-resource lower bridge before parameter optimization.',
 original_q40_conditional_use_target_preserved=True,fixed_n=16,
 full_repair_certified=False,actual_attack_or_design_impossibility_proved=False,
 new_parameter_set_adopted=False,new_source_game_declarations=0,whole_goal_complete=False)
(B/'FIRST-RECEIPT.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps(dict(status=out['status'],receipt_sha256=sha(B/'FIRST-RECEIPT.json'),controls=data['toy_coefficient_antichain_cases'],whole_goal_complete=False)))
