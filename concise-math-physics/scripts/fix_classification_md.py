#!/usr/bin/env python3
"""One-off repairs for ch05-math-physics-eq/02-classification.md."""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PATH = ROOT / "src/ch05-math-physics-eq/02-classification.md"


def main():
    text = PATH.read_text(encoding="utf-8")

    # Standalone \text{...} -> prose
    def text_line(m: re.Match) -> str:
        return m.group(1)

    text = re.sub(r"^\\text\{([^}]*)\}\s*\.?\s*$", text_line, text, flags=re.MULTILINE)

    replacements = [
        (
            r"\$\$\n\\left\{\\begin\{aligned\}",
            "$$\n$$\n\\left\\{\\\\begin{aligned}",
        ),
        (
            r"""\\text\{或者\}, 再作自变数代换
\\$\\$
\\left\\{\\begin\{array\} \{ l \}
\{ \\xi = \\alpha \+ \\beta , \} \\\\
\{ \\eta = \\alpha - \\beta , \}
\\end\{array\}   \\text \{ 即 \} \\left\\{\\begin\{array\}\{l\}
\\$\\$
\\alpha=\\frac\{1\}\{2\}\(\\xi\+\\eta\) \\\\
\\beta=\\frac\{1\}\{2\}\(\\xi-\\eta\)
\\end\{array\}\\right\.\\right\.
\\$\\$""",
            """或者, 再作自变数代换

$$
\\left\\{\\begin{array}{l}
\\xi = \\alpha + \\beta, \\\\
\\eta = \\alpha - \\beta,
\\end{array}
\\quad \\text{即} \\quad
\\left\\{\\begin{array}{l}
\\alpha=\\frac{1}{2}(\\xi+\\eta), \\\\
\\beta=\\frac{1}{2}(\\xi-\\eta).
\\end{array}\\right.\\right.
$$""",
        ),
    ]

    # Manual blocks (exact strings from file)
    text = text.replace(
        """\\end{array}\\right.
$$
\\left\\{\\begin{aligned}
        u_{x x}""",
        """\\end{array}\\right.
$$
$$
\\left\\{\\begin{aligned}
        u_{x x}""",
    )

    text = text.replace(
        """\\text{或者}, 再作自变数代换
$$
\\left\\{\\begin{array} { l }
{ \\xi = \\alpha + \\beta , } \\\\
{ \\eta = \\alpha - \\beta , }
\\end{array}   \\text { 即 } \\left\\{\\begin{array}{l}
$$
\\alpha=\\frac{1}{2}(\\xi+\\eta) \\\\
\\beta=\\frac{1}{2}(\\xi-\\eta)
\\end{array}\\right.\\right.
$$""",
        """或者, 再作自变数代换

$$
\\left\\{\\begin{array}{l}
\\xi = \\alpha + \\beta, \\\\
\\eta = \\alpha - \\beta,
\\end{array}
\\quad \\text{即} \\quad
\\left\\{\\begin{array}{l}
\\alpha=\\frac{1}{2}(\\xi+\\eta), \\\\
\\beta=\\frac{1}{2}(\\xi-\\eta).
\\end{array}\\right.\\right.
$$""",
    )

    text = text.replace(
        """\\text{注意这里的} $\\xi$ 和 $\\eta$ 是复变数. 通常又作代换
$$
\\left\\{\\begin{array} { l }
{ \\xi = \\alpha + \\mathrm{i} \\beta , } \\\\
{ \\eta = \\alpha - \\mathrm{i} \\beta , }
\\end{array}   \\text { 即 } \\left\\{\\begin{array}{l}
$$
\\alpha=\\Re \\xi=\\frac{1}{2}(\\xi+\\eta), \\\\
\\beta=\\Im \\xi=\\frac{1}{2 \\mathrm{i}}(\\xi-\\eta) .
\\end{array}\\right.\\right.
$$""",
        """注意这里的 $\\xi$ 和 $\\eta$ 是复变数. 通常又作代换

$$
\\left\\{\\begin{array}{l}
\\xi = \\alpha + \\mathrm{i} \\beta, \\\\
\\eta = \\alpha - \\mathrm{i} \\beta,
\\end{array}
\\quad \\text{即} \\quad
\\left\\{\\begin{array}{l}
\\alpha=\\Re \\xi=\\frac{1}{2}(\\xi+\\eta), \\\\
\\beta=\\Im \\xi=\\frac{1}{2 \\mathrm{i}}(\\xi-\\eta).
\\end{array}\\right.\\right.
$$""",
    )

    text = text.replace(
        """$$
\\begin{aligned}
        & \\frac{d y}{d x}""",
        """$$
$$
\\begin{aligned}
        & \\frac{d y}{d x}""",
    )

    text = text.replace("$$\n$$\n\\begin{aligned}", "$$\n\\begin{aligned}", 1)  # only first dup if any

    text = text.replace(
        """采用新自变数后, 将 $\\xi_x / \\xi_y=-d y / d x=$ $-a_{12} / a_{11}$ 和
$a_{12}= \\pm \\sqrt{a_{11} \\cdot a_{22}}$ 代入, 得方程的前三个系数为
$$
$$
\\begin{aligned}""",
        """采用新自变数后, 将 $\\xi_x / \\xi_y=-d y / d x=$ $-a_{12} / a_{11}$ 和
$a_{12}= \\pm \\sqrt{a_{11} \\cdot a_{22}}$ 代入, 得方程的前三个系数为

$$
\\begin{aligned}""",
    )

    text = text.replace(
        """平面稳定场方程, 如稳定浓度分布, 稳定温度分布, 静电场方程, 无旋恒定电流场方程, 无旋定常流动方程等都是标准形式的椭圆型方程.
$$
## 定解条件""",
        """平面稳定场方程, 如稳定浓度分布, 稳定温度分布, 静电场方程, 无旋恒定电流场方程, 无旋定常流动方程等都是标准形式的椭圆型方程.

## 定解条件""",
    )

    text = text.replace(
        """就得到如下的定解问题:

$$

$$
\\left\\{\\begin{array}{l}
\t\\frac{\\partial^2 u}{\\partial t^2}-a^2 \\frac{\\partial^2 u}{\\partial x^2}=f(x, t), \\\\
\tt=0: u=\\varphi(x), \\frac{\\partial u}{\\partial t}=\\psi(x), \\\\
\tx=0:   u=0, \\\\
\tx=l:   u=0 .
\\end{array}\\right.
$$

$$
要在区域""",
        """就得到如下的定解问题:

$$
\\left\\{\\begin{array}{l}
\t\\frac{\\partial^2 u}{\\partial t^2}-a^2 \\frac{\\partial^2 u}{\\partial x^2}=f(x, t), \\\\
\tt=0: u=\\varphi(x), \\frac{\\partial u}{\\partial t}=\\psi(x), \\\\
\tx=0:   u=0, \\\\
\tx=l:   u=0 .
\\end{array}\\right.
$$

要在区域""",
    )

    # Ensure even $$ count: if odd, append closing
    n = sum(1 for ln in text.splitlines() if ln.strip() == "$$")
    if n % 2:
        text = text.rstrip() + "\n$$\n"

    PATH.write_text(text, encoding="utf-8")
    print(f"Wrote {PATH} ($$ lines: {n})")


if __name__ == "__main__":
    main()
