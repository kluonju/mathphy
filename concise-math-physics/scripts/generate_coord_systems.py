#!/usr/bin/env python3
"""Professional textbook-style coordinate-system schematics (TikZ + tikz-3dplot)."""
from __future__ import annotations

import subprocess
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
FIG = ROOT / "src" / "figures"
FIG.mkdir(parents=True, exist_ok=True)

PREAMBLE = r"""
\documentclass[border=16pt]{standalone}
\usepackage{amsmath,amssymb}
\usepackage{tikz}
\usepackage{tikz-3dplot}
\usetikzlibrary{arrows.meta,calc}
\tdplotsetmaincoords{70}{125}
\tikzset{
  >=Stealth,
  axis/.style={black!70, line width=0.8pt, ->},
  guide/.style={black!25, line width=0.45pt},
  coord/.style={line width=1.2pt},
}
\begin{document}
"""

POST = r"\end{document}"

CARTESIAN = r"""
\begin{tikzpicture}[tdplot_main_coords, line join=round, line cap=round]
  \def\ax{3.35}
  \def\xx{2.25}
  \def\yy{1.65}
  \def\zz{2.05}
  \coordinate (O) at (0,0,0);
  \coordinate (P) at (\xx,\yy,\zz);
  \coordinate (A) at (\xx,0,0);
  \coordinate (B) at (\xx,\yy,0);
  \coordinate (Px) at (\xx,0,\zz);
  \coordinate (Py) at (0,\yy,\zz);
  \coordinate (Pz) at (0,0,\zz);
  \coordinate (Cy) at (0,\yy,0);

  \draw[axis] (0,0,0) -- (\ax,0,0);
  \draw[axis] (0,0,0) -- (0,\ax,0);
  \draw[axis] (0,0,0) -- (0,0,\ax);

  \draw[guide] (O) -- (A) -- (B) -- (Cy) -- cycle;
  \draw[guide] (A) -- (Px) -- (P) -- (B);
  \draw[guide] (Cy) -- (Py) -- (P);
  \draw[guide] (O) -- (Pz) -- (Px);
  \draw[guide] (Pz) -- (Py);

  \draw[coord, blue!60!black] (O) -- (A);
  \draw[coord, brown!70!black] (A) -- (B);
  \draw[coord, red!60!black] (B) -- (P);

  \fill[black] (P) circle (1.5pt);

  \node[anchor=north east] at (\ax,0,0) {$x$};
  \node[anchor=north west] at (0,\ax,0) {$y$};
  \node[anchor=south] at (0,0,\ax) {$z$};
  \node[anchor=south west, xshift=5pt, yshift=3pt] at (P) {$P$};

  % explicit midpoints (calc ! is unreliable in 3d)
  \node[text=blue!60!black, anchor=north, yshift=-6pt]
    at ({0.55*\xx},0,0) {$x$};
  \node[text=brown!70!black, anchor=north, yshift=-6pt]
    at (\xx,{0.5*\yy},0) {$y$};
  \node[text=red!60!black, anchor=west, xshift=6pt]
    at (\xx,\yy,{0.55*\zz}) {$z$};
\end{tikzpicture}
"""

CYLINDRICAL = r"""
\begin{tikzpicture}[tdplot_main_coords, line join=round, line cap=round]
  \def\ax{3.35}
  \def\R{2.10}
  \def\Z{2.15}
  \def\ph{50}
  \coordinate (O) at (0,0,0);
  \coordinate (Q) at ({\R*cos(\ph)},{\R*sin(\ph)},0);
  \coordinate (P) at ({\R*cos(\ph)},{\R*sin(\ph)},\Z);
  \coordinate (H) at (0,0,\Z);

  \draw[axis] (0,0,0) -- (\ax,0,0);
  \draw[axis] (0,0,0) -- (0,\ax,0);
  \draw[axis] (0,0,0) -- (0,0,{\ax+0.1});

  \tdplotdrawarc[guide]{(O)}{\R}{-25}{205}{}{}
  \tdplotdrawarc[guide]{(H)}{\R}{-25}{205}{}{}
  \draw[guide] ({\R*cos(-10)},{\R*sin(-10)},0) -- ({\R*cos(-10)},{\R*sin(-10)},\Z);
  \draw[guide] ({\R*cos(100)},{\R*sin(100)},0) -- ({\R*cos(100)},{\R*sin(100)},\Z);

  \draw[coord, blue!60!black] (O) -- (Q);
  \draw[coord, red!60!black] (Q) -- (P);
  \draw[blue!60!black, line width=0.75pt, dashed] (H) -- (P);

  \draw[guide] (O) -- (1.25,0,0);
  \tdplotdrawarc[green!40!black, line width=1.0pt]{(O)}{1.05}{0}{\ph}{}{}

  \fill[black] (P) circle (1.5pt);

  \node[anchor=north east] at (\ax,0,0) {$x$};
  \node[anchor=north west] at (0,\ax,0) {$y$};
  \node[anchor=south] at (0,0,{\ax+0.1}) {$z$};
  \node[anchor=south west, xshift=5pt, yshift=3pt] at (P) {$P$};

  \node[text=blue!60!black, anchor=north, yshift=-7pt]
    at ({0.45*\R*cos(\ph)},{0.45*\R*sin(\ph)},0) {$\rho$};
  \node[text=green!40!black]
    at ({1.48*cos(\ph/2)},{1.48*sin(\ph/2)},0) {$\phi$};
  \node[text=red!60!black, anchor=west, xshift=6pt]
    at ({\R*cos(\ph)},{\R*sin(\ph)},{0.55*\Z}) {$z$};
\end{tikzpicture}
"""

