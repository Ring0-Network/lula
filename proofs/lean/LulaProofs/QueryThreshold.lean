import Mathlib.Order.Monotone.Basic
import Mathlib.Order.MinMax

namespace LulaQueryThreshold

variable {α : Type*} [LinearOrder α]

def Certified (f : Nat → α) (target : α) (q : Nat) : Prop := f q ≤ target

theorem cap_monotone (f : Nat → α) (hf : Monotone f) (cap : α) :
    Monotone (fun q => min cap (f q)) := by
  intro a b hab
  exact min_le_min le_rfl (hf hab)

theorem minimum_monotone (f g : Nat → α) (hf : Monotone f) (hg : Monotone g) :
    Monotone (fun q => min (f q) (g q)) := by
  intro a b hab
  exact min_le_min (hf hab) (hg hab)

theorem cap_preserves_strict_failure (target cap value : α)
    (hcap : target < cap) (hvalue : target < value) :
    target < min cap value := by
  exact lt_min hcap hvalue

theorem certified_prefix (f : Nat → α) (hf : Monotone f) (target : α)
    {q k : Nat} (hq : q ≤ k) (hk : Certified f target k) :
    Certified f target q := by
  exact le_trans (hf hq) hk

theorem failed_suffix (f : Nat → α) (hf : Monotone f) (target : α)
    {q k : Nat} (hk : target < f k) (hq : k ≤ q) : target < f q := by
  exact lt_of_lt_of_le hk (hf hq)

theorem adjacent_boundary (f : Nat → α) (hf : Monotone f) (target : α)
    (k : Nat) (hk : Certified f target k) (hnext : target < f (k + 1)) :
    ∀ q, Certified f target q ↔ q ≤ k := by
  intro q
  constructor
  · intro hcert
    by_contra hnot
    have hgt : k < q := lt_of_not_ge hnot
    have hstep : k + 1 ≤ q := Nat.succ_le_of_lt hgt
    have hfailed : target < f q := failed_suffix f hf target hnext hstep
    exact (not_lt_of_ge hcert) hfailed
  · intro hq
    exact certified_prefix f hf target hq hk

theorem no_certified_budget_if_zero_fails (f : Nat → α) (hf : Monotone f)
    (target : α) (hzero : target < f 0) :
    ∀ q, ¬ Certified f target q := by
  intro q hcert
  exact (not_lt_of_ge hcert) (failed_suffix f hf target hzero (Nat.zero_le q))

#print axioms cap_monotone
#print axioms minimum_monotone
#print axioms cap_preserves_strict_failure
#print axioms certified_prefix
#print axioms failed_suffix
#print axioms adjacent_boundary
#print axioms no_certified_budget_if_zero_fails

end LulaQueryThreshold
