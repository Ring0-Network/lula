from pathlib import Path
import hashlib,json,difflib
HERE=Path(__file__).resolve().parent;X=HERE.parents[2]
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
p=X/'QUANTUM-UD-POLYNOMIAL-RO.md';raw=p.read_bytes();s=raw.decode('utf-8')
new1='**PROVED — manual finite-random-oracle lemma.** Three separately saved derivations obtain the bound below. Its acceptance is recorded in independently pinned final-subject receipts.'
old1='**PROVED — manual finite-random-oracle lemma; final subject review pending.** Three separately saved derivations obtain the bound below.'
new2='**PROVED — manual source-interface application.**'
old2='**PROVED — manual source-interface application, final subject review pending.**'
assert s.count(new1)==s.count(new2)==1
old=s.replace(new1,old1).replace(new2,old2).encode('utf-8')
assert hashlib.sha256(old).hexdigest()=='55971b61f6fd7cba54fe589c100d61351e67f7373182515593cf2c63d83bb7d5'
assert sha(p)=='5200165e5a66c138cf0e186f60c072699f3e5123a0dfdf869d00734a0c38450f'
assert sha(HERE/'FINAL-SUBJECT-REVIEW.json')=='6e65153080ffe310b1336fe736e75ad565534c16ed6e7d584cb332585565229a'
(HERE/'STATUS-PREDECESSOR-BYTES.md').write_bytes(old)
diff='\n'.join(difflib.unified_diff(old.decode('utf-8').splitlines(),s.splitlines(),fromfile='accepted-mathematical-subject',tofile='status-successor',lineterm=''))+'\n'
(HERE/'STATUS-SUCCESSOR-DIFF.txt').write_text(diff,encoding='utf-8')
out={'verdict':'ACCEPT_STATUS_ONLY_FINAL_UD_POLYNOMIAL_SUCCESSOR',
 'subject':'QUANTUM-UD-POLYNOMIAL-RO.md','subject_sha256':sha(p),
 'prior_subject_sha256':hashlib.sha256(old).hexdigest(),
 'prior_final_receipt_sha256':sha(HERE/'FINAL-SUBJECT-REVIEW.json'),
 'own_pins':{n:sha(HERE/n) for n in ('FINAL-SUBJECT-REVIEW.json','STATUS-PREDECESSOR-BYTES.md','STATUS-SUCCESSOR-DIFF.txt','check_status_successor.py')},
 'checks':{'inverse_exact_two_status_edits_matches_accepted_predecessor_hash':True,
   'full_math_scope_resources_unchanged':True,'stale_pending_status_replaced_by_actual_receipt_acceptance':True,
   'prior_final_receipt_preserved':True,'no_new_math_or_source_category_claim':True},
 'inherited_checks':'All scoped mathematical/caller/resource checks of prior accepted6e651 receipt',
 'new_source_game_checked_declarations':0,'whole_goal_complete':False}
q=HERE/'FINAL-STATUS-SUCCESSOR-REVIEW.json';q.write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8');print('PASS',sha(q));print(diff)
