"""Tiny exhaustive disclosure controls and symbolic all-key counter counts."""
from collections import defaultdict
from fractions import Fraction
from itertools import product
from pathlib import Path
import hashlib,json

HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[4]
src=ROOT/'publications/LULA-I/release/code/lula1/src/lib.rs'
pin='ac8e67f05af68dd8e1291c5909847f74103903fb7ffa2c70f500c6ec48f14210'
assert hashlib.sha256(src.read_bytes()).hexdigest()==pin
M=4

# Endpoints initially known, one predecessor queried while hidden, then
# legitimately revealed. Retain prior replies rather than overwrite them.
# Full images have two independently sampled limbs in this toy model.
groups=defaultdict(list)
all_hits=[]; good_consistent=0; conflicts=0; worlds=0
for x0,x1,x2,coin,uhi,ulo,tail1 in product(range(M),repeat=7):
    worlds+=1
    g1=(x2+coin)%M
    table={(1,g1):(uhi,ulo)}
    first_hit=g1==x1  # Analytical only; it does not select a table reply.
    before=dict(table)
    image1=(x2,tail1)
    if (1,x1) not in table:
        table[(1,x1)]=image1
    else:
        assert table[(1,x1)]==before[(1,x1)]
    known_reply=table[(1,x1)]
    assert table[(1,x1)]==known_reply  # Repetition remains byte-identical.
    if not first_hit:
        assert known_reply==image1
        good_consistent+=1
    elif known_reply!=image1:
        conflicts+=1
    # x1 and its suffix are now known; x0 is still hidden.
    g2=(known_reply[0]+x1+coin)%M
    second_hit=g2==x0
    history=(x1,x2,coin,uhi,ulo,tail1,known_reply)
    groups[history].append(second_hit)
    all_hits.append(first_hit or second_hit)
assert all(Fraction(sum(v),len(v))==Fraction(1,M) for v in groups.values())
assert Fraction(sum(all_hits),len(all_hits))==Fraction(7,16)

# Predictable FORS disclosure depends on public independent leaf images,
# never on an unexposed secret. The other leaf remains uniform.
fors_groups=defaultdict(list)
for s0,s1,L0,L1 in product(range(M),repeat=4):
    ss=(s0,s1); leaves=(L0,L1)
    revealed=(L0+L1)%2
    hidden=1-revealed
    g=(ss[revealed]+leaves[hidden])%M
    fors_groups[(L0,L1,revealed,ss[revealed])].append(g==ss[hidden])
assert all(Fraction(sum(v),len(v))==Fraction(1,M) for v in fors_groups.values())

# Counterexample: choose the suffix boundary by reading a still-hidden
# predecessor. Both boundaries leave x0 hidden, but the boundary leaks a bit.
bad_selector=[]
for x0,x1,x2,x3 in product(range(M),repeat=4):
    e=1 if x0<2 else 2
    other_digit=3-e
    assert e>0 and e+other_digit==3 and 0<=other_digit<=3
    guess=0 if e==1 else 2
    bad_selector.append(guess==x0)
assert Fraction(sum(bad_selector),len(bad_selector))==Fraction(1,2)>Fraction(1,M)

def count_slice(w,ell,S):
    d=[1]+[0]*S
    for _ in range(ell):
        pref=[0]
        for v in d:
            pref.append(pref[-1]+v)
        d=[pref[s+1]-pref[max(0,s-w+1)] for s in range(S+1)]
    return d[S]

nuL=count_slice(16,32,240)
nuT=count_slice(256,16,2040)
full=1<<128
assert nuL*1024>=full and nuT*1024>=full
NL=(1<<41)+(1<<36)+(1<<31)+(1<<26)
NT=1<<21
assert NL+NT < 1<<42
out={
 'status':'PASS_EXHAUSTIVE_DISCLOSURE_AND_NEGATIVE_CONTROLS_NOT_FULL_SECURITY',
 'source_sha256':pin,'toy_chain_worlds':worlds,
 'post_disclosure_remaining_hidden_guess_probability_each_history':'1/4',
 'two_hidden_query_union_probability':'7/16',
 'query_union_bound':'1/2',
 'good_prequery_histories_with_consistent_known_suffix_reply':good_consistent,
 'already_charged_histories_with_retained_conflicting_reply':conflicts,
 'fors_remaining_hidden_guess_probability_each_public_history':'1/4',
 'hidden_driven_suffix_selector_guess_probability':'1/2',
 'hidden_driven_selector_preserves_two_chain_w4_target_sum':3,
 'incorrect_unrestricted_disclosure_claim':'1/4',
 'global_counter_model':{
   'lower_key_addresses':NL,'top_key_addresses':NT,
   'lower_accepted_slice_count':str(nuL),'top_accepted_slice_count':str(nuT),
   'digest_space':str(full),'both_densities_at_least_1_over_1024':True,
   'exact_union_expression':'N_L*(1-p_L)^(2^32)+N_T*(1-p_T)^(2^32)',
   'conservative_all_key_failure_upper_bound':'2^(-4194262)',
   'conservative_setup_top_only_failure_upper_bound':'2^(-4194283)',
   'meaning':'Optional independent typed-RO plane existence event; not needed for the partial disclosure-lazy version or a source API failure guarantee.'
 },
 'final_verifier_protected_input_calls_max':17+4*240+2040,
 'scope':'No signatures, cache, timing, source changes or source uploads.'
}
(HERE/'CONTROL-RESULTS.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps(out,indent=2))
