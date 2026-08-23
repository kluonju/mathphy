#!/usr/bin/env python3
"""Escape bare underscores inside MathJax spans across the book source.

mdBook MathJax delimiters in this repo are written with two backslashes:
  \\( ... \\)   \\[ ... \\]
TeX commands use a single backslash. Subscripts must be \\_ or Markdown
turns _x into <em>x</em> and breaks rendering.
"""
from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent / "src"


def escape_us_in_body(body: str) -> str:
    out: list[str] = []
    i = 0
    n = len(body)
    while i < n:
        if body[i] == "\\" and i + 1 < n:
            out.append(body[i])
            out.append(body[i + 1])
            i += 2
            continue
        if body[i] == "_":
            out.append("\\_")
            i += 1
            continue
        out.append(body[i])
        i += 1
    return "".join(out)


def transform_math(text: str) -> str:
    bs = "\\"
    pairs = [
        (bs + bs + "(", bs + bs + ")"),
        (bs + bs + "[", bs + bs + "]"),
    ]
    result: list[str] = []
    i = 0
    n = len(text)
    while i < n:
        matched = False
        for open_d, close_d in pairs:
            if text.startswith(open_d, i):
                j = text.find(close_d, i + len(open_d))
                if j < 0:
                    break
                body = text[i + len(open_d) : j]
                result.append(open_d)
                result.append(escape_us_in_body(body))
                result.append(close_d)
                i = j + len(close_d)
                matched = True
                break
        if not matched:
            result.append(text[i])
            i += 1
    return "".join(result)


def count_bare(text: str) -> int:
    bs = "\\"
    pairs = [(bs + bs + "(", bs + bs + ")"), (bs + bs + "[", bs + bs + "]")]
    bare = 0
    i = 0
    n = len(text)
    while i < n:
        hit = False
        for o, c in pairs:
            if text.startswith(o, i):
                j = text.find(c, i + len(o))
                if j < 0:
                    break
                body = text[i + len(o) : j]
                k = 0
                while k < len(body):
                    if body[k] == "\\" and k + 1 < len(body):
                        k += 2
                        continue
                    if body[k] == "_":
                        bare += 1
                    k += 1
                i = j + len(c)
                hit = True
                break
        if not hit:
            i += 1
    return bare


def main() -> None:
    paths = sorted(ROOT.rglob("*.md"))
    if len(sys.argv) > 1:
        paths = [Path(a) for a in sys.argv[1:]]

    changed = 0
    for path in paths:
        text = path.read_text(encoding="utf-8")
        before = count_bare(text)
        if before == 0:
            continue
        text2 = transform_math(text)
        after = count_bare(text2)
        if text2 != text:
            path.write_text(text2, encoding="utf-8")
            changed += 1
            print(f"{path.relative_to(ROOT)}: {before} -> {after}")
    print(f"updated {changed} files")


if __name__ == "__main__":
    main()
