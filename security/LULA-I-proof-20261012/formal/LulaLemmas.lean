import Mathlib.Data.List.Forall2
import Mathlib.Data.List.TakeDrop

/- Abstract mathematical model only; no Rust refinement claim. -/
namespace Lula

theorem sum_monotone {x y : List Nat} (h : List.Forall₂ (· ≤ ·) x y) : x.sum ≤ y.sum := by
  induction h with
  | nil => simp
  | cons hab htail ih => simpa only [List.sum_cons] using Nat.add_le_add hab ih

theorem fixed_sum_antichain {x y : List Nat}
    (hle : List.Forall₂ (· ≤ ·) x y) (hs : x.sum = y.sum) : x = y := by
  induction hle with
  | nil => rfl
  | @cons a b xs ys hab htail ih =>
      have ht : xs.sum ≤ ys.sum := sum_monotone htail
      simp only [List.sum_cons] at hs
      have habEq : a = b := by omega
      have hsum : xs.sum = ys.sum := by omega
      subst b
      exact congrArg (List.cons a) (ih hsum)

def consistent {M S C : Type} (ref : M → Option S)
    (cached : M → C → Option S) (c : C) : Prop :=
  ∀ m, cached m c = ref m

theorem restored_cache_same {M S C : Type} (ref : M → Option S)
    (cached : M → C → Option S) (old fresh : C)
    (ho : consistent ref cached old) (hf : consistent ref cached fresh) :
    ∀ m, cached m old = cached m fresh := by
  intro m
  exact (ho m).trans (hf m).symm

/- A sequential adaptive protocol chooses the next message from prior responses.
   It is classical-query EUF-CMA, not superposition signing-oracle access. -/
def adaptiveRun {M S : Type} (oracle : M → Option S)
    (choose : List (Option S) → M) : Nat → List (Option S) → List (Option S)
  | 0, history => history
  | n + 1, history => adaptiveRun oracle choose n (history ++ [oracle (choose history)])

theorem adaptive_transcript_equal {M S : Type} (o₁ o₂ : M → Option S)
    (he : ∀ m, o₁ m = o₂ m) (choose : List (Option S) → M)
    (n : Nat) (history : List (Option S)) :
    adaptiveRun o₁ choose n history = adaptiveRun o₂ choose n history := by
  have ho : o₁ = o₂ := funext he
  subst o₂
  rfl

def restoredRun {M S C : Type} (cached : M → C → Option S)
    (pick : List (Option S) → C) (choose : List (Option S) → M) :
    Nat → List (Option S) → List (Option S)
  | 0, history => history
  | n + 1, history => restoredRun cached pick choose n
      (history ++ [cached (choose history) (pick history)])

theorem adaptive_restoration_equal {M S C : Type} (ref : M → Option S)
    (cached : M → C → Option S) (pick : List (Option S) → C)
    (choose : List (Option S) → M)
    (hc : ∀ history, consistent ref cached (pick history))
    (n : Nat) (history : List (Option S)) :
    restoredRun cached pick choose n history = adaptiveRun ref choose n history := by
  induction n generalizing history with
  | zero => rfl
  | succ n ih =>
      simp only [restoredRun, adaptiveRun, hc history (choose history)]
      exact ih _

/- We deliberately permit abort on corruption. Returning a value must agree
   with the reference; this property is an explicit hypothesis. -/
def outputSafe {M S C : Type} (ref : M → Option S)
    (cached : M → C → Option S) : Prop :=
  ∀ m c s, cached m c = some s → ref m = some s

theorem no_changed_success {M S C : Type} (ref : M → Option S)
    (cached : M → C → Option S) (hs : outputSafe ref cached)
    (m : M) (c : C) (s : S) (hr : ref m ≠ some s) : cached m c ≠ some s := by
  intro hc
  exact hr (hs m c s hc)

theorem equal_or_first_divergence {A : Type} [DecidableEq A] (x y : List A) :
    x = y ∨ ∃ i : Nat, x.take i = y.take i ∧ x[i]? ≠ y[i]? := by
  induction x generalizing y with
  | nil =>
      cases y with
      | nil => exact Or.inl rfl
      | cons b ys => exact Or.inr ⟨0, rfl, by simp⟩
  | cons a xs ih =>
      cases y with
      | nil => exact Or.inr ⟨0, rfl, by simp⟩
      | cons b ys =>
          by_cases hab : a = b
          · subst b
            rcases ih ys with h | ⟨i, hp, hd⟩
            · exact Or.inl (congrArg (List.cons a) h)
            · exact Or.inr ⟨i + 1, by simpa using congrArg (List.cons a) hp, by simpa using hd⟩
          · exact Or.inr ⟨0, rfl, by simpa using hab⟩

#print axioms fixed_sum_antichain
#print axioms sum_monotone
#print axioms restored_cache_same
#print axioms adaptive_transcript_equal
#print axioms adaptive_restoration_equal
#print axioms no_changed_success
#print axioms equal_or_first_divergence
end Lula
