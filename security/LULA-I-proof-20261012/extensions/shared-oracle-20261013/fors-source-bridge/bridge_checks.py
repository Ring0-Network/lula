#!/usr/bin/env python3
"""Exact source-format and oracle-budget discriminators; no cryptographic execution.

Run python -I -B bridge_checks.py. Standard library only; writes beside this script.
These are local controls for the stated classical joint ideal-game lemma, NOT EUF attacks.
"""
from fractions import Fraction as F
import hashlib
import itertools
import json
import math
from pathlib import Path

HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[4]


def rat(value):
    return dict(numerator=str(value.numerator),denominator=str(value.denominator),decimal=float(value))


def inner_prediction_control():
    # Two unique message labels, one four-valued R guess each; later select hit labels.
    values=list(itertools.product(range(4),repeat=2))
    predictions=[(0,0),(1,1)]
    hit=sum(any(j[m]==r for m,r in predictions) for j in values)
    exact=F(hit,len(values))
    assert exact==1-F(3,4)**2==F(7,16)
    union=F(len(predictions),4)
    assert exact<=union
    # A single queried point cannot predict 100 different labels: its suffix stays fixed.
    fixed_label_hit=sum(j[0]==0 for j in values)
    assert F(fixed_label_hit,len(values))==F(1,4)
    return dict(exact_adaptive_selected_prediction_hit=rat(exact),
                q_free_total_prediction_union=rat(union),
                naive_q_times_predictions_union=rat(F(2*len(predictions),4)),
                one_fixed_prediction_regardless_of_repeated_signing=rat(F(1,4)),
                note='Only unseen-label ideal J guesses. Public/raw J leakage is excluded by the preceding idealization.')


def randomizer_repetition_control():
    worlds=list(itertools.product(range(2),repeat=2))
    repeats=inner_alias=omitted_message_alias=0
    for r0,r1 in worlds:
        repeats+=int(r0==r1)
        i0=(r0,1,0,0)
        i1=(r1,1,0,1)
        inner_alias+=int(i0==i1)
        omitted_message_alias+=int((r0,1,0)==(r1,1,0))
    assert repeats==2 and inner_alias==0 and omitted_message_alias==2
    return dict(randomizer_repeat_probability=rat(F(repeats,len(worlds))),
                actual_framed_inner_input_aliases=inner_alias,
                negative_control_without_message_alias_probability=rat(F(omitted_message_alias,len(worlds))),
                note='A repeated R alone does not collide distinct complete I inputs.')


def format_separation_control():
    # Reduced literal framing: R|S|root|m and U_hi|U_lo|c|S.
    S=1
    I={(r,S,root,m) for r,root,m in itertools.product(range(2),repeat=3)}
    E={(hi,lo,c,S) for hi,lo,c in itertools.product(range(2),repeat=3)}
    eligible={x for x in E if x[1]!=S}
    intersection=I&E
    assert len(intersection)==4 and not (I&eligible)
    # Full actual byte formats; construct a structural overlap without hashing.
    public_seed=bytes(range(1,17))
    R=bytes([77])*16
    ctr=0x12345678
    root=ctr.to_bytes(4,'big')+public_seed[:12]
    message=public_seed[12:16]
    inner=R+public_seed+root+message
    U=R+public_seed
    outer=U+ctr.to_bytes(4,'big')+public_seed
    assert inner==outer and len(inner)==52
    assert U[16:32]==public_seed
    addressed=public_seed+bytes(48)+bytes(22)+bytes(16)
    assert inner[16:32]==public_seed and addressed[16:32]==bytes(16)
    assert len(addressed)==102 and len(outer)==52
    return dict(toy_unrestricted_I_E_intersection=len(intersection),eligible_I_E_intersection=0,
                full_byte_overlap_length=52,overlap_requires_U_half_equals_S=True,
                full_byte_control_sha256=hashlib.sha256(inner).hexdigest(),
                addressed_length=102,outer_length=52,
                note='Literal SHA input serialization control only. The constructed public root is a framing witness, not a generated signing key.')


