"""Hash-bound final manual review; writes only this reviewer directory."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import subprocess
import sys

B = Path(__file__).resolve().parent
X = B.parents[1]
def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()
def resolve(p):
    q = Path(p)
    return q if q.is_absolute() else X / p
def check_pins(pins):
    for p, expected in pins.items():
        assert sha(resolve(p)) == expected, p

subject = 'PARAMETER-UNIFORM-CLASSICAL-THEOREM.md'
subject_hash = 'e5fc68bc269ca98672caa99ec70d5695d3d578095a62ebbfc0f99f9d8fbc394b'
assert sha(X / subject) == subject_hash
provenance = {
    'selected-promotion-review/parameter-uniform-classical/INDEPENDENT-FIRST.md': 'e330e30759eac52adca83384ce5b9c95cfa9a491230376518cfa19302dd3bd67',
    'root-parameter-uniform-classical/FIRST-DERIVATION.md': '833a46073c70f3e6f702a925360ed54279f438fa557cd0ef3e63473e58b571fe',
    'selected-promotion-review/parameter-uniform-classical/PEER-REVIEW.md': '94a911fb26cefdf2293f4b61f76f366f6613e6241bf8630d4dac72f3493e2169',
    'selected-promotion-review/parameter-uniform-classical/PEER-REVIEW.json': 'e750b12f80b654ad06c35f92761f74f02e8fe932fba3bdd326c387dbbbfb490a',
    'selected-promotion-review/parameter-uniform-classical/finite_controls.py': '6bd00e18433d80a1a98fcfccda2d045754932c9db802cd0c6de3797b6904119d',
    'selected-promotion-review/parameter-uniform-classical/FINITE-CONTROLS.json': '63f604d2179e5e269fba1de0e6a8fc5b80e2d67916aa6eb44ba34fcf1c288ca9',
    'selected-promotion-review/parameter-uniform-classical/finalize_peer_review.py': 'a6de31e767636b9d8ad2cca9d4938a16694eb81522f4010f1cc06aadd45d9587',
}
preserved = {
    'CLASSICAL-RO-THEOREM.md': '3ff8d3c0457ce0525a5af416472f7188e75e20c52cc06d2220b4273a1db752fe',
    'CLASSICAL-JOINT-RO-THEOREM.md': '4fa7c3b63a268bd7535a753813d109a2f768f0089df44b54223a6e34cfaf35f0',
    'QUANTUM-RO-THEOREM.md': '94c8f29121760d1a09358257720bb123613084f07a645db9ba9296a43e49a607',
    'QUANTUM-COVERAGE-THEOREM.md': '24a031417b42ba03d266c638a4c3f94dae8887ffd8cf13f584b21387e6d01217',
    'QUANTUM-EVENT-SPECIFIC-THEOREM.md': 'd28e99570c0b6819f7a45169882252ffedc6e31cfad150751f7084a9fdea02f1',
    'CHANGED-CHILD-EXTRACTION.md': '03b11cebd09f26ba07bcf686b0e28521d7d89a636877217421a59774d3a0991c',
    'bounds.py': '2e0849d60bde394397ef917d667d8a547c910868b571157d6a26f8140eb338cd',
    'bounds-event-specific.py': '4f06f80befae967479a582fb644d4d24bcb40b9051324709f529abcf683a8a81',
    'C:/Users/angel/Desktop/paper/PAPERS/LUGEL/research/lula22/publications/LULA-I/release/code/lula1/src/lib.rs': 'ac8e67f05af68dd8e1291c5909847f74103903fb7ffa2c70f500c6ec48f14210',
}
original_goals = {
    'C:/Users/angel/.codex/attachments/032bcc59-5956-41c6-88fb-1d3d3779005f/pasted-text-1.txt': '655c5344c76c16d6e22d15ab169847385154a147dd28d0d31f1bbe86b465ee2f',
    'C:/Users/angel/.codex/attachments/7ca7dd75-961c-425a-94a2-2bc006720d14/pasted-text-1.txt': 'ccdcfbc8b10de3d10546573ea9d92c0f906b182dcb34ba2eb100225bb206a1e8',
}
for group in (provenance, preserved, original_goals):
    check_pins(group)

# Replay exact structural controls in a NEW directory, not the immutable packet.
replay = B / 'final-control-replay'
replay.mkdir(exist_ok=True)
for name in ('finite_controls.py', 'INDEPENDENT-FIRST.md'):
    target = replay / name
    if target.exists():
        assert target.read_bytes() == (B / name).read_bytes()
    else:
        target.write_bytes((B / name).read_bytes())
result = subprocess.run([sys.executable, str(replay / 'finite_controls.py')], capture_output=True, text=True)
assert result.returncode == 0, result.stderr
assert (replay / 'FINITE-CONTROLS.json').read_bytes() == (B / 'FINITE-CONTROLS.json').read_bytes()

audit = '''# Resumed guarded-domain audit

Both complete original objective attachments and this reviewer's independently
saved first proof and reciprocal receipt were reread. The final root subject was
then read in full and checked against the actual release source and the fixed
joint classical theorem. No new source-uniform defect was found.

## Source anchors and exact scope

- `lib.rs:121–147`: one literal framed hash; source 24-block tail scratch.
  Its largest variable input is the ordered r-node FORS compressor, so r<=94
  gives ceil((22+16r+9)/64)<=24. Arbitrary raw adversarial words have no such
  length restriction. This is a full-hash RO schema, not a compression oracle.
- `lib.rs:161–187`: private F and message J frames, full256 inner word and
  52-byte outer frame. No private-J/inner vs typed alias is assumed away at S=0;
  the single outer seed-zero charge handles it. K=P or P=S by themselves do not
  invalidate the nonzero-S literal-frame separation.
- `lib.rs:212–235,269–276`: fixed lw4/8, lfull=128/lw, active ell=lfull-z;
  omitted digits really are checked zero. Hence acceptance probability is
  coefficient(S;ell,w)/w^lfull, not coefficient/w^ell. Its rare/finite-bottom
  law is retained, with no successful-row normalization. Strict Smax guarantees
  a nonterminal verifier step even on an unexposed row; endpoint-only maximal
  sums are outside this proof, although representable by the code.
- `lib.rs:333–412`: r=k-1 real FORS trees; the forced coordinate exposes no
  secret. Global parent indices are j*2^(a-level)+(leaf>>level). Ordered root
  inputs retain multiplicity and order, even if numerical node values coincide.
- `lib.rs:470–495`: below+height shift must be <=63 and leaf height <=31.
  A zero-height layer still has a distinct layer ID and a single addressed
  WOTS leaf. Child g=(tree<<height)|leaf is message independent.
- `lib.rs:512–595,601–668`: cache correctness requires a consistent honest
  top segment with canonical first counters and true authentication data.
  A cache is not an arbitrary table of accepted counters. Actual invoked
  unsuccessful search is absorbing, unused rows need not all succeed, and
  the atomic interface reveals neither partial work nor timing/private bytes.
- `lib.rs:679–729`: exact signature-length and digest filters remain strict.
  Accepted layer i completes exactly ell_i(w_i-1)-S_i chain calls.

## Uniform coupling obligations

The subject reconstructs the same ordinary complete raw function by acyclic
addressed restrictions and fresh residual cells; it does not replace one shared
oracle by independent named primitives. Canonical metadata, endpoints and public
roots form a safe surface; hidden starts/interiors, full F and postaccept row
answers do not. The unflagged ghost never routes on an undisclosed coordinate or
private guess flag. Only source observations and queried/honest replies agree
up to first bad; complete unqueried functions need not agree. Permanent suffix
disclosure and install-only-if-fresh memoization preserve the unused-coordinate
property. There is no public adversarial slot during an atomic request or after
an absorbing noncompletion, so an unsigned J coin has not leaked in a failed
partial request before a later public slot.

Strict-target and full128 decoding yield the uniform accepted-witness cover;
no unexposed-row canonicality premise is inserted. The raw 3Q fee accounts for
overlapping inner and H/G risks in one continued world, not separate advice
worlds or a false one-query partition. Full256 U, distinct inner inputs even for
repeated nonces, and the common preview flags retain the N^2 bridge denominator.
The coverage argument uses independent padded coins only after its stop, not
postselection on an actual surviving execution. Counts q and Q+1 are pathwise;
an expected eligible-query count is insufficient.

## What is and is not concluded

The final constants are H=r+sum tails, G=r(a+1)+1+sum(tails+1+h_i), and
C=H+G+d+3=r(a+2)+2sum tails+h+2d+4, including seed zero exactly once.
Baseline H3017/G3217/C6242 agrees with the preserved fixed joint theorem.
The min1 envelope is a manual classical source-RO statement for guarded
ex-ante parameters and an atomic partial interface. Rare completion can make
the theorem unhelpful for availability; no successful retuning follows.
No retuned QROM, fixed-SHA hardness, optimal attack lower bound, AES resource
normalization, new kernel/source-game theorem or completed original goal follows.
The limitation Q<N/6 for this half-success certificate is a limitation of this
particular sufficient upper bound, not an attack or impossibility theorem.
'''
(B / 'RESUMED-DOMAIN-AUDIT.md').write_text(audit, encoding='utf-8')

review = '''# Final independent subject review

**ACCEPTED — manual guarded parameter-uniform classical source theorem.**

Subject: `PARAMETER-UNIFORM-CLASSICAL-THEOREM.md`.
SHA256: `''' + subject_hash + '''`.

No unresolved mathematical or scope defect was found in the exact subject.
This acceptance follows an independently saved source-first derivation, a
reciprocal technical comparison, and a resumed complete-objective/source audit.
The final root synthesis was read after those records; no new claim of blindness
is made for the final read. Original first proofs and reciprocal receipts remain
byte unchanged.

The complete guarded quantification in Section1 is essential. Sections2–3
retain ordinary fullraw REAL marginal, canonical-row bottom law, safe-surface
unused-coordinate coupling, honest atomic noncompletion and exhaustive H/G/D7/
coverage descent. Section4 rederives variable terminal counts and the same joint
3Q+2q ledger. Section5 uses the full256 bridge and exact finite-binomial law with
pathwise padding. Section6 combines these in one stopped world and charges S=0
once. Honest canonical cache transfer has loss0 under the stated interface.

The omitted-zero coefficient denominator is exactly 2^128, even when ell is
shortened. This keeps partial-row availability distinct from a 1/N residual
target-match fee. Zero-height, d1, B1, q0 and a full256 digest partition are
compatible edge cases; strict maximal-sum exclusion is essential for unexposed
WOTS completeness. The source-buffer, shift and address guards are preserved.

Finite supporting controls were replayed in a fresh reviewer-owned directory:
exit0 and byte-identical output. They check 36 occupancy/coverage dimensions,
98 chain cases, 1280 FORS parent schedules, 91 route cases and four symbolic
constant instances. They support local identities, not the entire source-game
proof. Full argument and exact source anchors are in RESUMED-DOMAIN-AUDIT.md
and the preserved independent first proof.

Historical theorems, calculators and cryptographic source match their prior
pins. No manuscript/source edit, source execution, signature, measurement or
remote operation was made. This is a final-subject review, not a current-index
integration receipt. New checked declarations0; new checked source/game
declarations0. No retuned QROM or parameter repair is proved. The original
complete adequate level/category/security objective remains open.
'''
(B / 'FINAL-SUBJECT-REVIEW.md').write_text(review, encoding='utf-8')

checks = {name: True for name in [
    'exact_final_subject_hash_and_full_read',
    'both_original_goals_reread_in_full',
    'independent_source_first_precedes_new_peer_read',
    'ex_ante_parameters_and_guarded_source_schema',
    'source_shifts_addresses_buffer_and_full256_budget',
    'fixed_lw4_8_and_full128_omitted_zero_filter',
    'acceptance_coefficient_denominator_2pow128',
    'strict_target_excludes_endpoint_only_unexposed_gap',
    'one_genuine_child_and_acyclic_injective_graph',
    'ordinary_complete_shared_raw_REAL_marginal_lower_limbs',
    'canonical_first_counter_bottom_no_global_conditioning',
    'safe_surface_no_full_secret_or_surplus_row_advice',
    'one_unflagged_ghost_and_unused_remaining_coordinates',
    'known_point_memo_firstbad_forward_exposure_closure',
    'atomic_unsigned_J_and_absorbing_noncompletion',
    'uniform_exhaustive_four_event_source_cover',
    'simultaneous_3Q_2q_role_and_honest_fees',
    'recomputed_variable_H_G_d_terminal_counts',
    'single_outer_seedzero_fee_and_baseline6242',
    'full256_message_bridge_and_repeated_nonce_handling',
    'exact_finite_binomial_coverage_and_counter_bottom',
    'same_world_independent_padding_pathwise_Qplus1',
    'zero_height_B1_q0_and_full256_edges',
    'honest_canonical_cache_transfer_only',
    'certificate_limitation_not_attack_or_impossibility',
    'no_retuned_QROM_category_or_repair_inference',
    'controls_replayed_exit0_identical',
    'all_source_historical_and_first_pins_unchanged',
    'current_index_promotion_outside_this_receipt',
]}
receipt = dict(
    status='ACCEPTED_MANUAL_GUARDED_PARAMETER_UNIFORM_CLASSICAL_FINAL_SUBJECT',
    reviewed_at_utc=datetime.now(timezone.utc).isoformat(),
    subject=subject, subject_sha256=subject_hash, checks=checks,
    source_subjects={subject: subject_hash}, provenance_pins=provenance,
    original_goal_pins=original_goals, preserved_artifacts=preserved,
    review_pins={str((B / name).relative_to(X)).replace('\\','/'): sha(B/name)
                 for name in ['RESUMED-DOMAIN-AUDIT.md','FINAL-SUBJECT-REVIEW.md','final_subject_review.py']},
    control_replay=dict(exit_code=result.returncode, stdout=result.stdout.strip(),
                        script_sha256=sha(replay/'finite_controls.py'),
                        output_sha256=sha(replay/'FINITE-CONTROLS.json'),
                        byte_identical_to_preserved_controls=True),
    final_subject_only_not_index_integration=True,
    new_checked_declarations=0, new_source_game_declarations=0,
    retuned_QROM_bound_established=False, parameter_repair_established=False,
    original_level_category_objective_established=False, whole_goal_complete=False,
)
check_pins(provenance)
check_pins(preserved)
assert sha(X / subject) == subject_hash
(B/'FINAL-SUBJECT-REVIEW.json').write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf-8')
print(json.dumps(dict(status=receipt['status'],checks=len(checks),
    subject_sha256=subject_hash, receipt_sha256=sha(B/'FINAL-SUBJECT-REVIEW.json'),
    markdown_sha256=sha(B/'FINAL-SUBJECT-REVIEW.md'),
    resumed_audit_sha256=sha(B/'RESUMED-DOMAIN-AUDIT.md'),whole_goal_complete=False)))
