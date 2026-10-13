# Independently checked single-event successor

This successor preserves `INDEPENDENT-DERIVATION.md` unchanged. It follows root's coordination note proposing one terminal event rather than two separately bounded events. No peer derivation or source implementation was changed.

## Common event and faithful REAL containment

Keep exactly the stopped controllers and CQ active-subblock proof from the independent derivation. B is the absorbing first honest/final PUBLIC I/E private alias; W is acceptance/freshness with no B. They are disjoint terminal outcomes by construction. Therefore their projectors are orthogonal and

    Pi_E = Pi_B + Pi_W

is one common orthogonal terminal projector. E is B OR W. The actual ordinary REAL winner satisfies E in stopped REAL: if an alias is ever reached before its winner, E is recorded immediately; otherwise the stopped controller reproduces every actual source/verifier step and records W. The stopping analysis need not reproduce REAL behavior after B.

## IDEAL union and one square-root comparison

On active histories before B, stopped IDEAL equals the keyblind unflagged HJ continuation without renormalizing. Its no-B winner subblocks are contained in the unflagged HJ winner blocks. Let

    b = min(1,(2q+2)/N),
    e = min(1,epsilon_HJ(q,Q)),
    a = 2Q/sqrt(N), N=2^128.

The alias union proof gives p_I(B)<=b; the positive-history containment gives p_I(W)<=e. Disjointness yields

    p_I(E) = p_I(B)+p_I(W) <= min(1,b+e).

The paired stopped purifications have vector gap <=a. Applying the same projector Pi_E to both yields

    |sqrt(p_R(E))−sqrt(p_I(E))| <= a.

Thus the sharper fixed-nonzero-S event transfer is

    p_REAL(Win | S!=0) <= min(1,
        [2Q/sqrt(N)+sqrt(min(1,b+e))]^2).

This is stronger than the sum of the two separately projected bounds: it pays one a^2 and one cross term2a sqrt(b+e), instead of two a^2 and2a(sqrt(b)+sqrt(e)). It does not require B and the ordinary HJ winning event to be independent; they may overlap in the unflagged continuation. Only B and W are disjoint in the stopped experiment.

## Uniform seed and retained limits

Use an epsilon_HJ bound valid for every fixed nonzero S, with no embedded S=0 charge. Average those branches and assign probability at most1 to the correct ordinary-RO S=0 REAL branch. A sufficient bound is

    min(1,1/N + [2Q/sqrt(N)+sqrt(min(1,b+e))]^2).

Keeping the factor1−1/N on the nonzero branch is slightly tighter but unnecessary. This charges seed zero once. It does not permit subtracting an earlier charge from an unrelated unconditional bound.

The positive-subblock claim is still ONLY the CQ/dephased classical environment/history statement for active unnormalized mass. Pure-state operator domination remains false; it is not needed because private-support expectations are diagonal in those registers. The purification is restored only for the query norm and the terminal projector inequality. No detector stops/measures coherent query inputs.

Outcome: **MANUALLY_DERIVED_SINGLE_PROJECTOR_RARE_EVENT_TRANSFER; INDEPENDENT_REVIEW_REQUIRED**. The current accepted conservative private distance and master numerical fields remain untouched. This is a finite event-transfer statement requiring a separately valid ordinary-HJ epsilon; it is not by itself a whole-signature/QROM certification or efficient simulation.
