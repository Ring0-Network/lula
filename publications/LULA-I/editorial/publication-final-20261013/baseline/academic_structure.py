"""Reader-ordered article structure; no construction or numerical changes."""
from pathlib import Path
import hashlib,json,re

P=Path(__file__).resolve().parents[1]
E=P/'editorial/li-structure-20261012'
B=E/'baseline'
patches=[]
def once(text,old,new):
    assert text.count(old)==1,old[:100]
    patches.append({'old':old,'new':new})
    return text.replace(old,new,1)
def para(text,prefix,new):
    return once(text,next(x for x in text.splitlines() if x.startswith(prefix)),new)
def write(path,text):path.write_bytes(text.encode('utf8'))

m=(B/'LULA-I.tex').read_text(encoding='utf8')
m=once(m,'\\subsection{Contributions and scope}','\\subsection{Our contributions}')
for i in range(1,6):
    m=once(m,'\\item[\\textbf{C'+str(i)+'.}]','\\item')
m=once(m,'\\section{Related work}','\\subsection{Related work}')
m=once(m,'\\section{Preliminaries and notation}\\label{sec:notation}',r'\section{Preliminaries}\label{sec:preliminaries}'+'\n'+r'\subsection{Notation}\label{sec:notation}')
m=once(m,'\\section{Threat model and security definitions}\\label{sec:game}\n\\subsection{Atomic chosen-message rollback game}',r'\subsection{Atomic chosen-message rollback game}\label{sec:game}')
m=once(m,'\\subsection{Randomness and excluded observations}','\\subsection{Randomness and observation model}')
m=once(m,'\\section{Correctness}\\label{sec:correctness}',r'\section{Correctness and security}\label{sec:security}'+'\n'+r'\subsection{Correctness}\label{sec:correctness}')
m=once(m,'\\section{Security analysis}\\label{sec:security}\n\\subsection{Scope of the transfer argument}','\\subsection{Reference-signer security}')
m=once(m,'\\section{Rollback resilience}\\label{sec:rollback}\n\\subsection{One common signing function}',r'\subsection{Cache transparency and rollback transfer}\label{sec:rollback}')
m=once(m,'\\subsection{Why frozen-state security has no general converse}',r'\subsection{Frozen-state security and adaptive rollback}\label{sec:frozen}')
m=once(m,'and a counterexample to a general converse from frozen-state security (\\Cref{sec:rollback}).','and a counterexample to a general converse from frozen-state security (\\Cref{thm:transfer,sec:frozen}).')
m=once(m,'\\paragraph{Scope of the result.}','\\paragraph{Security consequence.}')
m=once(m,'\\section{Signature format and computational cost}\\label{sec:cost}\n\\input{operating-model}\n\\FloatBarrier',r'\section{Signature format and computational cost}\label{sec:cost}')
m=once(m,'\\section{Cache-accelerated signing}\\label{sec:cache}',r'\input{operating-model}'+'\n'+r'\FloatBarrier'+'\n\n'+r'\section{Cache-accelerated signing}\label{sec:cache}')
m=once(m,'\\subsection{Verification accounting}','\\subsection{Verification complexity}')
m=once(m,'\\section{Discussion and limitations}','\\section{Discussion}')
m=once(m,' The classical FORS+C component model and its assumptions are given in \\Cref{sec:operating}.',' The FORS+C component analysis appears in \\Cref{sec:operating}.')
m=once(m,' We make no claim to have introduced stateless signing or caching as cryptographic principles. Its unforgeability remains conditional on the reference-signer premise in \\Cref{sec:security,thm:transfer}.','')
m=once(m,' Unforgeability under restoration still depends on the reference-signer premise in \\Cref{sec:security,thm:transfer}.','')
m=once(m,' Unforgeability under restoration still requires the reference-signer premise in \\Cref{sec:security,thm:transfer}.','')
m=once(m,' The rollback unforgeability statement is conditional on an applicable bound for the common reference signer, as in \\Cref{sec:security,thm:transfer}.','')
m=para(m,'The remainder reviews related work',r'\Cref{sec:preliminaries} introduces the notation and rollback game. \Cref{sec:construction} specifies LULA I, and \Cref{sec:security} establishes correctness, cache transparency and the conditional rollback transfer. \Cref{sec:cache,sec:cost} describe the cache architecture, signature format and computational costs. Discussion and conclusions follow in \Cref{sec:limits,sec:conclusion}; \Cref{app:search} gives the asymptotic and counter-search analysis.')

outputs={n:(B/n).read_text(encoding='utf8') for n in ['LULA-I.tex','stability-results.tex','comparison-results.tex','operating-model.tex','replay-results.tex']}
outputs['LULA-I.tex']=m
outputs['stability-results.tex']=once(outputs['stability-results.tex'],
    'The two SHA2-128s verification cells at 1 KiB and 64 KiB failed the repeatability criterion:',
    'Results pool six blocks per message length, with 1,000 calls per operation in each block for LULA I and SHA2-128f and 200 for SHA2-128s; LULA I used two keys, three blocks each. The two SHA2-128s verification cells at 1 KiB and 64 KiB failed the repeatability criterion:')
outputs['LULA-I.tex']=once(outputs['LULA-I.tex'],'the noncanonical-counter control returns','the cache-corruption example returns')
outputs['LULA-I.tex']=once(outputs['LULA-I.tex'],'termination behavior and emitted evidence in the declared interface','termination behavior and returned signatures in the declared interface')
outputs['LULA-I.tex']=once(outputs['LULA-I.tex'],'\\section{Signature format and computational cost}','\\section{Signature format, computational cost, and performance}')
outputs['comparison-results.tex']=once(outputs['comparison-results.tex'],'their exact encodings have no checked security reduction','we have not established a security reduction for their exact encodings')
outputs['comparison-results.tex']=once(outputs['comparison-results.tex'],'that reference does not certify these adapters','that reference does not certify these implementations')
outputs['LULA-I.tex']=once(outputs['LULA-I.tex'],'The transfer theorem is short because deterministic transparency carries the construction-specific obligation.','In LULA I, the construction-specific condition for the transfer theorem is deterministic cache transparency.')
for name,text in outputs.items():
    write(P/name,text)
    write(P/'release/paper'/name,text.replace('\\email{angel@r-0.org}\\\\','') if name=='LULA-I.tex' else text)
for name in ['stability-results.tex','comparison-results.tex']:write(P/'scripts/editorial_templates'/name,outputs[name])
abstract=re.search(r'\\begin\{abstract\}(.*?)\\keywords',m,re.S)[1].strip().replace('--','–')
for path in [P/'SUBMISSION_METADATA.json',P/'release/paper/SUBMISSION_METADATA.json']:
    metadata=json.loads(path.read_text(encoding='utf8'));metadata['abstract']=abstract
    write(path,json.dumps(metadata,ensure_ascii=False,indent=2)+'\n')
write(E/'PATCHES.json',json.dumps(patches,ensure_ascii=False,indent=2)+'\n')
write(E/'SOURCE_HASHES.json',json.dumps({n:{'before':hashlib.sha256((B/n).read_bytes()).hexdigest(),'after':hashlib.sha256((P/n).read_bytes()).hexdigest()} for n in outputs},indent=2)+'\n')
print(json.dumps({'status':'ACADEMIC_STRUCTURE_INSTALLED','top_level_sections':re.findall(r'\\section\{([^}]+)\}',m),'patches':len(patches),'abstract_words':len(abstract.split())}))
