#!/usr/bin/env python3
"""Professional textbook-style vector-analysis figures (TikZ + pdflatex).

Matches the visual language of generate_coord_systems.py.
"""
from __future__ import annotations

import subprocess
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
FIG = ROOT / "src" / "figures"
FIG.mkdir(parents=True, exist_ok=True)

PREAMBLE = r"""
\documentclass[border=14pt]{standalone}
\usepackage{amsmath,amssymb}
\usepackage{tikz}
\usepackage{tikz-3dplot}
\usetikzlibrary{arrows.meta,calc,decorations.markings,patterns,angles,quotes}
\tdplotsetmaincoords{70}{120}
\tikzset{
  >=Stealth,
  axis/.style={black!65, line width=0.75pt, ->},
  guide/.style={black!22, line width=0.45pt},
  vecA/.style={blue!62!black, line width=1.35pt, ->},
  vecB/.style={red!62!black, line width=1.35pt, ->},
  vecS/.style={green!42!black, line width=1.55pt, ->},
  soft/.style={black!35, line width=0.55pt},
  panel/.style={font=\small\sffamily},
}
\begin{document}
"""

POST = r"\end{document}"

# ---------------------------------------------------------------------------
# 2D figures
# ---------------------------------------------------------------------------

SUM_DIFF = r"""
\begin{tikzpicture}[line join=round, line cap=round]
  % (a) parallelogram
  \begin{scope}
    \coordinate (O) at (0,0);
    \coordinate (A) at (3.1,0.55);
    \coordinate (B) at (0.95,2.35);
    \coordinate (S) at ($(A)+(B)$);
    \draw[soft] (A) -- (S) -- (B);
    \draw[vecA] (O) -- (A);
    \draw[vecB] (O) -- (B);
    \draw[vecS] (O) -- (S);
    \node[text=blue!62!black, below] at ($(O)!0.55!(A)$) {$\mathbf{A}$};
    \node[text=red!62!black, left] at ($(O)!0.55!(B)$) {$\mathbf{B}$};
    \node[text=green!42!black, above right=-2pt] at ($(O)!0.62!(S)$) {$\mathbf{A}+\mathbf{B}$};
    \node[panel, anchor=north] at (2.0,-0.55) {(a) parallelogram sum};
  \end{scope}

  % (b) head-to-tail difference
  \begin{scope}[shift={(6.6,0)}]
    \coordinate (O) at (0,0);
    \coordinate (A) at (3.1,0.55);
    \coordinate (B) at (0.95,2.35);
    \draw[vecA] (O) -- (A);
    \draw[vecB] (O) -- (B);
    \draw[vecS] (A) -- (B);
    \node[text=blue!62!black, below] at ($(O)!0.55!(A)$) {$\mathbf{A}$};
    \node[text=red!62!black, left] at ($(O)!0.55!(B)$) {$\mathbf{B}$};
    \node[text=green!42!black, right] at ($(A)!0.55!(B)$) {$\mathbf{B}-\mathbf{A}$};
    \node[panel, anchor=north] at (1.8,-0.55) {(b) head-to-tail difference};
  \end{scope}
\end{tikzpicture}
"""

DOT = r"""
\begin{tikzpicture}[line join=round, line cap=round]
  \coordinate (O) at (0,0);
  \coordinate (A) at (4.2,0.55);
  \coordinate (B) at (2.35,2.85);
  % projection of B onto A
  \pgfmathsetmacro{\AdotB}{2.35*4.2 + 2.85*0.55}
  \pgfmathsetmacro{\Anormsq}{4.2*4.2 + 0.55*0.55}
  \coordinate (P) at ({4.2*\AdotB/\Anormsq},{0.55*\AdotB/\Anormsq});
  \draw[soft, densely dashed] (B) -- (P);
  \draw[green!42!black, line width=2.0pt] (O) -- (P);
  \fill[green!42!black] (P) circle (1.6pt);
  % right angle
  \coordinate (Ra) at ($(P)!0.18!(O)$);
  \coordinate (Rb) at ($(P)!0.18!(B)$);
  \coordinate (Rc) at ($(Ra)+(Rb)-(P)$);
  \draw[soft] (Ra) -- (Rc) -- (Rb);
  \draw[vecA] (O) -- (A);
  \draw[vecB] (O) -- (B);
  \pic[draw=black!50, angle radius=0.55cm, pic text={$\theta$},
       angle eccentricity=1.45] {angle = A--O--B};
  \node[text=blue!62!black, below] at ($(O)!0.72!(A)$) {$\mathbf{A}$};
  \node[text=red!62!black, above left] at ($(O)!0.62!(B)$) {$\mathbf{B}$};
  \node[text=green!42!black, below=6pt] at ($(O)!0.5!(P)$) {$|\mathbf{B}|\cos\theta$};
\end{tikzpicture}
"""

