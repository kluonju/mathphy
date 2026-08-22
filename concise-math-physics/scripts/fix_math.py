#!/usr/bin/env python3
"""Post-process Markdown: fix LaTeX display math for MathJax/mdBook."""
import re
import sys
from pathlib import Path

SKIP_WRAP = (
    "aligned",
    "align",
    "alignat",
    "gather",
    "gathered",
    "multline",
    "split",
    "cases",
    "array",
    "matrix",
    "pmatrix",
    "bmatrix",
    "vmatrix",
    "Bmatrix",
    "equation",
)


def has_tex_env(content: str) -> bool:
    return bool(re.search(r"\\begin\{(" + "|".join(SKIP_WRAP) + r")\*?\}", content))


def _content_lines(s: str) -> list[str]:
    return [ln.strip() for ln in s.splitlines() if ln.strip()]


def fix_inner(content: str) -> str:
    s = content.strip()
    s = re.sub(r"\\\s*$", "", s)
    s = re.sub(
        r"\\braket\{\s*([^}|]+?)\s*\|\s*([^}]+?)\s*\}",
        r"\\langle \1 \\mid \2 \\rangle",
        s,
    )
    if re.match(r"^[\u4e00-\u9fff]", s) and "\\text{" not in s:
        s = re.sub(r"^([\u4e00-\u9fff]+)", r"\\text{\1}", s)
    s = re.sub(r"\\text\s*\{\s*for\s*\}", r"\\text{for}", s)
    s = re.sub(r"\n{3,}", "\n", s)

    if has_tex_env(s):
        return s

    lines = _content_lines(s)
    has_amp = "&" in s
    has_bs = bool(re.search(r"\\\\", s))
    multi = len(lines) > 1

    if (has_amp or has_bs) and (multi or has_bs):
        if not has_tex_env(s):
            s = "\\begin{aligned}\n" + s + "\n\\end{aligned}"
    return s


def collapse_trivial_aligned(text: str) -> str:
    """Single-line aligned without & -> plain $$."""

    def repl(m: re.Match) -> str:
        inner = m.group(1).strip()
        lines = _content_lines(inner)
        if len(lines) == 1 and "&" not in lines[0] and "\\\\" not in lines[0]:
            return "$$\n" + lines[0] + "\n$$"
        if len(lines) == 2 and not has_amp_bs(inner):
            return "$$\n" + " \\\\\n".join(lines) + "\n$$"
        return m.group(0)

    def has_amp_bs(s: str) -> bool:
        return "&" in s or "\\\\" in s

    pat = re.compile(
        r"\$\$\s*\n\\begin\{aligned\}\s*\n(.*?)\n\\end\{aligned\}\s*\n\$\$",
        re.DOTALL,
    )
    return pat.sub(repl, text)


def fix_display_math_blocks(text: str) -> str:
    out = []
    i = 0
    lines = text.splitlines(keepends=True)
    n = len(lines)

    while i < n:
        line = lines[i]
        if line.strip() == "$$":
            block = []
            i += 1
            while i < n and lines[i].strip() != "$$":
                block.append(lines[i])
                i += 1
            if i < n and lines[i].strip() == "$$":
                i += 1
            inner = fix_inner("".join(block))
            out.append("$$\n")
            out.append(inner)
            if not inner.endswith("\n"):
                out.append("\n")
            out.append("$$\n")
            continue
        out.append(line)
        i += 1
    return "".join(out)


def strip_latex_indent(text: str) -> str:
    lines = []
    for line in text.splitlines():
        if re.match(r"^ {4}\S", line):
            line = line[4:]
        lines.append(line)
    return "\n".join(lines) + ("\n" if text.endswith("\n") else "")


def sanitize_math_blocks(text: str) -> str:
    """Close $$ only when blockquote/list clearly breaks math."""
    out = []
    in_math = False
    lines = text.splitlines()
    for idx, line in enumerate(lines):
        s = line.strip()
        if s == "$$":
            in_math = not in_math
            out.append(line)
            continue
        if in_math and s.startswith("> **"):
            in_math = False
            out.append("$$")
            out.append(line)
            continue
        if in_math and s.startswith("#"):
            in_math = False
            out.append("$$")
            out.append(line)
            continue
        out.append(line)
    return "\n".join(out) + "\n"


