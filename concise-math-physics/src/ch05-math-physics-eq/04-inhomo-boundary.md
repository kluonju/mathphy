## 非齐次边界条件的处理

在 \\(\S 8.1\\) 和 \\(\S 8.2\\) 两节中, 不管是齐次还是非齐次振动方程和输运方程,它们的定解问题的解法都有一个前提：边界条件是齐次的.

但是, 在实际问题中, 常有非齐次边界条件出现, 那么, 这样的定解问题又如何求解呢? 由于定解问题是线性的,处理的原则是利用叠加原理,把非齐次边界条件问题转化为另一未知函数的齐次边界条件问题. 请看例题.

### (一) 一般处理方法

例 1 自由振动问题

\\[
\begin{gathered}
u\_{t t}-a^{2} u\_{x x}=0, \\\\
\left.u\right|\_{x=0}=\mu(t),\left.u\right|\_{x=l}=\nu(t), \\\\
\left.u\right|\_{t=0}=\varphi(x),\left.u\_{t}\right|\_{t=0}=\psi(x) .
\end{gathered}
\\]

边界条件 (8.3.2) 是非齐次的.
选取一个函数 \\(v(x, t)\\), 使其满足非齐次边界条件 (8.3.2), 为了简单起见, 不妨取 \\(v(x, t)\\) 为 \\(x\\) 的线性函数, 即

\\[
v(x, t)=A(t) x+B(t) \text {. }
\\]

将 (8.3.4) 代入 (8.3.2), 解得

\\[
v(x, t)=\frac{[\nu(t)-\mu(t)]}{l} x+\mu(t)
\\]

利用叠加原理, 令

\\[
u(x, t)=v(x, t)+w(x, t) .
\\]

将 (8.3.5)、(8.3.6) 代入定解问题 (8.3.1) (8.3.3), 得 \\(w(x, t)\\) 的定解问题

\\[
\begin{gathered}
w\_{t u}-a^{2} w\_{\mathrm{i} \mathrm{i}}=-v\_{\mathrm{i} t}+a^{2} v\_{x x}=\frac{x}{l}\left[\mu^{\prime \prime}(t)-\nu^{\prime \prime}(t)\right]-\mu^{\prime \prime}(t), \\\\
\left.w\right|\_{x=0}=0,\left.w\right|\_{x=l}=0, \\\\
\left.w\right|\_{t=0}=\varphi(x)-\left.v\right|\_{\mathrm{i}=0}=\varphi(x)+\frac{1}{l}[\mu(0)-\nu(0)] x-\mu(0), \\\\
\left.w\_{\mathrm{i}}\right|\_{\mathrm{i}=0}=\psi(x)-\left.v\_{t}\right|\_{t=0}=\psi(x)+\frac{1}{l}\left[\mu^{\prime}(0)-\nu^{\prime}(0)\right] x-\mu^{\prime}(0) .
\end{gathered}
\\]

虽然 \\(w(x, t)\\) 的方程 (8.3.7)一般是非齐次的,但是,定解问题 (8.3.7) (8.3.9) 具有齐次边界条件, 可按 \\(\S 8.2\\) 求解.

