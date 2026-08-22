## 二阶线性偏微分方程的分类

前面, 我们分别讨论了弦振动方程、热传导方程与拉普拉斯方程.
这三类方程虽然形状很特殊,但是在二阶线性偏微分方程中,它们却是三个典型的代表.
一般的二阶线性偏微分方程之间的共性与差异, 往往可以从对这三类方程的研究得到.
本节中, 我们就以关于这三类方程的知识为基础,
研究一般的二阶线性偏微分方程, 并对这三类方程的性质进行比较深人的总结与讨论.
在下面的讨论中, 常将二阶线性偏微分方程简称为二阶线性方程.

把所有自变数 (包括空间坐标和时间坐标) 依次记作 $x_1, x_2, \cdots, x_n$. 二阶偏微分方程如果可以表为

$$
\sum_{j=1}^n \sum_{i=1}^n a_{i j} u_{x_i x_j}+\sum_{i=1}^n b_i u_{x_i}+c u+f=0,
$$


其中 $a_{i j}, b_i, c, f$ 只是 $x_1, x_2, \cdots, x_n$ 的函数, 就叫作**线性**的方程.
前面导出的泛定方程以及许多常见的偏微分方程都是线性的.

如果泛定方程和定解条件都是线性的, 可以把定解问题的解看作几个部分的线性叠加,
 只要这些部分各自所满足的泛定方程和定解条件的相应的线性叠加正好是原来的泛定方程和定解条件就行.
 这叫作**叠加原理**.

 下面我们研究方程的分类并把方程化成标准形式.
 ### 两个自变数的方程分类

先研究两个自变数 $x$ 和 $y$ 的二阶线性偏微分方程

$$
a_{11} u_{x x}+2 a_{12} u_{x y}+a_{22} u_{y y}+b_1 u_x+b_2 u_y+c u+f=0,
$$

其中 $a_{11}, a_{12}, a_{22}, b_1, b_2, c, f$ 只是 $x$ 和 $y$ 的函数. 在以下的讨论中, 我们假定 $a_{11}, a_{12}, a_{22}, b_1, b_2, c, f$ 都是实数.
试作自变数的代换