def fix_prose_in_display_math(text: str) -> str:
    def repl(m: re.Match) -> str:
        inner = m.group(1).strip()
        if "$" not in inner or "\\text{" not in inner:
            return m.group(0)
        inner = re.sub(r"\\text\{([^}]+)\}", r"\1", inner)
        inner = re.sub(r",\s*\$", "：$", inner)
        return "\n\n" + inner + "\n\n"

    return re.sub(r"\$\$\n([^\$]+?)\$\$", repl, text)


def remove_stray_env_lines(text: str) -> str:
    """Delete orphan \\end{aligned} lines outside $$ blocks."""
    out = []
    in_math = False
    for line in text.splitlines():
        s = line.strip()
        if s == "$$":
            in_math = not in_math
            out.append(line)
            continue
        if not in_math and s == r"\end{aligned}":
            continue
        out.append(line)
    return "\n".join(out) + "\n"


def strip_latex_layout(text: str) -> str:
    text = re.sub(r"\\vspace\{[^}]*\}", "", text)
    text = re.sub(
        r"\\begin\{proof\}.*?\\end\{proof\}",
        "",
        text,
        flags=re.DOTALL,
    )
    text = re.sub(r"\\begin\{proof\}", "", text)
    text = re.sub(r"\\end\{proof\}", "", text)
    for env in (
        "minipage",
        "wrapfigure",
        "figure",
        "center",
        "table",
        "tabular",
    ):
        text = re.sub(
            rf"\\begin\{{{env}\}}.*?\\end\{{{env}\}}",
            "",
            text,
            flags=re.DOTALL,
        )
        text = re.sub(rf"\\begin\{{{env}\}}[^}}]*\}}", "", text)
        text = re.sub(rf"\\end\{{{env}\}}", "", text)
    text = re.sub(r"\{\\bf\s+([^}]+)\}", r"**\1**", text)
    text = re.sub(r"\{\\textit\{([^}]+)\}\}", r"*\1*", text)
    return text


def normalize_display_delimiters(text: str) -> str:
    """Put $$ on its own lines so mdBook/MathJax recognize display math."""
    text = re.sub(r"\$\$\s*(\\begin\{)", r"$$\n\1", text)
    text = re.sub(r"\$\$\s*(\\left)", r"$$\n\1", text)
    text = re.sub(r"\$\$\s*(\\int)", r"$$\n\1", text)
    text = re.sub(r"(\\end\{[^}]+\})\s*\$\$", r"\1\n$$", text)
    text = re.sub(
        r"(\\end\{array\})\s*\n\s*(\\right\.?)\s*\n\s*\$\$",
        r"\1\n\2\n$$",
        text,
    )
    text = re.sub(r"(\\right\.?)\s*\$\$\s*$", r"\1\n$$", text, flags=re.MULTILINE)
    return text


def split_same_line_display_math(text: str) -> str:
    """Lines like $$\\frac{...}$$ or $$\\int...\\n...$$ -> $$ on own lines."""
    lines = text.splitlines()
    out: list[str] = []
    in_partial = False
    for line in lines:
        raw = line
        s = line.strip()
        if in_partial:
            if s.endswith("$$"):
                inner = line.rstrip()
                if inner.rstrip().endswith("$$"):
                    inner = inner.rstrip()[:-2].rstrip()
                if inner:
                    out.append(inner)
                out.append("$$")
                in_partial = False
            else:
                out.append(raw)
            continue
        if s.startswith("$$") and s != "$$":
            if s.endswith("$$") and len(s) > 4:
                inner = s[2:-2].strip()
                out.append("$$")
                out.append(inner)
                out.append("$$")
            else:
                out.append("$$")
                out.append(s[2:].strip())
                in_partial = True
            continue
        if s.endswith("$$") and not s.startswith("$$"):
            inner = line.rstrip()[:-2].rstrip()
            if inner:
                out.append(inner)
            out.append("$$")
            continue
        out.append(raw)
    if in_partial:
        out.append("$$")
    return "\n".join(out) + "\n"


