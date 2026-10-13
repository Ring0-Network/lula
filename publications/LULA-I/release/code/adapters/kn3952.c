/* KN-3952-RECON: independent reconstruction of the Kudinov-Nick 3,952 B row (ePrint 2025/2203: W+C, FORS,
 * h=44 d=4 a=16 k=8 w=256 l=16 S_wn=2040, n=16). NOT the authors' code and NOT interoperable with any author implementation.
 * Reused unchanged from the SHRINCS author C library (commit 345b0a64...): WOTS+C chains/grinding (wots_c.c), XMSS
 * verification path (xmss_pk_from_sig), address setters, hash context helpers. Written here: plain FORS (k=8 trees of 2^16
 * leaves), H_msg, the hypertree signing loop (root and authentication path computed in ONE pass per layer, unlike the library's
 * xmss_sign), and the driver. Domain-separation types 0x20..0x23 are this reconstruction's own choice.
 * Signature = R(32) | 8 x [sk(16) | auth 16x16] | 4 x [counter(4) | 16 x 16 | auth 11 x 16] = 3,952 B.
 * Usage: kn3952 prepare x <state> | run x <state> <scenario> <msg_bytes> <reps> <csv> <vec.json>   (scenario: hot|fresh) */
#define WIN32_LEAN_AND_MEAN
#include <windows.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <openssl/rand.h>
#include "xmss.h"

#define KK 8
#define AA 16
#define HH 44
#define DD 4
#define HP 11
#define FORS_PRF_T   0x20u
#define FORS_TREE_T  0x21u
#define FORS_ROOTS_T 0x22u
#define KN_HMSG_T    0x23u
#define LEAVES (1u << AA)
#define FORS_SIG (KK * (N + AA * N))
#define LAYER_SIG (4 + L * N + HP * N)
#define SIG_LEN (32 + FORS_SIG + DD * LAYER_SIG)

static LARGE_INTEGER F;
static long long tick(void) { LARGE_INTEGER t; QueryPerformanceCounter(&t); return t.QuadPart; }
static long long ns_since(long long t) { long long d = tick() - t; return (d / F.QuadPart) * 1000000000LL + (d % F.QuadPart) * 1000000000LL / F.QuadPart; }

typedef struct { uint8_t sk_seed[N], sk_prf[N], pk_seed[N], root[N]; } Key;

static void init_ctx(SHA256_CTX *c, const uint8_t *pk_seed) {
    uint8_t z[32] = {0};
    SHA256_Init(c);
    sha256_add_to_ctx(c, pk_seed, N);
    sha256_add_to_ctx(c, z, 32);
    sha256_add_to_ctx(c, z, 16);
}
static void fors_sk(const SHA256_CTX *h, const uint8_t *sk_seed, uint8_t *adrs, uint32_t kp, uint32_t gidx, uint8_t *out) {
    setTypeAndClear(adrs, FORS_PRF_T); setKeyPairAddress(adrs, kp); setTreeIndex(adrs, gidx);
    SHA256_CTX c = *h; sha256_add_to_ctx(&c, adrs, 32); sha256_add_to_ctx(&c, sk_seed, N); SHA256_Finalize(&c, out);
}
static void fors_leaf_from_sk(const SHA256_CTX *h, uint8_t *adrs, uint32_t kp, uint32_t gidx, const uint8_t *sk, uint8_t *out) {
    setTypeAndClear(adrs, FORS_TREE_T); setKeyPairAddress(adrs, kp); setTreeHeight(adrs, 0); setTreeIndex(adrs, gidx);
    SHA256_CTX c = *h; sha256_add_to_ctx(&c, adrs, 32); sha256_add_to_ctx(&c, sk, N); SHA256_Finalize(&c, out);
}
static void fors_node(const SHA256_CTX *h, uint8_t *adrs, uint32_t kp, uint32_t z, uint32_t gidx, const uint8_t *l, const uint8_t *r, uint8_t *out) {
    setTypeAndClear(adrs, FORS_TREE_T); setKeyPairAddress(adrs, kp); setTreeHeight(adrs, z); setTreeIndex(adrs, gidx);
    SHA256_CTX c = *h; sha256_add_to_ctx(&c, adrs, 32); sha256_add_to_ctx(&c, l, N); sha256_add_to_ctx(&c, r, N); SHA256_Finalize(&c, out);
}
static void fors_roots_compress(const SHA256_CTX *h, uint8_t *adrs, uint32_t kp, const uint8_t *roots, uint8_t *out) {
    setTypeAndClear(adrs, FORS_ROOTS_T); setKeyPairAddress(adrs, kp);
    SHA256_CTX c = *h; sha256_add_to_ctx(&c, adrs, 32); sha256_add_to_ctx(&c, roots, KK * N); SHA256_Finalize(&c, out);
}
/* message hash: 22 bytes needed (k*a + h = 172 bits); one SHA-256 block of output is used */
static void h_msg(const SHA256_CTX *h, uint8_t *adrs, const uint8_t *R, const uint8_t *root, const uint8_t *m, uint32_t ml, uint8_t dig[32]) {
    setTypeAndClear(adrs, KN_HMSG_T);
    SHA256_CTX c = *h; sha256_add_to_ctx(&c, adrs, 32); sha256_add_to_ctx(&c, R, 32); sha256_add_to_ctx(&c, root, N);
    sha256_add_to_ctx(&c, m, ml); SHA256_Finalize_32(&c, dig);
}
static void split(const uint8_t *dig, uint32_t idx[KK], uint64_t tree[DD], uint32_t leaf[DD]) {
    for (int i = 0; i < KK; i++) idx[i] = ((uint32_t)dig[2 * i] << 8) | dig[2 * i + 1];
    uint64_t v = 0; for (int i = 0; i < 6; i++) v = (v << 8) | dig[16 + i];
    v &= ((1ULL << HH) - 1);
    for (int l = 0; l < DD; l++) { leaf[l] = (uint32_t)(v & ((1u << HP) - 1)); v >>= HP; tree[l] = v; }
}

