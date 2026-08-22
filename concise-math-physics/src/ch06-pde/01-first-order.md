## 一阶常微分方程

下面讨论一阶微分方程

\\[
y' = f(x,y),
\\]

或写成对称形式的一阶微分方程

\\[
p(x,y) dx + q(x,y) dy = 0,
\\]

这里\\(f(x,y), p(x,y), q(x,y)\\)均表示含\\(x,y\\)两个变量的解析表达式. 当微分方程写为这种对称形式时,
变量\\(x,y\\)处于平等地位, 可将\\(x\\)或\\(y\\)看成是未知函数.

虽然对于一般的一阶常微分没有通用的求解方法, 但有一些特殊形式的一阶常微分方程
可以通过换元法或分离变量法等方法求解.

### 可分离变量的方程

常常我们会遇到形如以下形式的一阶微分方程

\\[
\frac{d y}{d x}=-\frac{p(x)}{q(y)}
\\]

那么我们可以写成

\\[
p(x) d x+q(y) d y=0 .
\\]

从\\((x_0, y_0)\\)积分到\\((x, y)\\)得到

\\[
\int_{x_0}^{x} p(x) d x+\int_{y_0}^{y} q(y) d y= 0.
\\]

两个不定积分的原函数分别是\\(P(x), Q(y)\\), 则上式的通解为
\\(P(x) + Q(y) = C\\). 这里的积分常数已单独写出.

### 全微分

分离变量的方程其实不需要微分方程线性.
如果恰有全微分\\(d \varphi\\)满足

\\[
d \varphi=\frac{\partial \varphi}{\partial x} d x+\frac{\partial \varphi}{\partial y} d y=0 .
\\]

则可得