def remove_empty_display_pairs(text: str) -> str:
    """Remove truly empty $$ blocks; keep adjacent $$ that close/open env blocks."""
    lines = text.splitlines()
    out: list[str] = []
    i = 0
    while i < len(lines):
        if lines[i].strip() == "$$" and i + 1 < len(lines) and lines[i + 1].strip() == "$$":
            j = i + 2
            while j < len(lines) and not lines[j].strip():
                j += 1
            nxt = lines[j].strip() if j < len(lines) else ""
            if nxt.startswith("\\begin{") or nxt.startswith("\\end{"):
                out.append("$$")
                out.append("$$")
                i += 2
                continue
            i += 1
            continue
        out.append(lines[i])
        i += 1
    return "\n".join(out) + "\n"


def merge_split_inline_math(text: str) -> str:
    """Join lines that continue an unclosed $...$ inline math span."""
    lines = text.splitlines()
    out: list[str] = []
    for line in lines:
        if out and out[-1].count("$") % 2 == 1:
            prev = out[-1]
            if not line.strip().startswith("$$") and "$$" not in line.strip():
                out[-1] = prev.rstrip() + " " + line.strip()
                continue
        out.append(line)
    return "\n".join(out) + "\n"


def wrap_orphan_cases_blocks(text: str) -> str:
    return wrap_orphan_env_block(text, r"\begin{cases}", r"\end{cases}")


def merge_continuation_lines(text: str) -> str:
    """Merge lines starting with = that continue a previous math expression."""
    lines = text.splitlines()
    out: list[str] = []
    for line in lines:
        s = line.strip()
        if out and s.startswith("=") and "\\frac" in s and not s.startswith("$$"):
            out[-1] = out[-1] + " " + s
        else:
            out.append(line)
    return "\n".join(out) + "\n"


def wrap_eqnarray_blocks(text: str) -> str:
    for env in ("eqnarray", "eqnarray*"):
        esc = env.replace("*", r"\*")
        pat = rf"\\begin\{{{esc}\}}(.*?)\\end\{{{esc}\}}"
        while re.search(pat, text, flags=re.DOTALL):
            text = re.sub(
                pat,
                lambda m: "$$\n\\begin{aligned}\n"
                + m.group(1).strip()
                + "\n\\end{aligned}\n$$",
                text,
                count=1,
                flags=re.DOTALL,
            )
    return text


def wrap_orphan_env_block(text: str, begin: str, end: str) -> str:
    lines = text.splitlines()
    out: list[str] = []
    i = 0
    in_display = False
    while i < len(lines):
        s = lines[i].strip()
        if s == "$$":
            in_display = not in_display
            out.append(lines[i])
            i += 1
            continue
        if not in_display and s.startswith(begin):
            block = [lines[i]]
            i += 1
            while i < len(lines) and not lines[i].strip().startswith(end):
                block.append(lines[i])
                i += 1
            if i < len(lines):
                block.append(lines[i])
                i += 1
            out.append("$$")
            out.extend(block)
            out.append("$$")
            continue
        out.append(lines[i])
        i += 1
    return "\n".join(out) + "\n"


def wrap_orphan_aligned_blocks(text: str) -> str:
    for begin, end in (
        (r"\begin{aligned}", r"\end{aligned}"),
        (r"\begin{align}", r"\end{align}"),
        (r"\begin{align*}", r"\end{align*}"),
        (r"\begin{gathered}", r"\end{gathered}"),
    ):
        text = wrap_orphan_env_block(text, begin, end)
    return text


