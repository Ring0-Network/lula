# Single-target random-function PRE: independent finite derivation

Saved before reading any NEW peer single-target quantitative derivation. This is a finite-query random-function result, not fixed-SHA hardness or a LULA source-security theorem. The earlier accepted one-query completion and primary average-search theorem are reusable tools.

## 1. Exact experiment and indispensable side-state hypothesis

Let N=2^n. A chooses one actual tweak T with coins independent of the random function before receiving P; it makes no public-function query before the challenge. Sample uniform public P, uniform hidden X in{0,1}^n and a random full-word function H on an injectively framed finite domain. Its selected row is a genuinely independent restriction at raw word frame(P,T,x). Give A the prefix Y=prefix_n H(frame(P,T,X)), P and its own prior state, but not X. Afterward it makes at most Q full-output XOR oracle queries and outputs a classical candidate z in{0,1}^n. Success is prefix_n H(frame(P,T,z))=Y. Non-node/invalid output fails.

Any auxiliary state/interquery service must be independent of X in the GHOST experiment conditional on P,T,Y and the ghost function. Independent lower-limb and outside function tables may be retained; they must not disclose X or provide extra target-row answers outside Q. Target-only accounting for a source simulation is a separate theorem. Arbitrary X-dependent advice invalidates this lemma even atQ=0. In particular this result cannot be imported solely because an ordinary primitive game has a similarly named property.

## 2. Original-input hit by a one-point ghost overlay

Sample uniform X,Y independently of a full random H0. Define H1 to equal H0 everywhere except the PREFIX at frame(P,T,X), which is replaced by Y; retain H0's lower output limb there. This has the exact real joint law of(P,T,X,H,Y=prefix H(P,T,X)): for each X, the special prefix is uniform, its lower limb is independently uniform, all other outputs are independently uniform, and the conditional challenge equation holds. No prior A query exists to be retroactively overwritten in the actual challenge chronology. The ghost experiment uses H0, the same independently sampled Y and the same initial A state.

In the continued ghost state X is unused: H0,P,T,Y and A's quantum state are jointly independent of X. Every coherent raw basis word nominates at most one selected payload x; therefore expected query support on frame(P,T,X) is at most1/N. The full-XOR discrepancy has norm at most twice the square root of that support. Purifying all function coins and algorithm measurements, the usual telescoping identity evaluated on ghost prefixes gives final vector distance at most2Q/sqrtN. No query history is measured, and no surviving-key/no-hit posterior is used.

Use the same terminal projector z=X in both purified experiments, with X retained solely in the analyst register. Ghost success for this original-input event is1/N (or at most1/N if invalid output is allowed), because z is independent of X. Triangle inequality after that projector gives

    Pr_real[z=X] <= min(1,(2Q+1)^2/N).

This includes challenge-image-informed coherent computation, lower output limbs, retained memory and intermediate measurements. It counts Q actual calls to the full oracle; every permitted side operation is part of the same X-independent ghost algorithm. Opaque source objects or free auxiliary target evaluations require separate validation of that condition.

## 3. Different-input hit as an ordinary average-search program

For this event only, the reduction samples and KNOWS X; it never reveals X to A. Also sample P,Y and the actual lower limb L_X at the designated word. Set H(P,T,X)=Y||L_X. For every other selected-row payload x, sample an independent Bernoulli mark f(x) with probabilitylambda=1/N. Independently choose full-word hit value r1(x) with prefixY and uniform lower limb, and miss value r0(x) with uniformly chosen prefix unequalY and uniform lower limb. The mixture has exactly the uniform full-word law at every x!=X. All marks are independent of the known pair tables, X,Y,P and outside functions. AtX and every outside/malformed word choose r0=r1 equal to the known corresponding value. Sample unused iid marks there too, but ignore them.

The reduction simulates every full XOR query using ONE ordinary Boolean XOR query: Fourier-transform the response, compute d=<z,r0 xor r1> into scratch, Hadamard the scratch, make one f-query, restore/uncompute scratch, apply the known phase for r0 and invert the response Fourier transform. The phase is exactly(-1)^<z,r0 xor f(x)(r0 xor r1)>; scratch returns clean. On the designated/outside words the difference is zero and scratch is|+>, so the unconditional Boolean call acts identically. This is valid on arbitrary entangled superpositions, with no free controlled-f oracle or measurement.

When A outputs a node z, the reduction outputs that z immediately, without evaluating its final digest, and without first recognizing whether it is a PRE winner. If z!=X and the actual real PRE predicate holds, then f(z)=1. On other branches average-search success can be larger; that is harmless. Hence this program uses Q_B<=Q, not Q+1, and

    Pr_real[z!=X AND prefix H(P,T,z)=Y] <= min(1,8(Q+1)^2/N).

The8 and+1 are from HK22 Section8.2 Definition9/Theorem4 (HRS16 average search), verified in the cached primary text lines1027–1036; pdf80dcd11e..., textbe27fac7.... Its+1 already permits a final unevaluated candidate. Performing a verification query first would produce a DIFFERENT program with Q_B<=Q+1 and8(Q+2)^2/N. No such query is needed here. Known pair tables may be exponentially large; this is information-theoretic finite query complexity, not an efficient sampler or a gate-cost certification.

## 4. Combined conclusion and limitation

The two events are disjoint and exhaust PRE success. Thus

    kappa_PRE(Q) <= min(1,[(2Q+1)^2+8(Q+1)^2]/N).

Equivalently the uncapped numerator is12Q^2+20Q+9. This proves the proposed constant under the exact no-prequery/independent-ghost-side-state interface. It does not substitute all honest source hash calls by Q, exclude a selected tweak's history by assumption, prove a target-only UD bound, or establish actual fixed-hash security. A lawful source adapter must supply that interface and account for all other functions/circuit/time/storage resources. No target sum/counter completion or seed-zero normalization is part of this primitive lemma; any relevant source failure branches remain unnormalized in the calling game.

AtQ=0 the expression9/N is loose. Direct real-law averaging with any fixed independent candidate gives2/N-1/N^2 (one original-input chance and one independent collision chance); this is a useful exact-law negative control against treating the target image as an entirely independent image without its planted preimage. This finite random-function fact is not an attack on an implementation.
