//! LULA I: deterministic hash-based signing with an honest-cache equivalence mechanism.
//! The cache contains deterministic upper-layer Merkle nodes and canonical WOTS+C counters.
//! Honest cache restoration preserves signature bytes when signing terminates. Rollback-security
//! transfer is conditional on an applicable reference security bound; the full bound remains open.
//! Timing and cache availability are observable. Arbitrary cache corruption is outside the claim.
//!
//! SHA-256 with 16-byte nodes, compressed 22-byte addresses, and a precomputed public-seed block.
//! Compression instrumentation is retained from the original measurement library.

use sha2::digest::generic_array::GenericArray;
use sha2::{compress256, Digest, Sha256};
use std::cell::Cell;

pub const N: usize = 16;
pub type Node = [u8; N];

const IV: [u32; 8] = [
    0x6a09e667, 0xbb67ae85, 0x3c6ef372, 0xa54ff53a, 0x510e527f, 0x9b05688c, 0x1f83d9ab, 0x5be0cd19,
];

thread_local! { static CALLS: Cell<u64> = const { Cell::new(0) }; }
#[inline]
fn count(c: u64) {
    CALLS.with(|x| x.set(x.get() + c));
}
pub fn calls() -> u64 {
    CALLS.with(|x| x.get())
}
pub fn reset_calls() {
    CALLS.with(|x| x.set(0));
}

#[inline]
fn compress(st: &mut [u32; 8], block: &[u8; 64]) {
    compress256(st, std::slice::from_ref(GenericArray::from_slice(block)));
    count(1);
}

#[inline]
fn st_node(st: &[u32; 8]) -> Node {
    let mut o = [0u8; N];
    for i in 0..4 {
        o[4 * i..4 * i + 4].copy_from_slice(&st[i].to_be_bytes());
    }
    o
}

fn sha256_counted(parts: &[&[u8]]) -> [u8; 32] {
    let mut h = Sha256::new();
    let mut len = 0usize;
    for p in parts {
        h.update(p);
        len += p.len();
    }
    count(((len + 9 + 63) / 64) as u64);
    h.finalize().into()
}

// ------------------------------------------------------------------------------------------------ address
pub const T_WOTS_HASH: u8 = 0;
pub const T_WOTS_PK: u8 = 1;
pub const T_TREE: u8 = 2;
pub const T_FORS_TREE: u8 = 3;
pub const T_FORS_ROOTS: u8 = 4;
pub const T_WOTS_PRF: u8 = 5;
pub const T_FORS_PRF: u8 = 6;
pub const T_WOTSC_MSG: u8 = 7;

/// 22-byte address: layer(1) | tree(8) | type(1) | keypair(4) | chain or height(4) | hash or index(4)
#[derive(Clone, Copy)]
pub struct Adrs(pub [u8; 22]);
impl Adrs {
    pub fn new(layer: u32, tree: u64, typ: u8) -> Adrs {
        let mut a = [0u8; 22];
        a[0] = layer as u8;
        a[1..9].copy_from_slice(&tree.to_be_bytes());
        a[9] = typ;
        Adrs(a)
    }
    pub fn kp(mut self, v: u32) -> Adrs {
        self.0[10..14].copy_from_slice(&v.to_be_bytes());
        self
    }
    pub fn w2(mut self, v: u32) -> Adrs {
        self.0[14..18].copy_from_slice(&v.to_be_bytes());
        self
    }
    pub fn w3(mut self, v: u32) -> Adrs {
        self.0[18..22].copy_from_slice(&v.to_be_bytes());
        self
    }
    #[inline]
    pub fn set_w3(&mut self, v: u32) {
        self.0[18..22].copy_from_slice(&v.to_be_bytes());
    }
}

// ---------------------------------------------------------------------------------------------- hash context
#[derive(Clone)]
pub struct Ctx {
    st0: [u32; 8],
    pub pk_seed: Node,
    pub pk_root: Node,
    sk_seed: Node,
    sk_prf: Node,
}

