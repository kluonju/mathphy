## 三角函数恒等式

弧度制下，三角函数与指数函数通过欧拉公式相联系：

\\[
e^{\mathrm{i}\theta} = \cos\theta + \mathrm{i}\sin\theta .
\\]

由此可得 \\(\cos\theta = \tfrac{1}{2}(e^{\mathrm{i}\theta}+e^{-\mathrm{i}\theta})\\)，\\(\sin\theta = \tfrac{1}{2\mathrm{i}}(e^{\mathrm{i}\theta}-e^{-\mathrm{i}\theta})\\)。

### 基本关系

\\[
\\[
\begin{aligned}
\sin^2\theta + \cos^2\theta &= 1, \\\\
1 + \tan^2\theta &= \sec^2\theta, \\\\
1 + \cot^2\theta &= \csc^2\theta .
\end{aligned}
\\]
\\]

### 和角与倍角公式

\\[
\\[
\begin{aligned}
\sin(\alpha \pm \beta) &= \sin\alpha\cos\beta \pm \cos\alpha\sin\beta, \\\\
\cos(\alpha \pm \beta) &= \cos\alpha\cos\beta \mp \sin\alpha\sin\beta, \\\\
\tan(\alpha \pm \beta) &= \frac{\tan\alpha \pm \tan\beta}{1 \mp \tan\alpha\tan\beta}, \\\\
\sin 2\alpha &= 2\sin\alpha\cos\alpha, \\\\
\cos 2\alpha &= \cos^2\alpha - \sin^2\alpha = 2\cos^2\alpha - 1 = 1 - 2\sin^2\alpha, \\\\
\tan 2\alpha &= \frac{2\tan\alpha}{1 - \tan^2\alpha} .
\end{aligned}
\\]
\\]

### 半角公式

\\[
\sin^2\frac{\alpha}{2} = \frac{1 - \cos\alpha}{2}, \qquad
\cos^2\frac{\alpha}{2} = \frac{1 + \cos\alpha}{2}, \qquad
\tan\frac{\alpha}{2} = \frac{\sin\alpha}{1 + \cos\alpha} = \frac{1 - \cos\alpha}{\sin\alpha} .
\\]

### 积化和差与和差化积

\\[
\\[
\begin{aligned}
\sin\alpha\cos\beta &= \tfrac{1}{2}[\sin(\alpha+\beta) + \sin(\alpha-\beta)], \\\\
\cos\alpha\sin\beta &= \tfrac{1}{2}[\sin(\alpha+\beta) - \sin(\alpha-\beta)], \\\\
\cos\alpha\cos\beta &= \tfrac{1}{2}[\cos(\alpha+\beta) + \cos(\alpha-\beta)], \\\\
\sin\alpha\sin\beta &= -\tfrac{1}{2}[\cos(\alpha+\beta) - \cos(\alpha-\beta)], \\\\
\sin\alpha + \sin\beta &= 2\sin\frac{\alpha+\beta}{2}\cos\frac{\alpha-\beta}{2}, \\\\
\cos\alpha + \cos\beta &= 2\cos\frac{\alpha+\beta}{2}\cos\frac{\alpha-\beta}{2} .
\end{aligned}
\\]
\\]

### 反三角函数

\\[
\arcsin x + \arccos x = \frac{\pi}{2}, \qquad
\arctan x + \operatorname{arccot} x = \frac{\pi}{2} \quad (x \in \mathbb{R}) .
\\]

在复变函数与留数计算中，常利用 \\(\cos\theta = \tfrac{1}{2}(z + z^{-1})\\)、\\(\sin\theta = \tfrac{1}{2\mathrm{i}}(z - z^{-1})\\)（\\(z = e^{\mathrm{i}\theta}\\)）将三角有理式化为代数有理式。更完整的级数展开见[附录：级数展开](../appendix/series.md)。
