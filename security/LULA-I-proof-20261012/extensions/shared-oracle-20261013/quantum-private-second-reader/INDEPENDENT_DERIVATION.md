# Independent QROM private-input hop derivation

**PROVED (independence receipt).** Saved before reading `quantum-private-frontier/DERIVATION.md` or its new controls. I first re-read the frozen release encoding and signing sites. The prior classical joint-hop proof is known from my earlier review; no new quantum author argument was used here.

## 1. Fixed source and finite quantum interface

**COMPUTED.** Source `publications/LULA-I/release/code/lula1/src/lib.rs` SHA-256 is `ac8e67f05af68dd8e1291c5909847f74103903fb7ffa2c70f500c6ec48f14210`. Addresses are fixed 22-byte encodings (69-98). Private calls are at 161-168; public I/E calls at 170-187 and 603-610. Honest typed calls of types 0,1,2,3,4,7 cannot be private type-5/type-6 calls by their full headers.

**ASSUMED (scope).** One fixed single-root source game, independent uniform 128-bit K,P,S, ordinary full-output 256-bit O, at most Q_q coherent public-O calls, q initiated classical signing requests and one final classical verifier. Snapshot/restore handles are key-blind and honest; no secret-bearing objects, cache/timing/hash-call transcript, quantum signing or compression-function oracle. Honest operations are atomic partial computations: noncompletion produces no further public response or winning completion. No normalization on successful setup is made.

**ASSUMED (register).** The adversary's raw query alphabet is any fixed finite set of byte strings represented injectively with explicit length and canonical padding. Use a 256-bit XOR output register. Invalid encodings have one common fixed action in both games and cannot count as hidden points. Honest classical calls can be evaluated on the same full byte-string oracle; a finite maximum classical message length may be declared if a fully finite global table representation is wanted. No two different byte strings are merged by the encoding. There is no efficiency claim for exposing/sampling full random tables.

## 2. One joint REAL/IDEAL latent-table coupling

**PROVED (nonzero seed).** Fix S != zero16. Let B=S||zero48,

    D_K = { B||A||K : A is a valid type-5/type-6 address },
    M_P = { P||S||m : m is any message byte string }.

D_K strings have bytes16..31 zero; M_P strings have bytes16..31 S. The families are disjoint. Each raw point can nominate at most one K or P candidate. Its labels are injective within its family. This is one shared raw oracle, not two independently declared oracle routines.

**PROVED (tables and full images).** Sample independent full-image F(A),J(m),O_0 tables and the keys. Set O_1(x)=F(A) on D_K, J(m) on M_P, and O_0(x) elsewhere. Conditional on fixed K,P,S this is an ordinary full 256-bit random oracle: it replaces independent entries at disjoint injective labeled points by independent full uniform images. In REAL, private source calls use O_1 and hence F/J; honest public and adversarial calls use O_1. In IDEAL, private calls use F/J while honest public and adversarial calls use O_0. Repeated labels and raw points are consistent; no answered point is overwritten later. Full tails matter because quantum/public queries return all 256 bits even though source private calls use only the first 128.

**PROVED (initial environment).** Keep the sampled tuple r=(K,P,S,F,J,O_0,adversarial coins) as a classical inaccessible environment register in both experiments. Initial states are identical on that enlarged space. Oracle behavior differs by controlled channels using r. Including r in the distance is conservative: discarding it cannot increase trace distance. Do not replace the REAL underlying function in the environment by an independent label in a way that creates an initial distance.

## 3. Ideal hidden-query mass

**PROVED (ideal noninterference).** For every fixed nonzero S, IDEAL source/public operations never inspect K or P. F/J are indexed by public addresses/messages, O_0 is independent, and handles are key-blind. This remains true for quantum public queries and classical messages chosen adaptively by measuring the adversary's current quantum state. Consequently the entire ideal prefix state is independent of K,P conditional on all other latent tables/coins, without conditioning on any hidden hit or its absence.

Let Pi_(K,P) project the query input onto D_K union M_P. For any ideal prequery density operator rho,

    E_(K,P) Tr(Pi_(K,P) rho) <= 1/N, N=2^128.

**PROVED (one rather than two).** For each raw query basis string x, either it identifies one literal K candidate, one literal P candidate, or neither. Their second-half languages are disjoint. Average membership of x is therefore at most 1/N, not 2/N. Summing over the input distribution proves the bound for an entangled query/work/output state. Direct sum branches for malformed encodings contribute zero. The huge address/message namespace is not a multiplier because the raw input fixes its label and its one key candidate.

**PROVED (quantum difference).** U_1 and U_0 agree outside the hidden-input subspace. For a pure ideal query state psi including work/output registers,

    ||(U_1-U_0)psi||_2 <= 2 ||Pi_(K,P)psi||_2.

