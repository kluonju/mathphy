#!/usr/bin/env python3
"""Fix ch09 / related math so Markdown does not eat underscores inside MathJax."""
from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent / "src"
FILES = [
    ROOT / "ch09-tensor" / "01-vector-algebra.md",
    ROOT / "ch09-tensor" / "02-coordinates.md",
    ROOT / "ch09-tensor" / "03-grad-del.md",
    ROOT / "ch09-tensor" / "04-flux-divergence.md",
    ROOT / "ch09-tensor" / "05-curl-stokes.md",
    ROOT / "ch09-tensor" / "index.md",
]


def escape_us_in_body(body: str) -> str:
    out: list[str] = []
    i = 0
    n = len(body)
    while i < n:
        ch = body[i]
        if ch == "\\" and i + 1 < n:
            out.append(ch)
            out.append(body[i + 1])
            i += 2
            continue
        if ch == "_":
            out.append("\\_")
            i += 1
            continue
        out.append(ch)
        i += 1
    return "".join(out)


def transform_math(text: str) -> str:
    """Escape bare _ inside \\( \\) and \\[ \\] spans (two-backslash delimiters)."""
    # Delimiter tokens as they appear in the file
    tokens = [
        ("\\\\(", "\\\\)", False),  # written wrong - need actual chars
    ]
    # Build real delimiter strings: two backslashes + paren/bracket
    bs = "\\"
    pairs = [
        (bs + bs + "(", bs + bs + ")", True),
        (bs + bs + "[", bs + bs + "]", False),
    ]

    result: list[str] = []
    i = 0
    n = len(text)
    while i < n:
        matched = False
        for open_d, close_d, _inline in pairs:
            if text.startswith(open_d, i):
                j = text.find(close_d, i + len(open_d))
                if j < 0:
                    result.append(text[i])
                    i += 1
                    matched = True
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


def plain_captions(text: str) -> str:
    """Replace figure alts that contain LaTeX with plain-text alts."""
    lines = text.splitlines(keepends=True)
    out: list[str] = []
    for line in lines:
        if line.lstrip().startswith("![") and ("\\(" in line or "\\\\(" in line or "\\rho" in line or "\\theta" in line or "\\mathbf" in line or "\\hat" in line):
            # known mappings by figure path
            if "vec_dot_product" in line:
                out.append("![点积：投影与夹角 θ](../figures/vec_dot_product.png)\n")
            elif "vec_line_integral" in line:
                out.append("![路径上的线积分：分段 F·dℓ](../figures/vec_line_integral.png)\n")
            elif "vec_flux_ds" in line:
                out.append("![通量贡献 A·dS](../figures/vec_flux_ds.png)\n")
            elif "vec_stokes_cancel" in line:
                out.append("![内边环量抵消，仅边界 L 留下](../figures/vec_stokes_cancel.png)\n")
            elif "coords_cartesian" in line:
                out.append("![直角坐标系：点 P(x,y,z) 与局部基](../figures/coords_cartesian.png)\n")
            elif "coords_cylindrical" in line:
                out.append("![圆柱坐标系：ρ、φ、z 与局部基](../figures/coords_cylindrical.png)\n")
            elif "coords_spherical" in line:
                out.append("![球坐标系：r、θ、φ 与局部基](../figures/coords_spherical.png)\n")
            else:
                # strip math delimiters roughly for unknown
                out.append(line)
        else:
            out.append(line)
    return "".join(out)


def fix_broken_braces(text: str) -> str:
    """Repair known broken \\mathbf{ / \\mathrm{ spans in 02-coordinates."""
    bs = "\\"
    d0 = bs + bs + "("
    d1 = bs + bs + ")"
    reps = [
        (
            f"{d0}\\mathbf{{i_x,\\mathbf{{i}}_y,\\mathbf{{i}}_z{d1}",
            f"{d0}\\mathbf{{i}}_x,\\mathbf{{i}}_y,\\mathbf{{i}}_z{d1}",
        ),
        (
            f"{d0}\\mathbf{{i,\\mathbf{{j,\\mathbf{{k}}{d1}",
            f"{d0}\\mathbf{{i}},\\mathbf{{j}},\\mathbf{{k}}{d1}",
        ),
        (
            f"{d0}\\mathrm{{dx,\\mathrm{{d}}y,\\mathrm{{d}}z{d1}",
            f"{d0}\\mathrm{{d}}x,\\mathrm{{d}}y,\\mathrm{{d}}z{d1}",
        ),
        (
            f"{d0}\\mathrm{{dS_x{d1}",
            f"{d0}\\mathrm{{d}}S_x{d1}",
        ),
        (
            f"{d0}\\mathbf{{e_r{d1}",
            f"{d0}\\mathbf{{e}}_r{d1}",
        ),
        (
            f"{d0}\\mathbf{{e_\\phi{d1}",
            f"{d0}\\mathbf{{e}}_\\phi{d1}",
        ),
        (
            f"{d0}\\mathbf{{e_z{d1}",
            f"{d0}\\mathbf{{e}}_z{d1}",
        ),
        (
            f"{d0}\\hat{{\\mathbf{{e}}_r\\times\\hat{{\\mathbf{{e}}}}_\\phi=\\hat{{\\mathbf{{e}}}}_z{d1}",
            f"{d0}\\hat{{\\mathbf{{e}}}}_r\\times\\hat{{\\mathbf{{e}}}}_\\phi=\\hat{{\\mathbf{{e}}}}_z{d1}",
        ),
    ]
    # The above f-string escaping is error-prone; do literal search on file instead.
    return text