def fix_minus_as_list_in_aligned(text: str) -> str:
    """Lines in $$ blocks starting with '- ' are mistaken for Markdown lists."""
    lines = text.splitlines()
    out: list[str] = []
    in_display = False
    for line in lines:
        if line.strip() == "$$":
            in_display = not in_display
            out.append(line)
            continue
        if in_display and re.match(r"^(\s*)-\s+\\", line):
            line = re.sub(r"^(\s*)-\s+", r"\1{}- ", line, count=1)
        out.append(line)
    return "\n".join(out) + "\n"


def fix_inline_artifacts(text: str) -> str:
    text = text.replace("\\half", r"$\frac{1}{2}$")
    for end in ("aligned", "gathered", "cases", "array"):
        text = text.replace(f"\\end{{{end}}}$$", f"\\end{{{end}}}\n$$")
    return text


def wrap_bare_env_on_line(text: str, env: str) -> str:
    """Wrap \\begin{env}...\\end{env} when line starts with \\left or \\begin."""
    esc = env.replace("*", r"\*")
    pat = rf"(\\begin\{{{esc}\}}.*?\\end\{{{esc}\}})"
    lines = text.splitlines()
    out: list[str] = []
    in_display = False
    i = 0
    while i < len(lines):
        s = lines[i].strip()
        if s == "$$":
            in_display = not in_display
            out.append(lines[i])
            i += 1
            continue
        if not in_display and re.search(pat, s, flags=re.DOTALL):
            m = re.search(pat, s, flags=re.DOTALL)
            if m and m.group(0) == s:
                out.append("$$")
                out.append(m.group(0))
                out.append("$$")
                i += 1
                continue
        if not in_display and s.startswith(r"\left\{") and "\\begin{array}" in s:
            block = [lines[i]]
            i += 1
            while i < len(lines) and "\\end{array}" not in lines[i]:
                block.append(lines[i])
                i += 1
            if i < len(lines):
                block.append(lines[i])
                i += 1
            out.append("$$")
            out.extend(block)
            out.append("$$")
            continue
        out.append(lines[i])
        i += 1
    return "\n".join(out) + "\n"


def merge_orphan_math_after_close(text: str) -> str:
    """$$\\n eq $$\\n latex_line $$ -> merge latex into previous block."""
    lines = text.splitlines()
    out: list[str] = []
    i = 0
    while i < len(lines):
        s = lines[i].strip()
        if (
            s == "$$"
            and out
            and out[-1].strip() == "$$"
            and i + 1 < len(lines)
            and lines[i + 1].strip() != "$$"
        ):
            nxt = lines[i + 1].strip()
            if (
                nxt
                and not nxt.startswith(("-", ">", "#"))
                and re.search(r"\\[a-zA-Z]", nxt)
            ):
                out.pop()  # remove closing $$
                out.append(lines[i + 1].rstrip() + " \\\\")
                i += 2
                if i < len(lines) and lines[i].strip() == "$$":
                    out.append("$$")
                    i += 1
                continue
        out.append(lines[i])
        i += 1
    return "\n".join(out) + "\n"


def move_text_out_of_display(text: str) -> str:
    """\\text{...} on its own between $$ pairs -> prose paragraph."""
    lines = text.splitlines()
    out: list[str] = []
    i = 0
    while i < len(lines):
        s = lines[i].strip()
        if (
            s.startswith(r"\text{")
            and i > 0
            and out
            and out[-1].strip() == "$$"
        ):
            m = re.match(r"\\text\{([^}]*)\}", s)
            prose = m.group(1) if m else s
            if i + 1 < len(lines) and lines[i + 1].strip() == "$$":
                i += 2
                out.append(prose)
                continue
        out.append(lines[i])
        i += 1
    return "\n".join(out) + "\n"


def unwrap_standalone_text_lines(text: str) -> str:
    """Convert lone \\text{...} lines to Markdown prose."""
    out: list[str] = []
    for line in text.splitlines():
        s = line.strip()
        m = re.fullmatch(r"\\text\{([^}]*)\}\s*\.?", s)
        if m and not re.search(r"\\[a-zA-Z]", m.group(1)):
            out.append(m.group(1))
            continue
        out.append(line)
    return "\n".join(out) + "\n"


