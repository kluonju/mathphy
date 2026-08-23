### 拉普拉斯反变换

前面对于拉普拉斯反变换(亦称逆变换)

\\[
f(t) = \mathcal{L}^{-1} [ \bar{f}(p)],
\\]

其具体表达式为

\\[
f(t)=\frac{1}{2 \pi \mathrm{i}} \int\_{\sigma-\mathrm{i} \infty}^{\sigma+\mathrm{i} \infty} \bar{f}(p) e^{ p t} dp,
\\]

见式.该式是著名的Bromwich积分(也叫做Riemann-Mellin积分).
由于像函数\\(\bar{f}(p)\\)是解析函数是\\(p\\)的解析函数,上述积分可以通过留数定理求得.这里需要用到推广的
约旦定理(具体证明略去).

**推广的约当引理** 设 \\(C\_R\\) 是以 \\(p=0\\) 为圆心, 以 \\(R\\) 为半径的圆周在直线 \\(\Re p=a(>0)\\) 左侧的圆弧. 若当 \\(|p| \rightarrow \infty\\) 时, \\(\bar{f(p)\\) 在 \\(\frac{\pi{2}-\delta \leqslant \operatorname{Arg} p \leqslant \frac{3}{2} \pi+\delta\\) 中一致趋于零 ( \\(\delta\\) 是小于 \\(\frac{\pi{2}\\) 的任意正数), 则

\\[
\lim \_{R \rightarrow \infty} \int\_{C\_R} \bar{f}(p) e^{p t} d p=0  (t>0) .
\\]

由于所作路径是在\\(\Re p = a\\)左半平面,而右半平面\\(\bar{f(p)\\)解析, 最终我们得到

\\[
f(t) = \sum\_{p\_j \in \text{全平面}} Res [ \bar{f}(p\_j) e^{p\_j t}].
\\]

> **例** 利用Bromwich积分求解\\(1/\sqrt{p}\\)的拉普拉斯变换原函数.

> **解** 求解参考梁昆淼书.
被积函数有唯一的奇点 \\(p=0\\), 这是极点型支点, 在考虑回路积分时,
不能像简单地加上圆弧 \\(C\_R\\), 因为在函数的多值区域不能作积分运算及应用留数定理.
为此, 先自 \\(p=0\\) 沿负实轴至 \\(\infty\\) 将 \\(p\\) 平面切割开,
再作如图回路, 然后在被积函数的一个单值分支上作积分运算,并应用留数定理.
被积函数在回路所围区域上无奇点,
     圆弧 \\(C\_R\\) 和圆 \\(C\_{\varepsilon\\)均以原点为圆心,
     半径分别为 \\(R\\) 和 \\(\varepsilon\\). 令 \\(R \rightarrow \infty\\),
     由推广的约当引理知, \\(\lim \_{R \rightarrow \infty} \int\_{C\_R}=0\\),
     同时不难验证 \\(\lim \_{s \rightarrow 0} \int\_{C\_s}=0\\).
     于是,

\\[
f(t)=\int\_{a-\mathrm{i} \infty}^{a+\mathrm{i} \infty} \frac{e^{p t}}{\sqrt{p}} d p=-\frac{1}{2 \pi \mathrm{i}} \lim \_{R \rightarrow \infty}\left(\int\_{l\_1}+\int\_{l\_2}\right) \frac{e^{p t}}{\sqrt{p}} d p .
\\]

\\(p\\) 在割线下沿 \\(l\_1\\) 和上沿 \\(l\_2\\) 上的辐角分别为 \\(-\pi\\) 和 \\(\pi\\). 这样, 在 \\(l\_1\\) 上, \\(\sqrt{p}=\sqrt{|p|} e^{-\mathrm{i} \pi / 2}=\\) \\(-\mathrm{i} \sqrt{|p|}\\); 在 \\(l\_2\\) 上 \\(\sqrt{p}=\sqrt{|p|} e^{\mathrm{i} \pi / 2}=\mathrm{i} \sqrt{|p|}\\). 于是,

\\[
\begin{aligned}
f(t) & =-\frac{1}{2 \pi \mathrm{i}} \int\_0^{-\infty} e^{p t} \frac{1}{-\mathrm{i} \sqrt{|p|}} d p-\frac{1}{2 \pi \mathrm{i}} \int\_{-\infty}^0 e^{p t} \frac{1}{\mathrm{i} \sqrt{|p|}} d p \\\\
& =\frac{1}{\pi} \int\_{-\infty}^0 e^{p t} \frac{1}{\sqrt{|p|}} d p .
\end{aligned}
\\]

改用 \\(y=\sqrt{|p| t}\\) 作为积分变数,

\\[
\begin{aligned}
f(t) & =\frac{1}{\pi} \int\_{\infty}^0 e^{-y^2} \frac{\sqrt{t}}{y}\left(-\frac{2 y}{t} d y\right) \\\\
& =\frac{2}{\pi \sqrt{t}} \int\_0^{\infty} e^{-y^2} d y=\frac{2}{\pi \sqrt{t}} \cdot \frac{\sqrt{\pi}}{2}=\frac{1}{\sqrt{\pi t}} .
\end{aligned}
\\]

很多时候,我们并不总需要用上述方法求解,对于有些问题,可以使用利用拉普拉斯变换的性质结合常见函数的表达式来求解.
对于像函数的导数, \\(f(t)\\)是满足Laplace变换的充分条件,那么\\(\bar{f(p)\\)在
\\(\Re p > \sigma\_0\\)的半平面解析,
于是求\\(n\\)阶导数得

\\[
\bar{f}^{(n)}(p)=\frac{d^{n}}{d p^n} \int\_0^{\infty} f(t) e^{-p t} d t=\int\_0^{\infty}(-t)^n f(t) e^{-p t} d t
\\]

所以有

\\[
\bar{f}^{(n)}(p) \Leftrightarrow  (-t)^n f(t)
\\]

不难发现,

\\[
\begin{aligned}
& \frac{1}{p^2}=-\frac{d}{d p} \frac{1}{p}  \Leftrightarrow   t \\\\
& \frac{1}{p^3}=\frac{1}{2} \frac{d^2}{d p^2} \frac{1}{p}  \Leftrightarrow  \frac{1}{2} t^2 .
\end{aligned}
\\]

例如, 利用留数性质可以用待定系数法分解

\\[
\begin{aligned}
\frac{1}{p^3(p+\alpha)} & =\frac{1}{\alpha} \frac{1}{p^3}-\frac{1}{\alpha^2} \frac{1}{p^2}+\frac{1}{\alpha^3} \frac{1}{p}-\frac{1}{\alpha^3} \frac{1}{p+\alpha} \\\\
&  \Leftrightarrow  \frac{1}{2 \alpha} t^2+\frac{1}{\alpha^2} t+\frac{1}{\alpha^3}-\frac{1}{\alpha^3} e^{-\alpha t}
\end{aligned}
\\]

> **例** 求 \\(\frac{e^{-\alpha p}}{p(p+b)}\\) 的原函数.

> **解** \\(\frac{1}{p}  \Leftrightarrow  \Theta(t)\\), 应用延迟定理,


\\[
e^{-\alpha p} / p  \Leftrightarrow  \Theta(t-\alpha) \text {. 又 } 1 /(p+b)  \Leftrightarrow  e^{-b t} \text {. }
\\]

这样, 本题给的像函数可以看作 \\(e^{-\alpha p} / p\\) 与 \\(1 /(p+b)\\) 的乘积, 应用卷积定理,即得

\\[
\begin{aligned}
\frac{e^{-\alpha p}}{p(p+b)} &  \Leftrightarrow  \int\_0^t \Theta(\tau-\alpha) e^{-b(t-\tau)} d \tau \\\\
& =\Theta(t-\alpha) \int\_\alpha^t e^{-b(t-\tau)} d \tau \\\\
& =\Theta(t-\alpha)\left[\frac{1}{b} e^{-b(t-\tau)}\right]\_\alpha^t \\\\
& =\frac{1}{b}\left[1-e^{-b(t-\tau)}\right] \Theta(t-\alpha) .
\end{aligned}
\\]

读者也可以运用裂项分解分母来求解验证.
