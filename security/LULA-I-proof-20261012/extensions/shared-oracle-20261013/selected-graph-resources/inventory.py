"""Symbolic source inventory only; never evaluates any cryptographic graph."""
from pathlib import Path
import json, hashlib

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
CODE = ROOT.parents[1] / 'publications/LULA-I/release/code/lula1/src/lib.rs'
PARENT = ROOT / 'code-review/SOURCE_AND_COUNTS.json'
PRIVATE = HERE.parent / 'PRIVATE-REDUCTION-PROGRAMS.md'
PIN = 'ac8e67f05af68dd8e1291c5909847f74103903fb7ffa2c70f500c6ec48f14210'
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
assert sha(CODE) == PIN
hs = [5,5,5,5,21]
lws = [4,4,4,4,8]
rows=[]
for j,(h,lw) in enumerate(zip(hs,lws)):
    trees=2**sum(hs[j+1:]); keys=trees*2**h
    ell=128//lw; w=2**lw
    rows.append(dict(layer=j,height=h,trees=trees,wots_keys=keys,
       ell=ell,w=w,type0=keys*ell*(w-1),type1=keys,
       type2=trees*(2**h-1),type5=keys*ell))
instances=2**sum(hs)
fleaf=instances*17*2**9
finternal=instances*17*(2**9-1)
classes={str(i):sum(r[f'type{i}'] for r in rows) for i in [0,1,2,5]}
classes.update({'3_leaf':fleaf,'3_internal':finternal,'3':fleaf+finternal,
                '4':instances,'6':fleaf})
G=sum(classes[str(i)] for i in range(5))
ND=classes['5']+classes['6']
UW=classes['1']; L=2**32
Hsetup=2**21*(19505+L)-1
Wtop=2**21*(16*255+1)+(2**21-1)
Hcold=Wtop+82090+6*L
Hhot=82090+5*L
Usetup=2**21*(16+32*32)
qrows=[]
for qlog in [24,30,38,40,41,44,50,64]:
    q=2**qlog
    # Raw counts exclude A's own Q_H, which must be added verbatim.
    qrows.append(dict(log2_q=qlog,q=q,
      D_cold=min(ND,Usetup+33567232*q),D_hot=min(ND,Usetup+12816*q),
      B_K_Raw_cold_minus_QH=Hsetup+q*(Hcold+1)+3224,
      B_K_Raw_hot_minus_QH=Hsetup+q*(Hhot+1)+3224,
      B_P_Raw_cold_minus_QH=Hsetup+q*Hcold+3224,
      B_P_Raw_hot_minus_QH=Hsetup+q*Hhot+3224,
      B_P_Randomizer=q))
pre=[]
for j,r in enumerate(rows):
    h,ell,w=r['height'],r['ell'],r['w']
    for v in range(1,h+1):
        pre.append(dict(class_name='type2',layer=j,height=v,
             strict_public_predecessors=2**v*(ell*(w-1)+2)-2,
             private_predecessors=2**v*ell,strict_graph_descendants=h-v,
             canonical_metadata_extra_counter_attempt_cap=L if j<4 else 0))
    for t in range(w-1):
        pre.append(dict(class_name='type0',layer=j,step=t,
          strict_public_predecessors=t,private_predecessors=1,
          strict_graph_descendants=w-1-t+h,
          canonical_metadata_extra_counter_attempt_cap=L if j<4 else 0))
    pre.append(dict(class_name='type1',layer=j,
        strict_public_predecessors=ell*(w-1),private_predecessors=ell,
        strict_graph_descendants=h,
        canonical_metadata_extra_counter_attempt_cap=L if j<4 else 0))
for v in range(10):
    pre.append(dict(class_name='type3',height=v,
          strict_public_predecessors=2**(v+1)-2,
          private_predecessors=2**v,strict_graph_descendants=10-v,
          canonical_metadata_extra_counter_attempt_cap=L))
