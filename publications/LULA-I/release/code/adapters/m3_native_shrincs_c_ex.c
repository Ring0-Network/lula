/* Measurement-only driver for unchanged upstream C B32 primitives. */
#define WIN32_LEAN_AND_MEAN
#include <windows.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "shrincs.h"
static long long tick(void){LARGE_INTEGER t;QueryPerformanceCounter(&t);return t.QuadPart;}
static long long ns(long long t){LARGE_INTEGER f;QueryPerformanceFrequency(&f);return (long long)((tick()-t)*1e9/f.QuadPart);}
static void hex(FILE*f,const unsigned char*b,size_t n){for(size_t i=0;i<n;i++)fprintf(f,"%02x",b[i]);}
int main(int argc,char**argv){
 if(argc<4)return 2;
 PublicKey pk;SecretKey sk;State state;long long t=tick();
 if(!strcmp(argv[1],"prepare")){
  shrincs_key_gen(&pk,&sk,&state);long long elapsed=ns(t);
  FILE*f=fopen(argv[3],"wb");if(!f)return 3;
  fwrite(&pk,sizeof pk,1,f);fwrite(&sk,sizeof sk,1,f);fwrite(&state,sizeof state,1,f);fclose(f);
  printf("{\"candidate\":\"shrincs-c-b32\",\"keygen_ns\":%lld,\"pk_bytes\":%u,\"sf_first_bytes\":%u,\"fallback_bytes\":%u}\n",elapsed,2*N,N+WOTS_SIGN_LEN+N,SL_SIZE);return 0;
 }
 if(argc<9)return 2;
 FILE*f=fopen(argv[3],"rb");if(!f)return 3;
 if(fread(&pk,sizeof pk,1,f)!=1||fread(&sk,sizeof sk,1,f)!=1||fread(&state,sizeof state,1,f)!=1)return 4;fclose(f);
 const char*sc=argv[4];unsigned n=(unsigned)atoi(argv[5]),reps=(unsigned)atoi(argv[6]);
 if(n<32||n>65536)return 5;
 FILE*out=fopen(argv[7],"w");if(!out)return 3;
 fprintf(out,"candidate,scenario,message_bytes,rep,operation,ns,hash_calls,sig_bytes,pk_bytes,valid,state_counter\n");
 if(!strcmp(sc,"missing")){shrincs_restore(sk.seed,&pk,&sk,&state);}
 fprintf(out,"shrincs-c-b32,%s,%u,0,fixture_load_or_restore,%lld,,0,%u,true,%u\n",sc,n,ns(t),2*N,state.q);
 State snapshot=state;
 if(!strcmp(sc,"exhaustion"))state.q=HSF-3; /* campaign addition: state is only a counter; place it 3 before the last valid index */
 unsigned char *msg=malloc(n),*sig=malloc(SL_SIZE+MAX_SF_SIZE);
 for(unsigned r=0;r<reps;r++){
  if(!strcmp(sc,"restored"))state=snapshot;
  for(unsigned i=0;i<n;i++)msg[i]=(unsigned char)(i*131+r*17+19);
  for(unsigned i=0;i<8;i++)msg[i]=(unsigned char)(((unsigned long long)r)>>(8*i));
  unsigned q=state.q;unsigned sl=!strcmp(sc,"fallback")||!strcmp(sc,"missing")||(!strcmp(sc,"exhaustion")&&state.q>=HSF+1);unsigned len;
  t=tick();unsigned ok;
  if(sl){len=SL_SIZE;ok=shrincs_sign_stateless(msg,n,&sk,sig);}
  else {len=N+WOTS_SIGN_LEN+((state.q+1>HSF)?HSF:(state.q+1))*N;ok=shrincs_sign_stateful(msg,n,&sk,&state,sig);}
  long long elapsed=ns(t);if(!ok)return 6;
  t=tick();ok=shrincs_verify(msg,n,sig,len,&pk);long long vns=ns(t);
  fprintf(out,"shrincs-c-b32,%s,%u,%u,sign,%lld,,%u,%u,%s,%u\n",sc,n,r,elapsed,len,2*N,ok?"true":"false",q);
  fprintf(out,"shrincs-c-b32,%s,%u,%u,verify,%lld,,%u,%u,%s,%u\n",sc,n,r,vns,len,2*N,ok?"true":"false",q);fflush(out);
  if(!ok)return 7;
  if(r==0){
   FILE*v=fopen(argv[8],"w");fprintf(v,"{\"kind\":\"shrincs-c-b32\",\"pk_hex\":\"");hex(v,pk.seed,N);hex(v,pk.root,N);
   fprintf(v,"\",\"msg_hex\":\"");hex(v,msg,n);fprintf(v,"\",\"sig_hex\":\"");hex(v,sig,len);fprintf(v,"\"}");fclose(v);
   msg[8]^=1;unsigned badmsg=!shrincs_verify(msg,n,sig,len,&pk);msg[8]^=1;
   pk.root[0]^=1;unsigned badpk=!shrincs_verify(msg,n,sig,len,&pk);pk.root[0]^=1;
   sig[len-1]^=1;unsigned badsig=!shrincs_verify(msg,n,sig,len,&pk);sig[len-1]^=1;
   printf("{\"negative_tests\":{\"message\":%u,\"pk\":%u,\"signature\":%u}}\n",badmsg,badpk,badsig);
  }
 }
 fclose(out);free(msg);free(sig);return 0;
}
