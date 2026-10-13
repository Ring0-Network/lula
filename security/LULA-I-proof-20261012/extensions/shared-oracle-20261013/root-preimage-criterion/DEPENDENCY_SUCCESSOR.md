# Dependency-safe successor: root-preimage criterion

**MANUALLY_DERIVED_SOURCE_MODEL_CRITERION_OBSTRUCTION — dependency-safe successor, awaiting independent review.** This preserves the original `INDEPENDENT_DERIVATION.md`, SHA256 `e1e344cc9424136f74f86691ddcb0573b63f02cd974feb541f77d7367dcdae8f`. Its source framing, skeleton, query counts and Grover identity remain unchanged. This successor replaces the joint-completion numerical conclusion: it uses a union bound rather than needing a whole-preprocessing conditional-on-setup independence proof. The original stronger961/4800 constant is **not promoted** by this successor. The retained claim is strict success greater than1/5.

## 1. Common latent experiment for setup and attacker preparation

Fix the original source parameters and public seed S. Split the ordinary complete256-bit RO into the final top root-address restriction H and its entire outside restriction O_out. Define

    A*=Adrs(4,0,type2,kp0,height21,index0),
    H(L,R)=RO(S16||zero48||A*||L16||R16).

The source's canonical graph below the final root uses only O_out and private key coins. This is directly supported by `WotsC::pk`/chain/compression at239–262, `Subtree::build` at291–306 and lower `child_value` at486–495. Address height21/index0/type2/layer4 is only the last top-tree node; graph children at height20 and every other layer/type use other restrictions. Private type5/6 derivations are different address types and shorter102-byte words. No message-randomizer call is needed by KeyGen. Hence the canonical final pair

    P*=(L*,R*)

is a function of O_out and key coins, **not of H**. Define its latent root r=Tr128 H(P*) even if the actual KeyGen service later fails to complete. This definition is analytical; it gives no public key or continuation to the adversary on a failed-setup branch.

Let T be the event that every original top cached counter row has an accepted member in its unchanged C=2^32 counter range. KeyGen at512–540 has2^21 such rows, with distinct addresses. Its child graph contains no type7 values. Conditional on that graph, the rows' images are independent and the success probability per candidate is p_t. Thus

    Pr(T)=[1-(1-p_t)^C]^(2^21)>31/32.

The source's potential runtime/resource failures are not replaced by this formula; it applies to the existing mathematical partial-RO service with no operating-system/timing interface. Every T world returns the same canonical root r. In other worlds the service has no completing public-key response.

Define A as success of the six-stage attacker prefix algorithm with L=2^20 on the **latent** public pair(S,r). In a T world this is the attacker's actual public computation; outside T it is only an unobserved analysis extension. The extension is needed to place both events in one probability space and apply union accounting. It neither calls the actual failed service nor adds hidden retries.

Without conditioning on T, each attacker grind selects its own row without using that row's outputs: the outer52-byte row follows an inner49-byte query; bottom WOTS child derives from FORS; each subsequent WOTS child derives from lower-layer data. The prefix has not inspected the selected own type7 restriction before that stage, and r/canonical graph have no type7 dependency. Honest KeyGen may already have queried the same canonical top row; those hidden reads neither resample the table nor change its unconditional law. Their completion event T is deliberately **not conditioned on** in this calculation of A. The root-selected route may change which row is selected, but selects it from information outside that own restriction. Consequently each six-stage failure is bounded, conditional on the preceding successful virtual prefix, by its ordinary independent row failure. Union accounting gives

    Pr(A)>=1-(511/512)^L-4(1-p_l)^L-(1-p_t)^L
         >=1-6*(1023/1024)^L>31/32.

This unconditioned statement deliberately does **not** infer independence between A and T. They can inspect the same top type7 row. The original row-level conditional formula for a canonical top row can be true without serving as a complete proof of every earlier prefix distribution conditioned on all setup rows; no such product shortcut is needed here.

The same-space union bound now suffices:

    Pr(T and A)>=1-Pr(not T)-Pr(not A)>15/16.

No independence or product of unconditional marginals is used. Exact finite controls demonstrate that Pr(T)Pr(A) can exceed the actual joint probability even when both marginals are31/32.

