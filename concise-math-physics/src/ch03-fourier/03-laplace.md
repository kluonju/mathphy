### 拉普拉斯变换

傅里叶变换在分析信号的频谱等方面是十分有效的,但在系统分析方面有不足之处:


- 对时间函数限制严格,绝对可积是充分条件,不少函数不能直接按定义求,如\\(e^{\alpha t}, \alpha > 0\\),其傅里叶变换不存在.


- 求解傅里叶反变换比较麻烦.

为了解决上述问题拓宽应用范围,人们发现适当地改造满足傅里叶变换的条件.
拉普拉斯变换常用于初始值问题, 即已知某个物理量在初始时刻 \\(t=0\\) 的 值 \\(f(0)\\), 而求解它在初始时刻之后的变化情况 \\(f(t)\\).
 至于它在初始时刻之前 的值, 我们置

\\[
f(t)=0,  (t<0) .
\\]

构造一个带收敛因子\\(e^{-\sigma t}, \sigma > 0\\)的函数

\\[
g(t) =e^{-\sigma t} f(t)
\\]

则\\(g(t)\\)绝对可积.于是对\\(g(t)\\)进行傅里叶变换:

\\[
g(\omega) = \frac{1}{2\pi}  \int\_{-\infty}^{\infty} g(t) e^{-\mathrm{i} \omega t} dt = \frac{1}{2\pi}  \int\_{0}^{\infty} f(t) e^{-(\sigma + \mathrm{i} \omega) t} dt
\\]