impl Ctx {
    pub fn new(sk_seed: Node, sk_prf: Node, pk_seed: Node) -> Ctx {
        let mut block = [0u8; 64];
        block[..N].copy_from_slice(&pk_seed);
        let mut st0 = IV;
        compress256(&mut st0, std::slice::from_ref(GenericArray::from_slice(&block)));
        Ctx { st0, pk_seed, pk_root: [0u8; N], sk_seed, sk_prf }
    }
    pub fn public(pk_seed: Node, pk_root: Node) -> Ctx {
        let mut c = Ctx::new([0u8; N], [0u8; N], pk_seed);
        c.pk_root = pk_root;
        c
    }
    /// Trunc_16(SHA-256(PK.seed || 0^48 || adrs || inp)); one compression when 22 + |inp| <= 55.
    pub fn th(&self, adrs: &Adrs, inp: &[u8]) -> Node {
        let tail = 22 + inp.len();
        let bitlen = ((64 + tail) as u64) * 8;
        let mut st = self.st0;
        if tail <= 55 {
            let mut b = [0u8; 64];
            b[..22].copy_from_slice(&adrs.0);
            b[22..tail].copy_from_slice(inp);
            b[tail] = 0x80;
            b[56..64].copy_from_slice(&bitlen.to_be_bytes());
            compress(&mut st, &b);
            return st_node(&st);
        }
        let nblocks = (tail + 9 + 63) / 64;
        let mut buf = [0u8; 64 * 24];
        assert!(nblocks <= 24);
        buf[..22].copy_from_slice(&adrs.0);
        buf[22..tail].copy_from_slice(inp);
        buf[tail] = 0x80;
        buf[nblocks * 64 - 8..nblocks * 64].copy_from_slice(&bitlen.to_be_bytes());
        for i in 0..nblocks {
            let mut blk = [0u8; 64];
            blk.copy_from_slice(&buf[i * 64..(i + 1) * 64]);
            compress(&mut st, &blk);
        }
        st_node(&st)
    }
    #[inline]
    pub fn f(&self, adrs: &Adrs, x: &Node) -> Node {
        self.th(adrs, x)
    }
    #[inline]
    pub fn h(&self, adrs: &Adrs, l: &Node, r: &Node) -> Node {
        let mut b = [0u8; 2 * N];
        b[..N].copy_from_slice(l);
        b[N..].copy_from_slice(r);
        self.th(adrs, &b)
    }
    #[inline]
    pub fn prf(&self, adrs: &Adrs) -> Node {
        self.th(adrs, &self.sk_seed.clone())
    }
    pub fn prf_msg(&self, m: &[u8]) -> Node {
        let d = sha256_counted(&[&self.sk_prf, &self.pk_seed, m]);
        let mut r = [0u8; N];
        r.copy_from_slice(&d[..N]);
        r
    }
    pub fn hmsg_inner(&self, r: &Node, m: &[u8]) -> [u8; 32] {
        sha256_counted(&[r, &self.pk_seed, &self.pk_root, m])
    }
    /// one compression: SHA-256(inner(32) || ctr(4) || PK.seed(16))
    pub fn hmsg_outer(&self, inner: &[u8; 32], ctr: u32) -> [u8; 32] {
        let mut b = [0u8; 64];
        b[..32].copy_from_slice(inner);
        b[32..36].copy_from_slice(&ctr.to_be_bytes());
        b[36..52].copy_from_slice(&self.pk_seed);
        b[52] = 0x80;
        b[56..64].copy_from_slice(&(52u64 * 8).to_be_bytes());
        let mut st = IV;
        compress(&mut st, &b);
        let mut o = [0u8; 32];
        for i in 0..8 {
            o[4 * i..4 * i + 4].copy_from_slice(&st[i].to_be_bytes());
        }
        o
    }
}

pub fn get_bits(d: &[u8], start: usize, cnt: usize) -> u64 {
    let mut v = 0u64;
    for i in 0..cnt {
        let bit = start + i;
        v = (v << 1) | (((d[bit / 8] >> (7 - (bit % 8))) & 1) as u64);
    }
    v
}