## 2. Exact root-address residual law after a root-dependent prefix

The needed independence can be expressed as an exact generative disintegration. First sample key coins and O_out. These fix P*. Next sample a fresh full256 image Y at P*, put r=Tr128 Y, and sample independent uniform full256 images for every other pair in H. This is exactly an ordinary uniform H table jointly with the source canonical graph: P* was selected without querying H. Repetition of the canonical root call repeats Y and changes no residual law.

Let Sigma contain key coins, O_out, P*, Y and all deterministic public-prefix/control records. This is an inaccessible analysis environment, not advice supplied to the adversary. T is determined by type7 rows in O_out. The prefix A, its root-dependent route/direction, final computed V, all counters and public nodes are functions of O_out and r. They never query H: the top path stops at height20, the other addresses/layers/types differ, and its I/E words have lengths49/52 rather than118. Therefore all of T,A,V,direction are Sigma-measurable; Sigma reveals no residual H entry.

Conditioning on arbitrary Sigma blocks with T and A does not sample a preferred residual row, reject a root-candidate response or condition on root-search success. In each block the injective family is already fixed:

    f_Sigma(X)=(V,X), if the direction is0,
    f_Sigma(X)=(X,V), if the direction is1.

If P* lies in this family, its unique X has a guaranteed matching prefix and the N-1 other complete images remain independent uniform. If P* lies outside, all N complete images are independent uniform. Both cases retain the exact result

    Pr(M=1 | Sigma,T,A)=(1-1/N)^(N-1)>1/3.

The dependence of V/route on r is harmless because r is **the canonical image Y**, not residual table data. The source root comparison uses only its128-bit prefix; every residual full256 suffix remains present and can be coherently computed/uncomputed. The attacker does not know P*, Sigma or M and uses the same fixed T_G iterations in every successful public-prefix world.

This is precisely where a prohibited adaptive residual read would break the argument. If one first inspected several H rows and then selected V to maximize their target counts, the selected row would no longer have the claimed distribution. The negative toy control checks that failure. Our actual public prefix has no H call, so it makes no such selection.

## 3. Dependency-safe quantum lower bound

All source layout/query counts and the primary Eq8 amplitude-amplification identity are unchanged from the independent first derivation. Write N=2^128 and

    B=6*2^20+3217+1+3224=6297898,
    T_G=floor((2^64-B)/2).

Preprocessing uses at most6L+3217 full-hash calls, a marking phase uses two complete-output XOR calls, a measured-candidate certificate uses one, and the exact final verifier adds3224. Total calls under this conservative ledger are at most2^64. Source KeyGen is the honest challenge setup, separate from adversarial Q as in the existing model.

On M=1, the fixed-angle success is sin^2((2T_G+1)arcsin(1/sqrt(N)))>16/25. Averaging **conditional on Sigma,T,A** gives a root-search success greater than(1/3)*(16/25). Then average the good joint event:

    Pr(ordinary source-model forgery)
      > Pr(T and A)*(1/3)*(16/25)
      > (15/16)*(1/3)*(16/25)=1/5.

These multiplications are the chain rule after a uniform conditional bound, not an independence assumption for T and A. On not-T or not-A the attack returns no forgery; on a root hit it outputs its5720-byte skeleton with the found last sibling. q_s=0 and the one-byte message is fresh.

The statement is an ordinary-RO quantum-query lower bound for the fixed128-bit root. It refutes the literal tiny-failure threshold at this enormous query budget, while remaining consistent with conventional128-bit classical target-preimage work and square-root quantum search. No actual SHA search, practical exploit, physical-runtime statement, category certification, new parameters or paper/master edit is part of this successor.

## 4. Checks and remaining gate

`joint_control.py` checks the invalid-product example, union bound equality, root-dependent selection using only the canonical image/outside coin, per-Sigma single-mark distribution, and the negative residual-informed selector. It writes `JOINT-CHECKS.json`. The first `control.py`/`CHECKS.json` are preserved as preliminary controls; their961/4800 numeric field is historical and superseded for the joint-completion conclusion.

Independent review must still verify the source exclusion of every noncanonical H query during keygen/prefix construction and the finite source-model/refinement scope. No published full-security theorem is altered merely by this lower-bound investigation.
