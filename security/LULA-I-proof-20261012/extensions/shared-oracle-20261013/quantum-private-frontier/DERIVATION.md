# Independent quantum joint-private-input frontier

Saved from the pinned source before any new quantum-private author report. This is an elementary state/channel-distance derivation, not a borrowed classical literal-guess argument. Status: MANUALLY_PROVED for the finite classical-service/coherent-RO model below; full QROM signature security remains OPEN.

## Source and finite experiment

Library SHA256 `ac8e67f05af68dd8e1291c5909847f74103903fb7ffa2c70f500c6ec48f14210`. Source 161–168 derives secrets as Tr16 SHA(B(S)||Addr||K) and message randomness as Tr16 SHA(P||S||m). Source 170–187 computes public I/E inputs; sign 601–617 uses one R and U per initiated call and grinds only its outer counter. Final verification 697–700 likewise uses one I and one E. Source secret/public seed fields are 104–105/102; keygen 503–505 copies the three components from the caller's 48-byte seed. Independent uniform entropy is a game assumption, not enforced by that copying operation.

ASSUMED model: uniform independent K,P,S in {0,1}^128; a classical fixed-parameter keygen/signing service; at most q initiated atomic signing calls on adaptively chosen **classical** messages; at most Q coherent queries to one ordinary complete-output RO; one final classical signature verification; no coherent signing oracle, private memory/cache/seed disclosure, compression-function access, timing or interrupted-call feedback. Only completed signatures are returned. Noncompletion is an absorbing nonwinning outcome. This is a mathematical partial-service channel, not an implemented overflow-return API.

Choose a finite input universe D of raw byte strings and an injective fixed register encoding. It must contain every allowed raw coherent input and every honest input relevant to this bounded experiment. In particular, a length cap L must exceed the largest addressed source string (598 bytes for the 32-node endpoint compressor), and allowed message lengths must satisfy 48+|m|<=L. Oracle action is the standard full256 XOR unitary `U_O|x,z>=|x,z xor O(x)>`. Domain restrictions, padding conventions and any invalid-register behavior are fixed independently of K/P. Arbitrary superpositions and ancillary entanglement are allowed. There is no materialization/efficiency claim for these finite tables or the enormous source service.

For fixed S!=0 define disjoint private families:

    D_K = { S16 || zero48 || A22 || K16 : A has source private type5/6 },
    M_P = { P16 || S16 || m : this raw point is in D }.

The first family has 102-byte strings. Full encoded address A, not a source-language alias, indexes F. The second indexes J by the entire suffix, including suffixes longer than an allowed signing message: an inner public point can be M_P(root||m), and an outer point can be M_P(counter||S). Those auxiliary J rows are sampled as well. The typed headers and S!=0 make these two families disjoint. Each raw input belongs to at most one eligibility class and nominates at most one K or one P. Thus for every fixed input x,

    Pr_(K,P)[x in D_K union M_P] <= 1/N,  N=2^128.

## Full256 coupling with correct marginals

PROVED: sample independent uniform full256 tables O_0, F(A), J(m), and uniform K/P. Define O_1 to equal F(A) at the unique D_K point for A, J(m) at its unique M_P point for m, and O_0 elsewhere. For fixed K/P/S!=0 these points are disjoint and injective, so O_1 is itself an ordinary uniform full256 RO. Its distribution is independent of K/P even though its coupling to O_0 uses them. REAL uses O_1 for all actual source calls; IDEAL uses F/J for private derivations and O_0 for public/coherent calls. The entire full256 private values are coupled, including unreturned suffixes; truncated source responses alone do not define a correct quantum oracle.

Pre-key queries are allowed: sample coins/tables at time zero and withhold public disclosure. This gives the correct original marginal and never overwrites a past real response. After a divergence, both processes continue according to their own genuine channels; no analytical flag changes IDEAL answers, stopping or disclosed values. In the continued IDEAL, K/P are unused except in the external coupling, and remain independent of its entire classical/quantum state conditional on S and the ideal tables.

## One coherent query bound

PROVED elementary lemma: for any pure query state psi, including an arbitrary ancilla, let mu be its squared input-register mass on D_K union M_P. Outside those inputs U_1=U_0; on them the difference of two unitaries has operator norm at most2. Hence

    || (U_1-U_0) psi || <= 2 sqrt(mu).

The pure-state trace distance is at most that vector norm. The same bound follows for a mixed state by purification. At an IDEAL query, unused uniform K/P imply `E[mu] <= 1/N`, even when the quantum state depends on prior O_0 answers, completed F/J signatures, adaptive measurements and message choices. Convexity of trace distance and Cauchy–Schwarz give the averaged one-query channel discrepancy

    D(U_1 rho_ID U_1*, U_0 rho_ID U_0*) <= 2/sqrt(N).

