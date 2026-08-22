## 微积分概要

### 极限与连续

函数 \\(f(x)\\) 在 \\(x_0\\) 处的极限记为 \\(\lim_{x \to x_0} f(x) = L\\)。若极限存在且等于函数值 \\(f(x_0)\\)，则称 \\(f\\) 在 \\(x_0\\) 处**连续**。初等函数在其定义域内连续。

### 导数

函数 \\(y = f(x)\\) 在 \\(x\\) 处的导数定义为

\\[
f'(x) = \lim_{\Delta x \to 0} \frac{f(x + \Delta x) - f(x)}{\Delta x} .
\\]

常用求导法则：

\\[
\\[
\begin{aligned}
(cf)' &= c f', \quad (f \pm g)' = f' \pm g', \quad (fg)' = f'g + fg', \\\\
\left(\frac{f}{g}\right)' &= \frac{f'g - fg'}{g^2}, \quad (f \circ g)'(x) = f'(g(x))\, g'(x) .
\end{aligned}
\\]
\\]

初等函数导数（\\(a>0\\)）：

\\[
\\[
\begin{aligned}
(x^n)' &= n x^{n-1}, \quad (e^x)' = e^x, \quad (a^x)' = a^x \ln a, \\\\
(\ln x)' &= \frac{1}{x}, \quad (\sin x)' = \cos x, \quad (\cos x)' = -\sin x, \\\\
(\tan x)' &= \sec^2 x, \quad (\arctan x)' = \frac{1}{1+x^2} .
\end{aligned}
\\]
\\]

### 积分

不定积分 \\(\int f(x)\,\mathrm{d}x = F(x) + C\\) 满足 \\(F'(x) = f(x)\\)。定积分

\\[
\int_a^b f(x)\,\mathrm{d}x = F(b) - F(a)
\\]

由牛顿–莱布尼茨公式给出。分部积分与换元是两类基本技巧：

\\[
\int u\,\mathrm{d}v = uv - \int v\,\mathrm{d}u, \qquad
\int f(g(x))\, g'(x)\,\mathrm{d}x = \int f(u)\,\mathrm{d}u \quad (u = g(x)) .
\\]

### 多元微积分

多元函数 \\(f(x_1,\ldots,x_n)\\) 的偏导数记 \\(\partial f / \partial x_i\\)。梯度为

\\[
\nabla f = \left( \frac{\partial f}{\partial x_1}, \ldots, \frac{\partial f}{\partial x_n} \right) .
\\]

链式法则：若 \\(f = f(x_1(t),\ldots,x_n(t))\\)，则

\\[
\frac{\mathrm{d}f}{\mathrm{d}t} = \sum_{i=1}^n \frac{\partial f}{\partial x_i}\frac{\mathrm{d}x_i}{\mathrm{d}t} .
\\]

二重、三重积分在直角、柱、球坐标下的体元形式见第 [7 章](../ch07-coordinates/index.md)。

### Taylor 级数

若 \\(f\\) 在 \\(x_0\\) 邻域内无穷次可微，则

\\[
f(x) = \sum_{n=0}^{\infty} \frac{f^{(n)}(x_0)}{n!}(x - x_0)^n .
\\]

一元情形的常用展开见[附录：级数展开](../appendix/series.md)。变分法与特殊函数各章将反复用到 Taylor 展开与逐项积分、求导。
