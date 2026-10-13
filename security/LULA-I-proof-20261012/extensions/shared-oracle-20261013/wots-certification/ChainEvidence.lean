import Mathlib.Data.List.Forall2
import Mathlib.Data.List.TakeDrop

namespace LulaWots

abbrev Node (n : Nat) := { bytes : List UInt8 // bytes.length = n }

theorem cancel_header {A : Type} (header left right : List A)
    (h : header ++ left = header ++ right) : left = right := by
  induction header with
  | nil => exact h
  | cons a rest ih =>
      simp only [List.cons_append, List.cons.injEq] at h
      exact ih h.2

def raw {Addr : Type} {n : Nat} (header : Addr → List UInt8)
    (address : Addr) (value : Node n) : List UInt8 := header address ++ value.val

theorem raw_value_injective {Addr : Type} {n : Nat}
    (header : Addr → List UInt8) (address : Addr) (a b : Node n)
    (h : raw header address a = raw header address b) : a = b :=
  Subtype.ext (cancel_header (header address) a.val b.val h)

def run {Addr : Type} {n : Nat} (H : List UInt8 → Node n)
    (header : Addr → List UInt8) : List Addr → Node n → Node n
  | [], start => start
  | address :: rest, start => run H header rest (H (raw header address start))

def trace {Addr : Type} {n : Nat} (H : List UInt8 → Node n)
    (header : Addr → List UInt8) : List Addr → Node n → List (Addr × List UInt8)
  | [], _ => []
  | address :: rest, start => (address, raw header address start) ::
      trace H header rest (H (raw header address start))

theorem chain_start_equal_or_witness {Addr : Type} {n : Nat}
    (H : List UInt8 → Node n) (header : Addr → List UInt8)
    (addresses : List Addr) (a b : Node n)
    (h : run H header addresses a = run H header addresses b) :
    a = b ∨ ∃ address x y,
      (address,x) ∈ trace H header addresses a ∧
      (address,y) ∈ trace H header addresses b ∧ x ≠ y ∧ H x = H y := by
  induction addresses generalizing a b with
  | nil => exact Or.inl h
  | cons address rest ih =>
      rcases ih (H (raw header address a)) (H (raw header address b)) h with
        hp | ⟨c,x,y,hx,hy,hn,he⟩
      · by_cases hab : a = b
        · exact Or.inl hab
        · have hn : raw header address a ≠ raw header address b := by
            intro he
            exact hab (raw_value_injective header address a b he)
          exact Or.inr ⟨address,raw header address a,raw header address b,
            by simp [trace], by simp [trace],hn,hp⟩
      · exact Or.inr ⟨c,x,y,
          by simp only [trace,List.mem_cons]; exact Or.inr hx,
          by simp only [trace,List.mem_cons]; exact Or.inr hy,hn,he⟩

theorem changed_chain_start_witness {Addr : Type} {n : Nat}
    (H : List UInt8 → Node n) (header : Addr → List UInt8)
    (addresses : List Addr) (a b : Node n)
    (h : run H header addresses a = run H header addresses b) (hn : a ≠ b) :
    ∃ address x y,
      (address,x) ∈ trace H header addresses a ∧
      (address,y) ∈ trace H header addresses b ∧ x ≠ y ∧ H x = H y := by
  rcases chain_start_equal_or_witness H header addresses a b h with he | hw
  · exact False.elim (hn he)
  · exact hw

theorem run_append {Addr : Type} {n : Nat}
    (H : List UInt8 → Node n) (header : Addr → List UInt8)
    (before after : List Addr) (start : Node n) :
    run H header (before ++ after) start = run H header after (run H header before start) := by
  induction before generalizing start with
  | nil => rfl
  | cons address rest ih => exact ih _

theorem last_step_preimage {Addr : Type} {n : Nat}
    (H : List UInt8 → Node n) (header : Addr → List UInt8)
    (before : List Addr) (last : Addr) (start target : Node n)
    (h : run H header (before ++ [last]) start = target) :
    ∃ x, x = raw header last (run H header before start) ∧ H x = target := by
  refine ⟨raw header last (run H header before start),rfl,?_⟩
  simpa only [run_append,run] using h

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
      have he : a = b := by omega
      have hsum : xs.sum = ys.sum := by omega
      subst b
      exact congrArg (List.cons a) (ih hsum)

#print axioms cancel_header
#print axioms raw_value_injective
#print axioms chain_start_equal_or_witness
#print axioms changed_chain_start_witness
#print axioms run_append
#print axioms last_step_preimage
#print axioms sum_monotone
#print axioms fixed_sum_antichain
end LulaWots