CROSS = r"""
\begin{tikzpicture}[tdplot_main_coords, line join=round, line cap=round]
  \coordinate (O) at (0,0,0);
  \coordinate (A) at (2.6,0.35,0);
  \coordinate (B) at (0.75,2.2,0);
  \coordinate (C) at (0,0,1.85);
  \coordinate (S) at ($(A)+(B)$);
  \fill[blue!55!black, opacity=0.12] (O) -- (A) -- (S) -- (B) -- cycle;
  \draw[guide] (A) -- (S) -- (B);
  \draw[vecA] (O) -- (A);
  \draw[vecB] (O) -- (B);
  \draw[vecS] (O) -- (C);
  \node[text=blue!62!black, anchor=north] at (A) {$\mathbf{A}$};
  \node[text=red!62!black, anchor=west] at (B) {$\mathbf{B}$};
  \node[text=green!42!black, anchor=west] at (C) {$\mathbf{A}\times\mathbf{B}$};
\end{tikzpicture}
"""

LINE_INT = r"""
\begin{tikzpicture}[line join=round, line cap=round]
  \draw[blue!62!black, line width=1.45pt,
        postaction={decorate, decoration={
          markings,
          mark=at position 0.18 with {
            \draw[black!48, line width=0.95pt, ->] (-0.20,0) -- (0.40,0);
            \draw[red!62!black, line width=1.2pt, ->] (0,0) -- (0.06,0.62);
          },
          mark=at position 0.40 with {
            \draw[black!48, line width=0.95pt, ->] (-0.20,0) -- (0.40,0);
            \draw[red!62!black, line width=1.2pt, ->] (0,0) -- (0.08,0.58);
          },
          mark=at position 0.62 with {
            \draw[black!48, line width=0.95pt, ->] (-0.20,0) -- (0.40,0);
            \draw[red!62!black, line width=1.2pt, ->] (0,0) -- (0.10,0.55);
          },
          mark=at position 0.82 with {
            \draw[black!48, line width=0.95pt, ->] (-0.20,0) -- (0.40,0);
            \draw[red!62!black, line width=1.2pt, ->] (0,0) -- (0.12,0.50);
          }
        }}]
    plot[smooth, tension=0.65] coordinates {
      (0.15,0.50) (1.05,1.05) (2.05,0.70) (3.15,1.45) (4.20,2.05) (5.20,2.60)
    };
  \fill[green!42!black] (0.15,0.50) circle (2.1pt);
  \fill[green!42!black] (5.20,2.60) circle (2.1pt);
  \node[panel, text=green!42!black, below left] at (0.15,0.50) {start};
  \node[panel, text=green!42!black, above] at (5.20,2.60) {end};
  \node[text=red!62!black] at (2.45,2.25) {$\mathbf{F}$};
  \node[text=black!50] at (3.85,1.15) {$d\boldsymbol{\ell}$};
\end{tikzpicture}
"""

FLUX_SRC = r"""
\begin{tikzpicture}[line join=round, line cap=round]
  \foreach \sx/\lab in {0/source (net out $>0$), 4.6/sink (net out $<0$), 9.2/no source (net $=0$)}{
    \begin{scope}[shift={(\sx,0)}]
      \draw[blue!62!black, line width=1.1pt] (0,0) circle (1.15);
      \node[panel, anchor=north] at (0,-1.55) {\lab};
    \end{scope}
  }
  % source
  \foreach \a in {0,45,...,315}{
    \draw[red!62!black, line width=1.05pt, ->]
      ({0.35*cos(\a)},{0.35*sin(\a)}) -- ({1.55*cos(\a)},{1.55*sin(\a)});
  }
  \fill[red!62!black] (0,0) circle (2.2pt);
  \node[panel, text=red!62!black, below=3pt] at (0,0) {src};
  % sink
  \begin{scope}[shift={(4.6,0)}]
    \foreach \a in {0,45,...,315}{
      \draw[red!62!black, line width=1.05pt, ->]
        ({1.55*cos(\a)},{1.55*sin(\a)}) -- ({0.35*cos(\a)},{0.35*sin(\a)});
    }
    \fill[red!62!black] (0,0) circle (2.2pt);
    \node[panel, text=red!62!black, below=3pt] at (0,0) {sink};
  \end{scope}
  % through-flow
  \begin{scope}[shift={(9.2,0)}]
    \foreach \y in {-0.55,0,0.55}{
      \draw[red!62!black, line width=1.05pt, ->] (-1.7,\y) -- (1.7,\y);
    }
  \end{scope}
\end{tikzpicture}
"""

