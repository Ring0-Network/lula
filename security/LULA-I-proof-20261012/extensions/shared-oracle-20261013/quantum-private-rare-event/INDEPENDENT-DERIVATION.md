# Independent event-specific joint-private replacement

Saved before reading root `QUANTUM-PRIVATE-RARE-EVENT-DRAFT.md`. Scope: finite coherent-public-RO/classical-service source model. Current accepted conservative private distance is not replaced by this unreviewed derivation.

## Coupling and source stop points

Pinned source SHA256 `ac8e67f05af68dd8e1291c5909847f74103903fb7ffa2c70f500c6ec48f14210`. For fixed S!=0 use the full256 coupling already independently derived: O_1 agrees with O_0 outside D_K union M_P; at D_K(A)=S||zero48||Addr5/6(A)||K it returns F(A), and at M_P(m)=P||S||m it returns J(m). Conditional on keys the patched O_1 is an ordinary full256 RO. In unflagged IDEAL, keys K/P are unused by all answers, source outputs, stopping and opaque-handle generation.

Source161–168 private F/J evaluations agree exactly between worlds. Keygen and other addressed public types0–4/7 cannot enter D_K or M_P on S!=0. Only the public message I/E calls can alias M_P: I=R||S||root||m nominates P=R; E=U||counter||S nominates P=U_high and requires U_low=S. All source outer counters nominate the same high half. Source601–617 supplies at most two such nominations per initiated call. Final verification697–700 supplies at most two more. Honest public I/E cannot enter D_K.

Define stopped REAL/IDEAL controllers which inspect each honest/final PUBLIC I/E input immediately before its evaluation. If it is in the private family, record terminal B and stop before returning a differing answer. Otherwise use its public hash. These stopped services are the SAME channel: private calls use the same F/J values; all reached nonalias public calls have O_1=O_0. This guard is an analysis device, not a production abort. It is not applied to coherent adversarial oracle queries, and no quantum query-hit history is created.

The actual REAL winner is contained in B of its stopped game or Win-with-no-B. On paths without B the stopped execution is identical to ordinary REAL. A source call that would later fail/noncomplete still contributes at most its two nominations; q counts initiated calls and no partial buffer is public.

## Critical positive-subblock lemma

Let rho_j be the UNFLAGGED IDEAL prefix just before its packed query slot j. Include a classical inaccessible environment containing sampled tables/keys, and copies of all measured classical histories. For fixed environment w and complete classical history h, write its positive block as

    rho_j[w,h] = pi(w,h) |w,h><w,h| tensor rho_adv(w,h).

The source nomination list through h is a function of its ideal tables and measured messages/candidate bytes, not of K/P. For active stopped-IDEAL histories, no preceding source alias occurred. The corresponding block is the SAME unnormalized block if all those nominations miss, and zero otherwise. Equivalently an indicator a(w,h,K,P) in {0,1} multiplies it. Noncompletion/inactive branches need not match the stopped dead-state records; only active query blocks are claimed to be subblocks. Therefore

    0 <= sigma_j^active <= rho_j

in this **CQ/dephased-environment** representation. This is a positive-operator statement without normalizing the surviving keys. It remains valid after packing common service operations: an active history reaches the same numbered query, with exactly the unflagged amplitudes/probability before removing failed-key histories. Stopped histories never rejoin the active game.

This claim must not be made about rank-one global purifications: projecting a pure state on surviving coin components does not generally yield an operator dominated by the original pure state. Dephase the sampled-coin/history environment for the PSD comparison. Query-support projectors are diagonal in those classical registers, so their expectations are unchanged when restoring the common purification used for vector telescoping.

It also fails for a hypothetical detector that measures/stops on coherent quantum query inputs: such a projector acts nontrivially on the adversary state inside a history block, rather than multiplying the block by a classical scalar. Only honest/final classical public I/E aliases are stopped here.

## Unnormalized support estimate and packed hybrid

Each raw input nominates at most one private key when S!=0. Since rho_j is keyblind, its expected query mass on D_K union M_P is at most1/N, N=2^128. Positivity gives

    Tr(Pi_private sigma_j^active)
      <= Tr(Pi_private rho_j) <= 1/N.

No divided survival probability appears. For example, surviving keys may be uniform on a complement with conditional next-guess probability1/(N−g)>1/N; that is consistent with the unnormalized inequality.

The public coherent query unitary acts identically on dead branches and differs only on active private-family support. Its squared global purified vector discrepancy on stopped IDEAL is at most4/N. Common source/local operations between consecutive query slots have common Stinespring dilations, including classical stop records. With Q coherent slots, inactive branches padded by identity,

    ||Psi_REALstop−Psi_IDEALstop|| <= 2Q/sqrt(N).

The REAL survivor state is not claimed keyblind. Every error is evaluated on the continued stopped IDEAL, bounded via its active submass of the unflagged IDEAL. No flag-induced classical posterior is renormalized.

Final verification can be a common stopped controller, so its I/E do not need additional coherent slots here: at an alias it stops before hash; elsewhere public images match and all later addressed calls are outside private families. Its two nominations enter the classical alias budget. This is the key distinction from a generic terminal oracle comparison.

## Two terminal probability bounds

In UNFLAGGED IDEAL, at most2q+2 PUBLIC I/E candidate P values are generated from keyblind data. The literal candidate-union argument gives probability at most(2q+2)/N that any is P, including eligibility checks and partial calls. First-alias agreement gives

    p_IDEALstop(B) <= (2q+2)/N.

The no-B winner subblocks are contained in ordinary IDEAL/HJ winner blocks, so

    p_IDEALstop(Win_noB) <= epsilon_HJ(q,Q),

where epsilon_HJ must be a separately accepted ordinary-HJ event bound for the same interface; no specific complete quantum bound is assumed here.

Use the same terminal projector/dilation for B and for Win_noB on paired purifications. For either event E,

    |sqrt(p_REALstop(E))−sqrt(p_IDEALstop(E))|
      <= 2Q/sqrt(N).

Consequently a candidate rare-event private transfer is

    p_REAL(Win | fixed S!=0) <= min(1,
      (2Q+sqrt(2q+2))^2/N
      + (2Q/sqrt(N)+sqrt(epsilon_HJ(q,Q)))^2).

For uniform S, add1/N once for the separate S=0 branch with its correct ordinary-RO REAL marginal, then cap at1. K/P entropy is a game assumption supplied by the seed caller, not enforced by copying seed bytes in keygen. q covers all initiated calls across restored branches. This does not establish a full quantum epsilon_HJ, category, efficient simulation or fixed-SHA security.

## Smallest validation obligations and controls

The central review gate is exact active-history domination at packed query slots, not a slogan about ideal key independence. Required finite controls: show unnormalized hidden mass stays <=1/N while normalized surviving mass exceeds it; show pure-state PSD domination is false even when the CQ version holds; and show stopping a coherent query projection would fail the block argument. A faithful source/controller proof must preserve common pre-alias public images, full256 programming, classical measured service inputs, absorbing noncompletion and opaque handles. These gates require independent review before replacing the accepted conservative private distance in any total.
