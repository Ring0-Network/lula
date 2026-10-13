"""A byte-encoding overlap control, not a secret-key recovery attack."""
import hashlib, json
from pathlib import Path
sk_prf=bytes([49])*16
pk_seed=bytes([82])*16
root=bytes([117])*16
m1=b"fresh raw message"
m0=root+m1
prf_input=sk_prf+pk_seed+m0
hmsg_input=sk_prf+pk_seed+root+m1
assert prf_input==hmsg_input
assert hashlib.sha256(prf_input).digest()[:16]==hashlib.sha256(hmsg_input).digest()[:16]
out={"status":"COMPUTED_ENCODING_COUNTEREXAMPLE_NOT_A_FORGERY",
 "condition":"R equals secret sk_prf; m0=pk_root||m1",
 "same_raw_sha256_input":True,"same_first_16_output_bytes":True,
 "attack_demonstrated":False,
 "required_lemma":"single-RO bad-overlap/secret-query bound rather than unconditional independent named oracles"}
Path(__file__).with_name("DOMAIN_OVERLAP_CONTROL.json").write_text(json.dumps(out,indent=2)+"\n",encoding="utf-8")
print(json.dumps(out,indent=2))