// --------------------------------------------------------------------------------------------------- WOTS+C
#[derive(Clone, Debug)]
pub struct WotsC {
    pub lw: u32,
    pub w: u32,
    pub lfull: u32,
    pub z: u32,
    pub l: u32,
    pub s: u32,
}

impl WotsC {
    pub fn new(lw: u32, z: u32, s: u32) -> WotsC {
        let lfull = 128 / lw;
        WotsC { lw, w: 1 << lw, lfull, z, l: lfull - z, s }
    }
    pub fn digest(&self, ctx: &Ctx, layer: u32, tree: u64, kp: u32, msg: &Node, ctr: u32) -> Node {
        let mut inp = [0u8; N + 4];
        inp[..N].copy_from_slice(msg);
        inp[N..].copy_from_slice(&ctr.to_be_bytes());
        ctx.th(&Adrs::new(layer, tree, T_WOTSC_MSG).kp(kp), &inp)
    }
    pub fn digits(&self, d: &Node) -> Vec<u32> {
        (0..self.lfull).map(|i| get_bits(d, (i * self.lw) as usize, self.lw as usize) as u32).collect()
    }
    pub fn accept(&self, dg: &[u32]) -> bool {
        dg[self.l as usize..].iter().all(|&x| x == 0) && dg.iter().sum::<u32>() == self.s
    }
    pub fn grind(&self, ctx: &Ctx, layer: u32, tree: u64, kp: u32, msg: &Node) -> (u32, Vec<u32>) {
        let mut ctr = 0u32;
        loop {
            let dg = self.digits(&self.digest(ctx, layer, tree, kp, msg, ctr));
            if self.accept(&dg) {
                return (ctr, dg);
            }
            ctr += 1;
        }
    }
    #[inline]
    pub fn chain(&self, ctx: &Ctx, layer: u32, tree: u64, kp: u32, i: u32, x: &Node, start: u32, steps: u32) -> Node {
        let mut a = Adrs::new(layer, tree, T_WOTS_HASH).kp(kp).w2(i);
        let mut v = *x;
        for p in start..start + steps {
            a.set_w3(p);
            v = ctx.f(&a, &v);
        }
        v
    }
    pub fn sk(&self, ctx: &Ctx, layer: u32, tree: u64, kp: u32, i: u32) -> Node {
        ctx.prf(&Adrs::new(layer, tree, T_WOTS_PRF).kp(kp).w2(i))
    }
    fn compress_pk(&self, ctx: &Ctx, layer: u32, tree: u64, kp: u32, ends: &[Node]) -> Node {
        let mut buf = Vec::with_capacity(ends.len() * N);
        for e in ends {
            buf.extend_from_slice(e);
        }
        ctx.th(&Adrs::new(layer, tree, T_WOTS_PK).kp(kp), &buf)
    }
    pub fn pk(&self, ctx: &Ctx, layer: u32, tree: u64, kp: u32) -> Node {
        let ends: Vec<Node> = (0..self.l)
            .map(|i| self.chain(ctx, layer, tree, kp, i, &self.sk(ctx, layer, tree, kp, i), 0, self.w - 1))
            .collect();
        self.compress_pk(ctx, layer, tree, kp, &ends)
    }
    pub fn sign(&self, ctx: &Ctx, layer: u32, tree: u64, kp: u32, dg: &[u32]) -> Vec<Node> {
        (0..self.l)
            .map(|i| self.chain(ctx, layer, tree, kp, i, &self.sk(ctx, layer, tree, kp, i), 0, dg[i as usize]))
            .collect()
    }
    pub fn pk_from_sig(&self, ctx: &Ctx, layer: u32, tree: u64, kp: u32, sig: &[Node], dg: &[u32]) -> Node {
        let ends: Vec<Node> = (0..self.l)
            .map(|i| {
                let d = dg[i as usize];
                self.chain(ctx, layer, tree, kp, i, &sig[i as usize], d, self.w - 1 - d)
            })
            .collect();
        self.compress_pk(ctx, layer, tree, kp, &ends)
    }
}

