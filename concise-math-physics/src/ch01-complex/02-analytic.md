### 区域的概念

在解析函数论中, 函数的定义域或者值域不是一般的点集,而是满足一定条件的点集,称为**区域**,用 \\(B\\) 表示.
为了说明区域的概念, 首先介绍邻域、内点、外点以及边界点的概念.

- **邻域**   以复数 \\(z_0\\) 为圆心, 以任意小正实数 \\(\varepsilon\\) 为半径作一圆, 则圆内所有 点的集合称为 \\(z_0\\) 的邻域.

- **内点**   若 \\(z_0\\) 及其邻域均属于点集 \\(Z\\), 则称 \\(z_0\\) 为该点集的内点.

- **外点**   若 \\(z_0\\) 及其邻域均不属于点集 \\(Z\\), 则称 \\(z_0\\) 为该点集的外点.

- **边界点**    若在 \\(z_0\\) 的每个邻域内, 既有属于 \\(Z\\) 的点, 也有不属于 \\(Z\\) 的点,
        则称 \\(z_0\\) 为该点集的边界点, 它既不是 \\(Z\\) 的内点, 也不是 \\(Z\\) 的外点. 边界点的 全体称为边界线.

现在介绍区域的概念.

**区域**   直观地说,  区域就是宗量 \\(z\\) 在复数平面上的取值范围,用\\(B\\)表示.
确切地说,区域是指满足下列两个条件的点集:



- 全由内点组成;

- 具有连通性, 即点集中的任意两点都可以用一条折线连接起来, 且 折线上的点全都属于该点集.


