// UNCHECKED: K is unavailable in the inspected WSL environment.
// Abstract boundary model only. Not extracted from Rust.
module CACHE-SYNTAX
  imports INT-SYNTAX
  imports BOOL-SYNTAX
  syntax CacheKind ::= "empty" | "fresh" | "stale" | "corrupt"
  syntax Outcome ::= "signed" "(" Int ")" | "abort" | "pending"
  syntax Command ::= "honest" "(" CacheKind "," Int "," Bool ")"
                   | "checked" "(" CacheKind "," Int "," Bool ")"
                   | "trusted" "(" CacheKind "," Int "," Bool ")"
                   | Outcome
endmodule

module CACHE
  imports CACHE-SYNTAX
  imports INT
  imports BOOL
  configuration <k> $PGM:Command </k>

  // Bool says the reference computation completed; pending models partiality.
  rule <k> honest(K:CacheKind, S:Int, false) => pending </k>
  rule <k> honest(empty, S:Int, true) => signed(S) </k>
  rule <k> honest(fresh, S:Int, true) => signed(S) </k>
  rule <k> honest(stale, S:Int, true) => signed(S) </k>
  // A corrupt state is deliberately not admitted to the honest equivalence.
  rule <k> honest(corrupt, S:Int, true) => abort </k>

  // This is a proposed guarded wrapper specification, NOT actual Rust behavior.
  rule <k> checked(corrupt, S:Int, B:Bool) => abort </k>
  rule <k> checked(K:CacheKind, S:Int, B:Bool) => honest(K, S, B) </k>
       requires K =/=K corrupt

  // S is the cache-influenced result. No equality with reference is stipulated.
  rule <k> trusted(K:CacheKind, S:Int, true) => signed(S) </k>
  rule <k> trusted(K:CacheKind, S:Int, false) => pending </k>
endmodule
