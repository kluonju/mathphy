#!/usr/bin/env python3
"""Convert lecture .tex to Markdown, preserving Chinese prose and math."""
import re
import sys
from pathlib import Path

_SCRIPTS = Path(__file__).resolve().parent
if str(_SCRIPTS) not in sys.path:
    sys.path.insert(0, str(_SCRIPTS))
from fix_math import fix_display_math_blocks  # noqa: E402


def strip_comments(text: str) -> str:
    lines = []
    for line in text.splitlines():
        if line.strip().startswith("%"):
            continue
        # remove inline % comments not in math
        if "%" in line and "\\" not in line.split("%")[0][-3:]:
            line = line.split("%", 1)[0]
        lines.append(line)
    return "\n".join(lines)


def convert(tex: str) -> str:
    tex = strip_comments(tex)
    # remove figure/tikz/input
    tex = re.sub(r"\\input\{[^}]+\}", "", tex)
    tex = re.sub(r"\\includegraphics(\[[^\]]*\])?\{[^}]+\}", "", tex)
    tex = re.sub(
        r"\\begin\{figure\}.*?\\end\{figure\}", "", tex, flags=re.DOTALL
    )
    tex = re.sub(r"\\begin\{tikzpicture\}.*?\\end\{tikzpicture\}", "", tex, flags=re.DOTALL)
    tex = re.sub(r"\\begin\{minipage\}.*?\\end\{minipage\}", "", tex, flags=re.DOTALL)
    tex = re.sub(r"\\begin\{wrapfigure\}.*?\\end\{wrapfigure\}", "", tex, flags=re.DOTALL)
    tex = re.sub(r"\\begin\{center\}.*?\\end\{center\}", "", tex, flags=re.DOTALL)
    tex = re.sub(r"\\vspace\{[^}]*\}", "", tex)

    repl = [
        (r"\\chapter\{([^}]+)\}", r"# \1\n\n"),
        (r"\\section\{([^}]+)\}", r"## \1\n\n"),
        (r"\\subsection\{([^}]+)\}", r"### \1\n\n"),
        (r"\\subsubsection\{([^}]+)\}", r"#### \1\n\n"),
        (r"\\textbf\{([^}]+)\}", r"**\1**"),
        (r"\\textit\{([^}]+)\}", r"*\1*"),
        (r"\\emph\{([^}]+)\}", r"*\1*"),
        (r"\\label\{[^}]+\}", ""),
        (r"\\ref\{[^}]+\}", ""),
        (r"\\eqref\{[^}]+\}", ""),
        (r"\\cite\{[^}]+\}", ""),
        (r"\\imath\b", r"\\mathrm{i}"),
        (r"\\mathrm\{Re\}", r"\\operatorname{Re}"),
        (r"\\mathrm\{Im\}", r"\\operatorname{Im}"),
        (r"\\half\b", r"\\frac{1}{2}"),
        (r"\\risingdotseq", r"\\;\\Leftrightarrow\\;"),
        (r"\\fallingdotseq", r"\\;\\Leftrightarrow\\;"),
        (r"\\braket\{([^}|]+)\|([^}]+)\}", r"\\langle \1 | \2 \\rangle"),
        (r"\\dd\b", r"\\mathrm{d}"),
        (r"\\textrm\{([^}]+)\}", r"\\text{\1}"),
        (r"\\operatorname\{([^}]+)\}", r"\\operatorname{\1}"),
        (r"\\nonumber\b", ""),
        (r"\\,", " "),
        (r"\\;", " "),
        (r"\\quad", " "),
        (r"\\qquad", "  "),
    ]
    for pat, rep in repl:
        tex = re.sub(pat, rep, tex)

    # environments
    tex = re.sub(
        r"\\begin\{definition\}(\[[^\]]*\])?\s*",
        r"\n> **定义** ",
        tex,
    )
    tex = re.sub(r"\\end\{definition\}", "\n\n", tex)
    tex = re.sub(
        r"\\begin\{example\}(\[[^\]]*\])?\s*",
        r"\n\n> **例** ",
        tex,
    )
    tex = re.sub(r"\\end\{example\}", "\n\n", tex)
    tex = re.sub(
        r"\\begin\{solution\}\s*",
        r"\n\n> **解** ",
        tex,
    )
    tex = re.sub(r"\\end\{solution\}", "\n\n", tex)
    tex = re.sub(
        r"\\begin\{note\}\s*",
        r"\n\n> **注** ",
        tex,
    )
    tex = re.sub(r"\\end\{note\}", "\n\n", tex)
    tex = re.sub(
        r"\\begin\{theorem\}(\[[^\]]*\])?\s*",
        lambda m: f"\n\n> **定理**{m.group(1) or ''} ",
        tex,
    )
    tex = re.sub(r"\\end\{theorem\}", "\n\n", tex)
    tex = re.sub(
        r"\\begin\{lemma\}(\[[^\]]*\])?\s*",
        lambda m: f"\n\n> **引理**{m.group(1) or ''} ",
        tex,
    )
    tex = re.sub(r"\\end\{lemma\}", "\n\n", tex)
    tex = re.sub(
        r"\\begin\{proposition\}(\[[^\]]*\])?\s*",
        lambda m: f"\n\n> **命题**{m.group(1) or ''} ",
        tex,
    )
    tex = re.sub(r"\\end\{proposition\}", "\n\n", tex)
    tex = re.sub(
        r"\\begin\{proof\}\s*",
        r"\n\n",
        tex,
    )
    tex = re.sub(r"\\end\{proof\}", "\n\n", tex)
    tex = re.sub(
        r"\\begin\{introduction\}.*?\\end\{introduction\}",
        "",
        tex,
        flags=re.DOTALL,
    )
    tex = re.sub(r"\\begin\{itemize\}", "\n", tex)
    tex = re.sub(r"\\end\{itemize\}", "\n", tex)
    tex = re.sub(r"\\begin\{enumerate\}", "\n", tex)
    tex = re.sub(r"\\end\{enumerate\}", "\n", tex)
    tex = re.sub(r"\\item\s*", "\n- ", tex)
    # 保留 equation / align / gather 环境结构（MathJax 需要）
    tex = re.sub(
        r"\\begin\{equation\*?\}(\[[^\]]*\])?\s*(.*?)\\end\{equation\*?\}",
        lambda m: "\n\n$$" + m.group(2).strip() + "$$\n\n",
        tex,
        flags=re.DOTALL,
    )
    tex = re.sub(
        r"\\begin\{align\*?\}(\[[^\]]*\])?",
        r"\n\n$$\\begin{aligned}\n",
        tex,
    )
    tex = re.sub(r"\\end\{align\*?\}", r"\n\\end{aligned}$$\n\n", tex)
    tex = re.sub(
        r"\\begin\{gather\*?\}(\[[^\]]*\])?",
        r"\n\n$$\\begin{gathered}\n",
        tex,
    )
    tex = re.sub(r"\\end\{gather\*?\}", r"\n\\end{gathered}$$\n\n", tex)
    for env in ("eqnarray", "eqnarray*"):
        esc = env.replace("*", r"\*")
        pat = rf"\\begin\{{{esc}\}}(.*?)\\end\{{{esc}\}}"
        tex = re.sub(
            pat,
            lambda m: "\n\n$$\\begin{aligned}\n"
            + m.group(1).strip()
            + "\n\\end{aligned}$$\n\n",
            tex,
            flags=re.DOTALL,
        )
    tex = re.sub(r"\\\[(.*?)\\\]", r"$$\1$$", tex, flags=re.DOTALL)
    tex = re.sub(r"\\\((.*?)\\\)", r"$\1$", tex, flags=re.DOTALL)
    # 裸 $$ ... $$ 与 $ ... $
    tex = re.sub(
        r"(?<!\$)\$\$([\s\S]+?)\$\$(?!\$)",
        lambda m: "\n\n$$" + m.group(1).strip() + "$$\n\n",
        tex,
    )
    tex = re.sub(r"(?<!\$)\$([^$\n]+)\$(?!\$)", r"$\1$", tex)

    # cleanup
    tex = re.sub(r"\n{3,}", "\n\n", tex)
    tex = re.sub(r"[ \t]+\n", "\n", tex)
    tex = fix_display_math_blocks(tex)
    return tex.strip() + "\n"


def merge_files(paths: list[Path], title: str = "") -> str:
    parts = []
    if title:
        parts.append(f"# {title}\n")
    for p in paths:
        if p.exists():
            parts.append(convert(p.read_text(encoding="utf-8", errors="replace")))
    return "\n".join(parts)


def main():
    if len(sys.argv) < 3:
        print("Usage: tex2md.py <output.md> <tex1> [tex2 ...]")
        sys.exit(1)
    out = Path(sys.argv[1])
    paths = [Path(p) for p in sys.argv[2:]]
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(merge_files(paths), encoding="utf-8")
    print(f"Wrote {out} ({len(paths)} sources)")


if __name__ == "__main__":
    main()
