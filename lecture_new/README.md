# LaTeX Book Template

This directory contains a simple book template where each chapter is kept in its own file.

## Structure

- `main.tex` : the master document
- `chapters/` : individual chapter files

## To compile the whole book

Run:

```bash
pdflatex main.tex
```

or, more robustly:

```bash
latexmk -pdf main.tex
```

## To build only one chapter at a time

Edit `main.tex` and uncomment:

```tex
\includeonly{chapters/ch01-introduction}
```

You can include multiple chapter files separated by commas:

```tex
\includeonly{chapters/ch01-introduction,chapters/ch02-foundations}
```

This is useful when you want to work on one chapter while avoiding a full rebuild of the whole book.
