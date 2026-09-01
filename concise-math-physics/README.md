# 简明数学物理方法

基于 [`../lecture/`](../lecture/) LaTeX 讲义编写的 mdBook 在线教材：保留讲义主要文字说明，结构精简；可用 `scripts/expand_all.sh` 从 `lecture/` 重新同步正文。

**作者**：罗凯  
**副标题**：学数学工具，探物理真谛

## 公式写法（必读）

正文是 Markdown + MathJax。**所有公式必须按 [MATHJAX.md](MATHJAX.md) 书写**，否则无法正确显示。要点：

| 项 | 源文件正确写法 |
|----|----------------|
| 行内 / 独立定界符 | `\\( ... \\)`、`\\[ ... \\]` |
| TeX 命令 | 单个反斜杠：`\frac`、`\mathbf` |
| 下标 | `A\_x`、`\int\_a^b`（不要写裸 `_`） |
| 细空格 | `\\,`（不要写 `\,`，会被 Markdown 变成逗号） |
| 独立公式行首 | 不要用 `+` / `-` / `*` 起行（会变成列表） |
| 星号上标 | `x^{\ast}`（不要 `x^*`） |

Agent / Cursor 规则同步见仓库 [`.cursor/rules/mdbook-mathjax.mdc`](../.cursor/rules/mdbook-mathjax.mdc)。

## 构建

### 依赖

- [mdBook](https://github.com/rust-lang/mdBook) ≥ 0.4
- 数学公式由 mdBook 内置 **MathJax** 渲染（可选安装 [mdbook-katex](https://github.com/lzanini/mdbook-katex)）

```bash
cargo install mdbook
# 可选: cargo install mdbook-katex
```

### 编译与预览

```bash
cd concise-math-physics
mdbook build          # 输出到 book/
mdbook serve          # http://localhost:3000
```

若公式显示异常，先对照 [MATHJAX.md](MATHJAX.md)；下标类问题可批量修复：

```bash
python3 scripts/fix_math_underscores.py
bash scripts/expand_all.sh   # 从讲义重新同步时也会跑 fix_math.py
```

## 数值示例

### Python

```bash
pip install numpy scipy sympy matplotlib
python scripts/ch01_residue_integral.py
python scripts/ch03_fourier_square_wave.py
python scripts/ch03_laplace_oscillator.py
bash scripts/run_all.sh
```

### Julia（可选）

```bash
julia scripts/ch01_residue_integral.jl      # 需要 QuadGK.jl
julia scripts/ch02_pendulum.jl              # 需要 DifferentialEquations.jl
julia scripts/ch03_fourier_square_wave.jl
julia scripts/ch05_wave_equation.jl
```

## 目录结构

```
concise-math-physics/
├── book.toml
├── MATHJAX.md        # 公式书写约定（必读）
├── src/              # Markdown 章节
├── scripts/          # Python / Julia 数值实验
├── assets/figures/   # 脚本生成的图
└── theme/            # 自定义 CSS
```

## 章节

1. 复变函数  
2. 变分法  
3. 傅里叶与拉普拉斯变换  
4. 特殊函数  
5. 数学物理方程  
6. 常微分与 Sturm–Liouville  
7. 曲线坐标系  
附录：级数展开、矢量恒等式

源 LaTeX 讲义保持只读，不在此目录修改。
