/* SLH-DSA through OpenSSL 3.5.7 libcrypto (Git for Windows build), loaded at run time; no OpenSSL headers needed.
 * One thread. Whole-message ("pure") signing: EVP_PKEY_sign_message_init + EVP_PKEY_sign, empty context.
 * Timing: QueryPerformanceCounter around ONE call each (Sign, Verify). Verify result is checked outside the Sign timer.
 * Usage: slhdsa_ossl <alg> <msg_bytes> <N> <csv_out> [dll_dir]
 * alg: SLH-DSA-SHA2-128s | SLH-DSA-SHA2-128f.  Output columns:
 * alg,msg_bytes,rep,operation,ns,sig_bytes,verified
 * Negative controls (not timed): message altered at the last byte and at byte 0, signature altered; all must reject. */
#include <windows.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>

typedef void *P;
static P (*Q_keygen)(P, const char *, const char *, ...);
static P (*CTX_new)(P, P, const char *);
static void (*CTX_free)(P);
static void (*PKEY_free)(P);
static int (*SIGN_MI)(P, P, const void *);
static int (*VER_MI)(P, P, const void *);
static int (*SIGN)(P, unsigned char *, size_t *, const unsigned char *, size_t);
static int (*VER)(P, const unsigned char *, size_t, const unsigned char *, size_t);
static int (*GETPUB)(P, unsigned char *, size_t, size_t *);

static LARGE_INTEGER F;
static uint64_t now_ns(void) { LARGE_INTEGER c; QueryPerformanceCounter(&c); uint64_t q = (uint64_t)c.QuadPart, fq = (uint64_t)F.QuadPart; return (q / fq) * 1000000000ULL + (q % fq) * 1000000000ULL / fq; }
static void *sym(HMODULE h, const char *n) { void *p = (void *)GetProcAddress(h, n); if (!p) { fprintf(stderr, "missing symbol %s\n", n); exit(2); } return p; }
static void message(unsigned char *m, size_t n, uint64_t rep) {
    for (size_t i = 0; i < n; i++) m[i] = (unsigned char)((i * 131 + rep * 17 + 19) & 255);
    if (n >= 8) memcpy(m, &rep, 8);
}

int main(int argc, char **argv) {
    if (argc < 5) { fprintf(stderr, "usage\n"); return 1; }
    const char *alg = argv[1]; size_t mb = (size_t)atoll(argv[2]); int N = atoi(argv[3]); const char *out = argv[4];
    const char *dir = argc > 5 ? argv[5] : getenv("LULA_OPENSSL_DLL_DIR");
    if (!dir || !*dir) { fprintf(stderr, "Set LULA_OPENSSL_DLL_DIR or pass dll_dir\n"); return 2; }
    SetDllDirectoryA(dir);
    char path[512]; snprintf(path, sizeof path, "%s\\libcrypto-3-x64.dll", dir);
    HMODULE h = LoadLibraryA(path); if (!h) { fprintf(stderr, "LoadLibrary failed %lu\n", GetLastError()); return 2; }
    Q_keygen = sym(h, "EVP_PKEY_Q_keygen"); CTX_new = sym(h, "EVP_PKEY_CTX_new_from_pkey"); CTX_free = sym(h, "EVP_PKEY_CTX_free");
    PKEY_free = sym(h, "EVP_PKEY_free"); SIGN_MI = sym(h, "EVP_PKEY_sign_message_init"); VER_MI = sym(h, "EVP_PKEY_verify_message_init");
    SIGN = sym(h, "EVP_PKEY_sign"); VER = sym(h, "EVP_PKEY_verify"); GETPUB = sym(h, "EVP_PKEY_get_octet_string_param");
    QueryPerformanceFrequency(&F);
    FILE *f = fopen(out, "w"); if (!f) return 3;
    fprintf(f, "alg,msg_bytes,rep,operation,ns,sig_bytes,verified\n");
    uint64_t t0 = now_ns();
    P pkey = Q_keygen(NULL, NULL, alg);
    uint64_t t1 = now_ns();
    if (!pkey) { fprintf(stderr, "keygen failed\n"); return 4; }
    fprintf(f, "%s,%zu,0,keygen,%llu,0,1\n", alg, mb, (unsigned long long)(t1 - t0));
    P sctx = CTX_new(NULL, pkey, NULL), vctx = CTX_new(NULL, pkey, NULL);
    if (!sctx || !vctx || SIGN_MI(sctx, NULL, NULL) != 1 || VER_MI(vctx, NULL, NULL) != 1) { fprintf(stderr, "init failed\n"); return 5; }
    unsigned char *m = malloc(mb ? mb : 1), *m2 = malloc(mb ? mb : 1), *sig = malloc(65536);
    int bad = 0;
    for (int r = 1; r <= N; r++) {
        message(m, mb, (uint64_t)r);
        size_t sl = 65536;
        uint64_t a = now_ns(); int ok = SIGN(sctx, sig, &sl, m, mb); uint64_t b = now_ns();
        fprintf(f, "%s,%zu,%d,sign,%llu,%zu,%d\n", alg, mb, r, (unsigned long long)(b - a), sl, ok == 1);
        uint64_t c = now_ns(); int v = VER(vctx, sig, sl, m, mb); uint64_t d = now_ns();
        fprintf(f, "%s,%zu,%d,verify,%llu,%zu,%d\n", alg, mb, r, (unsigned long long)(d - c), sl, v == 1);
        if (ok != 1 || v != 1) bad++;
        if (r <= 3 || r == N) { /* negative controls, untimed */
            memcpy(m2, m, mb); m2[mb - 1] ^= 1; int n1 = VER(vctx, sig, sl, m2, mb);
            memcpy(m2, m, mb); m2[0] ^= 1; int n2 = VER(vctx, sig, sl, m2, mb);
            sig[sl / 2] ^= 1; int n3 = VER(vctx, sig, sl, m, mb); sig[sl / 2] ^= 1;
            fprintf(f, "%s,%zu,%d,negative_controls_rejected,0,%zu,%d\n", alg, mb, r, sl, (n1 != 1) && (n2 != 1) && (n3 != 1));
            if (!((n1 != 1) && (n2 != 1) && (n3 != 1))) bad++;
        }
    }
    fclose(f);
    printf("done alg=%s msg=%zu N=%d failures=%d\n", alg, mb, N, bad);
    return bad ? 6 : 0;
}
