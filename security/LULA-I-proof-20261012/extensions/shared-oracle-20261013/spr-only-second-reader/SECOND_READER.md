# SPR-only premise: independent second-reader result

**Outcome: GENERIC_SAME_TWEAK_SPR_ONLY_PREMISE_REFUTED.** The identity-chain countermodel satisfies perfect same-tweak second-preimage uniqueness while providing trivial public inversion and no WOTS message binding. The result is an assumption separation, not a LULA I/SHA-256 forgery.

## Source-first derivation and exact parameter control

The actual pinned source was read first, including the lower-layer parameter literal and WOTS acceptance/signing/completion loops. `INDEPENDENT_SOURCE_CHECK.md` was saved before reading the supplied Lean source and receipt. Library SHA-256 remains `ac8e67f05af68dd8e1291c5909847f74103903fb7ffa2c70f500c6ec48f14210`.

Take the fixed-width chain primitive `F_A(x)=x` for each address. Given a target input x, no distinct x' at the same A has an equal output; thus same-tweak second-preimage advantage is exactly0 for every adversary. Given a target output y, public inversion returns y with success1. A chain at any position contains its own start unchanged.

For the exact lower-layer shape,32 chains / width16 / sum240 / no forced zeros, the accepted vectors are

```
e  = 15 repeated16 times, then0 repeated16 times;
e' = 0 repeated16 times, then15 repeated16 times.
```

Their full128-bit encodings are `ffffffffffffffff0000000000000000` and `0000000000000000ffffffffffffffff`. Both sum to240, are distinct and incomparable. This uses no digest collision. A signature on e exposes all32 starts. The same node vector completes to the same endpoints for e', hence preserves any independent public-key compression.

`control.py` instantiates a two-message injective preprocessing map to these two accepted encodings and an independent SHA-256-based PK compression. One516-byte **countermodel WOTS** signature validates both messages, and every start is exposed. The use of SHA-256 for this separate compression does not change the identity-chain model or turn the control into a real-source attack. It is not a complete LULA I5720-byte signature. The script returned exit0 and records the exact values in `CHECKS.json`.

The fixed-sum antichain prevents a distinct accepted vector obtained by increasing every chain position. It supplies no hardness for moving backward. In this model backward movement is trivial because every step is publicly invertible. A premise covering preimages, exposed-chain origin or an applicable random-oracle model is materially stronger than same-tweak SPR alone.

## What Lean actually checked

Reviewed `root-formal/SPRSeparation.lean` SHA-256 `bec31567ae07abbdf8ae868b2d2f804fe469dce276d938bf6fdd8a24e1a425da` and existing successful `SPRSeparation-check.json` SHA-256 `49c4fde2f4d390bc9123f053cd446a8cde2ce453275b306a34df42f59865601f`. Then reran the actual pinned local checker without editing the Lean source; exit0. `LEAN_RECHECK.json` preserves the command and live stdout.

| Declaration | Checked content | Printed axioms |
|---|---|---|
| `LulaSPRSeparation.identity_injective` | Identity is injective on any type. | None |
| `LulaSPRSeparation.identity_chain` | Every identity iterate returns its input. | None |
| `LulaSPRSeparation.identity_values_any_digits` | Any digit choices give the same vector of identity-chain values. | `propext`, `Quot.sound` |
| `LulaSPRSeparation.identity_has_public_inverse` | Identity has an explicitly constructed public inverse. | None |

The four declarations contain no `sorry`, `admit`, `native_decide` or added custom axiom. Their proof source uses elementary equality, induction, function extensionality and an explicit inverse. They do **not** formalize a SPR game, a WOTS verifier, fixed-sum acceptance, byte serialization, EUF-CMA or the Rust implementation. Those cryptographic implications and the exact32-chain instance are the separate manual argument / executable control.

## Exact claim boundary

This refutes a premise that assumes **only same-tweak SPR for the fixed-width chain family** and claims WOTS binding/unforgeability. It does not refute a stronger package of preimage, tweak/key binding, digest, composition or random-oracle assumptions. If a definition permits changing the tweak as part of a second-preimage witness, identity across tweaks need not have zero advantage in that different game; the same-tweak qualifier is essential.

Identity here is not an injective hash from arbitrary variable-length payloads to128 bits. Compression/digest functions have separate domains and assumptions. The finite preprocessing used in the control is injective only on its two-message test domain, not a proposed complete source message-hash construction. No real SHA chains, source binary, full hypertree attack, benchmark or parameter-security certificate is involved.

No paper, frozen packet or peer source was changed. Only this reviewer lane received new artifacts. The conclusion should be cited as a generic assumption counterexample with four supporting checked algebraic lemmas, not a machine-checked full cryptographic separation theorem.
