### 留数定理

柯西定理指出,若被积函数\\(f(z)\\)在回路\\(\ell\\)所围区域是解析的,则回路积分\\(\oint_\ell f(z) dz\\)为零.下面讨论所围区域包含奇点的情况.
假设一个含有\\(m\\)阶极点\\(z=z_0\\)的函数,它可以展开为洛朗级数

\\[
f(z) = \sum_{k = -m} ^{\infty} a_k (z - z_0)^k
\\]

取圆环内包含\\(z_0\\)的闭合回路,由柯西定理可知,回路积分\\(\oint_\ell f(z) dz = \oint_C f(z) dz\\), 将洛朗展开带入逐项积分,可得

\\[
\oint_\ell f(z) dz = \sum_{k = -m} ^{\infty} \oint_C  (z - z_0)^k dz,
\\]

由前面例题可知,只有\\(a_{-1}\\)项不为零,其他项为零.而\\(a_{-1\\)项的积分为\\(2\pi\mathrm{i}\\).因此,我们得到

\\[
\oint_\ell f(z) dz = 2\pi \mathrm{i} a_{-1} .
\\]

又因为\\(a_{-1}\\)为函数\\(f(z)\\)在\\(z=z_0\\)处的留数,记为\\(\operatorname{Res f(z_0)\\).于是有

\\[
\oint_\ell f(z) dz = 2\pi \mathrm{i} \operatorname{Res} f(z_0) .
\\]

扩展到多个奇点的情况,不难得到

\\[
\oint_\ell f(z) dz = 2\pi \mathrm{i} \sum_{j=1}^{n} \operatorname{Res} f(z_j) .
\\]

上式为**留数定理**的数学表达式,即回路积分可以写成被积函数在回路所围区域上各个奇点的留数之和.

下面介绍一下计算留数的一种方法.
通常,我们并不总是要将一个函数展开为洛朗级数来找出\\(a_{-1}\\)的值.如果\\(f(z)\\)有
\\(n\\)阶极点\\(z_0\\),那么有

\\[
\left(z-z_0\right)^n f(z)=a_{-n}+\cdots+a_{-1}\left(z-z_0\right)^{n-1}+a_0\left(z-z_0\right)^n+\cdots .
\\]

不断求导后可以验证

\\[
a_{-1}=\frac{1}{(n-1) !} \lim _{z \to z_0}\left[\frac{d^{n-1}}{d z^{n-1}}\left(\left(z-z_0\right)^n f(z)\right)\right]
\\]

此外,另外一种方法也比较常见. 若 \\(f(z)\\) 可以表示为 \\(P(z) / Q(z)\\) 的特殊形式, 其中 \\(P(z)\\) 和 \\(Q(z)\\) 都在 \\(z_0\\) 点 解析, \\(z_0\\) 是 \\(Q(z)\\) 的一阶零点. \\(P\left(z_0\right) \neq 0\\), 从而 \\(z_0\\) 是 \\(f(z)\\) 的一阶极点, 则

\\[
\operatorname{Res} f\left(z_0\right)=\lim _{z \to z_0}\left(z-z_0\right) \frac{P(z)}{Q(z)}=\frac{P\left(z_0\right)}{Q^{\prime}\left(z_0\right)} .
\\]

上式最后一步应用了罗毕达法则.
下面给出一些计算留数的例子.

> **例** 计算留数.

> **解**


- \\(\frac{1}{\sin z}\\)在\\(z=0\\)处的留数为\\(\lim_{z\to 0 \frac{z}{\sin{z}} = 1\\).

- \\(\frac{\ln{z}}{z^2 + 4}\\)在\\(z=2e^{\mathrm{i} \frac{1}{2} \pi}\\)处的留数为\\(\lim_{z\to 2e^{\mathrm{i} \frac{1}{2} \pi}} \frac{(z-2e^{\mathrm{i} \frac{1}{2}\pi})\ln{z} }{z^2 + 4} = \frac{\ln 2 + \mathrm{i} \frac{1}{2} \pi}{4\mathrm{i}} = \frac{\pi}{8} - \frac{\mathrm{i}\ln{2}}{4}.\\)

- \\(f(z) = \frac{\cot{\pi z}}{z(z+2)}\\)在\\(z=0\\)处的留数.\\


\\[
f(z) = \frac{1}{z} \left[\frac{1}{\pi z} + O(z) \right]\frac{1}{2} \left[1 - \frac{z}{2} + O(z^2)\right]
\\]

            可以得到该函数的留数为\\(-1/(4\pi)\\).

- \\(f(z) = \frac{1}{z^n - 1}\\)在\\(z=1\\)处的留数可通过如下方法.可知


\\[
f(z)=\frac{1}{z^n-1}=\frac{1}{(z-1)\left(z^{n-1}+z^{n-2}+\cdots+z+1\right)},
\\]

        因此,有


\\[
\begin{aligned}
                \operatorname{Res} f(1) & =\lim _{z \to 1}\left[(z-1) \frac{1}{(z-1)\left(z^{n-1}+z^{n-2}+\cdots+z+1\right)}\right] \\\\
                & =\lim _{z \to 1} \frac{1}{z^{n-1}+z^{n-2}+\cdots+z+1}=\frac{1}{n} .
            \end{aligned}
\\]

        或者用

\\[
\lim _{z \to 1}\left[\frac{1}{\left(z^n-1\right)^{\prime}}\right]=\lim _{z \to 1} \frac{1}{n z^{n-1}}=\frac{1}{n} .
\\]

 因此,此函数在\\(z=1\\)处的留数为\\(1/n\\).


留数的概念还可以帮助求解裂项分解时的待定系数,如

\\[
f(z) = \frac{1}{(z-1)(z-2)(z-3)} = \frac{A}{z-1} + \frac{B}{z-2} + \frac{C}{z-3},
\\]

中求待定系数\\(A,B,C\\)这样的只包含一阶极点的问题. 不难看出\\(A,B,C\\)分别对应\\(f(z)\\)在\\(z=1,2,3\\)的留数.
于是有

\\[
\begin{aligned}
A &= \operatorname{Res} f(1) = \lim_{z\to 1} (z-1) f(z) = \frac{1}{2},
\\\\
B &= \operatorname{Res} f(2) = \lim_{z\to 2} (z-2) f(z) = -1,
\\\\
C &= \operatorname{Res} f(3) = \lim_{z\to 3} (z-3) f(z) = \frac{1}{2}.
\end{aligned}
\\]

对于高阶极点的情况,可以类似处理.

\\[
\frac{1}{(z-1)^2(z-2)(z-3)}=\frac{A}{(z-1)^2}+\frac{B}{z-1}+\frac{C}{z-2}+\frac{D}{z-3}
\\]

注意\\(A\\)的处理

\\[
\begin{aligned}
A &= \operatorname{Res}  (z-1) f(z) |_{z=1}  = \frac{1}{2},
\\\\
B &= \operatorname{Res} f(1) =  \lim_{z\to 1} \frac{d}{dz} \left[ (z-1)^2 f(z) \right] = \frac{3}{4},
\\\\
C &= \operatorname{Res} f(2) = \lim_{z\to 2} (z-2) f(z) = -1,
\\\\
D &= \operatorname{Res} f(3) = \lim_{z\to 3} (z-3) f(z) = \frac{1}{4}.
\end{aligned}
\\]

### 留数定理应用

对于实变函数的定积分,我们已经学会了一些积分技巧,如变量代换,分部积分等.这一章节我们
将介绍利用留数定理的积分技巧,并介绍以物理学家Richard P. Feynman命名的
特殊技巧.
#### 三角函数的积分

考虑积分区间为\\(\left[ 0, 2\pi \right]\\),被积函数为三角函数有理式的积分

\\[
\int_{0}^{2\pi} R(\cos{x}, \sin{x}) dx,
\\]

当实变数 \\(x\\) 从 0 变到 \\(2 \pi\\) 时, 复变数 \\(z=e^{\mathrm{i} x}\\) 从 \\(z=1\\) 出发沿单位圆 \\(|z|=1\\) 逆时针 走一圈又回到 \\(z=1\\),
实变定积分化为复变回路积分, 就可以应用留数定理了. 至于实变定积分里的 \\(\cos x, \sin x\\) 和 \\(d x\\), 作如下变换:

\\[
\cos x=\frac{1}{2}\left(z+z^{-1}\right),   \sin x=\frac{1}{2 \mathrm{i}}\left(z-z^{-1}\right),   d x=\frac{1}{\mathrm{i} z} d z .
\\]

于是, 原积分化为

\\[
I=\oint_{|z|=1} R\left(\frac{z+z^{-1}}{2}, \frac{z-z^{-1}}{2 \mathrm{i}}\right) \frac{d z}{\mathrm{i} z}
\\]

利用留数定理即可求得.

> **例** 求定积分

\\[
I=\int_0^{2 \pi} \frac{d \theta}{1+a \cos \theta},  |a|<1
\\]

> **解** 根据上面的方法,可得


\\[
\begin{aligned}
        I & =-\mathrm{i} \oint_{|z|=1} \frac{d z}{z\left[1+(a / 2)\left(z+z^{-1}\right)\right]} \\\\
        & =-\mathrm{i} \frac{2}{a} \oint \frac{d z}{z^2+(2 / a) z+1} .
        \end{aligned}
\\]

两个极点分别为


\\[
z_1=-\frac{1+\sqrt{1-a^2}}{a}   \text {和}   z_2=-\frac{1-\sqrt{1-a^2}}{a}
\\]

不难看出,\\(z_1\\)在单位圆外,\\(z_2\\)在单位圆内.积分可以写成


\\[
\oint \frac{dz}{(z-z_1)(z-z_2)}
\\]

留数则为\\(\frac{1}{z_2 - z_1}\\), 利用留数定理可得


\\[
I=  -\mathrm{i} \frac{2}{a} 2\pi\mathrm{i} \frac{1}{z_2 - z_1} = \frac{2 \pi }{\sqrt{1 - a^2}} .
\\]

#### 积分上下限为\\(( -\infty, \infty)\\)

 考虑如下形式的定积分


\\[
\int_{-\infty}^{\infty} f(x) dx
\\]

 我们先讨论复变函数 \\(f(z)\\) 在实轴上没有奇点的情况,有奇点的情况后面讨论.
被积函数在上半平面除有限个奇点外是解析的; 当 \\(z\\) 在上半平面及实轴上 \\(\to \infty\\) 时,
\\(z f(z)\\) 一致地 \\(\to 0\\).

取如图所示的上半平面的半径为\\(R\\)的半圆路径\\(\ell\\).路径积分可以写成两部分的和

\\[
\oint_l f(z) d z=\int_{-R}^R f(x) d x+\int_{C_R} f(z) d z .
\\]

根据留数定理,上式等于\\(2\pi \mathrm{i}  \sum_j \operatorname{Res} f(z_j)\\).

下面证明上式第二项为零.一般的对于任意\\(\theta_1 \leq \theta \leq \theta_2\\),
有\\(\lim_{R\to \infty} zf(z) = 0\\),可以证明对于该角度对应的圆弧\\(C\\)有,

\\[
\lim_{R \rightarrow \infty} \int_C f(z) dz = 0 .
\\]

\\[
\begin{aligned}
\lim _{R \rightarrow \infty}\left|\int_C f(z) d z\right| \leq \int_{\theta_1}^{\theta_2} \lim _{R \rightarrow \infty}\left|f\left(R e^{i \theta}\right) i R e^{i \theta}\right| & d \theta \\\\
& \leq\left(\theta_2-\theta_1\right) \lim _{R \rightarrow \infty}\left|f\left(R e^{i \theta}\right) R e^{i \theta}\right|=0 .
\end{aligned}
\\]

也就是说,

\\[
\int_{-R}^R f(x) d x = 2\pi \mathrm{i}  \sum_{z_j\in \text{上半平面}} \operatorname{Res} f(z_j),
\\]

> **例** 计算

\\[
I = \int_{-\infty}^{\infty} \frac{dx}{1 + x^2}   .
\\]

> **解** 由\\(f(z) = \frac{1}{1+ x^2} = \frac{1}{(z-\mathrm{i})(z+\mathrm{i})}\\)可知
其单极点\\(\pm \mathrm{i}\\),其中\\(\mathrm{i}\\)在上半平面.


\\[
\operatorname{Res} f(+\mathrm{i}) = \frac{1}{2\mathrm{i}}
\\]

因此,\\(I = 2\pi \mathrm{i}  \frac{1}{2\mathrm{i}} = \pi\\).由于该积分是一个常见积分
亦可以通过原函数\\(\arctan(x)\\)得到.留数定理的还可以计算这样的积分,


\\[
I\int_{-\infty}^{\infty} \frac{dx}{(1 + x^2)^n}
\\]

具体求解过程参考梁昆淼数学物理方法的解.

 #### 带复指数的定积分

 考虑以下类型的定积分


\\[
I=\int_{-\infty}^{\infty} f(x) e^{\mathrm{i} m x} d x
\\]

其中,\\(m\\)为正实数;\\(f(z)\\)在上半平面除有限个奇点外是解析的,且\\(\lim_{|z|\to \infty f(z) = 0, 0 \leq arg z \leq \pi\\).
我们使用同样的半圆路径,类似的可以通过留数定理将实轴的积分转换为环路积分求得.
为了使用留数定理,我们先需要证明在半圆上的路径积分为零,这里就要用到**约旦引理**(Jordan lemma
).
即证明

\\[
\lim _{R \rightarrow \infty} \int_{C_R} f(z) e^{\mathrm{i} m z} d z=0 .
\\]

当\\(R\\)足够大时,我们有\\(|f(z)| < \epsilon\\).半圆积分

\\[
\begin{aligned}
I_R&=\int_0^\pi f\left(R e^{\mathrm{i} \theta}\right)
e^{\mathrm{i} m R \cos \theta- m R \sin \theta} \mathrm{i} R e^{\mathrm{i} \theta} d \theta
\\\\
&\leq \epsilon R \int_0^\pi e^{-m R \sin \theta} d \theta=2 \epsilon R \int_0^{\pi / 2} e^{-m R \sin \theta} d \theta,
\end{aligned}
\\]

可以发现在\\(\left[ 0, \pi/2\right]\\)时,

\\[
\frac{2}{\pi}\theta \leq \sin{\theta},
\\]

于是有

\\[
I_R \leq 2 \epsilon R \int_0^{\pi / 2} e^{-2 m R \theta / \pi} d \theta=2 \epsilon R \frac{1-e^{-m R}}{2 m R / \pi}<\frac{\pi}{m} \epsilon
\\]

即

\\[
\lim_{R\to \infty} I_R = 0.
\\]

回到定积分\\(I\\),可以得

\\[
I=\int_{-\infty}^{\infty} f(x) e^{ \mathrm{i} m x} d x = 2\pi \mathrm{i} \sum_{z_j \in \text{上半平面}} \operatorname{Res} e^{\mathrm{i} m z_j} f(z_j)
\\]

对于以下类型的积分,可以利用上述结论.如

\\[
\int_{0}^{\infty} f(x) \cos {m x} dx, \int_{0}^{\infty} G(x) \sin{m x} dx
\\]

其中,\\(F(z)\\)为偶函数,\\(G(z)\\)为奇函数,它们在实轴上没有奇点,上半平面上除有限个奇点外解析.
很容易通过\\(\cos{mx} = \frac{1}{2}\left( e^{\mathrm{i} m x} + e^{-\mathrm{i} mx}\right)\\)等变换得到,即

\\[
\begin{aligned}
\int_0^{\infty} F(x) \cos m x d x & =\int_0^{\infty} F(x) \frac{1}{2}\left(e^{\mathrm{i} m x}+e^{-\mathrm{i} m x}\right) d x \\\\
& =\frac{1}{2} \int_0^{\infty} F(x) e^{\mathrm{i} m x} d x+\frac{1}{2} \int_0^{\infty} F(x) e^{-\mathrm{i} m x} d x
\\\\
& = \frac{1}{2} \int_{-\infty}^{\infty} F(x) e^{\mathrm{i} m x} d x.
\end{aligned}
\\]

> **例** 计算 \\(\int_0^{\infty} \frac{\cos m x}{x^2+a^2} d x\\).

> **解** 偶函数\\(F(z) e^{\mathrm{i} m z}=\frac{1}{z^2+a^2} e^{\mathrm{i} m z}\\) 有两个单极点 \\(\pm a \mathrm{i}\\), 其中 \\(+a \mathrm{i}\\) 在上半平面. 而 \\(e^{\mathrm{i} m z} /\left(z^2+a^2\right)\\) 在单极点 \\(+a \mathrm{i}\\) 的留数为


\\[
\lim _{z \rightarrow a \mathrm{i}}\left[(z-a \mathrm{i}) \frac{e^{\mathrm{i} m z}}{z^2+a^2}\right]=\lim _{z \rightarrow a \mathrm{i}}\left[\frac{e^{\mathrm{i} m z}}{z+a \mathrm{i}}\right]=\frac{e^{-m a}}{2 a \mathrm{i}}
\\]

应用,


\\[
\int_0^{\infty} \frac{\cos m x}{x^2+a^2} d x=\pi \mathrm{i} \frac{e^{-m a}}{2 a \mathrm{i}}=\frac{\pi}{2 a} e^{-m a}.
\\]

## 三角函数的积分

考虑积分区间为\\(\left[ 0, 2\pi \right]\\),被积函数为三角函数有理式的积分

\\[
\int_{0}^{2\pi} R(\cos{x}, \sin{x}) dx,
\\]

当实变数 \\(x\\) 从 0 变到 \\(2 \pi\\) 时, 复变数 \\(z=e^{\mathrm{i} x}\\) 从 \\(z=1\\) 出发沿单位圆 \\(|z|=1\\) 逆时针 走一圈又回到 \\(z=1\\),
实变定积分化为复变回路积分, 就可以应用留数定理了. 至于实变定积分里的 \\(\cos x, \sin x\\) 和 \\(d x\\), 作如下变换:

\\[
\cos x=\frac{1}{2}\left(z+z^{-1}\right),   \sin x=\frac{1}{2 \mathrm{i}}\left(z-z^{-1}\right),   d x=\frac{1}{\mathrm{i} z} d z .
\\]

于是, 原积分化为

\\[
I=\oint_{|z|=1} R\left(\frac{z+z^{-1}}{2}, \frac{z-z^{-1}}{2 \mathrm{i}}\right) \frac{d z}{\mathrm{i} z}
\\]

利用留数定理即可求得.

> **例** 求定积分

\\[
I=\int_0^{2 \pi} \frac{d \theta}{1+a \cos \theta},  |a|<1
\\]

> **解** 根据上面的方法,可得


\\[
\begin{aligned}
        I & =-\mathrm{i} \oint_{|z|=1} \frac{d z}{z\left[1+(a / 2)\left(z+z^{-1}\right)\right]} \\\\
        & =-\mathrm{i} \frac{2}{a} \oint \frac{d z}{z^2+(2 / a) z+1} .
        \end{aligned}
\\]

两个极点分别为


\\[
z_1=-\frac{1+\sqrt{1-a^2}}{a}   \text {和}   z_2=-\frac{1-\sqrt{1-a^2}}{a}
\\]

不难看出,\\(z_1\\)在单位圆外,\\(z_2\\)在单位圆内.积分可以写成


\\[
\oint \frac{dz}{(z-z_1)(z-z_2)}
\\]

留数则为\\(\frac{1}{z_2 - z_1}\\), 利用留数定理可得


\\[
I=  -\mathrm{i} \frac{2}{a} 2\pi\mathrm{i} \frac{1}{z_2 - z_1} = \frac{2}{\sqrt{1 - a^2}} .
\\]
