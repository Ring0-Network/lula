# Independent source/game derivation: quantum FORS coverage

Saved before reading the root quantum-coverage draft or new peer multi-call proofs. This is a source/game audit, not a full QROM security statement. A primary adaptive-reprogramming constant is deliberately not guessed.

## Ordinary HJ sampler and exact source fields

Pinned library SHA256 `ac8e67f05af68dd8e1291c5909847f74103903fb7ffa2c70f500c6ec48f14210`. In the joint-private ideal HJ game, source161–187 gives R_m=Tr16 J(m), I(R,m)=R||S||root||m, U=G(I), and E(U,c)=U||BE32(c)||S. Source601–624 takes the first counter whose omitted9-bit FORS coordinate is zero, then exposes the41-bit instance and17 real9-bit indices. Verification697–706 accepts arbitrary transmitted R,c and a fresh message. All203 used digest bits have separate roles; the remaining53 are unused.

For fixed nonzero S/root and a finite raw register, sample independent R_m uniform128 and full256 U_m for every allowed message label. Program G(I(R_m,m))=U_m; fill the other inner points independently. Different labels m give disjoint inner planes even when R values repeat. This has the ordinary HJ public-RO marginal jointly with J. Full256 images, including suffixes, are required. Addressed hashes cannot be inner points because their bytes16–31 are zero; E points with U[16:32]!=S cannot be in any inner language with those bytes equal S.

## Masking nonces and the guard order

Define a dynamic public inner overlay: uncompleted message's designated I_m point returns a residual value; completed messages' I_m points return U_m. The classical server always uses the fixed programmed G. At completed return, add R_m and U_m to auxiliary Known, optionally granting U_m for free (the real client can derive it). Repeats reuse the same R/U/outer row and do not draw a new exposure. A partial request reveals no nonce; q counts initiated requests and noncompletion is absorbing/nonwinning.

The source controller must stop its analysis game BEFORE outer hashing if U_m[16:32]=S. Otherwise E(U_m,c) can lie in the inner language and hit another unrevealed nonce point, leaking a future nonce's image via source metadata. An invariant claiming that remaining R/U are unused without this guard is not justified. This stop is an analytical error branch, not an implemented production abort.

For the guard-stopped controller, source metadata never reads a still-uncompleted nonce coordinate besides its own. The continued ghost's remaining R values are iid and independent of its retained quantum state. A raw query names one message label and one R candidate, so hidden-inner query mass averages at most1/2^128. Classical services and Known updates are common channels. Packed query slots yield a purified vector gap at most2Q/2^64.

Use a common terminal examiner that stops before hashing if a final fresh-message input equals an uncompleted genuine nonce point. The unflagged ghost continuation has one such candidate and probability at most1/2^128. One cannot simply run the REAL terminal oracle G in the masked ghost at this unknown point and claim common-channel equality. Alternatively counting its final hash as another coherent query is a conservative distinct route.

Before each new source call, its U_m is unused by the ghost public interface and independent of its state/table history. Thus U_m is uniform256 even under adaptive message choice. The per-call tail-S guard costs at most1/2^128. Repeats add no draw. A namespace-collision guard U_m=U_j for an earlier new-message call costs at most binom(q,2)/2^256. Stop before deriving/programming an independent exposure when this occurs. These guards can be included in a terminal 'error OR coverage' predicate so that the initial nonce hybrid is paid once, rather than separately paying it to every guard event. Noncompletion later in WOTS signing may conceal a latent FORS draw; padding includes it conservatively.

## Why nonce masking alone does not make exposures iid

Even with fresh hidden U, the source exposure is the first accepted tuple from the **existing** quantum-accessed outer row G(E(U,c)). Conditioning on a previously observed quantum state/table can correlate that tuple with a candidate. A uniform U marginal is not an iid-exposure proof. Nor can all future U_m rows be independently programmed globally: a finite message universe can vastly exceed the2^256 namespace universe, so U_m collisions are unavoidable across all labels. Only actual initiated new-message rows are relevant; collision guards and a valid row-refresh lemma are needed.

After refreshing each reached new namespace, draw its complete counter row independently, with an exact successful/failed first-acceptance sampler. On success, counter kappa is truncated geometric, earlier omitted digits are nonzero, its accepted tuple X is uniform on [2^41] x [512]^17, later rows are uniform, and all full-output suffixes are consistent. On failure allC=2^32 omitted digits are nonzero and no signature is returned; an independent latent X can still be padded for upper bounding coverage. No need to invent a total exhaustion API or charge failure as a real forgery.

