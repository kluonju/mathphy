# LaTeX Book Template

This directory contains a simple book template where each chapter is kept in its own file.

## Structure

- `main.tex` : the master document
- `chapters/` : one directory per chapter, named by topic:
  - `prelim` Preliminaries
  - `vec` Vector Analysis
  - `complex` Complex Analysis
  - `pde` Mathematical Physics Equations
  - `fs` Fourier Series
  - `ft` Fourier Transform and Laplace Transform
  - `cov` Calculus of Variations
  - `gf` Green's Function Method

## To compile the whole book

The notes use XeLaTeX, BibTeX, and MakeIndex:

```bash
xelatex main.tex
bibtex main
python3 scripts/build_index.py main.idx main.ind
xelatex main.tex
xelatex main.tex
```

or, more robustly:

```bash
latexmk -xelatex -bibtex main.tex
```

The local `.latexmkrc` runs XeLaTeX and builds the index with `scripts/build_index.py` (the `makeindex` binary is not required).

## To build only one chapter at a time

Edit `main.tex` and uncomment:

```tex
\includeonly{chapters/prelim/prelim}
```

You can include multiple chapter files separated by commas:

```tex
\includeonly{chapters/prelim/prelim,chapters/vec/vec}
```

This is useful when you want to work on one chapter while avoiding a full rebuild of the whole book.
