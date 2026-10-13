# Independent second-reader review of the adaptive FORS source bridge

**Outcome: ACCEPTED_MANUAL_SCOPED_BRIDGE_AFTER_PADDING_REPAIR.** The repaired final coverage inequality is justified in the stated classical, partial, atomic joint F/J ideal game. It is not a Lean/EasyCrypt-checked source refinement, an efficient reduction, a claim about fixed SHA-256, or full LULA I EUF-CMA security. No additional blocking defect was found within that scope.

## Independence and reviewed subjects

`INDEPENDENT_DERIVATION.md` was saved before reading the authoring lane. It independently identified the fresh-message framing, zero-seed and lower-half guards, prediction and full-image collision losses, finite-search event, and the same conservative beta below. The initial author review then found a false expectation-based padding step. The author repaired that step before this final review; the independent derivation was not restarted or rewritten.

The release source `publications/LULA-I/release/code/lula1/src/lib.rs` was rechecked directly: SHA-256 `ac8e67f05af68dd8e1291c5909847f74103903fb7ffa2c70f500c6ec48f14210`. The relevant source anchors are message hashing at lines 164–187, signing at 601–624, and verification at 679–714. The reviewed **repaired** author `fors-source-bridge/DERIVATION.md` has SHA-256 `2515bbec53db0cf3bde805c38a0c6c00ac45cd899c3c1407a7d6e81ab7978752`.

The repair receipt reports the earlier author hash as `07b75430d3605310bbc5e3d0be12aac81fff175dc7057fbf103a22bde22dbfad`. I read that earlier text but did not independently hash it before it changed; this earlier hash is attributed to the author receipt rather than presented as a personally measured hash. The final repaired hash and the source hash were independently measured. All writes in this review stay in this second-reader directory.

## Exact defect and counterexample

The earlier argument defined `Q_E = E[N_E]` for a random number of eligible outer queries, then treated `Q_E+1` as a candidate-stream padding cap. An expectation cannot be used as a pathwise cap. Adaptive allocation can concentrate queries on unusually well-covered exposure sets.

Here is an exact counterexample to that intermediate stream claim using the actual alphabet and instance parameters. Let `q=2`, `B=2^41`, `t=512`, `k=17`, and `Q=2^30`. After two iid exposures, query Q raw independent candidates only if their instance addresses coincide, an event G of probability `pi=1/B`. Otherwise query none. The number D of real-tree positions where the two leaves differ, conditional on G, is `Bin(k,1-1/t)`. A candidate's conditional coverage probability is

```
c_D = 2^D / (B t^(k+1)),
mu = E[c_D | G] = (2-1/t)^k / (B t^(k+1)),
nu = E[c_D^2 | G] = (4-3/t)^k / (B^2 t^(2k+2)).
```

The omitted-coordinate acceptance factor is included in `t^(k+1)`. For an unconditional single candidate against two exposures,

```
p_fixed(2) = (1-pi) 2/(B t^(k+1)) + pi mu.
E[N_E] = Q/B = 1/2048.
```

Bonferroni gives a rigorous success lower bound

```
lower = pi [Q mu - binom(Q,2) nu]
      > 31 (E[N_E]+1) p_fixed(2).
```

`expected_cap_counterexample.py` proves the strict rational comparison using Python `Fraction`, without evaluating huge approximate powers. Its exit code was 0. `EXPECTED_CAP_COUNTEREXAMPLE.json` records exact fractions; the displayed approximate ratio is 31.457519154862567, and the lower bound's approximate log2 is -197.02396269432944. The deterministic `(Q+1)p_fixed(2)` bound exceeds the lower bound.

This is a counterexample to the expected-count padding justification, **not** an executable LULA I forgery or a refutation of the displayed source-loss bound: the beta loss at this query budget is far larger than this stream event. The repaired author §§5–6 now explicitly use `N_E+1 <= Q_H+1` and forbid replacing that deterministic cap with `E[N_E]+1`.

## Coefficient and case audit

Write `M=2^128`, `L=2^256`, `C=2^32`. The independently accepted sufficient loss is

```
beta(q,Q_H) <= min(1,
    (2 Q_H+q+2)/M
    + [q Q_H+binom(q,2)+q]/L
    + q(511/512)^C).
```

