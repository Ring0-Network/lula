"""Compare new independent data only after first+dataset were saved."""
from pathlib import Path
import hashlib,json
import mpmath as mp
E=Path(__file__).resolve().parent; X=E.parent.parent
read=lambda p:json.loads(p.read_text(encoding='utf-8'))
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
own=read(E/'INDEPENDENT-NUMERICS.json')
root=read(X/'root-polynomial-private-composition/RESULTS.json')
assert len(own['rows'])==len(root['rows'])==16
assert sha(X/'root-polynomial-private-composition/bounds.py')==root['script_sha256']
for n,h in root['input_pins'].items():assert sha(X/n)==h,n
oldpaths={32:X/'root-checks/bounds-QH64/bounds.json',64:X/'root-checks/bounds-QH128/bounds.json'}
evpaths={32:X/'root-checks/refined-Qq32/bounds.json',64:X/'root-checks/refined-Qq64/bounds.json'}
old={e:read(p) for e,p in oldpaths.items()}; ev={e:read(p) for e,p in evpaths.items()}
qc=read(X/'quantum-composition-numeric/ROOT-CROSSCHECK.json')
assert all(sha(p)==qc['root_output_sha256'][p.parent.name] for p in oldpaths.values())
for e,data in ev.items():
    assert data['base_output_sha256']==sha(oldpaths[e])
    assert data['base_script_sha256']==sha(X/'bounds.py')
    assert data['conservative_theorem_sha256']==sha(X/'QUANTUM-RO-THEOREM.md')
    assert data['refined_theorem_sha256']==sha(X/'QUANTUM-EVENT-SPECIFIC-THEOREM.md')
    assert data['script_sha256']==sha(X/'bounds-event-specific.py')
checks=[]; numeric_count=0
with mp.workdps(260):
    N=mp.mpf(1<<128); cap=lambda x:min(mp.mpf(1),x)
    def close(a,b,tol):
        global numeric_count
        a,b=mp.mpf(a),mp.mpf(b)
        numeric_count+=1
        error=abs(a-b)/max(abs(a),abs(b),mp.mpf('1e-250'))
        assert error<mp.mpf(tol),(mp.nstr(a,15),mp.nstr(b,15),mp.nstr(error,20))
        return mp.nstr(error,30)
    for r in own['rows']:
        qe,ae=r['q_exponent'],r['QA_exponent']; q=1<<qe; Q=1<<ae
        rr=next(t for t in root['rows'] if (t['log2_q'],t['log2_Q'])==(qe,ae))
        pp=rr['probabilities']; vals={k:mp.mpf(v) for k,v in r['values'].items()}
        mapping={'pF':'pF_exact_binomial_formula','vK':'vK','aliasP':'P_stopped_alias','aP':'aP',
                 'c':'c_COVER','h':'h_hidden','g':'g_graph','d7':'d7','poly_total':'complete_bound'}
        errs=[close(pp[k],vals[v],'1e-85') for k,v in mapping.items()]
        ideal=cap(vals['c_COVER']+vals['h_hidden']+vals['g_graph']+vals['d7'])
        errs.append(close(pp['ideal_union'],ideal,'1e-85'))
        # Root caps the public union before the outside cap; this equals the
        # own ungrouped outside cap because every summand is nonnegative.
        errs.append(close(cap(1/N+vals['vK']+vals['aP']+ideal),vals['complete_bound'],'1e-210'))
        oldprivate=cap(2*mp.mpf(Q)/mp.sqrt(N)+mp.mpf(2*q+2)/N)
        conservative=cap(1/N+oldprivate+vals['c_COVER']+vals['h_hidden']+vals['g_graph']+vals['d7'])
        event=cap(1/N+(2*mp.mpf(Q)/mp.sqrt(N)+mp.sqrt(cap(cap(mp.mpf(2*q+2)/N)+ideal)))**2)
        best=min(vals['complete_bound'],conservative,event)
        errs += [close(pp['old_conservative'],conservative,'1e-85'),close(pp['old_event'],event,'1e-85'),close(pp['best_total'],best,'1e-85')]
        orow=next(t for t in old[ae]['rows'] if t['log2_q']==qe)
        erow=next(t for t in ev[ae]['rows'] if t['log2_q']==qe)
        assert int(orow['Qq'])==int(erow['Qq'])==Q
        errs += [close(orow['quantum_total'],conservative,'1e-42'),close(erow['event_specific_total'],event,'1e-42')]
        errs.append(close(orow['FORS_binomial_per_raw_candidate'],vals['pF_exact_binomial_formula'],'1e-42'))
        for field,key in [('quantum_COVER_final_event_bound_nonzero','c_COVER'),('quantum_hidden_final_event_bound_nonzero','h_hidden'),('quantum_graph_final_event_bound_nonzero','g_graph'),('quantum_canonical_final_event_bound_nonzero','d7')]:
            errs.append(close(orow[field],vals[key],'1e-42'))
        win=vals['complete_bound']<min(conservative,event)
        assert win==rr['new_wins_minimum']
        checks.append({'q_exponent':qe,'QA_exponent':ae,'new':mp.nstr(vals['complete_bound'],90),
                       'old_conservative':mp.nstr(conservative,90),'old_event_specific':mp.nstr(event,90),
                       'retained_minimum':mp.nstr(best,90),'new_strictly_stronger':win,
                       'worst_relative_comparison_error':mp.nstr(max(mp.mpf(t) for t in errs),30)})
assert sum(r['new_strictly_stronger'] for r in checks)==6
p_review=read(X/'outside-field-check/private-p-polynomial/FINAL-SUBJECT-REVIEW.json')
assert p_review['subject_sha256']==sha(X/'SOURCE-PRIVATE-P-POLYNOMIAL-QROM.md')
assert all(x=='PASS' or x is True for x in p_review['checks'].values())
assert not p_review['whole_goal_complete']
for obj in p_review['pins'].values():assert sha(Path(obj['path']))==obj['sha256']
out={'status':'PASS_ALL16_NEW_ROOT_AND_PRESERVED_OLD_CONSERVATIVE_EVENT_SPECIFIC_ROWS',
 'independent_first_sha256':sha(E/'INDEPENDENT-FIRST.md'),'independent_dataset_sha256':sha(E/'INDEPENDENT-NUMERICS.json'),
 'root_final_subject_sha256':sha(X/'QUANTUM-POLYNOMIAL-PRIVATE-COMPOSITION.md'),
 'root_new_dataset_sha256':sha(X/'root-polynomial-private-composition/RESULTS.json'),
 'root_new_calculator_sha256':sha(X/'root-polynomial-private-composition/bounds.py'),
 'private_P_final_review_sha256':sha(X/'outside-field-check/private-p-polynomial/FINAL-SUBJECT-REVIEW.json'),
 'old_preserved_dataset_pins':{str(p.relative_to(X)):sha(p) for p in (*oldpaths.values(),*evpaths.values())},
 'comparison_script_sha256':sha(Path(__file__)),'mpmath_dps':260,'new_tolerance':'1e-85 relative','old_tolerance':'1e-42 relative',
 'numeric_comparisons':numeric_count,'rows':checks,'strict_improvement_rows':6,
 'private_P_receipt_exact_subject_and_allpins_verified':True,
 'public_union_cap_algebra_equivalence_verified':True,'source_or_old_scalar_edits':0,
 'new_source_game_declarations':0,'whole_goal_complete':False,'category':'not established'}
(E/'AFTER-FIRST-COMPARISON.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'status':out['status'],'numeric_comparisons':numeric_count,'strict_improvement_rows':6,
                  'private_P_review_sha256':out['private_P_final_review_sha256']}))
