// SPDX-License-Identifier: Apache-2.0
// Campaign driver: imported library primitives are unchanged. All keys are synthetic fixtures.
package main

import (
 "bytes"
 "context"
 "encoding/binary"
 "encoding/hex"
 "encoding/json"
 "fmt"
 "os"
 "runtime"
 "strconv"

 hash "github.com/andrepatta/hashsig/go/internal/hash"
 "github.com/andrepatta/hashsig/go/pors"
 "github.com/andrepatta/hashsig/go/shrincs"
 "github.com/andrepatta/hashsig/go/sphincs"
 "github.com/andrepatta/hashsig/go/state"
 "github.com/andrepatta/hashsig/go/state/filestate"
 "github.com/andrepatta/hashsig/go/wotsc"
)

type fixture struct {Kind string `json:"kind"`; Seed string `json:"seed_hex"`; PK string `json:"pk_hex"`}
type memoryIO struct {data []byte; writeNS int64; readNS int64}
func(m *memoryIO)Read()([]byte,error){if m.data==nil{return nil,os.ErrNotExist};return bytes.Clone(m.data),nil}
func(m *memoryIO)Write(b []byte)error{t:=qnow();m.data=bytes.Clone(b);m.writeNS=qns(t);return nil}
type timedIO struct {base state.StateIO; writeNS int64; readNS int64}
func(m *timedIO)Read()([]byte,error){t:=qnow();b,e:=m.base.Read();m.readNS=qns(t);return b,e}
func(m *timedIO)Write(b []byte)error{t:=qnow();e:=m.base.Write(b);m.writeNS=qns(t);return e}
func must(err error){if err!=nil{panic(err)}}
func unhex(s string)[]byte{b,e:=hex.DecodeString(s);must(e);return b}
func number(s string)int{n,e:=strconv.Atoi(s);must(e);return n}
func message(n,rep int)[]byte{b:=make([]byte,n);for i:=range b{b[i]=byte((i*131+rep*17+19)&255)};binary.LittleEndian.PutUint64(b[:8],uint64(rep));return b}
func knparams()sphincs.SPHINCSParams{
 w,e:=wotsc.NewWOTSPlusCParams(16,16,256,0,2040,32);must(e)
 return sphincs.SPHINCSParams{N:16,H:40,D:5,WOTS:w,PORS:pors.PORSParams{N:16,K:11,ALog2:14,RBits:32,MMax:118},RBits:32}
}
func knkey()(*hash.Params,[]byte,[]byte){return &hash.Params{N:16,PKSeed:bytes.Repeat([]byte{3},16)},bytes.Repeat([]byte{1},16),bytes.Repeat([]byte{2},16)}
func seed32()([32]byte){var s [32]byte;for i:=range s{s[i]=byte(i+31)};return s}
func save(path string,x any){b,e:=json.MarshalIndent(x,"","  ");must(e);must(os.WriteFile(path,b,0600))}
func load(path string)fixture{b,e:=os.ReadFile(path);must(e);var f fixture;must(json.Unmarshal(b,&f));return f}
func writeVector(path string,kind string,pk,msg,sig []byte){save(path,map[string]any{"kind":kind,"pk_hex":hex.EncodeToString(pk),"msg_hex":hex.EncodeToString(msg),"sig_hex":hex.EncodeToString(sig)})}
func verifyShrincs(pk,msg,wire []byte)bool{s,e:=shrincs.DeserializeSig(wire);return e==nil&&shrincs.Verify(pk,msg,s)}
func negatives(pk,msg,sig []byte,verify func([]byte,[]byte,[]byte)bool)map[string]bool{
 tests:=map[string]bool{}
 for _,i:=range []int{0,16,len(sig)/2,len(sig)-1}{bad:=bytes.Clone(sig);bad[i]^=1;tests[fmt.Sprintf("byte_flip_%d_rejected",i)]=!verify(pk,msg,bad)}
 bad:=bytes.Clone(msg);bad[8]^=1;tests["wrong_message_rejected"]=!verify(pk,bad,sig)
 badpk:=bytes.Clone(pk);badpk[len(badpk)-1]^=1;tests["wrong_pk_rejected"]=!verify(badpk,msg,sig)
 tests["truncated_rejected"]=!verify(pk,msg,sig[:len(sig)-1])
 tests["appended_rejected"]=!verify(pk,msg,append(bytes.Clone(sig),0))
 return tests
}
func main(){
 if runtime.GOMAXPROCS(0)!=1{panic("GOMAXPROCS must be 1")}
 a:=os.Args[1:];if len(a)<3{panic("prepare|bench kn4036|shrincs fixture [scenario bytes reps csv vector statepath]")}
 op,kind,path:=a[0],a[1],a[2];ctx:=context.Background();t:=qnow()
 if op=="verify"{
  data,e:=os.ReadFile(path);must(e);var v map[string]string;must(json.Unmarshal(data,&v))
  pub,msg,wire:=unhex(v["pk_hex"]),unhex(v["msg_hex"]),unhex(v["sig_hex"])
  ok:=false;if kind=="shrincs"{ok=verifyShrincs(pub,msg,wire)}else{sp:=knparams();ok=sp.Verify(&hash.Params{N:16,PKSeed:pub[:16]},msg,wire,pub[16:])}
  fmt.Printf("{\"verified\":%t}\n",ok);if !ok{os.Exit(1)};return
 }
 if op=="prepare"{
  if kind=="kn4036"{p,s,_:=knkey();sp:=knparams();pk,e:=sp.GenPK(p,s);must(e);ns:=qns(t);pub:=append(bytes.Clone(p.PKSeed),pk...);f:=fixture{Kind:kind,Seed:hex.EncodeToString(append(bytes.Clone(s),bytes.Repeat([]byte{2},16)...)),PK:hex.EncodeToString(pub)};save(path,f);fmt.Printf("{\"candidate\":\"kn4036\",\"keygen_ns\":%d,\"sig_bytes\":%d,\"pk_bytes\":32,\"gomaxprocs\":1}\n",ns,sp.SigSize());return}
  if kind=="shrincs"{s:=seed32();k,e:=shrincs.NewStatefulKey(ctx,s,nil);must(e);ns:=qns(t);save(path,fixture{Kind:kind,Seed:hex.EncodeToString(s[:]),PK:hex.EncodeToString(k.PublicKey)});fmt.Printf("{\"candidate\":\"shrincs-go\",\"keygen_ns\":%d,\"pk_bytes\":%d,\"slots\":%d,\"stateful_body_first_bytes\":%d,\"fallback_body_bytes\":%d}\n",ns,len(k.PublicKey),k.NumSlots(),k.StatefulBodyLen(0),k.StatelessBodyLen());return}
  panic("unknown candidate")
 }
 f:=load(path);if f.Kind!=kind{panic("fixture kind mismatch")};scenario:=a[3];n,reps:=number(a[4]),number(a[5]);csv,vector:=a[6],a[7]
 out,e:=os.Create(csv);must(e);defer out.Close();fmt.Fprintln(out,"candidate,scenario,message_bytes,rep,operation,ns,hash_calls,sig_bytes,pk_bytes,valid,alloc_bytes,mallocs,state_counter,body_bytes")
 emit:=func(candidate,operation string,rep int,ns int64,siglen int,ok bool,alloc,malloc uint64,q uint64,body int){fmt.Fprintf(out,"%s,%s,%d,%d,%s,%d,,%d,%d,%t,%d,%d,%d,%d\n",candidate,scenario,n,rep,operation,ns,siglen,len(unhex(f.PK)),ok,alloc,malloc,q,body);must(out.Sync())}
 if kind=="kn4036"{
  p,s,prf:=knkey();sp:=knparams();pk:=unhex(f.PK);root:=pk[16:];emit(kind,"fixture_load",0,qns(t),0,true,0,0,0,0)
  verify:=func(pub,m,sig []byte)bool{if len(pub)!=32{return false};return sp.Verify(&hash.Params{N:16,PKSeed:pub[:16]},m,sig,pub[16:])}
  for rep:=0;rep<reps;rep++{
   msg:=message(n,rep);var before,after runtime.MemStats;runtime.ReadMemStats(&before);t=qnow();sig,e:=sp.Sign(p,s,prf,nil,msg,root);ns:=qns(t);must(e);runtime.ReadMemStats(&after);emit(kind,"sign",rep,ns,len(sig),true,after.TotalAlloc-before.TotalAlloc,after.Mallocs-before.Mallocs,0,len(sig))
   t=qnow();ok:=verify(pk,msg,sig);vns:=qns(t);if !ok{panic("signature failed")};emit(kind,"verify",rep,vns,len(sig),ok,0,0,0,len(sig))
   if rep==0{writeVector(vector,kind,pk,msg,sig);save(vector+".negative.json",negatives(pk,msg,sig,verify))}
  }
  fmt.Println("{\"candidate\":\"kn4036\",\"all_verify\":true}");return
 }
 var seed [32]byte;copy(seed[:],unhex(f.Seed));var key *shrincs.StatefulKey;var restored *shrincs.RestoredKey
 var io state.StateIO;var timed *timedIO;var mem *memoryIO
 if scenario=="durable"{if len(a)<9{panic("state path required")};timed=&timedIO{base:filestate.New(a[8])};io=timed}else{mem=&memoryIO{};io=mem}
 if scenario=="missing"||scenario=="fallback"{restored,e=shrincs.Restore(ctx,seed)}else{key,e=shrincs.NewStatefulKey(ctx,seed,io)};must(e)
 pub:=unhex(f.PK);actual:=pub;if key!=nil{actual=key.PublicKey}else{actual=restored.PublicKey};if !bytes.Equal(actual,pub){panic("restored public key mismatch")}
 emit("shrincs-go","key_restore_and_state_init",0,qns(t),0,true,0,0,0,0)
 var snapshot []byte;if mem!=nil{snapshot=bytes.Clone(mem.data)}
 for rep:=0;rep<reps;rep++{
  if scenario=="restored"&&rep>0{mem.data=bytes.Clone(snapshot)}
  msg:=message(n,rep);var before,after runtime.MemStats;runtime.ReadMemStats(&before);q:=uint64(0);if key!=nil{q=key.Counter};t=qnow();var sig *shrincs.Sig
  if key!=nil{sig,e=key.Sign(ctx,msg)}else{sig,e=restored.Sign(ctx,msg)};must(e);wire:=shrincs.SerializeSig(sig);ns:=qns(t);runtime.ReadMemStats(&after)
  q=sig.Counter
  emit("shrincs-go","sign",rep,ns,len(wire),true,after.TotalAlloc-before.TotalAlloc,after.Mallocs-before.Mallocs,q,len(sig.Body))
  if timed!=nil{emit("shrincs-go","state_write",rep,timed.writeNS,len(wire),true,0,0,q,len(sig.Body));emit("shrincs-go","state_read",rep,timed.readNS,len(wire),true,0,0,q,len(sig.Body))}
  t=qnow();ok:=verifyShrincs(pub,msg,wire);vns:=qns(t);if !ok{panic("signature failed")};emit("shrincs-go","verify",rep,vns,len(wire),ok,0,0,q,len(sig.Body))
  if rep==0{writeVector(vector,"shrincs-go",pub,msg,wire);save(vector+".negative.json",negatives(pub,msg,wire,verifyShrincs))}
  if scenario=="restored"{writeVector(fmt.Sprintf("%s.restore_%d.json",vector,rep),"shrincs-go",pub,msg,wire)}
 }
 fmt.Println("{\"candidate\":\"shrincs-go\",\"all_verify\":true}")
}