def outer_prefix_prediction_control():
    # Two counters with one guessed U prefix; fresh future U is four-valued.
    prefixes=[0,0]
    U_values=list(range(4))
    one=F(sum(u in prefixes for u in U_values),len(U_values))
    assert one==F(1,4)
    q=2
    worlds=list(itertools.product(U_values,repeat=q))
    any_hit=F(sum(any(u in prefixes for u in us) for us in worlds),len(worlds))
    assert any_hit==F(7,16)
    assert any_hit<=q*one
    return dict(distinct_counter_points=2,distinct_guessed_namespaces=1,
                one_future_U_hit=rat(one),two_future_U_hit=rat(any_hit),
                q_times_distinct_namespace_union=rat(q*one),
                note='The q factor is legitimate for a U-prefix guess that does not encode a message label.')


def conditioning_control():
    # Candidate output Y is uniform. The schedule makes more prefix guesses when Y=1.
    # Good means future uniform U avoids those guesses; conditioning biases Y.
    worlds=list(itertools.product(range(2),range(4)))
    good=[]
    for y,u in worlds:
        guessed={0} if y==0 else {0,1,2}
        if u not in guessed:
            good.append((y,u))
    conditioned_zero=F(sum(y==0 for y,u in good),len(good))
    assert conditioned_zero==F(3,4) and conditioned_zero!=F(1,2)
    return dict(unconditional_candidate_Y_zero=rat(F(1,2)),
                candidate_Y_zero_conditioned_on_no_prefix_hit=rat(conditioned_zero),
                note='Do not assert iid streams after conditioning on no Bad. Unconditional prefix coupling/padding is required.')


def collision_pair_control():
    # Collision of one signing U with two distinct public inner outputs, then with one final output.
    world=list(itertools.product(range(4),repeat=4))
    success=sum(any(values[i]==values[0] for i in (1,2,3)) for values in world)
    exact=F(success,len(world))
    assert exact==1-F(3,4)**3==F(37,64)
    assert exact<=F(3,4)
    return dict(one_honest_two_public_one_final_exact_collision=rat(exact),
                relevant_pair_union=rat(F(3,4)),
                note='Only pairs containing an honest inner value are needed; full-oracle birthday pairs are not silently charged.')


def final_point_cases_control():
    S=1
    oldU=(0,0)
    old_rejected=(oldU,0)
    old_accepted=(oldU,1)
    retained_public=((1,0),2)
    counts={}
    for U,c in itertools.product(itertools.product(range(2),repeat=2),range(4)):
        if U[1]==S:
            case='Bad_end'
        elif (U,c)==old_rejected:
            case='old_rejected_filter_failure'
        elif (U,c)==old_accepted:
            case='old_accepted_requires_Bad_U_for_fresh_message'
        elif U==oldU:
            case='new_counter_old_namespace_requires_Bad_U'
        elif (U,c)==retained_public:
            case='retained_public_candidate'
        else:
            case='extra_fresh_final_candidate'
        counts[case]=counts.get(case,0)+1
    assert sum(counts.values())==16
    assert counts=={'old_rejected_filter_failure':1,
                   'old_accepted_requires_Bad_U_for_fresh_message':1,
                   'new_counter_old_namespace_requires_Bad_U':2,
                   'Bad_end':8,'extra_fresh_final_candidate':3,'retained_public_candidate':1}
    assert (0,S,0,1)!=(1,S,0,0)  # Different message => different full inner input.
    # A preinstalled accepted first-counter value can correlate X with public Y,
    # but the guessed U namespace is exactly what Bad_Epre flags.
    guessed_prefix=(1,0)
    new_honest_U=(1,0)
    public_candidate=(1,0)  # toy (leaf,filter), with filter zero
    honest_exposure=public_candidate[:-1]
    assert guessed_prefix==new_honest_U and honest_exposure==public_candidate[:-1]
    return dict(final_pair_cases=counts,total_pairs=16,
                correlated_preinstalled_counter_has_Bad_Epre=True,
                note='Complete tiny final-point partition and a deliberately prequeried accepted-counter dependency; no real verification API is used.')


def expected_budget_is_not_cap_control():
    # Two equally probable transcript states. Search only when success probability is1/2.
    # N(T)=0 or2; E[N]=1 is not a bound on N and is correlated with p(T).
    worlds=list(itertools.product(range(2),range(2),range(2)))
    wins=sum(t==1 and (y0==1 or y1==1) for t,y0,y1 in worlds)
    actual=F(wins,len(worlds))
    mean_N=F(1)
    mean_p=F(1,4)
    invalid=mean_N*mean_p
    deterministic_cap_union=2*mean_p
    assert actual==F(3,8)>invalid==F(1,4)
    assert actual<=deterministic_cap_union==F(1,2)
    return dict(actual_adaptive_search=rat(actual),mean_candidate_count=rat(mean_N),
                mean_single_try_coverage=rat(mean_p),invalid_expected_count_times_mean_coverage=rat(invalid),
                deterministic_cap=2,valid_deterministic_cap_union=rat(deterministic_cap_union),
                note='Generic adaptive-allocation discriminator, not LULA parameters. Padding requires a deterministic pathwise bound.')