/* one layer: WOTS+C signature on msg from the library, plus root and auth path from a single pass over the 2^11 leaves */
static void layer_sign(const Key *k, const SHA256_CTX *h, uint8_t *adrs, const uint8_t *msg, uint32_t leaf, uint8_t *out, uint8_t *root_out) {
    SHA256_CTX hc = *h;
    wots_sign(msg, N, k->sk_seed, k->sk_prf, k->pk_seed, k->root, &hc, adrs, leaf, 0, 1, out);
    static uint8_t lv[1u << HP][N];
    for (uint32_t i = 0; i < (1u << HP); i++) wots_pk_gen(k->sk_seed, &hc, adrs, i, 0, lv[i]);
    uint32_t n = 1u << HP, idx = leaf;
    for (uint32_t z = 1; z <= HP; z++) {
        memcpy(out + WOTS_SIGN_LEN + (z - 1) * N, lv[idx ^ 1], N);
        for (uint32_t i = 0; i < n / 2; i++) {
            uint8_t o[N];
            setTypeAndClear(adrs, SL_TREE); setTreeHeight(adrs, z); setTreeIndex(adrs, i);
            SHA256_CTX c = hc; sha256_add_to_ctx(&c, adrs, 32); sha256_add_to_ctx(&c, lv[2 * i], N); sha256_add_to_ctx(&c, lv[2 * i + 1], N);
            SHA256_Finalize(&c, o); memcpy(lv[i], o, N);
        }
        n /= 2; idx >>= 1;
    }
    memcpy(root_out, lv[0], N);
}

static void keygen(Key *k, const uint8_t seed[48]) {
    memcpy(k->sk_seed, seed, N); memcpy(k->sk_prf, seed + N, N); memcpy(k->pk_seed, seed + 2 * N, N);
    SHA256_CTX h; init_ctx(&h, k->pk_seed);
    uint8_t adrs[32] = {0}; setLayerAddress(adrs, DD - 1); setTreeAddress(adrs, 0, 0);
    xmss_root(k->sk_seed, &h, adrs, HP, k->root);
}

