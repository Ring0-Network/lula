import hashlib
from pathlib import Path

HERE = Path(__file__).resolve().parent
PEER = HERE.parents[2] / "keyed-target-reader" / "restricted-row-qrom"
SCRIPT = PEER / "controls.py"
assert hashlib.sha256((PEER / "INDEPENDENT-FIRST.md").read_bytes()).hexdigest() == "44dcb6acf797cf27875eece1a9f52f6e8faf2c365a8a391d4d5a14812b1c419b"
assert hashlib.sha256(SCRIPT.read_bytes()).hexdigest() == "3a8d9ac5481fa74a1859e92082f25e840f40073629fd325d238c7a8ea092c9b5"
DEST = HERE / "peer-rerun"
DEST.mkdir(exist_ok=True)
text = SCRIPT.read_text(encoding="utf-8")
assert text.count("OUT = Path(__file__).resolve().parent") == 1
# Redirect only output destination in memory; never edit peer input/output files.
text = text.replace("OUT = Path(__file__).resolve().parent", "OUT = PEER_REVIEW_DEST")
exec(compile(text, str(SCRIPT), "exec"), {"__file__": str(SCRIPT), "PEER_REVIEW_DEST": DEST})