def fix_coordinates_literal(text: str) -> str:
    """Literal substring fixes using snippets copied from the file."""
    # Extract and print candidates if miss
    needles = [
        "\\mathbf{i_x,\\mathbf{i}_y,\\mathbf{i}_z",
        "\\mathbf{i,\\mathbf{j,\\mathbf{k}",
        "\\mathrm{dx,\\mathrm{d}y,\\mathrm{d}z",
        "\\mathrm{dS_x",
        "\\mathbf{e_r",
        "\\mathbf{e_\\phi",
        "\\mathbf{e_z",
        "\\hat{\\mathbf{e}_r\\times\\hat{\\mathbf{e}}_\\phi=\\hat{\\mathbf{e}}_z",
    ]
    # Actually in file TeX cmds have ONE backslash. Delimiters have TWO.
    # So broken bits look like: \\(\mathbf{i_x,\mathbf{i}_y,\mathbf{i}_z\\)
    bs = "\\"
    open_i = bs + bs + "("
    close_i = bs + bs + ")"

    pairs = [
        (
            open_i + bs + "mathbf{i_x," + bs + "mathbf{i}_y," + bs + "mathbf{i}_z" + close_i,
            open_i + bs + "mathbf{i}_x," + bs + "mathbf{i}_y," + bs + "mathbf{i}_z" + close_i,
        ),
        (
            open_i + bs + "mathbf{i," + bs + "mathbf{j," + bs + "mathbf{k}" + close_i,
            open_i + bs + "mathbf{i}," + bs + "mathbf{j}," + bs + "mathbf{k}" + close_i,
        ),
        (
            open_i + bs + "mathrm{dx," + bs + "mathrm{d}y," + bs + "mathrm{d}z" + close_i,
            open_i + bs + "mathrm{d}x," + bs + "mathrm{d}y," + bs + "mathrm{d}z" + close_i,
        ),
        (
            open_i + bs + "mathrm{dS_x" + close_i,
            open_i + bs + "mathrm{d}S_x" + close_i,
        ),
        (
            open_i + bs + "mathbf{e_r" + close_i,
            open_i + bs + "mathbf{e}_r" + close_i,
        ),
        (
            open_i + bs + "mathbf{e_" + bs + "phi" + close_i,
            open_i + bs + "mathbf{e}_" + bs + "phi" + close_i,
        ),
        (
            open_i + bs + "mathbf{e_z" + close_i,
            open_i + bs + "mathbf{e}_z" + close_i,
        ),
        (
            open_i
            + bs
            + "hat{"
            + bs
            + "mathbf{e}_r"
            + bs
            + "times"
            + bs
            + "hat{"
            + bs
            + "mathbf{e}}_"
            + bs
            + "phi="
            + bs
            + "hat{"
            + bs
            + "mathbf{e}}_z"
            + close_i,
            open_i
            + bs
            + "hat{"
            + bs
            + "mathbf{e}}_r"
            + bs
            + "times"
            + bs
            + "hat{"
            + bs
            + "mathbf{e}}_"
            + bs
            + "phi="
            + bs
            + "hat{"
            + bs
            + "mathbf{e}}_z"
            + close_i,
        ),
    ]
    for a, b in pairs:
        if a in text:
            text = text.replace(a, b)
            print("  fixed brace/span:", repr(a[:50]))
        else:
            # show nearby if key fragment present
            key = a[4:20] if len(a) > 20 else a
            if key in text:
                idx = text.find(key)
                print("  PARTIAL near:", repr(text[idx - 5 : idx + 40]))
            else:
                print("  miss:", repr(a[:55]))
    return text


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
    for path in FILES:
        if not path.exists():
            print("skip missing", path)
            continue
        text = path.read_text(encoding="utf-8")
        before = count_bare(text)
        text2 = plain_captions(text)
        if path.name == "02-coordinates.md":
            text2 = fix_coordinates_literal(text2)
        text2 = transform_math(text2)
        after = count_bare(text2)
        if text2 != text:
            path.write_text(text2, encoding="utf-8")
            print(f"UPDATED {path.relative_to(ROOT)} bare {before}->{after}")
        else:
            print(f"unchanged {path.relative_to(ROOT)} bare {before}")


if __name__ == "__main__":
    main()
