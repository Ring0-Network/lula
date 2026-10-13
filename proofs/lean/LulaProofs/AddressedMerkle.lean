import Mathlib.Data.List.Forall2
import Mathlib.Data.List.TakeDrop

namespace LulaTree

abbrev Node (n : Nat) := { bytes : List UInt8 // bytes.length = n }

theorem split_fixed_left {A : Type} (left right otherLeft otherRight : List A)
    (hlen : left.length = otherLeft.length)
    (he : left ++ right = otherLeft ++ otherRight) :
    left = otherLeft ∧ right = otherRight := by
  induction left generalizing otherLeft with
  | nil =>
      cases otherLeft with
      | nil => exact ⟨rfl, he⟩
      | cons b bs => simp at hlen
  | cons a xs ih =>
      cases otherLeft with
      | nil => simp at hlen
      | cons b bs =>
          simp only [List.length_cons, Nat.succ.injEq] at hlen
          simp only [List.cons_append, List.cons.injEq] at he
          rcases ih bs hlen he.2 with ⟨hl, hr⟩
          exact ⟨by simpa [hl] using congrArg (fun v => v :: bs) he.1, hr⟩

theorem cancel_prefix {A : Type} (header left right : List A)
    (he : header ++ left = header ++ right) : left = right := by
  induction header with
  | nil => exact he
  | cons a xs ih =>
      simp only [List.cons_append, List.cons.injEq] at he
      exact ih he.2

def frame {Addr : Type} {n : Nat} (header : Addr → List UInt8)
    (address : Addr) (left right : Node n) : List UInt8 :=
  header address ++ (left.val ++ right.val)

theorem frame_children_injective {Addr : Type} {n : Nat}
    (header : Addr → List UInt8) (address : Addr)
    (left right otherLeft otherRight : Node n)
    (he : frame header address left right = frame header address otherLeft otherRight) :
    left = otherLeft ∧ right = otherRight := by
  have hc := cancel_prefix (header address) (left.val ++ right.val)
    (otherLeft.val ++ otherRight.val) he
  have hl : left.val.length = otherLeft.val.length := left.property.trans otherLeft.property.symm
  rcases split_fixed_left left.val right.val otherLeft.val otherRight.val hl hc with ⟨h₁, h₂⟩
  exact ⟨Subtype.ext h₁, Subtype.ext h₂⟩

structure Step (Addr : Type) (n : Nat) where
  address : Addr
  currentOnRight : Bool
  sibling : Node n
  deriving DecidableEq

def input {Addr : Type} {n : Nat} (header : Addr → List UInt8)
    (s : Step Addr n) (current : Node n) : List UInt8 :=
  if s.currentOnRight then frame header s.address s.sibling current
  else frame header s.address current s.sibling

def schedule {Addr : Type} {n : Nat} (path : List (Step Addr n)) : List (Addr × Bool) :=
  path.map (fun s => (s.address, s.currentOnRight))

def root {Addr : Type} {n : Nat} (H : List UInt8 → Node n)
    (header : Addr → List UInt8) : Node n → List (Step Addr n) → Node n
  | current, [] => current
  | current, s :: rest => root H header (H (input header s current)) rest

def trace {Addr : Type} {n : Nat} (H : List UInt8 → Node n)
    (header : Addr → List UInt8) : Node n → List (Step Addr n) → List (Addr × List UInt8)
  | _, [] => []
  | current, s :: rest =>
      (s.address, input header s current) :: trace H header (H (input header s current)) rest

theorem same_root_agreement_or_witness {Addr : Type} {n : Nat}
    (H : List UInt8 → Node n) (header : Addr → List UInt8)
    (path₁ path₂ : List (Step Addr n)) (leaf₁ leaf₂ : Node n)
    (hs : schedule path₁ = schedule path₂)
    (hr : root H header leaf₁ path₁ = root H header leaf₂ path₂) :
    (leaf₁ = leaf₂ ∧ path₁ = path₂) ∨
      ∃ address x y,
        (address, x) ∈ trace H header leaf₁ path₁ ∧
        (address, y) ∈ trace H header leaf₂ path₂ ∧
        x ≠ y ∧ H x = H y := by
  induction path₁ generalizing path₂ leaf₁ leaf₂ with
  | nil =>
      cases path₂ with
      | nil => exact Or.inl ⟨hr, rfl⟩
      | cons t ts => simp [schedule] at hs
  | cons s ss ih =>
      cases path₂ with
      | nil => simp [schedule] at hs
      | cons t ts =>
          simp only [schedule, List.map_cons, List.cons.injEq, Prod.mk.injEq] at hs
          rcases hs with ⟨⟨ha, hd⟩, htail⟩
          have hr' : root H header (H (input header s leaf₁)) ss =
              root H header (H (input header t leaf₂)) ts := hr
          rcases ih ts (H (input header s leaf₁)) (H (input header t leaf₂)) htail hr' with
            ⟨hparent, hrest⟩ | ⟨a, x, y, hx, hy, hne, heq⟩
          · by_cases hi : input header s leaf₁ = input header t leaf₂
            · rcases s with ⟨a, d, sib₁⟩
              rcases t with ⟨b, e, sib₂⟩
              simp only at ha hd
              subst b
              subst e
              cases d <;> simp only [input, Bool.false_eq_true, ↓reduceIte] at hi
              · rcases frame_children_injective header a leaf₁ sib₁ leaf₂ sib₂ hi with ⟨hleaf, hsib⟩
                exact Or.inl ⟨hleaf, by simp [hsib, hrest]⟩
              · rcases frame_children_injective header a sib₁ leaf₁ sib₂ leaf₂ hi with ⟨hsib, hleaf⟩
                exact Or.inl ⟨hleaf, by simp [hsib, hrest]⟩
            · exact Or.inr ⟨s.address, input header s leaf₁, input header t leaf₂,
                by simp [trace],
                by simp only [trace, List.mem_cons]; exact Or.inl (by simp [ha]), hi, hparent⟩
          · exact Or.inr ⟨a, x, y,
              by simp only [trace, List.mem_cons]; exact Or.inr hx,
              by simp only [trace, List.mem_cons]; exact Or.inr hy, hne, heq⟩

theorem changed_leaf_or_path_yields_witness {Addr : Type} {n : Nat}
    (H : List UInt8 → Node n) (header : Addr → List UInt8)
    (path₁ path₂ : List (Step Addr n)) (leaf₁ leaf₂ : Node n)
    (hs : schedule path₁ = schedule path₂)
    (hr : root H header leaf₁ path₁ = root H header leaf₂ path₂)
    (hd : leaf₁ ≠ leaf₂ ∨ path₁ ≠ path₂) :
    ∃ address x y,
      (address, x) ∈ trace H header leaf₁ path₁ ∧
      (address, y) ∈ trace H header leaf₂ path₂ ∧
      x ≠ y ∧ H x = H y := by
  rcases same_root_agreement_or_witness H header path₁ path₂ leaf₁ leaf₂ hs hr with
    ⟨hleaf, hpath⟩ | hw
  · rcases hd with hn | hn
    · exact False.elim (hn hleaf)
    · exact False.elim (hn hpath)
  · exact hw

#print axioms split_fixed_left
#print axioms cancel_prefix
#print axioms frame_children_injective
#print axioms same_root_agreement_or_witness
#print axioms changed_leaf_or_path_yields_witness
end LulaTree
