require import AllCore.

(* Abstract total completion outcome. No hash-security or Rust claim. *)
type outcome = [ Abort | Signed of int ].
op reference : int -> outcome.
op valid : int -> bool.

module Ref = {
  proc sign(m : int) : outcome = {
    return reference m;
  }
}.

module Cached = {
  proc sign(m : int, c : int) : outcome = {
    var r : outcome;
    if (valid c) {
      r <- reference m;
    } else {
      r <- Abort;
    }
    return r;
  }
}.

lemma consistent_equivalence :
  equiv [Ref.sign ~ Cached.sign : ={m} /\ valid c{2} ==> ={res}].
proof.
  proc.
  if{2}; auto.
qed.

lemma abort_or_reference :
  forall m c,
  hoare [Cached.sign : arg = (m,c) ==> res = Abort \/ res = reference m].
proof.
  move=> m c.
  proc; if; auto.
qed.

lemma successful_response :
  forall m c s,
  hoare [Cached.sign : arg = (m,c) ==> res = Signed s => reference m = Signed s].
proof.
  move=> m c s.
  proc; if; auto.
qed.
