# Owned Go adapter addition

The two owned files are code/adapters/go/hashsig_driver/main.go and qpc_windows.go. The pinned hashsig module does not contain this driver path. Install those files at go/cmd/hashsig_driver/ inside a separately obtained andrepatta/hashsig checkout at commit da711b11f03c4af0d610996f89848e9e15770b73, or apply hashsig-driver-addition.patch at that checkout's root. Use one method, not both. The patch adds our files only and includes no upstream implementation body or context.

The adapter must reside inside the upstream Go module because it imports that module's internal packages. Use the build conditions in code/PORTABLE_CODE.md. This assembly does not claim a new Go compilation, matched historical binary or benchmark. The imported library remains MIT, with its exact notice in LICENSE-hashsig-MIT.txt; our new adapter files are Apache-2.0.
