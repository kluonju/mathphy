## 积分求解实例


- 计算定积分


\\[
I=\int_0^{\infty} x^{\alpha-1} \frac{1}{1+x} d x  (0<\alpha<1).
\\]

将被积函数 \\(x^{\alpha-1} /(1+x)\\) 从实轴延拓到复数 \\(z\\) 平面得到
\\(f(z)=z^{\alpha-1} /(1+z)\\). 由于 \\(f(z)\\) 含 有 \\(z^{\alpha-1\\) ,
而 \\(\alpha\\) 不是整数,所以 \\(f(z)\\) 是多值函数, 它有两个支点：原点和无限远点.
\\(z\\) 每绕原点或 无限远点一圈, 辐角增加 \\(2 \pi, z^{\alpha-1\\) 多出因子
\\(e^{\mathrm{i} 2 \pi(\alpha-1)}\\) 亦即 \\(e^{\mathrm{i} 2 \pi \alpha}\\),
     从而 \\(f(z)\\) 也多出这么一个 因子.
从原点沿着正实轴直至无限远作割线.



\\[
\oint_l f(z) d z=\int_{\epsilon}^R \frac{x^{\alpha-1}}{1+x} d x+\int_{C_R} f(z) d z+\int_R^{\epsilon} \frac{x^{\alpha-1} e^{\mathrm{i} 2 \pi \alpha}}{1+x} d x+\int_{C_{\epsilon}} f(z) d z .
\\]

令 \\(R \rightarrow \infty, \epsilon \rightarrow 0\\).
 上式左边按照留数定理应为 \\(2 \pi i\{f(z)\\) 在有限远各奇点留数之和\
  右边第一个积分成为所求的 \\(I\\), 第三个积分则成为 \\(-e^{\mathrm{i} 2 \pi \alpha} I\\).
  可以证明第 二个和第四个积分则成为零. 事实上,


\\[
\begin{aligned}
\left|\int_{C_R} \frac{z^{\alpha-1}}{1+z} d z\right| & =\left|\int_{C_R} \frac{z^\alpha}{1+z} \frac{d z}{z}\right| \leqslant \max _{\left(C_R \text { 上 }\right)}\left|\frac{z^\alpha}{1+z}\right| \frac{\int|d z|}{|z|} \\ = & \max \frac{R^\alpha}{|1+z|} \cdot \frac{2 \pi R}{R}=2 \pi \max \frac{R^\alpha}{|1+z|} \\\\
& \sim 2 \pi \frac{1}{R^{1-\alpha} \rightarrow 0}  (\text { 于 } R \rightarrow \infty) .
\end{aligned}
\\]

\\[
\begin{aligned}
\left|\int_{C_{\epsilon}} \frac{z^{\alpha-1}}{1+z} d z\right|= & \left|\int_{C_{\epsilon}} \frac{z^\alpha}{1+z} \frac{d z}{z}\right| \leqslant \max _{\left(C_{\epsilon} \text { 上 }\right)}\left|\frac{z^\alpha}{1+z}\right| \frac{\int|d z|}{|z|} \\ = & \max \frac{\epsilon^\alpha}{|1+z|} \cdot \frac{2 \pi \epsilon}{\epsilon}=2 \pi \max \frac{\epsilon^\alpha}{|1+z|} \\\\
& \sim 2 \pi \frac{\epsilon^\alpha}{1} \rightarrow 0  (\text { 于 } \epsilon \rightarrow 0) .
\end{aligned}
\\]

于是 \\(\left(1-e^{\mathrm{i} 2 \pi \alpha}\right) I=2 \pi \mathrm{i}\{f(z)\\) 在有限远各奇点留数之和 \\(\\\).
\\(f(z)=z^{\alpha-1}(1+z)^{-1}\\) 只有一个单极点 \\(z_0=-1=e^{\mathrm{i} \pi}\\), 而

\\[
\operatorname{Res} f(-1)=\lim _{z \rightarrow-1}[(z+1) f(z)]=\lim _{z \rightarrow-1}\left[z^{\alpha-1}\right]=e^{\mathrm{i}(\alpha \pi-\pi)}=-e^{\mathrm{i} \alpha \pi} \text {. }
\\]

因此

\\[
\begin{aligned}
I & =-\frac{2 \pi \mathrm{i} e^{\mathrm{i} \pi \alpha}}{1-e^{\mathrm{i} 2 \pi \alpha}}=-\frac{2 \pi \mathrm{i} e^{\mathrm{i} \pi \alpha}}{e^{\mathrm{i} \pi \alpha}\left(e^{-\mathrm{i} \pi \alpha}-e^{\mathrm{i} \pi \alpha}\right)} \\\\
& =\frac{2 \pi \mathrm{i}}{\left(e^{-\mathrm{i} \pi \alpha}-e^{\mathrm{i} \pi \alpha}\right)}=\frac{2 \pi \mathrm{i}}{2 \sin \pi \alpha}=\frac{\pi}{\sin \pi \alpha} .
\end{aligned}
\\]


- 计算菲涅耳积分(Fresnel integrals)


\\[
I_1=\int_0^{\infty} \sin \left(x^2\right) d x \text { 及 } I_2=\int_0^{\infty} \cos \left(x^2\right) d x \text {. }
\\]

由于 \\(\sin \left(x^2\right)=\Im e^{\mathrm{i} x^2}\\), 而 \\(\cos \left(x^2\right)=\Re e^{\mathrm{i} x^2}\\), 所以

\\[
I_2+\mathrm{i} I_1=\int_0^{\infty} e^{\mathrm{i} x^2} d x .
\\]

取图 4-10 所示回路 \\(l\\). 由于 \\(e^{\mathrm{i} z^2}\\) 没有有限远奇点, 所以根据留数定理得

\\[
\oint_l e^{\mathrm{i} z^2} d z=0,
\\]

即 \\(\int_0^R e^{\mathrm{i} x^2} d x+\int_{C_R} e^{\mathrm{i} z^2} d z+\int_R^0 e^{\mathrm{i}\left(\rho e^{\mathrm{i} \pi / 4}\right)^2} d\left(\rho e^{\mathrm{i} \pi / 4}\right)=0\\),

令 \\(R \rightarrow \infty\\). 第一个积分即所求的 \\(I_2+\mathrm{i} I_1\\). 第三个积分不难如下算出 :

\\[
\begin{aligned}
\lim _{R \rightarrow \infty} \int_R^0 e^{\mathrm{i}\left(\rho^2 \mathrm{i}\right)} e^{\mathrm{i} \pi / 4} d \rho & =\lim _{R \rightarrow \infty}\left(-e^{\mathrm{i} \pi / 4}\right) \int_0^R e^{-\rho^2} d \rho=-e^{\mathrm{i} \pi / 4} \int_0^{\infty} e^{-\rho^2} d \rho \\\\
& =-\frac{\sqrt{\pi}}{2} e^{\mathrm{i} \pi / 4}=-(1+\mathrm{i}) \sqrt{\frac{\pi}{8}} .
\end{aligned}
\\]

可以证明第二个积分成为零. 为此, 先作一次分部积分,

\\[
\int_{C_R} e^{\mathrm{i} z^2} d z=\left.\frac{e^{\mathrm{i} z^2}}{2 \mathrm{i} z}\right|_{z=R} ^{R e^{\mathrm{i} \pi / 4}}+\int_{C_R} e^{\mathrm{i} z^2} \frac{d z}{2 \mathrm{i} z^2},
\\]

其中已积出部分的模

\\[
\left|\frac{e^{-R^2}}{2 \mathrm{i} R e^{\mathrm{i} \pi / 4}}-\frac{e^{\mathrm{i} R^2}}{2 \mathrm{i} R}\right| \leqslant \frac{e^{-R^2}}{2 R}+\frac{1}{2 R} \rightarrow 0  (\text { 于 } R \rightarrow \infty),
\\]

未积出部分的模

\\[
\begin{aligned}
\left|\int_{C_R} \frac{e^{\mathrm{i} 2^2}}{2 \mathrm{i} {z}^2} d z\right| & =\left|\int_{C_R} \frac{e^{-R^2 \sin 2 \varphi+\mathrm{i}^2 \cos 2 \varphi}}{2 \mathrm{i} R^2 e^{\mathrm{i} 2 \varphi}} R e^{\mathrm{i} \varphi} \mathrm{i} d \varphi\right| \\\\
& \leqslant \int_{C_R} \frac{e^{-R^2 \sin 2 \varphi}}{2 R^2} R d \varphi \leqslant \max \left(\frac{e^{-R^2 \sin 2 \varphi}}{2 R}\right) \frac{\pi}{4}
\\\\
&=\frac{1}{2 R} \frac{\pi}{4} \rightarrow 0  (\text { 于 } R \rightarrow \infty) .
\end{aligned}
\\]

于是

\\[
\begin{gathered}
I_2+\mathrm{i} I_1-\sqrt{\frac{\pi}{8}}(1+\mathrm{i})=0, \\\\
I_1=\sqrt{\frac{\pi}{8}},   I_2=\sqrt{\frac{\pi}{8}} .
\end{gathered}
\\]

- 考虑用Feynman技巧来计算

\\[
I = \int_0^1 \frac{x^2-1}{\log x} d x
\\]

设计这样的函数

\\[
G(t):=\int_0^1 \frac{x^t-1}{\log x} d x
\\]

\\(G(0) = 0\\),于是问题变为求\\(G(2)\\).不难验证

\\[
G^{\prime}(t)=\int_0^1 x^t d x=\frac{1}{t+1}
\\]

对\\(t\\)求积分后得到

\\[
G(2)=\int_0^2 G^{\prime}(t) d t=\int_0^2 \frac{d t}{t+1}=\log 3.
\\]

- 考虑用Feynman技巧来验证高斯积分:

\\[
\int_0^{\infty} e^{-x^2} d x = \frac{\sqrt{\pi}}{2}.
\\]

\\
定义一个\\(t\\)的函数

\\[
I(t):=\int_0^{\infty} \frac{e^{-x^2}}{1+(x / t)^2} d x, t>0.
\\]

于是菲涅尔积分就是求\\(I_1 = I(\infty)\\).
做代换\\(x/t=y\\)后,并换回积分变量为\\(x\\)有

\\[
I(t)=t \int_0^{\infty} \frac{e^{-t^2 x^2}}{1+x^2} d x
\\]

可以得到

\\[
\lim _{t \rightarrow 0} \frac{I(t)}{t}=\frac{\pi}{2}.
\\]

为了能利用上面的技巧,我们将考虑

\\[
e^{-t^2} I(t)=t \int_0^{\infty} \frac{e^{-t^2\left(1+x^2\right)}}{1+x^2} d x
\\]

对于

\\[
\frac{d}{d t}\left(t^{-1} e^{-t^2} I(t)\right)=\int_0^{\infty}-2 t e^{-t^2\left(1+x^2\right)} d x=-2 e^{-t^2} \int_0^{\infty} e^{-u^2} d u=-2 e^{-t^2} I(\infty)
\\]

两边积分

\\[
\underbrace{\int_0^{\infty} \frac{d}{d t}\left(t^{-1} e^{-t^2} I(t)\right) d t}_{=-\lim _{t \rightarrow 0} \frac{I(t)}{t}}=\underbrace{\int_0^{\infty}-2 e^{-t^2} I(\infty) d t}_{=-2 I(\infty)^2}
\\]

得到

\\[
I(\infty) = \sqrt{\frac{\pi}{4}} = \frac{\sqrt{\pi}}{2}.
\\]

## Feynman技巧

我们将讨论下面几个计算定积分的技巧.

### 复变量代换

以一个例子说明复变量代换的方法.求解定积分

\\[
I =  \int_0^{\infty} e^{-a x} \cos b x d x
\\]

利用\\(\cos{bx} = \frac{1}{2}\left( e^{\mathrm{i} b x} + e^{-\mathrm{i} bx}\right)\\)

\\[
\begin{aligned}
I= & \frac{1}{2} \int_{0}^{\infty} \left(e^{-(a-\mathrm{i} b) x} + e^{-(a + \mathrm{i} b) x} \right)  d x \\ = & \frac{1}{2} \left( \frac{1}{a-\mathrm{i} b} +  \frac{1}{a+\mathrm{i} b} \right)\\ = & \frac{a}{a^2+b^2}
\end{aligned}
\\]

### 参数微分

求解定积分

\\[
I =  \int_0^{\infty} x e^{-a x} \cos b x d x
\\]

我们令

\\[
S(a) =   \int_0^{\infty} e^{-a x} \cos b x d x
\\]

已知 \\(S(a) = \frac{a}{a^2+b^2}\\),通过对\\(S(a)\\)对\\(a\\)的求导得到

\\[
I = - S'(a)  = \frac{a^2 - b^2}{(a^2 +b^2)^2}
\\]

对于一般的含参数的微分,我们有

\\[
\begin{aligned}
\frac{d}{d \alpha} \int_{x_1(\alpha)}^{x_2(\alpha)} f(x, \alpha) d x= & \int_{x_1}^{x_2} \frac{\partial}{\partial \alpha} f(x, \alpha) d x \\\\
& \left[\frac{d x_2(\alpha)}{d \alpha} \right] f(x_2, \alpha)-
\left[\frac{d x_1(\alpha)}{d \alpha}\right] f(x_1, \alpha)
\end{aligned}
\\]

### 被积函数添加函数因子

求解定积分

\\[
I =  \int_0^{\infty} \frac{\sin{x}}{x} d x
\\]

可以通过乘以一个函数因子\\(e^{-a x}\\)来构造参数函数

\\[
S(a) =     \int_0^{\infty}  e^{-a x} \frac{\sin{x}}{x} d x
\\]

这样我们有

\\[
S'(a) = -  \int_0^{\infty}  e^{-a x} \sin{x} d x  = \frac{1}{1+a^2}
\\]

对于\\(a \to \infty\\), 有 \\(S(\infty) = 0\\).
而\\(\frac{1}{1+x^2}\\)的原函数为\\(\arctan{x\\),因此

\\[
S(a) = - \arctan{a} + C
\\]

可确定\\(C = \frac{\pi}{2}\\),因此我们有\\(S(a) = \frac{\pi{2} - \arctan{\alpha}\\).
因此,

\\[
I = S(0) = \frac{\pi}{2} .
\\]

该结果我们已通过留数定理求得.

## 数值实验

```bash
python scripts/ch01_residue_integral.py
julia scripts/ch01_residue_integral.jl
```
