# Monotonicity and integer query-budget certification

**PROVED — manual mathematical analysis of the already reviewed envelopes.** This derivation was saved before inspecting any threshold candidate or another agent's resource analysis. It uses only `CLASSICAL-RO-THEOREM.md`, `QUANTUM-RO-THEOREM.md`, and `QUANTUM-EVENT-SPECIFIC-THEOREM.md`. No source-valid forgery, executable search, runtime, or gate-cost estimate is constructed.

## 1. Variables and event meaning

Fix an initiated signing-call cap q in the nonnegative integers, the pinned source parameters, N=2^128, M=N^2-N, and the exact candidate probability p=p_F(q). Then 0<=p<=1/512. The variable Q is the nonnegative integer adversarial complete-hash query cap; classical and coherent caps are distinct interfaces. Write B_C(Q), B_Q(Q), B_E(Q) for the classical, conservative quantum, and refined quantum sufficient winning-probability bounds, respectively. Write B_best(Q)=min(B_Q(Q),B_E(Q)). Every B bounds the winning probability of every adversary with that query budget in the specified game. It is an upper bound, rather than an asserted attainable success curve.

## 2. Classical monotonicity and exact symbolic threshold

The classical envelope is min(1,a*Q+b), where

    a = 6/N + q/N^2 + p > 0,
    b = (3q+6243)/N + (binom(q,2)+q)/N^2
        + q*(511/512)^(2^32) + p >= 0.

The uncapped affine function is strictly increasing in Q. The cap at one preserves nondecreasing order. For a target t=1/2, the cap changes no gate because t<1: B_C(Q)<=t iff a*Q+b<=t. If b>t, no nonnegative integer Q is certified. If b<=t, the exact largest certified integer is

    Q_C = floor((t-b)/a).

Equality is included. The exact real quotient and floor must be computed or enclosed sufficiently to resolve the integer boundary; a decimal approximation to log2 of the quotient does not certify an integer floor. Also B_C(N)=1 since its affine term contains 6Q/N=6. Thus any classical certified integer is smaller than N, regardless of the value of q.

## 3. Quantum monotonicity

The following operations preserve order for nonnegative real inputs: addition, multiplication by a nonnegative constant, division by a strictly positive constant, square root, squaring, and a cap x |-> min(1,x). Squaring requires nonnegative inputs: it is not generally monotone over all real numbers.

For fixed q, Q+q+1 and Q+2 are nonnegative increasing functions. Consequently

    D(Q) = min(1,q*(sqrt((Q+q+1)/M)+(Q+q+1)/(2M)))

is nonnegative and nondecreasing. Therefore A(Q)=min(1,D(Q)+8*(Q+2)^2*(p+1/N+q/N^2)) is nonnegative and nondecreasing. Both nonnegative summands inside c(Q), including the square of 2*(Q+2)/sqrt(N)+sqrt(A(Q)), are nondecreasing, so c is nondecreasing. The same argument applies to h, g, and d7. It applies to delta=min(1,2Q/sqrt(N)+(2q+2)/N). Hence B_Q=min(1,1/N+delta+c+h+g+d7) is nondecreasing.

For the refinement, e(Q)=min(1,c+h+g+d7) is nonnegative and nondecreasing, while b_E=min(1,(2q+2)/N) is constant. Thus min(1,b_E+e(Q)), its square root, the nonnegative sum with 2Q/sqrt(N), the square of that sum, and the final seed-inclusive cap are all nondecreasing. This proves that B_E is nondecreasing. The pointwise minimum of two nondecreasing functions is nondecreasing, so B_best is also nondecreasing.

At Q=2^63, 2Q/sqrt(N)=1. The conservative bound is one because delta=1; the event-specific bound is one because its square is at least one. Thus B_best=1 for all Q>=2^63. This is a finite upper bracket for the first failed target gate; it is not a quantum attack or a security classification.

## 4. Inclusive integer convention and boundary certificate

For any of these nondecreasing envelopes B, define

    Cert(B,t) = { Q in the nonnegative integers : B(Q)<=t }, t=1/2.

If B(0)>t, Cert is empty, and report `NO_CERTIFIED_NONNEGATIVE_QUERY_BUDGET`, with a null largest-certified integer. Do not report zero: zero would falsely claim that the Q=0 gate passed. If B(0)<=t, the set is a finite initial interval because the preceding finite brackets have bound one. Its largest integer K is unique and is certified exactly by the two inequalities

    B(K)<=t < B(K+1).