// --------------------------------------------------------------------------------------------------- Merkle
#[derive(Clone)]
pub struct Subtree {
    pub h: u32,
    pub nodes: Vec<Node>, // level-major: 2^h leaves, then 2^(h-1), ..., 1 root
}

impl Subtree {
    fn off(&self, level: u32) -> usize {
        (1usize << (self.h + 1)) - (1usize << (self.h + 1 - level))
    }
    pub fn build(ctx: &Ctx, base: Adrs, leaves: Vec<Node>) -> Subtree {
        let h = leaves.len().trailing_zeros();
        let mut nodes = leaves;
        nodes.reserve(nodes.len());
        let mut start = 0usize;
        let mut width = 1usize << h;
        for level in 1..=h {
            let a = base.w2(level);
            for i in 0..width / 2 {
                let l = nodes[start + 2 * i];
                let r = nodes[start + 2 * i + 1];
                nodes.push(ctx.h(&a.w3(i as u32), &l, &r));
            }
            start += width;
            width /= 2;
        }
        Subtree { h, nodes }
    }
    pub fn root(&self) -> Node {
        *self.nodes.last().unwrap()
    }
    pub fn auth(&self, mut leaf: usize) -> Vec<Node> {
        let mut p = Vec::with_capacity(self.h as usize);
        for level in 0..self.h {
            p.push(self.nodes[self.off(level) + (leaf ^ 1)]);
            leaf >>= 1;
        }
        p
    }
}

pub fn root_from_path(ctx: &Ctx, base: Adrs, leafnode: &Node, mut idx: u32, path: &[Node]) -> Node {
    let mut x = *leafnode;
    for (lv, sib) in path.iter().enumerate() {
        let a = base.w2(lv as u32 + 1).w3(idx >> 1);
        x = if idx & 1 == 1 { ctx.h(&a, sib, &x) } else { ctx.h(&a, &x, sib) };
        idx >>= 1;
    }
    x
}

// ----------------------------------------------------------------------------------------------------- FORS
#[derive(Clone, Debug)]
pub struct Fors {
    pub k: u32,     // trees addressed by the digest (FORS+C: the last one is forced to index 0 and not stored)
    pub a: u32,
    pub forsc: bool,
}