\\[
\left\{\begin{array}{l}
\frac{\partial \varphi}{\partial x}=p(x, y) . \\\\
\frac{\partial \varphi}{\partial y}=q(x, y) .
\end{array}\right.
\\]
那么原方程的解为 \\(\varphi(x, y)=C\\).

在找这样的解之前, 有必要先验证下

\\[
\frac{\partial^2 \varphi}{\partial y \partial x}=\frac{\partial p(x, y)}{\partial y}   \frac{\partial^2 \varphi}{\partial x \partial y}=\frac{\partial q(x, y)}{\partial x}
\\]

两式是否相等. 也就是说, 我们需要验证

\\[
\frac{\partial p(x, y)}{\partial y} = \frac{\partial q(x, y)}{\partial x}
\\]

最终解可以写为

\\[
\varphi(x, y)=\int_{x_0}^x p(x, y) d x+\int_{y_0}^y q(x_0, y) \equiv C
\\]

注意可分离变量和全微分的区别: 所有可分离变量的方程都是全微分方程, 但并非所有全微分方程都是可分离变量的.
换句话说,

\\[
\begin{aligned}
& \text { 可分离 } \Rightarrow \text { 全微分 } \\\\
& \text { 但全微分} \nRightarrow \text{可分离} \\\\
\end{aligned}
\\]

> **例** 考虑常微分方程

\\[
y'+\left(1+\frac{y}{x}\right)=0
\\]

> **解** 左右两边同时乘以\\(x dx\\), 得

\\[
(x+y) d x+x d y=0
\\]

按照上述形式可以知\\(p(x,y) = x+y\\), \\(q(x,y) = x\\). 方程无法分离变量, 但可以验证

\\[
\frac{\partial p}{\partial y}=1, \frac{\partial q}{\partial x}=1
\\]

二者相同，于是可以知道符合全微分条件

\\[
\varphi=\int_{x_0}^x(x+y) d x+\int_{y_0}^y x_0 d y=\left(\frac{x^2}{2}+x y-\frac{x_0^2}{2}-x_0 y\right)+\left(x_o y-x_0 y_0\right)
\\]

解为

\\[
\frac{x^2}{2}+x y=c.
\\]

可以写成\\( y = \frac{c}{x} - \frac{x}{2} \\)的形式并验证是否满足原方程.

### 可换元法

下面考虑可以换元法解决的方程, 它的形式为

\\[
\frac{dy}{dx} = f(a x + by + c), b\neq 0
\\]

我们可以采用换元\\(u = ax + by\\), 将\\(u\\)作为未知函数,有\\(a dx + b dy = du \\),
可以化为

\\[
du  = ( a + b f(u+c) ) dx,
\\]

变成了可分离变量形式. 我们可得\\(u  = \varphi (x, C)\\), 原方程解为

\\[
y = \frac{1}{b} \left(\varphi(x, C) - a x \right).
\\]

### 权重法

若常微分方程的每项\\(x, y\\)幂次合在一起为同一数\\(n\\), 则称该方程为\\(n\\)次的**齐次方程**. 注意这里的齐次不同于线性齐次方程的概念.
例如方程

\\[
(2x + y) dx + x dy = 0.
\\]

方程的解可以用\\(y = x v\\)替代, 有\\(dy = x dv + v dx\\).
这一替代后所有项的方程包含\\(dv\\)都有\\(x^{n+1\\), 各项包含\\(dx\\)的有\\(x^n\\), 于是可以将其化成对\\(x, v\\)
可分离的形式.
对上式不难看出

\\[
(2 v + 2 ) dx + x dv  = 0,
\\]

是可分离的, 其解为 \\(\ln x + \frac{1}{2} \ln (v + 1) = c, \\) 等价于\\(x^2 (v + 1) = c\\), 于是可以得到

\\[
y = \frac{c}{x} - x.
\\]

基于次数齐次的思想, 我们可以推广到更一般的情况. 如果方程中每一项的\\(x, y\\)幂次之和不是同一数,
但可以通过换元使得每一项的\\(x, y\\)幂次之和变成同一数. 我们将y或dy赋予权重\\(m\\).

我们以

\\[
\left(x^2-y\right) d x+x d y=0 .
\\]

为例, 作替换\\(y=x^{m}v\\).

\\[
\begin{aligned}
& x \text { 权重为 } 1, y\text { 权重为 }m \\\\
& x^2 d x \text { 权重为 } 3:
\end{aligned}
\\]

\\(-ydx,  x d y\\) 权重为 \\(1+m\\).
为了配平权重

\\[
1+m=3 \Rightarrow m=2.
\\]

于是令\\(y=x^2 v\\), 则\\(dy = 2 x v d x + x^2 d v\\).
带入可得

\\[
(1-v) d x+x d v=0
\\]

其解为 \\( \ln x+\ln (v+1)=c\\) 或 \\(x(v+1)=c\\).
得到最终解

\\[
y=x^2 v=x^2\left(\frac{c}{x}-1\right) = -x^2+c x
\\]

### 一阶线性方程

一般一阶线性常微分方程的标准形式为

\\[
\frac{d y}{d x}+p(x) y=q(x).
\\]

当\\(q(x) \equiv 0\\)时, 上式为特殊形式

\\[
\frac{d y}{d x}+p(x) y = 0.
\\]

成为**一阶线性齐次方程**
当上式可以写成全微分的形式时, 可直接求解. 但一般情况下, 我们可以引入一个**积分因子** \\(\alpha(x)\\),
它的选择可以使得方程变成全微分的形式. 具体做法如下.

两边同时乘以 \\(\alpha(x)\\) .

\\[
\alpha \frac{d y}{d x}+\alpha p y=\alpha q
\\]

而对\\(\alpha y\\)求导有

\\[
\frac{d}{d x}(\alpha y)=\frac{d \alpha}{d x} y+\alpha \frac{d y}{d x} .
\\]

为了使左式是一个全微分, 比较两式要求
\\(\frac{d \alpha}{d x}=\alpha p \\), 即 \\(\frac{d \alpha{\alpha}=p d x \\). 于是有

\\[
\alpha(x)=e^{\int p(x) d x}.
\\]

回到原问题,需求

\\[
\frac{d}{d x}(\alpha y)=\alpha q
\\]

即

\\[
y=\frac{1}{\alpha(x)}\left[\int^x \alpha(t) q(t) dt+C\right] \equiv y_1(x)+y_2(x)
\\]

这里，我们将该解分成两个部分

\\[
\begin{aligned}
& y_1(x)=\frac{1}{\alpha(x)} \int^x \alpha(t) q(t) d t \\\\
& y_2(x)=\frac{C}{\alpha(x)}
\end{aligned}
\\]

可以看出, \\(y_2(x)=\frac{c}{\alpha(x)}\\)是齐次方程的通解,
而 \\(y_1(x)=\frac{1}{\alpha(x)} \int^x \alpha(t) q(t) d t\\)是方程的特解.
一般地, 微分方程的解是**特解**加**通解**的形式.

> **例** 对于一个电阻-电感（RL）电路，基尔霍夫定律给出

\\[
L \frac{d I(t)}{d t}+R I(t)=V(t)
\\]

其中 \\(I(t)\\) 是电流，\\(L\\) 和 \\(R\\) 分别为电感和电阻的常数值，\\(V(t)\\) 是随时间变化的输入电压。

> **解** 积分因子 \\(\alpha(t)\\) 为

\\[
\alpha(t)=\exp \int^t \frac{R}{L} d t=e^{R t / L}
\\]

根据公式, 有

\\[
I(t)=e^{-R t / L}\left[\int^t e^{R t / L} \frac{V(t)}{L} d t+C\right]
\\]

其中常数 \\(C\\) 由初始条件确定。
对于特殊情况 \\(V(t)=V_0\\)（常数），

\\[
I(t)=e^{-R t / L}\left[\frac{V_0}{L} \cdot \frac{L}{R} e^{R t / L}+C\right]=\frac{V_0}{R}+C e^{-R t / L}
\\]

若初始条件为 \\(I(0)=0\\)，则 \\(C=-V_0 / R\\)，因此

\\[
I(t)=\frac{V_0}{R}\left[1-e^{-R t / L}\right]
\\]

###  常系数的常微分方程 (ODE)

常系数的常微分方程的标准形式为

\\[
\frac{d^n y}{d x^n}+a_{n-1}\frac{d^{n-1} }{d x^{n-1}} y  + \cdots +a_{1} \frac{d}{d x} y+a_0 y=F(x)
\\]

其中\\(a_i\\)为常数.

\\[
\Rightarrow \text { 解的形式为 } y=e^{m x}
\\]

其中\\(m\\)需满足代数方程

\\[
m^n+a_{n-1} m^{n-1}+\cdots a_1 m+a_0=0
\\]

对于二阶常系数线性齐次方程,

\\[
y" + a y' + by = 0,
\\]

代数方程化成

\\[
m^2 + a m + b = 0
\\]

该方程成为微分方程的**特征方程**，其解为**特征根**. 如果两根不同
则有通解

\\[
y = C_1 e^{m_1 x} +  C_2 e^{m_2 x}
\\]

若特征根为二重实根\\(m\\), 则解为

\\[
y = (C_1 + C_2  x) e^{m x}
\\]

> **例** 一个质量为 \\(M\\) 的物体连接在胡克定律弹簧（劲度系数为 \\(k\\)）上，做振动运动。设 \\(y\\) 为物体相对于平衡位置的位移，根据牛顿运动定律，有

\\[
M \frac{d^2 y}{d t^2}=-k y,
\\]

> **解** 这是一个形如 \\(y^{\prime \prime}+a_0 y=0\\) 的常微分方程，其中 \\(a_0=+k / M\\)。该方程的通解为 \\(C_1 e^{m_1 t+C_2 e^{m_2 t}\\)，其中 \\(m_1\\) 和 \\(m_2\\) 是代数方程 \\(m^2+a_0=0\\) 的解。

\\(m_1\\) 和 \\(m_2\\) 的取值为 \\(\pm i \omega\\)，其中 \\(\omega=\sqrt{k / M\\)，因此方程的通解为



\\[
y(t)=C_1 e^{+i \omega t}+C_2 e^{-i \omega t} .
\\]

由于该方程是齐次的，我们可以将上述两个解的任意线性组合作为通解。这样可以将解组合成实数形式，更适合当前问题。注意到



\\[
\frac{e^{i \omega t}+e^{-i \omega t}}{2}=\cos \omega t   \text { 且 }   \frac{e^{i \omega t}-e^{-i \omega t}}{2 i}=\sin \omega t,
\\]

因此，通解的另一种常用形式为



\\[
y(t)=C_1 \cos \omega t+C_2 \sin \omega t .
\\]

对于具体的振动问题，解的系数 \\(C_1\\) 和 \\(C_2\\) 需要根据初始条件（如 \\(y(0)\\) 和 \\(y^{\prime(0)\\)）来确定。