SPHERICAL = r"""
\begin{tikzpicture}[tdplot_main_coords, line join=round, line cap=round]
  \def\ax{3.15}
  \def\R{2.50}
  \def\th{56}
  \def\ph{45}
  \coordinate (O) at (0,0,0);
  \tdplotsetcoord{P}{\R}{\th}{\ph}
  \coordinate (Q) at ({\R*sin(\th)*cos(\ph)},{\R*sin(\th)*sin(\ph)},0);

  \draw[axis] (0,0,0) -- (\ax,0,0);
  \draw[axis] (0,0,0) -- (0,\ax,0);
  \draw[axis] (0,0,0) -- (0,0,\ax);

  \tdplotdrawarc[guide]{(O)}{\R}{-20}{200}{}{}
  \tdplotsetthetaplanecoords{\ph}
  \tdplotdrawarc[tdplot_rotated_coords, guide]{(O)}{\R}{8}{172}{}{}

  \draw[coord, red!60!black] (O) -- (P);
  \draw[brown!65!black, line width=0.8pt, dashed] (O) -- (Q);
  \draw[guide] (Q) -- (P);

  \tdplotdrawarc[tdplot_rotated_coords, green!40!black, line width=1.0pt]
    {(O)}{1.15}{0}{\th}{}{}
  \draw[guide] (O) -- (1.2,0,0);
  \tdplotdrawarc[blue!55!black, line width=1.0pt]{(O)}{1.05}{0}{\ph}{}{}

  \fill[black] (P) circle (1.5pt);

  \node[anchor=north east] at (\ax,0,0) {$x$};
  \node[anchor=north west] at (0,\ax,0) {$y$};
  \node[anchor=south] at (0,0,\ax) {$z$};
  \node[anchor=west, xshift=6pt] at (P) {$P$};

  \node[text=red!60!black, anchor=east, xshift=-5pt] at (
    {0.55*\R*sin(\th)*cos(\ph)},
    {0.55*\R*sin(\th)*sin(\ph)},
    {0.55*\R*cos(\th)}
  ) {$r$};

  % theta beside the arc (not near P)
  \node[text=green!40!black, anchor=west, xshift=3pt] at (
    {1.35*sin(\th/2)*cos(\ph)},
    {1.35*sin(\th/2)*sin(\ph)},
    {1.35*cos(\th/2)}
  ) {$\theta$};

  \node[text=blue!55!black]
    at ({1.55*cos(\ph/2)},{1.55*sin(\ph/2)},0) {$\phi$};
\end{tikzpicture}
"""

