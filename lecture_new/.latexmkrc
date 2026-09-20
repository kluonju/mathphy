# XeLaTeX is required (ctex / Unicode). This directory's indexer
# replaces makeindex, which is not installed on this machine.
$pdf_mode = 5;
$xelatex = 'xelatex -synctex=1 -interaction=nonstopmode -file-line-error %O %S';
$makeindex = 'python3 scripts/build_index.py %S %D';
