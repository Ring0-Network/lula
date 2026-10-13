import Mathlib.Algebra.Order.BigOperators.Ring.Finset
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Ring

namespace LulaQuantumSelector
open scoped BigOperators
variable {ι R : Type*} [Field R] [LinearOrder R] [IsStrictOrderedRing R]

-- The supplied roots represent sqrt(p_j), sqrt(b_j), and the vector-error terms.
-- Their interpretation and the quantum source-prefix inequality are hypotheses.
theorem sum_root_error_square (s : Finset ι) (a b e : ι → R)
    (ha : ∀ i ∈ s, 0 ≤ a i) (hb : ∀ i ∈ s, 0 ≤ b i)
    (he : ∀ i ∈ s, 0 ≤ e i) (h : ∀ i ∈ s, a i ≤ b i + e i) :
    (∑ i ∈ s, (a i)^2) ≤
      (∑ i ∈ s, (b i)^2) + 2*(∑ i ∈ s, b i*e i) + (∑ i ∈ s, (e i)^2) := by
  calc
    _ ≤ ∑ i ∈ s, (b i + e i)^2 := Finset.sum_le_sum fun i hi => by
      exact (sq_le_sq₀ (ha i hi) (add_nonneg (hb i hi) (he i hi))).2 (h i hi)
    _ = _ := by
      simp_rw [add_sq]
      simp only [Finset.sum_add_distrib, Finset.mul_sum, mul_assoc]

theorem mixed_sum_bound (s : Finset ι) (b e : ι → R) (c : R)
    (hc : 0 ≤ c)
    (hcsq : c^2 = (∑ i ∈ s, (b i)^2)*(∑ i ∈ s, (e i)^2)) :
    (∑ i ∈ s, b i*e i) ≤ c := by
  have hCS := Finset.sum_mul_sq_le_sq_mul_sq s b e
  rw [← hcsq] at hCS
  nlinarith [sq_nonneg ((∑ i ∈ s, b i*e i) + c)]

theorem padded_root_upper (s : Finset ι) (a b e : ι → R)
    (L bbar deltaCut cross : R)
    (ha : ∀ i ∈ s, 0 ≤ a i) (hb : ∀ i ∈ s, 0 ≤ b i)
    (he : ∀ i ∈ s, 0 ≤ e i) (h : ∀ i ∈ s, a i ≤ b i + e i)
    (hB : (∑ i ∈ s, (b i)^2) = L*bbar)
    (hD : (∑ i ∈ s, (e i)^2) = deltaCut)
    (hc : 0 ≤ cross) (hcSq : cross^2 = L*bbar*deltaCut) :
    (∑ i ∈ s, (a i)^2) ≤ L*bbar + 2*cross + deltaCut := by
  have hsum := sum_root_error_square s a b e ha hb he h
  have hcross := mixed_sum_bound s b e cross hc (by simpa [hB,hD] using hcSq)
  rw [hB,hD] at hsum
  linarith

omit [IsStrictOrderedRing R] in
theorem cap_padded_probability (P total envelope : R)
    (hprob : P ≤ 1) (hsource : P ≤ total) (henvelope : total ≤ envelope) :
    P ≤ min 1 envelope := le_min hprob (le_trans hsource henvelope)

-- Exact source inventory and padded selector arithmetic, not a source theorem.
theorem interior_cut_count :
    32*14*(2^41+2^36+2^31+2^26 : Nat)+16*254*2^21 = 1016949404336128 := by decide

theorem protected_union_count :
    32*15*(2^41+2^36+2^31+2^26 : Nat)+16*255*2^21+2^41*17*512 =
      20229886488608768 := by decide

theorem padded_namespace :
    (2^54 : Nat) < 20229886488608768 ∧ 20229886488608768 < 2^55 := by decide

end LulaQuantumSelector
#print axioms LulaQuantumSelector.sum_root_error_square
#print axioms LulaQuantumSelector.mixed_sum_bound
#print axioms LulaQuantumSelector.padded_root_upper
#print axioms LulaQuantumSelector.cap_padded_probability
#print axioms LulaQuantumSelector.interior_cut_count
#print axioms LulaQuantumSelector.protected_union_count
#print axioms LulaQuantumSelector.padded_namespace