No assertion is made that a REAL state still has uniform hidden-key query weight, or that measuring a quantum query yields only one classical trial. The bound deliberately evaluates the comparison on the unused-key IDEAL state.

## Honest classical service calls are not Q coherent calls

PROVED from source: privatized secret accesses agree exactly because O_1(D_K(A))=F(A) and O_1(M_P(m))=J(m). On S!=0 all honest addressed public type0–4/7 calls are outside both private families. Keygen therefore agrees without an extra private-input discrepancy, even though it may perform enormous internal work.

A signing request has only two possible **public** private-family nominations in its IDEAL computation:

1. Inner I=R||S||root||m belongs to M_P only if R=P.
2. Every outer E=U||BE32(c)||S belongs to M_P only if U[0:16]=P and U[16:32]=S. All counters nominate the same first128 bits of U. No counter-loop multiplier is needed.

Neither can belong to D_K. These two literal P candidates are functions of the ideal tables and the measured classical message, independent of unused P. The probability that either is P is at most2/N. If neither nomination hits, the entire REAL and IDEAL signing handler agrees on that input/world, including completed bytes and noncompletion. If the inner nomination hits, possible later REAL divergence need not be analyzed: that handler branch is already charged.

Because the service input/output is classical, the key/world/message register decomposition is block diagonal. On identical branches the two output channels coincide; on bad branches their trace distance is at most1. The averaged **classical handler** discrepancy on its IDEAL input is therefore at most2/N, rather than a square-root loss. The untouched adversarial quantum memory may be arbitrarily entangled with the classical message; this CQ decomposition still applies after the message register is measured. A coherent signing oracle would invalidate this linear charge.

The one final classical verifier has arbitrary transmitted R,c but similarly adds at most two unused-P nominations, so its discrepancy is at most2/N. Classical adversarial computations of the hash must consume its Q oracle calls; they are not free service invocations. Repeated nominations reduce the actual discrepancy. The q bound counts initiated attempts; unlimited retryable/interrupted attempts are a different experiment.

## Adaptive channel telescoping

PROVED: include the secret coins and sampled tables in a classical inaccessible environment register. At an interaction step, CPTP contraction yields

    D(rho_REAL_next,rho_ID_next)
      <= D(rho_REAL,rho_ID)
       + D(T_REAL(rho_ID),T_ID(rho_ID)).

Thus every local discrepancy is evaluated on the continued IDEAL state, where keys remain unused. For adaptive classical scheduling, decompose each step over its measured public-history blocks. Convexity gives at most `2 p_query/sqrt(N) + 2 p_sign/N` on that step, where p_query/p_sign are its IDEAL probabilities of activating those operations. The pathwise caps imply the sums of those probabilities are at most Q and q. This avoids applying a square-root bound to a randomly active history block and inadvertently charging its activation probability as sqrt(p). Controlled coherent oracle use counts as one quantum slot; coherent signing/service choice is excluded. Unused and post-noncompletion slots act identically. Classical scheduling/measurements and identical setup transitions cause no extra loss. Combine the per-query, service and final-check discrepancies:

    fixed S!=0:
    |Pr_REAL[Win]-Pr_ID[Win]|
       <= min(1, 2 Q/sqrt(N) + (2q+2)/N).

For uniform S, handle S=0 separately: REAL must keep its actual ordinary shared oracle, including all overlaps. Independent F/J images at overlapping REAL points would be wrong. This branch may be coupled arbitrarily and costs at most Pr[S=0]=1/N. Therefore the complete stated finite quantum-private hop is

    Delta_joint_quantum <= min(1, 2 Q/sqrt(N) + (2q+3)/N).

The constants are conservative and not claimed optimal. This is a distance bound, not a quantum forgery classification or a QROM SPR theorem. The term linear in Q/sqrt(N) is precisely why the classical Q/N literal-guess term cannot be copied into QROM.

## Limits and smallest missing bridges

PROVED only under the model: finite-register coherent public RO plus classical atomic service, correct full-output coupling, ideal unused-key invariance and CQ honest-call transitions. If source internal query transcript/counters, in-flight state, seed-bearing snapshots or coherent service requests are exposed, the channel definitions and budgets must be replaced. A generic computational/PPT simulation of the full source is not supplied; no infinite-query-register limiting argument is silently used.

OPEN for the signature goal: quantum FORS adaptive coverage, hidden-value acquisition/disclosure, chosen-address graph target collisions, canonical digest collisions, composition with those terms, QROM source refinement, concrete fixed-SHA justification and a complete resource-security interpretation. None follows from this one hop. The finite controls to accompany this derivation test the state-distance inequality and refute transplanting a classical guess count; they cannot prove full QROM security.
