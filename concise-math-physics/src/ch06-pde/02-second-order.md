## 二阶线性常微分方程（齐次）

我们现在转向本章的主要内容——二阶线性常微分方程。这类方程极为重要，
因为它们出现在量子力学、电磁理论以及物理学其他领域中求解偏微分方程的常用方法里。
与一阶线性常微分方程不同，二阶线性常微分方程通常没有普适的封闭解，
一般需要采用幂级数形式的解法。在讨论级数解法的一般方法之前，我们首先考察微分方程中奇点的概念。

奇点

微分方程的奇点概念对我们有两方面的重要意义：
（1）它有助于对微分方程进行分类，并识别那些可以转化为常见形式的方程
（本小节后面会讨论）；（2）它关系到能否找到级数解的可行性。

当一个线性齐次二阶常微分方程写成如下形式时：

\\[
y"+p(x) y '+q(x) y=0
\\]

若 \\(p(x)\\) 和 \\(q(x)\\) 在 \\(x\_0\\) 处有限，则称 \\(x\_0\\) 为该方程的常点（ordinary point）。如果 \\(p(x)\\) 或 \\(q(x)\\) 在 \\(x \rightarrow x\_0\\) 时发散，则 \\(x\_0\\) 称为奇点（singular point）。奇点进一步分为正则奇点（regular）和非常奇点（irregular，也称为本性奇点 essential singularity）：


- 若 \\(x\_0\\) 为奇点，但 \\(\left(x-x\_0\right) p(x)\\) 和 \\(\left(x-x\_0\right)^2 q(x)\\) 在 \\(x\_0\\) 处仍有限，则 \\(x\_0\\) 为正则奇点。

- 若 \\(p(x)\\) 发散速度快于 \\(1 /\left(x-x\_0\right)\\)，使得 \\(\left(x-x\_0\right) p(x)\\) 在 \\(x \rightarrow x\_0\\) 时趋于无穷，或 \\(q(x)\\) 发散快于 \\(1 /\left(x-x\_0\right)^2\\)，使得 \\(\left(x-x\_0\right)^2 q(x)\\) 在 \\(x \rightarrow x\_0\\) 时趋于无穷，则 \\(x\_0\\) 为非常奇点。

这些定义适用于所有有限的 \\(x\_0\\)。

> **注** 注意这里的\\(\infty\\)为常奇点的情况具体
解释我们并没有给出, 它的解决需要用\\(z=1/x\\)的代换研究\\(z=0\\)时的情形, 具体讨论这里略去.

常奇点(或正则奇点)

