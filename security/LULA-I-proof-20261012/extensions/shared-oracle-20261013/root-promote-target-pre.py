from pathlib import Path
import hashlib,json,shutil
X=Path(__file__).resolve().parent
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
read=lambda n:json.loads((X/n).read_text(encoding='utf8'))
docs=['PROOF.md','OPEN.md','TERM-TABLE.md','REQUIREMENT-MAP.md','HANDOFF.md','SECURITY-CRITERION.md']
prior=read('HIDDEN-UD-PRE-PROMOTION.json')
index=read('selected-promotion-review/HIDDEN-UD-PRE-INTEGRATION-REVIEW.json')
assert all(index['checks'].values())
assert all(sha(X/n)==h for n,h in prior['documents'].items())
receipt_names=[
 'outside-field-check/target-only-ud/FINAL-SUBJECT-REVIEW.json',
 'outside-field-check/target-only-ud/single-pre-third/FINAL-SUBJECT-REVIEW.json',
 'outside-field-check/target-only-ud/FINAL-HIDDEN-BOUND-REVIEW.json',
 'selected-promotion-review/quantitative-goal-audit/single-pre/FINAL-SUBJECT-REVIEW.json',
 'selected-promotion-review/quantitative-goal-audit/single-pre/FINAL-TARGET-HIDDEN-SUBJECT-REVIEW.json',
 'pre-start-second/interior-ud/quantitative-boundary/activation/single-pre/FINAL-SUBJECT-REVIEW.json']
receipts=[read(n) for n in receipt_names]
for d in receipts:
    assert all(d['checks'].values()),'A final-subject check failed.'
    assert not d['whole_goal_complete']
    assert d.get('new_source_game_declarations',d.get('new_source_game_checked_declarations'))==0
assert receipts[0]['subject_sha256']==sha(X/'TARGET-ONLY-UD-RO.md')
assert receipts[1]['subject_sha256']==receipts[3]['subject_sha256']==receipts[5]['subject_sha256']==sha(X/'SINGLE-TARGET-PRE-RO.md')
assert receipts[2]['subject_sha256']==receipts[4]['subject_sha256']==sha(X/'TARGET-ONLY-HIDDEN-BOUND.md')
pins=dict(prior['accepted_evidence_absolute_pins'])
def add(n,h=None):
    p=Path(n)
    if not p.is_absolute():p=X/p
    actual=sha(p)
    if h is not None:assert actual==h,str(p)
    pins[str(p)]=actual
for prefix,d in zip([str(Path(n).parent) for n in receipt_names],receipts):
    for group in ('own_pins','peer_first_pins','supporting_subject_pins','subject_pins','premise_receipt_pins','preserved_artifacts','preserved_old_direct_subject_pins','prior_target_only_subject_and_receipt_pins','root_quantitative_pins','activation_peer_pins'):
        for n,h in d.get(group,{}).items():
            if not isinstance(h,str) or len(h)!=64:continue
            p=Path(n)
            if p.is_absolute():add(p,h)
            elif group=='activation_peer_pins':add('pre-start-second/interior-ud/quantitative-boundary/activation/'+n,h)
            elif group=='root_quantitative_pins':add('root-target-only-ud/'+n,h)
            elif (X/n).is_file():add(n,h)
            elif (X/prefix/n).is_file():add(str(Path(prefix)/n),h)
            else:raise AssertionError((prefix,group,n))
for n,h in index['provenance_pins'].items():add(n,h)
artifacts=['TARGET-ONLY-UD-RO.md','SINGLE-TARGET-PRE-RO.md','TARGET-ONLY-HIDDEN-BOUND.md']
for n in artifacts+receipt_names+['root-target-only-ud/quantitative.py','root-target-only-ud/QUANTITATIVE-RESULTS.json',
 'root-target-only-ud/router_controls.py','root-target-only-ud/ROUTER-CONTROLS.json',
 'selected-promotion-review/HIDDEN-UD-PRE-INTEGRATION-REVIEW.json']:add(n)