def wrap_left_brace_env_blocks(text: str) -> str:
    """Wrap \\left\\{...\\end{array}...\\right. blocks not already in $$."""
    lines = text.splitlines()
    out: list[str] = []
    i = 0
    in_display = False
    while i < len(lines):
        s = lines[i].strip()
        if s == "$$":
            in_display = not in_display
            out.append(lines[i])
            i += 1
            continue
        if not in_display and s.startswith(r"\left\{") and (
            r"\begin{array}" in s or r"\begin{aligned}" in s
        ):
            block = [lines[i]]
            i += 1
            while i < len(lines):
                if lines[i].strip() == "$$" and len(block) > 1:
                    break
                block.append(lines[i])
                if r"\right." in lines[i] or r"\right\}" in lines[i]:
                    i += 1
                    break
                i += 1
            out.append("$$")
            out.extend(block)
            out.append("$$")
            continue
        out.append(lines[i])
        i += 1
    return "\n".join(out) + "\n"


def sanitize_code_fences(text: str) -> str:
    """Remove spurious $$ lines inside fenced code blocks."""

    def repl(m: re.Match) -> str:
        lang = m.group(1) or ""
        body = m.group(2)
        lines = [ln for ln in body.splitlines() if ln.strip() != "$$"]
        cleaned = "\n".join(lines)
        if cleaned and not cleaned.endswith("\n"):
            cleaned += "\n"
        return f"```{lang}\n{cleaned}```"

    return re.sub(r"```([^\n]*)\n(.*?)```", repl, text, flags=re.DOTALL)


BOLD_MACROS: dict[str, str] = {
    "brpppp": r"\mathbf{r}^{\prime\prime\prime\prime}",
    "brppp": r"\mathbf{r}^{\prime\prime\prime}",
    "brpp": r"\mathbf{r}^{\prime\prime}",
    "brp": r"\mathbf{r}^{\prime}",
    "bzp": r"\mathbf{z}^{\prime}",
    "bxp": r"\mathbf{x}^{\prime}",
    "tbr": r"\tilde{\mathbf{r}}",
    "mbf": r"\mathbf{f}",
    "br": r"\mathbf{r}",
    "bv": r"\mathbf{v}",
    "bz": r"\mathbf{z}",
    "bx": r"\mathbf{x}",
    "bk": r"\mathbf{k}",
    "bp": r"\mathbf{p}",
    "bq": r"\mathbf{q}",
    "bR": r"\mathbf{R}",
    "bM": r"\mathbf{M}",
    "bP": r"\mathbf{P}",
    "bT": r"\mathbf{T}",
    "bK": r"\mathbf{K}",
    "bA": r"\mathbf{A}",
    "bB": r"\mathbf{B}",
    "bD": r"\mathbf{D}",
    "bE": r"\mathbf{E}",
    "bF": r"\mathbf{F}",
    "bG": r"\mathbf{G}",
    "bH": r"\mathbf{H}",
    "bI": r"\mathbf{I}",
    "bJ": r"\mathbf{J}",
    "bS": r"\mathbf{S}",
    "bV": r"\mathbf{V}",
    "bX": r"\mathbf{X}",
    "bY": r"\mathbf{Y}",
}


def expand_bold_macros(text: str) -> str:
    for name in sorted(BOLD_MACROS, key=len, reverse=True):
        repl = BOLD_MACROS[name]

        def _sub(_: re.Match, r: str = repl) -> str:
            return r

        text = re.sub(
            rf"\\{re.escape(name)}(?![A-Za-z])",
            _sub,
            text,
        )
    text = re.sub(r"\\vec\{\\mathbf\{([a-zA-Z])\}\}", r"\\mathbf{\1}", text)
    return text


