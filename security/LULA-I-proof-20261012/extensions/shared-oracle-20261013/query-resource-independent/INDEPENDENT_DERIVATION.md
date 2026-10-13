# Independent constant-success query interpretation

## Scope and independence

I read the three accepted manual source-model theorems and the older independent classical occupancy interval dataset. I did not read any new root query-threshold output; none was used to construct this calculation. `thresholds.py` does not import the root numerical scripts. It implements the theorem expressions afresh using Python exact integers, `Fraction`, and `isqrt`. The prior occupancy dataset is an explicitly reused input, not a new independent proof of the FORS term.

This task asks a distinct resource question: for fixed initiated signing cap q, how many adversarial raw-oracle queries does the accepted sufficient upper bound permit while still proving winning probability at most 1/2? It does not replace the original small-failure requirements or certify them. The declared source interface remains partial, unconditioned, classical-signing, opaque honest-cache only. Query counts do not include honest computation, circuit depth, gates, memory costs or implementation leakage.

## Formula derivation

Set N=2^128, M=N^2-N, and p=p_F(q), the exact-binomial per-raw-candidate FORS coverage probability. The classical accepted expression is

    E_C(q,Q) = min(1, (6Q+3q+6243)/N
        +(qQ+q(q-1)/2+q)/N^2
        +q(511/512)^(2^32)+(Q+1)p).

Its uncapped expression is affine in Q, with strictly positive coefficient a=6/N+q/N^2+p and nonnegative constant b=(3q+6243)/N+[q(q-1)/2+q]/N^2+q(511/512)^(2^32)+p.

The complete quantum components, taken from their reviewed theorem rather than fixed numerical rows, are

    D=min(1,q[sqrt((Q+q+1)/M)+(Q+q+1)/(2M)]),
    A=min(1,D+8(Q+2)^2[p+1/N+q/N^2]),
    c=min(1,(2Q+sqrt(q))^2/N+[2(Q+2)/sqrt(N)+sqrt(A)]^2),
    h=min(1,(2Q+sqrt(3017))^2/N),
    g=min(1,8(Q+3218)^2/N),
    d=min(1,8(Q+6)^2/N).

The conservative complete expression is

    E_K=min(1,1/N+min(1,2Q/sqrt(N)+(2q+2)/N)+c+h+g+d).

The separate shared-projector expression is

    E_R=min(1,1/N+[2Q/sqrt(N)
        +sqrt(min(1,min(1,(2q+2)/N)+min(1,c+h+g+d)))]^2).

Both remain valid; their minimum E_B=min(E_K,E_R) is therefore valid. Although E_R sharply improves the small-probability regime, it is not globally smaller than E_K. At the 1/2 crossing, the conservative expression yields the larger query allowance for q<=2^44. The integer allowances agree for q=2^50 and 2^64. Treating the refined bound alone as globally strongest would lose a valid theorem.

Every input and operation is nonnegative and nondecreasing in Q. Sums, squares, square roots, positive divisions, caps at one and minima preserve that monotonicity. Therefore an adjacent pair Q_pass and Q_fail=Q_pass+1 with E(Q_pass)<=1/2<E(Q_fail) characterizes the unique integer crossing of the selected accepted bound expression. For all eight requested q, E(0)<1/2; increasing powers of two eventually provide a failing upper endpoint.

## Outward rational computation

The older independent occupancy dataset stores binary floating-point endpoints as exact (sign,mantissa,exponent,bit-count) tuples. Their exact dyadic interpretations enclose p. Repeated q rows agree exactly and are checked before use. No decimal conversion is used.

All subsequent operations use exact `Fraction`. At sqrt input x=a/b>=0, let t=isqrt(floor(a*2^(2P)/b)), P=1024. Then t^2/2^(2P)<=x<(t+1)^2/2^(2P). Thus [t/2^P,(t+1)/2^P] is an outward interval; if the upper endpoint input is a perfect square, its exact square root is retained. Applied to the two ends of an input interval, monotonicity gives a rigorous square-root enclosure. The script asserts the defining floor inequalities for every square-root endpoint.

The enormous exhaustion power is not explicitly exponentiated. Its enclosure is

    0 <= (511/512)^(2^32) <= 2^-4096.

Indeed (1-x)^m<=exp(-mx), mx=2^23, and exp(-2^23)<=2^(-2^23)<=2^-4096 because ln(2)<1. Its total contribution is at most 2^-4032 for q<=2^64. This is a rigorous interval for the unchanged accepted expression, not omission of the term.

Each bisection comparison is certified PASS only if the outward upper endpoint is <=1/2 and FAIL only if its outward lower endpoint is >1/2. Any overlap raises an error instead of guessing. Exact rational margins from 1/2 are saved for both adjacent endpoints. This makes arbitrary rounding in the printed approximate logarithms irrelevant to the gate.

The rigorous conclusion is relative to the previously accepted outward occupancy input and the manually reviewed source-model theorems. It is not mechanical verification of those mathematical/source theorems or a fresh occupancy certification. Hash pins identify all inputs and this calculation.

`crosscheck.py` independently inverts the affine classical bound with exact rational lower/upper coefficient brackets and recovers all eight same integer thresholds. It also evaluates every pass/fail endpoint with 128-bit and 256-bit outward square-root brackets: all 64 endpoint comparisons agree at each precision. A 64-bit probe leaves 30 endpoints straddling 1/2, so that precision is insufficient for adjacent integer certification here. This does not claim 128 is the minimal possible precision; it demonstrates that 128 suffices and the delivered 1024-bit calculation has ample margin.

## Interpretation

`Q_pass` proves that the selected accepted bound suffices for at most 1/2 winning probability at that adversarial query cap. `Q_fail` proves that the sufficient bound expression exceeds 1/2; it does not prove an attack, an optimal adversarial probability, or an actual security failure. Monotonicity of the bound cannot be inverted to obtain a lower bound on the adversary's success.

At q=2^40 the classical query-bound crossing has approximate log2(Q_pass)=124.404903734342; the minimum of the two quantum bounds gives approximately 60.416375433175. At q=2^64 the corresponding integer passes are 254 classical queries and 3 quantum queries. These are finite-query model guarantees at the selected constant success target, not 124-bit/60-bit security category assertions and not measured attack costs.

## Artifacts

`THRESHOLDS.json` contains all 32 certified adjacent pairs, exact rational pass/fail margins, source theorem and occupancy data digests, and the script digest. `THRESHOLDS.md` is the human-readable table. No manuscript, timing, source, fixed parameters, proof packet outside this directory, implementation attack or external upload was changed.

Outcome: CERTIFIED_RATIONAL_BRACKETS_OF_REVIEWED_BOUND_CROSSINGS. Full level/category and implementation certification remains NOT ESTABLISHED.
