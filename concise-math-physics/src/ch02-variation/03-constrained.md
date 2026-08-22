### 约束问题

有限维函数在等式约束下的极值，由 [Lagrange 乘子法](02b-lagrange-multipliers.md) 处理。变分问题中更常见的是**积分型约束**：例如两点间曲线在围成面积为定值 \\(A\\) 的条件下求最短路径，即要求 \\(\\int u(x)\\,\\mathrm{d}x=A\\)。做法是在目标泛函上添加乘子项，化为无约束变分：对目标泛函 \\(J[u]\\) 添加 \\(\\lambda\\bigl(\\int u(x)\\,\\mathrm{d}x-A\\bigr)\\)。这里的 \\(\\lambda\\) 仍称为**拉格朗日乘子**。

以上例为例，我们需要极小化的泛函变成

\\[
J[u] = \int_{x_1}^{x_2} \sqrt{ 1 + u'(x)^2} dx   + \lambda \left( \int_{x_1}^{x_2} u(x) dx - A \right).
\\]

这样拉式量内包含了这一约束.对于该例子应用欧拉-拉格朗日方程,我们有

\\[
\lambda - \frac{\mathrm{d} }{\mathrm{d} x} \frac{u'}{\sqrt{1 + u'^2}} = 0,
\\]

可以求得

\\[
\frac{u'}{\sqrt{1+u'^2}}= \lambda x + c
\\]

令辅助函数\\( p(x)   = \lambda x + c   \\),  两边平方,得到

\\[
u' = \frac{p}{\sqrt{1 - p^2}} .
\\]

换元令\\( t = \lambda x + c\\), 则有 \\(dt = \lambda dx\\), 于是

\\[
du = u' dx = \frac{t}{\sqrt{1 - t^2}} \frac{dt}{\lambda} .
\\]

积分得到

\\[
u(x) = \int \frac{t}{\sqrt{1 - t^2}} \frac{dt}{\lambda} = - \frac{\sqrt{1 - t^2}}{\lambda} + d,
\\]

其中\\(d\\)为积分常数.
最终得到方程

\\[
(\lambda x +c)^2 + (\lambda u -d)^2 = 1
\\]

其中\\(c,d,\lambda\\)由\\(u(x_1)=y_1, u(x_2) = y_2\\) 和\\(\int u(x) dx = A\\)决定.
在这样的约束条件下,最短路径是一段圆弧！
此外, 可以对\\(p(x)\\)直接求导得到

\\[
\lambda = \frac{u"}{(1+y'^2) ^{3/2}}
\\]

而右边正式平面曲线的曲率\\(\kappa\\), 因此在约束条件下, 最短路径的曲率是常数.
故也可知曲线为圆弧.