**闭区域**   区域\\(B\\) 及其边界线所组成的点集称为闭区域,以 \\(\bar{B\\) 表示.区域可以是各种各样的, 例如圆形域及环形域(如图所示).
圆形域可以用不等式 \\(\left|z-z_0\right|<r\\) 来表示, 式中 \\(z_0\\) 为圆心, \\(r\\) 为半径;
环形域可以用 \\(a<\left|z-z_0\right|<b\\) 来表示, \\(z_0\\) 为环心, 式中 \\(a\\) 为内半径, \\(b\\) 为外半径.
 若将其中的 "<" 换成 \\(\leqslant\\), 则这两个式子分别表示闭圆域和闭环域.

### 复变函数定义

> **定义** {复变函数}
存在复数平面的点集\\(Z\\),每一点\\(z\in Z\\)有一个或多个复数值\\(w\\)与之对应, 该对应规则记为\\(f\\), 则称\\(w\\)为\\(z\\)的**复变函数**, 简称**复函数**.
记作

\\[
w = f(z), z\in Z .
\\]

\\(z\\)称为\\(w\\)的宗量,定义域为\\(Z\\).

任意一个复变函数\\(f(z)\\),\\(z=x + \mathrm{i} y\\),我们可以写称实部和虚部的组合,

\\[
f(z) = u(x,y) +\mathrm{i}   v(x,y) ,
\\]

其中\\(u(x,y), v(x,y)\\)为纯实函数.它们可以类似的写成

\\[
\Re f(z) = u(x,y),   \Im f(z) = v(x,y) ,
\\]

\\(f(z)\\)的复共轭为\\(u(x,y) - \mathrm{i}   v(x,y)\\).取决于\\(f(z)\\),二者可能相等也可能不等.

这里我们列举一些常见复变函数.


- 多项式:


\\[
a_0 + a_1 z + a_2 z^2 + \cdots + a_n z^n ,   n\in \mathbb{Z}^+ ,
\\]


- 有理分式:


\\[
\frac{a_0 + a_1 z + a_2 z^2 + \cdots + a_n z^n}{{b_0 + b_1 z + b_2 z^2 + \cdots + b_m z^m}} ,    n,m\in \mathbb{Z}^+ ,
\\]


- 根式:


\\[
(z-a)^{m/n} ,    n,m\in \mathbb{Z}^+ ,
\\]


- 对数、指数


\\[
\ln z = \ln |z| + \mathrm{i} \Arg z,   z^s = e^{s\ln z} ,
\\]


- 正余弦,正余切函数


\\[
\sin z , \cos z , \tan z, \cot z ,
\\]


- 双曲正余弦, 双曲正余切函数


\\[
\sinh z , \cosh z , \tanh z, \coth z  .
\\]

以上所有出现的常数均为复数.

> **例** 验证

\\[
|\sin z|=\frac{1}{2} \sqrt{\left(e^{2 y}+e^{-2 y}\right)+2\left(\sin ^2 x-\cos ^2 x\right)} .
\\]

> **解** 由正弦函数定义得


\\[
\begin{aligned}
        \sin z &= \frac{e^{\mathrm{i} z} - e^{-\mathrm{i} z}}{2\mathrm{i}}
        \\\\
        & = \frac{e^{\mathrm{i} x - y} - e^{-\mathrm{i} x + y}}{2\mathrm{i}}
        \\\\
        & = \frac{1}{2\mathrm{i}}\left( e^{-y} (\cos x + \mathrm{i} \sin x ) - e^{y} (\cos x - \mathrm{i} \sin x ) \right)
        \\\\
        & = \frac{1}{2\mathrm{i}} \left( \cos x (e^{-y} - e^{y}) + \mathrm{i} \sin x (e^{-y} + e^{y}) \right)
\end{aligned}
\\]

取模后可得,


\\[
\begin{aligned}
        |\sin z | &= \frac{1}{2}\sqrt{ \cos^2x (e^{2y} + e^{-2y} -2) + \sin^2 x (e^{2y} + e^{-2y} +2) }
        \\\\
        &=\frac{1}{2}\sqrt{\left(e^{2 y}+e^{-2 y}\right)+2\left(\sin ^2 x-\cos ^2 x\right)}
\end{aligned}
\\]

可见,与实函数不同的是,\\(|\sin z|\\)的取值完全可以大于\\(1\\).

双曲函数(hyperbolic functions)为三角函数(trigonometric functions)的复数类比.
许多同三角函数一样的等式和积分上都可以类似的应用在双曲函数上.
通过复数的引入,我们很容易定义三角函数,如正余弦函数(sine/cosine function)可以表示为互为共轭的指数函数的和差

\\[
\begin{aligned}
\cos \theta = \frac{e^{\mathrm{i} \theta} + e^{ -\mathrm{i} \theta} }{2}
\\\\
\sin \theta = \frac{e^{\mathrm{i} \theta} - e^{ -\mathrm{i} \theta} }{2\mathrm{i}}
\end{aligned}
\\]

双曲正余函数(hyperbolic sine/cosine function)表达为

\\[
\begin{aligned}
\cosh \theta &= \frac{e^{\theta} + e^{ - \theta} }{2}
\\\\
\sinh \theta &= \frac{e^{\theta} - e^{ - \theta} }{2} .
\end{aligned}
\\]

比较两组方程可以得到

\\[
\begin{aligned}
\cosh iz &= \cos z
\\\\
\sinh iz &= i \sin z.
\end{aligned}
\\]

不难验证下面两个等式成立

\\[
\begin{aligned}
& \sin (x+i y)=\sin x \cosh y+i \cos x \sinh y, \\\\
& \cos (x+i y)=\cos x \cosh y-i \sin x \sinh y.
\end{aligned}
\\]

对于三角函数,有一很重要的de Moivre(棣莫弗)公式.我们可以用两种方式表示\\(\exp(\mathrm{i} n \theta)\\),于是有

\\[
\cos n \theta + \mathrm{i} \sin n\theta = (\cos \theta + i \sin \theta)^n  .
\\]

于是可以验证三角函数的倍角公式

\\[
\sin(2\theta) = 2\sin\theta \cos\theta,   \cos (2\theta) = \cos^2\theta - \sin^2\theta .
\\]

> **例** 应用de Moivre公式计算 \\(\sin(5\theta)\\).

> **解** 考虑复数 \\(z = \cos\theta + i\sin\theta\\).根据de Moivre定理,计算 \\(z^5\\)：


\\[
z^5 = (\cos\theta + i\sin\theta)^5 = \cos(5\theta) + i\sin(5\theta)
\\]


展开 \\((\cos\theta + i\sin\theta)^5\\) 使用二项式定理并简化每一项：：



\\[
\begin{aligned}
(\cos\theta + i\sin\theta)^5  &= \sum_{k=0}^{5} \binom{5}{k} (\cos\theta)^{5-k} (i\sin\theta)^k \\\\
        &= \binom{5}{0} \cos^5\theta + \binom{5}{1} \cos^4\theta(i\sin\theta) + \binom{5}{2} \cos^3\theta(i\sin\theta)^2
        \\\\
        & & +  \binom{5}{3} \cos^2\theta(i\sin\theta)^3 +  \binom{5}{4} \cos\theta(i\sin\theta)^4 + \binom{5}{5}(i\sin\theta)^5
        \\\\
        &=  \cos^5\theta + 5i\cos^4\theta \sin\theta - 10\cos^3\theta \sin^2\theta - 10i\cos^2\theta \sin^3\theta + 5\cos\theta \sin^4\theta + i\sin^5\theta
\end{aligned}
\\]




将实部和虚部分离：



\\[
\cos(5\theta) = \cos^5\theta - 10\cos^3\theta \sin^2\theta + 5\cos\theta \sin^4\theta
\\]




\\[
\sin(5\theta) = 5\cos^4\theta \sin\theta - 10\cos^2\theta \sin^3\theta + \sin^5\theta
\\]


利用幂次公式,\\(\cos^2\theta = 1 - \sin^2\theta\\) 和 \\(\sin^2\theta = 1 - \cos^2\theta\\),我们可以将 \\(\sin(5\theta)\\) 表示为 \\(\sin\theta\\) 和 \\(\cos\theta\\) 的函数：



\\[
\sin(5\theta) = 5\cos^4\theta \sin\theta - 10\cos^2\theta \sin^3\theta + \sin^5\theta
\\]


进一步化简 \\(\cos^4\theta = (1 - \sin^2\theta)^2\\) 和 \\(\cos^2\theta = 1 - \sin^2\theta\\),我们得到：



\\[
\sin(5\theta) = 5(1 - \sin^2\theta)^2\sin\theta - 10(1 - \sin^2\theta)\sin^3\theta + \sin^5\theta
\\]


这就是 \\(\sin(5\theta)\\) 以 \\(\sin\theta\\) 的表示形式.

最终,简化表达式：



\\[
\sin(5\theta) = 5\sin\theta - 20\sin^3\theta + 16\sin^5\theta
\\]


因此,\\(\sin(5\theta)\\) 通过de Moivre公式可以表示为 \\(\sin\theta\\) 的函数：


\\[
\sin(5\theta) = 5\sin\theta - 20\sin^3\theta + 16\sin^5\theta.
\\]



利用\\(\cos \theta = \sqrt{1 - \sin ^2 \theta }\\)(取正),可以得到

\\[
e^{\mathrm{i} \theta} = \sqrt{ 1 - \sin ^2 \theta } + \mathrm{i} \sin \theta .
\\]


令\\(\sin \theta = z\\),\\(\theta = \sin^{-1 (z)\\),对两边同时求对数得到

\\[
\sin^{-1} (z) = -\mathrm{i} \ln \left[ \mathrm{i} z + \sqrt{1-z^2} \right]
\\]

这样我们便通过对数函数表示出三角函数的反函数.
类似的,

\\[
\begin{array}{cc}
\sin ^{-1}(z)=-i \ln \left[i z+\sqrt{1-z^2}\right],   \tan ^{-1}(z)=\frac{i}{2}[\ln (1-i z)-\ln (1+i z)], \\\\
\sinh ^{-1}(z)=\ln \left[z+\sqrt{1+z^2}\right],   \tanh ^{-1}(z)=\frac{1}{2}[\ln (1+z)-\ln (1-z)] .
\end{array}
\\]

> **例** 证明


\\[
\tanh \frac{z}{2}=\frac{\sinh x+i \sin y}{\cosh x+\cos y} .
\\]

> **解** 根据双曲正切函数的定义

\\[
\begin{aligned}
\tanh \frac{z}{2} &= \frac{\sinh \frac{z}{2} }{ \cosh \frac{z}{2}}
\\\\
&= \frac{e^{\frac{z}{2}} - e^{-\frac{z}{2}}}{e^{\frac{z}{2}} + e^{-\frac{z}{2}}}
\\\\
&= \frac{e^{z} - 1}{e^{z} + 1}
\\\\
&= \frac{e^{x+\mathrm{i} y } -1 } { e^{x + \mathrm{i} y } + 1}
\\\\
&=\frac{e^{\mathrm{i} y } -e^{-x} } { e^{\mathrm{i} y } + e^{-x}}
\end{aligned}
\\]


分子分母同乘以分母的复共轭可得

\\[
\begin{aligned}
&=\frac{e^{\mathrm{i} y } -e^{-x} } { e^{\mathrm{i} y } + e^{-x}} \frac{e^{-\mathrm{i} y } + e^{-x}} { e^{-\mathrm{i} y } + e^{-x}}
\\\\
&=\frac{ 1 - e^{-2x} + 2 \mathrm{i} \sin y e^{-x}}{1+ e^{-2x} + 2 \cos y e^{-x} }
\\\\
&= \frac{\sinh x + \mathrm{i} \sin y} {\cosh x + \cos y} .
\end{aligned}
\\]

证毕.

此外,类似于三角函数,我们有以下双曲函数

\\[
\begin{aligned}
\tanh z & =\frac{\sinh z}{\cosh z}=\frac{e^z-e^{-z}}{e^z+e^{-z}}, \\\\
\operatorname{sech} z & =\frac{1}{\cosh z}=\frac{2}{e^z+e^{-z}}, \\\\
\operatorname{cosech} z & =\frac{1}{\sinh z}=\frac{2}{e^z-e^{-z}}, \\\\
\coth z & =\frac{1}{\tanh z}=\frac{e^z+e^{-z}}{e^z-e^{-z}} .
\end{aligned}
\\]

### 导数

首先,我们来讨论一下函数的极限和连续性问题.

> **定义** 设\\(w=f(z)\\)在\\(z_0\\)的邻域有定义,对于任意
\\(\epsilon > 0\\),存在\\(\delta > 0\\),使得\\(|z-z_0| < \delta\\)时,有

\\[
|f(z) - w_0| < \epsilon ,
\\]

称\\(z\to z_0\\)时\\(w_0\\)为\\(f(z)\\)的**极限**,记为

\\[
\lim_{z\to z_0} f(z) = w_0 .
\\]

当\\(z\\)以任意方式趋近\\(z_0\\)时都有\\( \lim_{z\to z_0 f(z) = w_0\\),称\\(f(z)\\)在\\(z_0\\)点**连续**.
如果\\(f(z)\\) 在\\(z_0=x_0 + \mathrm{i} y_0\\)点连续,可以等价为

\\[
\begin{aligned}
\lim_{\substack{x\to x_0\\y\to y_0}} \left(u(x,y), v(x,y)\right) = \left(u(x_0, y_0), v(x_0, y_0)\right) .
\end{aligned}
\\]

复变函数的导数定义同实函数一样,定义为

\\[
\begin{aligned}
f'(z) = \frac{df}{dz} \\\\
\equiv\lim_{\Delta z \to 0} \frac{\Delta w} {\Delta z} = \lim_{\Delta z\to 0} \frac{f(z+\Delta z) - f(z) } {(z+\Delta z ) - z}
\end{aligned}
\\]

这里的前提条件是该极限与\\(\Delta z \to 0\\)的方式无关.该极限为函数\\(f(z)\\)在\\(z\\)点的导数.通过该定义,实函数的求导公式对于复变函数同样试用,如
\\((f+g)' = f' + g', (fg)' =f'g + fg'\\)等.与实变函数求导不同的是,复变函数导数存在条件是\\(\Delta z\\)以任意方式趋于\\(0\\),因而可导条件的要求比较严格.

按照图)两种方式逼近\\(z_0\\),可以得到

\\[
\begin{aligned}
\lim _{\Delta z \rightarrow 0} \frac{\Delta f}{\Delta z} &=\lim _{\Delta x \rightarrow 0}\left(\frac{\Delta u}{\Delta x}+i \frac{\Delta v}{\Delta x}\right)=\frac{\partial u}{\partial x}+i \frac{\partial v}{\partial x},
\\\\
\lim _{\Delta z \rightarrow 0} \frac{\Delta f}{\Delta z} &=\lim _{\Delta y \rightarrow 0}\left(-i \frac{\Delta u}{\Delta y}+\frac{\Delta v}{\Delta y}\right)=-i \frac{\partial u}{\partial y}+\frac{\partial v}{\partial y}
\end{aligned}
\\]

于是,令实部虚部分别相等,即

\\[
\begin{cases}
        \frac{\partial u}{\partial x}=\frac{\partial v}{\partial y} \\\\
        \frac{\partial v}{\partial x}=-\frac{\partial u}{\partial y} .
\end{cases}
\\]

这就是著名的**柯西-黎曼条件**(Cauchy-Riemann conditions)或**柯西-黎曼方程**,是复变函数可导的必要条件,但不是充分条件.
下面我们证明:若\\(u(x,y), v(x,y)\\)偏微分存在且连续,并满足柯西-黎曼条件,则\\(f(z)\\)可导.

对于极坐标系,我们也可以得到相应的柯西-黎曼方程,

\\[
\left\{\begin{array}{l}
\frac{\partial u}{\partial \rho}=\frac{1}{\rho} \frac{\partial v}{\partial \varphi} \\\\
\frac{1}{\rho} \frac{\partial u}{\partial \varphi}=-\frac{\partial v}{\partial \rho}
\end{array}\right.
\\]
其中两种推导作为习题.

利用\\(z,\bar{z}\\)的关于\\(x,y\\)的定义,不难有

\\[
d z=d x+i d y,   d \bar{z}=d x-i d y
\\]

可得到

\\[
\frac{\partial}{\partial z}=\frac{1}{2}\left(\frac{\partial}{\partial x}-i \frac{\partial}{\partial y}\right),   \frac{\partial}{\partial z}=\frac{1}{2}\left(\frac{\partial}{\partial x}+i \frac{\partial}{\partial y}\right)
\\]

因此, 柯西黎曼方程意味着

\\[
\frac{\partial f}{\partial \bar{z}}=0.
\\]

\\(f\\)的全微分 仅由关于 \\(z\\)的微分给出, 即

\\[
\mathrm{d}f \equiv \frac{\partial f}{\partial z} \mathrm{~d} z+\frac{\partial f}{\partial \bar{z}} \mathrm{~d} \bar{z}=\frac{\partial f}{\partial z} \mathrm{~d} z
\\]

这实际上就是解析的本质.

### 解析函数

> **定义** 若函数 \\(f(z)\\) 在点 \\(z_0\\) 及其邻域上处处可导, 则称 \\(f(z)\\) 在 \\(z_0\\) 点解析.\\
 又若 \\(f(z)\\) 在区域 \\(B\\) 上每一点都解析, 则称 \\(f(z)\\) 是区域 \\(B\\) 上的解析函数.


 可见, 函数若在某一点解析, 则必在该点可导. 反之却不一定成立. 若在全复数域上解析,我们
 称其为**完全函数**(entire function).
 若\\(f(z)\\)在某点\\(z_0\\)不可导,\\(z_0\\)称为\\(f(z)\\)的一个**奇点**(singular point).



> **例** 说明\\(f(z)=z^2\\)是完全函数,而\\(f(z)=|z|^2\\)的奇点数有无数个.

> **解** 首先,\\(f(z) =z^2 = (x^2 - y ^2) + \mathrm{i} 2 x y\\),实部和虚部分别为\\(u(x,y) = x^2 - y^2, v(x,y)=2x y\\),
连续条件和柯西-黎曼条件在全实数域均满足,可知\\(f(z)\\)在全复平面每点均可导.因此,\\(f(z)=z^2\\)是完全函数.
类似的,我们可以知道\\(f(z)=z^n, n\in N\\)的也是完全函数.\\
接着,我们来看\\(f(z) = |z|^2 = (x^2 + y ^2)\\),可以知道只有在\\((0,0)\\)处满足可导条件,其他点均不解析.因此,\\(f(z)=|z|^2\\)的奇点数有无数个.


 解析函数实际上有着深刻的内涵. 其中要义之一就是其实部和虚部(统一用\\(\psi\\)来表示)都必须满足二维的拉普拉斯方程即


\\[
\frac{\partial^2 \psi}{\partial x^2}+\frac{\partial^2 \psi}{\partial y^2}=0
\\]

上式可以利用柯西-黎曼条件进行验证,作为作业.\\(u,v\\)被成为调和函数或谐函数(harmonic functions)(注意不要同球谐函数spherical harmonics混淆).

第二要义就是,满足\\(u(x,y) = C_1\\)和\\(v(x,y)= C_2\\)的曲线为正交曲线族.
再次利用柯西-黎曼条件,可以验证梯度\\(\nabla u \\)和\\(\nabla v\\)正交,

\\[
\nabla u \cdot \nabla v = \frac{\partial u}{\partial x}
\frac{\partial v}{\partial x}+\frac{\partial u}{\partial y} \frac{\partial v}{\partial y}=0 ,
\\]

由于\\(\nabla u, \nabla v\\)代表两曲线的法向矢量,因此两曲线是正交的. 例如, \\(f(z) = z^2\\)的实部和虚部分别为

\\[
u(x,y) = x^2 - y^2,   v(x,y) = 2xy .
\\]

可以画出\\(u(x,y) = C_1\\)和\\(v(x,y)= C_2\\)的曲线,如图所示.
其中蓝色曲线为\\(u(x,y) = C_1\\),红色曲线为\\(v(x,y)=C_2\\). 可以看到,两曲线在交点处是正交的.

第三要义就是,当解析函数的实部(或虚部)给定,可以根据柯西-黎曼条件求解相应的虚部(或实部),进而确定该解析函数.
如已知实部,可以发现

\\[
d v = \frac{\partial v}{\partial x} dx + \frac{\partial v}{\partial y} dy = -\frac{\partial u}{\partial y} dx + \frac{\partial u}{\partial x} dy
\\]

可以验证

\\[
\frac{\partial }{\partial y} \left( - \frac{\partial u}{\partial y} \right) = \frac{\partial }{\partial x} \left( \frac{\partial u}{\partial x} \right) ,
\\]

可知, \\(dv\\)是一全微分, \\(v = \int dv\\).

> **例** 解析函数实部为\\(u(x,y) = x^2 - y^2\\),求解该解析函数.

> **解** 首先,可以验证\\(u\\)为调和函数.然后,利用柯西-黎曼条件可得

\\[
\frac{\partial u}{\partial x } = 2x,   \frac{\partial u}{\partial y } = -2y  ,
\\]

因此

\\[
d v = \frac{\partial v}{\partial x } dx + \frac{\partial v}{\partial y } dy = 2y dx + 2x dy .
\\]

该积分与路径无关,可以用几种方法得到.容易得到\\(v(x,y) = 2xy + C\\), \\(C\\)为积分常数.解析函数为\\(f(z)=x^2 - y^2 + \mathrm{i} (2x y + C) = z^2 + \mathrm{i} C\\).

### 多值函数

在定义解析函数的时候,其中一个条件就是要求函数为单值的.
然而除了单值函数外,还有许多多值函数,例如对数函数和根式函数等.
碰巧的是,解析函数的许多性质仍然可以应用到多值函数上,但前提是要到
多值函数的|**支点**  (branch points).

一般来说,多值函数\\(f(z)\\),若\\(z\\)绕某点一周,\\(f(z)\\)不会返回原值,
我们称该点为多值函数的**支点**.若\\(z\\)绕该支点\\(n\\)周,\\(f(z)\\)复原,
则称该点为多值函数\\(f(z)\\)的\\(n\\)阶支点.
以\\(f(z) = z^{1/2}\\)为例,我们来介绍多值函数的性质.

易知,

\\[
f(z) = \sqrt{r} e^{\mathrm{i} \frac{1}{2}  \Arg z} =  \sqrt{r} e^{\mathrm{i} \left( \frac{1}{2} \arg z + n \pi \right)},
\\]

于是,对于\\(n= 2k\\)和\\(n=2k+1\\),\\(f(z)\\)有两个值.

\\[
\left\{\begin{aligned}
f_1(z) & =\sqrt{r}  e^{\mathrm{i}(\arg z) / 2} \\\\
f_2(z) & =-\sqrt{r}  e^{\mathrm{i}(\arg z) / 2} \\\\
\end{aligned}\right.
\\]
这两个函数成为\\(f(z)= z^{1/2}\\)的两个**单值分支**.可以发现,
取任意包含\\(z=0\\)的闭合路径(或围道)\\(C\\),沿着该路径绕行一圈,辐角增加\\(2\pi\\),
可以发现\\(f(z)\\)从其一单值分支\\(f_1(z)\\)进入到另一单值分支\\(f_2(z)\\).
若绕行两周,则回归原分支\\(f_1(z)\\).根据定义,可知\\(z=0\\)为该函数的支点,且
为2阶支点.

> **注** 注意这与梁昆淼的说法不同.

此外,利用变换\\(z=1/t\\),可以发现\\(z=\infty\\)也是2阶支点.

为了能够像对待单值函数一样对待多值函数,我们需要定义复平面Argand diagram
中的**割线**(branch cut).割线可以被认为是复平面里一个人为
设定的不可穿过的壁垒.割线的存在,使得我们能够避免形成一个包含支点的路径,
这样一来,在割线之间多值函数仍然是单值的.

对于\\(f(z)=z^{1/2}\\),可以取任意一条过\\(z=0\\)的指向\\(|z|=\infty\\)的割线,使得
无法形成包含\\(z=0\\)支点的闭合路径.按照约定,我们通常沿着实轴或者虚轴取这样的割线.
由于割线的存在,辐角被限制在\\((0,2\pi)\\),因而\\(f(z)\\)保持单值.
割线的取法多种多样,正确连接各支点,同时规定辐角的值即可.

> **例** 找出函数\\(f(z) = \sqrt{z^2 + 1}\\)的支点,并取合适的割线.

> **解** 不难看出,

\\[
f(z) = \sqrt{z + \mathrm{i}} \sqrt{z-\mathrm{i}} .
\\]

前面我们了解了\\(f(z)=\sqrt{z}\\)的支点为\\(z=0\\),不难看出来,\\(z=\pm \mathrm{i}\\)也会成为
该函数的两个支点.
如图所示,令

\\[
z - i = r_1 e^{\mathrm{i} \theta_1 }
z + i = r_2 e^{\mathrm{i} \theta 2}
\\]

我们有

\\[
f(z) = \sqrt{r_1 r_2} e^{\mathrm{i} \frac{1}{2} (\theta_1 + \theta_2)}.
\\]

如果我们做以下几种情况的闭合路径\\(C\\),我们会得到不同的情况.若\\(C\\)


- [(i)] 不包含两个支点,那么\\(\theta_1 \to \theta_1, \theta_2 \to \theta_2\\), 于是\\(f(z)\to f(z)\\);

- [(ii)] 包含\\(\mathrm{i}\\)但不含\\(-\mathrm{i}\\),那么\\(\theta_1 \to \theta_1 + 2\pi, \theta_2 \to \theta_2\\), 于是\\(f(z)\to - f(z)\\);

- [(iii)] 包含\\(-\mathrm{i}\\)但不含\\(\mathrm{i}\\),那么\\(\theta_1 \to \theta_1, \theta_2 \to \theta_2  + 2\pi\\), 于是\\(f(z)\to - f(z)\\);

- [(iv)] 包含\\(\pm \mathrm{i}\\)两个支点,那么\\(\theta_1 \to \theta_1  + 2\pi, \theta_2 \to \theta_2  + 2\pi\\), 于是\\(f(z)\to  f(z)\\).

因此,为了阻止闭合路径绕支点完成完整的回路,我们必须选择合适的割线.图中连接\\(\pm \mathrm{i}\\)的标红线段是一种选择.