static int sign(const Key *k, const uint8_t *m, uint32_t ml, uint8_t *sig) {
    SHA256_CTX h; init_ctx(&h, k->pk_seed);
    uint8_t adrs[32] = {0}, opt[N]; memcpy(opt, k->pk_seed, N);
    prf_msg(k->sk_prf, k->pk_seed, opt, m, ml, 0, 0, 32, sig);              /* R */
    uint8_t dig[32]; h_msg(&h, adrs, sig, k->root, m, ml, dig);
    uint32_t idx[KK], leaf[DD]; uint64_t tree[DD]; split(dig, idx, tree, leaf);
    uint8_t roots[KK * N]; uint8_t *p = sig + 32;
    static uint8_t lv[LEAVES][N];
    for (int i = 0; i < KK; i++) {
        uint32_t base = (uint32_t)i * LEAVES;
        for (uint32_t j = 0; j < LEAVES; j++) {
            uint8_t sk[N]; setLayerAddress(adrs, 0); setTreeAddress(adrs, 0, tree[0]);
            fors_sk(&h, k->sk_seed, adrs, leaf[0], base + j, sk);
            if (j == idx[i]) memcpy(p, sk, N);
            fors_leaf_from_sk(&h, adrs, leaf[0], base + j, sk, lv[j]);
        }
        p += N;
        uint32_t n = LEAVES, ix = idx[i];
        for (uint32_t z = 1; z <= AA; z++) {
            memcpy(p + (z - 1) * N, lv[ix ^ 1], N);
            for (uint32_t j = 0; j < n / 2; j++) {
                uint8_t o[N]; fors_node(&h, adrs, leaf[0], z, (base >> z) + j, lv[2 * j], lv[2 * j + 1], o); memcpy(lv[j], o, N);
            }
            n /= 2; ix >>= 1;
        }
        memcpy(roots + i * N, lv[0], N); p += AA * N;
    }
    uint8_t msg[N]; setLayerAddress(adrs, 0); setTreeAddress(adrs, 0, tree[0]);
    fors_roots_compress(&h, adrs, leaf[0], roots, msg);
    for (int l = 0; l < DD; l++) {
        setLayerAddress(adrs, l); setTreeAddress(adrs, 0, tree[l]);
        uint8_t root[N]; layer_sign(k, &h, adrs, msg, leaf[l], p, root); memcpy(msg, root, N); p += LAYER_SIG;
    }
    return memcmp(msg, k->root, N) == 0;
}

static int verify(const uint8_t pk_seed[N], const uint8_t root[N], const uint8_t *m, uint32_t ml, const uint8_t *sig, uint32_t sl) {
    if (sl != SIG_LEN) return 0;
    SHA256_CTX h; init_ctx(&h, pk_seed); uint8_t adrs[32] = {0};
    uint8_t dig[32]; h_msg(&h, adrs, sig, root, m, ml, dig);
    uint32_t idx[KK], leaf[DD]; uint64_t tree[DD]; split(dig, idx, tree, leaf);
    uint8_t roots[KK * N]; const uint8_t *p = sig + 32;
    for (int i = 0; i < KK; i++) {
        uint32_t base = (uint32_t)i * LEAVES; uint8_t cur[N], t[N];
        setLayerAddress(adrs, 0); setTreeAddress(adrs, 0, tree[0]);
        fors_leaf_from_sk(&h, adrs, leaf[0], base + idx[i], p, cur);
        const uint8_t *auth = p + N; uint32_t ix = idx[i];
        for (uint32_t z = 1; z <= AA; z++) {
            if ((ix & 1) == 0) fors_node(&h, adrs, leaf[0], z, (base >> z) + (ix >> 1), cur, auth + (z - 1) * N, t);
            else fors_node(&h, adrs, leaf[0], z, (base >> z) + (ix >> 1), auth + (z - 1) * N, cur, t);
            memcpy(cur, t, N); ix >>= 1;
        }
        memcpy(roots + i * N, cur, N); p += N + AA * N;
    }
    uint8_t msg[N]; setLayerAddress(adrs, 0); setTreeAddress(adrs, 0, tree[0]);
    fors_roots_compress(&h, adrs, leaf[0], roots, msg);
    for (int l = 0; l < DD; l++) {
        setLayerAddress(adrs, l); setTreeAddress(adrs, 0, tree[l]);
        uint8_t out[N]; SHA256_CTX hc = h;
        xmss_pk_from_sig(p, p + WOTS_SIGN_LEN, msg, root, &hc, adrs, HP, leaf[l], out);
        memcpy(msg, out, N); p += LAYER_SIG;
    }
    return memcmp(msg, root, N) == 0;
}