impl Fors {
    pub fn real_trees(&self) -> u32 {
        if self.forsc { self.k - 1 } else { self.k }
    }
    fn tree(&self, ctx: &Ctx, tree: u64, kp: u32, j: u32) -> Subtree {
        let t = 1u32 << self.a;
        let leaves: Vec<Node> = (0..t)
            .map(|i| {
                let g = j * t + i;
                let sk = ctx.prf(&Adrs::new(0, tree, T_FORS_PRF).kp(kp).w3(g));
                ctx.f(&Adrs::new(0, tree, T_FORS_TREE).kp(kp).w2(0).w3(g), &sk)
            })
            .collect();
        // node indices are global across trees: at height hh the index is j * 2^(a-hh) + local
        let h = self.a;
        let mut nodes = leaves;
        let mut start = 0usize;
        let mut width = t as usize;
        for level in 1..=h {
            for i in 0..width / 2 {
                let gi = j * (t >> level) + i as u32;
                let a = Adrs::new(0, tree, T_FORS_TREE).kp(kp).w2(level).w3(gi);
                let l = nodes[start + 2 * i];
                let r = nodes[start + 2 * i + 1];
                nodes.push(ctx.h(&a, &l, &r));
            }
            start += width;
            width /= 2;
        }
        Subtree { h, nodes }
    }
    fn roots_pk(&self, ctx: &Ctx, tree: u64, kp: u32, roots: &[Node]) -> Node {
        let mut buf = Vec::with_capacity(roots.len() * N);
        for r in roots {
            buf.extend_from_slice(r);
        }
        ctx.th(&Adrs::new(0, tree, T_FORS_ROOTS).kp(kp), &buf)
    }
    pub fn pk(&self, ctx: &Ctx, tree: u64, kp: u32) -> Node {
        let roots: Vec<Node> = (0..self.real_trees()).map(|j| self.tree(ctx, tree, kp, j).root()).collect();
        self.roots_pk(ctx, tree, kp, &roots)
    }
    /// returns (signature parts (sk, auth path) per real tree, FORS public key)
    pub fn sign(&self, ctx: &Ctx, tree: u64, kp: u32, idx: &[u32]) -> (Vec<(Node, Vec<Node>)>, Node) {
        let t = 1u32 << self.a;
        let mut parts = Vec::new();
        let mut roots = Vec::new();
        for j in 0..self.real_trees() {
            let st = self.tree(ctx, tree, kp, j);
            let i = idx[j as usize];
            let sk = ctx.prf(&Adrs::new(0, tree, T_FORS_PRF).kp(kp).w3(j * t + i));
            parts.push((sk, st.auth(i as usize)));
            roots.push(st.root());
        }
        (parts, self.roots_pk(ctx, tree, kp, &roots))
    }
    pub fn pk_from_sig(&self, ctx: &Ctx, tree: u64, kp: u32, idx: &[u32], parts: &[(Node, Vec<Node>)]) -> Node {
        let t = 1u32 << self.a;
        let mut roots = Vec::new();
        for j in 0..self.real_trees() {
            let i = idx[j as usize];
            let g = j * t + i;
            let (sk, path) = &parts[j as usize];
            let mut x = ctx.f(&Adrs::new(0, tree, T_FORS_TREE).kp(kp).w2(0).w3(g), sk);
            let mut gi = g;
            for (lv, sib) in path.iter().enumerate() {
                let a = Adrs::new(0, tree, T_FORS_TREE).kp(kp).w2(lv as u32 + 1).w3(gi >> 1);
                x = if gi & 1 == 1 { ctx.h(&a, sib, &x) } else { ctx.h(&a, &x, sib) };
                gi >>= 1;
            }
            roots.push(x);
        }
        self.roots_pk(ctx, tree, kp, &roots)
    }
}

// --------------------------------------------------------------------------------------------------- scheme
#[derive(Clone, Debug)]
pub struct LayerP {
    pub h: u32,
    pub lw: u32,
    pub z: u32,
    pub s: u32,
    pub cached: bool,
}

#[derive(Clone, Debug)]
pub struct Params {
    pub name: String,
    pub k: u32,
    pub a: u32,
    pub forsc: bool,
    pub layers: Vec<LayerP>, // layers[0] = bottom (signs the FORS public key)
}

impl Params {
    pub fn htotal(&self) -> u32 {
        self.layers.iter().map(|l| l.h).sum()
    }
    pub fn sig_bytes(&self) -> usize {
        let f = Fors { k: self.k, a: self.a, forsc: self.forsc };
        let mut s = N + if self.forsc { 4 } else { 0 } + (f.real_trees() * (self.a + 1)) as usize * N;
        for l in &self.layers {
            let w = WotsC::new(l.lw, l.z, l.s);
            s += 4 + w.l as usize * N + l.h as usize * N;
        }
        s
    }
}

#[derive(Clone)]
pub struct LayerCache {
    pub subtrees: Vec<Subtree>,
    pub ctrs: Vec<Vec<u32>>,
}

pub struct Signer {
    pub p: Params,
    pub fors: Fors,
    pub wots: Vec<WotsC>,
    pub ctx: Ctx,
    pub cache: Vec<Option<LayerCache>>,
}

pub struct KeygenReport {
    pub calls: u64,
    pub secs: f64,
    pub cache_bytes: u64,
}

fn tree_leaf(p: &Params, idx: u64, layer: usize) -> (u64, u32) {
    let below: u32 = p.layers[..layer].iter().map(|l| l.h).sum();
    let hj = p.layers[layer].h;
    let leaf = ((idx >> below) & ((1u64 << hj) - 1)) as u32;
    let tree = idx >> (below + hj);
    (tree, leaf)
}

