# 第6章 偏微分方程与 ODE

对于求解未知函数 \\(y(x)\\) 满足型如 \\(y'(x) = f(x)\\) 类型的问题衍生出了微分方程这一数学分支。而微分方程又可分为**常微分方程**（ordinary differential equation, ODE）和**偏微分方程**（partial differential equation, PDE）。

含有**独立变量**（一般用 \\(x,y,z,t\\) 等表示）和**依赖变量**（一般用 \\(f,g,h\\) 等表示），以及依赖变量的导数的等式称为**微分方程**。微分方程中所含导数的最高阶数称为微分方程的**阶**（order）。

如 \\(f' + a f = b\\)，\\(f" + p(x) f' + q(x) f = \lambda\\)，\\(\frac{\partial f{\partial x} + \frac{\partial^2 f}{\partial y^2} + \frac{\partial^2 f}{\partial x \partial y} = 0\\)，\\(f^{(n) - x f(x) f^{(n-1)} = 0\\) 等等都是微分方程，对应的阶数分别为 1 阶、2 阶、2 阶和 \\(n\\) 阶。有且仅有一个独立变量的称为常微分方程，而超过一个独立变量的称为偏微分方程。

## 线性算子

\\(\frac{d}{dx}\\) 是线性算子：

\\[
\frac{d}{dx}(\alpha f+\beta g)=\alpha \frac{d}{dx} f +\beta \frac{d}{dx} g
\\]

线性算子的通用形式可表示为

\\[
L=\sum\_{\nu=0}^n p\_\nu(x) \frac{d^\nu}{d x^\nu}, \quad p\_\nu(x) \text{ 任意 }
\\]

类似的 \\(\frac{d^2}{dx^2}\\) 也是线性算子。

如果依赖变量在所有项中都是同样的幂次，则称为齐次的，否则称为非齐次的。如 \\(f" + p(x) f' + q(x) f = 0\\) 是齐次的，而 \\(f" + p(x) f' + q(x) f = g(x)\\) 是非齐次的。

本章在常微分方程理论基础上，为分离变量法与 Sturm–Liouville 本征值问题提供数学工具。
