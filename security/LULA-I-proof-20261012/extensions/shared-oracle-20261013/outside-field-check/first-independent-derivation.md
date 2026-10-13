# Independent finite random-function simulator derivation

Saved before inspecting any existing outside-simulator proposal. Author: outside-field-check subagent. Scope: a manual construction/proof and conservative circuit-resource upper bounds, not an implementation benchmark or a proof of any surrounding protocol. Date: 2026-10-13.

## 1. The actual obligation

Let D_b be all byte strings of length at most the nonnegative integer b, including the empty string. Its size is sum_{j=0}^b 256^j. Let a combined quantum experiment, including honest generation, signing, verification, challenger work, and adversary work, make at most T calls to one shared function D_b -> {0,1}^256 on EVERY execution branch. Classical calls count as calls. Oracle-dependent initial state construction and preprocessing count too. An expected query bound alone is insufficient. Take T >= 1; the T=0 experiment requires no oracle simulation.

We seek equality of the final averaged state/output distribution, for every such experiment, with a uniformly random function. We do not seek a uniformly random full function table, an efficient classical simulation of arbitrary quantum computation, or an infinite-domain oracle. The secret sampled polynomial coefficients remain internal; revealing them is outside the experiment being simulated.

## 2. Injective byte-string encoding without a domain table

Write v(x) for the base-256 integer represented by x, with leading zero bytes permitted. For length l, set E(x)=2^(8l)+v(x). The l-th interval is [2^(8l),2^(8l+1)-1]; these intervals are disjoint. Therefore E is injective even for leading-zero strings and the empty string (E(empty)=1).

B=8b+1 bits suffice. Set d=max(B,256). Let m be the least power of two at least d, so d <= m < 2d, except equality at powers of two. We will construct a binary field with m-bit elements, use the B-bit integer E as its coefficient-basis vector padded with zeros, and use the first 256 field-coordinate bits for the reply. No integer-to-field reduction that could identify distinct inputs is performed.

A canonical quantum input representation is a length register plus a right-aligned 8b-bit payload with zero padding outside the indicated length. Copy the payload and toggle the sentinel bit 8l. The sentinel can be computed by testing each of the b+1 possible length values, reusing a small equality-test workspace. This costs O(B + (b+1)log(b+2)) elementary reversible gates and O(B+log(b+2)) temporary bits. The oracle's domain is the span of canonical encodings. Its extension on invalid encodings can be arbitrary and consistent; no random-function claim is made on them. All actual protocol serializations, including domain-separation prefixes, must fit this b.

## 3. Deterministic field tower; no hidden irreducible-polynomial search

Start K_0=F_2 and a_0=1. For i>=0 define

K_(i+1)=K_i[z_i]/(z_i^2+z_i+a_i), and a_(i+1)=a_i z_i.

Inductively [K_i:F_2]=2^i and Tr_(K_i/F_2)(a_i)=1. To see irreducibility: the map h(u)=u^2+u on a binary finite field has kernel {0,1}; its image has half the field's elements. The absolute trace of h(u) is zero by telescoping. The trace-zero set also has half the elements because trace(a_i)=1 proves the trace map is nonzero. Thus h(u)=a_i has no solution. The quadratic is irreducible. Its two roots are z_i and z_i+1, so the relative trace of a_i z_i is a_i. Trace transitivity proves the inductive trace-one assertion.

Choose i=log_2(m). This is an explicit deterministic representation of F_(2^m). The element a_i is the tensor-basis monomial z_0...z_(i-1). Construction needs no randomness, candidate modulus enumeration, factoring, or probabilistic success assumption. The tower has O(log m) recursively described levels; materializing its constants/basis and arithmetic circuit is charged below. A single degree-m polynomial basis is not required.

## 4. Uniform polynomial family and full uniform replies

Put k=2T. Sample a_0',...,a_(k-1)' independently uniformly from the m-bit field (km independent fair bits). Define P(u)=sum_(j=0)^(k-1) a_j' u^j and F(x)=pi(P(E(x))), where pi selects the first 256 coordinate bits.

For r distinct inputs with r<=min(k,|D_b|), the corresponding field points are distinct. The r by r Vandermonde submatrix on coefficients 0,...,r-1 is invertible; the remaining coefficients only translate the output vector. Hence (P(E(x_1)),...,P(E(x_r))) is uniformly distributed on K^r. Coordinate projection pi is a surjective F_2-linear map K -> F_2^256, with exactly 2^(m-256) preimages per reply. Thus the replies are independent, uniform FULL 256-bit strings. F is k-wise independent. This proof does not require k <= |K|: only the number r of distinct queried domain points is at most |K|.

This is unconditional, exact limited independence, not a computational PRF. The random key has km=2Tm bits. Nonuniform or correlated coefficients, hashing the encoding into fewer field points, or an unproved output map can destroy the conclusion.

## 5. Arithmetic is charged in bit gates

Addition in K is m XORs. At one tower level write X=x+yz and U=u+vz. With z^2=z+a, multiplication is

XU=(xu+a*yv)+(xv+yu+yv)z.

