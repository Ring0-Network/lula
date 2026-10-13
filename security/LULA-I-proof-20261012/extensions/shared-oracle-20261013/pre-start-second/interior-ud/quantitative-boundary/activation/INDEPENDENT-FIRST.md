# Independent activation law and query-scale thresholds

**COMPUTED — first-save provenance.** This file is saved before reading any new activation peer derivation or the old direct-H theorem for this task. It rederives namespace counts from `release/code/lula1/src/bin/lula1_driver_original.rs:9–20`, plus release lib.rs's address/chain/tree loops. The prior coarse arithmetic is known and may be compared, but it is not used instead of source geometry. Source release lib.rs is pinned to `ac8e67f05af68dd8e1291c5909847f74103903fb7ffa2c70f500c6ec48f14210`. Only analysis/arithmetic is permitted; prior firsts/receipts and source/core files are preserved.

## 1. Exact activation from the source

**COMPUTED — geometry.** Heights are (5,5,5,5,21), widths (16,16,16,16,256), chain counts (32,32,32,32,16), and real FORS trees17 with512 leaves. Put K=2^41+2^36+2^31+2^26 and K_top=2^21. The source's WOTS nonterminal positions are p=0,...,14 for the lower four layers, and p=0,...,254 for the top. A 55-bit selector has M=2^55 equally likely bit strings. FORS secret coordinates, WOTS p=0 coordinates and invalid/dummy selectors are inactive in every UD hop.

**PROVED — active labels in hop r.** Hop r, 0<=r<=253, invokes its source program only on a WOTS selector with p>r. The exact number is

A_r = 32 K max(14-r,0) + 16 K_top (254-r),

and the selector activation probability is a_r=A_r/M. For 0<=r<=13 both lower and top chains contribute. For 14<=r<=253 only top chains contribute. A_253=16*2^21=33,554,432, so a_253=2^-30. If B2 locally fails at S=0 before invoking source A, the actual source-execution probability is a_r(1-2^-128); stage-one target queries still occur on every selector because p=1 syntax includes inactive/dummy challenges. Do not confuse target-query probability1 with source-execution probability a_r.

**COMPUTED — summed position multiplicity.** Summing the active-label counts over all254 hops counts each WOTS coordinate p exactly p times:

P_sum = sum_r A_r = 32 K*(1+...+14)+16 K_top*(1+...+254)
      =3360 K+518160 K_top
      =7,628,143,271,608,320.

Hence sum_r a_r=P_sum/2^55, rather than254. FORS contributes no UD multiplicity. This is an exact combinatorial source count, not an assumption about hardness.

## 2. Lawful advantage weighting before any random-function lemma

**PROVED — fixed-family signed decomposition.** For each active label ell and hop r, fix that label before the public parameter and let d_(ell,r) be the signed real-minus-random output-bit gap of its ordinary one-target UD program. Let epsilon_(ell,r)=abs(d_(ell,r)); this is an actual fixed-family advantage at that program's actual resources. Inactive programs output0 in both branches. Therefore the constructed random-selector program has

delta_r = abs((1/M) sum_(ell active at r) d_(ell,r))
        <= (1/M) sum_(ell active at r) epsilon_(ell,r)
        <= a_r epsilon_r_max,

where epsilon_r_max is any common upper bound on those fixed-label program advantages. No random-Th premise, scalar security substitution, independence between gaps or triangle equality is used. The bound delta_r<=a_r is unconditional; the nonzero-source skip also gives the sharper trivial delta_r<=a_r(1-2^-128). Actual signed cancellation can make delta_r smaller.

**PROVED — weighted successor.** Keeping the ordinary PRE program's success pi_PRE symbolic, the reviewed manual event inequality can consequently be bounded by

Pr[Win AND H_final AND S!=0]
 <= min(1, M*pi_PRE + sum_r sum_(ell active at r) epsilon_(ell,r)).

If the SAME resource-suitable bound epsilon applies to every fixed-label active program, this becomes min(1,M*pi_PRE+P_sum*epsilon). This is a lawful weighted upper bound on constructed advantages BEFORE adopting any generic random-function formula. It is not a claim that the actual sum equals P_sum*epsilon or cannot admit a better joint/signed argument.

