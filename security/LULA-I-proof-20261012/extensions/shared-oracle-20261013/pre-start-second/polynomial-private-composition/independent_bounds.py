"""Independent high-precision formula arithmetic; no source/signature execution."""
from pathlib import Path
from fractions import Fraction
import hashlib, json, math
import mpmath as mp

OUT=Path(__file__).resolve().parent
X=OUT.parent.parent
assert mp.__version__=='1.3.0'
QEXP=(24,30,38,40,41,44,50,64)
N=1<<128
def mfrac(f): return mp.mpf(f.numerator)/f.denominator
def cap(x): return min(mp.mpf(1),x)
def v_exact(Q):
    d2=4*Q*Q
    return min(Fraction(1),Fraction(d2,N-d2)) if d2<N else Fraction(1)
def coverage_moment(q):
    p=mp.mpf(1)/(1<<41); miss=mp.mpf(511)/512
    return mp.fsum([(-1)**j*math.comb(17,j)*mp.exp(q*mp.log1p(-p*(1-miss**j))) for j in range(18)])/512
def positive_check(q,pf):
    prob=mp.mpf(1)/(1<<41); mu=q*prob; miss=mp.mpf(511)/512
    if mu>4096:
        bad=mp.exp(-mu/8)
        deficiency=bad+17*mp.exp(-mu/(2*512))
        low=mp.mpf(1)/512*(1-bad)*(1-mp.exp(mu*mp.log(miss)/2))**17
        high=mp.mpf(1)/512
        assert low-mp.mpf('1e-240')<=pf<=high+mp.mpf('1e-240')
        return {'method':'analytic Chernoff saturation interval','lower':mp.nstr(low,220),'upper':mp.nstr(high,220),'fractional_deficit_upper':mp.nstr(deficiency,80)}
    stop=min(q,max(800,int(mu+32*mp.sqrt(mu+1)+700)))
    mass=mp.exp(q*mp.log1p(-prob)); value=mp.mpf(0)
    for r in range(1,stop+1):
        mass*=mp.mpf(q-r+1)*prob/(r*(1-prob))
        value+=mass*(-mp.expm1(r*mp.log(miss)))**17
    low=value/512
    L=stop+1
    tail=mp.mpf(0) if stop==q else mp.exp(-mu+L*(1+mp.log(mu/L)))
    high=low+tail/512
    rel=abs(pf-low)/pf
    # Cancellation-stability check; not a machine interval implementation.
    assert rel<mp.mpf('1e-180')
    return {'method':'positive binomial recurrence with analytic omitted-tail cap','stop':stop,'lower':mp.nstr(low,220),'upper':mp.nstr(high,220),'omitted_tail_upper':mp.nstr(tail,80),'relative_direct_positive_difference':mp.nstr(rel,40)}
