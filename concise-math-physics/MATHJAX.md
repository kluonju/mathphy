# mdBook / MathJax 公式约定

本书（`concise-math-physics`）用 mdBook + MathJax（`book.toml`：`mathjax-support = true`）。  
**写或改 `src/**/*.md` 时必须遵守本节**，否则公式会显示为碎斜体、缺下标，或被 Markdown 拆成列表。

Agent 侧同步规则：[`.cursor/rules/mdbook-mathjax.mdc`](../.cursor/rules/mdbook-mathjax.mdc)。

## 定界符

| 用途 | 源文件写法 | 说明 |
|------|------------|------|
| 行内 | `\\( ... \\)` | 两个反斜杠 + 括号 |
| 独立 | 单独一行 `\\[` … `\\]` | 同上 |
| TeX 命令 | `\mathbf`、`\frac`、`\partial` | **单个**反斜杠 |

## 必须转义（Markdown 会先吃掉这些字符）

| 符号 / 写法 | 正确（源文件） | 错误 | 原因 |
|-------------|--------------|------|------|
| 下标 `_` | `A\_x`、`\lim\_{n}`、`\int\_a^b` | `A_x` | `_` → `<em>` |
| 星号上标 | `x^{\ast}` | `x^*` | `*` → 强调 |
| 细空格 `\,` | `f(x)\\,\mathrm{d}x` | `f(x)\,\mathrm{d}x` | `\,` 被当成转义逗号，变成 `,` |
| 独立公式行首 | 用 `aligned`，或把 `+`/`-` 放在行中 | 行首写 `+` / `-` / `*` | 会被当成 Markdown 列表，公式断裂 |

### 细空格示例

```markdown
正确：\\(\int f(x)\\,\mathrm{d}x\\)
错误：\\(\int f(x)\,\mathrm{d}x\\)   ← 渲染后变成 f(x),mathrm{d}x
```

### 行首加减示例

```markdown
错误（`+` 单独起一行会被当成列表）：
\\[
A
+ B
\\]

正确：
\\[
\begin{aligned}
A
&= \cdots \\\\
&\quad + B .
\end{aligned}
\\]
```

## 图注

`![说明](图.png)` 的说明里不要放 `\\(...\\)`，用纯文字（如 `θ`、`A·dS`）。

## 自检

改完公式后建议：

```bash
cd concise-math-physics
mdbook build
# 打开 book/.../对应.html，确认公式块仍是完整的 \[...\]，未被拆成 <ul><li>
```

下标批量修复（不处理 `\,` / 行首 `+`）：

```bash
python3 scripts/fix_math_underscores.py
```
