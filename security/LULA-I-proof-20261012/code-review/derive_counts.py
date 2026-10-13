"""Source binding and symbolic object counts; no signing or cache generation."""
from pathlib import Path
import hashlib, json

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
paths = {
    "original": ROOT / "R6/R6A-state-as-accelerator/work/rust/src/lib.rs",
    "private": ROOT / "publications/LULA-I/private/implementation/work/rust/src/lib.rs",
    "release": ROOT / "publications/LULA-I/release/code/lula1/src/lib.rs",
    "manuscript": ROOT / "publications/LULA-I/LULA-I.tex",
}
binding = {}
for name,path in paths.items():
    b=path.read_bytes()
    binding[name] = {"path": str(path), "sha256": hashlib.sha256(b).hexdigest()}
    if name != "manuscript":
        code=b[b.index(b"use sha2::digest"):].replace(b"\r\n",b"\n")
        binding[name]["body_sha256"] = hashlib.sha256(code).hexdigest()
assert len({binding[n]["body_sha256"] for n in ("original","private","release")}) == 1
hs=[5,5,5,5,21]; ls=[32,32,32,32,16]; ws=[16,16,16,16,256]
layers=[]
for i in range(5):
    above=sum(hs[i+1:]); keys=1<<sum(hs[i:]); trees=1<<above
    layers.append({"layer":i,"height":hs[i],"trees":trees,"wots_keys":keys,
      "chain_starts":keys*ls[i],"nodes_per_tree":(1<<(hs[i]+1))-1,
      "total_merkle_nodes":trees*((1<<(hs[i]+1))-1),
      "internal_merkle_nodes":trees*((1<<hs[i])-1),
      "chain_function_steps":keys*ls[i]*(ws[i]-1),
      "distinct_honest_messages_per_key":1,
      "signature_layer_bytes":4+16*ls[i]+16*hs[i]})
fors_instances=1<<41
out={"status":"COMPUTED_SYMBOLIC_COUNTS_NOT_A_SECURITY_BOUND", "binding":binding,
 "layers":layers,"fors_instances":fors_instances,
 "fors_secret_locations":fors_instances*17*512,
 "fors_tree_nodes":fors_instances*17*1023,
 "wots_secret_locations":sum(l["chain_starts"] for l in layers),
 "all_secret_prf_locations":fors_instances*17*512+sum(l["chain_starts"] for l in layers),
 "keygen_without_cache_prf_calls":(1<<21)*16,
 "keygen_top_cache_prf_calls":(1<<21)*(16+32*32),
 "prepared_sign_prf_invocations":17*(512+1)+4*(32*32+32)+16,
 "uncached_sign_prf_invocations":17*(512+1)+4*(32*32+32)+(1<<21)*16+16,
 "prepared_sign_distinct_prf_locations_max":17*512+4*32*32+16,
 "uncached_sign_distinct_prf_locations_max":17*512+4*32*32+(1<<21)*16,
 "cache_payload":16*((1<<22)-1)+4*(1<<21),
 "signature_bytes":16+4+17*(9+1)*16+sum(l["signature_layer_bytes"] for l in layers)}
(HERE / "SOURCE_AND_COUNTS.json").write_text(json.dumps(out,indent=2)+"\n",encoding="utf-8")
print(json.dumps(out,indent=2))
