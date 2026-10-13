"""Exhaustive finite addressed-chain/endpoint classifier; not a forgery test."""
from collections import Counter
from itertools import product
from pathlib import Path
import json

M, W, L, S = 2, 3, 2, 2
digits = [v for v in product(range(W), repeat=L) if sum(v)==S]
counts = Counter()
worlds = 0
for maps in product(range(M), repeat=L*(W-1)*M):
    def oracle(i,p,x):
        return maps[(i*(W-1)+p)*M+x]
    for seeds in product(range(M),repeat=L):
        xs = []
        for i in range(L):
            row=[seeds[i]]
            for p in range(W-1):
                row.append(oracle(i,p,row[-1]))
            xs.append(row)
        ends=tuple(row[-1] for row in xs)
        for pk_map in product(range(M),repeat=M**L):
            def pk(v): return pk_map[v[0]*M+v[1]]
            worlds += 1
            honest_pk=pk(ends)
            for exposed in [None]+digits:
                for y in digits:
                    for supplied in product(range(M),repeat=L):
                        hidden=False
                        graph=False
                        got=[]
                        for i in range(L):
                            x=supplied[i]
                            for p in range(y[i],W-1):
                                genuine=xs[i][p]
                                known=exposed is not None and p>=exposed[i]
                                hidden |= x==genuine and not known
                                nxt=oracle(i,p,x)
                                graph |= x!=genuine and nxt==xs[i][p+1]
                                x=nxt
                            got.append(x)
                        got=tuple(got)
                        if pk(got)!=honest_pk:
                            continue
                        graph |= got!=ends
                        if hidden:
                            counts["hidden_witness"]+=1
                        elif graph:
                            counts["graph_witness"]+=1
                        else:
                            assert exposed is not None, "unexposed accepted key escaped"
                            assert y==exposed, "changed digits escaped constant-sum classifier"
                            assert supplied==tuple(xs[i][y[i]] for i in range(L))
                            counts["same_canonical_digits_and_genuine_values"]+=1
result={"status":"PASS_EXHAUSTIVE_TOY_CLASSIFICATION_ONLY", "worlds":worlds,
        "accepted_classifications":dict(counts),
        "model":"two typed radix3 chains, binary values, fixed sum2, arbitrary typed endpoint compressor; all numerical collisions allowed"}
Path(__file__).with_name("CLASSIFIER-RESULTS.json").write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8")
print(json.dumps(result,indent=2))
