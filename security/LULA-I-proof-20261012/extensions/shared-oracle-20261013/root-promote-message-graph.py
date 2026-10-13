"""Promote reviewed symbolic successors, preserving the prior accepted cut."""
from pathlib import Path
import hashlib,json,shutil
X=Path(__file__).resolve().parent
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
read=lambda p:json.loads(p.read_text(encoding='utf8'))
docs=['PROOF.md','OPEN.md','TERM-TABLE.md','REQUIREMENT-MAP.md','HANDOFF.md','SECURITY-CRITERION.md']
prior=read(X/'PRIMITIVE-SUCCESSORS-PROMOTION.json')
current=read(X/'selected-promotion-review/PRIMITIVE-INTEGRATION-REVIEW.json')
assert all(current['checks'].values())
assert current['cumulative_supporting_checked_declarations']==44
assert all(sha(X/n)==h for n,h in prior['documents'].items())
selected=read(X/'selected-promotion-review/message-hash-identification/FINAL-ORDINARY-SUBJECT-REVIEW.json')
field=read(X/'outside-field-check/message-hash-identification/FINAL-ORDINARY-SUBJECT-REVIEW.json')
graph=read(X/'graph-collection-second/FINAL-SUBJECT-REVIEW.json')
composition=read(X/'selected-promotion-review/FINAL-COMPOSITION-SUBJECT-REVIEW.json')
assert all(selected['checks'].values()) and all(field['checks'].values())
assert all(composition['checks'].values())
assert composition['whole_goal_complete'] is False
assert composition['subject_sha256']==sha(X/'FIXED-H-COMPOSITION.md')
pins=dict(prior['accepted_evidence_absolute_pins'])
def add(n,h=None):
    p=Path(n)
    if not p.is_absolute():p=X/p
    actual=sha(p)
    if h is not None:assert actual==h,str(p)
    pins[str(p)]=actual
for n,h in selected['subject_pins'].items():add(n,h)
for n,h in selected['own_pins'].items():add('selected-promotion-review/message-hash-identification/'+n,h)
for n,h in selected['peer_pins'].items():add(n,h)
for n,h in field['own_pins'].items():add('outside-field-check/message-hash-identification/'+n,h)
add(graph['graph_subject'],graph['graph_subject_sha256'])
add(graph['composition_subject'],graph['composition_subject_sha256'])
add('graph-collection-second/INDEPENDENT-FIRST.md',graph['independent_first_sha256'])
add('graph-collection-second/PEER-REVIEW.md',graph['peer_review_sha256'])
for version in selected['primary_versions']:
    add(version['pdf'],version['pdf_sha256']);add(version['text'],version['text_sha256'])
projection=read(X/'root-message-hash/PROJECTION-CHECK.json')
assert projection['exit_code']==0 and projection['checked_declarations']==3
assert all(set(a)<={'propext','Classical.choice','Quot.sound'} for a in projection['axiom_sets'])
add('root-message-hash/DigestProjection.lean',projection['source_sha256'])
add('root-message-hash/DigestProjection.log',projection['log_sha256'])
new_artifacts=['MESSAGE-HASH-PRIMITIVE-COMPONENT.md','MESSAGE-HASH-ORDINARY-LIFT.md','FIXED-H-GRAPH-COMPONENT.md','FIXED-H-COMPOSITION.md']
receipts=['selected-promotion-review/message-hash-identification/FINAL-ORDINARY-SUBJECT-REVIEW.json',
 'outside-field-check/message-hash-identification/FINAL-ORDINARY-SUBJECT-REVIEW.json',
 'selected-promotion-review/message-hash-identification/DIRECT-COMPONENT-SUBJECT-REVIEW.json',
 'outside-field-check/message-hash-identification/FINAL-COMPONENT-REVIEW.json',
 'graph-collection-second/FINAL-SUBJECT-REVIEW.json',
 'selected-promotion-review/FINAL-COMPOSITION-SUBJECT-REVIEW.json',
 'selected-promotion-review/PRIMITIVE-INTEGRATION-REVIEW.json',
 'root-message-hash/PROJECTION-CHECK.json',
 'root-message-hash/SUCCESSOR-COUNTS.json','root-message-hash/check_successors.py']
