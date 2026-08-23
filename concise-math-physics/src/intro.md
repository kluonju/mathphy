# 前言

**简明数学物理方法** 在《数学物理方法》讲义（`lecture/`）基础上编写：保留讲义中的主要文字说明、定义、例题与推导，删去重复插图与部分冗长证明细节；各章末尾附 **数值实验**（`scripts/`）。

> 学数学工具，探物理真谛。

正文由 `lecture/` 源稿经脚本转换后人工校对，若与讲义有出入请以 `lecture/` 为准。

## 本书结构

每章对应讲义中的一章或多节：**概念与定理**（含讲义原文表述）、**例题**、**应用**；部分章节含 Python / Julia 数值示例。

| 章 | 主题 |
|----|------|
| 0 | 预备知识（数集、三角、微积分、指标记号、向量、线性代数） |
| 1 | 复变函数、留数与鞍点渐近 |
| 2 | 变分法 |
| 3 | 傅里叶与拉普拉斯变换 |
| 4 | 特殊函数 |
| 5 | 数学物理方程（含电磁学中的波动/Poisson 衔接） |
| 6 | 常微分与 Sturm–Liouville 理论 |
| 7 | 曲线坐标系 |
| 8 | 数值方法（求根、积分、插值、ODE） |
| 9 | 矢量与张量 |
| 附录 | 级数展开与矢量恒等式 |

部分应用素材亦参考 Warwick PX284（Electromagnetic Theory and Optics）中与向量分析、波动方程相关的章节，已改写为本书体例。

## 符号约定

| 记号 | 含义 |
|------|------|
| \\(\mathrm{i}\\) | 虚数单位 |
| \\(\mathcal{L}\{f\}\\) | \\(f(t)\\) 的拉普拉斯变换 |
| \\(\mathcal{L}^{-1}\{\bar f\}\\) | 拉普拉斯反变换 |
| \\(\mathcal{F}\{f\}\\) | 傅里叶变换 |
| \\(\delta\_{ij}\\) | Kronecker 符号 |
| \\(\delta(x)\\) | Dirac \\(\delta\\) 函数（分布） |
| \\(\varepsilon\_{ijk}\\) | Levi-Civita（完全反对称）符号 |
| \\(\partial\_i\\) | \\(\partial/\partial x\_i\\) |
| \\(\mathrm{Res}(f,z\_0)\\) | \\(f\\) 在 \\(z\_0\\) 的留数 |

偏导数记 \\(\partial f/\partial x\\)（指标形式常写 \\(\partial\_i\\)）；函数对自变量的全导数记 \\(\mathrm{d}f/\mathrm{d}x\\)。

第 0 章汇总了数集、三角恒等式、微积分、[指标记号与爱因斯坦约定](ch00-prerequisites/04-index-notation.md)与向量、线性代数等预备内容。

## 如何使用本书

```bash
# 构建 HTML
cd concise-math-physics
mdbook build

# 本地预览（热重载）
mdbook serve
```

数值示例：

```bash
python scripts/ch03_fourier_square_wave.py
julia scripts/ch03_fourier_square_wave.jl
```
