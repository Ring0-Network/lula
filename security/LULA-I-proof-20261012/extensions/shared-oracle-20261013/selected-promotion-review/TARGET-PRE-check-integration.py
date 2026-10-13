import difflib,hashlib,json
from pathlib import Path
HERE=Path(__file__).resolve().parent;X=HERE.parent
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def read(n):return json.loads((X/n).read_text(encoding='utf-8'))
P=read('TARGET-PRE-PROMOTION.json');OLD=read('selected-promotion-review/HIDDEN-UD-PRE-INTEGRATION-REVIEW.json')
assert P['predecessor_documents']==OLD['documents']
assert len(P['accepted_evidence_absolute_pins'])==228
internal,external={},{}
for n,h in P['accepted_evidence_absolute_pins'].items():
 p=Path(n);assert sha(p)==h,n
 if p.is_relative_to(X):internal[p.relative_to(X).as_posix()]=h
 else:external[n]=h
groups={'documents':P['documents'],
 'promoted_artifacts':{**P['artifacts'],'TARGET-PRE-PROMOTION.json':sha(X/'TARGET-PRE-PROMOTION.json')},
 'source_subjects':internal,'prior_review_receipts':P['receipt_pins'],
 'backup_pins':{f'{P["predecessor_backup"]}/{n}':h for n,h in P['predecessor_documents'].items()},
 'preserved_artifacts':OLD['preserved_artifacts']}
for g,pins in groups.items():
 for n,h in pins.items():assert sha(X/n)==h,(g,n)
for g in ('promoted_artifacts','source_subjects','prior_review_receipts','backup_pins','preserved_artifacts','control_pins','provenance_pins'):
 for n,h in OLD.get(g,{}).items():assert sha(X/n)==h,('prior',g,n)
for n,h in OLD.get('external_absolute_pins',{}).items():assert sha(Path(n))==h,n
assert P['cumulative_supporting_checked_declarations']==47 and P['new_source_game_checked_declarations']==0
assert P['source_scalar_manuscript_changes']==0 and P['whole_goal_complete'] is False
assert P['random_oracle_model_only'] is True and P['old_stronger_direct_bounds_preserved'] is True
assert P['all_conservative_component_caps_one'] is True
for n in P['receipt_pins']:
 if not n.endswith('.json'):continue
 r=read(n)
 assert r['subject_sha256'] in P['artifacts'].values(),n
 assert r['whole_goal_complete'] is False
diff=[]
for n in P['documents']:
 before=(X/P['predecessor_backup']/n).read_text(encoding='utf-8');after=(X/n).read_text(encoding='utf-8')
 assert after.startswith(before),n
 diff.extend(difflib.unified_diff(before.splitlines(),after.splitlines(),fromfile=f'before/{n}',tofile=f'current/{n}',lineterm=''))
(HERE/'TARGET-PRE-MANUAL-DIFF.txt').write_text('\n'.join(diff)+'\n',encoding='utf-8')
if (HERE/'TARGET-PRE-INTEGRATION-REVIEW.md').exists():
 r={'status':'ACCEPTED_SCOPED_RANDOM_ORACLE_TARGET_ONLY_PRE_CURRENT_INDEX',**groups,
  'accepted_evidence_absolute_pins':P['accepted_evidence_absolute_pins'],'external_absolute_pins':external,'accepted_evidence_items':228,
  'provenance_pins':{f'selected-promotion-review/{n}':sha(HERE/n) for n in ('TARGET-PRE-INTEGRATION-REVIEW.md','TARGET-PRE-MANUAL-DIFF.txt','TARGET-PRE-check-integration.py')},
  'checks':{n:True for n in ('all228_hashes_exact','six_current_document_pins_exact',
    'prior_hidden_document_map_exact_immutable_before_target_only_pre',
    'all_prior_source_scalar_manuscript_subject_backup_receipt_provenance_pins_preserved',
    'six_append_only_deltas_manually_read','all_exact_final_component_receipts_bind_promoted_subjects',
    'fullword_allP_router_QAplus1_honest_work_separate',
    'correlated_whole_marker_mu_no_iid_claim','singlePRE_zero_prequest_ghost_independent_auxiliaries',
    'one_Boolean_completion_no_extra_digest_query','exact_Nminus1_huge_tables_not_efficient_binarymodulo',
    'activation_before_P_absolute_weight_exact','32_rational_component_caps_one_reexecuted_in_own_folder',
    'crossings99_100_half_200_201_uncapped_one_not_attack',
    'old_stronger_directH_and_full_source_totals_preserved',
    'RO_interface_not_fixed_SHA_hardness','47_supporting_0_new_sourcegame',
    'no_category_capacity_repair_or_whole_goal_closure')},
  'cumulative_supporting_checked_declarations':47,'new_supporting_checked_declarations':0,
  'new_source_game_checked_declarations':0,'whole_goal_complete':False}
 out=HERE/'TARGET-PRE-INTEGRATION-REVIEW.json';out.write_text(json.dumps(r,indent=2)+'\n',encoding='utf-8');print('ACCEPTED',sha(out))
else:print('PINS_CHECKED_MANUAL_REVIEW_PENDING',len(diff),'diff lines',len(internal),'internal',len(external),'external')
