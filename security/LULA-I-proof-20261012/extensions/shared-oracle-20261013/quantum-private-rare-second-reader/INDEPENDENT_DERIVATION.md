# Independent source-alias stopped QROM private-hop derivation

Saved before reading `QUANTUM-PRIVATE-RARE-EVENT-DRAFT.md` or any new private-rare-event author report. This derivation uses the pinned source and the previously accepted conservative joint-private coupling only. It changes no published conservative statement.

**Status: MANUALLY_DERIVED_SCOPED_STOPPED_EVENT_LEMMA.** A classical environment/history-block domination proves the required support-mass estimate. It does not use the generally false inequality P rho P<=rho for a coherent projector. The construction remains a finite information-theoretic source-model argument, not an efficient reduction or a verified Rust proof.

## 1. Actual source calls and coupling

Pinned release `code/lula1/src/lib.rs` SHA256: `ac8e67f05af68dd8e1291c5909847f74103903fb7ffa2c70f500c6ec48f14210`. Its private calls at161–168 have raw forms

    D_K(A)=S16||zero48||A22||K16  (private address types5/6),
    M_P(t)=P16||S16||t.

The complete suffix t is not restricted to legitimate message lengths. In particular it includes root||m and counter||S when public calls alias. Work at each fixed nonzero S, with independently uniform K/P in N=2^128 and full256 independently sampled tables O0,F,J. O1 is O0 except it installs full F(A) at D_K(A) and full J(t) at M_P(t). These two private families are disjoint and injectively framed for nonzero S. Each raw basis input nominates at most one K or one P. This is the earlier exact full-output marginal coupling; prequeries are permitted, with all tables fixed before the first query.

REAL uses O1 on public/coherent calls and F/J-equivalent private derivations; continued IDEAL uses O0 on all public/coherent calls and independent F/J on private derivations. In continued IDEAL, K/P are unused by every operational response/channel. Their registers remain independent of its entire operative classical/quantum state, even with retained quantum memory, adaptive measured messages and previously completed signatures. Source-internal work is classical and atomic; private contents/timing, coherent signing, interruption and partial output are excluded. q counts initiated signing calls and Q bounds adversarial complete-output public-RO calls.

At every honest or final public I/E call, define an analytical source-alias flag **before** performing that call. Source at170–187,603–617 and697–700 gives exactly:

* I=R||S||root||m aliases M_P precisely when R=P.
* E=U||BE32(c)||S aliases M_P precisely when U_hi=P and U_lo=S. Every counter in a given outer loop has the same nominee U_hi; one alias test suffices before its first outer call.

Neither point can lie in D_K. Addressed public type0–4/7 source work lies outside both private families for nonzero S. Therefore setup, private derivations, type0–4/7 work and honest canonical-cache operations cause no stopped discrepancy. A counter overflow/noncompletion remains an absorbing nonwinning branch of the specified mathematical partial-service game; no new total-abort API is invented.

## 2. Shared stopped channels and their true continuation meaning

Define stopped REAL and stopped IDEAL to set a persistent terminal B flag and absorb **before the first source I/E alias**. Until B they retain exactly their respective ordinary public-oracle channels and source service outputs. They do not stop coherent adversarial queries at private points; those remain the only two-oracle difference. Their detectors/services are one common channel on every fixed environment and classical history: compute the same candidate input; stop if private-family membership holds; otherwise O1=O0 on that classical input. If an earlier public I output differs only through an alias, that branch was already stopped before the differing call. F/J accesses are identical.

This stopping is an analytical experiment, not a claimed production API. In each original process, the probability of ever encountering its first source alias is exactly its stopped B probability. On no-B paths, the stopped process and its own genuine original continuation are identical through the final verifier. Consequently

    Pr_REAL_original[B_alias] = Pr_REAL_stop[B],
    Pr_REAL_original[Win and not B_alias] = Pr_REAL_stop[W],

where W is the classical final winning outcome on an active/no-B branch. B and W are disjoint terminal classical records. No claim is made that REAL and IDEAL resume with the same semantics after an alias; they need not.

## 3. The needed domination is a classical block fact

The inaccessible environment E contains the sampled S,K,P,O0,F,J and all private graph/cache coins. Include in an unexposed record h every measured classical interaction/controller outcome, including internal deterministic source I/E points needed to annotate aliases. Measuring or recording genuinely classical values does not measure the adversary's retained quantum register. Different E,h values are orthogonal classical blocks.

For the j-th numbered adversarial query slot, pad terminated/short executions by common identity slots. Let rho_cont(j) be the unnormalized continued-IDEAL state at that slot, retaining E,h and the adversary's coherent query/work registers. The execution up to any history with no earlier source alias is unchanged by stopping. Thus the stopped-IDEAL active blocks obey the **literal block identity**

    rho_act(j) = sum_(E,h) a(E,h) |E,h><E,h| tensor rho_cont(E,h;j),

where a is1 exactly when that continued history is active at query j and has no earlier source alias; otherwise a=0. Numbering is by actual adversarial queries along each history. The stopped and continued schedules have the same prefix at each surviving history. Continued histories after an earlier alias are removed; they are not relabelled as surviving histories. Retained quantum memory can alter the rho_cont(E,h;j) blocks without invalidating this identity.