impl Signer {
    fn compute_subtree(&self, layer: usize, tree: u64) -> Subtree {
        let w = &self.wots[layer];
        let leaves: Vec<Node> =
            (0..(1u32 << self.p.layers[layer].h)).map(|kp| w.pk(&self.ctx, layer as u32, tree, kp)).collect();
        Subtree::build(&self.ctx, Adrs::new(layer as u32, tree, T_TREE), leaves)
    }
    /// value signed by WOTS key (layer, tree, leaf): FORS pk (layer 0) or the root of the child subtree
    fn child_value(&self, layer: usize, tree: u64, leaf: u32) -> Node {
        let g = (tree << self.p.layers[layer].h) | leaf as u64;
        if layer == 0 {
            let (t0, k0) = (g >> self.p.layers[0].h, (g & ((1u64 << self.p.layers[0].h) - 1)) as u32);
            return self.fors.pk(&self.ctx, t0, k0);
        }
        if let Some(c) = &self.cache[layer - 1] {
            return c.subtrees[g as usize].root();
        }
        self.compute_subtree(layer - 1, g).root()
    }

    pub fn keygen(p: Params, seed: &[u8; 48], threads: usize) -> (Signer, KeygenReport) {
        let t0 = std::time::Instant::now();
        let mut sk_seed = [0u8; N];
        let mut sk_prf = [0u8; N];
        let mut pk_seed = [0u8; N];
        sk_seed.copy_from_slice(&seed[..16]);
        sk_prf.copy_from_slice(&seed[16..32]);
        pk_seed.copy_from_slice(&seed[32..48]);
        let ctx = Ctx::new(sk_seed, sk_prf, pk_seed);
        let wots = p.layers.iter().map(|l| WotsC::new(l.lw, l.z, l.s)).collect();
        let fors = Fors { k: p.k, a: p.a, forsc: p.forsc };
        let d = p.layers.len();
        let mut s = Signer { p: p.clone(), fors, wots, ctx, cache: (0..d).map(|_| None).collect() };
        let mut total_calls = 0u64;
        // cached layers must be a top segment; build bottom-up
        for layer in 0..d {
            if !p.layers[layer].cached {
                continue;
            }
            let above: u32 = p.layers[layer + 1..].iter().map(|l| l.h).sum();
            let nsub = 1usize << above;
            let hl = p.layers[layer].h;
            let nleaf = 1usize << hl;
            // work items = every (subtree, leaf) of the layer, split over threads: each item computes the WOTS+C
            // public key of the leaf and the smallest accepted counter for the leaf's child value
            let total = nsub * nleaf;
            let chunk = (total + threads - 1) / threads;
            let sref = &s;
            let results: Vec<(Vec<(Node, u32)>, u64)> = std::thread::scope(|sc| {
                let hs: Vec<_> = (0..threads)
                    .map(|ti| {
                        sc.spawn(move || {
                            reset_calls();
                            let lo = ti * chunk;
                            let hi = ((ti + 1) * chunk).min(total);
                            let w = &sref.wots[layer];
                            let mut out = Vec::with_capacity(hi.saturating_sub(lo));
                            for item in lo..hi {
                                let t = (item / nleaf) as u64;
                                let leaf = (item % nleaf) as u32;
                                let pk = w.pk(&sref.ctx, layer as u32, t, leaf);
                                let cv = sref.child_value(layer, t, leaf);
                                let (c, _) = w.grind(&sref.ctx, layer as u32, t, leaf, &cv);
                                out.push((pk, c));
                            }
                            (out, calls())
                        })
                    })
                    .collect();
                hs.into_iter().map(|h| h.join().unwrap()).collect()
            });
            let mut items = Vec::with_capacity(total);
            for (v, c) in results {
                items.extend(v);
                total_calls += c;
            }
            reset_calls();
            let mut subtrees = Vec::with_capacity(nsub);
            let mut ctrs = Vec::with_capacity(nsub);
            for t in 0..nsub {
                let leaves: Vec<Node> = items[t * nleaf..(t + 1) * nleaf].iter().map(|x| x.0).collect();
                subtrees.push(Subtree::build(&s.ctx, Adrs::new(layer as u32, t as u64, T_TREE), leaves));
                ctrs.push(items[t * nleaf..(t + 1) * nleaf].iter().map(|x| x.1).collect());
            }
            total_calls += calls();
            s.cache[layer] = Some(LayerCache { subtrees, ctrs });
        }
        // public root
        reset_calls();
        let top = d - 1;
        let root = match &s.cache[top] {
            Some(c) => c.subtrees[0].root(),
            None => s.compute_subtree(top, 0).root(),
        };
        total_calls += calls();
        s.ctx.pk_root = root;
        let mut cache_bytes = 0u64;
        for c in s.cache.iter().flatten() {
            for st in &c.subtrees {
                cache_bytes += (st.nodes.len() * N) as u64;
            }
            for v in &c.ctrs {
                cache_bytes += (v.len() * 4) as u64;
            }
        }
        let rep = KeygenReport { calls: total_calls, secs: t0.elapsed().as_secs_f64(), cache_bytes };
        (s, rep)
    }