\\[
\left\{\begin{array}{l}
\left(x-x\_0\right) p\left(x\_0\right) \text{有限}
\\\\
\left(x-x\_0\right)^2 q(x) \text{有限}
\\ p\left(x\_0\right), q(x) \rightarrow \infty .\end{array}
\right.
\\]
其他情况为非常奇点.

下面给出几种重要的ODE的常奇点


- 超几何(hypergeometic):


\\[
x(x-1) y"+[(1+a+b) x+c] y'+a b y= 0
\\]

常奇点 \\(0,1, \infty\\)\\

- 勒让德 (Legendre):


\\[
\left(1-x^2\right) y"-2 x y'+l(l+1) y=0
\\]

常奇点. \\(-1,1, \infty\\) .\\

- 切比雪夫. (Chebyshev):


\\[
\left(1-x^2\right) y"-x y'+n^2 y=0
\\]

常奇点 \\(-1,1, \infty\\).\\


- 合流超几何 (confluent hypergeometic):


\\[
x y"+(c-x) y'-a y=0,
\\]

\\

- 拉盖尔(Laguerre)


\\[
x y"+(1-x) y'+a y=0,
\\]

常奇点 \\(0\\).

- 贝塞尔(Bessel)


\\[
x^2 y" + xy' + (x^2 - n^2) y = 0
\\]

常奇点\\(0\\).

### 几类特殊的二阶方程

####  \\(y" = f(x)\\) 型

此类方程只需要积分两次就可以得到通解

\\[
y = \int F(x) dx + C\_1 x + C\_2
\\]

其中\\(F(x) = \int f(x) dx\\), \\(C\_1, C\_2\\)是积分常数.
####  \\(y" = f(x, y')\\) 型

利用换元\\(u = y'\\), 则有\\(u' = y"\\), 原方程化为一阶方程

\\[
u' = f(x,u)
\\]

该解为\\(u = \varphi(x, C\_1)\\), 原方程解为

\\[
y = \int \varphi(x, C\_1) dx  + C\_2.
\\]

### 常点邻域上的级数解

考虑线性（经典）振子方程

\\[
\frac{d^2 y}{d x^2}+\omega^2 y=0
\\]

我们已经用其他方法解过这个方程，得到的解为 \\(y=\sin \omega x\\) 和 \\(\cos \omega x\\)。

我们尝试设

\\[
\begin{aligned}
y(x) & =x^s\left(a\_0+a\_1 x+a\_2 x^2+a\_3 x^3+\cdots\right) \\\\
& =\sum\_{j=0}^{\infty} a\_j x^{s+j},   a\_0 \neq 0
\end{aligned}
\\]

其中指数 \\(s\\) 以及所有系数 \\(a\_j\\) 都尚未确定。注意 \\(s\\) 不必为整数。对 \\(y(x)\\) 两次求导，得到

\\[
\begin{aligned}
\frac{d y}{d x} & =\sum\_{j=0}^{\infty} a\_j(s+j) x^{s+j-1}, \\\\
\frac{d^2 y}{d x^2} & =\sum\_{j=0}^{\infty} a\_j(s+j)(s+j-1) x^{s+j-2} .
\end{aligned}
\\]

将上述表达式代入方程，有

\\[
\sum\_{j=0}^{\infty} a\_j(s+j)(s+j-1) x^{s+j-2}+\omega^2 \sum\_{j=0}^{\infty} a\_j x^{s+j}=0 .
\\]

由于幂级数的性质, 各个系数必须为零.
对于最低幂次项有

\\[
a\_0(s)(s-1)=0
\\]

这个方程来自于最低次幂\\(x\\)的系数，被称为判别方程（indicial equation）。
判别方程及其根对我们的分析至关重要。在本例中，它清楚地告诉我们\\(s=0\\)或\\(s=1\\)，
因此我们的级数解必须以\\(x^0\\)或\\(x^1\\)项开始。

进一步考察, 我们发现下一个最低次幂\\(x\\)，即\\(x^{s-1\\)，
也只在一项中出现（即第一组求和中\\(j=1\\)时）。令\\(x^{s-1\\)的系数为零，有

\\[
a\_1(s+1)s=0 .
\\]

这表明如果\\(s=1\\)，则必须有\\(a\_1=0\\)。而如果\\(s=0\\)，该方程对系数没有任何限制。

\\[
\begin{aligned}
& x^{s-1}: a\_1(s+1)(s)=0 \\\\
& x^s: a\_2(s+2)(s+1)+a\_0 w^2=0
\end{aligned}
\\]

若 \\(s=0\\), \\(y \sim  a\_0+a\_1 x+\cdots\\)
若 \\(s=1, y \sim a\_0 x+a\_1 x^2+\cdots\\)
当 \\(s=1\\)时, \\(a\_1=0\\).
当 \\(s=0\\) 时, \\(a\_1\\) 任意, 因此我们取\\(a\_1=0\\).

\\[
\begin{gathered}
\Rightarrow a\_{j+2}(s+j+2)(s+j+1)+w^2 a\_j=0 \\\\
\Rightarrow a\_{j+2}=\frac{-w^2}{(s+j+2)(s+j+1)} a\_j
\end{gathered}
\\]

递推关系.
若\\(s=0\\)

\\[
\begin{aligned}
a\_{j+2}=\frac{-\omega^2}{(j+2)(j+1)} a\_j \\\\
& a\_2=-\frac{w^2}{2 !} a\_0 \\\\
& a\_4=-\frac{a\_2}{3^3 4}=+\frac{w^4}{4 !} a\_0 \\\\
& a\_6=-\frac{a\_0^{3.4}}{5.6}=-\frac{w 6}{6 !} a\_0 \\\\
&
\end{aligned}
\\]

\\[
a\_{2 n}=(-1)^n \frac{w^{2 n}}{2 n !} a\_0
\\]

\\[
\begin{aligned}
y & \left.=a\_0\left[1-\frac{(\omega x)^2}{2 !}+\frac{(\omega x}{4}\right)^4-\frac{\omega x x^6}{6 !}+\omega\right] \\\\
& =a\_0 \cos \omega x .
\end{aligned}
\\]

若 \\(s=1\\)

\\[
\begin{aligned}
& a\_{j+2}=-a\_j \frac{\omega^2}{(j+3) (j+2)} \\\\
& \Rightarrow a\_2=-a\_0 \frac{\omega^2}{2 \cdot 3}=\frac{\omega^2}{3 !} a\_0 \\\\
& a\_4=-a\_2 \frac{\omega^2}{5 \cdot 4}=\frac{\omega^4}{5 !} a\_0 \\\\
& a\_6=-a\_4 \frac{\omega^2}{6\cdot 7}=\frac{w^6}{7 !} a\_0 \\\\
\end{aligned}
\\]

\\[
\begin{aligned}
& \Rightarrow   a\_0 x\left[1-\frac{(\omega x)^2}{3 !}+\frac{(\omega x)^{4}}{5 !}-\frac{(\omega x)^6}{7 !} \cdots\right] \\\\
& =\frac{a\_0}{\omega}\left[(\omega x)-\frac{(\omega x)^3}{3 !}+\frac{(\omega x)^5}{5 !} \cdots\right] \\\\
& =\frac{a\_0}{\omega} \sin \omega x
\end{aligned}
\\]

此方法称为Frobenius方法,上面关于\\(x\_0\\)上展开的,一般的
我们可以在 \\(x\_0\\)处展开

\\[
y(x)=\sum\_{j=0}^{\infty} a\_j\left(x-x\_0\right)^{s+j}, a\_0 \neq 0 .
\\]

### 正则奇点邻域上的级数求解

对线性振子的处理似乎过于简单。我们将幂级数（见式(7.28)）代入微分方程（见式(7.27)），很容易就得到了两个线性无关的解。

为了了解可能出现的其他情况，我们尝试求解贝塞尔方程：

\\[
x^2 y^{\prime \prime}+x y^{\prime}+\left(x^2-n^2\right) y=0 .
\\]

同样，假设解的形式为

\\[
y(x)=\sum\_{j=0}^{\infty} a\_j x^{s+j},
\\]

对其求导并代入方程（7.40），得到

\\[
\begin{aligned}
& \sum\_{j=0}^{\infty} a\_j(s+j)(s+j-1) x^{s+j}+\sum\_{j=0}^{\infty} a\_j(s+j) x^{s+j} \\\\
&  +\sum\_{j=0}^{\infty} a\_j x^{s+j+2}-\sum\_{j=0}^{\infty} a\_j^2 x^{s+j}=0
\end{aligned}
\\]

令 \\(j=0\\)，得到 \\(x^s\\) 的系数，即左边最低次幂的系数：

\\[
a\_0\left[s(s-1)+s-n^2\right]=0
\\]

且 \\(a\_0 \neq 0\\)（定义如此）。因此，式（7.42）给出判别方程

\\[
s^2-n^2=0
\\]

解为 \\(s= \pm n\\)。
还需要考察 \\(x^{s+1}\\) 的系数，得到

\\[
a\_1\left[(s+1) s+s+1-n^2\right]=0,
\\]

即

\\[
a\_1(s+1-n)(s+1+n)=0 .
\\]

对于 \\(s= \pm n\\)，\\(s+1-n\\) 和 \\(s+1+n\\) 都不为零，因此必须有 \\(a\_1=0\\)。
继续考察 \\(x^{s+j}\\) 的系数（取 \\(s=n\\)），它出现在第一、二、四项中 \\(a\_j\\) 的系数，在第三项中则是 \\(a\_{j-2\\)。令 \\(x^{s+j\\) 的总系数为零，得到

\\[
a\_j\left[(n+j)(n+j-1)+(n+j)-n^2\right]+a\_{j-2}=0 .
\\]

将 \\(j\\) 替换为 \\(j+2\\)，对 \\(j \geq 0\\) 可写为

\\[
a\_{j+2}=-a\_j \frac{1}{(j+2)(2 n+j+2)},
\\]

这就是所需的递推关系。不断应用该递推关系可得

\\[
\begin{aligned}
& a\_2=-a\_0 \frac{1}{2(2 n+2)}=-\frac{a\_0 n!}{2^2 1!(n+1)!} \\\\
& a\_4=-a\_2 \frac{1}{4(2 n+4)}=\frac{a\_0 n!}{2^4 2!(n+2)!} \\\\
& a\_6=-a\_4 \frac{1}{6(2 n+6)}=-\frac{a\_0 n!}{2^6 3!(n+3)!},   \text { 以此类推 }
\end{aligned}
\\]

一般地，

\\[
a\_{2 p}=(-1)^p \frac{a\_0 n!}{2^{2 p} p!(n+p)!} .
\\]

将这些系数代入假设的级数解，有

\\[
y(x)=a\_0 x^n\left[1-\frac{n!x^2}{2^2 1!(n+1)!}+\frac{n!x^4}{2^4 2!(n+2)!}-\cdots\right] .
\\]

用求和式表示为

\\[
\begin{aligned}
y(x) & =a\_0 \sum\_{j=0}^{\infty}(-1)^j \frac{n!x^{n+2 j}}{2^{2 j} j!(n+j)!} \\\\
& =a\_0 2^n n!\sum\_{j=0}^{\infty}(-1)^j \frac{1}{j!(n+j)!}\left(\frac{x}{2}\right)^{n+2 j} .
\end{aligned}
\\]

在第14章中，最终的求和式（取 \\(a\_0=1 / 2^n n!\\)）被定义为贝塞尔函数 \\(J\_n(x)\\)：

\\[
J\_n(x)=\sum\_{j=0}^{\infty}(-1)^j \frac{1}{j!(n+j)!}\left(\frac{x}{2}\right)^{n+2 j} .
\\]

注意，这个解 \\(J\_n(x)\\) 具有偶或奇对称性，正如从贝塞尔方程的形式可以预期的那样。
当 \\(s=-n\\) 且 \\(n\\) 不是整数时，可以得到第二个不同的级数解，记为 \\(J\_{-n(x)\\)。但当 \\(-n\\) 是负整数时，会出现问题。此时系数的递推关系仍由式（7.45）给出，只是 \\(2n\\) 替换为 \\(-2n\\)。当 \\(j+2=2n\\) 或 \\(j=2(n-1)\\) 时，\\(a\_{j+2\\) 的分母为零，Frobenius 方法无法得到与假设 \\(x^{-n\\) 开头的级数解相容的解。

通过代入无穷级数，我们为线性振子方程得到了两个解，为贝塞尔方程得到了一个（若 \\(n\\) 不是整数则有两个）解。对于“是否总能这样做？该方法是否总是有效？”的问题，答案是“不，总不能这样做。级数解法并不总是有效。”

\\(\nu\\)阶贝塞尔方程的级数求解参考书上.

Frobenius 方法并不总是能给出两个解，当特征根的差为整数时,级数解法会给出两个线性相关的, 因此需要其他方法.
一般会给出一个级数解，找出第二个解的方式可以通过如下方法获得.

这里引入朗斯基行列式(Wronskian)

\\[
\Delta(x)=\left|\begin{array}{ll}
y\_1(x) & y\_2(x) \\\\
y\_1'(x) & y\_2'(x)
\end{array}\right|= y\_1(x) y\_2'(x) - y\_2(x) y\_1'(x)
\\]

由于\\(y\_1, y\_2\\)满足微分方程,

\\[
\begin{aligned}
& \left(y\_1 y\_2"-y\_1"
y\_2\right)+p\left(y\_1 y\_2'-y\_1' y\_2\right) = 0\\\\
& \frac{d \Delta}{d x} - p \Delta(x)=0
\end{aligned}
\\]

\\[
\Delta(x)=\Delta\_0 e^{-\int p(x) d x}
\\]

\\[
\begin{aligned}
& \frac{d}{d x}\left(\frac{y\_{2}}{y\_1}\right)=\frac{y\_{1} y\_{2}'-y\_{1}' y\_{2}}{y\_{1}^2}=\frac{\Delta(x)}{y\_{1}^2} \\\\
& y\_{2}=y\_{1} \int \frac{\Delta(x)}{\left(y\_{1}(x)\right)^2} d x
\end{aligned}
\\]