这里还要特别说一下 \\(x=0\\) 和 \\(x=l\\) 两端都是第二类非齐次边界条件 \\(\left.u\_{x\right|\_{x=0}\\) \\(=\mu(t),\left.u\_{x\right|\_{x=l}=\nu(t)\\) 的情况. 如果仍按 (8.3.4) 取 \\(x\\) 的线性函数作为 \\(v\\), 则代入非齐次边界条件得

\\[
\left.v\_{x}\right|\_{x=0}=A(t)=\mu(t),\left.  v\_{x}\right|\_{x=l}=A(t)=\nu(t) .
\\]

除非 \\(\mu(t)=\nu(t)\\), 否则这两式互相矛盾. 这时不妨改试

\\[
v(x, t)=A(t) x^{2}+B(t) x .
\\]

### (二) 特殊处理方法

例 2 弦的 \\(x=0\\) 端固定, \\(x=l\\) 端受迫作谐振动 \\(A \sin \omega t\\), 弦的初始位移和初始速度都是零, 求弦的振动. 这个定解问题是

\\[
\begin{gathered}
u\_{t t}-a^{2} u\_{x x}=0  (x<0<l), \\\\
\left.u\right|\_{x=0}=0,\left.  u\right|\_{x=l}=A \sin \omega t, \\\\
\left.u\right|\_{t=0}=0,\left.  u\_{t}\right|\_{t=0}=0 .
\end{gathered}
\\]

\\(x=l\\) 端为非齐次边界条件.

如果按上述一般处理方法, 应取 \\(v(x, t)=(A \sin \omega t / l) x\\), 但是, 相应的 \\(w(x, t)\\) 的定解问题中泛定方程为 \\(w\_{u-a^{2} w\_{x x}=-\left(v\_{u t}-a^{2} v\_{x x}\right)=\left(A \omega^{2} x / l\right) \sin \omega t\\),是非齐次方程, 求解麻烦. 能否有较为简便的方法呢?

由于求解的是弦在 \\(x=l\\) 端受迫作谐振动 \\(A \sin \omega t\\) 情况下的振动, 它一定有一个特解 \\(v(x, t)\\), 满足齐次方程 (8.3.11)、非齐次边界条件 (8.3.12), 且跟 \\(x\\)
\\(=l\\) 端同步振动, 即其时间部分的函数亦为 \\(\sin \omega t\\), 就是说, 特解具有分离变数的形式:

\\[
v(x, t)=X(x) \sin \omega t
\\]

将(8.3.14) 代入 (8.3.11)、

\\[
\begin{aligned}
& (8.3 .12), \text { 得 } \\\\
& \left\{\begin{array}{l}
X^{\prime \prime}+\left(\frac{\omega}{a}\right)^{2} X=0, \\\\
X(0)=0, X(l)=A .
\end{array}\right.
\end{aligned}
\\]

将常微分方程 (8.3.15) 的解 \\(X(x)=C \cos (\omega x / a)+D \sin (\omega x / a)\\) 代入 (8.3.16), 由此确定 \\(X(x)=[A / \sin (\omega l / a)] \sin (\omega x / a)\\), 从而

\\[
v(x, t)=\frac{A}{\sin \frac{\omega l}{a}} \sin \frac{\omega x}{a} \sin \omega t
\\]

于是令

\\[
u(x, t)=v(x, t)+w(x, t),
\\]

将 (8.3.17)、(8.3.18) 代入 (8.3.11) (8.3.13), 得 \\(w(x, t)\\) 的定解问题

\\[
\begin{gathered}
w\_{t t}-a^{2} w\_{x x}=-\left(v\_{x x}-a^{2} v\_{x x}\right)=0 \\\\
\left.w\right|\_{x=0}=0,\left.  w\right|\_{x=\mathrm{i}}=0 \\\\
\left.w\right|\_{\mathrm{i}=0}=0,\left.  w\_{\mathrm{i}}\right|\_{t=0}=-A \omega \frac{\sin (\omega x / a)}{\sin (\omega l / a)}
\end{gathered}
\\]

定解问题 (8.3.19) (8.3.21) 为齐次方程、齐次边界条件, 可用分离变数法求解, 其一般解由 (8.1.14) 给出, 因此,

\\[
w(x, t)=\sum\_{n=1}^{\infty}\left(A\_{n} \cos \frac{n \pi a}{l} t+B\_{n} \sin \frac{n \pi a}{l} t\right) \sin \frac{n \pi}{l} x
\\]

其中系数 \\(A\_{n}\\) 和 \\(B\_{n\\) 可由 (8.1.16) 确定, 得

\\[
\begin{aligned}
A\_{n} & =0 \\\\
B\_{n} & =\frac{2}{n \pi a} \int\_{0}^{l}(-A \omega) \frac{\sin (\omega \xi / a)}{\sin (\omega l / a)} \sin \frac{n \pi \xi}{l} d \xi \\\\
& =\frac{-2 A \omega}{n \pi a \sin (\omega l / a)}\left[-\frac{\sin (\omega / a+n \pi / l) \xi}{2(\omega / a+n \pi / l)}+\frac{\sin (\omega / a-n \pi / l) \xi}{2(\omega / a-n \pi / l)}\right]\_{0}^{l} \\\\
& =\frac{A \omega}{n \pi a \sin (\omega l / a)}\left[\frac{\sin (\omega l / a+n \pi)}{\omega / a+n \pi / l}-\frac{\sin (\omega l / a-n \pi)}{\omega / a-n \pi / l}\right] \\\\
& =(-1)^{n} \frac{A \omega}{n \pi a}\left[\frac{1}{\omega / a+n \pi / l}-\frac{1}{\omega / a-n \pi / l}\right] \\\\
& =(-1)^{n} \frac{2 A \omega}{a l} \cdot \frac{1}{\omega^{2} / a^{2}-n^{2} \pi^{2} / l^{2}} .
\end{aligned}
\\]

这样

\\[
\begin{aligned}
w(x, t)= & \frac{2 A \omega}{a l} \sum\_{n=1}^{\infty} \frac{1}{\omega^{2} / a^{2}-n^{2} \pi^{2} / l^{2}} \sin \frac{n \pi a t}{l} \sin \frac{n \pi x}{l}, \\\\
u(x, t)= & A \frac{\sin (\omega x / a)}{\sin (\omega l / a)} \sin \omega t \\\\
& +\frac{2 A \omega}{a l} \sum\_{n=1}^{\infty} \frac{1}{\omega^{2} / a^{2}-n^{2} \pi^{2} / l^{2}} \sin \frac{n \pi a t}{l} \sin \frac{n \pi x}{l} .
\end{aligned}
\\]