DIV_CANCEL = r"""
\begin{tikzpicture}[line join=round, line cap=round]
  \foreach \i in {0,1,2,3}{
    \foreach \j in {0,1,2}{
      \fill[blue!55!black, opacity=0.07] (\i,\j) rectangle ++(1,1);
      \draw[blue!62!black, line width=0.7pt] (\i,\j) rectangle ++(1,1);
    }
  }
  % cancel marks on interior vertical edges
  \foreach \i in {1,2,3}{
    \foreach \j in {0,1,2}{
      \draw[red!62!black, line width=0.85pt, ->]
        ({\i-0.28},{\j+0.5}) -- ({\i-0.05},{\j+0.5});
      \draw[red!62!black, line width=0.85pt, ->]
        ({\i+0.28},{\j+0.5}) -- ({\i+0.05},{\j+0.5});
    }
  }
  \draw[green!42!black, line width=2.2pt] (0,0) rectangle (4,3);
  \node[panel, text=red!62!black] at (2,3.35) {interior faces cancel};
  \node[panel, text=green!42!black] at (2,-0.45) {outer surface $S$ (survives)};
\end{tikzpicture}
"""

CURL_LOOP = r"""
\begin{tikzpicture}[line join=round, line cap=round]
  % (a)
  \begin{scope}
    \coordinate (BL) at (0,0);
    \coordinate (BR) at (2.8,0);
    \coordinate (TR) at (2.8,1.9);
    \coordinate (TL) at (0,1.9);
    \draw[blue!62!black, line width=1.15pt] (BL) rectangle (TR);
    \draw[red!62!black, line width=1.15pt, ->] (0.25,0) -- (2.55,0);
    \draw[red!62!black, line width=1.15pt, ->] (2.8,0.25) -- (2.8,1.65);
    \draw[red!62!black, line width=1.15pt, ->] (2.55,1.9) -- (0.25,1.9);
    \draw[red!62!black, line width=1.15pt, ->] (0,1.65) -- (0,0.25);
    \node[panel, black!55] at (1.4,-0.35) {$A_x(y)$};
    \node[panel, black!55, rotate=90] at (3.25,0.95) {$A_y(x+\Delta x)$};
    \node[panel, black!55, anchor=north east] at (0,-0.08) {$(x,y)$};
    \node[panel, anchor=north] at (1.4,-0.85) {(a) infinitesimal circulation};
  \end{scope}
  % (b)
  \begin{scope}[shift={(5.4,0.15)}]
    \draw[blue!62!black, line width=1.15pt] (0,0) circle (1.15);
    \foreach \a in {20,80,140,200,260,320}{
      \draw[red!62!black, line width=1.05pt, ->]
        ({1.15*cos(\a-12)},{1.15*sin(\a-12)}) --
        ({1.15*cos(\a+12)},{1.15*sin(\a+12)});
    }
    \draw[green!42!black, line width=1.3pt] (0,0) circle (0.22);
    \fill[green!42!black] (0,0) circle (2.2pt);
    \node[text=green!42!black, right] at (0.35,0.25) {$\hat{\mathbf{n}}$};
    \node[panel, anchor=north] at (0,-1.55) {(b) right-hand normal};
  \end{scope}
\end{tikzpicture}
"""