将\\(\sigma + \mathrm{i} \omega\\)记作\\(p\\),令\\(\bar{f(p)=2\pi g(\omega)\\),则有
函数\\(f(t)\\)的拉普拉斯变换\\(\bar{f(p)\\)为

\\[
\bar{f}(p) = \mathcal{L} \{ f(t) \} = \int\_0 ^{\infty} e^{-pt} f(t) dt .
\\]

该积分称为**拉普拉斯积分**,\\(\mathcal{L}\\)称为**拉普拉斯变换算符**.\\(e^{-pt\\)称为拉普拉斯变换的**核**.注意
这里的积分上下限.

\\(g(\omega)\\) 的傅里叶逆变换是

\\[
g(t)=\int\_{-\infty}^{\infty} g(\omega) e^{\mathrm{i} \omega t} d \omega=\frac{1}{2 \pi} \int\_{-\infty}^{\infty} \bar{f}(\sigma+\mathrm{i} \omega) e^{\mathrm{i} \omega t} d \omega,
\\]

即

\\[
f(t)=\frac{1}{2 \pi} \int\_{-\infty}^{\infty} \bar{f}(\sigma+\mathrm{i} \omega) e^{(\sigma+\mathrm{i} \omega)t} d \omega
\\]

由 \\(\sigma+\mathrm{i} \omega=p\\), 有 \\(d \omega=\frac{1{\mathrm{i}} d p\\). 所以

\\[
f(t)=\frac{1}{2 \pi \mathrm{i}} \int\_{\sigma-\mathrm{i} \infty}^{\sigma+\mathrm{i} \infty} \bar{f}(p) e^{ p t} d p .
\\]

\\(\bar{f}(p)\\) 又称为**像函数**, 而 \\(f(t)\\) 称为**原函数**, 它们之间的关系常用简单的符号写为

\\[
\begin{aligned}
& \bar{f}(p)=\mathcal{L}[f(t)], \\\\
& f(t)=\mathcal{L}^{-1}[\bar{f}(p)]
\end{aligned}
\\]

或

\\[
\begin{aligned}
& \bar{f}(p)  \Leftrightarrow  f(t), \\\\
& f(t)  \Leftrightarrow  \bar{f}(p) .
\end{aligned}
\\]

拉普拉斯变换存在的充分条件是


- [(1)]  在 \\(0 \leqslant t<\infty\\) 的任一有限区间上; 除了有限个间断点外, 函数 \\(f(t)\\) 及其导数是处处连续的;

- [(2)]  存在常数 \\(M>0\\) 和 \\(\sigma \geqslant 0\\), 使对任何 \\(t\\) 值 \\((0 \leqslant t<\infty)\\), 有


\\[
|f(t)|<M e^{\sigma t} \text {. }
\\]

\\(\sigma\\) 的下界称为收敛横标, 用 \\(\sigma\_0\\) 表示. 在实际应用中, 大多数函数都满足 这个充分条件.
但一个反例是\\(e^{t^2}\\). 对于满足拉普拉斯变换存在条件的函数,通过证明可以知道\\(\lim\_{p\to \infty \bar{f}(p) = 0\\).
也就意味着,若\\(\bar{f}(p)\\)在\\(p\to \infty\\)的渐近行为是\\(p\\)的正幂次,那么逆变换不存在. 且可以证明\\(\bar{f(p)\\)在\\(\Re \sigma > \sigma\_0\\)的半平面是解析的(具体证明
见梁昆淼书).
不难看出拉普拉斯变换为**线性变换**, 即满足

\\[
\mathcal{L}\{a f(t)+b g(t)\}=a \mathcal{L}\{f(t)\}+b \mathcal{L}\{g(t)\}  .
\\]

不言而喻的是, 傅里叶变换也是线性变换.

对于\\(\delta\\)函数,易知

\\[
\mathcal{L}\left\{\delta\left(t-t\_0\right)\right\}=\int\_0^{\infty} e^{-p t} \delta\left(t-t\_0\right) d t=e^{-p t\_0},    t\_0>0 .
\\]

> **例** 求以下函数的拉普拉斯变换



- \\(f(t) = 1\\),

- \\(f(t) = t\\),

- \\(f(t) =e^{s t}, \text{s为常数}\\),

- \\(f(t) = t e^{s t}, \text{s为常数}\\),

- \\(f(t) = \cosh {k t}\\), \\(g(t)= \sinh {kt\\).


> **解**


- \\(\Re p > 0\\),


\\[
\int\_{0}^{\infty} 1 \cdot e^{-p t} dt = \frac{1}{p}
\\]


- \\(\Re p > 0\\),


\\[
\int\_{0}^{\infty} t \cdot e^{-p t} dt = \frac{1}{p^2}
\\]

            因此类似有\\(\mathcal{L}[t^n] = \frac{n!}{p^{n+1}}\\).

-

\\[
\int\_{0}^{\infty} e^{s t} e^{-p t} dt = \frac{1}{p-s} ,
\\]

        要求\\(\Re (p-s) > 0\\).

-

\\[
\int\_{0}^{\infty} t e^{s t} e^{-p t} dt = \frac{1}{(p-s)^2} ,
\\]

        要求\\(\Re (p-s) > 0\\).
类似有 \\(\mathcal{L}[t^n e^{s t}] = \frac{n!}{(p-s)^{n+1}}\\).

- 利用


\\[
\cosh{k t}  = \frac{1}{2} \left[ e^{kt} + e^{-kt}\right]
         \sinh{k t}  = \frac{1}{2} \left[ e^{kt} - e^{-kt}\right]
\\]



\\[
\mathcal{L}[ \cosh{k t} ] = \frac{1}{2} \left( \frac{1}{p-k} + \frac{1}{p+k} \right) = \frac{p}{p^2 - k^2} ,
\\]



\\[
\mathcal{L}[ \sinh{k t} ] = \frac{1}{2} \left( \frac{1}{p-k} - \frac{1}{p+k} \right) = \frac{k}{p^2 - k^2} .
\\]



更多的拉普拉斯变换对见附录二(梁昆淼书).

### 拉普拉斯变换的性质

与傅里叶变换类似,拉氏变换\\(\bar{f}(p)\\)也满足很多基本性质.


- 导数定理


\\[
f^{\prime}(t)  \Leftrightarrow   p \bar{f}(p)-f(0),
\\]

        对于高阶导数有递推关系


\\[
f^{(n)}(t)  \Leftrightarrow  p^n \bar{f}(p)-p^{n-1} f(0)-p^{n-2} f^{\prime}(0)-\cdots-p f^{(n-2)}(0)-f^{(n-1)}(0)
\\]



- 积分定理


\\[
\int\_0^t \psi(\tau) d \tau  \Leftrightarrow   \frac{1}{p} \mathcal{L}[\psi(t)]
\\]


- 相似性定理


\\[
f(a t)  \Leftrightarrow
         \frac{1}{a} \bar{f}\left(\frac{p}{a}\right)
\\]



- 位移定理


\\[
e^{-\lambda t} f(t)  \Leftrightarrow   \bar{f}(p+\lambda)
\\]


- 延迟定理


\\[
f\left(t-t\_0\right)  \Leftrightarrow   e^{-p t\_0} \bar{f}(p).
\\]


- 卷积定理 若  \\(f\_1(t)  \Leftrightarrow   \bar{f}\_1(p), f\_2(t)  \Leftrightarrow   \bar{f}\_2(p)\\) , 则


\\[
f\_1(t) * f\_2(t)  \Leftrightarrow   \bar{f}\_1(p) \bar{f}\_2(p),
\\]

其中


\\[
f\_1(t) * f\_2(t) \equiv \int\_0^t f\_1(\tau) f\_2(t-\tau) d \tau
\\]

称为 \\(f\_1(t)\\) 与 \\(f\_2(t)\\) 的**卷积**.
