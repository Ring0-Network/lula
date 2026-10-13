import difflib
import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
X = HERE.parent
def sha(path): return hashlib.sha256(path.read_bytes()).hexdigest()
def read(name): return json.loads((X/name).read_text(encoding='utf-8'))
P = read('MESSAGE-GRAPH-PROMOTION.json')
OLD = read('selected-promotion-review/PRIMITIVE-INTEGRATION-REVIEW.json')
assert OLD['documents'] == P['predecessor_documents']
assert len(P['accepted_evidence_absolute_pins']) == 145
internal, external = {}, {}
for name,h in P['accepted_evidence_absolute_pins'].items():
    path = Path(name)
    assert sha(path) == h, name
    if path.is_relative_to(X): internal[path.relative_to(X).as_posix()] = h
    else: external[name] = h
groups = {
    'documents':P['documents'],
    'promoted_artifacts':{**P['artifacts'],'MESSAGE-GRAPH-PROMOTION.json':sha(X/'MESSAGE-GRAPH-PROMOTION.json')},
    'source_subjects':internal,
    'prior_review_receipts':P['receipt_pins'],
    'backup_pins':{f'{P["predecessor_backup"]}/{n}':h for n,h in P['predecessor_documents'].items()},
    'preserved_artifacts':OLD['preserved_artifacts'],
}
for group,pins in groups.items():
    for name,h in pins.items(): assert sha(X/name)==h,(group,name)
for group in ('promoted_artifacts','source_subjects','backup_pins','preserved_artifacts','control_pins','prior_review_receipts','provenance_pins'):
    for name,h in OLD.get(group,{}).items(): assert sha(X/name)==h,('prior',group,name)
for name,h in OLD.get('external_absolute_pins',{}).items(): assert sha(Path(name))==h,('prior external',name)
assert P['source_scalar_manuscript_changes']==0
assert P['cumulative_supporting_checked_declarations']==47
assert P['new_source_game_checked_declarations']==0
assert P['whole_goal_complete'] is False
projection = read('root-message-hash/PROJECTION-CHECK.json')
assert projection['exit_code']==0 and projection['checked_declarations']==3
assert projection['new_source_game_checked_declarations']==0
assert projection['axiom_sets']==[['Quot.sound','propext']]*3
assert sha(X/'root-message-hash/DigestProjection.lean')==projection['source_sha256']
ordinary=read('selected-promotion-review/message-hash-identification/FINAL-ORDINARY-SUBJECT-REVIEW.json')
ordinary_peer=read('outside-field-check/message-hash-identification/FINAL-ORDINARY-SUBJECT-REVIEW.json')
graph=read('graph-collection-second/FINAL-SUBJECT-REVIEW.json')
composition=read('selected-promotion-review/FINAL-COMPOSITION-SUBJECT-REVIEW.json')
for name,h in ordinary['subject_pins'].items(): assert P['artifacts'][name]==h
assert ordinary_peer['subject']['sha256']==P['artifacts']['MESSAGE-HASH-ORDINARY-LIFT.md']
assert graph['graph_subject_sha256']==P['artifacts']['FIXED-H-GRAPH-COMPONENT.md']
assert composition['subject_sha256']==P['artifacts']['FIXED-H-COMPOSITION.md']
assert graph['composition_subject']=='FIXED-H-COMPOSITION-CANDIDATE.md'
assert graph['composition_subject_sha256']!=composition['subject_sha256']
assert composition['whole_goal_complete'] is False and ordinary['whole_goal_complete'] is False
assert composition['epsilon_H']=='OPEN'
assert composition['new_selector_bits']=={'16':55,'32':55,'256':21,'272':41,'512':42}
assert P['epsilon_H']=='OPEN; no interior transfer relied upon'
assert P['ordinary_family_hardness']=='ASSUMED_WITHOUT_NUMERICAL_CERTIFICATE'
diff=[]
for name in P['documents']:
    before=(X/P['predecessor_backup']/name).read_text(encoding='utf-8')
    after=(X/name).read_text(encoding='utf-8')
    assert after.startswith(before), ('non-append alteration',name)
    diff.extend(difflib.unified_diff(before.splitlines(),after.splitlines(),fromfile=f'before/{name}',tofile=f'current/{name}',lineterm=''))
(HERE/'MESSAGE-GRAPH-MANUAL-DIFF.txt').write_text('\n'.join(diff)+'\n',encoding='utf-8')
if (HERE/'MESSAGE-GRAPH-INTEGRATION-REVIEW.md').exists():
    receipt={
        'status':'ACCEPTED_SCOPED_MESSAGE_GRAPH_FIXED_H_SYMBOLIC_CURRENT_INDEX',
        **groups,
        'accepted_evidence_absolute_pins':P['accepted_evidence_absolute_pins'],
        'external_absolute_pins':external,
        'accepted_evidence_items':145,
        'provenance_pins':{f'selected-promotion-review/{n}':sha(HERE/n) for n in ('MESSAGE-GRAPH-INTEGRATION-REVIEW.md','MESSAGE-GRAPH-MANUAL-DIFF.txt','MESSAGE-GRAPH-check-integration.py')},
        'checks':{n:True for n in (
            'current_six_documents_exact_pins','all145_accepted_items_exact_hashes',
            'prior_primitive_documents_match_immutable_before_message_graph',
            'historical_primitive_receipt_artifacts_subjects_backups_controls_preserved',
            'six_deltas_append_only_and_manually_read','four_exact_final_subjects_previously_read_and_accepted',
            'graph_reader_old_composition_candidate_scope_not_final_subject_acceptance',
            'ordinary_dense_q_vs_sparse_k_distinct_resources','total_rank_family_exante_domain_full_h_nonce_law',
            'loss_2pow544_not_security_bits','real17_not_eighteen_secret_trees',
            'tagged297_namespace_only41_route_entropy','new_per_class_55_55_21_41_42_successes_not_old_common56',
            'all_full_h_other_tweak_alias_and_source_runtime_obligations_retained',
            'fixed_h_signed_private_average_no_additional_seedzero','single_outer_seedzero_charge',
            'symbolic_gamma_alternatives_require_particular_adversary_resources',
            'epsilon_H_explicitly_open_and_uniform_start_candidate_not_relied_upon',
            'all_prior_scalar_source_theorems_unchanged','three_projection_helpers_only_same_word',
            'supporting47_new_source_game0','no_SHA_numeric_category_capacity_or_whole_goal_closure')},
        'cumulative_supporting_checked_declarations':47,
        'new_supporting_checked_declarations':3,
        'new_source_game_checked_declarations':0,
        'fixed_SHA_hardness_or_category_claim':False,
        'whole_goal_complete':False,
    }
    (HERE/'MESSAGE-GRAPH-INTEGRATION-REVIEW.json').write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf-8')
    print('ACCEPTED',sha(HERE/'MESSAGE-GRAPH-INTEGRATION-REVIEW.json'))
else: print('PINS_CHECKED_MANUAL_REVIEW_PENDING',len(diff),'diff lines',len(internal),'internal',len(external),'external')