The q latent X values may then be presampled iid, independently of the residual outer table. Actual completed disclosures are a prefix/subset, and their coverage is bounded by the q-padded transcript T_q. This is an unconditional construction, not conditioning all prior reprogramming disturbances away and asserting iid streams.

## Conservative elementary row-refresh route, pending exact implementation

A potential self-contained route is the following table-swap lemma: before a reached new call, draw a fresh U uniformly256 independent of the current public state. Couple the residual table R and a table R' differing by an independently resampled **entire counter row** at U. R' has the same ordinary-table marginal. Express the resampled game with R' as its environment and compare the retained pre-call state generated with R to the state generated with R'. The current source row read and output can then be the same postprocessing channel of the resulting table.

On the comparison algorithm's past public query, one raw point nominates one U namespace; expected changed-row mass is at most1/2^256. A unitary hybrid therefore costs at most2Q_before/2^128. Past independent refreshed source rows are nuisance tables, not residual-table reads; if an implementation still reads the underlying residual table in those callbacks, their reads must be charged separately. A conservative fallback can include previous classical source-row collisions, at most(q-1)/2^256, rather than multiplying byC.

This suggests a valid but loose total row-refresh loss of order2qQ/2^128 (plus any separately justified callback charge). It requires an exact table/controller coupling before use; it is not asserted merely from a fresh-U slogan. A tighter adaptive-reprogramming theorem may improve Q to sqrt(Q), but its exact primary statement, row-read simulation cost, source callback reads and entropy convention must be inspected. A raw XOR oracle query simulated through a packed-row oracle generally needs a row read AND its uncomputation: two row queries. A classical source lookup must also be accounted if that theorem counts it. No claimed primary bound is imported here.

## Final inner target search

After nonce masking and valid row refresh, a final fresh message cannot use a completed nonce point; the uncompleted nonce equality event is separately examined. Otherwise its inner image is from the residual inner table. A valid outer candidate must also avoid a U namespace from completed signatures and the tail-S half. For at mostq known namespace values, the bad-image density is bounded by

    d_inner <= 2^-128 + q*2^-256.

Those are full256 targets, not literal q prequeries or q^2 R-birthday events. Given independent padded U targets and residual inner table, a marked-output sampler plus a common stopped final query gives a conservative quantum search bound `(2Q+1)^2*d_inner`. Completed nonce points are common programmed exceptions, and a fresh final message cannot be one. Removing/changing their targets must be predictable and must not read the hidden marking bits.

Advice revealing the padded U targets can strengthen this target-event experiment AFTER establishing the row-refresh hop for the original adversary. It must not be given before a row-reprogramming proof that relies on U being freshly unpredictable. Mixing these two advice views is an invalid proof shortcut.

## Final outer coverage search

For a q-padded iid transcript T define C_(b,j) as covered leaf sets and

    p(T)=1/(2^41*512) sum_b product_(j=1..17) |C_(b,j)|/512.

The zero filter is included once. Its expectation is

    p_F(q)=1/512 E[(1-(511/512)^L)^17],
    L~Bin(q,2^-41).

After row refresh, residual eligible outer images are uniform independently of T. The q programmed honest namespaces must be excluded from the final candidate by the inner target event. Their full row data can be nuisance advice; their canonical accepted tuples are already part of T and are not fresh raw search trials.

Condition on a fixed T in a SEPARATE event-only advice experiment. Sample residual covered-marker bits independently Bernoulli p(T), good images uniformly outside the covered set, and bad images uniformly inside it. The ghost oracle returns good images, while source programmed rows are common and chosen without reading those marker bits. The ghost candidate list/state is independent of unexamined marks, including retained earlier quantum memory. A packed query hybrid plus a common final marker examiner gives `(2Q+1)^2*p(T)` for one final eligible nonhonest outer candidate. Averaging gives `(2Q+1)^2*p_F(q)`; no realized transcript is asserted bounded by p_F(q).

Again the future transcript advice is a separate target-event upper bound AFTER the reprogramming hop. It must not retroactively be provided to the original row-refresh adversary. No classical quantum-query-history union bound is used.

## Expected review gates

The primary row-refresh bound and its exact read/uncompute/callback budget remain to be reviewed. The source/game derivation must keep global inner sampler correct, guard before aliasing, nonce/U closure, q-initiated partial semantics, duplicate namespace stopping, common terminal handling, and distinct advice projections. Failure of any gate keeps the complete quantum coverage bound OPEN. Full signature QUANTUM total remains unestablished by this derivation alone.
