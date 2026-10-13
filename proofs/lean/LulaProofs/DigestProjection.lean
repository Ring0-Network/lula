import Mathlib.Data.List.TakeDrop

namespace LulaDigestProjection

abbrev Word256 := Fin 256 → Bool
abbrev Prefix128 := Fin 128 → Bool

def embedPrefix (i : Fin 128) : Fin 256 :=
  ⟨i.val, Nat.lt_trans i.isLt (by decide)⟩

def takePrefix (d : Word256) : Prefix128 := fun i => d (embedPrefix i)

def zeroLower (d : Word256) : Word256 :=
  fun i => if i.val < 128 then d i else false

def routeIndex (i : Fin 41) : Fin 256 :=
  ⟨162 + i.val, Nat.lt_trans (Nat.add_lt_add_left i.isLt 162) (by decide)⟩

def filterIndex (i : Fin 9) : Fin 256 :=
  ⟨153 + i.val, Nat.lt_trans (Nat.add_lt_add_left i.isLt 153) (by decide)⟩

def route (d : Word256) : Fin 41 → Bool := fun i => d (routeIndex i)
def filterBits (d : Word256) : Fin 9 → Bool := fun i => d (filterIndex i)

theorem prefix_preserved (d : Word256) : takePrefix (zeroLower d) = takePrefix d := by
  funext i
  simp [takePrefix, zeroLower, embedPrefix, i.isLt]

theorem route_all_zero (d : Word256) : route (zeroLower d) = fun _ => false := by
  funext i
  have bound : 128 ≤ 162 + i.val :=
    Nat.le_trans (by decide : 128 ≤ 162) (Nat.le_add_right 162 i.val)
  simp [route, zeroLower, routeIndex, Nat.not_lt_of_ge bound]

theorem filter_all_zero (d : Word256) : filterBits (zeroLower d) = fun _ => false := by
  funext i
  have bound : 128 ≤ 153 + i.val :=
    Nat.le_trans (by decide : 128 ≤ 153) (Nat.le_add_right 153 i.val)
  simp [filterBits, zeroLower, filterIndex, Nat.not_lt_of_ge bound]

end LulaDigestProjection

#print axioms LulaDigestProjection.prefix_preserved
#print axioms LulaDigestProjection.route_all_zero
#print axioms LulaDigestProjection.filter_all_zero
