# Build LULA I

Run pdflatex -interaction=nonstopmode -halt-on-error LULA-I.tex, bibtex LULA-I and pdflatex twice in the publication root or release/paper/. Current builds produce 21 pages using the unchanged A4/LNCS preamble. Dependencies include llncs/splncs04, CM-Super, algorithm2e, TikZ, placeins, booktabs and hyperref.

Current logs and package checks are in editorial/li-structure-20261012/. Document-level unresolved references and overfull boxes are absent. MiKTeX duplicate font-map notices and its update reminder are environment notices. Execution instructions remain outside the article.