for n in new_artifacts+receipts:add(n)
backup=X/'root-docs-before-message-graph'
assert not backup.exists(),'Never replace an accepted predecessor.'
backup.mkdir()
for n in docs:shutil.copyfile(X/n,backup/n)
addition='''

## Fixed-h message, graph and symbolic-composition successor

**PROVED / ASSUMED — ordinary message-hash lifting.** MESSAGE-HASH-ORDINARY-LIFT.md supplies a legal loss-aware ordinary ITSR adapter for the exact total rank-encoded H_free family, retaining completed source responses, memoized nonces, all literal full-h words and adaptive quantum public computation. Dense guessing uses at most q distinct target queries and loss (2^32)^min(17,q). Sparse ordinal selection uses at most min(17,q) targets and its separate loss/resources. At every requested q the dense loss is 2^544; this is NOT a security exponent. The optional eighteenth public zero coordinate introduces no eighteenth source secret, target witness or counter guess. The tagged297-bit label has only41 route bits, not297 uniform bits. Ordinary family hardness is ASSUMED and unevaluated; direct RC-CTAC-SR remains an explicit alternative property, not a numeric certificate.

**PROVED / COMPUTED / ASSUMED — fixed-h graph collection.** FIXED-H-GRAPH-COMPONENT.md legally targets differing-payload/equal-output public graph witnesses using NEW within-class SM-TCR programs. Their payload/selector pairs in bits are (128,55),(256,55),(2048,21),(2176,41),(4096,42), independently recomputed in root-message-hash/SUCCESSOR-COUNTS.json. These smaller coefficients cannot be applied to OLD common56-bit particular successes. Challenged-tweak predecessor cones query only other tweaks and lengths; the same public h and all source/challenger resources remain explicit. No collection generic-bound conjecture or RO hardness number is imported.

**PROVED / OPEN — symbolic composition.** FIXED-H-COMPOSITION.md combines exact ordinary private hops, the pointwise source witness cover, the legal coverage alternatives, new graph programs and canonical type7 programs. Its inequality keeps the hidden predecessor probability epsilon_H explicit and pays source seed-zero once. Full fixed-h family hardness and epsilon_H remain unevaluated/open. PRE for uniform starts is a separately reviewed candidate; interior-prefix UD/PRE work is pending and is not relied upon by this accepted cut. The historical RO/QROM model bounds and numerics retain their original scope and values. A numeric full-security claim remains "not established" at all eight requested signing caps.

**PROVED — scoped kernel support.** Three DigestProjection.lean declarations were checked under pinned Lean4.28 and independently reexecuted; their axiom sets are subsets of {propext,Quot.sound}. They prove same-word prefix preservation and the two bit slices under a zero lower limb, not preservation of the whole two-stage H_msg digest, SHA hardness or a source-security reduction. Current cumulative supporting declarations are47; newly checked whole-source/game declarations are0.
'''
for n in docs:
    text=(X/n).read_text(encoding='utf8').rstrip()
    (X/n).write_text(text+addition+'\n',encoding='utf8')
for n,h in prior['documents'].items():
    pins.pop(str(X/n),None)
    add(backup/n,h)
assert all(sha(Path(p))==h for p,h in pins.items())
out={'status':'REVIEWED_MESSAGE_GRAPH_FIXED_H_SYMBOLIC_SUCCESSORS_PROMOTED',
     'documents':{n:sha(X/n) for n in docs},
     'predecessor_documents':prior['documents'],'predecessor_backup':'root-docs-before-message-graph',
     'artifacts':{n:sha(X/n) for n in new_artifacts},
     'receipt_pins':{n:sha(X/n) for n in receipts},
     'accepted_evidence_absolute_pins':pins,
     'cumulative_supporting_checked_declarations':47,
     'new_source_game_checked_declarations':0,'source_scalar_manuscript_changes':0,
     'epsilon_H':'OPEN; no interior transfer relied upon',
     'ordinary_family_hardness':'ASSUMED_WITHOUT_NUMERICAL_CERTIFICATE',
     'whole_goal_complete':False,'original_level_category_statement':'not established'}
(X/'MESSAGE-GRAPH-PROMOTION.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf8')
print(json.dumps({'status':out['status'],'pins':len(pins),'helpers':47,'security':'not established'}))