Use p=xu, q=yv, r=(x+y)(u+v). Then XU=(p+a*q)+(r+p)z. Three unrestricted lower-level products plus a fourth lower-level product by the PUBLIC constant a suffice. Charging even this constant multiplication as unrestricted gives C(n)<=4C(n/2)+O(n), C(1)=O(1), hence C(m)=O(m^2) Boolean gates. This deliberately avoids claiming a fast polynomial multiplication algorithm or treating a field operation as one bit gate. A circuit generator expands the recursion in O(m^2) time/description size. Constants can be materialized within that budget. Faster bounds would need their own algorithm and reversible analysis.

Compile an ordinary XOR/AND Boolean multiplication circuit into a reversible multiply-to-fresh-register circuit: retain each intermediate result, XOR-copy the product, then reverse the circuit. This uses O(m^2) NOT/CNOT/Toffoli gates and O(m^2) scratch bits, all cleared. No division, inversion, or modulus discovery is used in evaluation.

## 6. Reversible Horner oracle and resource accounting

Horner evaluation uses k-1 multiplications and O(k) additions. Keep the successive m-bit accumulators rather than overwriting them, and reuse the clean multiplier scratch for each multiplication. Compute E and all accumulators, XOR pi(final accumulator) into the 256-bit response register, and reverse the full computation. This implements exactly |x,y> -> |x,y XOR F(x)>, with all work registers cleared.

Per oracle call:

- Gates: O(k m^2 + (b+1)log(b+2)); all gates are ordinary bit/qubit gates, not unit-cost field operations.
- Clean quantum workspace beyond the caller's registers: O(km+m^2+B+log(b+2)). This includes Horner history and reusable multiplication scratch, but excludes a read-only coefficient key when held classically.
- Classical key storage/randomness: km bits. If the key is stored in qubits, include km additional qubits; it is still sampled in the computational basis, not exposed to the adversary.
- Uniform circuit generation/setup: O(km^2+(b+1)log(b+2)) time and circuit-description size, plus O(km) sampling time. The field representation itself is deterministic and fully charged inside this polynomial bound.

For an original non-oracle circuit of S gates and W qubits, one valid implementation has total O(S+km^2+(b+1)log(b+2)+T[km^2+(b+1)log(b+2)]) gates/setup work and W+O(km+m^2+B+log(b+2)) live quantum workspace, plus km classical key bits. With k=2T, the leading replacement work is O(T^2 m^2), not O(Tm^2). There is no exponential table in b. These are conservative upper bounds, not optimized constants. If a resource gate requires less key, time, or workspace than these bounds allow, this construction does not establish that gate.

The algorithm still runs on a quantum computer. The construction does not promise polynomial classical simulation of its state vector. Every additional honest function evaluation incurs its own polynomial-evaluation gates and contributes to the total query cap.

## 7. Exactness and quantifier scope

Zhandry's Fact 2, ECCC TR12-140, says that a quantum algorithm using at most q queries has identical behavior under a 2q-wise independent function and a random function. Source: https://eccc.weizmann.ac.il/report/2012/140/download/ , Section 2.2, printed page 5. This source was checked before saving this derivation; no outside-simulator proposal was inspected.

The underlying reason can also be seen directly. Treat the oracle entries as indicator variables delta_(x,y)=[F(x)=y]. A query matrix entry is linear in these variables. After T calls, amplitudes have degree at most T, and final density-matrix entries have degree at most 2T. Each monomial mentions at most 2T DISTINCT inputs. Its expectation is identical under 2T-wise independence and the uniform function distribution. Thus the averaged final density operator, and every final measurement distribution, agree exactly. Deferred measurements/purification cover adaptive classical branching and honest classical calls; treating each classical call as a quantum basis-state call gives the conservative 2T bound.

If only the adversary makes q calls and honest parties make c additional calls, Fact 2 applies safely with T=q+c, NOT T=q. A more economical mixed-query theorem may lower the required independence, but is not needed for this construction. A single fixed sampled key need not agree with a single random-function sample; equality is after averaging over the sampled internal key/oracle. Any other oracle-dependent advice, function-key revelation, or unbounded later calls requires a fresh theorem/budget, not an extension by assertion.

## 8. Three construction routes and the selected route

1. Deterministic binary quadratic tower (selected): exact uniform bit sampling and output projection, explicit arithmetic; degree rounds up to a power of two.
2. Randomly search for a degree-m irreducible binary polynomial: also viable with verified irreducibility tests and charged expected sampling/test cost, but a strict deterministic resource gate must account for unbounded rejection tails or a failure/abort branch. A preexisting modulus cannot silently be free.
3. Prime-field polynomial: possible with a sufficiently large prime, but prime generation and exact uniform 256-bit output conversion require explicit work; naive reduction modulo 2^256 is generally biased. No such assumptions are required by route 1.

The central issue is the simulator's quantified resource and query obligation, rather than choosing an apparently fast arithmetic syntax. The construction resolves it only for a finite, explicitly encoded domain and a worst-case total call cap.

## 9. Status of evidence

Manual derivation complete; the Vandermonde, trace, and reversible-compute arguments are supplied above. No formal proof checker was run. Toy controls should subsequently check tower arithmetic/trace and exhaustive limited-independence on small fields; such controls will test implementation errors and will not prove the universal statements. No surrounding paper, source, bound, prior receipt, or production artifact was edited.
