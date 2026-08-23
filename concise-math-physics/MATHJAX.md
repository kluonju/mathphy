# mdBook / MathJax 公式约定

本书（`concise-math-physics`）用 mdBook + MathJax。写 Markdown 时按下列规则，避免行内公式被 Markdown 破坏。

更完整的 Agent 规则见仓库根目录：[`.cursor/rules/mdbook-mathjax.mdc`](../.cursor/rules/mdbook-mathjax.mdc)。

## 定界符

| 用途 | 源文件写法 |
|------|------------|
| 行内 | `\\( ... \\)` |
| 独立 | 单独一行 `\\[` … `\\]` |
| TeX 命令 | 单个反斜杠：`\mathbf`、`\frac` |

## 必须转义

| 符号 | 正确 | 错误 | 原因 |
|------|------|------|------|
| 下标 `_` | `A\_x`、`\lim\_{n}` | `A_x` | `_` 变成 `<em>` |
| 星号上标 | `x^{\ast}` | `x^*` | `*` 变成强调 |

## 图注

`![说明](图.png)` 的说明里不要放 `\\(...\\)`，用纯文字。

## 修复脚本

```bash
python3 scripts/fix_math_underscores.py
```
