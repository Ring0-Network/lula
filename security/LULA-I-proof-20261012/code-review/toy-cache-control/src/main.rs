use lula1::*;

fn main() {
    // Actual production WOTS widths, chain counts and target sums; two height-one
    // trees and small FORS only. This is not a LULA I parameter-set security test.
    let p = Params {name:"cache-control-only".into(), k:2, a:1, forsc:true,
        layers:vec![LayerP{h:1,lw:4,z:0,s:240,cached:false},
                    LayerP{h:1,lw:8,z:0,s:2040,cached:true}]};
    let (mut s, _) = Signer::keygen(p.clone(), &[0x31;48], 1);
    let m = b"independent cache control";
    let pk = s.pk();
    let good = s.sign(m, true);
    let uncached = s.sign(m, false);
    assert_eq!(good, uncached);
    assert!(verify(&p, &pk.0, &pk.1, m, &good));
    let r: Node = good[..16].try_into().unwrap();
    let fc = u32::from_be_bytes(good[16..20].try_into().unwrap());
    let d = s.ctx.hmsg_outer(&s.ctx.hmsg_inner(&r,m),fc);
    let idx = get_bits(&d, (p.k*p.a) as usize, p.htotal() as usize);
    let leaf = ((idx>>1)&1) as u32;
    let w0 = &s.wots[0];
    let child = Subtree::build(&s.ctx, Adrs::new(0,leaf as u64,T_TREE),
        (0..2).map(|kp|w0.pk(&s.ctx,0,leaf as u64,kp)).collect()).root();
    let w = &s.wots[1];
    let canonical = s.cache[1].as_ref().unwrap().ctrs[0][leaf as usize];
    let canonical_dg = w.digits(&w.digest(&s.ctx,1,0,leaf,&child,canonical));
    let alternate = ((canonical+1)..(canonical+1_000_000)).find(|&c| {
        let dg=w.digits(&w.digest(&s.ctx,1,0,leaf,&child,c));
        w.accept(&dg) && dg != canonical_dg
    }).expect("small alternate-counter search exhausted");
    s.cache[1].as_mut().unwrap().ctrs[0][leaf as usize] = alternate;
    let different = s.sign(m,true);
    assert_ne!(different,good);
    assert!(verify(&p,&pk.0,&pk.1,m,&different));
    println!("accepted_noncanonical_counter: canonical={canonical}, alternate={alternate}, different_bytes=true, verify=true");
    let invalid = (0..1_000_000).find(|&c|!w.accept(&w.digits(&w.digest(&s.ctx,1,0,leaf,&child,c)))).unwrap();
    s.cache[1].as_mut().unwrap().ctrs[0][leaf as usize] = invalid;
    assert_eq!(s.sign(m,true),good);
    println!("rejected_counter: recomputes_canonical=true");
    s.cache[1].as_mut().unwrap().ctrs[0][leaf as usize] = canonical;
    let sibling = (leaf^1) as usize;
    s.cache[1].as_mut().unwrap().subtrees[0].nodes[sibling][0] ^= 1;
    let bad_path=s.sign(m,true);
    assert_ne!(bad_path,good);
    assert!(!verify(&p,&pk.0,&pk.1,m,&bad_path));
    println!("corrupt_authentication_node: signer_returns=true, verify=false");
    s.cache[1].as_mut().unwrap().subtrees[0].nodes[sibling][0] ^= 1;
    s.cache[1].as_mut().unwrap().subtrees[0].nodes[2][0] ^= 1;
    assert_eq!(s.sign(m,true),good);
    println!("corrupt_unused_top_root: signature_unchanged=true");
    println!("honest_cache: equals_uncached=true; all_controls=PASS");
}