THREE = r"""
\begin{tikzpicture}[line join=round, line cap=round]
  \begin{scope}[shift={(0,0)}, tdplot_main_coords]
    \def\ax{2.45}
    \coordinate (P) at (1.65,1.20,1.50);
    \coordinate (A) at (1.65,0,0);
    \coordinate (B) at (1.65,1.20,0);
    \draw[axis] (0,0,0) -- (\ax,0,0);
    \draw[axis] (0,0,0) -- (0,\ax,0);
    \draw[axis] (0,0,0) -- (0,0,\ax);
    \draw[guide] (0,0,0)--(A)--(B)--(0,1.20,0)--cycle;
    \draw[guide] (A)--(1.65,0,1.50)--(P)--(B);
    \draw[coord, blue!60!black] (0,0,0)--(A);
    \draw[coord, brown!70!black] (A)--(B);
    \draw[coord, red!60!black] (B)--(P);
    \fill (P) circle (1.3pt);
    \node[anchor=south west, xshift=3pt, yshift=2pt] at (P) {$P$};
    \node[anchor=north east] at (\ax,0,0) {$x$};
    \node[anchor=north west] at (0,\ax,0) {$y$};
    \node[anchor=south] at (0,0,\ax) {$z$};
  \end{scope}
  \node[font=\large, anchor=north] at (1.1,-2.95) {Cartesian $(x,y,z)$};

  \begin{scope}[shift={(5.7,0)}, tdplot_main_coords]
    \def\ax{2.45}
    \def\R{1.50}
    \def\Z{1.55}
    \def\ph{48}
    \coordinate (Q) at ({\R*cos(\ph)},{\R*sin(\ph)},0);
    \coordinate (P) at ({\R*cos(\ph)},{\R*sin(\ph)},\Z);
    \draw[axis] (0,0,0) -- (\ax,0,0);
    \draw[axis] (0,0,0) -- (0,\ax,0);
    \draw[axis] (0,0,0) -- (0,0,\ax);
    \tdplotdrawarc[guide]{(0,0,0)}{\R}{-20}{200}{}{}
    \tdplotdrawarc[guide]{(0,0,\Z)}{\R}{-20}{200}{}{}
    \draw[coord, blue!60!black] (0,0,0)--(Q);
    \draw[coord, red!60!black] (Q)--(P);
    \tdplotdrawarc[green!40!black, line width=0.95pt]{(0,0,0)}{0.82}{0}{\ph}{}{}
    \fill (P) circle (1.3pt);
    \node[anchor=south west, xshift=3pt, yshift=2pt] at (P) {$P$};
    \node[text=blue!60!black, anchor=north, yshift=-4pt]
      at ({0.5*\R*cos(\ph)},{0.5*\R*sin(\ph)},0) {$\rho$};
    \node[text=green!40!black] at ({1.12*cos(\ph/2)},{1.12*sin(\ph/2)},0) {$\phi$};
    \node[anchor=north east] at (\ax,0,0) {$x$};
    \node[anchor=north west] at (0,\ax,0) {$y$};
    \node[anchor=south] at (0,0,\ax) {$z$};
  \end{scope}
  \node[font=\large, anchor=north] at (6.8,-2.95) {Cylindrical $(\rho,\phi,z)$};

  \begin{scope}[shift={(11.4,0)}, tdplot_main_coords]
    \def\ax{2.35}
    \def\R{1.80}
    \def\th{54}
    \def\ph{42}
    \tdplotsetcoord{P}{\R}{\th}{\ph}
    \coordinate (Q) at ({\R*sin(\th)*cos(\ph)},{\R*sin(\th)*sin(\ph)},0);
    \draw[axis] (0,0,0) -- (\ax,0,0);
    \draw[axis] (0,0,0) -- (0,\ax,0);
    \draw[axis] (0,0,0) -- (0,0,\ax);
    \tdplotdrawarc[guide]{(0,0,0)}{\R}{-15}{195}{}{}
    \tdplotsetthetaplanecoords{\ph}
    \tdplotdrawarc[tdplot_rotated_coords, guide]{(0,0,0)}{\R}{10}{170}{}{}
    \draw[coord, red!60!black] (0,0,0)--(P);
    \draw[brown!65!black, line width=0.75pt, dashed] (0,0,0)--(Q);
    \tdplotdrawarc[tdplot_rotated_coords, green!40!black, line width=0.95pt]{(0,0,0)}{0.78}{0}{\th}{}{}
    \tdplotdrawarc[blue!55!black, line width=0.95pt]{(0,0,0)}{0.72}{0}{\ph}{}{}
    \fill (P) circle (1.3pt);
    \node[anchor=west, xshift=5pt] at (P) {$P$};
    \node[text=red!60!black, anchor=east, xshift=-4pt] at (
      {0.55*\R*sin(\th)*cos(\ph)},
      {0.55*\R*sin(\th)*sin(\ph)},
      {0.55*\R*cos(\th)}
    ) {$r$};
    \node[text=green!40!black, anchor=south, yshift=2pt] at (
      {1.05*sin(\th/2)*cos(\ph)},
      {1.05*sin(\th/2)*sin(\ph)},
      {1.05*cos(\th/2)}
    ) {$\theta$};
    \node[text=blue!55!black] at ({1.00*cos(\ph/2)},{1.00*sin(\ph/2)},0) {$\phi$};
    \node[anchor=north east] at (\ax,0,0) {$x$};
    \node[anchor=north west] at (0,\ax,0) {$y$};
    \node[anchor=south] at (0,0,\ax) {$z$};
  \end{scope}
  \node[font=\large, anchor=north] at (12.5,-2.95) {Spherical $(r,\theta,\phi)$};
\end{tikzpicture}
"""

FIGURES = {
    "coords_cartesian": CARTESIAN,
    "coords_cylindrical": CYLINDRICAL,
    "coords_spherical": SPHERICAL,
    "coords_three_systems": THREE,
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
        print(log[-3500:])
        raise SystemExit(1)
    pdf = work / f"{stem}.pdf"
    subprocess.run(
        ["pdftocairo", "-png", "-r", "220", "-singlefile", str(pdf), str(FIG / stem)],
        check=True,
        capture_output=True,
    )
    subprocess.run(
        ["pdftocairo", "-svg", str(pdf), str(FIG / stem)],
        check=True,
        capture_output=True,
    )
    bare = FIG / stem
    svg = FIG / f"{stem}.svg"
    if bare.exists() and bare.is_file():
        if svg.exists():
            bare.unlink()
        else:
            bare.rename(svg)
    print("OK", stem)


def main() -> None:
    with tempfile.TemporaryDirectory(prefix="coords_") as tmp:
        work = Path(tmp)
        for stem, body in FIGURES.items():
            compile_one(stem, body, work)
    for p in FIG.glob("_*.png"):
        p.unlink(missing_ok=True)


if __name__ == "__main__":
    main()
