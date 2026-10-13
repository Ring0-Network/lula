import hashlib,json
from pathlib import Path
HERE=Path(__file__).resolve().parent
X=HERE.parent
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
subject='ece1d8311059d3b7d8dd3f2aca091ab28b2e17fb8cdff84fc2792e1443e892ae'
assert sha(X/'FIXED-H-COMPOSITION.md')==subject
rows=[2**41,2**36,2**31,2**26,2**21]; heights=[5,5,5,5,21]; low=sum(rows[:4])
counts={16:480*low+4080*rows[4]+2**41*17*512,32:sum(r-r//2**h for r,h in zip(rows,heights))+2**41*17*511,256:2**21,272:2**41,512:low}
pads={m:(n-1).bit_length() for m,n in counts.items()}
assert list(pads.values())==[55,55,21,41,42]
assert sum(counts.values())==39339469515522047
qlogs=[24,30,38,40,41,44,50,64]
sparse=[17*(32+lq) for lq in qlogs]
assert sparse==[952,1054,1190,1224,1241,1292,1394,1632]
artifactnames=('CHANGED-CHILD-EXTRACTION.md','PRIVATE-FIXED-H-REDUCTION.md','STANDARD-CANONICAL-COMPONENT.md','FIXED-H-GRAPH-COMPONENT.md','MESSAGE-HASH-PRIMITIVE-COMPONENT.md','MESSAGE-HASH-ORDINARY-LIFT.md','CLASSICAL-RO-THEOREM.md','QUANTUM-RO-THEOREM.md','bounds.py','bounds-event-specific.py')
SRC=Path(r'C:\Users\angel\Desktop\paper\PAPERS\LUGEL\research\lula22\publications\LULA-I\release\code\lula1\src\lib.rs')
assert sha(SRC)=='ac8e67f05af68dd8e1291c5909847f74103903fb7ffa2c70f500c6ec48f14210'
result={
 'status':'ACCEPTED_EXACT_FINAL_MANUAL_SYMBOLIC_FIXED_H_COMPOSITION_SUBJECT',
 'subject_sha256':subject,
 'subject_pins':{'FIXED-H-COMPOSITION.md':subject},
 'artifact_pins':{n:sha(X/n) for n in artifactnames},
 'own_pins':{n:sha(HERE/n) for n in ('FINAL-COMPOSITION-SUBJECT-REVIEW.md','FINAL-COMPOSITION-check.py','message-hash-identification/FINAL-ORDINARY-SUBJECT-REVIEW.json','message-hash-identification/DIRECT-COMPONENT-SUBJECT-REVIEW.json')},
 'source_path':str(SRC),'source_sha256':sha(SRC),
 'payload_byte_domains':counts,'new_selector_bits':pads,'sparse_loss_exponents':sparse,
 'checks':{n:True for n in ('private_particular_signed_average_no_new_S0','source_pointwise_Win_fresh_root_cover','real17_completed_index_exposures','global_first_G_witness_independent_selector','NEW_perclass55_55_21_41_42_program_success_binding','bytes_bits_members_consistent','other_tweak_cone_allmembers_excludes_challenge','old_common56_successes_not_recoefficiented','particular_success_vs_maxinsecurity_separated','Gamma_cov_three_distinct_adversary_resource_instances','total_rank_family_dense_q_vs_sparse_k_targets','q0_coverage_zero','type7_unconditional42_21_no_extra_eta','outer_seedzero_mass_paid_once','epsilon_H_explicit_OPEN_not_PRE_or_TCR','all_source_challenger_h_memory_byte_circuit_costs','loss_arithmetic_not_security_bits','no_fixed_h_equals_RO_or_actual_gamma_numeric','honest_cache_transfer_keeps_premise','old_source_manuscript_scalar_unchanged')},
 'current_index_review':False,'new_source_game_checked_declarations':0,
 'epsilon_H':'OPEN','actual_family_hardness':'NOT_ESTABLISHED',
 'whole_goal_complete':False,
}
(HERE/'FINAL-COMPOSITION-SUBJECT-REVIEW.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(sha(HERE/'FINAL-COMPOSITION-SUBJECT-REVIEW.json'))