def fix_texorpdfstring(text: str) -> str:
    """Convert LaTeX \\texorpdfstring{$math$}{fallback} to inline math."""

    single = re.compile(r"\\texorpdfstring\{\$([^$]+)\$\}\{([^}]*)\}")
    while single.search(text):
        text = single.sub(r"$\1$", text)

    multi = re.compile(
        r"\\texorpdfstring\{\$([^$]+)\$\s*\n?\{([^}]*)\}([^}\n]*)",
        re.MULTILINE,
    )

    def repl(m: re.Match) -> str:
        math = m.group(1).strip()
        prefix = m.group(2).strip()
        suffix = m.group(3).strip()
        if suffix.endswith("}"):
            suffix = suffix[:-1]
        if prefix.replace(" ", "") == f"({math})" or prefix == math:
            return f"${math}$"
        rest = re.sub(r"^[A-Za-z]+", "", prefix)
        if rest:
            return f"${math}${rest}{suffix}"
        return f"${math}${suffix}"

    while multi.search(text):
        text = multi.sub(repl, text)
    return text


def fix_latex_quotes(text: str) -> str:
    """Replace LaTeX `` / '' quotes that break Markdown inline code parsing."""
    text = text.replace("''", '"')
    text = text.replace("``", '"')
    return text


def fix_latex_section_commands(text: str) -> str:
    text = re.sub(r"\\subsection\*\{([^}]*)\}", r"### \1", text)
    text = re.sub(r"\\section\*\{([^}]*)\}", r"## \1", text)
    return text


def repair_damaged_inline_math(text: str) -> str:
    """Fix inline math where a stray-brace pass removed closing } from \\mathbb / \\mathrm."""
    text = re.sub(r"\\mathbb\{([A-Z])\$", r"\\mathbb{\1}$", text)
    text = re.sub(r"\\mathbb\{([A-Z])\)\$", r"\\mathbb{\1}$)", text)
    text = re.sub(
        r"\\mathbb\{([A-Z])\)(?=[,，。；;])",
        r"\\mathbb{\1}$",
        text,
    )
    text = re.sub(
        r"\\mathbb\{([A-Z])\)(?=[）)）])",
        r"\\mathbb{\1}$)",
        text,
    )
    text = re.sub(r"\\mathrm\{i\$", r"\\mathrm{i}$", text)
    text = re.sub(r"\{ f\(x\) \| x \\in A \$", r"{ f(x) | x \\in A } $", text)
    text = re.sub(r"z\^{-1 =", r"z^{-1} =", text)
    text = re.sub(r"\\mathbb\{([A-Z]) (?=[^}])", r"\\mathbb{\1} ", text)
    text = re.sub(r"\\mathrm\{i ([^$]+)\$", r"\\mathrm{i} \1$", text)
    for _ in range(6):
        new = re.sub(
            r"\\mathrm\{i ((?:[^{}]|\\[a-zA-Z]+)+)\}",
            r"\\mathrm{i} \1}",
            text,
        )
        if new == text:
            break
        text = new
    text = re.sub(r"\\mathrm\{i([a-zA-Z0-9(])", r"\\mathrm{i} \1", text)
    text = re.sub(r"\\sqrt\{p=", r"\\sqrt{p}=", text)
    text = re.sub(r"-\\mathrm\{i ", r"-\\mathrm{i} ", text)
    return text


def fix_inline_math_spans(text: str) -> str:
    """Repair common inline-math artifacts."""
    text = re.sub(
        r"\$\{\s*(\\mathbb\{[A-Z]\}\s*)\}\$",
        r"$\1$",
        text,
    )
    return text


def fix_prose_texorpdfstring(text: str) -> str:
    text = fix_texorpdfstring(text)
    text = fix_latex_quotes(text)
    text = fix_latex_section_commands(text)
    return text


def collapse_blank_lines_in_display_math(text: str) -> str:
    """Remove blank lines inside $$ ... $$ blocks (they break mdBook rendering)."""

    def repl(m: re.Match) -> str:
        body = m.group(1)
        lines = [ln for ln in body.splitlines() if ln.strip()]
        if not lines:
            return "$$\n$$"
        return "$$\n" + "\n".join(lines) + "\n$$"

    return re.sub(r"\$\$\n(.*?)\n\$\$", repl, text, flags=re.DOTALL)