static void hexw(FILE *f, const uint8_t *b, size_t n) { for (size_t i = 0; i < n; i++) fprintf(f, "%02x", b[i]); }
int main(int argc, char **argv) {
    QueryPerformanceFrequency(&F);
    if (argc < 4) return 2;
    Key k; long long t = tick();
    if (!strcmp(argv[1], "prepare")) {
        uint8_t seed[48]; for (int i = 0; i < 48; i++) seed[i] = (uint8_t)(i * 7 + 3);   /* benchmark fixture seed, not entropy */
        keygen(&k, seed); long long e = ns_since(t);
        FILE *f = fopen(argv[3], "wb"); if (!f) return 3; fwrite(&k, sizeof k, 1, f); fclose(f);
        printf("{\"candidate\":\"kn3952-recon\",\"keygen_ns\":%lld,\"sig_bytes\":%d,\"pk_bytes\":32}\n", e, SIG_LEN); return 0;
    }
    if (argc < 9) return 2;
    FILE *f = fopen(argv[3], "rb"); if (!f || fread(&k, sizeof k, 1, f) != 1) return 3; fclose(f);
    const char *sc = argv[4]; uint32_t n = (uint32_t)atoi(argv[5]), reps = (uint32_t)atoi(argv[6]);
    FILE *out = fopen(argv[7], "w"); if (!out) return 3;
    fprintf(out, "candidate,scenario,message_bytes,rep,operation,ns,hash_calls,sig_bytes,pk_bytes,valid\n");
    fprintf(out, "kn3952-recon,%s,%u,0,fixture_load,%lld,,0,32,true\n", sc, n, ns_since(t));
    uint8_t *msg = malloc(n), *sig = malloc(SIG_LEN);
    for (uint32_t r = 0; r < reps; r++) {
        for (uint32_t i = 0; i < n; i++) msg[i] = (uint8_t)(i * 131 + r * 17 + 19);
        for (int i = 0; i < 8; i++) msg[i] = (uint8_t)(((unsigned long long)r) >> (8 * i));
        t = tick(); int ok = sign(&k, msg, n, sig); long long sn = ns_since(t);
        t = tick(); int v = verify(k.pk_seed, k.root, msg, n, sig, SIG_LEN); long long vn = ns_since(t);
        fprintf(out, "kn3952-recon,%s,%u,%u,sign,%lld,,%d,32,%s\n", sc, n, r, sn, SIG_LEN, ok ? "true" : "false");
        fprintf(out, "kn3952-recon,%s,%u,%u,verify,%lld,,%d,32,%s\n", sc, n, r, vn, SIG_LEN, v ? "true" : "false");
        fflush(out);
        if (!ok || !v) return 6;
        if (r == 0) {
            FILE *vf = fopen(argv[8], "w");
            fprintf(vf, "{\"kind\":\"kn3952-recon\",\"pk_hex\":\""); hexw(vf, k.pk_seed, N); hexw(vf, k.root, N);
            fprintf(vf, "\",\"msg_hex\":\""); hexw(vf, msg, n); fprintf(vf, "\",\"sig_hex\":\""); hexw(vf, sig, SIG_LEN); fprintf(vf, "\"}"); fclose(vf);
            int rej[6] = {0}; uint8_t *bad = malloc(SIG_LEN);
            msg[0] ^= 1; rej[0] = !verify(k.pk_seed, k.root, msg, n, sig, SIG_LEN); msg[0] ^= 1;
            msg[n - 1] ^= 1; rej[1] = !verify(k.pk_seed, k.root, msg, n, sig, SIG_LEN); msg[n - 1] ^= 1;
            size_t pos[4] = {0, 40, 32 + FORS_SIG + 10, SIG_LEN - 1};
            for (int j = 0; j < 4; j++) { memcpy(bad, sig, SIG_LEN); bad[pos[j]] ^= 1; rej[2 + j] = !verify(k.pk_seed, k.root, msg, n, bad, SIG_LEN); }
            int shortrej = !verify(k.pk_seed, k.root, msg, n, sig, SIG_LEN - 1);
            uint8_t badroot[N]; memcpy(badroot, k.root, N); badroot[0] ^= 1; int pkrej = !verify(k.pk_seed, badroot, msg, n, sig, SIG_LEN);
            printf("{\"negative_tests\":{\"msg_first\":%d,\"msg_last\":%d,\"R\":%d,\"fors\":%d,\"layer\":%d,\"last_byte\":%d,\"short\":%d,\"pk\":%d}}\n",
                   rej[0], rej[1], rej[2], rej[3], rej[4], rej[5], shortrej, pkrej);
            free(bad);
        }
    }
    fclose(out); return 0;
}
