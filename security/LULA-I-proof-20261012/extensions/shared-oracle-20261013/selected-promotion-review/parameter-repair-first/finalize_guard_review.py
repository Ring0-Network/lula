from pathlib import Path
import hashlib,json
B=Path(__file__).resolve().parent;X=B.parents[1]
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
receipt=B/'FIRST-RECEIPT.json'
assert sha(receipt)=='008e75bbbf04d18bcd7e680d82c92ec1aca3f92fbcaf83b3e6915545f9ed79b7'
prior=json.loads(receipt.read_text(encoding='utf-8'))
for n,h in prior['own_artifacts'].items():assert sha(X/n)==h,n
for n,h in prior['preserved_artifacts'].items():
    p=Path(n) if Path(n).is_absolute() else X/n
    assert sha(p)==h,n
controls=json.loads((B/'PROOF-GUARD-CONTROLS.json').read_text(encoding='utf-8'))
assert controls['exit_code']==0 and controls['strict_target_digit_cases']==682
checks={k:True for k in ['root_note_reinspected_against_exact_source_and_old_exhaustive_lemma',
    'source_geometry_not_old_template_eligibility','strict_S_less_than_ell_w_minus_1_required_for_unexposed_H_step',
    'Smax_endpoint_negative_is_not_forgery_or_design_attack','exposed_D7_not_silently_extended_to_unexposed_rows',
    'fixed_lw4_8_only_ell_to_z_and_all_omitted_zero_injectivity',
    'tail_compressions_distinct_from_full_raw_queries','Ctx_prefix_direct_uninstrumented_cost_separate',
    'original_prepared_cache_top_only_four_lower_trees_recomputed','all_cached_hypothesis_not_original_hot_measurement',
    'first_package_preserved_exact','source_root_scalar_untouched','no_retuned_complete_bound_or_level_claim']}
newfiles=['PROOF-GUARD-CLARIFICATION.md','proof_guard_controls.py','PROOF-GUARD-CONTROLS.json','finalize_guard_review.py']
out=dict(status='ACCEPTED_SCOPED_PARAMETER_PROOF_GUARD_REVIEW_FULL_RETUNED_BOUND_OPEN',
    subject_sha256=sha(B/'PROOF-GUARD-CLARIFICATION.md'),checks=checks,
    source_subjects=controls['source_pins'],prior_review_receipts={str(receipt.relative_to(X)).replace('\\','/'):sha(receipt)},
    preserved_first_package_pins=prior['own_artifacts'],preserved_artifacts=prior['preserved_artifacts'],
    provenance_pins={str((B/n).relative_to(X)).replace('\\','/'):sha(B/n) for n in newfiles},
    source_geometry_domain='All first-package encodings and acceptance guards including non-strict0<=S<=ell(w−1).',
    old_proof_template_guard='All geometry guards plusell>=1 and0<=S<ell(w−1) at every layer;fixedlw4/8 with all omitteddigits0.',
    finite_controls=dict(digit_cases=682,local_endpoint_inference_negatives=9,geometry_rows=7,exit_code=0),
    new_checked_declarations=0,new_source_game_declarations=0,retuned_complete_bound_established=False,
    actual_forgery_or_design_impossibility_proved=False,whole_goal_complete=False)
(B/'PROOF-GUARD-RECEIPT.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps(dict(status=out['status'],receipt_sha256=sha(B/'PROOF-GUARD-RECEIPT.json'),checks=len(checks),whole_goal_complete=False)))
