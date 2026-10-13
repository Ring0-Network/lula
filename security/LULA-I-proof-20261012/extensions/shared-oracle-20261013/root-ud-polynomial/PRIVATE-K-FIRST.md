# Root independent source-specific private-K candidate

**PROVED candidate / OPEN independent source review.** Read pinned release lib.rs and PRIVATE-FIXED-H-REDUCTION.md before saving. No new peer private-K proof was read. Only the full random-oracle instantiation is considered. This does not assign a hardness value to literal SHA.

## 1. Exact source restriction

**PROVED.** At fixed nonzero public S, let DK be the valid type5/6 private-address language of raw102-byte words S16||zero48||A22||k16. Genuine source private-F calls evaluate its128-bit prefix. Independently sample a complete full256-bit map Ffull(A), an outside full raw oracle G, and all other coins including secret P. The private services return prefix Ffull(A), and the source simulator intercepts these calls rather than reading K or querying DK.

**PROVED candidate.** In REAL let b(k)=[k=K] for a uniform unknown K. For every syntactically valid DK query the full raw response is Ffull(A) if b(k)=1, else G(word); every other word returns G(word). In IDEAL take b identicallyzero while retaining the same private Ffull service. REAL then has exactly the joint law of a uniformly random raw oracle and its genuine private-F service. IDEAL has an independent raw oracle/private-F map. The unused random variable K need not be read by the simulator; only the Boolean challenger holds it. Lower output limbs at the selected private slice are independent sampled Ffull lower limbs, rather than zeros or duplicated prefixes.

## 2. No free hidden-marker calls or advice

**PROVED from byte geometry, subject to independent caller audit.** Public typed source calls use types0..4 or7, disjoint from valid private5/6. Honest PRF_msg remains REAL and has raw word P||S||m: its second16 bytes are nonzeroS, while DK haszero there. Honest H_msg inner/randomizer frames also have second16S; outer frames are52 bytes, shorter thanDK. Thus every honest public call avoidsDK for fixed nonzeroS. Source privateF calls are intercepted; they consume Ffull but no hidden-marker query. The public root/cache payload and signer outputs depend on Ffull and G, notK, before any A public-query dependence. Pre-key A public computations run after challenge and count in Q_A, preserving chronology and retained quantum memory.

**PROVED interface restriction.** Expose no seed/context bytes or file framing that contains K/P. Logical public cache payload is admissible because it is computed from Ffull and outside G. Source code must be simulated using the intercepted private interface, not executed with a placeholder K whose bytes accidentally reach a public frame. Partial failure is absorbing output0. These are exactly the source-game boundaries already reviewed; arbitrary secret-cache disclosure would defeat this lemma.

## 3. Boolean reduction and polynomial bound

**PROVED candidate.** Fixed independent Ffull/G pairs permit clean one-Boolean-query full-response completion, including all valid A values coherently. On invalid/outside words choose identical response branches; the inactive mask uses a plus-state Boolean response. Every A full raw-oracle query costs at most one b query. All source private/challenger work, independent tables, circuit generation, message bytes and storage remain separately charged. No quantum-controlled unknown oracle or second b query is assumed.

**CITED / PROVED.** Conditional on independent Ffull,G,P,S and local initial auxiliaries, Beals et al. acceptance probability is a polynomial degree<=2Q_A in the N Boolean b coordinates. Averaging over the uniform single marker gives p(1); the ideal allzero case gives p(0). The grid derivative estimate from root-ud-polynomial/INDEPENDENT-FIRST.md yields

`|PrREAL[Win|S]-PrFideal[Win|S]| <= min(1,4Q_A^2/(N-4Q_A^2))` if4Q_A^2<N, else1.

This is a source-specific hidden-key quantum PRF-hop envelope with classical private services; it does not establish coherent private-oracle PRF security. The bound is Q_A-independent of q only because all honest classical F work is genuinely supplied by marker-independent local services. It does not mean that work is free or that arbitrary private-key constructions admit this improvement.

## 4. Zero-seed and complete composition

**PROVED.** S=0 can create private/public raw aliases and is excluded above. An unconditional standalone gap is at most1/N+(1-1/N)*alpha_nonzero by triangle inequality over S, or min1 thereof. A newly derived whole-source nonzero-S composition may pay the seedzero branch once outside all terms. Do not insert the standalone1/N and then also subtract a previous seedzero allowance without a complete coupling review.

**OPEN.** Independent source audit and exact full-word controls are required before promotion. This candidate concerns only the K hop, not the P/randomizer hop, message coverage or public graph composition. Those may retain linear quantum or q-dependent losses. No original security level, category, signing capacity or minimal parameter repair is established by this note.