    pub fn pk(&self) -> (Node, Node) {
        (self.ctx.pk_seed, self.ctx.pk_root)
    }

    /// Bind the message digest to `root` instead of this signer's own hypertree root (dual-branch scheme).
    /// Returns the hypertree root, which the caller must keep.
    pub fn bind_digest_to(&mut self, root: Node) -> Node {
        let own = self.ctx.pk_root;
        self.ctx.pk_root = root;
        own
    }

    /// Deterministic signing (R = PRF_msg(SK.prf, m)). use_cache = false recomputes every layer from scratch
    /// (the stateless signer); the output must be byte-identical.
    pub fn sign(&self, m: &[u8], use_cache: bool) -> Vec<u8> {
        let p = &self.p;
        let r = self.ctx.prf_msg(m);
        let inner = self.ctx.hmsg_inner(&r, m);
        let ka = (p.k * p.a) as usize;
        let h = p.htotal() as usize;
        let mut ctr = 0u32;
        let mut dig;
        loop {
            dig = self.ctx.hmsg_outer(&inner, ctr);
            if !p.forsc || get_bits(&dig, ka - p.a as usize, p.a as usize) == 0 {
                break;
            }
            ctr += 1;
        }
        let idxs: Vec<u32> = (0..p.k).map(|j| get_bits(&dig, (j * p.a) as usize, p.a as usize) as u32).collect();
        let idx = get_bits(&dig, ka, h);
        let mut out = Vec::with_capacity(p.sig_bytes());
        out.extend_from_slice(&r);
        if p.forsc {
            out.extend_from_slice(&ctr.to_be_bytes());
        }
        let (t0, k0) = tree_leaf(p, idx, 0);
        let (parts, fpk) = self.fors.sign(&self.ctx, t0, k0, &idxs);
        for (sk, path) in &parts {
            out.extend_from_slice(sk);
            for n in path {
                out.extend_from_slice(n);
            }
        }
        let mut cur = fpk;
        for layer in 0..p.layers.len() {
            let (tree, leaf) = tree_leaf(p, idx, layer);
            let w = &self.wots[layer];
            let cached = if use_cache { self.cache[layer].as_ref() } else { None };
            let (c, st_root, path) = match cached {
                Some(lc) => {
                    let st = &lc.subtrees[tree as usize];
                    (lc.ctrs[tree as usize][leaf as usize], st.root(), st.auth(leaf as usize))
                }
                None => {
                    let (c, _) = w.grind(&self.ctx, layer as u32, tree, leaf, &cur);
                    let st = self.compute_subtree(layer, tree);
                    (c, st.root(), st.auth(leaf as usize))
                }
            };
            let mut c = c;
            let mut dg = w.digits(&w.digest(&self.ctx, layer as u32, tree, leaf, &cur, c));
            if !w.accept(&dg) {
                // a corrupted cache entry (not possible under honest restores): never sign a second digest with
                // this one-time key; recompute the canonical (smallest) counter instead
                let (c2, dg2) = w.grind(&self.ctx, layer as u32, tree, leaf, &cur);
                c = c2;
                dg = dg2;
            }
            let sig = w.sign(&self.ctx, layer as u32, tree, leaf, &dg);
            out.extend_from_slice(&c.to_be_bytes());
            for n in &sig {
                out.extend_from_slice(n);
            }
            for n in &path {
                out.extend_from_slice(n);
            }
            cur = st_root;
        }
        debug_assert_eq!(out.len(), p.sig_bytes());
        out
    }
}

