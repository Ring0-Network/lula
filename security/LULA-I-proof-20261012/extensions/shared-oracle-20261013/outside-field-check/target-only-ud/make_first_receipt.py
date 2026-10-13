from pathlib import Path
import hashlib,json
HERE=Path(__file__).resolve().parent
ROOT=HERE.parent.parent
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
source=Path(r'C:\Users\angel\Desktop\paper\PAPERS\LUGEL\research\lula22\publications\LULA-I\release\code\lula1\src\lib.rs')
hk=Path(r'C:\Users\angel\Desktop\paper\PAPERS\LUGEL\research\lula22\M-measure\M2-sphincs-reparam\refs\eprint_2022_346_hulsing_kudinov_tight.txt')
assert sha(HERE/'INDEPENDENT-FIRST.md')=='fca41de9835bd7b681fac94ecbd8a521f00361d7a2c007cb8410e1655c5650bd'
assert sha(source)=='ac8e67f05af68dd8e1291c5909847f74103903fb7ffa2c70f500c6ec48f14210'
assert sha(hk)=='be27fac74e2885f3d5fe4b7a24a09b3166ba82e4c726e988766527c29293c561'
controls=json.loads((HERE/'CONTROL-RESULTS.json').read_text())
assert controls['script_sha256']==sha(HERE/'controls.py')
out={
 'status':'SOURCE_FIRST_MANUAL_TARGET_ONLY_QUERY_ROUTER_DERIVED_CONTROLS_PASS',
 'own_first_saved_before_any_new_target_only_peer_root_artifact_read':True,
 'direction_provenance':'Parent supplied research direction and all-P slice/phase-router sketch during own source/primary derivation; no claim of independent discovery',
 'own_pins':{n:sha(HERE/n) for n in ['INDEPENDENT-FIRST.md','controls.py','CONTROL-RESULTS.json']},
 'source':{'path':str(source),'sha256':sha(source),'anchors':'69-95;121-151;161-187;239-267;479-584;601-729'},
 'accepted_hidden_subject_sha256':sha(ROOT/'FIXED-H-HIDDEN-PREDECESSORS.md'),
 'primary':{'text':str(hk),'text_sha256':sha(hk),'pdf_sha256':sha(hk.with_suffix('.pdf')),'UD_anchor':'HK22 Section8.3 Lemma3 text1065-1078/printed24; Algorithm4 text1081-1095','PRE_constant_scope':'Section8.1 text990-1000 supports single-target asymptotic discussion; no explicit finite constant invented here'},
 'model':'ONE full shared O:bytes->256 random oracle; ideal independent persistent private F/J; source S!=0 conjunction. No fixed-SHA hardness inference.',
 'router':{'slice':'ALL P16||zero48||selectedT22||x16, length102','high':'unknown random H(P,x),128 bits','low':'independent low128 G(w)','off_slice':'full256 G(w)','coherent_implementation':'One ordinary XOR H query with clean |+> response scratch and controlled SWAP; one known G evaluation with high-limb mask; no controlled black-box assumption or measurement'},
 'remote_public_query_cap':'Q_A+1 including coherent pre-key/all continuing A full-raw queries and at most one final selected typed verifier call; ordinary target service separately accounted',
 'local_outside_budget':'2T_all independence with ALL honest and A G invocations; all generation/field/key/evaluator/storage/circuit costs charged, not free namespace table',
 'activation':{'D_H':20229886488608768,'D_active_r':'32*(2^41+2^36+2^31+2^26)*max(14-r,0)+16*2^21*max(254-r,0)','sum_D_active':7628143271608320,'UD_bound':'delta_r <= D_active_r/2^55 * 12*(Q_A+1)/2^64','PRE_bound':'pi_PRE <= D_H/2^55 * kappa_PRE(Q_A+1,128)'},
 'source_bound_schematic':'Pr_HJ_O[Win AND H_final AND S!=0] <= min(1,D_H*kappa_PRE(Q_A+1,128)+12*7628143271608320*(Q_A+1)/2^64)',
 'explicit_finite_PRE_constant':'OPEN_INPUT_NOT_INVENTED',
 'checks':{'all_parameter_prekey_slice_not_current_S_only':True,'full_lower128_joint_random_reply_preserved':True,'actual_nonzero_S_raw_inner_separation':True,'S0_alias_negative_control':True,'other_typed_addresses_lengths_partitioned':True,'designated_selected_images_intercepted_persistently':True,'final_selected_hash_counted_once_and_reused':True,'ordinary_HK_randomTh_UD_query_bound_applicable':True,'known_independent_outside_circuits_not_unknown_H_queries':True,'all_honest_outside_calls_counted_in_T_all':True,'no_programming_no_nohit_no_history_measurement':True},
 'control_execution':{'exit_code':0,'unitary_checks':4160,'actual_byte_checks':33,'selected_uniform_joint_tables':256,'scope':controls['scope']},
 'new_source_game_declarations':0,
 'source_manuscript_old_scalar_prior_receipt_edits':0,
 'fixed_h_hardness_numeric_security_category_capacity':'NOT_ESTABLISHED',
 'whole_goal_complete':False,
 'builder_sha256':sha(Path(__file__)),
}
(HERE/'SOURCE-FIRST-RECEIPT.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf8')
print('SOURCE-FIRST-RECEIPT.json',sha(HERE/'SOURCE-FIRST-RECEIPT.json'))
print('CONTROL-RESULTS.json',sha(HERE/'CONTROL-RESULTS.json'))