def _trailing_backslashes(line: str) -> int:
    stripped = line.rstrip()
    count = 0
    for ch in reversed(stripped):
        if ch == "\\":
            count += 1
        else:
            break
    return count


def convert_to_mdbook_math_delimiters(text: str) -> str:
    """mdBook only typesets \\(...\\) and \\[...\\], not $...$ / $$...$$."""

    def disp_repl(m: re.Match) -> str:
        body = m.group(1).strip("\n")
        return "\\\\[\n" + body + "\n\\\\]"

    text = re.sub(r"\$\$\n(.*?)\n\$\$", disp_repl, text, flags=re.DOTALL)

    def inline_repl(m: re.Match) -> str:
        body = m.group(1)
        return "\\\\(" + body + "\\\\)"

    text = re.sub(r"(?<!\$)\$([^$\n]+)\$(?!\$)", inline_repl, text)
    return text


def fix_display_math_line_breaks(text: str) -> str:
    """Double trailing \\ in display math so mdBook passes \\\\ to MathJax."""

    def repl(m: re.Match) -> str:
        body = m.group(1)
        out: list[str] = []
        for ln in body.splitlines():
            stripped = ln.rstrip()
            suffix = ln[len(stripped) :]
            n = _trailing_backslashes(ln)
            if 0 < n < 4:
                ln = stripped + "\\" * (4 - n) + suffix
            out.append(ln)
        return "$$\n" + "\n".join(out) + "\n$$"

    return re.sub(r"\$\$\n(.*?)\n\$\$", repl, text, flags=re.DOTALL)


def expand_lecture_macros(text: str) -> str:
    """Replace lecture-only TeX macros with MathJax-safe forms."""
    for _ in range(8):
        new = re.sub(
            r"\\funcpd\s*\{([^{}]*)\}\{([^{}]*)\}",
            r"\\frac{\\partial \1}{\\partial \2}",
            text,
        )
        if new == text:
            break
        text = new
    text = re.sub(
        r"\\funcd\s*\{([^{}]*)\}\{([^{}]*)\}",
        r"\\frac{\\mathrm{d} \1}{\\mathrm{d} \2}",
        text,
    )
    text = re.sub(
        r"\\fnald\s*\{([^{}]*)\}\{([^{}]*)\}",
        r"\\frac{\\delta \1}{\\delta \2}",
        text,
    )
    text = re.sub(r"\\operatorname\{\\Res\}", r"\\operatorname{Res}", text)
    text = re.sub(r"\\Res(?![A-Za-z])", r"\\operatorname{Res}", text)
    text = re.sub(r"(?<![A-Za-z])\\dd(?![A-Za-z])", r"\\mathrm{d}", text)
    text = re.sub(r"\\half(?![A-Za-z])", r"\\frac{1}{2}", text)
    text = re.sub(r"\\oiint(?![A-Za-z])", r"\\oint\\!\\!\\!\\!\\!\\iint", text)
    text = replace_braket(text)
    text = expand_bold_macros(text)
    return text


def replace_braket(text: str) -> str:
    needle = r"\braket{"
    out: list[str] = []
    i = 0
    while i < len(text):
        if text.startswith(needle, i):
            i += len(needle)
            depth = 1
            start = i
            while i < len(text) and depth:
                ch = text[i]
                if ch == "{":
                    depth += 1
                elif ch == "}":
                    depth -= 1
                i += 1
            out.append(r"\langle " + text[start : i - 1] + r" \rangle")
        else:
            out.append(text[i])
            i += 1
    return "".join(out)


def fix_eqnarray_ampersands(text: str) -> str:
    text = text.replace("&=&", "&=")
    text = re.sub(r"&\s*=\s*&", "&=", text)
    return text


