//! Dedicated measurement driver. Original lula1 library is unmodified.
//! Persistent cache is a harness fixture, not a new signature field.
use lula1::*;
use sha2::{Digest, Sha256};
use std::{fs, io::{Read, Write}, time::Instant};

fn params(which: &str, cached: bool) -> Params {
    let spec = match which {
        "lula1" => "18,9,1;5:4:0:240:0|5:4:0:240:0|5:4:0:240:0|5:4:0:240:0|21:8:0:2040:1",
        "nc" => "21,10,1;7:4:0:240:0|6:4:0:240:0|6:4:0:240:0|6:4:0:240:0|6:4:0:240:0|6:4:0:240:0",
        "mini" => "4,3,0;2:4:0:240:0|3:4:0:240:1",
        _ => panic!("unknown parameter set"),
    };
    let (f, ls) = spec.split_once(';').unwrap();
    let v: Vec<u32> = f.split(',').map(|x|x.parse().unwrap()).collect();
    let layers = ls.split('|').map(|s| {
        let a: Vec<u32> = s.split(':').map(|x|x.parse().unwrap()).collect();
        LayerP {h:a[0], lw:a[1], z:a[2], s:a[3], cached: cached && a[4]==1}
    }).collect();
    Params {name:which.into(), k:v[0], a:v[1], forsc:v[2]==1, layers}
}
fn h16(parts: &[&[u8]]) -> Node {
    let mut h=Sha256::new(); for p in parts {h.update(p);} let d=h.finalize();
    let mut out=[0u8;16]; out.copy_from_slice(&d[..16]); out
}
fn seed_a() -> [u8;48] {
    let master=[0x31u8;32]; let pk=h16(&[b"R6A-dual-pkseed", &master]);
    let mut out=[0u8;48];
    out[..16].copy_from_slice(&h16(&[b"R6A-dual-sk",b"A",&master]));
    out[16..32].copy_from_slice(&h16(&[b"R6A-dual-prf",b"A",&master]));
    out[32..].copy_from_slice(&h16(&[&pk,b"A"])); out
}
fn seed_b() -> [u8;48] {
    let master=[0x31u8;32]; let pk=h16(&[b"R6A-dual-pkseed", &master]);
    let mut out=[0u8;48];
    out[..16].copy_from_slice(&h16(&[b"R6A-dual-sk",b"B",&master]));
    out[16..32].copy_from_slice(&h16(&[b"R6A-dual-prf",b"B",&master]));
    out[32..].copy_from_slice(&h16(&[&pk,b"B"])); out
}
fn put64(f:&mut fs::File,x:u64) {f.write_all(&x.to_le_bytes()).unwrap();}
fn get64(f:&mut fs::File)->u64 {let mut a=[0;8];f.read_exact(&mut a).unwrap();u64::from_le_bytes(a)}
fn save(path:&str,s:&Signer,seed:&[u8;48]) {
    let mut f=fs::File::create(path).unwrap(); f.write_all(b"M3RAC01\0").unwrap();
    f.write_all(seed).unwrap(); f.write_all(&s.pk().1).unwrap(); put64(&mut f,s.cache.len() as u64);
    for lc in &s.cache {
        f.write_all(&[u8::from(lc.is_some())]).unwrap();
        if let Some(c)=lc {
            put64(&mut f,c.subtrees.len() as u64);
            for (st,cs) in c.subtrees.iter().zip(&c.ctrs) {
                put64(&mut f,st.h as u64); put64(&mut f,st.nodes.len() as u64);
                for n in &st.nodes {f.write_all(n).unwrap();}
                put64(&mut f,cs.len() as u64);
                for c in cs {f.write_all(&c.to_le_bytes()).unwrap();}
            }
        }
    }
    f.sync_all().unwrap();
}
fn load(path:&str,p:Params,keep:bool)->Signer {
    let bytes=fs::metadata(path).unwrap().len(); assert!(bytes < 128*1024*1024);
    let mut f=fs::File::open(path).unwrap(); let mut magic=[0;8]; f.read_exact(&mut magic).unwrap();
    assert_eq!(&magic,b"M3RAC01\0"); let mut seed=[0;48]; f.read_exact(&mut seed).unwrap();
    let mut root=[0;16]; f.read_exact(&mut root).unwrap();
    let mut ctx=Ctx::new(seed[..16].try_into().unwrap(),seed[16..32].try_into().unwrap(),seed[32..].try_into().unwrap());
    ctx.pk_root=root;
    let d=get64(&mut f) as usize; assert_eq!(d,p.layers.len()); let mut cache=Vec::new();
    if !keep {
        let wots=p.layers.iter().map(|l|WotsC::new(l.lw,l.z,l.s)).collect();
        let fors=Fors{k:p.k,a:p.a,forsc:p.forsc};
        cache=(0..d).map(|_|None).collect();
        return Signer{p,ctx,wots,fors,cache};
    }
    for lp in &p.layers {
        let mut tag=[0]; f.read_exact(&mut tag).unwrap(); assert!(tag[0]<=1);
        if tag[0]==0 {cache.push(None);continue;}
        let n=get64(&mut f) as usize; assert!(n<=1<<22); let mut subtrees=Vec::new();let mut ctrs=Vec::new();
        for _ in 0..n {
            let h=get64(&mut f) as u32; assert_eq!(h,lp.h);
            let count=get64(&mut f) as usize; assert_eq!(count,(1usize<<(h+1))-1);
            let mut nodes=vec![[0u8;16];count]; for node in &mut nodes {f.read_exact(node).unwrap();}
            let count=get64(&mut f) as usize; assert_eq!(count,1usize<<h);
            let mut cs=Vec::with_capacity(count); for _ in 0..count {let mut a=[0;4];f.read_exact(&mut a).unwrap();cs.push(u32::from_le_bytes(a));}
            if keep {subtrees.push(Subtree{h,nodes});ctrs.push(cs);}
        }
        cache.push(if keep {Some(LayerCache{subtrees,ctrs})} else {None});
    }
    let mut end=[0]; assert_eq!(f.read(&mut end).unwrap(),0);
    let wots=p.layers.iter().map(|l|WotsC::new(l.lw,l.z,l.s)).collect();
    let fors=Fors{k:p.k,a:p.a,forsc:p.forsc}; Signer{p,ctx,wots,fors,cache}
}
fn message(n:usize,rep:usize)->Vec<u8> {
    let mut m:Vec<u8>=(0..n).map(|i| ((i*131+rep*17+19)&255) as u8).collect();
    m[..8].copy_from_slice(&(rep as u64).to_le_bytes());m
}
fn hex(b:&[u8])->String {b.iter().map(|x|format!("{:02x}",x)).collect()}
fn join(seed:&Node,a:&Node,b:&Node)->Node {
    let mut x=[0u8;32];x[..16].copy_from_slice(a);x[16..].copy_from_slice(b);
    Ctx::public(*seed,[0;16]).th(&Adrs::new(0,0,8),&x)
}
fn check(which:&str,s:&Signer,pks:&Node,pkr:&Node,_other:Option<&Node>,_tag:u8,m:&[u8],sig:&[u8])->bool {
    if which!="dual" {return verify(&s.p,pks,pkr,m,sig);}
    if sig.len()<17 || sig[0]>1 {return false;}
    let tag=sig[0];let p=params(if tag==0 {"lula1"} else {"nc"},false);
    if sig.len()!=p.sig_bytes()+17 {return false;}
    let sibling:Node=sig[1..17].try_into().unwrap();
    let seed=h16(&[pks,if tag==0 {b"A"} else {b"B"}]);
    match verify_root(&p,&seed,pkr,m,&sig[17..]) {
        None=>false,
        Some(root)=> if tag==0 {join(pks,&root,&sibling)==*pkr} else {join(pks,&sibling,&root)==*pkr},
    }
}
fn main() {
    let a:Vec<String>=std::env::args().collect();
    let op=&a[1]; let which=&a[2]; let fixture=&a[3];
    if op=="prepare" {
        let seed=if which=="nc" {seed_b()} else {seed_a()};
        let p=params(which,true); let(s,r)=Signer::keygen(p,&seed,1);
        let t=Instant::now();save(fixture,&s,&seed);let write_ns=t.elapsed().as_nanos();
        println!("{{\"operation\":\"keygen_and_cache_preparation\",\"candidate\":\"{}\",\"secs\":{},\"hash_calls\":{},\"cache_bytes\":{},\"fixture_bytes\":{},\"persist_ns\":{},\"seed_hex\":\"{}\",\"pk_hex\":\"{}{}\"}}",which,r.secs,r.calls,r.cache_bytes,fs::metadata(fixture).unwrap().len(),write_ns,hex(&seed),hex(&s.pk().0),hex(&s.pk().1));return;
    }
    let scenario=&a[4]; let n:usize=a[5].parse().unwrap(); let reps:usize=a[6].parse().unwrap();
    let output=&a[7]; let vector=&a[8]; let start=Instant::now();
    // Missing-cache loads the seed/root but no cache values into the signer;
    // disk cache parsing is recorded as preparation, not hidden inside signing.
    let mut s;
    let pks;let pkr;let sibling;let tag;
    if which=="dual" {
        let bfixture=&a[9];
        let mut sa=load(fixture,params("lula1",true),scenario!="missing");
        let mut sb=load(bfixture,params("nc",false),false);
        let ar=sa.pk().1;let br=sb.pk().1;
        pks=h16(&[b"R6A-dual-pkseed",&[0x31u8;32]]);pkr=join(&pks,&ar,&br);
        sa.bind_digest_to(pkr);sb.bind_digest_to(pkr);
        tag=u8::from(scenario=="missing");
        sibling=Some(if tag==0 {br} else {ar});s=if tag==0 {sa} else {sb};
    } else {
        s=load(fixture,params(which,true),scenario!="missing");
        (pks,pkr)=s.pk();sibling=None;tag=0;
    }
    let prep_ns=start.elapsed().as_nanos();
    let mut f=fs::File::create(output).unwrap();
    writeln!(f,"candidate,scenario,message_bytes,rep,operation,ns,hash_calls,sig_bytes,pk_bytes,valid").unwrap();
    writeln!(f,"{},{},{},0,fixture_load,{},0,0,32,true",which,scenario,n,prep_ns).unwrap();
    for rep in 0..reps {
        let m=message(n,rep);reset_calls();let t=Instant::now();let inner=s.sign(&m,true);
        let sig=if let Some(other)=sibling {let mut out=vec![tag];out.extend_from_slice(&other);out.extend_from_slice(&inner);out} else {inner};
        let sign_ns=t.elapsed().as_nanos();let sign_calls=calls();reset_calls();let t=Instant::now();
        let ok=check(which,&s,&pks,&pkr,sibling.as_ref(),tag,&m,&sig);let verify_ns=t.elapsed().as_nanos();let vc=calls();assert!(ok);
        writeln!(f,"{},{},{},{},sign,{},{},{},32,{}",which,scenario,n,rep,sign_ns,sign_calls,sig.len(),ok).unwrap();
        writeln!(f,"{},{},{},{},verify,{},{},{},32,{}",which,scenario,n,rep,verify_ns,vc,sig.len(),ok).unwrap();
        f.flush().unwrap();
        if rep==0 {
            fs::write(vector,format!("pk_seed {}\npk_root {}\nmsg {}\nsig {}\n",hex(&pks),hex(&pkr),hex(&m),hex(&sig))).unwrap();
            for pos in [0,16,sig.len()/2,sig.len()-1] {let mut bad=sig.clone();bad[pos]^=1;assert!(!check(which,&s,&pks,&pkr,sibling.as_ref(),tag,&m,&bad));}
            assert!(!check(which,&s,&pks,&pkr,sibling.as_ref(),tag,&m,&sig[..sig.len()-1]));
            let mut extra=sig.clone();extra.push(0);assert!(!check(which,&s,&pks,&pkr,sibling.as_ref(),tag,&m,&extra));
            let mut badpk=pkr;badpk[0]^=1;assert!(!check(which,&s,&pks,&badpk,sibling.as_ref(),tag,&m,&sig));
            let mut badm=m.clone();badm[8]^=1;assert!(!check(which,&s,&pks,&pkr,sibling.as_ref(),tag,&badm,&sig));
        }
    }
    println!("{{\"candidate\":\"{}\",\"scenario\":\"{}\",\"message_bytes\":{},\"repetitions\":{},\"all_verify\":true,\"negative_tests\":\"PASS\"}}",which,scenario,n,reps);
}
