"""Pin-check third-reader type7 resource/scope and exact control acceptance."""
from pathlib import Path
import hashlib,json
X=Path(__file__).resolve().parents[1]
OUT=Path(__file__).resolve().parent
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
read=lambda p:json.loads(p.read_text(encoding='utf-8-sig'))
prior=read(OUT/'QPRE-INTEGRATION-REVIEW.json')
for group in ('documents','promoted_artifacts','preserved_artifacts'):
    for n,h in prior[group].items():assert sha(X/n)==h,n
controls=read(OUT/'T7-CONTROL-RESULTS.json')
assert controls['script_sha256']==sha(OUT/'T7-Exact-Control.py')
assert controls['WOTS_rows']==2269959421952 and controls['selector_pad']==2**42
assert controls['source_counter_cap']==2**32 and len(controls['q_resource_rows'])==8
assert len(controls['cases'])==3 and all(c['fresh_different_base_prefix_hit_given_success']=='1/4' for c in controls['cases'])
assert controls['source_slice_cardinalities']['lower32x16sum240']=='5181241160064611531897369560287267312'
assert controls['source_slice_cardinalities']['top16x256sum2040']=='454918678781617793203528879683071744'
names=['chain-pre-independent/type7/INDEPENDENT_DERIVATION.md',
       'chain-pre-adapter/type7/INDEPENDENT-DERIVATION.md',
       'chain-pre-adapter/type7/CLARIFICATION.md',
       'chain-pre-independent/type7/REVIEW.json',
       'chain-pre-independent/type7/SECOND-READER.md']
peer=read(X/'chain-pre-independent/type7/REVIEW.json')
assert peer['subject_sha256']==sha(X/'chain-pre-adapter/type7/INDEPENDENT-DERIVATION.md')
assert peer['source_sha256']=='ac8e67f05af68dd8e1291c5909847f74103903fb7ffa2c70f500c6ec48f14210'
clar=(X/'chain-pre-adapter/type7/CLARIFICATION.md').read_text(encoding='utf8')
for phrase in ('D7_base_final','D7_base_public','not a claim that the actual terminated B supplies','does not introduce a new source abort','No division by this success probability','Fresh off-base prefix-equality chance is2^-128'):
    assert phrase in clar,phrase
release=Path(r'C:\Users\angel\Desktop\paper\PAPERS\LUGEL\research\lula22\publications\LULA-I\release\code\lula1\src\lib.rs')
assert sha(release)==peer['source_sha256']
ownnames=['T7-INDEPENDENT-RESOURCES.md','T7-RESOURCE-REVIEW.md','T7-Exact-Control.py','T7-CONTROL-RESULTS.json']
receipt={
 'verdict':'ACCEPT_SCOPED_FIRST_ACCEPTED_TYPE7_ROW_RESOURCES_AND_INTERFACE',
 'subject_pins':{n:sha(X/n) for n in names},
 'own_pins':{n:sha(OUT/n) for n in ownnames},
 'prior_quantum_PRE_current_receipt_sha256':sha(OUT/'QPRE-INTEGRATION-REVIEW.json'),
 'prior_documents':prior['documents'],'preserved_scalar_artifacts':prior['preserved_artifacts'],
 'source_sha256':sha(release),'rows':2269959421952,'selector_bits':42,'selector_pad':2**42,
 'C_public_max':17392,'C_F_distinct_max':8704,'higher_child_public':15423,'higher_child_F':1024,
 'target_row_challenge_preprocessing_cap':2**32,
 'selected_B_cap':'Q_H+1 or Q_q coherent plus1 final classical, using supplied canonical target shortcuts',
 'raw_quantum_router':'one selected plusone outside call per logical query',
 'collision_predicate':'different16-bytebase,128-prefix equality, full256 images retained',
 'row_failure':'Unconditioned local B zero-contribution branch; not a new global source abort',
 'source_event':'original exposed successful final D7_base_final; optional broader classical D7_base_public distinct',
 'fresh_different_base_probe_probability':'1/2^128 conditional on registered row, no1/p',
 'checker_sha256':sha(Path(__file__)),
 'checks':{'saved_source_counts_before_peer_read':True,'exact_C_before_own_restriction':True,
  'full_row_counter_lower_limb_and_bottom_law':True,'challenge_preprocessing_not_hidden_in_A_budget':True,
  'fixed_table_public_classical_coherent_calls':True,'early_extraction_source_prefix_not_full_later_transcript':True,
  'final_and_broader_classical_events_not_conflated':True,'global_partiality_not_conditioned':True,
  'scalar_calculator_and_prior_documents_unchanged':True,'conventional_and_efficiency_still_open':True},
 'new_checked_supporting_declarations':0,'prior_checked_supporting_declarations':40,
 'full_source_game_checked_declarations':0,'conventional_S_TCR':'OPEN',
 'efficient_quantum_outside':'OPEN','category_capacity':'not established','whole_goal_complete':False}
(OUT/'T7-REVIEW.json').write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf8')
print(json.dumps({'verdict':receipt['verdict'],'rows':receipt['rows'],'control_cases':3,'q_rows':8,
 'receipt_sha256':sha(OUT/'T7-REVIEW.json')}))
