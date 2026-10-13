# Note: which Kudinov–Nick row is which (checked in the paper text copy `sources/hashsig-go/spec/eprint-2025-2203-kudinov-nick.txt`)

[read] The table row `W+C, h=44, d=4, a=16, k=8, w=256, l=16, S_wn=2040` has signature size 3,952 B and SigTime 3,571·10^4
compressions (35.7 million). At the 18.5 million compressions per second used in the user's table that is about 1.9 s, not 347 ms.
The row `h=40, d=5, a=14, k=11` is 4,612 B with 5.98 million compressions. The 4,036 B configuration used by the third-party
Go adapter is PORS+FP and is a different row of the author repository. The user's table value of 347 ms therefore does not
belong to the 3,952 B row.

[measured, smoke on an efficiency core, not a campaign number] the reconstruction signed in about 2.2 s, consistent with
35.7 million compressions at about 63 ns each.

Compressions per byte for the 3,952 B row is 2.16 in the paper's last column, just under the paper's own 2.6 bound.
