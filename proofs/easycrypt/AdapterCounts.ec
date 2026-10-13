require import AllCore.

(* Abstract byte-word routing helper.  This is not the complete Rust model. *)
type addr.
type msg.
type word.

module type PRIVATE = {
  proc derive(a : addr) : word
  proc randomizer(m : msg) : word
}.

module Adapter(C : PRIVATE) = {
  proc secret(a : addr) : word = {
    var v;
    v <@ C.derive(a);
    return v;
  }
  proc nonce(m : msg) : word = {
    var v;
    v <@ C.randomizer(m);
    return v;
  }
}.

(* Procedural consistency under a common challenger; no cryptographic axiom. *)
lemma secret_adapter_equiv (C <: PRIVATE) :
  equiv [Adapter(C).secret ~ Adapter(C).secret :
    ={arg, glob C} ==> ={res, glob C}].
proof. proc; sim. qed.

lemma nonce_adapter_equiv (C <: PRIVATE) :
  equiv [Adapter(C).nonce ~ Adapter(C).nonce :
    ={arg, glob C} ==> ={res, glob C}].
proof. proc; sim. qed.

lemma private_cold_caps (q : int) :
  0 <= q =>
  2181038080 + 33567232*q <= 2181038080 + 33567393*q.
proof. smt(). qed.

lemma private_hot_caps (q : int) :
  0 <= q =>
  2181038080 + 12816*q <= 2181038080 + 12961*q.
proof. smt(). qed.

lemma private_hot_le_cold (q : int) :
  0 <= q =>
  2181038080 + 12816*q <= 2181038080 + 33567232*q.
proof. smt(). qed.
