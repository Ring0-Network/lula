# Build LULA I

Run pdflatex -interaction=nonstopmode -halt-on-error LULA-I.tex, bibtex LULA-I, then pdflatex twice in the publication root or release/paper/. Required packages: llncs/splncs04, CM-Super, algorithm2e, TikZ, placeins, booktabs and hyperref.

Final main/repository builds passed all four commands and produce 21 A4 pages with embedded vector fonts. No overfull boxes, unresolved references/citations or final changed-label requests remain. The source ZIP was built separately in isolation and reproduces every page's extracted text.

Current build logs and the isolated source check are in editorial/publication-final-20261013/root/. MiKTeX environment notices are not document errors. Historical article-transform scripts are not the current build entry point.