def source_receipt():
    lib=ROOT/'M-measure/LULA-I-comparison-20261011-a1/sources/ra-r6a/src/lib.rs'
    driver=ROOT/'M-measure/LULA-I-comparison-20261011-a1/sources/ra-r6a/src/bin/m3_ra.rs'
    src=lib.read_text(encoding='utf-8')
    required=[
        'sha256_counted(&[&self.sk_prf, &self.pk_seed, m])',
        'sha256_counted(&[r, &self.pk_seed, &self.pk_root, m])',
        'b[..32].copy_from_slice(inner);',
        'b[32..36].copy_from_slice(&ctr.to_be_bytes());',
        'b[36..52].copy_from_slice(&self.pk_seed);',
        'get_bits(&dig, ka - p.a as usize, p.a as usize) == 0',
        'let idx = get_bits(&dig, ka, h);',
        'out.extend_from_slice(&ctr.to_be_bytes());',
    ]
    assert all(x in src for x in required)
    verify=src[src.index('pub fn verify_root'):]
    assert 'prf_msg' not in verify
    assert 'let r = take(&mut off);' in verify
    assert 'ctx.hmsg_outer(&inner, ctr)' in verify
    parameter='18,9,1;5:4:0:240:0|5:4:0:240:0|5:4:0:240:0|5:4:0:240:0|21:8:0:2040:1'
    assert parameter in driver.read_text(encoding='utf-8')
    return dict(original_library_path=str(lib),original_library_sha256=hashlib.sha256(lib.read_bytes()).hexdigest(),
                driver_path=str(driver),driver_sha256=hashlib.sha256(driver.read_bytes()).hexdigest(),
                static_source_interface_checks=len(required)+4,
                FORS=dict(B=1<<41,t=512,K_real=17,used_digest_bits=203,output_bits=256,C_counter_inputs=1<<32),
                joint_idealization='F and J private memoized full images; other complete SHA calls share O',
                note='Static source anchors, not a Rust semantics proof or signature execution.')


def sufficient_beta_components():
    q=1<<40
    rows=[]
    for logQ in (0,32,40,64,128):
        QH=1<<logQ
        b128=F(2*QH+q+2,1<<128)
        b256=F(q*QH+math.comb(q,2)+q,1<<256)
        # Avoid constructing enormous fraction exponents for the tiny finite-search term.
        rows.append(dict(q_initiated=str(q),log2_Q_H=logQ,
                         beta_128bit_events=rat(b128),beta_256bit_events=rat(b256),
                         beta_nonexhaustion=rat(b128+b256),
                         exhaustion_upper='2^-8388568 under fresh-counter premise',
                         beta_total_expression='min(1,beta_nonexhaustion + q*(511/512)^(2^32))',
                         meaning='Sufficient ideal coverage-coupling loss; NOT full EUF-CMA advantage or a demonstrated attack'))
    return rows


def main():
    result=dict(status='PASS_EXACT_SOURCE_BRIDGE_CONTROLS',
                source=source_receipt(),inner_prediction=inner_prediction_control(),
                R_repeat=randomizer_repetition_control(),formats=format_separation_control(),
                outer_prefix_guess=outer_prefix_prediction_control(),
                survivor_conditioning=conditioning_control(),relevant_U_collisions=collision_pair_control(),
                final_outer_cases=final_point_cases_control(),
                padding_budget=expected_budget_is_not_cap_control(),
                sufficient_beta_components=sufficient_beta_components(),
                source_bound_coverage_lemma_status='PROVED under joint ideal-game and declared atomic/classical interface; manual source refinement',
                full_reference_euf_bound=None,full_cached_euf_bound=None,QROM_bound=None,
                script_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
    (HERE/'CHECKS.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:v for k,v in result.items() if k not in ('sufficient_beta_components','source')},indent=2))
    print('Source static interface checks and exact discriminators passed; no signing or timing measurements executed.')


if __name__=='__main__':
    main()
