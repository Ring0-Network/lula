# One-query full-word completion of a Boolean marking oracle

**PROVED — manual algebraic lemma; independent review pending.** This is a successor to the conservative two-query completion in the independently saved restricted-row derivations (selected first 74d25d6b and reader first 44dcb6ac). It does not edit either derivation, any earlier theorem, the numerical scripts or the manuscript. The derivation of the identity below is root's new contribution; root had read the two-query candidates first and does not claim blindness to them.

## 1. Exact oracle identity

**PROVED.** Let f:X->{0,1} be an unknown Boolean function with its ordinary XOR oracle U_f|x,b>=|x,b xor f(x)>. Let r_0,r_1:X->{0,1}^w be arbitrary KNOWN functions independent of f. Define Delta(x)=r_0(x) xor r_1(x) and R_f(x)=r_0(x) xor f(x)Delta(x). The full-word XOR oracle U_R|x,y>=|x,y xor R_f(x)> can be implemented exactly using ONE call to U_f, known reversible gates, and a scratch bit returned to zero. There is no controlled-U_f assumption.

**PROVED — program.** Start with |x,y,0>. Apply the w-qubit Walsh-Hadamard transform to the response register. In its Fourier basis z, reversibly compute d=<z,Delta(x)> (binary inner product) into the scratch bit. Apply Hadamard to that scratch: it is |+> for d=0 and |-> for d=1. Call U_f once on (x,scratch). Its sole effect is phase (-1)^(f(x)d); the scratch eigenstate itself is preserved. Apply Hadamard to the scratch and uncompute d, returning scratch=0. Apply the known diagonal phase (-1)^<z,r_0(x)> and invert the response Hadamards.

**PROVED — amplitude calculation.** Before the final response transform the phase on Fourier component z is

`(-1)^(<z,r_0(x)> + f(x)<z,Delta(x)>) = (-1)^<z,R_f(x)>`.

Fourier conjugation of this diagonal character is translation by R_f(x). Thus the output is exactly |x,y xor R_f(x),0>, with no residual x-dependent phase or garbage. The identity holds on every basis vector and hence, by linearity, every superposition and state entangled with arbitrary untouched reference registers. Input x is preserved. Computing known tables may require huge gates/storage: this is a query identity, not a claim of efficient table evaluation.

## 2. Selected and outside words in one coherent query

**PROVED.** For an actual byte-word register u, define the known changed-region predicate e(u) and fixed payload routing pi(u); use a fixed valid payload for malformed/outside u. Let a_0(u),a_1(u) be the full output tables when the selected mark is 0 or 1. On changed words set them to the independently sampled miss/hit completion values. On ALL other words set a_0(u)=a_1(u)=the same fixed side-function value, including rejected and accepted genuine-child counters and any matched invalid-state extension. Set Delta=a_0 xor a_1 in the above program and query U_f at pi(u), computing/uncomputing the routing with known gates.

**PROVED.** Every outside branch has Delta=0, therefore d=0 and the scratch is |+>; the U_f query acts identically there. Mixed-region superpositions use the same single unconditional oracle call. No measurement of region membership, query support or history is performed, and no independent replacement of actual aliases is introduced. Both hit and miss values remain complete w-bit words. The response register is never measured. The uniform Fourier transform is legal for the fixed-width XOR answer interface used in the existing global-Raw model.

## 3. Consequence for the restricted canonical row

**CITED — search theorem.** SPHINCS+C, https://eprint.iacr.org/2022/778, Appendix E, Theorem E.3 (printed page 35, PDF index 37 in the pinned local PDF) gives success at most 8 lambda (k+1)^2 for k Boolean queries to an independent Bernoulli-lambda random function. This lemma uses that theorem, not a fresh claim about the proof of E.3.

**PROVED — conditional consequence.** In the independently derived restricted-row experiment, condition on independent side data BEFORE source A begins: parameter, address, ideal F/J, genuine child and its entire same-child canonical row. On each nonbottom branch the changed-base full256 region is product uniform and its target-prefix equality marks are Bernoulli lambda=2^-128. Independent hit/miss completion tables and outside data are known interquery operations. The identity above simulates M fullRaw calls with M Boolean calls rather than 2M. Hence the component success bound is

`min(1, 8*(M+1)^2 / 2^128)`.

**PROVED — exact scope of M.** The preserved adapter that executes the selected final verifier digest uses M<=Q+1 and therefore 8*(Q+2)^2/2^128. The NEW stopping search extractor described in the first author's restricted-row derivation outputs the classical candidate immediately before that digest and has M<=Q, therefore 8*(Q+1)^2/2^128. This does not silently tighten the resource count of an earlier program. The extractor may output from branches not ultimately accepted; search success is a superevent, so recognizing the full source winning event is unnecessary. All honest work is still charged in execution time/global source queries, even where its values are part of f-independent side data.

**PROVED — preservation conditions.** The first accepted literal BE32 counter and unconditioned bottom mass remain in the side data. No 1/tau normalization occurs. The tighter optional factor tau_kind remains valid if target existence is independently accounted for as in the reader's first proof. Source seed-zero must remain excluded in the marked-domain argument and charged once elsewhere. Source prekey/hidden target computation is commuted only under the SAME static full oracle with disjoint private registers, not by a marginal-independence or no-hit argument.

**OPEN.** Review of the restricted experiment's factorization, source honest-query exclusions and stopping extractor is separate from the pure one-query identity. This file alone does not promote the source selector inequality, fixed-h SHA hardness, ordinary collection security or a complete signature bound. Old scalar bounds are unchanged. No operational source attack, timing benchmark, global installation, private upload or new source-game kernel declaration is supplied.

## 4. Controls and mechanization boundary

**COMPUTED — pending actual execution of the paired script.** one_query_completion.py exhausts all two-point Boolean functions and all two-bit hit/miss tables, checks every clean-input computational basis vector over exact Q(sqrt(2)), and compares the complete state with the desired XOR state. Small finite controls complement, rather than replace, the general amplitude proof. A classical Lean helper for the binary dot-product identity can be checked separately; it would not be a kernel proof of the entire quantum circuit or cryptographic game.
