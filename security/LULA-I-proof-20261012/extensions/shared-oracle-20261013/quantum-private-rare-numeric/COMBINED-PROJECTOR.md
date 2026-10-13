# Independent check of the combined terminal projector

This check follows my saved independent stopped-CQ derivation. The root subsequently suggested using one common B-or-W projector rather than adding two separate square-root inequalities. I have not yet read its rare-event draft or another author lane. Thus this is independent verification of that suggested strengthening, not a claim of blind discovery of the suggestion.

Let STOP_REAL and STOP_ID use the common stop-before-response I/E guard and have purified prefix vector discrepancy d<=2Q/sqrt(N). Their common terminal examiner is:

1. If any guard flagged, output1. This absorbing branch supplies B.
2. Otherwise run the common guarded final verifier, outputting1 on acceptance and0 on rejection/noncompletion. This supplies W=WinNoB.

B and W are disjoint outcomes of the same terminal instrument. A common dilation and output1 projector therefore give

    sqrt(p_STOP_REAL(B or W))
       <= d+sqrt(p_STOP_ID(B or W)).

The original REAL accepting event is contained in B-or-W under the first-flag-preserving coupling: before a flag the source trace is identical, and flag branches are pessimistically accepted irrespective of their eventual original result. No observation/reprogramming of old coherent queries is needed.

In the stopped IDEAL, predictable continued-key-blind nominations give p(B)<=b=min(1,(2q+2)/N). CQ active terminal domination gives p(W)<=Pr_HJ(Win)<=A_HJ, where A_HJ=min(1,c+h+g+d7) is the accepted ordinary HJ union. Summing these **IDEAL** probabilities once gives p(B or W)<=min(1,b+A_HJ). The combined projector consequently suggests the sharper sufficient comparison

    Pr_REAL(Win | fixed nonzero S)
       <= min(1,[2Q/sqrt(N)+sqrt(min(1,b+A_HJ))]^2).

Unlike the earlier separate bounds, this does not pay the vector discrepancy twice. It follows from a single event norm inequality, not subtraction of correlated losses or an assumed independence of B and W. The b+A_HJ term can be loose because the dominating ordinary HJ Win event may include histories that would flag; this does not invalidate its upper bound.

For independently uniform S, first apply the fixed-nonzero expression and then charge the single zero-S branch. A conservative unconditioned envelope is

    min(1,1/N+min(1,[2Q/sqrt(N)+sqrt(min(1,b+A_HJ))]^2)).

Retaining1-1/N on the conditional expression is a tighter optional averaging; it is not needed for this sufficient formula. Do not also add the earlier private-hop distance or its extra seed-zero charge. The accepted conservative theorem/master remain immutable; the sharper envelope stays a candidate until independent review validates the common channels, physical CQ active domination and one projector.

The forthcoming exact control measures B, W and their sum on both stopped sides, retaining measured history and quantum work. It checks their common combined-projector norm inequality and includes the required negative controls. No toy acceptance event is labelled real LULA EUF.

**Status: COMBINED_PROJECTOR_IMPLICATION_CHECKED_AS_CANDIDATE_PENDING_REVIEW.**