## 3. Conditional hypothetical envelopes and exact rational thresholds

**ASSUMED — arithmetic-only substitution.** To compare coarse envelopes, suppose epsilon<=min(1,12Q/2^64), with Q a charged constructed-adversary oracle budget. HK22's random-Th Lemma3 applicability to the actual fixed h/full same-h interface is not asserted here. PRE is optimistically set to zero solely for a diagnostic of the UD term. The uniform254 substitution gives E_uniform(Q)=min(1,(381/64)Q) in its linear regime. Activation weighting gives E_active(Q)=min(1,(682009155/137438953472)Q) in its linear regime. Thresholds below are thresholds of these hypothetical sufficient expressions, never attack work factors or security bits.

**PROVED — constant-probability and cap crossings.** For c=1/2, uniform Q*=32/381 and activation-aware Q*=68719476736/682009155. For c=1, uniform Q*=64/381 and activation-aware Q*=137438953472/682009155. The latter values are about100.7603435 and201.520687; exact fractions are authoritative. For integer effective Q, uniform first crosses both at1; activation first crosses1/2 at101 and1 at202. The formulas use the linear regime, where individual12Q/2^64 is far below1 at these thresholds.

**PROVED — source-global budget versus target-only proposal.** Reviewed global complete-h cap for one active program is Q_B=Q_A+9,007,240,159,690,751+q H_mode+3224+254, with H_hot=21,474,918,570 and H_absent_cache=34,330,460,329. Source setup alone exceeds both query-scale thresholds, so no nonnegative Q_A/q can make these global-budget envelopes nontrivial. A proposed random-full-oracle target-only lift could instead give Q_target<=Q_A+1, without dropping actual source time/storage. Under that additional unproved lift, the activation half-probability crossing occurs at Q_A*=68037467581/682009155 and its cap crossing at136756944317/682009155; first integer Q_A crossings are100 and201. The uniform crossing is already passed at Q_A=0 because the final selected verifier call contributes1. Target-only accounting is a separate coherent raw-oracle/lower-limb/outside-simulation theorem, not a property of the fixed h algorithm.

**COMPUTED — requested rows.** At Q_A=2^32 and2^64 and each q=2^24,2^30,2^38,2^40,2^41,2^44,2^50,2^64, both hot and absent-cache global budgets exceed the activation cap threshold. All32 activation-aware hypothetical aggregate cells therefore equal1 even with PRE optimistically zero. This weaker diagnostic must not be used to declare an attack, actual hardening failure, or impossibility of a sharper activation-aware/signed/joint analysis.

## 4. Direct final-hidden event comparison to verify next

**ASSUMED — supplied comparison subject, not yet read in this task.** The parent supplies the current reviewed nonzero final-hidden bound min(1,(2Q_A+sqrt(3017))^2/2^128) from DYNAMIC-QUANTUM-HIDDEN-THEOREM.md / QUANTUM-RO-THEOREM.md. Its native random-oracle/source model and event/resource meanings must be verified before a final comparison. It is not an actual fixed-h hardness statement.

**PROVED — conditional algebra on that supplied formula.** Its c=1/2 crossing is Q_A*=2^62 sqrt(2)-sqrt(3017)/2; its c=1 crossing is Q_A*=2^63-sqrt(3017)/2. These are algebraic radicals, not rational numbers. Exact dyadic lower/upper enclosures from integer-square-root arithmetic can certify the nearest integer queries without replacing the radicals by an unjustified exact rational. Comparisons must remain confined to the same final event, source model and query budgets. Existing certificate/core files will not be changed.

**OPEN — completion boundary.** This first derives the actual activation law, signed-weighted ordinary-advantage inequality and conditional envelope thresholds. The intended follow-up is exact arithmetic tables, independent verification of the direct-bound scope and a comparison receipt. No actual primitive advantage, SHA hardness, whole-security category/capacity or source-game declaration is established.
