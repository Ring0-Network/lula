"""Exact abstract marker marginals and clean-plus oracle equality; no attack."""
from fractions import Fraction
from itertools import product
from collections import Counter, defaultdict
from pathlib import Path
import hashlib, json

BASE = Path(__file__).resolve().parent
unitary_columns = 0
def swap_bits(x,a,b):
    if ((x>>a)&1) != ((x>>b)&1):
        x ^= (1<<a)|(1<<b)
    return x

def L(x,d,n):
    pivot = next(j for j in range(n) if (d>>j)&1)
    z = swap_bits(x,0,pivot)
    dp = swap_bits(d,0,pivot)
    for j in range(1,n):
        if ((dp>>j)&1) and (z&1):z ^= 1<<j
    return z

def Linv(x,d,n):
    pivot = next(j for j in range(n) if (d>>j)&1)
    dp = swap_bits(d,0,pivot)
    z=x
    for j in range(n-1,0,-1):
        if ((dp>>j)&1) and (z&1):z ^= 1<<j
    return swap_bits(z,0,pivot)

for n in (1,2,3):
    size=1<<n
    for d in range(1,size):
        assert L(d,d,n)==1
        for x in range(size):assert Linv(L(x,d,n),d,n)==x
        for base,w,active,b in product(range(size),range(size),(False,True),(0,1)):
            outputs=Counter()
            for anc in (0,1):
                z=L(w^base,d,n)
                a=anc
                if not active:
                    old=z&1
                    z=(z&~1)|a
                    a=old
                z^=b
                if not active:
                    old=z&1
                    z=(z&~1)|a
                    a=old
                z=Linv(z,d,n)
                outputs[(z,a)]+=1
            wanted=w^base^(d if active and b else 0)
            assert outputs==Counter({(wanted,0):1,(wanted,1):1})
            unitary_columns+=1

marginal_checks=0
for size in (2,4):
    x=0;y=0
    other=tuple(range(1,size))
    distribution=defaultdict(Fraction)
    whole_marker_marginals=[Fraction(0) for _ in range(size)]
    # Conditional H|X=0,Y=0; exact nonbinary G alphabet is 1,...,N-1.
    for bits in product((0,1),repeat=size-1):
        marked=sum(bits)
        prob=Fraction(1,size)**marked*Fraction(size-1,size)**(size-1-marked)
        for G in product(other,repeat=size):
            value=[y]
            for j,bit in enumerate(bits,start=1):value.append(y if bit else G[j])
            distribution[tuple(value)]+=prob/Fraction((size-1)**size)
    assert len(distribution)==size**(size-1)
    assert all(p==Fraction(1,size**(size-1)) for p in distribution.values())
    assert sum(distribution.values())==1
    marginal_checks+=len(distribution)
    for original in range(size):
        for bits in product((0,1),repeat=size-1):
            marked=sum(bits)
            prob=Fraction(1,size)*Fraction(1,size)**marked*Fraction(size-1,size)**(size-1-marked)
            field=[None]*size
            field[original]=1
            for j,bit in zip((j for j in range(size) if j!=original),bits):field[j]=bit
            for j,val in enumerate(field):whole_marker_marginals[j]+=prob*val
    mu=Fraction(2,size)-Fraction(1,size*size)
    assert all(p==mu for p in whole_marker_marginals)
    marginal_checks+=size

out={
    "classification":"COMPUTED_ABSTRACT_FINITE_CONTROLS_NOT_SOURCE_OR_ATTACK",
    "one_boolean_query_clean_plus_columns":unitary_columns,
    "exact_nonbinary_marginal_checks":marginal_checks,
    "node_domain_sizes":[2,4],
    "unitary_node_sizes":[2,4,8],
    "candidate_whole_bound":"min(1,(2Q+1)^2*(2/N-1/N^2))",
    "zero_query_exactness_checked":True,
    "modulo_sampling_used":False,
    "new_source_game_declarations":0,
    "whole_goal_complete":False,
    "source_attack_benchmark_or_large_table_generated":False,
    "script_sha256":hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    "exit_code":0,
}
(BASE/"FINITE-CONTROLS.json").write_text(json.dumps(out,indent=2)+"\n",encoding="utf-8")
print(json.dumps(out))
