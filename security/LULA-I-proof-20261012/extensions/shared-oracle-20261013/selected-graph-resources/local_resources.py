"""Exact proposed localized overhead, separate from immutable eager inventory."""
from pathlib import Path
import hashlib,json
HERE=Path(__file__).resolve().parent
base=HERE/'INVENTORY.json'
PIN='8d2264ff13a3a76a00c50768149d4864d86093e57a5f48bdaac21673c07fe202'
assert hashlib.sha256(base.read_bytes()).hexdigest()==PIN
d=json.loads(base.read_text())
s=d['setup']; ND=d['total_private_locations']
Cpre=s['Wtop']-1; Upre=2**21*16
Cextract=s['Wtop']+4*(32*(32*15+1)+31)+17*(512+511)+1
Uextract=2**21*16+4*32*32+17*512
assert (Cpre,Upre,Cextract,Uextract)==(8560574462,33554432,8560653547,33567232)
rows=[]
for r in d['qrows']:
    q=r['q']; modes={}
    for mode,dcap,hcap in [('hot',12816,s['Hhot']),('cold',33567232,s['Hcold'])]:
        priv=min(ND,Upre+s['Usetup']+q*dcap+Uextract)
        pub=Cpre+1+s['Hsetup']+q*hcap+3224+Cextract
        modes[mode]=dict(private_coordinate_cap=priv,
             HJ_public_Raw_minus_QH=pub,REAL_total_Raw_minus_QH=pub+q+priv,
             B_K_Derive_cap=priv,B_K_Raw_minus_QH=pub+q,
             B_P_local_F_cap=priv,B_P_Randomizer_cap=q,B_P_Raw_minus_QH=pub)
    rows.append(dict(log2_q=r['log2_q'],q=q,modes=modes))
out=dict(status='COMPUTED_PROPOSED_LOCALIZED_CAPS_NOT_PROMOTED_SUCCESSOR',
  base_inventory_sha256=PIN,selected_predecessor_public_max=Cpre,
  selected_predecessor_private_max=Upre,final_route_public=Cextract,
  final_route_private=Uextract,trace_payload_bytes=630*3217,
  final_route_node_array_bytes=16*((2**22-1)+4*63+17*1023),
  pre_root_node_array_bytes=16*(2**22-2),
  fixed_bit_selector_loss=2**56,selected_handle_cap='1+Q_H+3217 for nonzero S with known target response reused',
  qrows=rows)
(HERE/'LOCAL-RESOURCES.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k!='qrows'},indent=2))