$$
\left\{\begin{array} { l }
{ x = x ( \xi , \eta ) , } \\
{ y = y ( \xi , \eta ) , }
\end{array} \text { 即 } \left\{\begin{array}{l}
\xi=\xi(x, y), \\
\eta=\eta(x, y),
\end{array}\right.\right.
$$
代换的雅可比式

$$
\frac{\partial(\xi, \eta)}{\partial(x, y)} = \left|\begin{array}{ll}
        \xi_x & \xi_y \\
        \eta_x & \eta_y
        \end{array}\right|
\neq 0
$$

通过代换, $u\left(x, y_0\right)$ 成为 $\xi$ 和 $\eta$ 的函数.
这里, 还应把方程改用新的自变数 $\xi$ 和 $\eta$ 表出.
为此, 作如下计算:

$$
\left\{\begin{array}{l}
        u_x=u_{\xi} \xi_x+u_\eta \eta_x \\
        u_y=u_{\xi} \xi_y+u_\eta \eta_y
        \end{array}\right.
$$
$$
\left\{\begin{aligned}
        u_{x x} & =\left(u_{\xi \xi} \xi_x^2+u_{\xi \eta} \xi_x \eta_x+u_{\xi} \xi_{x x}\right)+\left(u_{\eta \xi} \eta_x \xi_x+u_{\eta \eta} \eta_x^2+u_\eta \eta_{x x}\right) \\
        & =u_{\xi \xi} \xi_x^2+2 u_{\xi \eta} \xi_x \eta_x+u_{\eta \eta} \eta_x^2+u_{\xi} \xi_{x x}+u_\eta \eta_{x x}, \\
        u_{x y} & =\left(u_{\xi \xi} \xi_x \xi_y+u_{\xi \eta} \xi_x \eta_y+u_{\xi} \xi_{x y}\right)+\left(u_{\eta \xi} \eta_x \xi_y+u_{\eta \eta} \eta_x \eta_y+u_\eta \eta_{x y}\right) \\
        & =u_{\xi \xi} \xi_x \xi_y+u_{\xi \eta} \cdot\left(\xi_x \eta_y+\xi_y \eta_x\right)+u_{\eta \eta} \eta_x \eta_y+u_{\xi} \xi_{x y}+u_\eta \eta_{x y}, \\
        u_{y y} & =\left(u_{\xi \xi} \xi_y^2+u_{\xi \eta} \xi_y \eta_y+u_{\xi} \xi_{y y}\right)+\left(u_{\eta \xi} \eta_y \xi_y+u_{\eta \eta} \eta_y^2+u_\eta \eta_{y y}\right) \\
        & =u_{\xi \xi} \xi_y^2+2 u_{\xi \eta} \xi_y \eta_y+u_{\eta \eta} \eta_y^2+u_{\xi} \xi_{y y}+u_\eta \eta_{y y} .
        \end{aligned}\right.
$$
把和代入得到采用新自变数 $\xi$ 和 $\eta$ 后的方程

$$
A_{11} u_{\xi \xi}+2 A_{12} u_{\xi \eta}+A_{22} u_{\eta \eta}+B_1 u_{\xi}+B_2 u_\eta+C u+F=0 \text {, }
$$

其中系数

$$
\left\{\begin{array}{l}A_{11}=a_{11} \xi_x^2+2 a_{12} \xi_x \xi_y+a_{22} \xi_y^2,
        \\
        A_{12}=a_{11} \xi_x \eta_x+a_{12}\left(\xi_x \eta_y+\xi_y \eta_x\right)+a_{22} \xi_y \eta_y,
        \\ A_{22}=a_{11} \eta_x^2+2 a_{12} \eta_x \eta_y+a_{22} \eta_y^2,
        \\ B_1=a_{11} \xi_{x x}+2 a_{12} \xi_{x y}+a_{22} \xi_{y y}+b_1 \xi_x+b_2 \xi_y,
        \\ B_2=a_{11} \eta_{x x}+2 a_{12} \eta_{x y}+a_{22} \eta_{y y}+b_1 \eta_x+b_2 \eta_y,
        \\ C=c
        \\ F=f\end{array}\right.
$$
方程仍然是线性的.
从 可以看到, 如果取一阶偏微分方程

$$
a_{11} z_x^2+2 a_{12} z_x z_y+a_{22} z_y^2=0,
$$

它的一个特解作为新自变数 $\xi$, 则 $a_{11} \xi_x^2+2 a_{12} \xi_x \xi_j+a_{22} \xi_y^2=0$,
从而 $A_{11}=$ 0 . 同理, 如果的另一特解作为新自变数 $\eta$, 则 $A_{22}=0$.
这样, 方程就得以化简.

一阶偏微分方程的求解可转化为常微分方程的求解. 事实上, 可改写为

$$
a_{11}\left(-\frac{z_x}{z_y}\right)^2-2 a_{12}\left(-\frac{z_x}{z_y}\right)+a_{22}=0
$$

如果把

$$
z(x, y)=\text { 常数 }
$$

当作定义隐函数 $y(x)$ 的方程, 则 $d y / d x=-z_x / z_y$, 可得

$$
a_{11}\left(\frac{d y}{d x}\right)^2-2 a_{12}
\frac{d y}{d x}+a_{22}=0 .
$$

常微分方程叫作二阶线性偏微分方程的**特征方程**,
特征方程的一般积分$\xi(x, y)= C_1$和$\eta(x, y)=C_2$叫做**特征线**.

特征方程可分为两个方程

$$
\begin{aligned}
        & \frac{d y}{d x}=\frac{a_{12}+\sqrt{a_{12}^2-a_{11} a_{22}}}{a_{11}}, \\
        & \frac{d y}{d x}=\frac{a_{12}-\sqrt{a_{12}^2-a_{11} a_{22}}}{a_{11}},
        \end{aligned}
$$

通常根据根号下的符号划分偏微分方程的类型:

$$
\left\{\begin{array}{l}
a_{12}^2-a_{11} a_{22}>0, \textbf { 双曲型; } \\
a_{12}^2-a_{11} a_{22}=0, \textbf { 抛物型; } \\
a_{12}^2-a_{11} a_{22}<0, \textbf { 椭圆型. }
\end{array}\right.
$$
方程的系数 $a_{11}, a_{12}$ 和 $a_{22}$ 可以是 $x$ 和 $y$ 的函数,
 所以, 一个方程在自变数的某一区域上属于某一类型, 在另一区域上可能属于另一类型.
 用容易验证

$$
A_{12}^2-A_{11} A_{22}=\left(a_{12}^2-a_{11} a_{22}\right)\left(\xi_x \eta_y-\xi_y \eta_x\right)^2,
$$

这是说, 作自变数的代换时, 方程的类型不变.


- **双曲型方程**

特征线方程的解为$\xi(x, y)=$ 常数, $\eta(x, y)=$ 常数.
取 $\xi=\xi(x, y)$ 和 $\eta=\eta(x, y)$ 作为新的自变数, 则 $A_{11}=0, A_{22}=0$. 从而自变数代换后的方程 成为


$$
u_{\xi \eta}=-\frac{1}{2 A_{12}}\left[B_1 u_{\xi}+B_2 u_\eta+C u+F\right]
$$

或者, 再作自变数代换


$$
\left\{\begin{array} { l }
{ \xi = \alpha + \beta , } \\
{ \eta = \alpha - \beta , }
\end{array}   \text { 即 } \left\{\begin{array}{l}
\alpha=\frac{1}{2}(\xi+\eta) \\
\beta=\frac{1}{2}(\xi-\eta)
\end{array}\right.\right.
$$
则方程  化为


$$
u_{\alpha \alpha}-u_{\beta \beta}=-\frac{1}{A_{12}}\left[\left(B_1+B_2\right) u_\alpha+\left(B_1-B_2\right) u_\beta+2 C u+2 F\right] .
$$

     或是双曲型方程的标准形式.
一维波动方程, 如弦振动方程和, 杆的纵振动方程, 电报方程等, 都是标准形式的双曲型方程.


- **抛物型方程**

由于 $a_{12}^2-a_{11} a_{22}=0$, 特征方程和变成一个方程:


$$
\frac{d y}{d x}=\frac{a_{12}}{a_{11}},
$$

它们只能给出一族实的特征线


$$
\xi(x, y)=\text { 常数, }
$$

则 $\xi=\xi(x, y)$ 是的解.
取 $\xi$ 作为新的自变数, 取与 $\xi(x, y)$ 无关的函数 $\eta=\eta(x, y)$ 作为另一新的自变数.
采用新自变数后, 将 $\xi_x / \xi_y=-d y / d x=$ $-a_{12} / a_{11}$ 和
$a_{12}= \pm \sqrt{a_{11} \cdot a_{22}}$ 代入, 得方程的前三个系数为


$$
\begin{aligned}
A_{11} & =\xi_y^2\left[a_{11}\left(\frac{\xi_x}{\xi_y}\right)^2+2 a_{12} \frac{\xi_x}{\xi_y}+a_{22}\right]=-\frac{\xi_y^2}{a_{11}}\left[a_{12}^2-a_{11} \cdot a_{22}\right]=0 \\
A_{12} & =\xi_y\left[a_{11}\left(\frac{\xi_x}{\xi_y}\right)^2 \eta_y+a_{12}\left(\frac{\xi_x}{\xi_y} \eta_y+\eta_x\right)+a_{22} \eta_y\right] \\
& =-\frac{\xi_y \eta_y}{a_{11}}\left[a_{12}^2-a_{11} \cdot a_{22}\right]=0 \\
A_{22} & =\eta_y^2\left[a_{11}\left(\frac{\eta_x}{\eta_y}\right)^2+2 a_{12} \frac{\eta_x}{\eta_y}+a_{22}\right]=\eta_y^2\left[\sqrt{a_{11}}\left(\frac{\eta_x}{\eta_y}\right) \pm \sqrt{a_{22}}\right]^2 .
\end{aligned}
$$

可见, 只要取 $\eta(x, y)$ 使 $\eta_x / \eta_y \neq \sqrt{a_{22}} / \sqrt{a_{11}}$, 即 $\eta$ 不满足特征方程,
则 $A_{22} \neq 0$, 从而自变数代换后的方程成为


$$
u_{\eta \eta}=-\frac{1}{A_{22}}\left[B_1 u_{\xi}+B_2 u_\eta+C u+F\right] .
$$

这是抛物型方程的标准形式. 一维输运方程, 如扩散方程, 热传导方程等, 都是标准形式的抛物型方程.

- **椭圆型方程**

各给出一族复数的特征线

$$
\xi(x, y)=\text { 常数, } \eta(x, y)=\text { 常数, }
$$

而且 $\eta=\xi^*$. 取 $\xi=\xi(x, y)$ 和 $\eta=\eta(x, y)=\xi^*(x, y)$ 作为新的自变数,
则 $A_{11}=0, A_{22}=0$, 从而自变数代换后的方程成为

$$
u_{\xi \eta}=-\frac{1}{2 A_{12}}\left[B_1 u_{\xi}+B_2 u_\eta+C u+F\right] .
$$

注意这里的 $\xi$ 和 $\eta$ 是复变数. 通常又作代换

$$
\left\{\begin{array} { l }
{ \xi = \alpha + \mathrm{i} \beta , } \\
{ \eta = \alpha - \mathrm{i} \beta , }
\end{array}   \text { 即 } \left\{\begin{array}{l}
\alpha=\Re \xi=\frac{1}{2}(\xi+\eta), \\
\beta=\Im \xi=\frac{1}{2 \mathrm{i}}(\xi-\eta) .
\end{array}\right.\right.
$$
则方程化为

$$
u_{\alpha \alpha}+u_{\beta \beta}=-\frac{1}{A_{12}}\left[\left(B_1+B_2\right) u_\alpha+\mathrm{i}\left(B_2-B_1\right) u_\beta+2 C u+F\right] .
$$

 或  是椭圆型方程的标准形式.
平面稳定场方程, 如稳定浓度分布, 稳定温度分布, 静电场方程, 无旋恒定电流场方程, 无旋定常流动方程等都是标准形式的椭圆型方程.

## 定解条件

上面所导出的弦振动方程包含有未知函数 $u(x, t)$ 和它的关于自变量的偏导数,
所以是偏微分方程.对于一个偏微分方程来说, 如果有一个函数 $u(x, t)$,具有方程中所需要的各阶连续偏导数,
且将它代入方程时能使方程成为恒等式, 就称这个函数为该方程的解.列出微分方程以后, 目的就是要从微分方程中求得解或研究解的性质.
例如, 为了了解弦的振动情况, 就应该设法求出相应的弦振动方程的解.

我们看到, 弦振动方程 描述了弦作微小横振动时位移函数 $u(x, t)$ 所应满足的一般性规律,
但仅仅利用它还不能完全确定所考察弦的运动状况.这是因为弦的运动还与其初始状态以及边界所处的状况有关,因此还得给出一些其他条件.
在上述弦振动问题中, 弦的两端被固定在 $x=0$ 及 $x=l$ 两点, 因此有

$$
u(0, t)=0,   u(l, t)=0,
$$

称为**边界条件**(boundary conditions).此外, 设弦在初始时刻 $t=0$ 时的位置和速度为

$$
u(x, 0)=\varphi(x),   \frac{\partial u(x, 0)}{\partial t}=\psi(x)  (0 \leqslant x \leqslant l),
$$

称为**初始条件**(initial conditions).边界条件与初始条件总称为定解条件.把弦振动方程
和定解条件,结合起来, 就得到如下的定解问题:

$$
\left\{\begin{array}{l}
	\frac{\partial^2 u}{\partial t^2}-a^2 \frac{\partial^2 u}{\partial x^2}=f(x, t), \\
	t=0: u=\varphi(x), \frac{\partial u}{\partial t}=\psi(x), \\
	x=0:   u=0, \\
	x=l:   u=0 .
\end{array}\right.
$$
要在区域 $(0 \leqslant x \leqslant l, t \geqslant 0)$ 上求上述定解问题的解,
就是要求这样的连续函数 $u=u(x, t)$, 它在区域 $0<x<l, t>0$ 中满足波动方程;
在 $x$ 轴 $(t=0)$ 一段区间 $0 \leqslant x \leqslant l$ 上满足初始条件,
 并在边界 $x=0$及$x=l$上分别满足边界条件.

一般称形如 的边界条件为**第一类边界条件**, ( 又称狄利克雷(Dirichlet) 边界条件).
对于弦振动方程的边界条件通常还可以有以下两种:

(a) 弦的一端 (例如 $x=0$ ) 处于自由状态, 即可以在垂直于 $x$ 轴的直线上自由滑动, 未受到垂直方向外力.
在边界右端的张力的垂直方向分量是 $T \frac{\partial u}{\partial x}$, 得出此时应成立

$$
\left.\frac{\partial u}{\partial x}\right|_{x=0}=0 .
$$

也可以考虑更普遍的边界条件

$$
\left.\frac{\partial u}{\partial x}\right|_{x=0}=\mu(t) ,
$$

其中 $\mu(t)$ 是 $t$ 的已知函数.这种边界条件称为**第二类边界条件** (又称诺伊曼 (Neumann) 边界条件).

(b)在应用上还会遇到另一种情形.将弦的一端固定在弹性支承上,也就是说此时支承的伸缩符合胡克定律.
如果支承原来的位置为 $u=0$, 则 $u$ 在端点的值表示支承在该点的伸长.例如在 $x=l$ 的一端,
弦对支承拉力的垂直方向分量为 $-T \frac{\partial u}{\partial x}$, 由胡克定律知

$$
-\left.T \frac{\partial u}{\partial x}\right|_{x=l}=\left.k u\right|_{x=l},
$$

其中 $k$ 为弹性系数. 因此在弹性支承的情形,边界条件归结为

$$
\left.\left(\frac{\partial u}{\partial x}+\sigma u\right)\right|_{x=l}=0
$$

其中 $\sigma=\frac{k}{T}$ 是已知正数.在数学中也可以考虑更普遍的边界条件

$$
\left.\left(\frac{\partial u}{\partial x}+\sigma u\right)\right|_{x=l}=v(t),
$$

其中 $v(t)$ 是 $t$ 的已知函数.这种边界条件称为**第三类边界条件**.

下面我们再介绍几个概念. 一个偏微分方程所含有的未知函数最高阶导数的阶数称为这个偏微分方程的**阶**, 例如弦振动方程就是一个二阶偏微分方程.
如果方程对未知函数及其各阶导数总体来说是线性的,则称这个方程是**线性方程**. 否则称这个方程是非线
性方程.进一步, 如果方程对未知函数的所有最高阶导数总体来说是线性的, 则称它为**拟线性方程**.例如,方程

$$
\frac{\partial u}{\partial t}+u \frac{\partial u}{\partial x}=0
$$

是一阶拟线性方程.如果非线性方程中方程对未知函数的最高阶导数不是线性的, 则称它为**完全非线性方程**.例如, 方程

$$
\left(\frac{\partial u}{\partial x}\right)^2+\left(\frac{\partial u}{\partial y}\right)^2=u
$$

就是一阶完全非线性方程.
我们看到, 包含$f(x, t)$这样的方程称为**非齐次方程**,而 $f\equiv 0$的方程称为**齐次方程**.
类似地,边界条件$u(0,t) = 0, u(l, t) = 0$ 称为**齐次边界条件**,
相应地, 若边界条件为 $\left.u\right|_{1=0}=\mu_1(t),\left.u\right|_{x^{-1}}=\mu_2(t)$, 则称为**非齐次边界条件**.
同样, 初始条件 $u(x, 0) = \varphi(x), u'(x, 0) = \psi(x)$ 称为**非齐次初始条件**,
而对应于 $\varphi \equiv \psi \equiv 0$ 的初始条件称为**齐次初始条件**.
