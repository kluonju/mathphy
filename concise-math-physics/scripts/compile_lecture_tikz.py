#!/usr/bin/env python3
"""Compile lecture TikZ figures to SVG for the mdBook."""
from __future__ import annotations

import shutil
import subprocess
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
REPO = ROOT.parent
FIG = ROOT / "src" / "figures"
FIG.mkdir(parents=True, exist_ok=True)

LECTURE = REPO / "lecture"

# (output stem, absolute path to .tex fragment or body)
FIGURES: list[tuple[str, Path]] = [
    ("tikz_complex_plane", LECTURE / "complex/tikz/complex_plane.tex"),
    ("tikz_zaddition", LECTURE / "complex/tikz/zaddition.tex"),
    ("tikz_zminus", LECTURE / "complex/tikz/zminus.tex"),
    ("tikz_rotate", LECTURE / "complex/tikz/rotate.tex"),
    ("tikz_region", LECTURE / "complex/tikz/region.tex"),
    ("tikz_annular", LECTURE / "complex/tikz/annular.tex"),
    ("tikz_limits", LECTURE / "complex/tikz/limits.tex"),
    ("tikz_orthogo", LECTURE / "complex/tikz/orthogo.tex"),
    ("tikz_branchcut", LECTURE / "complex/tikz/branchcut.tex"),
    ("tikz_complex_region", LECTURE / "complex/tikz/complex_region.tex"),
    ("tikz_integral", LECTURE / "complex/tikz/integral.tex"),
    ("tikz_ex", LECTURE / "complex/tikz/ex.tex"),
    ("tikz_semicircle", LECTURE / "complex/tikz/semicircle.tex"),
    ("tikz_cubic_equation", LECTURE / "numerical/tikz/cubic_equation.tex"),
]

# Extra bodies written next to this script's temp work (not in lecture/)
EXTRA_BODIES: dict[str, str] = {
    "tikz_path_compare": r"""
\begin{tikzpicture}[>=stealth,scale=1.0]
    \draw[->,thick] (-0.2,0) -- (3.2,0) node[right] {$x$};
    \draw[->,thick] (0,-0.2) -- (0,2.2) node[above] {$y$};
    \node[left] at (0,0) {$O$};
    \coordinate (A) at (2,1.6);
    \coordinate (B) at (2,0);
    \draw[thick] (0,0) -- (A) node[midway,above left] {$(1)$};
    \draw[thick,green!60!black] (0,0) -- (B) node[midway,below] {$(2)$}
        -- (A) node[midway,right] {$(2)$};
    \filldraw (A) circle (1.5pt) node[above right] {$A=(2,i)$};
    \filldraw (B) circle (1.5pt) node[below right] {$B=(2,0)$};
\end{tikzpicture}
""",
    "tikz_coord_systems": r"""
\begin{tikzpicture}[scale=1]
	\draw[->] (0,0) -- (2,0) node[right] {$x$};
	\draw[->] (0,0) -- (0,2) node[above] {$y$};
	\draw[->] (0,0) -- (-0.8,-0.8) node[below left] {$z$};
	\node at (1.0,1.0) {直角坐标};
\end{tikzpicture}
\hspace{1.2cm}
\begin{tikzpicture}[scale=0.9]
	\draw[->] (0,0) -- (1.8,0) node[right] {$r$};
	\draw (0,0) circle (1.2);
	\draw[->] (0.8,0) arc (0:40:0.8) node[midway, right] {$\phi$};
	\node at (0.5,-1.5) {柱坐标平面};
\end{tikzpicture}
\hspace{1.2cm}
\begin{tikzpicture}[scale=0.9]
	\draw[->] (0,0) -- (1.6,0) node[right] {$r\sin\theta\cos\phi$};
	\draw (0,0) -- (0.6,1.4) node[above right] {$\theta$};
	\draw (0,0) -- (-0.7,0.9) node[left] {$\phi$};
	\node at (0.3,-1.3) {球坐标示意};
\end{tikzpicture}
""",
}

PREAMBLE = r"""
\documentclass[border=12pt]{standalone}
\usepackage{ctex}
\usepackage{amsmath,amssymb}
\usepackage{tikz}
\usepackage{pgfplots}
\pgfplotsset{compat=1.18}
\usetikzlibrary{arrows.meta,angles,quotes,calc,patterns}
\begin{document}
"""

POSTAMBLE = r"""
\end{document}
"""


def compile_one(stem: str, body: str, work: Path) -> Path | None:
    tex_path = work / f"{stem}.tex"
    tex_path.write_text(PREAMBLE + body + POSTAMBLE, encoding="utf-8")
    try:
        subprocess.run(
            [
                "xelatex",
                "-interaction=nonstopmode",
                "-halt-on-error",
                tex_path.name,
            ],
            cwd=work,
            check=True,
            capture_output=True,
            text=True,
        )
    except subprocess.CalledProcessError as exc:
        log = work / f"{stem}.log"
        print(f"FAIL {stem}")
        if log.exists():
            print(log.read_text(encoding="utf-8", errors="replace")[-2500:])
        else:
            print(exc.stderr[-2000:] if exc.stderr else exc)
        return None

    pdf = work / f"{stem}.pdf"
    out_svg = FIG / f"{stem}.svg"
    out_png = FIG / f"{stem}.png"
    # pdftocairo writes <prefix>.svg when given a prefix path
    subprocess.run(
        ["pdftocairo", "-svg", str(pdf), str(FIG / stem)],
        check=True,
        capture_output=True,
    )
    produced_svg = FIG / f"{stem}.svg"
    bare = FIG / stem
    if bare.exists() and not bare.is_dir() and not produced_svg.exists():
        bare.rename(produced_svg)
    elif bare.exists() and bare.is_file() and produced_svg.exists():
        bare.unlink()
    subprocess.run(
        ["pdftocairo", "-png", "-r", "160", "-singlefile", str(pdf), str(FIG / stem)],
        check=True,
        capture_output=True,
    )
    png1 = FIG / f"{stem}-1.png"
    if png1.exists():
        png1.replace(out_png)
    print("OK", out_svg.name if out_svg.exists() else "MISSING_SVG", out_png.name if out_png.exists() else "")
    return out_svg if out_svg.exists() else None


def main() -> None:
    with tempfile.TemporaryDirectory(prefix="tikzfig_") as tmp:
        work = Path(tmp)
        for stem, src in FIGURES:
            body = src.read_text(encoding="utf-8")
            compile_one(stem, body, work)
        for stem, body in EXTRA_BODIES.items():
            compile_one(stem, body, work)

    # Copy existing lecture raster figures used by calculus of variations
    var_dir = LECTURE / "calculus_variation"
    for name in ("fastest_track.png", "roadside.png", "cobweb.png"):
        src = var_dir / name
        if src.exists():
            dst = FIG / f"lecture_{name}"
            shutil.copy2(src, dst)
            print("Copied", dst.name)


if __name__ == "__main__":
    main()
