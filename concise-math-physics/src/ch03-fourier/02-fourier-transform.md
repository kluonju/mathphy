### 傅里叶变换

前面我们讨论了周期性体系的傅里叶级数展开.现在我们希望研究非周期性函数的傅里叶展开问题.
假设\\(f(x)\\)是定义在\\(-\infty < x < \infty\\)的实函数,我们依旧对该函数进行傅里叶级数展开,
该级数必须理解为周期\\(2\ell\\)扩展至\\(\infty\\)的极限情况.
由于三角函数族的变量为

\\[
\frac{n\pi x}{\ell}
\\]

引入非连续变量

\\[
\omega_n = \frac{n\pi} {\ell},   k = 0,1,2,\cdots
\\]

可知\\(\omega_n = n \omega_0\\), 其中\\(\omega_0 = \frac{\pi{\ell}\\)为基础频率(Fundamental Frequency),

\\[
\Delta \omega_n = \omega_n - \omega_{n-1} = \omega_0 .
\\]


有

\\[
f(x) = \lim_{\ell\to \infty} \sum_{n=-\infty}^{\infty} \left[
        c_n e^{\mathrm{i} \omega_n x}
\right]
\\]

其中系数

\\[
c_n = \frac{1}{2\ell} \int_{-\ell}^{\ell} f(x) e^{-\mathrm{i} \omega_n x} dx
\\]

取\\(\ell\to \infty\\)的极限,则

\\[
\sum_n \to  \frac{ \ell}{\pi}  \int d\omega
\\]

傅里叶系数记为\\(F(\omega)\\),
有

\\[
f(x) = \int_{-\infty}^{\infty} d \omega F(\omega) e^{\mathrm{i} \omega x},
\\]

上式的积分称为**傅里叶积分**(Fourier integral),是\\(f(x)\\)的**傅里叶变换**(Fourier transform).
其中

\\[
F (\omega) \equiv \lim_{\ell\to \infty} \frac{ 2\ell c_n}{2\pi}  = \frac{1}{2\pi} \int_{-\infty}^{\infty} e^{-\mathrm{i} \omega x} f(x) dx,
\\]

这被称为**逆傅里叶变换**(inverse Fourier transform). 这里积分前的系数并不要紧,更关键的是积分关于\\(\omega\\)的形式.

傅里叶积分存在的条件由**傅里叶积分定理**判定:
若函数 \\(f(x)\\) 在区间 \\((-\infty, \infty)\\) 上满足条件: \\((1) f(x)\\) 在 任一有限区间上满足狄里希利条件; (2) \\(f(x)\\) 在 \\((-\infty, \infty)\\)
上绝对可积 (即 \\(\int_{-\infty}^{\infty}|f(x)| dx\\) 收敛), 则 \\(f(x)\\) 可表示成傅里叶积分, 且

\\[
\text{傅里叶积分值} = \lim_{\epsilon\to 0} \frac{1}{2} \left[ f(x+\epsilon) + f(x-\epsilon) . \right]
\\]

若采用正余弦展开,

\\[
f(x) =\int_{0}^{\infty} A(\omega) \cos {\omega x} d\omega + \int_{0}^{\infty} B(\omega) \sin {\omega x} d\omega
\\]

其中

\\[
\left\{\begin{array}{l}
A(\omega)=\frac{1}{\pi} \int_{-\infty}^{\infty} f(x) \cos \omega x d x, \\\\
B(\omega)=\frac{1}{\pi} \int_{-\infty}^{\infty} f(x) \sin \omega x d x .
\end{array}\right.
\\]
上式还可以写成

\\[
f(x)=\int_0^{\infty} C(\omega) \cos [\omega x-\varphi(\omega)] d \omega,
\\]

其中

\\[
\begin{gathered}
C(\omega)=\sqrt{[A(\omega)]^2+[B(\omega)]^2} \\\\
\varphi(\omega)=\arctan [B(\omega) / A(\omega)] .
\end{gathered}
\\]

\\(C(\omega)\\) 称为 \\(f(x)\\) 的振幅谱, \\(\varphi(\omega)\\) 称为 \\(f(x)\\) 的相位谱.如果\\(f(x)\\)是奇函数或偶函数,
对应的级数为**傅里叶余弦积分**或**傅里叶正弦积分**.

复数形式的傅里叶积分可以写成对称的形式,

\\[
\begin{aligned}
f(x) & =\frac{1}{\sqrt{2 \pi}} \int_{-\infty}^{\infty} F(\omega)e^{\mathrm{i} \omega x} d \omega, \\\\
F(\omega) & =\frac{1}{\sqrt{2 \pi}} \int_{-\infty}^{\infty} f(x)\left[e^{\mathrm{i} \omega x}\right]^* d x .
\end{aligned}
\\]

并常用符号简写为

\\[
F(\omega)=\mathcal{F}[f(x)],   f(x)=\mathcal{F}^{-1}[F(\omega)] .
\\]

\\(f(x)\\) 和 \\(F(\omega)\\) 分别称为傅里叶变换的**原函数**和**像函数**.

> **例** 求以下函数的复数傅里叶变换.


- \\(f(x) = e^{-\alpha |x|}, \alpha > 0\\);

- \\(f(x) = \delta (x)\\);

- \\(f(x) = e^{-\alpha x^2}, \alpha > 0\\).

> **解**


- 对\\(x\\)分段进行处理,利用对称形式的傅里叶变换有


\\[
\begin{aligned}
        F(\omega) &=
        \sqrt{\frac{1}{2 \pi}} \int_{-\infty}^0 e^{\alpha x+i \omega t} dx
        +
        \sqrt{\frac{1}{2 \pi}} \int_0^{\infty} e^{-\alpha x+i \omega t} dx
        \\\\
        &= \sqrt{\frac{1}{2 \pi}} \left[\frac{1}{\alpha + \mathrm{i} \omega } + \frac{1}{\alpha - \mathrm{i} \omega } \right]
        \\\\
        &= \sqrt{\frac{1}{2 \pi}} \frac{2\alpha}{\alpha^2 + \omega^2},
\end{aligned}
\\]

越大的\\(\alpha\\)则\\(f(x)\\)越窄,集中在\\(x=0\\)附近,也就是越局域,而其傅里叶变换则越弥散.当\\(f(x)\\)是偶函数时,傅里叶变换的像函数为实函数.


- 代入


\\[
\begin{aligned}
        F(\omega) &=
        \sqrt{\frac{1}{2 \pi}} \int_{-\infty}^{\infty} \delta(x) e^{+\mathrm{i} \omega x} d x = \sqrt{\frac{1}{2 \pi}} ,
\end{aligned}
\\]

\\(f(x)\\)无限局域对应的傅里叶变换为无限弥散.


- 类似的,


\\[
\begin{aligned}
        F(\omega) &=\frac{1}{\sqrt{2 \pi}} \int_{-\infty}^{\infty} e^{-\alpha x^2} e^{\mathrm{i} \omega x} d x = \frac{ e^{-\omega^2 / 4\alpha }}{\sqrt{2 \pi}} \int_{-\infty}^{\infty} e^{-\alpha  \left( x - \frac{\mathrm{i} \omega}{2\alpha} \right)^2}  d x
        \\\\
        & = \frac{ e^{-\omega^2 / 4\alpha }}{\sqrt{2 \pi}} \int_{-\infty - \mathrm{i} \omega / 2\alpha}^{\infty - \mathrm{i} \omega / 2\alpha} e^{-\alpha t^2} dt
        \\\\
        & = \frac{ e^{-\omega^2 / 4\alpha }}{\sqrt{2 \pi}} \sqrt{\frac{\pi}{\alpha}}
        \\\\
            & = \frac{1}{\sqrt{2\alpha}} e^{- \frac{\omega^2}{4\alpha}}  .
\end{aligned}
\\]

上式用了变量代换\\(t = x - \mathrm{i} \omega /2 \alpha\\),高斯函数的像函数还是高斯函数.

### 傅里叶变换基本性质

傅里叶变换满足以下基本性质.假定\\(f(x)\\)的傅里叶变换存在,记为\\(\mathcal{F[f(x)] = F(\omega)\\).


- 导数定理


\\[
\mathcal{F} [f'(x)] = \mathrm{i} \omega F(\omega)
\\]


- 积分定理


\\[
\mathcal{F} [ \int^{x} f(x) dx ] = \frac{1}{\mathrm{i} \omega} F(\omega)
\\]


- 相似性定理


\\[
\mathcal{F} [ f(ax) ] = \frac{1}{a} F(\frac{\omega}{a}),
\\]


- 延迟定理


\\[
\mathcal{F} [ f(x - x_0 ) ] = e^{-\mathrm{i} \omega x_0} F(\omega),
\\]


- 位移定理


\\[
\mathcal{F} [ e^{\mathrm{i} \omega_0 x} f(x) ] = F(\omega - \omega_0),
\\]


- 卷积定理, 如果


\\[
\mathcal{F} [f_1(x)] =  F_1(\omega), \mathcal{F} [f_2(x)] =  F_2(\omega),
\\]

有


\\[
\mathcal{F} [f_1(x)\star f_2(x) ] = F_1(\omega) F_2(\omega).
\\]

其中 \\(f_1(x) \star f_2(x)=\int_{-\infty}^{\infty} f_1(\alpha) f_2(\alpha-x) d \alpha\\) 称为 \\(f_1(x)\\) 与 \\(f_2(x)\\) 的卷积.

以上部分定理作为作业由大家完成.

### 高维傅里叶变换

二维连续函数 \\(f(x, y)\\) 的傅里叶变换定义如下:
设 \\(f(x, y)\\) 是两个独立变量 \\(x, y\\) 的函数, 且在 \\(\pm \infty\\) 上绝对可积, 则定义积分

\\[
F\left(k_1, k_2\right)=\frac{1}{2 \pi} \int_{-\infty}^{\infty} \int_{-\infty}^{\infty} f(x, y) e^{-\mathrm{i}\left(k_1 x+k_2 y\right)} d x d y
\\]

为二维连续函数 \\(f(x, y)\\) 的傅里叶变换,并定义

\\[
f(x, y)=\int_{-\infty}^{\infty} \int_{-\infty}^{\infty} F\left(k_1, k_2\right) e^{\mathrm{i}\left(k_1 x+k_2 y\right)} d k_1 d k_2
\\]

为 \\(F\left(k_1, k_2\right)\\) 的逆变换.
\\(f(x, y)\\) 和 \\(F\left(k_1, k_2\right)\\) 称为傅里叶变换对. 注意这里可以取对称的形式,只有一个系数
\\(\frac{1}{(2 \pi)^2}\\), 结果与上面形式相同.

> **例** 求函数 \\(f(x, y)= \begin{cases}A, & |x| \leq X,|y| \leq Y \\ 0, & |x|>X,|y|>Y\end{cases}\\) 的傅里叶变换 (矩孔费琅和夫衍射).

> **解** 由傅里叶变换关系

\\[
F\left(k_1, k_2\right)=\frac{1}{(2 \pi)^2} \int_{-\infty}^{\infty} \int_{-\infty}^{\infty} f(x, y) e^{-i\left(k_1 x+k_2 y\right)} d x d y
\\]

有

\\[
\begin{aligned}
F\left(k_1, k_2\right) & =\frac{A}{2 \pi} \int_{-X}^X e^{-i k_1 x} d x \int_{-Y}^Y e^{-i k_2 y} d y \\\\
& =\left.\left.\frac{A}{2 \pi} \frac{1}{-i k_1} e^{-i k_1 x}\right|_{-X} ^X \frac{1}{-i k_2} e^{-i k_2 y}\right|_{-Y} ^Y \\\\
& =\frac{2A}{\pi} \frac{1}{i 2 k_1}\left(e^{i k_1 X}-e^{-i k_1 X}\right) \frac{1}{i 2 k_2}\left(e^{i k_2 Y}-e^{-i k_2 Y}\right) \\\\
& =\frac{2A X Y}{\pi} \frac{\sin \left(k_1 X\right)}{k_1 X} \frac{\sin \left(k_2 Y\right)}{k_2 Y}
\end{aligned}
\\]

对于三维情况,\\(\vec{k}=\left(k_1, k_2, k_3\right), \vec{r}=(x, y, z)\\),

\\[
F(\vec{k})=\frac{1}{(2 \pi)^3} \iiint_{-\infty}^{\infty} f(\vec{r}) e^{-\mathrm{i}  \vec{k} \cdot \vec{r}} d^3 \vec{r}
\\]

或者

\\[
F\left(k_1, k_2, k_3\right)=\frac{1}{(2 \pi)^3} \iiint_{\infty}^{\infty} f(x, y, z) e^{-\mathrm{i}\left(k_1 x+k_2 y+k_3 z\right)} d x d y d z
\\]

逆变换为

\\[
f(\vec{r})=\iiint_{-\infty}^{\infty} F(k) e^{\mathrm{i} \vec{k} \cdot \vec{r}} d^3 \vec{k}
\\]


或

\\[
f(x, y, z)=\iiint_{-\infty}^{\infty} F\left(k_1, k_2, k_3\right) e^{\mathrm{i}\left(k_1 x+k_2 y+k_3 z\right)} d k_1 d k_2 d k_3
\\]
