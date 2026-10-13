require import AllCore List Distr DInterval.

(* Candidate lists are fixed before hidden keys are sampled.
   This is a key-blind ideal-game lemma, not a source-level LULA reduction. *)

lemma uniform_atom_bound (n x : int) :
  0 < n => mu1 (dinter 0 (n-1)) x <= 1%r / n%r.
proof.
  move=> hn.
  rewrite dinter1E.
  have -> : n - 1 - 0 + 1 = n by ring.
  case (0 <= x <= n-1); smt().
qed.

lemma one_seed_hit_bound (n : int) (candidates : int list) :
  0 < n =>
  mu (dinter 0 (n-1)) (mem candidates)
  <= (size candidates)%r * (1%r / n%r).
proof.
  move=> hn.
  apply mu_mem_le_mu1.
  by move=> x; apply uniform_atom_bound.
qed.

lemma two_seed_hit_bound (n : int) (prefixes suffixes : int list) :
  0 < n =>
  mu (dinter 0 (n-1) `*` dinter 0 (n-1))
    (fun (keys : int * int) => keys.`1 \in prefixes \/ keys.`2 \in suffixes)
  <= (size prefixes + size suffixes)%r * (1%r / n%r).
proof.
  move=> hn.
  have hp := one_seed_hit_bound n prefixes hn.
  have hs := one_seed_hit_bound n suffixes hn.
  have hu := le_dprod_or (dinter 0 (n-1)) (dinter 0 (n-1))
    (mem prefixes) (mem suffixes).
  have hz : 0 <= n - 1 by smt().
  rewrite fromintD RField.mulrDl.
  move: hu.
  rewrite !weight_dinter hz /=.
  smt().
qed.

module KeyBlind = {
  proc sample(prefixes suffixes : int list, n : int) : bool = {
    var keys : int * int;
    keys <$ dinter 0 (n-1) `*` dinter 0 (n-1);
    return keys.`1 \in prefixes \/ keys.`2 \in suffixes;
  }
}.

lemma key_blind_game_bound (n : int) (prefixes suffixes : int list) :
  0 < n =>
  phoare [KeyBlind.sample : arg = (prefixes,suffixes,n) ==> res]
    <= ((size prefixes + size suffixes)%r * (1%r / n%r)).
proof.
  move=> hn.
  proc; rnd; skip; auto=> />.
  by apply two_seed_hit_bound.
qed.