def process_text(text: str) -> str:
    pipeline = sanitize_code_fences(text)
    pipeline = fix_prose_texorpdfstring(pipeline)
    pipeline = repair_damaged_inline_math(pipeline)
    pipeline = expand_lecture_macros(pipeline)
    pipeline = fix_eqnarray_ampersands(pipeline)
    pipeline = strip_latex_indent(pipeline)
    pipeline = strip_latex_layout(pipeline)
    pipeline = merge_split_inline_math(pipeline)
    pipeline = merge_continuation_lines(pipeline)
    pipeline = split_same_line_display_math(pipeline)
    pipeline = wrap_eqnarray_blocks(pipeline)
    pipeline = normalize_display_delimiters(pipeline)
    pipeline = split_same_line_display_math(pipeline)
    pipeline = wrap_orphan_cases_blocks(pipeline)
    pipeline = wrap_orphan_aligned_blocks(pipeline)
    pipeline = wrap_bare_env_on_line(pipeline, "cases")
    pipeline = remove_stray_env_lines(pipeline)
    pipeline = sanitize_math_blocks(pipeline)
    pipeline = fix_prose_in_display_math(pipeline)
    pipeline = fix_display_math_blocks(pipeline)
    pipeline = collapse_trivial_aligned(pipeline)
    pipeline = fix_display_math_blocks(pipeline)
    pipeline = wrap_orphan_aligned_blocks(pipeline)
    pipeline = wrap_orphan_cases_blocks(pipeline)
    pipeline = unwrap_standalone_text_lines(pipeline)
    pipeline = remove_empty_display_pairs(pipeline)
    pipeline = fix_minus_as_list_in_aligned(pipeline)
    pipeline = expand_lecture_macros(pipeline)
    pipeline = sanitize_code_fences(pipeline)
    pipeline = collapse_blank_lines_in_display_math(pipeline)
    pipeline = fix_display_math_line_breaks(pipeline)
    pipeline = fix_inline_math_spans(pipeline)
    pipeline = convert_to_mdbook_math_delimiters(pipeline)
    return fix_inline_artifacts(pipeline)


def process_text_safe(text: str) -> str:
    """Apply math fixes only outside fenced code blocks."""
    parts = re.split(r"(```.*?```)", text, flags=re.DOTALL)
    out: list[str] = []
    for part in parts:
        if part.startswith("```"):
            out.append(sanitize_code_fences(part))
        else:
            out.append(process_text(part))
    return "".join(out)


def process_file(path: Path) -> bool:
    old = path.read_text(encoding="utf-8")
    new = process_text_safe(old)
    if new != old:
        path.write_text(new, encoding="utf-8")
        return True
    return False


CLASSIFICATION_MD = (
    Path(__file__).resolve().parent.parent
    / "src/ch05-math-physics-eq/02-classification.md"
)


def run_classification_fix() -> None:
    script = Path(__file__).resolve().parent / "fix_classification_md.py"
    if script.exists():
        import subprocess

        subprocess.run([sys.executable, str(script)], check=False)


def main():
    root = Path(__file__).resolve().parent.parent / "src"
    targets: list[Path] = []

    if len(sys.argv) > 1:
        for arg in sys.argv[1:]:
            p = Path(arg)
            if not p.is_absolute():
                p = root.parent / arg if (root.parent / arg).exists() else root / arg
            if p.is_dir():
                targets.extend(sorted(p.rglob("*.md")))
            elif p.exists():
                targets.append(p)
            else:
                alt = root / arg
                if alt.exists():
                    targets.append(alt)
    else:
        targets = sorted(root.rglob("*.md"))

    need_class_fix = any(
        t.resolve() == CLASSIFICATION_MD.resolve() for t in targets
    )
    targets = [t for t in targets if t.resolve() != CLASSIFICATION_MD.resolve()]

    changed = 0
    for md in targets:
        if process_file(md):
            changed += 1
            try:
                rel = md.relative_to(root.parent)
            except ValueError:
                rel = md
            print("fixed:", rel)
    if need_class_fix:
        run_classification_fix()
        print("fixed:", CLASSIFICATION_MD.relative_to(root.parent))
    print(f"Done. {changed} files updated.")


if __name__ == "__main__":
    main()