backup=X/'root-docs-before-target-only-pre'
assert not backup.exists()
backup.mkdir()
for n in docs:shutil.copyfile(X/n,backup/n)
addition='''

## Quantitative random-full-oracle selected restriction and one-target PRE

**PROVED / CITED — manual remote-target lift.** TARGET-ONLY-UD-RO.md identifies the chosen102-byte all-public-parameter restriction of a complete256-bit random oracle, preserving lower output limbs and coherent outside branches. The clean router uses one ordinary remote and one ordinary outside XOR call, without a controlled-unknown-oracle assumption. Honest designated target uses bypass the unknown input via Y; all other source work remains charged in the outside2T polynomial resource ledger. A public adversary with Q_A raw queries yields remote cap Q_A+1, including a final verifier call. This is randomO-only, not a hardness value for fixedSHA.

**PROVED — explicit one-target preimage constant.** SINGLE-TARGET-PRE-RO.md proves kappa_PRE(Q,n)<=min(1,(2Q+1)^2*(2/N-1/N^2)), N=2^n, for an ex-ante target with zero prequeries and marker-independent ghost auxiliaries. A planted correlated marker needs only its common point marginal, not iid coordinates. One Boolean query completes one full-word query. Three first derivations/reviews preserve the distinction between independently derived split proofs and the stronger whole-marker discovery/review. Exact nonbinary miss tables have N-1 outputs; their potentially enormous entropy/storage/gates are charged, not claimed to be a binary-polynomial or efficient implementation.

**PROVED / COMPUTED — calling source and quantitative envelope.** TARGET-ONLY-HIDDEN-BOUND.md audits the actual source program's no-prequery chronology, opaqueX and ghost-side independence, completed-response guard, public/cache/counter values computed from Y and independent auxiliaries, and counted remote replies. ValidPRE selectors have D_H=20229886488608768; activeUD counts sum to A_H=7628143271608320. The conservative randomO hidden component is at most min(1,D_H*kappa_PRE(Q_A+1,128)+12*A_H*(Q_A+1)/2^64). Exact32 rows cover eight q values, prepared/absent caches and Q_A2^32/2^64; all caps are1. Exact adjacent UNCAPPED component-expression crossings are pass99/fail100 at1/2 and pass200/fail201 at1; the capped probability envelope never exceeds1. These are not attacks, work factors or parameter repairs. The stronger historical direct H_final envelope and complete source tables remain unchanged.

**OPEN — original adequacy target.** This closes a finite random-oracle PRE/UD interface and calling-resource obligation. It does not certify128-bit classical strength, category1, a query capacity or a successful minimal parameter repair. Fixed-SHA instantiation is distinct from the requested random-oracle proof, not an added requirement to prove SHA unconditionally. The original resource/adequacy question still needs a sufficiently strong bound under a valid comparison criterion. Cumulative supporting checked declarations remain47, newly checked whole-source/game declarations0, and the full-security statement remains "not established". Manuscript, cryptographic source and old scalars are preserved.
'''
for n in docs:(X/n).write_text((X/n).read_text(encoding='utf8').rstrip()+addition+'\n',encoding='utf8')
for n,h in prior['documents'].items():pins.pop(str(X/n),None);add(backup/n,h)
assert all(sha(Path(n))==h for n,h in pins.items())
out={'status':'REVIEWED_RANDOM_ORACLE_TARGET_ONLY_PRE_QUANTITATIVE_SUCCESSORS_PROMOTED',
 'documents':{n:sha(X/n) for n in docs},'predecessor_documents':prior['documents'],
 'predecessor_backup':'root-docs-before-target-only-pre','artifacts':{n:sha(X/n) for n in artifacts},
 'receipt_pins':{n:sha(X/n) for n in receipt_names},'accepted_evidence_absolute_pins':pins,
 'cumulative_supporting_checked_declarations':47,'new_source_game_checked_declarations':0,
 'source_scalar_manuscript_changes':0,'random_oracle_model_only':True,
 'unknown_target_query_cap':'Q_A+1','old_stronger_direct_bounds_preserved':True,
 'eight_q_two_modes_two_QA_rows':32,'all_conservative_component_caps_one':True,
 'original_level_category_statement':'not established','whole_goal_complete':False}
(X/'TARGET-PRE-PROMOTION.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf8')
print(json.dumps({'status':out['status'],'pins':len(pins),'helpers':47,'security':'not established'}))