CURL_PADDLE = r"""
\begin{tikzpicture}[line join=round, line cap=round]
  % (a) uniform
  \begin{scope}
    \foreach \y in {0.3,0.9,1.5,2.1,2.7}{
      \draw[blue!62!black, line width=1.05pt, ->] (0.15,\y) -- (3.0,\y);
    }
    \draw[red!62!black, line width=2.0pt] (1.55,0.85) -- (1.55,2.15);
    \draw[red!62!black, line width=2.0pt] (0.9,1.5) -- (2.2,1.5);
    \fill[red!62!black] (1.55,1.5) circle (2.4pt);
    \node[panel, anchor=north] at (1.55,-0.25) {(a) $\nabla\times\mathbf{v}=\mathbf{0}$};
  \end{scope}
  % (b) vortex
  \begin{scope}[shift={(4.6,0)}]
    \foreach \r in {0.55,0.95,1.35}{
      \draw[blue!55!black, opacity=0.35, line width=0.9pt] (1.55,1.5) circle (\r);
      \foreach \a in {30,120,210,300}{
        \draw[blue!62!black, line width=1.05pt, ->]
          ({1.55+\r*cos(\a-14)},{1.5+\r*sin(\a-14)}) --
          ({1.55+\r*cos(\a+14)},{1.5+\r*sin(\a+14)});
      }
    }
    \draw[red!62!black, line width=2.0pt] (1.55,0.85) -- (1.55,2.15);
    \draw[red!62!black, line width=2.0pt] (0.9,1.5) -- (2.2,1.5);
    \fill[red!62!black] (1.55,1.5) circle (2.4pt);
    \draw[green!42!black, line width=1.4pt, ->]
      ({1.55+1.15*cos(25)},{1.5+1.15*sin(25)}) arc (25:105:1.15);
    \node[panel, anchor=north] at (1.55,-0.25) {(b) nonzero curl};
  \end{scope}
\end{tikzpicture}
"""

STOKES = r"""
\begin{tikzpicture}[line join=round, line cap=round]
  \def\L{(0.05,2.25) (1.45,2.75) (2.65,2.40) (3.05,1.15) (2.35,-0.15)
         (0.75,-0.30) (-0.45,0.55) (-0.65,1.55)}
  \draw[green!42!black, line width=2.05pt,
        postaction={decorate, decoration={
          markings,
          mark=at position 0.08 with {\arrow{Stealth}},
          mark=at position 0.28 with {\arrow{Stealth}},
          mark=at position 0.48 with {\arrow{Stealth}},
          mark=at position 0.68 with {\arrow{Stealth}},
          mark=at position 0.88 with {\arrow{Stealth}}
        }}]
    plot[smooth cycle, tension=0.85] coordinates {\L};
  \foreach \i in {0,1,2}{
    \foreach \j in {0,1,2}{
      \pgfmathsetmacro{\cx}{-0.10+\i*0.85}
      \pgfmathsetmacro{\cy}{0.40+\j*0.85}
      \fill[blue!55!black, opacity=0.08] (\cx,\cy) rectangle ++(0.70,0.70);
      \draw[blue!62!black, line width=0.65pt] (\cx,\cy) rectangle ++(0.70,0.70);
    }
  }
  \draw[red!62!black, line width=1.05pt, ->] (0.80,1.25) -- (1.40,1.25);
  \draw[red!62!black, line width=1.05pt, ->] (1.45,1.30) -- (1.45,1.90);
  \draw[red!62!black, line width=1.05pt, ->] (1.40,1.95) -- (0.80,1.95);
  \draw[red!62!black, line width=1.05pt, ->] (0.75,1.90) -- (0.75,1.30);
  \node[panel, text=red!62!black] at (1.15,3.10) {interior edges cancel};
  \node[panel, text=green!42!black] at (1.15,-0.85) {boundary $L$ (survives)};
\end{tikzpicture}
"""

# ---------------------------------------------------------------------------
# 3D figures
# ---------------------------------------------------------------------------

FLUX_DS = r"""
\begin{tikzpicture}[tdplot_main_coords, line join=round, line cap=round]
  \def\ax{2.6}
  \draw[axis] (0,0,0) -- (\ax,0,0) node[anchor=north east] {$x$};
  \draw[axis] (0,0,0) -- (0,\ax,0) node[anchor=north west] {$y$};
  \draw[axis] (0,0,0) -- (0,0,\ax) node[anchor=south] {$z$};
  % patch in plane of constant x
  \coordinate (C) at (1.35,0.95,0.95);
  \fill[blue!55!black, opacity=0.18]
    (1.35,0.25,0.35) -- (1.35,1.65,0.35) -- (1.35,1.65,1.55) -- (1.35,0.25,1.55) -- cycle;
  \draw[blue!62!black, line width=0.8pt]
    (1.35,0.25,0.35) -- (1.35,1.65,0.35) -- (1.35,1.65,1.55) -- (1.35,0.25,1.55) -- cycle;
  \draw[vecS] (C) -- ++(1.05,0,0);
  \draw[vecB] (C) -- ++(0.75,0.55,0.45);
  \node[text=green!42!black, anchor=west] at (2.5,0.95,0.95)
    {$d\mathbf{S}=\hat{\mathbf{n}}\,dS$};
  \node[text=red!62!black, anchor=south west] at (2.15,1.5,1.4) {$\mathbf{A}$};
\end{tikzpicture}
"""

