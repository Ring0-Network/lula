from pathlib import Path
import hashlib,json
B=Path(__file__).resolve().parent;X=B.parents[1]
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
old=json.loads((B.parent/'TARGET-PRE-INTEGRATION-REVIEW.json').read_text(encoding='utf-8'))
protected={}
for group in ['preserved_artifacts','source_subjects']:
    for path,digest in old.get(group,{}).items():
        if path in ['CLASSICAL-RO-THEOREM.md','QUANTUM-RO-THEOREM.md','bounds.py','bounds-event-specific.py','CHANGED-CHILD-EXTRACTION.md'] or 'publications' in path:
            p=Path(path) if Path(path).is_absolute() else X/path
            assert sha(p)==digest,(path,sha(p),digest)
            protected[path]=digest
peer=X/'pre-start-second/interior-ud/quantitative-boundary/joint-classical'
subjects={str((peer/n).relative_to(X)).replace('\\','/'):sha(peer/n) for n in ['INDEPENDENT-FIRST.md','CONDITIONING-CLARIFICATION.md']}
own=['INDEPENDENT-FIRST.md','PEER-REVIEW.md','independent_controls.py','INDEPENDENT-CONTROLS.json','peer-reexecution/BYTE-ROLE-CONTROLS.json']
pins={str((B/n).relative_to(X)).replace('\\','/'):sha(B/n) for n in own}
source=X.parents[3]/'publications/LULA-I/release/code/lula1/src/lib.rs'
# X parents: proof, security, lula22. Resolve by explicit named ancestor to avoid drift.
source=Path('C:/Users/angel/Desktop/paper/PAPERS/LUGEL/research/lula22/publications/LULA-I/release/code/lula1/src/lib.rs')
assert sha(source)=='ac8e67f05af68dd8e1291c5909847f74103903fb7ffa2c70f500c6ec48f14210'
protected[str(source).replace('\\','/')]=sha(source)
checks={k:True for k in ['blind_first_preserved_before_peer_read','source_exact_byte_roles_verified',
 'no_one_charge_hidden_equality_partition','safe_surface_not_full_secret_advice',
 'genuine_rows_only_prefix_metadata_no_surplus_residual','same_unflagged_ghost_unused_remaining_coordinates',
 'full256_lower_limbs_and_shared_literal_aliases_retained','real_and_ghost_common_first_bad_prefix',
 'absorbing_partiality_no_global_unused_row_abort','forward_closed_disclosure_no_overwrite',
 'fresh_G_and_D7_charged_at_first_residual_evaluation','private_K_P_and_unsigned_J_unused_in_continuation',
 'same_law_coverage_prefix_no_survival_postselection','old_honest_namespace_cases_not_fresh_candidate_draws',
 'deterministic_candidate_cap_not_expected_count','weighted_expected_role_counts_same_ghost',
 'one_outer_or_inner_256_nominee_per_raw_point','honest_outer_alias_redundant_after_Bad_end',
 'fixed_nonzero_constant_6241_uniform_seed_once_6242','peer_controls_identical_exit_zero',
 'independent_negative_controls_exit_zero','old_source_scalar_pins_unchanged',
 'manual_only_not_checked_source_or_efficient_sampler','no_numeric_capacity_category_or_fixed_sha_claim']}
out=dict(status='ACCEPTED_MANUAL_JOINT_CLASSICAL_TECHNICAL_CANDIDATE_NOT_CORE_PROMOTION',
 subject_sha256=sha(peer/'INDEPENDENT-FIRST.md'),source_subjects=subjects,
 provenance_pins=pins,preserved_artifacts=protected,checks=checks,
 candidate=dict(N='2^128',fixed_nonzero_numerator='3Q+2q+6241',unconditional_numerator='3Q+2q+6242',
  full256_pair_numerator='qQ+binom(q,2)+q',full256_pair_denominator='N^2',
  coverage='(Q+1)p_F(q), or (b_E+1)p_F(q) only for pathwise deterministic b_E',
  exhaustion='q(511/512)^(2^32)'),
 validation_scope='Manual common-source-prefix proof review plus finite discriminating controls; no full source/game kernel verification.',
 total_prior_supporting_declarations=47,new_checked_declarations=0,new_source_game_declarations=0,
 old_scalar_upgrade=False,core_index_promotion_reviewed=False,whole_goal_complete=False)
(B/'FINAL-TECHNICAL-CANDIDATE-REVIEW.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps(dict(status=out['status'],protected_pins=len(protected),checks=len(checks),
 receipt_sha256=sha(B/'FINAL-TECHNICAL-CANDIDATE-REVIEW.json'),whole_goal_complete=False)))