Monotonicity proves B(Q)<=t for every Q<=K and B(Q)>t for every Q>=K+1. The endpoint K is included, even if B(K)=t. Equivalently, the least failing integer F has B(F)>t and K=F-1 when F>0. A binary search over integer Q, followed by verification of both adjacent endpoint inequalities, implements this convention. Rounding a continuous root down without checking its adjacent integers is insufficient near equality.

## 5. Numerical evidence needed for a rigorous threshold

The gate concerns the true mathematical envelope. High-precision evaluation alone does not enclose its rounding error. To certify a proposed K, use a valid upper enclosure U(K)<=1/2 and a valid lower enclosure L(K+1)>1/2 for that same envelope, with outward propagation through all additions, products, roots, and minima. An interval for p_F(q), including its series-tail error, must feed these enclosures. For B_best, its true value is the minimum of the two true expressions; an upper enclosure may use either, but a lower enclosure of the minimum requires lower bounds for both expressions. If an enclosure straddles the target, increase precision or return an unresolved integer bracket instead of promoting an approximate floor.

It is possible to certify a useful safe budget even when its exact largest integer cannot be resolved: if U(Q_safe)<=1/2, all lower integers are certified. Distinguish such a sufficient budget from an exact boundary. A failed sufficient gate at Q=0 likewise does not prove a real zero-query attack; it only means this envelope supplies no budget certification.

## 6. What the data establishes

The certificate proves an adversarial raw-query lower bound for attaining winning probability strictly greater than 1/2: no adversary with Q<=K can attain such success in the stated interface. It does not rule out success exactly 1/2 at Q=K. A certificate B(Q_safe)<1/2 can instead exclude success at least 1/2 at that safe budget. Neither B(K+1)>1/2 nor a cap at one gives an attack, an attainable success probability, a runtime, a gate count, or an upper bound on the cost of attacking the construction.

The result is conditional on the reviewed RO/QROM game, source parameters, initiated-call convention, and honest opaque atomic cache interface. It is not an efficient primitive reduction, fixed-SHA theorem, mechanical Rust refinement, classical security level, NIST category, or a claim that query cost equals the reference AES circuit cost. A logarithm of K is a logarithm of a sufficient raw-query budget, not a certified number of security bits.

## 7. Separate no-crossing result for the original tiny-failure gates

**PROVED — exact algebra, independently derived from the displayed formulas.** This is a different criterion from the success target 1/2. For every q>=0 and Q>=0, the uncapped classical sufficient sum is at least 6243/N. Because N=2^128>6243>1, both 6243/N and the cap 1 are strictly greater than 1/N. Consequently the capped classical envelope is strictly greater than 2^-128 everywhere in this domain, even at q=Q=0. There is no q crossing where this particular sufficient envelope satisfies a failure-probability target 2^-128. At the specifically requested Q_H=N, the term 6Q_H/N alone is six, so the capped classical envelope is exactly one for every q.

At the specifically requested Q=sqrt(N)=2^64, the private vector term is a=2Q/sqrt(N)=2. The conservative delta is one, so its seed-inclusive total cap is one. In the event-specific expression the nonnegative square is at least a^2=4, so its final cap is also one. Their minimum is one for every q. Hence this sufficient best envelope never satisfies the requested failure-probability target 2^-64 at that Q. The stronger observation in Section 3 already makes both envelopes one at Q=2^63.

These facts certify failure of the reviewed sufficient estimates to establish the original tiny-failure criteria. They do not certify failure of the construction, an actual adversarial success rate, or absence of a stronger proof. Neither conventional 128-bit classical work strength nor NIST category1 is defined by requiring such tiny success after the full corresponding search budget. Preserve these `BOUND_DOES_NOT_ESTABLISH_REQUESTED_GATE` results separately from the success-target-1/2 resource thresholds.

## 8. Small checked support

`QueryThreshold.lean` separately checks the order-theoretic steps for caps, minima, certified prefixes, failed suffixes, and an adjacent integer boundary. It abstracts over a linearly ordered codomain and assumes monotonicity only in the threshold declarations. The manual derivation above proves monotonicity of the actual nested scalar formulas; the Lean file does not mechanize square-root arithmetic, p_F evaluation, or the full cryptographic theorem. Its checked status is reported separately from numerical thresholds.
