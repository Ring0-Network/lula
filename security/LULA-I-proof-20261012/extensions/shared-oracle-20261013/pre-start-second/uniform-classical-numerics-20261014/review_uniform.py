"""Final peer subject and exact certificate crosscheck; own outputs only."""
from pathlib import Path
from fractions import Fraction as F
from math import comb,factorial
import hashlib,importlib.util,json,subprocess,sys
import mpmath as mp
E=Path(__file__).resolve().parent;X=E.parent.parent
spec=importlib.util.spec_from_file_location('own_uniform_evaluator',E/'evaluate.py');own=importlib.util.module_from_spec(spec);spec.loader.exec_module(own)
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
THEOREM=X/'PARAMETER-UNIFORM-CLASSICAL-THEOREM.md'
assert sha(THEOREM)=='e5fc68bc269ca98672caa99ec70d5695d3d578095a62ebbfc0f99f9d8fbc394b'
root=X/'root-parameter-uniform-classical';script=root/'uniform_bounds.py'
def read(p):return json.loads(p.read_text(encoding='utf8'))
def fraction(rec):return F(int(rec['numerator']),int(rec['denominator']))
def independent_touchard(q,p):
    # Explicit surjection inclusion-exclusion, independent of root's recurrence.
    r=p['r'];mu=F(q,1<<sum(p['heights']));t=1<<p['a'];moment=F(0)
    for j in range(1,r+1):
        stir=F(sum((-1)**(j-v)*comb(j,v)*v**r for v in range(j+1)),factorial(j))
        assert stir.denominator==1 and stir>=0
        moment+=stir*mu**j
    return min(F(1,t),moment/t**(r+1))
comparisons=[];own_rows=[];runs=[]
for stem in ['BASELINE','HEIGHT63']:
    src=root/f'{stem}-CERTIFICATES.json';data=read(src);p=data['parameters']
    ownp=dict(label=stem.lower()+'_separate_exact_crosscheck',a=p['a'],k=p['r']+1,
        layers=[dict(h=h,ell=l,S=s,cached=i==len(p['heights'])-1) for i,(h,l,s) in enumerate(zip(p['heights'],p['ell'],p['S']))])
    g=own.guard(ownp)
    assert data['theorem_sha256']==sha(THEOREM) and data['script_sha256']==sha(script)
    param=E/f'{stem}-ROOT-PARAMETERS.json';param.write_text(json.dumps(p,indent=2)+'\n',encoding='utf8')
    target=E/f'{stem}-ROOT-RERUN.json';argv=[sys.executable,'-I','-B',str(script),'--params',str(param),'--out',str(target)]
    run=subprocess.run(argv,capture_output=True,text=True);assert run.returncode==0,run.stderr
    assert read(target)==data
    runs.append(dict(subject=stem,argv=argv,exit_code=run.returncode,stdout=run.stdout,result_sha256=sha(target),original_sha256=sha(src),objects_identical=True))
    pfs={qe:own.exact_binomial(1<<qe,g) for qe in own.GRID}
    assert len(data['rows'])==24
    for row in data['rows']:
        qe=row['log2_q'];Qe=row['log2_Q'];q=1<<qe;Q=1<<Qe
        assert int(row['q'])==q and int(row['Q'])==Q
        pfupper=independent_touchard(q,p)
        assert fraction(row['pF_positive_upper'])==pfupper
        pfiv,lo,hi,display,pfpoint=pfs[qe]
        assert hi<=pfupper
        exponent=min(1<<(32-p['a']),2048)
        terms=dict(public_slots=F(3*Q,own.N),honest_inner=F(2*q,own.N),terminal_seed_constant=F(g['C_p'],own.N),
                   full256_bridge=F(q*Q+comb(q,2)+q,own.N**2),finite_counter_upper=F(q,1<<exponent),coverage_upper=(Q+1)*pfupper)
        assert set(terms)==set(row['terms']) and all(fraction(row['terms'][k])==v for k,v in terms.items())
        U=sum(terms.values(),F(0));assert fraction(row['uncapped_upper'])==U and fraction(row['capped_upper'])==min(F(1),U)
        assert row['sufficient_at_success_half']==(U<=F(1,2))
        assert (row['H'],row['G'],row['C'],row['signature_bytes'])==(g['H_fin'],g['G_fin'],g['C_p'],g['signature_bytes'])
        assert row['cache_payload_bytes']==36*(1<<p['heights'][-1])-16
        exact=own.one_row(ownp,g,qe,Qe,pfs[qe]);own_rows.append(exact)
        exacthi=own.frac_tuple(exact['uncapped_interval_dyadic'][1])
        exactlo=own.frac_tuple(exact['uncapped_interval_dyadic'][0])
        # At saturated pF=1/t an outward rounded total can straddle the
        # exact rational upper by a rounding unit. Per-term bounds above
        # prove the comparison; do not assert the rounded upper is smaller.
        assert exactlo<=U
        assert exacthi<=U+max(F(1),U)*F(1,1<<1000)
        comparisons.append(dict(shape=stem,q_exponent=qe,Q_exponent=Qe,root_exact_fraction_upper_recomputed=True,
                                own_exact_binomial_interval_below_root_certificate=True,
                                whole_total_outward_rounding_straddles_rational_upper=exacthi>U,
                                sufficient_half=row['sufficient_at_success_half'],own_exact_half=exacthi<=F(1,2)))
    if stem=='HEIGHT63':
        assert (g['h'],g['C_p'],g['signature_bytes'])==(63,6281,6344)
        assert all(c['sufficient_half'] and c['own_exact_half'] for c in comparisons if c['shape']==stem and c['Q_exponent']==125)
    assert all(F(*map(int,r['capped_interval_rational'][0]))==1 for r in own_rows if r['parameter_label']==ownp['label'] and r['Q_exponent']==128)
result=dict(status='ACCEPT_EXACT_ROOT_CERTIFICATES_WITH_OWN_EXACT_BINOMIAL_CROSSCHECK',subject_sha256=sha(THEOREM),root_script_sha256=sha(script),own_first_sha256=sha(E/'INDEPENDENT-FIRST.md'),own_original_numeric_data_sha256=sha(E/'OWN-UNIFORM-NUMERICS.json'),root_reruns=runs,comparisons=comparisons,own_exact_rows=own_rows,scope='Touchard gives a rational upper certificate for finite Binomial pF, not a Poisson substitution; all8 HEIGHT63 Q125 half-success certificates pass, but Q128 caps1 and no category/repair/minimality claim follows',new_source_game_declarations=0,new_signatures_benchmarks_or_attacks=0,QROM_retuning=False,whole_goal_complete=False)
(E/'ROOT-CERTIFICATE-REVIEW.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf8')
print(json.dumps(dict(status=result['status'],checked_root_rows=len(comparisons),new_own_exact_rows=len(own_rows),height63_half125_passes=8,sha256=sha(E/'ROOT-CERTIFICATE-REVIEW.json')),indent=2))
