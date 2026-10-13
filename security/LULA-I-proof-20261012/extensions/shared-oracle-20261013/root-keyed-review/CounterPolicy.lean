import Mathlib.Data.List.TakeDrop

/-
An abstract counter-policy separation, not LULA/SHA or its actual digit predicate.
Registerable bases are Bool; counter zero emits a common label, later counters
emit a base-specific label. Both policies satisfy the same acceptance predicate.
These declarations check the countermodel only, not a security reduction.
-/
namespace LulaCounterPolicy

def toyHash (base : Bool) (counter : Nat) : Nat :=
  if counter = 0 then 0 else if base then 2 else 1

def accepts (value : Nat) : Prop := value ≤ 2

theorem both_policies_accepted (base : Bool) :
    accepts (toyHash base 0) ∧ accepts (toyHash base 1) := by
  cases base <;> simp [accepts, toyHash]

theorem canonical_policy_collision (base : Bool) :
    (!base) ≠ base ∧ toyHash (!base) 0 = toyHash base 0 := by
  cases base <;> decide

theorem later_policy_no_changed_base_collision (base other : Bool) (counter : Nat)
    (hdiff : other ≠ base) : toyHash other counter ≠ toyHash base 1 := by
  cases base <;> cases other <;> try exact (hdiff rfl).elim
  all_goals by_cases hc : counter = 0 <;> simp [toyHash, hc]

theorem no_finite_factor_from_zero_success (factor : Nat) :
    ¬ (1 ≤ factor * 0) := by simp

#print axioms both_policies_accepted
#print axioms canonical_policy_collision
#print axioms later_policy_no_changed_base_collision
#print axioms no_finite_factor_from_zero_success
end LulaCounterPolicy
