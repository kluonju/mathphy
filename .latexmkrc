# Default engine for this repo (Chinese / ctex documents need XeLaTeX).
$pdf_mode = 5;  # 5 = xelatex
$xelatex = 'xelatex -synctex=1 -interaction=nonstopmode -file-line-error %O %S';
