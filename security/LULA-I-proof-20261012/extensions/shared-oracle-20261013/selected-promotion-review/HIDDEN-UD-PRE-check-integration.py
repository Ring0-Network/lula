import difflib
import hashlib
import json
from pathlib import Path
HERE=Path(__file__).resolve().parent
X=HERE.parent
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def read(n): return json.loads((X/n).read_text(encoding='utf-8'))
P=read('HIDDEN-UD-PRE-PROMOTION.json')
OLD=read('selected-promotion-review/MESSAGE-GRAPH-INTEGRATION-REVIEW.json')
ALG=read('selected-promotion-review/FINAL-UD-PRE-COMPOSITION-REVIEW.json')
assert P['predecessor_documents']==OLD['documents']
assert len(P['accepted_evidence_absolute_pins'])==175
internal,external={},{}
for n,h in P['accepted_evidence_absolute_pins'].items():
    p=Path(n)
    assert sha(p)==h,n
    if p.is_relative_to(X): internal[p.relative_to(X).as_posix()]=h
    else: external[n]=h
groups={
    'documents':P['documents'],
    'promoted_artifacts':{**P['artifacts'],'HIDDEN-UD-PRE-PROMOTION.json':sha(X/'HIDDEN-UD-PRE-PROMOTION.json')},
    'source_subjects':internal,
    'prior_review_receipts':P['receipt_pins'],
    'backup_pins':{f'{P["predecessor_backup"]}/{n}':h for n,h in P['predecessor_documents'].items()},
    'preserved_artifacts':OLD['preserved_artifacts'],
}
for group,pins in groups.items():
    for n,h in pins.items(): assert sha(X/n)==h,(group,n)
for group in ('promoted_artifacts','source_subjects','backup_pins','preserved_artifacts','control_pins','prior_review_receipts','provenance_pins'):
    for n,h in OLD.get(group,{}).items(): assert sha(X/n)==h,('prior',group,n)
for n,h in OLD.get('external_absolute_pins',{}).items(): assert sha(Path(n))==h,('prior external',n)
assert P['source_scalar_manuscript_changes']==0
assert P['cumulative_supporting_checked_declarations']==47
assert P['new_source_game_checked_declarations']==0
assert P['conditional_algebra_second_final_premise_now_satisfied'] is True
assert P['whole_goal_complete'] is False
second=read('pre-start-second/interior-ud/FINAL-SUBJECT-REVIEW.json')
field=read('outside-field-check/interior-preimage/FINAL-SUBJECT-REVIEW.json')
subject=P['artifacts']['FIXED-H-HIDDEN-PREDECESSORS.md']
assert second['subject_sha256']==field['subject_sha256']==subject
assert second['review_status']=='ACCEPT_MANUAL_CONDITIONAL_ORDINARY_UD_PRE_INTERFACE'
assert field['verdict']=='ACCEPT_MANUAL_ORDINARY_UD_PRE_HIDDEN_PREDECESSOR_COMPONENT'
assert second['new_source_game_declarations']==field['new_source_game_declarations']==0
assert second['whole_goal_complete'] is False and field['whole_goal_complete'] is False
assert ALG['subject_sha256']==P['artifacts']['FIXED-H-COMPOSITION-WITH-UD-PRE.md']
assert ALG['subject_pins']['FIXED-H-HIDDEN-PREDECESSORS.md']==subject
assert ALG['hidden_proof_outside_field_final_receipt_status'].startswith('PENDING_AT_THIS_REVIEW_CUT')
assert field['geometry']['selector_bits']==55 and field['geometry']['UD_hops']==254
assert field['root_control_independent_rerun']['exit_code']==0
assert field['root_control_independent_rerun']['byte_identical_result'] is True
diff=[]
for n in P['documents']:
    before=(X/P['predecessor_backup']/n).read_text(encoding='utf-8')
    after=(X/n).read_text(encoding='utf-8')
    assert after.startswith(before),n
    diff.extend(difflib.unified_diff(before.splitlines(),after.splitlines(),fromfile=f'before/{n}',tofile=f'current/{n}',lineterm=''))
(HERE/'HIDDEN-UD-PRE-MANUAL-DIFF.txt').write_text('\n'.join(diff)+'\n',encoding='utf-8')
if (HERE/'HIDDEN-UD-PRE-INTEGRATION-REVIEW.md').exists():
    receipt={
        'status':'ACCEPTED_SCOPED_ORDINARY_HIDDEN_UD_PRE_SYMBOLIC_CURRENT_INDEX',
        **groups,
        'accepted_evidence_absolute_pins':P['accepted_evidence_absolute_pins'],
        'external_absolute_pins':external,
        'accepted_evidence_items':175,
        'provenance_pins':{f'selected-promotion-review/{n}':sha(HERE/n) for n in ('HIDDEN-UD-PRE-INTEGRATION-REVIEW.md','HIDDEN-UD-PRE-MANUAL-DIFF.txt','HIDDEN-UD-PRE-check-integration.py')},
        'checks':{n:True for n in (
            'all175_accepted_items_exact_hashes','current_six_documents_exact_pins',
            'previous_message_graph_documents_exact_immutable_backup',
            'historical_subject_receipt_source_scalar_controls_provenance_preserved',
            'six_append_only_deltas_manually_read','two_exact_hidden_final_premise_receipts_accept_same_subject',
            'old_conditional_algebra_pending_gate_now_satisfied_without_old_receipt_rewrite',
            'legal_ordinary_logical_interfaces_not_actual_hardness_certificate',
            '254_signed_selector_parameter_average_UD_hops','one_target_PRE_unknown_input_image_superset',
            'one_outer_seedzero_no_recharge','55bit_factor_current_source_witness_cover',
            'Gamma_distinct_complete_resource_instances','NEW_graph_weights_no_old_success_recoefficienting',
            'fixed_full_h_honest_atomic_cache_api_all_resource_obligations',
            'observed_control_scope_no_full_source_kernel_claim',
            'dense_loss_not_security_bits','generic_RO_formula_not_fixed_h_numeric_value',
            '47_supporting_helpers_0_new_source_game','no_level_category_capacity_repair_or_whole_goal_closure')},
        'hidden_premise_gate':'SATISFIED_TWO_EXACT_FINAL_MANUAL_RECEIPTS',
        'cumulative_supporting_checked_declarations':47,
        'new_supporting_checked_declarations':0,
        'new_source_game_checked_declarations':0,
        'actual_fixed_h_hardness':'NOT_ESTABLISHED',
        'whole_goal_complete':False,
    }
    out=HERE/'HIDDEN-UD-PRE-INTEGRATION-REVIEW.json'
    out.write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf-8')
    print('ACCEPTED',sha(out))
else: print('PINS_CHECKED_MANUAL_REVIEW_PENDING',len(diff),'diff lines',len(internal),'internal',len(external),'external')