pre.append(dict(class_name='type4',strict_public_predecessors=17*(2**10-1),
      private_predecessors=17*2**9,strict_graph_descendants=0,
      canonical_metadata_extra_counter_attempt_cap=L))
out=dict(status='COMPUTED_SYMBOLIC_NOT_A_SECURITY_REDUCTION',
  binding={str(p):sha(p) for p in [CODE,PARENT,PRIVATE]},layers=rows,classes=classes,
  total_graph_nodes=G,total_private_locations=ND,wots_keys=UW,
  fixed_bit_selector_bits=G.bit_length(),fixed_bit_selector_loss=2**G.bit_length(),
  eager_full256_outputs_bytes=32*(G+ND),eager_node16_outputs_bytes=16*(G+ND),
  eager_raw_caps=dict(graph_only=G+ND,
    graph_plus_all_canonical_metadata=G+ND+L*UW),
  eager_metadata_uint32_bytes=4*UW,
  eager_metadata_counter_and_byte_flag_cap=5*UW,
  eager_optional_full_raw_records_payload_bytes=630*G+134*ND+138*L*UW,
  setup=dict(Usetup=Usetup,Hsetup=Hsetup,Wtop=Wtop,Hcold=Hcold,Hhot=Hhot),
  qrows=qrows,selected_point_dependency_rows=pre)
# Comparison is deliberately done AFTER our formulas have been independently formed.
parent=json.loads(PARENT.read_text())
for r,pr in zip(rows,parent['layers']):
    for own,old in [('trees','trees'),('wots_keys','wots_keys'),('type0','chain_function_steps'),
                    ('type2','internal_merkle_nodes'),('type5','chain_starts')]:
        assert r[own]==pr[old],(r['layer'],own)
assert fleaf==parent['fors_secret_locations']
assert fleaf+finternal==parent['fors_tree_nodes']
assert ND==parent['all_secret_prf_locations']
(HERE/'INVENTORY.json').write_text(json.dumps(out,indent=2)+'\n')
table=['# Exact symbolic inventory and private-adapter resource caps','',
       'COMPUTED. No source execution or measurement. All numbers are exact integers.','',
       '| Layer | Trees | WOTS keys | Type0 | Type1 | Type2 | Type5 |',
       '|---|---:|---:|---:|---:|---:|---:|']
for r in rows:
    table.append('| '+' | '.join(str(r[k]) for k in ['layer','trees','wots_keys','type0','type1','type2','type5'])+' |')
table+=['',f'Public graph total G={G}. Private address total ND={ND}.',
        f'Type3 leaves={fleaf}; type3 internal={finternal}; type4={instances}.','',
        '| log2 q | q | D cold | D hot | B_K Raw cold minus Q_H | B_K Raw hot minus Q_H | B_P Raw cold minus Q_H | B_P Raw hot minus Q_H |',
        '|---|---:|---:|---:|---:|---:|---:|---:|']
for r in qrows:
    table.append('| '+' | '.join(str(r[k]) for k in ['log2_q','q','D_cold','D_hot',
      'B_K_Raw_cold_minus_QH','B_K_Raw_hot_minus_QH','B_P_Raw_cold_minus_QH','B_P_Raw_hot_minus_QH'])+' |')
table+=['','B_P Randomizer calls are at most q. The adversarial Q_H is added to every Raw cap above.',
        '',f'Eager graph-only invocation count G+ND={G+ND}.',
        f'Eager graph and full canonical metadata invocation cap={G+ND+L*UW}.',
        f'Full256 graph and private outputs alone occupy {32*(G+ND)} bytes.',
        f'Canonical counter table alone occupies {4*UW} bytes.',
        f'Optional complete raw-record payload occupies at most {630*G+134*ND+138*L*UW} bytes, before dictionary indexing.','']
(HERE/'TABLES.md').write_text('\n'.join(table))
print(json.dumps({'graph':G,'private':ND,'classes':classes,'qrows':len(qrows),'dependency_rows':len(pre)},indent=2))
