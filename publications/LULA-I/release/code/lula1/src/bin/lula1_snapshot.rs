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
    // Campaign addition: "snap <fixture> <start_rep> <count> <msg_bytes> <out.txt>": sign messages start..start+count-1 with a
    // signer loaded from the cache file, verify each, write "rep hex(sig)" lines. The signer holds no mutable state.
    let a:Vec<String>=std::env::args().collect();
    let fixture=&a[2]; let start:usize=a[3].parse().unwrap(); let count:usize=a[4].parse().unwrap();
    let n:usize=a[5].parse().unwrap(); let output=&a[6];
    let t=Instant::now(); let s=load(fixture,params("lula1",true),true); let (pks,pkr)=s.pk(); let load_ns=t.elapsed().as_nanos();
    let mut f=fs::File::create(output).unwrap();
    writeln!(f,"# load_ns {}",load_ns).unwrap();
    for rep in start..start+count {
        let m=message(n,rep);
        let t=Instant::now(); let sig=s.sign(&m,true); let ns=t.elapsed().as_nanos();
        let ok=verify(&s.p,&pks,&pkr,&m,&sig); assert!(ok);
        writeln!(f,"{} {} {} {}",rep,ns,sig.len(),hex(&sig)).unwrap();
    }
    println!("{{\"snap\":true,\"count\":{},\"all_verify\":true}}",count);
}
