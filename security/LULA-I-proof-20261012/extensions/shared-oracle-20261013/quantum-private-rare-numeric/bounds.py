"""New unpromoted rare-private envelope, independent saved HJ components."""
from pathlib import Path
from fractions import Fraction
import hashlib
import json
import mpmath as mp

mp.mp.dps=240
HERE=Path(__file__).resolve().parent
OWN=HERE.parent/'quantum-composition-numeric'/'OWN-BOUNDS.json'
EXPECTED_OWN='2a6320bd6689ada00bf25265aa08dde009700c489930736521f26c8d4762026a'
N=2**128
def fmt(x):return mp.nstr(x,110)
def cap(x):return min(mp.mpf(1),x)
def bits(x):return -mp.log(cap(x),2)

def main():
    assert hashlib.sha256(OWN.read_bytes()).hexdigest()==EXPECTED_OWN
    old=json.loads(OWN.read_text(encoding='utf-8'))
    rows=[]
    for r in old['rows']:
        q=2**r['q_exponent'];Q=2**r['Qq_exponent']
        exact_b=Fraction(2*q+2,N)
        b=cap(mp.mpf(exact_b.numerator)/exact_b.denominator)
        e=mp.mpf(r['HJ_union_probability'])
        a=2*mp.mpf(Q)/mp.sqrt(N)
        inside=cap(b+e)
        fixed_raw=(a+mp.sqrt(inside))**2
        fixed=cap(fixed_raw)
        seed=mp.mpf(1)/N
        total=cap(seed+fixed)
        expanded=a*a+inside+2*a*mp.sqrt(inside)
        assert abs(fixed_raw-expanded)<mp.mpf('1e-200')
        # Separately arranged average over the actual zero-seed branch.
        weighted=seed+(1-seed)*fixed
        assert total+mp.mpf('1e-200')>=weighted
        separate=cap(seed+(a+mp.sqrt(b))**2+(a+mp.sqrt(e))**2)
        assert total<=separate+mp.mpf('1e-200')
        conservative=mp.mpf(r['candidate_reference_probability'])
        assert total<=conservative+mp.mpf('1e-95')
        # Reconstruct e from separately stored scoped C/H/G/D7 inputs.
        comps=[mp.mpf(r[k]) for k in ['C_probability','H_probability_capped',
                                     'G_probability_capped','D7_probability_capped']]
        assert abs(e-cap(mp.fsum(comps)))<mp.mpf('1e-95')
        rows.append(dict(q_exponent=r['q_exponent'],Qq_exponent=r['Qq_exponent'],
          source_C_probability=r['C_probability'],source_H_probability=r['H_probability_capped'],
          source_G_probability=r['G_probability_capped'],source_D7_probability=r['D7_probability_capped'],
          source_HJ_union_probability=fmt(e),honest_alias_probability_exact=str(exact_b),
          honest_alias_probability_capped=fmt(b),stopped_vector_gap=fmt(a),
          stopped_IDEAL_union_envelope=fmt(inside),fixed_nonzero_candidate_uncapped=fmt(fixed_raw),
          fixed_nonzero_candidate=fmt(fixed),seed_probability=fmt(seed),
          candidate_rare_quantum_total=fmt(total),candidate_rare_quantum_total_bits=fmt(bits(total)),
          independently_expanded_fixed_nonzero=fmt(expanded),
          weighted_seed_candidate_probability=fmt(weighted),
          two_projector_candidate_probability=fmt(separate),
          accepted_conservative_reference_probability=fmt(conservative),
          accepted_conservative_reference_bits=r['candidate_reference_bits'],
          promoted_rare_total=None,
          status='CANDIDATE_SINGLE_PROJECTOR_RARE_PRIVATE_BOUND_PENDING_PEER_REVIEW'))
    out=dict(status='PASS_ALL16_INDEPENDENT_CANDIDATE_RARE_ENVELOPES',
      independent_HJ_inputs_sha256=EXPECTED_OWN,precision_decimal_digits=mp.mp.dps,
      query_budget_semantics='Qq adversarial complete-RO coherent calls; q initiated atomic services',
      no_master_or_old_data_edits=True,category_status='NOT_ESTABLISHED',
      numeric_qualification='240-digit evaluation, exact b/seed rational components, independent expanded square and seed averaging; not a formal directed-rounded certificate',
      rows=rows,promoted_rare_total=None)
    (HERE/'CANDIDATE-BOUNDS.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
    print('PASS:16 independent rare-private candidate totals; HJ components, exact alias/seed, expanded square, seed average, separate-projector and conservative comparisons. No promotion.')

if __name__=='__main__':main()
