import Mathlib.Logic.Function.Iterate

namespace LulaSPRSeparation

variable {α : Type*}

-- Perfect same-tweak second-preimage uniqueness can coexist with trivial inversion.
theorem identity_injective : Function.Injective (id : α → α) := by
  intro a b h
  exact h

theorem identity_chain (n : Nat) (x : α) : ((id : α → α)^[n]) x = x := by
  induction n with
  | zero => rfl
  | succ n ih => simpa only [Function.iterate_succ_apply, id_eq] using ih

def chainValues {ell : Nat} (secret : Fin ell → α) (digits : Fin ell → Nat) :
    Fin ell → α := fun i => ((id : α → α)^[digits i]) (secret i)

theorem identity_values_any_digits {ell : Nat} (secret : Fin ell → α)
    (e e' : Fin ell → Nat) : chainValues secret e = chainValues secret e' := by
  funext i
  simp only [chainValues, identity_chain]

theorem identity_has_public_inverse :
    ∃ inv : α → α, ∀ x : α, inv ((id : α → α) x) = x := by
  exact ⟨id, fun _ => rfl⟩

#print axioms identity_injective
#print axioms identity_chain
#print axioms identity_values_any_digits
#print axioms identity_has_public_inverse

end LulaSPRSeparation
