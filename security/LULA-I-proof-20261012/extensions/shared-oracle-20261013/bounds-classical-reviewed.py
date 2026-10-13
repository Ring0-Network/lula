"""Reproduce reviewed classical RO event-union and separate quantum branch arithmetic.

Not a level-1 certificate, generic primitive reduction or full QROM total.

python -I -B bounds.py --out root-checks/bounds
Dependency: mpmath 1.3.0. No signing, cache setup or timing.
"""
from pathlib import Path
import argparse
import hashlib
import importlib.util
import json
import mpmath as mp

assert mp.__version__ == '1.3.0', 'Use the checked numerical dependency'

X = Path(__file__).resolve().parent
source = X.parents[1] / 'numerics/bounds.py'
spec = importlib.util.spec_from_file_location('frozen_component_calculator', source)
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--out', type=Path, default=X / 'root-checks/bounds')
    ap.add_argument('--h', type=int, default=41)
    ap.add_argument('--a', type=int, default=9)
    ap.add_argument('--k', type=int, default=18)
    ap.add_argument('--log2-QH', type=int, default=64)
    ap.add_argument('--log2-Qq', type=int, default=32)
    args = ap.parse_args()
    assert 0 < args.h and 0 < args.a and 1 < args.k and 0 <= args.log2_QH and 0 <= args.log2_Qq
    args.out.mkdir(parents=True, exist_ok=True)
    rows = []
    with mp.workdps(220):
        for lq in (24,30,38,40,41,44,50,64):
            q = 1 << lq
            b = mod.fors_moment(q,args.h,args.a,args.k,dps=220)
            p = mod.fors_moment(q,args.h,args.a,args.k,poisson=True,dps=220)
            bp = mod.fors_positive(q,args.h,args.a,args.k,dps=220)
            pp = mod.fors_positive(q,args.h,args.a,args.k,poisson=True,dps=220)
            assert abs(mod.bits(b)-bp['bits']) < 1e-10
            assert abs(mod.bits(p)-pp['bits']) < 1e-10
            if lq == 40:
                assert abs(mod.bits(b)-mod.bits(p)) < 0.01
            QH = 1 << args.log2_QH
            numerator = QH + 2*q + 3
            joint = min(mp.mpf(1), mp.mpf(numerator) / (1 << 128))
            fors_union = min(mp.mpf(1), (QH+1)*b)
            fixed_source = (args.h,args.a,args.k) == (41,9,18)
            exhaust = q * mp.exp((1 << 32) * mp.log1p(-mp.power(2,-9)))
            beta = min(mp.mpf(1),mp.mpf(2*QH+q+2)/(1 << 128)
                       +mp.mpf(q*QH+q*(q-1)//2+q)/(1 << 256)+exhaust)
            ideal_covered = min(mp.mpf(1),beta+fors_union)
            real_covered = min(mp.mpf(1),joint+beta+fors_union)
            N = 1 << 128
            hidden = min(mp.mpf(1),mp.mpf(QH+3017)/N)
            graph_nonzero = min(mp.mpf(1),mp.mpf(QH+3217)/N)
            canonical = min(mp.mpf(1),mp.mpf(QH+5)/N)
            pair_term = mp.mpf(q*QH+q*(q-1)//2+q)/(N*N)
            linear_numerator = 6*QH+3*q+6243
            linear = mp.mpf(linear_numerator)/N
            classical_total = min(mp.mpf(1),linear+pair_term+exhaust+(QH+1)*b)
            joint_nonzero = min(mp.mpf(1),mp.mpf(QH+2*q+2)/N)
            beta_nonzero = min(mp.mpf(1),mp.mpf(2*QH+q+1)/N+pair_term+exhaust)
            Qq = 1 << args.log2_Qq
            quantum_graph = min(mp.mpf(1),mp.mpf(8*(Qq+3218)**2)/N)
            quantum_canonical = min(mp.mpf(1),mp.mpf(8*(Qq+6)**2)/N)
            rows.append({'log2_q':lq, 'q':str(q), 'QH':str(QH),
                'FORS_status':'COMPUTED_INDEPENDENT_SELECTION_MODEL_ONLY',
                'FORS_binomial_per_raw_candidate':mp.nstr(b,45),
                'FORS_binomial_bits':mod.bits(b),'FORS_poisson_bits':mod.bits(p),
                'positive_binomial_check':bp,'positive_poisson_check':pp,
                'joint_status':'COMPUTED_BOUND_FROM_MANUAL_CLASSICAL_JOINT_LEMMA',
                'joint_numerator_initiated':str(numerator),'joint_denominator':str(1 << 128),
                'joint_probability_bound':mp.nstr(joint,45),'joint_bound_bits':mod.bits(joint),
                'completed_plus_one_pending_numerator':str(QH+2*q+5),
                'conditional_FORS_union_status':'COMPUTED_FRESH_STREAM_SUBTERM_OF_REVIEWED_CLASSICAL_COVERAGE_LEMMA',
                'conditional_FORS_union_probability':mp.nstr(fors_union,45),
                'conditional_FORS_union_bits':mod.bits(fors_union),
                'fixed_source_parameters':fixed_source,
                'FORS_source_bridge_status':('PROVED_MANUAL_REVIEWED_CLASSICAL_IDEAL_COVERAGE_ROUTE'
                    if fixed_source else 'OPEN_SOURCE_LEMMA_NOT_INSTANTIATED_FOR_CHANGED_PARAMETERS'),
                'FORS_source_beta':mp.nstr(beta,45) if fixed_source else None,
                'FORS_exhaustion_term':mp.nstr(exhaust,30) if fixed_source else None,
                'ideal_covered_route_bound':mp.nstr(ideal_covered,45) if fixed_source else None,
                'ideal_covered_route_bound_bits':mod.bits(ideal_covered) if fixed_source else None,
                'real_covered_route_bound':mp.nstr(real_covered,45) if fixed_source else None,
                'real_covered_route_bound_bits':mod.bits(real_covered) if fixed_source else None,
                'seed_accounting':'Separate unconditional joint and bridge losses conservatively charge S=0 twice',
                'typed_graph_collision_bound':mp.nstr(min(mp.mpf(1),mp.mpf(QH+3218)/(1 << 128)),45) if fixed_source else None,
                'typed_graph_collision_status':('PROVED_MANUAL_CLASSICAL_DAG_EVENT_ONLY_NOT_FULL_EUF'
                    if fixed_source else 'OPEN_SOURCE_CALL_COUNT_NOT_INSTANTIATED_FOR_CHANGED_PARAMETERS'),
                'hidden_input_event_bound_nonzero':mp.nstr(hidden,45) if fixed_source else None,
                'hidden_input_event_bound_bits':mod.bits(hidden) if fixed_source else None,
                'graph_target_event_bound_nonzero':mp.nstr(graph_nonzero,45) if fixed_source else None,
                'canonical_type7_event_bound_nonzero':mp.nstr(canonical,45) if fixed_source else None,
                'canonical_type7_event_bound_bits':mod.bits(canonical) if fixed_source else None,
                'classical_RO_linear_numerator':str(linear_numerator) if fixed_source else None,
                'classical_RO_linear_bound_bits':mod.bits(linear) if fixed_source else None,
                'classical_RO_pair_term':mp.nstr(pair_term,45) if fixed_source else None,
                'joint_nonzero_probability':mp.nstr(joint_nonzero,45) if fixed_source else None,
                'joint_nonzero_bits':mod.bits(joint_nonzero) if fixed_source else None,
                'coverage_beta_nonzero_probability':mp.nstr(beta_nonzero,45) if fixed_source else None,
                'coverage_beta_nonzero_bits':mod.bits(beta_nonzero) if fixed_source else None,
                'graph_target_event_bound_bits':mod.bits(graph_nonzero) if fixed_source else None,
                'seed_zero_probability':mp.nstr(mp.mpf(1)/N,45),
                'total_probability':mp.nstr(classical_total,45) if fixed_source else None,
                'total_bits':mod.bits(classical_total) if fixed_source else None,
                'total_status':('COMPUTED_FROM_REVIEWED_MANUAL_CLASSICAL_RO_EVENT_UNION'
                                if fixed_source else 'OPEN_SOURCE_THEOREM_NOT_INSTANTIATED_FOR_CHANGED_PARAMETERS'),
                'classical_total_seed_accounting':'Fixed-nonzero-S component inequalities averaged, then S=0 paid once',
                'classical_level1_status':'NOT_ESTABLISHED_NO_CERTIFIED_CAPACITY',
                'WOTS_generic_primitive_reduction':None,'tree_generic_primitive_embedding':None,
                'Qq':str(Qq),
                'quantum_graph_final_event_bound_nonzero':mp.nstr(quantum_graph,45) if fixed_source else None,
                'quantum_graph_final_event_bound_bits':mod.bits(quantum_graph) if fixed_source else None,
                'quantum_canonical_final_event_bound_nonzero':mp.nstr(quantum_canonical,45) if fixed_source else None,
                'quantum_canonical_final_event_bound_bits':mod.bits(quantum_canonical) if fixed_source else None,
                'quantum_total':None,'quantum_status':'OPEN_NO_QROM_REDUCTION'})
    record={'parameters':{'h':args.h,'a':args.a,'k':args.k,'n':16},'rows':rows,
        'dependency':{'mpmath':mp.__version__},
        'frozen_calculator_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),
        'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'classification':'PROVED reviewed manual classical source-model RO event union; COMPUTED arithmetic; OPEN level1/full QROM/efficient primitive reductions',
        'warning':'Classical total is an upper bound for the specified partial atomic RO experiment, not a security-level certificate. Quantum branches are not a quantum total.'}
    (args.out / 'bounds.json').write_text(json.dumps(record,indent=2)+'\n',encoding='utf8')
    lines=['# Extension component arithmetic','',
      'COMPUTED. Q_H = 2^'+str(args.log2_QH)+'. The joint bound uses initiated signing calls.',
      'Classical total uses the independently reviewed complete event union in CLASSICAL-RO-THEOREM.md. It is not a level1 certificate or a checked Rust refinement. OPEN is not zero.','',
      '| log2 q | FORS binomial bits/candidate | FORS Poisson bits/candidate | joint-distance bound exponent | fresh-stream union exponent | real covered-route exponent | classical RO total exponent |',
      '|---:|---:|---:|---:|---:|---:|---|']
    for r in rows:
        rb='OPEN' if r['real_covered_route_bound_bits'] is None else f"{r['real_covered_route_bound_bits']:.9f}"
        total='OPEN' if r['total_bits'] is None else f"{r['total_bits']:.9f}"
        lines.append(f"| {r['log2_q']} | {r['FORS_binomial_bits']:.9f} | {r['FORS_poisson_bits']:.9f} | {r['joint_bound_bits']:.9f} | {r['conditional_FORS_union_bits']:.9f} | {rb} | {total} |")
    if (args.h,args.a,args.k)==(41,9,18):
        lines.extend(['','## Complete classical event ledger','',
          'COMPUTED from PROVED manual reviewed event bounds. Values are -log2 of capped probability upper bounds, never work-factor estimates. All nonzero-seed terms share one fixed-S HJ marginal; seed-zero exponent128 is added once.','',
          '| log2 q | joint nonzero | beta nonzero | coverage trials | hidden input | graph target | type7 target | seed-zero | RO total |',
          '|---:|---:|---:|---:|---:|---:|---:|---:|---:|'] )
        for r in rows:
            keys=['joint_nonzero_bits','coverage_beta_nonzero_bits','conditional_FORS_union_bits','hidden_input_event_bound_bits','graph_target_event_bound_bits','canonical_type7_event_bound_bits']
            fields=' | '.join(f"{r[k]:.9f}" for k in keys)
            lines.append(f"| {r['log2_q']} | {fields} | 128.000000000 | {r['total_bits']:.9f} |")
        lines.extend(['','## Quantum event branches','',
          'COMPUTED from CITED+PROVED reviewed finite-query event theorems, at Q_q=2^'+str(args.log2_Qq)+'. No complete QROM total is supplied.',
          f"Types0–4 observable final-trace event: exponent {rows[0]['quantum_graph_final_event_bound_bits']:.9f} for fixed nonzero S.",
          f"Type7 observable final-trace event: exponent {rows[0]['quantum_canonical_final_event_bound_bits']:.9f} for fixed nonzero S.",
          'Full QROM and level1/category1 certification: OPEN, not established.'])
    (args.out/'bounds.md').write_text('\n'.join(lines)+'\n',encoding='utf8')
    print(json.dumps({'status':'PASS_REVIEWED_CLASSICAL_RO_TOTAL_ARITHMETIC_FULL_QROM_OPEN','rows':len(rows),'QH_exponent':args.log2_QH,'Qq_exponent':args.log2_Qq}))

if __name__ == '__main__':
    main()