def evaluate(q,Q):
    n=mp.mpf(N); M=n*n-n
    pf=coverage_moment(q)
    vk=mfrac(v_exact(Q))
    nominees=2*q+2
    stopped=cap((2*mp.mpf(Q)+mp.sqrt(min(N,nominees)))**2/n)
    ap=cap(vk+stopped)
    row=cap(q*(mp.sqrt(mp.mpf(Q+q+1)/M)+mp.mpf(Q+q+1)/(2*M)))
    ac=cap(row+8*(mp.mpf(Q)+2)**2*(pf+1/n+mp.mpf(q)/(n*n)))
    c=cap((2*mp.mpf(Q)+mp.sqrt(q))**2/n+(2*(mp.mpf(Q)+2)/mp.sqrt(n)+mp.sqrt(ac))**2)
    h=cap((2*mp.mpf(Q)+mp.sqrt(3017))**2/n)
    g=cap(8*(mp.mpf(Q)+3218)**2/n)
    d7=cap(8*(mp.mpf(Q)+6)**2/n)
    private_sum=vk+ap
    uncapped=1/n+private_sum+c+h+g+d7
    total=cap(uncapped)
    kept=1/n+(1-1/n)*cap(private_sum+c+h+g+d7)
    exhaust=q*mp.exp((1<<32)*mp.log1p(-mp.mpf(1)/512))
    beta=cap(mp.mpf(2*Q+q+1)/n+mp.mpf(q*Q+q*(q-1)//2+q)/(n*n)+exhaust)
    return {'pF_exact_binomial_formula':pf,'seed_zero':1/n,'vK':vk,'P_stopped_alias':stopped,'aP':ap,
            'private_sum':private_sum,'D_ROW':row,'A_C':ac,'c_COVER':c,'h_hidden':h,
            'g_graph':g,'d7':d7,'uncapped_complete_sum':uncapped,'complete_bound':total,
            'seed_weight_kept_complete_bound':kept,'classical_beta_not_used_in_quantum_sum':beta,
            'source_exhaustion_not_separately_added_to_quantum_sum':exhaust}

rows=[];pf_checks=[];stability=[]
for qe in QEXP:
    q=1<<qe
    with mp.workdps(260):
        pf=coverage_moment(q)
        pf_checks.append({'q_exponent':qe,'pF':mp.nstr(pf,220),'positive_check':positive_check(q,pf)})
    for ae in (32,64):
        Q=1<<ae
        with mp.workdps(260):
            values=evaluate(q,Q)
            serialized={k:mp.nstr(v,220) for k,v in values.items()}
            exponents={k:mp.nstr(-mp.log(v,2),80) if v>0 else None for k,v in values.items() if k not in ('source_exhaustion_not_separately_added_to_quantum_sum',)}
            total_float=float(values['complete_bound'])
            display_exponent=float(-mp.log(values['complete_bound'],2))
        with mp.workdps(340):
            higher=evaluate(q,Q)
            errors={k:abs(higher[k]-values[k])/max(abs(higher[k]),mp.mpf('1e-200')) for k in higher}
            # Exhaustion is a remote analytic exponent; absolute normalization would
            # discard its relative check, so verify that positive tiny value too.
            errors['exhaustion_relative']=abs(higher['source_exhaustion_not_separately_added_to_quantum_sum']-values['source_exhaustion_not_separately_added_to_quantum_sum'])/higher['source_exhaustion_not_separately_added_to_quantum_sum']
            worst=max(errors.values())
            assert worst<mp.mpf('1e-170'),(qe,ae,mp.nstr(worst,20))
            stability.append({'q_exponent':qe,'QA_exponent':ae,'relative_or_normalized_error_upper':mp.nstr(worst,45)})
        rows.append({'q_exponent':qe,'q':str(q),'QA_exponent':ae,'QA':str(Q),
                     'vK_exact_rational':str(v_exact(Q)),'nominee_count':str(2*q+2),
                     'values':serialized,'probability_bound_exponents_not_work_factors':exponents,
                     'display_complete_bound':total_float,'display_bound_exponent':display_exponent})

sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
subjects=('SOURCE-PRIVATE-K-POLYNOMIAL-QROM.md','SOURCE-PRIVATE-P-POLYNOMIAL-QROM.md','QUANTUM-RO-THEOREM.md','QUANTUM-COVERAGE-THEOREM.md','CLASSICAL-RO-THEOREM.md')
record={'status':'COMPUTED_INDEPENDENT_NEW_COMPLETE_QROM_FORMULA_BEFORE_NEW_ROOT_COMPARISON',
        'model':'partial atomic finite-query source RO; fixed nonzero-S components then one seed-zero branch',
        'formula':'min(1,1/N+vK+aP+c+h+g+d7)',
        'precision_decimal_digits':260,'stability_precision_decimal_digits':340,
        'serialized_significant_digits':220,'mpmath':mp.__version__,'script_sha256':sha(Path(__file__)),
        'own_first_sha256':sha(OUT/'INDEPENDENT-FIRST.md'),'subject_pins':{n:sha(X/n) for n in subjects},
        'q_exponents':list(QEXP),'QA_exponents':[32,64],'row_count':16,
        'cache_modes_have_same_formula_not_same_resource_cost':True,'rows':rows,
        'exact_binomial_positive_controls':pf_checks,'stability_checks':stability,
        'classical_beta_included_for_provenance_not_quantum_application':True,
        'old_conservative_event_specific_results_read_for_comparison_yet':False,
        'new_root_combined_theorem_calculator_results_read':False,
        'new_source_game_declarations':0,'whole_goal_complete':False,
        'category':'not established','source_or_attack_runs':0}
(OUT/'INDEPENDENT-NUMERICS.json').write_text(json.dumps(record,indent=2)+'\n',encoding='utf-8')
table=['# Independent complete QROM formula values','',
       'COMPUTED with260 decimal digits and340-digit stability checks. Values are probability upper bounds; their exponents are not work factors or categories. All two cache modes share these16 values; local work differs.','',
       '| log2 q | log2 Q_A | complete probability upper bound | minus log2 bound |','|---:|---:|---:|---:|']
for r in rows:table.append(f"| {r['q_exponent']} | {r['QA_exponent']} | {r['display_complete_bound']:.15g} | {r['display_bound_exponent']:.12f} |")
(OUT/'INDEPENDENT-NUMERICS.md').write_text('\n'.join(table)+'\n',encoding='utf-8')
print(json.dumps({'status':record['status'],'rows':16,'precision':260,'QA32':[(r['q_exponent'],r['display_complete_bound']) for r in rows if r['QA_exponent']==32],'QA64_all_cap1':all(r['values']['complete_bound']=='1.0' for r in rows if r['QA_exponent']==64)}))