DIV_BOX = r"""
\begin{tikzpicture}[tdplot_main_coords, line join=round, line cap=round]
  \def\ax{2.85}
  \def\a{1.85}
  \def\b{1.45}
  \def\c{1.25}
  \draw[axis] (-0.35,0,0) -- (\ax,0,0) node[anchor=north east] {$x$};
  \draw[axis] (0,-0.25,0) -- (0,\ax,0) node[anchor=north west] {$y$};
  \draw[axis] (0,0,-0.2) -- (0,0,\ax) node[anchor=south] {$z$};
  % subtle faces (back / bottom / left first)
  \fill[blue!55!black, opacity=0.06] (0,0,0) -- (0,\b,0) -- (0,\b,\c) -- (0,0,\c) -- cycle;
  \fill[blue!55!black, opacity=0.05] (0,0,0) -- (\a,0,0) -- (\a,\b,0) -- (0,\b,0) -- cycle;
  \fill[blue!55!black, opacity=0.04] (0,0,0) -- (\a,0,0) -- (\a,0,\c) -- (0,0,\c) -- cycle;
  \draw[black!55, line width=0.75pt]
    (0,0,0) -- (\a,0,0) -- (\a,\b,0) -- (0,\b,0) -- cycle
    (0,0,\c) -- (\a,0,\c) -- (\a,\b,\c) -- (0,\b,\c) -- cycle
    (0,0,0) -- (0,0,\c)  (\a,0,0) -- (\a,0,\c)
    (\a,\b,0) -- (\a,\b,\c)  (0,\b,0) -- (0,\b,\c);
  % outward normals (flux convention)
  \draw[vecB] (\a,{0.5*\b},{0.5*\c}) -- ++(0.72,0,0);
  \draw[vecA] (0,{0.5*\b},{0.5*\c}) -- ++(-0.72,0,0);
  \draw[vecB] ({0.5*\a},\b,{0.5*\c}) -- ++(0,0.58,0);
  \draw[vecA] ({0.5*\a},0,{0.5*\c}) -- ++(0,-0.58,0);
  \draw[vecB] ({0.5*\a},{0.5*\b},\c) -- ++(0,0,0.58);
  \draw[vecA] ({0.5*\a},{0.5*\b},0) -- ++(0,0,-0.58);
  \node[text=red!62!black, anchor=west] at ({\a+0.78},{0.5*\b},{0.5*\c})
    {$A_x(x+\Delta x)$};
  \node[text=blue!62!black, anchor=east] at (-0.78,{0.5*\b},{0.5*\c})
    {$A_x(x)$};
\end{tikzpicture}
"""

FIGURES = {
    "vec_sum_diff": SUM_DIFF,
    "vec_dot_product": DOT,
    "vec_cross_product": CROSS,
    "vec_line_integral": LINE_INT,
    "vec_flux_source_sink": FLUX_SRC,
    "vec_flux_ds": FLUX_DS,
    "vec_div_box": DIV_BOX,
    "vec_div_cancel": DIV_CANCEL,
    "vec_curl_loop": CURL_LOOP,
    "vec_curl_paddle": CURL_PADDLE,
    "vec_stokes_cancel": STOKES,
}


def compile_one(stem: str, body: str, work: Path) -> None:
    tex = work / f"{stem}.tex"
    tex.write_text(PREAMBLE + body + POST, encoding="utf-8")
    r = subprocess.run(
        ["pdflatex", "-interaction=nonstopmode", "-halt-on-error", tex.name],
        cwd=work,
        capture_output=True,
        text=True,
    )
    if r.returncode != 0:
        log = (work / f"{stem}.log").read_text(encoding="utf-8", errors="replace")
        print("FAIL", stem)
        print(log[-4000:])
        raise SystemExit(1)
    pdf = work / f"{stem}.pdf"
    subprocess.run(
        ["pdftocairo", "-png", "-r", "220", "-singlefile", str(pdf), str(FIG / stem)],
        check=True,
        capture_output=True,
    )
    print("OK", stem)


def main() -> None:
    with tempfile.TemporaryDirectory(prefix="vecfig_") as tmp:
        work = Path(tmp)
        for stem, body in FIGURES.items():
            compile_one(stem, body, work)


if __name__ == "__main__":
    main()