| Item | Second-reader finding |
|---|---|
| Zero public seed | One `1/M` contribution is needed because addressed inputs have zero bytes 16–31. Nonzero S separates them from inner strings. A separate privatization triangle bound may charge this event twice conservatively; deleting a charge requires a simultaneous coupling with one shared flag. |
| New-message inner prequeries | Each raw inner point fixes one message suffix and one R prediction. Unused J(m) is independent in the continued unflagged ideal execution. Union-count literal predictions once, yielding `Q_I/M`, with no additional q factor. Pre-key queries are included; future root/message selection does not multiply a fixed prediction. |
| Randomizer collisions | No gratuitous `q^2/M` term. Different messages give different framed inner inputs even when their 128-bit randomizers coincide. Repeat message requests add no fresh exposure. |
| Inner/outer aliasing | `U[16:32] != S` prevents aliasing independently of the root distribution. The relevant inner output count is at most `Q_I+q+1`, giving this coefficient over M. The final +1 is one potentially fresh final inner evaluation. |
| Full-image inner collisions | Count later fresh evaluations of distinct input pairs containing a signing inner point. Honest/public pairs contribute `q Q_I/L`, honest/honest pairs `binom(q,2)/L`, and a fresh final inner image `q/L`. Equal old inputs are memoization, not independent collision samples. |
| Future counter-namespace guesses | A previously chosen eligible outer prefix has 256 bits. It can target any later fresh signing U, requiring `q Q_E/L`; removing q would be unjustified. |
| Combining raw-query classes | Eligible inner and eligible outer languages have respectively equal and unequal bytes 16–31 to S. They are disjoint pathwise. Thus `q(Q_I+Q_E) <= q Q_H`; no extra factor 2 is needed for the 256-bit raw-query term. |
| Random class counts | Expected counts are legitimate only in predictable, later-fresh-output event accounting. They are not latent-stream lengths or deterministic query caps. The repaired author distinguishes these uses. |
| Finite counter space | The source has only C distinct counter inputs. On a fresh counter namespace, all-C failure is `(511/512)^C`; wraparound or checked-build panic is not a further iid trial. At `q<=2^40`, `q(511/512)^C <= 2^-8388568` is a valid conservative bound. It certifies neither an implemented abort return nor a runtime worst case. |
| Final verification | For a fresh final message, equal inner input to an old signing input is impossible by framing. Equal U requires the collision event. A genuinely fresh eligible final outer point is exactly one additional candidate; an already public point is already counted. Thus the candidate cap is deterministic `Q_H+1`. |
| Rejected grind outputs | Their omitted digit is nonzero and verification rejects them. Other points in an old honest U namespace cannot verify a fresh message without the U-collision event. Fresh but irrelevant oracle points are nuisance outputs, not additional signing exposures. |
| Old and repeated public points | The public oracle memoizes them. They supply no new iid Y draw. Adversarial queries before or after exposure can be retained and tested against the final padded exposure set. |
| Partial completion | q bounds initiated atomic requests. A failed/nonterminating later WOTS operation may prevent disclosure of an already latent FORS draw; adding its unused exposure is conservative. The experiment is not normalized on successful completion. Unlimited interrupted/retryable attempts require a different game and budget. |

## Coupling, padding and retained inequality

The same public complete-hash oracle must be used throughout; treating source inner and outer hashes as globally independent functions would be wrong. On a good prefix, the byte-level guards make fresh honest inner points and outer namespaces disjoint from old relevant points. Their fresh images can therefore be assigned from independent streams with first-writer-wins table consistency. A first accepted counter is selected only by the omitted digit, leaving the retained route and real-tree coordinates uniform and independent of the rejection count and rejected coordinate noise.

The argument uses unconditional latent streams: at most q fresh signing-coordinate draws X, at most `Q_H+1` fresh eligible nonhonest/final candidate draws Y, and independent nuisance outputs. Adaptive source names consume prefixes; repeated points reuse existing entries. At the first Bad event, stop claiming correspondence while continuing the source ideal game without an observable analytical flag. The entire successful transcript is **not** conditioned on `NoBad` and declared iid. Such conditioning can bias stopping and allocations.

Pad the X stream to q and the Y stream to the deterministic cap `Q_H+1`. Adding exposures only increases coordinate coverage. A union over all padded Y draws avoids assumptions about when the adversary allocates its candidates or stops. Consequently, with

```
p_fixed(q) = (1/t) E[(1-(1-1/t)^N)^17],
N ~ Bin(q,1/B), B=2^41, t=512,
```

the retained, manually justified source-bridge inequality is

```
Pr_IDEAL(covered-leaf route for a fresh-message output)
 <= beta(q,Q_H) + min(1,(Q_H+1)p_fixed(q)).
```

The complete right-hand side may be capped at 1. This is a coverage-route event bound, including the omitted-coordinate filter. It does not classify all valid signatures as covered-leaf forgeries.

## Standing qualifications and open obligations

The conclusion assumes the previously specified joint F/J idealization with independently uniform private K/P and public S; the hidden flag cannot influence observable output or stopping. Keys remain unused by the continued ideal execution except analytical comparisons. Snapshot/restore handles must be opaque and honestly consistent; real cache files containing seed bytes are not an adversarial snapshot interface for this lemma. The interface excludes timing, private objects/cache bytes, compression queries, in-flight interruption and quantum queries. q and Q_H must cover all restored branches and initiated signing attempts, with adversarial local verification charged to Q_H and one challenger verification.

The accepted result is a **manual mathematical source bridge** under those hypotheses. A machine-checked semantics/refinement and efficient simulation remain open. Full FORS node/root binding, equal secret-value aliases across addresses, WOTS certification, efficient moving-target extraction, complete EUF-CMA composition and QROM bounds remain separate open obligations. Composing the joint real/ideal distance and beta with coverage is not a substitute for those obligations. None of this establishes a 128-bit complete-signer guarantee or a capacity certificate.

## Reproducible check

Run `python -I -B expected_cap_counterexample.py` in this directory. The recorded run returned exit code 0 and verified exact rational inequalities. That small discriminator validates the review finding only; it does not prove the source refinement. Source and repaired author hashes above were measured with PowerShell `Get-FileHash -Algorithm SHA256`. No benchmark, proof packet, manuscript, or implementation was changed.
