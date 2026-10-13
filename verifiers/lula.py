"""Independent LULA I verifier for the public test vectors.

The supplied fixture carries the parameter string and public-key nodes.
Run the maintained checks with ``python -I -B scripts/check.py``.
This module checks signatures; it does not generate keys or prove security.
"""
import hashlib

N = 16


def parse_spec(spec):
    f, ls = spec.split(";")
    k, a, forsc = (int(x) for x in f.split(","))
    layers = []
    for part in ls.split("|"):
        h, lw, z, S, c = (int(x) for x in part.split(":"))
        layers.append(dict(h=h, lw=lw, z=z, S=S, l=128 // lw - z, w=1 << lw))
    return k, a, bool(forsc), layers


def adrs(layer, tree, typ, kp=0, w2=0, w3=0):
    return (bytes([layer]) + tree.to_bytes(8, "big") + bytes([typ]) + kp.to_bytes(4, "big")
            + w2.to_bytes(4, "big") + w3.to_bytes(4, "big"))


def bits(b, start, cnt):
    x = int.from_bytes(b, "big")
    return (x >> (8 * len(b) - start - cnt)) & ((1 << cnt) - 1)


def verify(spec, pk_seed, pk_root, msg, sig):
    if len(pk_seed) != N or len(pk_root) != N:
        return False
    k, a, forsc, layers = parse_spec(spec)
    kr = k - 1 if forsc else k
    h = sum(L["h"] for L in layers)
    size = N + (4 if forsc else 0) + kr * (a + 1) * N + sum(4 + L["l"] * N + L["h"] * N for L in layers)
    if len(sig) != size:
        return False
    pre = pk_seed + b"\x00" * 48

    def th(ad, x):
        return hashlib.sha256(pre + ad + x).digest()[:N]

    off = 0

    def take(n):
        nonlocal off
        v = sig[off:off + n]
        off += n
        return v

    R = take(N)
    ctr = int.from_bytes(take(4), "big") if forsc else 0
    inner = hashlib.sha256(R + pk_seed + pk_root + msg).digest()
    D = hashlib.sha256(inner + ctr.to_bytes(4, "big") + pk_seed).digest()
    idxs = [bits(D, j * a, a) for j in range(k)]
    if forsc and idxs[k - 1] != 0:
        return False
    idx = bits(D, k * a, h)
    t0, q0 = idx >> layers[0]["h"], idx & ((1 << layers[0]["h"]) - 1)
    roots = []
    for j in range(kr):
        g = j * (1 << a) + idxs[j]
        x = th(adrs(0, t0, 3, q0, 0, g), take(N))
        for e in range(a):
            sib = take(N)
            ad = adrs(0, t0, 3, q0, e + 1, g >> 1)
            x = th(ad, sib + x) if g & 1 else th(ad, x + sib)
            g >>= 1
        roots.append(x)
    V = th(adrs(0, t0, 4, q0), b"".join(roots))
    below = 0
    for j, L in enumerate(layers):
        q = (idx >> below) & ((1 << L["h"]) - 1)
        t = idx >> (below + L["h"])
        below += L["h"]
        c = int.from_bytes(take(4), "big")
        dig = th(adrs(j, t, 7, q), V + c.to_bytes(4, "big"))
        digits = [bits(dig, i * L["lw"], L["lw"]) for i in range(128 // L["lw"])]
        if any(digits[L["l"]:]) or sum(digits) != L["S"]:
            return False
        ends = []
        for i in range(L["l"]):
            x = take(N)
            for p in range(digits[i], L["w"] - 1):
                x = th(adrs(j, t, 0, q, i, p), x)
            ends.append(x)
        x = th(adrs(j, t, 1, q), b"".join(ends))
        qq = q
        for e in range(L["h"]):
            sib = take(N)
            ad = adrs(j, t, 2, 0, e + 1, qq >> 1)
            x = th(ad, sib + x) if qq & 1 else th(ad, x + sib)
            qq >>= 1
        V = x
    return V == pk_root
