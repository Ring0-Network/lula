from pathlib import Path
import hashlib,json
B=Path(__file__).resolve().parent;X=B.parents[1]
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
assert sha(B/'INDEPENDENT-FIRST.md')=='e330e30759eac52adca83384ce5b9c95cfa9a491230376518cfa19302dd3bd67'
peer=X/'root-parameter-uniform-classical/FIRST-DERIVATION.md'
assert sha(peer)=='833a46073c70f3e6f702a925360ed54279f438fa557cd0ef3e63473e58b571fe'
source=Path('C:/Users/angel/Desktop/paper/PAPERS/LUGEL/research/lula22/publications/LULA-I/release/code/lula1/src/lib.rs')
preserve={'CLASSICAL-RO-THEOREM.md':'3ff8d3c0457ce0525a5af416472f7188e75e20c52cc06d2220b4273a1db752fe',
 'CLASSICAL-JOINT-RO-THEOREM.md':'4fa7c3b63a268bd7535a753813d109a2f768f0089df44b54223a6e34cfaf35f0',
 'bounds.py':'2e0849d60bde394397ef917d667d8a547c910868b571157d6a26f8140eb338cd',
 'bounds-event-specific.py':'4f06f80befae967479a582fb644d4d24bcb40b9051324709f529abcf683a8a81'}
for n,h in preserve.items():assert sha(X/n)==h,n
assert sha(source)=='ac8e67f05af68dd8e1291c5909847f74103903fb7ffa2c70f500c6ec48f14210'
control=json.loads((B/'FINITE-CONTROLS.json').read_text(encoding='utf-8'))
assert control['exit_code']==0 and control['coverage_dimension_cases']==36
checks={k:True for k in ['own_source_first_before_peer_read','ex_ante_parameters_and_source_guards_agree',
 'strict_target_and_full128_omitted_zero_injectivity','acyclic_distinct_restrictions_one_genuine_child',
 'shared_full_raw_REAL_marginal_with_full_lower_limbs','same_safe_graph_rows_private_unflagged_continuation',
 'unused_hidden_and_unsigned_J_coins_atomic_partiality','knownpoint_install_firstbad_and_forward_exposure',
 'no_unexposed_canonical_row_or_success_normalization_assumption','uniform_complete_four_event_source_cover',
 'parameterized_terminal_H_G_d_counts_recomputed','same3Q_2q_and_full256_pair_law_derived',
 'uniform_finite_binomial_coverage_and_counter_exhaustion','deterministic_candidate_padding_same_world',
 'uniform_seedzero_paid_once','zero_height_B1_and_full256_edge_controls',
 'source_scalars_and_both_firsts_preserved','no_category_QROM_or_repair_inference']}
files=['INDEPENDENT-FIRST.md','PEER-REVIEW.md','finite_controls.py','FINITE-CONTROLS.json','finalize_peer_review.py']
out=dict(status='ACCEPTED_MANUAL_PARAMETER_UNIFORM_CLASSICAL_TECHNICAL_CANDIDATE',
 subject='root-parameter-uniform-classical/FIRST-DERIVATION.md',subject_sha256=sha(peer),checks=checks,
 source_subjects={str(peer.relative_to(X)).replace('\\','/'):sha(peer)},
 provenance_pins={str((B/n).relative_to(X)).replace('\\','/'):sha(B/n) for n in files},
 preserved_artifacts={**preserve,str(source).replace('\\','/'):sha(source)},
 acceptance_scope='Manual source-RO theorem under fixed n16/lw4/8 representation, strict-target and honest atomic-interface guards. Not merely numeric substitution.',
 new_checked_declarations=0,new_source_game_declarations=0,
 retuned_QROM_bound_established=False,parameter_repair_established=False,whole_goal_complete=False)
(B/'PEER-REVIEW.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps(dict(status=out['status'],receipt_sha256=sha(B/'PEER-REVIEW.json'),checks=len(checks))))