After purification this bounds mixed-state channel trace distance by 2 sqrt(Tr(Pi rho)). Average over the inaccessible classical key blocks and use Jensen/Cauchy-Schwarz:

    D((U_1 rho U_1^dagger),(U_0 rho U_0^dagger))
      <= 2 sqrt(E Tr(Pi rho)) <= 2/sqrt(N),

where D denotes one-half trace norm on the enlarged classical-environment/quantum-adversary state. The state psi used on the right is the ideal prefix, not a real state assumed to have unchanged key posterior.

## 4. Honest classical handler distance

**PROVED (source nominees).** At one initiated atomic sign(m), the ideal execution uses one R prefix and one U prefix:

    I = R||S||root||m,
    E_c = U||BE32(c)||S, with fixed U for the entire search.

I can enter M_P only when R=P. Any E_c can enter M_P only when U[0:16]=P and U[16:32]=S. Thus the entire handler nominates at most two P values, R and U[0:16]. Millions of private metadata/tree hashes and potentially all 2^32 distinct outer counters do not add P candidates. Other typed public hashes are outside both private families. Final verification nominates at most two P values in exactly the same way. Setup uses typed hashes only and adds none.

**PROVED (classical CQ condition).** A signing request message is a classical register: its interface measures/dephases the submitted message and returns a classical completed signature, not a coherent signing superposition. Conditional on the classical request and other latent tables, the ideal nominations are independent of P. Outside their membership event the real and ideal handler execute the same function at every call and have the same completion behavior/output. Therefore for an ideal input with classical request,

    D(H_1(rho),H_0(rho)) <= Pr_ideal[P is nominated] <= 2/N.

This is a probability contribution, not 2/sqrt(N). The real suffix after this handler may be quantum, but trace-distance contractivity still applies. An adaptive classical message may depend on ideal public quantum-query outcomes; IDEAL key noninterference is what permits the nomination bound. No claim about the surviving REAL posterior is needed. A message-coherent signing interface would require a different bound and is expressly excluded.

**PROVED (partial semantics).** A first possible difference in a nonterminating search is already covered by one of those same ideal nominations. If neither nomination hits, all public source evaluations agree, so completion/noncompletion agrees even over every finite prefix. One can prove the channel bound with finite-prefix stopped semantics and take the partial-operation limit; this adds no exhaustion-return API or free retries. q counts initiated requests, including a pending absorbing noncompletion.

## 5. Correct product/channel telescoping

**PROVED.** Pad the interaction to fixed bounded query/request slots, including skipped slots and common key-blind handles. Let T_1,i and T_0,i be the corresponding real and ideal CPTP channels, including the common adversary operation. The telescoping identity uses ideal prefixes and real suffixes:

    T_1,L...T_1,1(rho)-T_0,L...T_0,1(rho)
      = sum_i T_1,L...T_1,i+1 (T_1,i-T_0,i)
                 T_0,i-1...T_0,1(rho).

Every prefix argument of (T_1,i-T_0,i) is IDEAL and key-independent. Every suffix is contractive. It is not legitimate to evaluate differences on arbitrary partly REAL states and then cite IDEAL key independence. At most Q_q coherent slots contribute 2/sqrt(N) each; q classical signing handlers plus one classical final handler contribute 2/N each. Thus for fixed nonzero S,

    D(REAL_final,IDEAL_final)
      <= min(1, 2 Q_q/sqrt(N) + (2q+2)/N).

**PROVED (uniform seed).** Preserve the true shared-RO REAL marginal when S=0 and assign that branch distance at most one. Averaging adds Pr[S=0]=1/N, giving

    Delta_joint,Q <= min(1, 2 Q_q*2^-64 + (2q+3)*2^-128).

Any final winning-event probability difference is at most this state distance by measurement contractivity. This is a private-input joint-hop bound only, not full quantum signer security. The factor2 is the local oracle-difference norm and no unproved generic substitution Q -> Q^2 is used. A larger conservative factor can also be valid, but a smaller claim needs its own proof.

## 6. Needed discriminators and review gate

**PROVED (scope counterexamples to test).** A coherent, undephased honest request can have a square-root-scale state change on a rare hidden branch, so the classical probability-only handler charge cannot be reused for quantum signing. Conditioning on earlier no-hit events changes the hidden-key posterior. Programming only an output prefix cannot claim full-image consistency. Reversing telescoping orientation changes the prefix state and can remove the very independence used in the query-mass estimate.

**OPEN (scope beyond this save point).** Independently review the author's concrete state-distance convention, telescope orientation, classical-handler implementation, finite register encoding and full-image sampler. No efficient oracle simulator, standard-model quantum PRF theorem, complete QROM advantage bound, successful-setup normalization, or category certification follows from this lemma. Finite controls to be saved here validate those mathematical distinctions only.

**Status: INDEPENDENT_QUANTUM_PRIVATE_HOP_SAVED_BEFORE_AUTHOR_READ.**
