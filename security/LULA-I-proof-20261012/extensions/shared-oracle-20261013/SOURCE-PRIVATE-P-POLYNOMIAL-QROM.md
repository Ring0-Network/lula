# Source-specific mixed classical/quantum private-P hop

**PROVED — manual finite-random-oracle one-sided source lemma.** Root and outside-field-check saved separate derivations before peer inspection. This combines a decision-polynomial gap with a distinct stopped classical-nomination probability. It is not a general trace-distance assertion or a full-security/category certificate.

## 1. Source experiment and full private-P overlay

**ASSUMED — exact interface.** Fix nonzero publicS and N=2^128; privateK is already idealized. Keep mandatory source setup, publicS/pk withheld during pre-keyA, at mostq initiated classical atomic signing services, honest logical caches/restores, no private bytes/timing/coherent signing/interrupted buffers, and one strict final verifier. All counter searches have2^32 distinct attempts, with exhaustion/noncompletion absorbing and nonwinning. Every Boolean interpolation game enforces pathwiseQ_A public-A queries andq initiated requests, including pre-key, even on tables with more thanone marker.

**PROVED.** Independently sample full rawG, full256 randomizer mapJfull(m) for EVERY eligible suffixm, other private source coins and an inaccessible uniformP. On raw p16||S16||m returnJfull(m) if b(p)=1, elseG(word); elsewhere returnG. Private randomizers always return prefixJfull(M). Singleton b=e_P has the faithful REAL-P full-oracle/private-service law; zero b has the ideal independent law. The same full lower limbs and literal suffixes are retained; an inner alias usesJfull(root||M), notJfull(M). Initial G/Jfull/auxiliary state has the SAME joint law and is marker-independent in both experiments. Multi-marker oracle functions are persistent physical functions but need not have ordinary RO law.

## 2. Blind honest-source intermediate

**PROVED.** In BLIND, all A queries use the overlay but every honest public source hash usesG, retaining privateJfull and the same other source services. In ZERO, both A and honest public queries useG. Honest typed hashes startS||zero48 and cannot enter the private-P language atS!=0. An honest inner word nominatesR, while an outer word can alias only if bothU[0:16]=P andU[16:32]=S. All its counters share the sameU. Counting Ufirst=P without the second-half test is a conservative overcount. Setup nominates noP. At mostC=2q+2 nominees cover all initiated source requests and final verification.

Faithful REAL and BLIND agree in their complete views until the first actual honest/public aliasB; private calls and every prior raw call agree. The proof-side stop occurs before a potentially differing public reply and exposes no flag toA. This first-stop channel equality bounds REAL winning probability by BLIND winning probability plus its first-alias probability. It does not claim BLIND's quantum state is P-independent.

## 3. Blind decision comparison

**PROVED / CITED.** For fixed common G/Jfull and local auxiliaries, all BLIND honest services and its final Win decision are marker-independent channel descriptions, even though their arguments depend on past counted replies. One clean Boolean query simulates each full overlay response, with lower limbs/outside branches retained. Beals acceptance degree and weight symmetrization give degree<=2Q_A and normalized integer-grid values. The derivative proof in QUANTUM-UD-POLYNOMIAL-RO.md gives

`|Pr_BLIND[Win]-Pr_ZERO[Win]| <= v(Q_A,n)`

where v=min(1,4Q_A^2/(N-4Q_A^2)) for4Q_A^2<N andv=1 otherwise. AtQ_A=0 it iszero. There is no1-1/N prefactor: this compares a uniform singleton marker withzero, rather than iid/planted UD fields. Final BLIND verification readsG, not the marker, so no extraQ_A+1 query is added here. All honest/local work, messages, huge tables, circuit and storage costs remain charged separately.

## 4. Separate stopped classical-nomination bound

**PROVED — common channel argument.** Stop BLIND/ ZERO immediately before the first actual measured honest public aliasB defined in section2, recording an absorbingB. In particular an outer alias requires BOTH U[0:16]=P and U[16:32]=S. Their honest service/detection channels are the SAME, withP only in an inaccessible sampled environment. Their only discrepancy is A's coherent overlay query. The stopped REAL source agrees with stopped BLIND through the firstB. Counting every outer Ufirst=P nomination without its second-half condition is used only to upper-bound the ZERO baseline probability; it does not redefine the stopped event or its exact source equality.

In the unflagged ZERO continuationP is unused and independent of the entire source/A state, conditional on common G/Jfull/other environment. Its at mostC adaptive nominees give Pr[B]<=min(1,C/N). The active stopped ZERO physical CQ state deletes complete dephased environment/history blocks of that unflagged prefix; retained query memory within blocks is arbitrary. Unnormalized deletion cannot increase averaged private-support mass, so it is at most1/N. This does NOT assert normalized survivingP is uniform, independence of nominees in BLIND, or pure-stateP*rho*P<=rho.

Use common stopped purifications and invariant-plus padding forQ_A query slots. Each full-output overlay discrepancy has squared norm<=4/N; telescoping gives total vector norm<=2Q_A/sqrt(N). Apply the SAME terminalB projector, whose baseline norm is at mostsqrt(min(1,C/N)). Thus

`Pr_REAL[firstB] <= min(1,(2Q_A+sqrt(min(N,C)))^2/N)`.

The detector is key-dependent and common to these two channels; it is not a terminal test inserted into the polynomial proof. The latter applies only to the separate marker-independent BLIND Win bit.

## 5. One-sided source inequality and scope

**PROVED.** Let a_P=min(1,v(Q_A,n)+min(1,(2Q_A+sqrt(min(N,2q+2)))^2/N)). Then

`Pr_SrcFideal_REALP[Win|S] <= Pr_SrcFJideal[Win|S]+a_P`.

This is the direction needed for full winning-probability composition. ChargeS=0 once outside a newly derived complete source composition, not independently in every private hop. No coherent-signing or arbitrary secret-cache interface is covered. The newly proposed simultaneous classical ledger is unrelated and remains unpromoted.

**COMPUTED — independent finite controls.** outside-field-check/private-p-polynomial/controls.py tests9 unique/zero polynomial examples,2304 full-response Fourier columns,34 unnormalized-block/survival controls, six one-query adaptive nomination cases,256 shared-counter nominees andS=0/free-advice/hidden-tester negatives. Root and peer firsts are preserved. These are finite discriminators, not execution of LULA, an attack, efficient large-table generation or checked source/game declarations.

**OPEN.** Final subject acceptance and an independently checked complete quantitative composition are required before replacing any historical full source bound. Literal SHA hardness, adequate original level/category/capacity and successful smallest parameter repair are not established by this component. No manuscript/source/timing change is made.