Because the deletion is of whole **classical environment/history blocks**, rho_act(j)<=rho_cont(j) in positive-semidefinite order on this full CQ state. Equivalently M_a commutes with this block-diagonal density operator, so M_a rho_cont M_a<=rho_cont. This is not a statement for arbitrary coherent postselection. Upon purification, use the copied E,h reference flags to compute the same unnormalized norm, rather than claiming a coherent-projector PSD inequality for the pure vector.

Let Pi_priv be the query-input projector onto D_K union M_P, controlled by E. Then

    Tr(Pi_priv rho_act(j)) <= Tr(Pi_priv rho_cont(j)) <= 1/N.

The last inequality is evaluated before conditioning on surviving histories: continued IDEAL's operative state is key-blind and each raw point nominates at most one independent key. A surviving normalized state need not retain uniform keys or private-point mass1/N. No such conditional assertion is used. Activation/termination can only decrease the unnormalized block contribution.

At an adaptive slot where histories perform different operations, preserve their classical controller blocks and postpone comparison to the next numbered query slot; common classical source/adversary channels between slots are contractive. Coherently controlled oracle use is one query and the operation counter is not used to dephase its query state. Finite channels/registers and padded query caps are explicit model hypotheses.

## 4. Purified stopped hybrid and shared terminal projectors

Use common dilations for all identical channels, with copied measurement/environment records. At an active public query the O1/O0 difference has norm at most2 and is supported only on Pi_priv. On an inactive block both slots are identity. Therefore its norm on the stopped IDEAL vector is at most2/sqrt(N) by §3. A REAL-prefix/IDEAL-prefix triangle telescoping with common inter-query channels gives, at the shared terminal record,

    ||psi_REAL_stop - psi_IDEAL_stop|| <= d,  d=2Q/sqrt(N).

The environments and references are retained in this norm. No private-source-service additive norm loss is present: every such channel is common after the pre-alias stopping rule. This is a vector-norm bound; a trace-distance bound alone would not justify squaring a rare-event probability this way.

For any common terminal projector Pi_T,

    sqrt(Pr_REAL_stop[T]) <= sqrt(Pr_IDEAL_stop[T])+d.

The same terminal B/W projectors are classical outcome flags in both stopped games. They do not compare different definitions of a transcript's winning predicate after an alias.

## 5. Exact scoped event bounds

Continued IDEAL has unused uniform P. Each initiated signing call contributes at most two classical nominations, irrespective of its outer grind length. The final verifier contributes two more. A union bound on continued histories gives

    b = min(1,(2q+2)/N),
    Pr_IDEAL_stop[B] <= b.

This is conservative; duplicate nominations or the outer lower-half condition can reduce the probability. The detector's mere stopped history need not remain key-blind. The probability statement is proved by embedding its first flag into the genuinely continued key-blind history, not by conditioning on no earlier flags.

Let p be any bound on the winning probability in the ordinary continued IDEAL/HJ game for the same q,Q, fixed nonzero S and exact final verifier. Surviving stopped winning blocks are a subset of its continued winning blocks, hence Pr_IDEAL_stop[W]<=p. Then

    Pr_REAL_original[B_alias] <= min(1,(d+sqrt(b))^2),
    Pr_REAL_original[Win and not B_alias] <= min(1,(d+sqrt(p))^2).

The sum of these separately bounded disjoint events is valid but repeats the same norm budget. A sharper direct bound uses the single shared projector Pi_(B or W):

    Pr_REAL_original[Win]
      <= Pr_REAL_stop[B or W]
      <= min(1,(d+sqrt(min(1,b+p)))^2).

This requires no event independence and no joint auxiliary advice. If p is instantiated by the existing ordinary HJ C/H/G/D7 sum, their bounds must retain the same nonzero-seed source marginal and their respective accepted query conventions. With uniformly sampled S, charge its zero branch once: add1/N to this fixed-nonzero expression before capping at1. Do not independently add old unconditional private charges.

The bounded final observer remains exactly source-specific: two final public I/E calls, then addressed public work. No exponential counter-loop factor is inserted because all E calls nominate the same P. No free adversarial classical hash calls are hidden in the final observer.

## 6. The false alternative and smallest control

For rho=|+><+| and P=|0><0|, P rho P<=rho is false: vector v=(1,-1) has v* rho v=0 but v*P rho P v=1/2. A proof that kills a coherent query branch by this assertion is invalid.

The valid support calculation deletes E,h blocks after classical source decisions. The accompanying exact rational control checks all16 masks on two hidden keys and two classical histories with nontrivial coherent/retained states. It demonstrates unnormalized support domination and also that normalization of a selected active set can raise private-point mass from1/N to1. These controls test the distinction; they do not replace the manual source/channel proof.

## 7. Limits and next review gate

The crucial hypothesis is the literal history-block embedding at each numbered query slot. It must be established from an actual classical stopping detector whose original good-prefix channels agree. It cannot be presumed for coherent service choice, coherent source detector outcomes, secret-dependent oracle registers, leaked analytical history, altered post-alias continuations or arbitrary time/interruption interfaces.

Within the declared source model, I find no obstruction to that embedding: I/E values are classical, source services are atomic, continued HJ ignores K/P operationally, and the exact typed raw forms permit pre-query stopping. The argument supplies an event-specific alternative, not a replacement of the published conservative hop without independent candidate review. I have not read the root rare-event candidate or new author lane at this save.
