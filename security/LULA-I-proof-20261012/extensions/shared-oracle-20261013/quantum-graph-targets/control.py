"""Exact finite coherent-oracle and distribution controls, not a quantum signer run.

Run python -I -B control.py. Standard library only. The basis checks prove the
function-oracle action on arbitrary superpositions by linearity; no measurement
or query-register collapse is part of the simulated circuit.
"""
from collections import Counter
from fractions import Fraction as F
import hashlib
import itertools
import json
from pathlib import Path

HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[4]
ELIGIBLE=(False,True,True,False)
LAMBDA=F(1,4)  # two target-prefix bits in the tiny3-bit function model


def transform(y,delta,pivot):
    # CNOT from pivot to every other1-coordinate of delta; self inverse.
    return y ^ (delta ^ (1<<pivot)) if (y>>pivot)&1 else y


def swap_bit(y,a,pivot):
    if ((y>>pivot)&1)!=a:
        y ^= 1<<pivot
        a ^= 1
    return y,a


def simulated_basis(x,y,a,b,V0,V1):
    y ^= V0[x]
    if ELIGIBLE[x]:
        delta=V0[x]^V1[x]
        assert delta
        pivot=(delta & -delta).bit_length()-1
        y=transform(y,delta,pivot)
        y,a=swap_bit(y,a,pivot)
    # Exactly ONE standard Boolean XOR query on the common input x.
    a ^= b[x]
    if ELIGIBLE[x]:
        y,a=swap_bit(y,a,pivot)
        y=transform(y,delta,pivot)
    return x,y,a


def main():
    pairs=list(itertools.product(range(2,8),range(2),range(2,8),range(2)))
    mixtures=Counter()
    checked_plus_basis_vectors=0
    checked_raw_basis_terms=0
    for v01,v11,v02,v12 in pairs:
        # x0 designated honest image1; x3 outside image6, ignored by marks.
        V0=(1,v01,v02,6)
        V1=(1,v11,v12,6)
        assert all((V0[x]>>1)!=0 and (V1[x]>>1)==0 for x in (1,2))
        for b in itertools.product(range(2),repeat=4):
            values=tuple((V1[x] if b[x] else V0[x]) if ELIGIBLE[x] else V0[x] for x in range(4))
            for x,y in itertools.product(range(4),range(8)):
                # The two equal terms are the unnormalized |+> ancillary state.
                actual=Counter(simulated_basis(x,y,a,b,V0,V1) for a in (0,1))
                expected=Counter((x,y^values[x],a) for a in (0,1))
                assert actual==expected
                checked_plus_basis_vectors+=1
                checked_raw_basis_terms+=2
        # Average eligible residual images under independent Bernoulli marks.
        for b1,b2 in itertools.product(range(2),repeat=2):
            weight=F(1,len(pairs))
            for bit in (b1,b2):
                weight*=LAMBDA if bit else 1-LAMBDA
            f1=v11 if b1 else v01
            f2=v12 if b2 else v02
            mixtures[(f1,f2)]+=weight
    assert len(mixtures)==64
    assert all(p==F(1,64) for p in mixtures.values())
    assert sum(mixtures.values())==1
    source=ROOT/'publications/LULA-I/release/code/lula1/src/lib.rs'
    source_hash=hashlib.sha256(source.read_bytes()).hexdigest()
    assert source_hash=='ac8e67f05af68dd8e1291c5909847f74103903fb7ffa2c70f500c6ec48f14210'
    pdfs=[ROOT/'M-measure/M2-sphincs-reparam/refs/eprint_2022_346_hulsing_kudinov_tight.pdf',
          ROOT/'R8/R8B-immutable-authority/refs/eprint-2022-346.pdf']
    primary=[dict(path=str(p),sha256=hashlib.sha256(p.read_bytes()).hexdigest()) for p in pdfs]
    assert len({p['sha256'] for p in primary})==1
    assert primary[0]['sha256']=='80dcd11e56448d07e2a2465a11ef1a9ca8f4561387abeb3fabdd6d40d4ffe3c3'
    target_calls=17*(1+9)+1+4*(240+1+5)+2040+1+21
    assert target_calls==3217
    result=dict(status='PASS_EXACT_FINITE_COHERENT_FUNCTION_ORACLE_SIMULATION',
        model=dict(query_inputs=4,function_output_bits=3,target_prefix_bits=2,mark_density='1/4',
                   designated_input=0,outside_input=3,eligible_alternate_inputs=[1,2]),
        independent_value_pair_worlds=len(pairs),all_mark_tables_checked=16,
        ancillary_plus_basis_vectors_checked=checked_plus_basis_vectors,
        raw_basis_terms_checked=checked_raw_basis_terms,
        one_boolean_query_per_full_xor_oracle=True,
        ancilla_returns_unentangled_plus=True,
        arbitrary_superpositions_supported_by_linearity=True,
        eligible_function_mixture_support=len(mixtures),
        every_two_residual_output_pair_probability='1/64',
        designated_and_outside_marks_ignored_coherently=True,
        source_sha256=source_hash,primary_pdf_receipts=primary,
        primary_theorem='Hulsing-Kudinov2022/346§8.2Definition9/Theorem4, PDFpage23:8*lambda*(Q_B+1)^2',
        target_verifier_complete_calls=target_calls,
        conditional_one_query_bound='min(1,8*2^-128*(Q+3218)^2)',
        conditional_two_query_fallback='min(1,8*2^-128*(2*(Q+3217)+1)^2)',
        event='Classically extracted alternative-input/same-address targethit in finalverifier trace',
        efficiency='Information-theoretic precompiled finite tables; efficient blackbox simulator OPEN',
        full_QROM_signer_bound=None,quantum_signing_limit=None,NIST_category_certificate=None,
        script_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
    (HERE/'CHECKS.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result,indent=2))


if __name__=='__main__':
    main()
