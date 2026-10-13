import hashlib
import json
from pathlib import Path
HERE=Path(__file__).resolve().parent
X=HERE.parents[1]
PEER=X/'outside-field-check/message-hash-identification'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
assert sha(HERE/'INDEPENDENT-FIRST.md')=='540ae17ba73ff61d178c3f8c96601bff18db857138c078f54b22ba10dfeb609f'
assert sha(HERE/'CONTEXT-LIFT-CLARIFICATION.md')=='514cc20605b3f6f3306ebf4cca87a32846b6ca596e27ba21434c345d809e5f41'
assert sha(PEER/'INDEPENDENT-FIRST.md')=='b07700807df0f78be2272afd7a5372044603b92697b3760afaa8cdfac5a3a1df'
assert (HERE/'peer-rerun-successor/CONTROL-RESULTS.json').read_bytes()==(PEER/'CONTROL-RESULTS.json').read_bytes()
assert sha(HERE/'peer-rerun/CONTROL-RESULTS.json')=='578d7aea2a86f2d5af9492566e2d7f11e25248d9465da3e0e60bf74e5e311b0e'
primary=[
 (HERE/'sphincs-round3-specification.pdf','540968e4d58cb582d5f85636beed7a10894622ed8b99a7a863f85996869743c6',HERE/'sphincs-round3-specification.txt','official round3 Section9.1 printed48/PDF47'),
 (Path(r'C:\Users\angel\Desktop\paper\PAPERS\LUGEL\research\lula22\R4\R4B-rollback-tolerant-state\refs\sphincsplus_r31\sphincs+-r3.1-specification.pdf'),'1169896fff4160e7a294162b8a3e061ffdf1888f3925f5614532c28bd3473c4a',Path(r'C:\Users\angel\Desktop\paper\PAPERS\LUGEL\research\lula22\R4\R4B-rollback-tolerant-state\refs\sphincsplus_r31\sphincs+-r3.1-specification.txt'),'official r3.1 Section9.1 printed49/text1911-1935'),
 (Path(r'C:\Users\angel\Desktop\paper\PAPERS\LUGEL\research\lula22\M-measure\M2-sphincs-reparam\refs\eprint_2022_346_hulsing_kudinov_tight.pdf'),'80dcd11e56448d07e2a2465a11ef1a9ca8f4561387abeb3fabdd6d40d4ffe3c3',Path(r'C:\Users\angel\Desktop\paper\PAPERS\LUGEL\research\lula22\M-measure\M2-sphincs-reparam\refs\eprint_2022_346_hulsing_kudinov_tight.txt'),'HK22 AppendixA Definition11 printed30/PDF29'),
]
for pdf,h,txt,anchor in primary:assert sha(pdf)==h
assert sha(primary[1][2])=='ddaf6d600a05c2e9b3bef113bf995827a79f76616f09f8e7b4cef0ba90e17323'
SRC=Path(r'C:\Users\angel\Desktop\paper\PAPERS\LUGEL\research\lula22\publications\LULA-I\release\code\lula1\src\lib.rs')
assert sha(SRC)=='ac8e67f05af68dd8e1291c5909847f74103903fb7ffa2c70f500c6ec48f14210'
names=('INDEPENDENT-FIRST.md','CONTEXT-LIFT-CLARIFICATION.md','controls.py','CONTROL-RESULTS.json','PEER-REVIEW.md','REVIEW-CLARIFICATION.md','rerun-peer.py','peer-rerun/CONTROL-RESULTS.json','archive-and-rerun-peer-successor.py','peer-rerun-successor/CONTROL-RESULTS.json')
receipt={
 'status':'ACCEPTED_MANUAL_NAMED_FIXED_H_COVERAGE_ADAPTER_WITH_PRIMARY_LIFTING_GAP_OPEN',
 'own_first_and_context_lift_saved_before_new_peer_read':True,
 'files':{n:sha(HERE/n) for n in names},
 'peer_subject_pins':{str((PEER/n).relative_to(X)).replace('\\','/'):sha(PEER/n) for n in ('INDEPENDENT-FIRST.md','CLARIFICATION.md','EVENT-BINDING.md','controls.py','CONTROL-RESULTS.json')},
 'primary_versions':[{'pdf':str(pdf),'pdf_sha256':h,'text':str(txt),'text_sha256':sha(txt),'anchor':anchor} for pdf,h,txt,anchor in primary],
 'source_path':str(SRC),'source_sha256':sha(SRC),
 'event_anchor':{'CHANGED-CHILD-EXTRACTION.md':sha(X/'CHANGED-CHILD-EXTRACTION.md')},
 'event':'Win AND indexed C_cov:17 real routed-instance tuples from completed honest responses',
 'conditional_inequality':'Pr_SrcFJideal_h[Win AND C_cov] <= Succ_named_CTAC_fixed_h(B)',
 'checks':{n:True for n in (
  'primary_nonce_and_output_explicit_versions_pinned','no_invented_C_ITSR_citation','full256_same_h_inner_outer_and_aliases',
  'source17real_zero9_and41route_correct','memoized_J_repaired_by_first_label_caching',
  'source_root_F_jointlaw_not_independent_uniform_root','tagged_logical_context_decodes_exact_literal_sourcewords',
  'B_retains_consistent_F_for_signature_auxiliaries','prekey_quantum_continuation_retained',
  'canonical_target_free_valid_final_counter_gap_explicit','finite_BE32_bottom_unnormalized',
  'superset_target_registration_or_absorbing_completion_no_false_exposure','safe_final_Win_fresh_Ccov_binding',
  'own_controls_exit0','peer_controls_independent_rerun_exit0_byte_identical','all_challenger_local_runtime_bytes_circuits_charged',
  'no_new_seedzero_charge_interface_identity','no_HJ_h_equals_HJ_O_or_uniform_lowerbit_inference')},
 'ordinary_ITSR_quantitative_transfer':'OPEN',
 'named_additional_property_hardness':'ASSUMED_WITHOUT_NUMERICAL_CERTIFICATE',
 'new_kernel_declarations':0,'new_source_game_checked_declarations':0,
 'source_attack_benchmark_or_manuscript_change':False,'whole_goal_complete':False,
}
(HERE/'REVIEW-RECEIPT.json').write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf-8')
print(sha(HERE/'REVIEW-RECEIPT.json'))
