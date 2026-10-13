import Mathlib.Data.List.Forall2
import Mathlib.Data.List.TakeDrop

/-!
# A fixed-sum antichain property for pointwise-ordered lists of naturals

Checked with Lean `v4.28.0` and Mathlib `v4.28.0`
(commit `8f9d9cff6bd728b17a24e163c9402775d9e6a365`).
-/

namespace IndependentLula

/-- If two lists of naturals are pointwise `≤` and have the same sum, they are equal. -/
theorem fixed_sum_antichain {x y : List Nat}
    (hle : List.Forall₂ (· ≤ ·) x y) (hs : x.sum = y.sum) : x = y := by
  induction hle with
  | nil => rfl
  | @cons a b l₁ l₂ hab hrest ih =>
    have hmono : ∀ {u v : List Nat}, List.Forall₂ (· ≤ ·) u v → u.sum ≤ v.sum := by
      intro u v h
      induction h with
      | nil => exact Nat.le_refl _
      | cons h₁ _ ih' => simp only [List.sum_cons]; omega
    have h₂ := hmono hrest
    simp only [List.sum_cons] at hs
    have hab' : a = b := by omega
    have hl : l₁.sum = l₂.sum := by omega
    rw [hab', ih hl]

end IndependentLula

#print axioms IndependentLula.fixed_sum_antichain
