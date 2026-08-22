#!/usr/bin/env python3
"""Lint Markdown files for MathJax-compatible math."""
import re
import sys
from pathlib import Path

LATEX_CMD = re.compile(
    r"\\(?:frac|sum|int|begin|end|left|right|mathrm|mathbf|vec|partial|sqrt|lim|infty|delta|alpha|beta|gamma|operatorname|text|cases|aligned|pmatrix|bmatrix)\b"
)


INLINE_MATH = re.compile(r"\\\([^\\]*(?:\\.[^\\]*)*\\\)")
DISPLAY_OPEN = re.compile(r"^\\\[$")
DISPLAY_CLOSE = re.compile(r"^\\\]$")


def _strip_math_spans(line: str) -> str:
    line = re.sub(r"\\\([^\\]*(?:\\.[^\\]*)*\\\)", "", line)
    return line


def lint_file(path: Path) -> list[tuple[str, int, str]]:
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()
    issues: list[tuple[str, int, str]] = []

    in_display = False
    display_start = 0
    for i, line in enumerate(lines, 1):
        s = line.strip()
        if s == r"\[":
            if in_display:
                issues.append(("error", i, "Nested display math block"))
            in_display = True
            display_start = i
            continue
        if s == r"\]":
            if not in_display:
                issues.append(("error", i, "Unmatched \\] display delimiter"))
            else:
                in_display = False
            continue
        if not in_display and (s.startswith("\\begin{") or s.startswith("\\end{")):
            issues.append(("error", i, f"LaTeX environment outside math: {s[:50]}"))

        if in_display:
            if s.startswith(">") or s.startswith("#"):
                issues.append(
                    ("error", i, "Markdown inside display math block (started ~" + str(display_start) + ")")
                )
            if re.match(r"^[-*]\s", s):
                issues.append(("error", i, "List item inside display math block"))
            continue

        if re.match(r"^\\end\{", s) or re.match(r"^\\begin\{", s):
            issues.append(("error", i, f"LaTeX environment line outside math: {s[:60]}"))

        stripped = _strip_math_spans(line)
        if LATEX_CMD.search(stripped):
            issues.append(("error", i, f"LaTeX command outside math: {stripped.strip()[:70]}"))

        if s == r"\end{aligned}" or s == r"\begin{aligned}":
            issues.append(("error", i, "Stray aligned delimiter outside display math"))

    if in_display:
        issues.append(("error", display_start, "Unclosed \\[ display block"))

    return issues


def main():
    if len(sys.argv) < 2:
        print("Usage: lint_math.py <file.md> [file2.md ...]")
        sys.exit(1)

    root = Path(__file__).resolve().parent.parent
    total_err = 0
    for arg in sys.argv[1:]:
        path = Path(arg)
        if not path.is_absolute():
            path = root / path
        if not path.exists():
            print(f"MISSING: {path}")
            total_err += 1
            continue
        issues = lint_file(path)
        rel = path.relative_to(root) if path.is_relative_to(root) else path
        errs = [x for x in issues if x[0] == "error"]
        warns = [x for x in issues if x[0] == "warning"]
        print(f"\n{rel}: {len(errs)} errors, {len(warns)} warnings")
        for kind, line, msg in issues:
            print(f"  [{kind}] L{line}: {msg}")
        total_err += len(errs)

    sys.exit(1 if total_err else 0)


if __name__ == "__main__":
    main()