/// Stateless verification from (pk, m, sig) only.
pub fn verify(p: &Params, pk_seed: &Node, pk_root: &Node, m: &[u8], sig: &[u8]) -> bool {
    verify_root(p, pk_seed, pk_root, m, sig) == Some(*pk_root)
}

/// The hypertree root implied by `sig`, with the message digest bound to (pk_seed, bind_root); None if the
/// signature is malformed or a WOTS+C / FORS+C acceptance check fails. Used directly by the dual-branch scheme,
/// whose branches bind the OUTER public key in the message digest.
pub fn verify_root(p: &Params, pk_seed: &Node, bind_root: &Node, m: &[u8], sig: &[u8]) -> Option<Node> {
    if sig.len() != p.sig_bytes() {
        return None;
    }
    let ctx = Ctx::public(*pk_seed, *bind_root);
    let fors = Fors { k: p.k, a: p.a, forsc: p.forsc };
    let mut off = 0usize;
    let take = |off: &mut usize| -> Node {
        let mut x = [0u8; N];
        x.copy_from_slice(&sig[*off..*off + N]);
        *off += N;
        x
    };
    let take4 = |off: &mut usize| -> u32 {
        let v = u32::from_be_bytes([sig[*off], sig[*off + 1], sig[*off + 2], sig[*off + 3]]);
        *off += 4;
        v
    };
    let r = take(&mut off);
    let ctr = if p.forsc { take4(&mut off) } else { 0 };
    let inner = ctx.hmsg_inner(&r, m);
    let dig = ctx.hmsg_outer(&inner, ctr);
    let ka = (p.k * p.a) as usize;
    if p.forsc && get_bits(&dig, ka - p.a as usize, p.a as usize) != 0 {
        return None;
    }
    let idxs: Vec<u32> = (0..p.k).map(|j| get_bits(&dig, (j * p.a) as usize, p.a as usize) as u32).collect();
    let idx = get_bits(&dig, ka, p.htotal() as usize);
    let mut parts = Vec::new();
    for _ in 0..fors.real_trees() {
        let sk = take(&mut off);
        let path: Vec<Node> = (0..p.a).map(|_| take(&mut off)).collect();
        parts.push((sk, path));
    }
    let (t0, k0) = tree_leaf(p, idx, 0);
    let mut cur = fors.pk_from_sig(&ctx, t0, k0, &idxs, &parts);
    for layer in 0..p.layers.len() {
        let lp = &p.layers[layer];
        let w = WotsC::new(lp.lw, lp.z, lp.s);
        let (tree, leaf) = tree_leaf(p, idx, layer);
        let c = take4(&mut off);
        let dg = w.digits(&w.digest(&ctx, layer as u32, tree, leaf, &cur, c));
        if !w.accept(&dg) {
            return None;
        }
        let ws: Vec<Node> = (0..w.l).map(|_| take(&mut off)).collect();
        let wpk = w.pk_from_sig(&ctx, layer as u32, tree, leaf, &ws, &dg);
        let path: Vec<Node> = (0..lp.h).map(|_| take(&mut off)).collect();
        cur = root_from_path(&ctx, Adrs::new(layer as u32, tree, T_TREE), &wpk, leaf, &path);
    }
    Some(cur)
}
