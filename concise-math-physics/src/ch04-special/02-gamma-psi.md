## \\(\Gamma\\)函数和\\(B\\)函数
\\(\Gamma\\)函数是特殊函数里最常见的. 对于整数变量,作为阶乘,它出现在每一个泰勒展开里.对于半整数变量,
许多函数的展开也会用上.

### \\(\Gamma\\)函数定义和性质

\\(\Gamma\\)函数的第一个定义由欧拉给出

\\[
\Gamma(z) \equiv \lim _{n \rightarrow \infty} \frac{1 \cdot 2 \cdot 3 \cdots n}{z(z+1)(z+2) \cdots(z+n)} n^{z},   z \neq 0,-1,-2,-3, \ldots
\\]

这里的\\(z\\)可以是实数也可以是复数. 于是我们有最基本的递推关系

\\[
\begin{aligned}
\Gamma(z+1) & =\lim _{n \rightarrow \infty} \frac{1 \cdot 2 \cdot 3 \cdots n}{(z+1)(z+2)(z+3) \cdots(z+n+1)} n^{z+1} \\\\
& =\lim _{n \rightarrow \infty} \frac{n z}{z+n+1} \cdot \frac{1 \cdot 2 \cdot 3 \cdots n}{z(z+1)(z+2) \cdots(z+n)} n^{z} \\\\
& =z \Gamma(z) .
\end{aligned}
\\]

由定义可得

\\[
\Gamma(1)=\lim _{n \rightarrow \infty} \frac{1 \cdot 2 \cdot 3 \cdots n}{1 \cdot 2 \cdot 3 \cdots n(n+1)} n=1
\\]

进而得到阶乘的表达式

\\[
\Gamma(n)=1 \cdot 2 \cdot 3 \cdots(n-1)=(n-1) ! .
\\]

\\(\Gamma\\)函数的第二个定义也由欧拉给出,以第二类欧拉积分的形式给出

\\[
\Gamma(z) \equiv \int_{0}^{\infty} e^{-t} t^{z-1} d t,   \Re z>0 .
\\]

这里的\\(z\\)的限制是为了避免积分发散. 当变量代换的时候,常常可以化成以下两个形式

\\[
\Gamma(z)=2 \int_{0}^{\infty} e^{-t^{2}} t^{2 z-1} d t,   \Re z>0
\\]

和

\\[
\Gamma(z)=\int_{0}^{1}\left[\ln \left(\frac{1}{t}\right)\right]^{z-1} d t,   \Re z>0
\\]

当\\(z=\frac{1}{2}\\), 可以利用高斯积分求得

\\[
\Gamma\left(\frac{1}{2}\right)=\sqrt{\pi}
\\]

\\(\Gamma\\)函数的第三个定义也由Weierstrass给出,以无穷乘积形式给出

\\[
\frac{1}{\Gamma(z)} \equiv z e^{\gamma z} \prod_{n=1}^{\infty}\left(1+\frac{z}{n}\right) e^{-z / n}
\\]

其中\\(\gamma\\)为Euler-Mascheroni常数

\\[
\gamma=0.5772156619 \cdots
\\]

\\(\Gamma\\)函数有以下性质:


- \\(\Gamma(z)\\)函数在全平面解析(除\\(z=0, -1, -2, \cdots\\)).

- 反射公式


\\[
\Gamma(z) \Gamma(1-z)=\frac{\pi}{\sin z \pi}
\\]

 证明见后. \\(\Gamma(\frac{1}{2}) = \sqrt{\pi}\\).

- 倍乘公式


\\[
\Gamma(1+z) \Gamma\left(z+\frac{1}{2}\right)=2^{-2 z} \sqrt{\pi} \Gamma(2 z+1)
\\]


- 单极点\\(z=-n\\)处的留数


\\[
\begin{aligned}
Res \Gamma(z=-n) & =\lim _{\varepsilon \rightarrow 0}(\varepsilon \Gamma(-n+\varepsilon))=\lim _{\varepsilon \rightarrow 0} \frac{\varepsilon \Gamma(-n+1+\varepsilon)}{-n+\varepsilon}=\lim _{\varepsilon \rightarrow 0} \frac{\varepsilon \Gamma(-n+2+\varepsilon)}{(-n+\varepsilon)(-n+1+\varepsilon)} \\\\
& =\lim _{\varepsilon \rightarrow 0} \frac{\varepsilon \Gamma(1+\varepsilon)}{(-n+\varepsilon) \cdots(\varepsilon)}=\frac{(-1)^{n}}{n !},
\end{aligned}
\\]

> **例** Maxwell-Boltzmann分布

> **解** 经典统计物理中, Maxwell-Boltzmann分布能量为\\(E\\)的状态被占据的概率正比于
\\(e^{-E/kT}\\), \\(k\\)为玻尔兹曼常数, \\(T\\)为绝对温度. 常记\\(\beta=1 / k T\\)
在\\(E\\)到\\(E+dE\\)区间内的占据概率为\\(C n(E) e^{-\beta E dE\\), 其中\\(n(E)dE\\)为
状态数目. 归一化条件要求


\\[
1=C \int n(E) e^{-\beta E} d E
\\]

体系能量可以由下式求得


\\[
\langle E\rangle=C \int E n(E) e^{-\beta E} d E
\\]

对于理想气体来说态密度函数\\(n(E)\\)正比于\\(E^{1/2\\), 因此可得到归一化系数


\\[
1=C \int_0^{\infty} E^{1 / 2} e^{-\beta E} d E=C \frac{\Gamma\left(\frac{3}{2}\right)}{\beta^{3 / 2}}=C \frac{\sqrt{\pi}}{2 \beta^{3 / 2}},   \text { or } C=\frac{2 \beta^{3 / 2}}{\sqrt{\pi}}
\\]

进而得到平均能量为


\\[
\begin{aligned}
\langle E\rangle
        &=C \int_{0}^{\infty} E^{3 / 2} e^{-\beta E} d E
        \\\\
        &=C \frac{\Gamma\left(\frac{5}{2}\right)}{\beta^{5 / 2}}
        \\\\
        &=\left(\frac{2 \beta^{3 / 2}}{\sqrt{\pi}}\right)
        \frac{\sqrt{\pi}}{\beta^{5 / 2}}\left(\frac{1}{2} \cdot \frac{3}{2}\right)
        \\\\
        &=\frac{3}{2} k T.
\end{aligned}
\\]

### \\(B\\)
贝塔函数由第一类欧拉积分定义的

\\[
B(p, q) = \int_0^1 t^{p -1} (1-t)^{q-1} dt, \Re p> 0, \Re q >0.
\\]

令\\(t=\sin^2{\theta}\\), 可以得到另一种形式

\\[
B(p, q)  = 2\int_{0}^{\pi/2} \sin ^{2p -1}{\theta} \cos^{2q -1}{\theta} d\theta.
\\]

我们可以通过\\(\Gamma\\)函数表达\\(B\\)函数

\\[
B(p, q)=\frac{\Gamma(p) \Gamma(q)}{\Gamma(p+q)}
\\]

上式证明如下.

\\[
\Gamma(p) \Gamma(q)=4 \int_{0}^{\infty} s^{2 p-1} e^{-s^{2}} d s \int_{0}^{\infty} t^{2 q-1} e^{-t^{2}} d t
\\]

利用极坐标代换
 \\(s=r \cos \theta, t=r \sin \theta, r^{2}=s^{2}+t^{2}\\),  \\(d s d t=r d r d \theta\\).
 得到


\\[
\begin{aligned}
 \Gamma(p) \Gamma(q) & =4 \int_{0}^{\infty} r^{2 p+2 q-1} e^{-r^{2}} d r \int_{0}^{\pi / 2} \cos ^{2 p-1} \theta \sin ^{2 q-1} \theta d \theta \\\\
 & =2 \Gamma(p+q) \int_{0}^{\pi / 2} \cos ^{2 p-1} \theta \sin ^{2 q-1} \theta d \theta,
 \end{aligned}
\\]

 由式可得.

令\\(p=z, q=1-z\\)可以得到\\(\Gamma\\)函数的反射公式

\\[
B(z, 1-z) = \int_0^{1} t^{z-1} (1-t)^{-z} dt = \int_0^{\infty} \frac{x^{z-1}}{1+x} dx = \frac{\pi}{\sin{\pi z} },
\\]

上式做了\\(x = t/(1-t)\\)的代换,并利用留数定理的例题.

利用B函数可以倍乘公式. 事实上,

\\[
\begin{aligned}
\frac{\Gamma(z) \Gamma(z)}{\Gamma(2 z)} & =B(z, z)=\int_{0}^{1} t^{z-1}(1-t)^{z-1} d t \\\\
& =2 \int_{0}^{\frac{1}{2}} t^{z-1}(1-t)^{z-1} d t
\end{aligned}
\\]

作变量代换 \\(t=\frac{1-\sqrt{\xi}}{2}\\), 得到

\\[
\begin{aligned}
\frac{\Gamma(z) \Gamma(z)}{\Gamma(2 z)} & =2^{1-2 z} \int_{0}^{1}(1-\xi)^{z-1} \xi^{-\frac{1}{2}} d \xi \\\\
& =2^{1-2 z} \mathrm{~B}\left(z, \frac{1}{2}\right)=2^{1-2 z} \frac{\Gamma(z) \Gamma\left(\frac{1}{2}\right)}{\Gamma\left(z+\frac{1}{2}\right)}
\end{aligned}
\\]

## \\(\psi\\)函数
\\(\psi\\) 函数是 \\(\Gamma\\) 函数的对数微商

\\[
\psi(z)=\frac{d \ln \Gamma(z)}{d z}=\frac{\Gamma^{\prime}(z)}{\Gamma(z)}
\\]

根据 \\(\Gamma\\) 函数的性质,可以得出 \\(\psi(z)\\) 的下列性质：


- \\(z=0,-1,-2, \cdots\\) 都是 \\(\psi(z)\\) 的一阶极点, 留数均为 -1 ; 除了这些点以外, \\(\psi(z)\\) 在全平面解析.

-

\\[
\begin{aligned}
\psi(z+1) & =\psi(z)+\frac{1}{z} \\\\
\psi(z+n) & =\psi(z)+\frac{1}{z}+\frac{1}{z+1}+\cdots+\frac{1}{z+n-1},   n=2,3, \cdots
\end{aligned}
\\]


- \\(\psi(1-z)=\psi(z)+\pi \cot \pi z\\).

- \\(\psi(z)-\psi(-z)=-\frac{1}{z}-\pi \cot \pi z\\).

- \\(\psi(2 z)=\frac{1}{2} \psi(z)+\frac{1}{2} \psi\left(z+\frac{1}{2}\right)+\ln 2\\).

- \\(\lim _{n \rightarrow \infty}[\psi(z+n)-\ln n]=0\\).

\\(\psi\\) 函数的特殊值有

\\[
\begin{array}{ll}
\psi(1)=-\gamma, & \psi^{\prime}(1)=\frac{\pi^{2}}{6}, \\\\
\psi\left(\frac{1}{2}\right)=-\gamma-2 \ln 2, & \psi^{\prime}\left(\frac{1}{2}\right)=\frac{\pi^{2}}{2} \\\\
\psi\left(-\frac{1}{2}\right)=-\gamma-2 \ln 2+2, & \psi^{\prime}\left(-\frac{1}{2}\right)=\frac{\pi^{2}}{2}+4, \\\\
\psi\left(\frac{1}{4}\right)=-\gamma-\frac{\pi}{2}-3 \ln 2, & \psi\left(\frac{3}{4}\right)=-\gamma+\frac{\pi}{2}-3 \ln 2, \\\\
\psi\left(\frac{1}{3}\right)=-\gamma-\frac{\pi}{2 \sqrt{3}}-\frac{3}{2} \ln 3, & \psi\left(\frac{2}{3}\right)=-\gamma+\frac{\pi}{2 \sqrt{3}}-\frac{3}{2} \ln 3 .
\end{array}
\\]

其中 \\(\gamma=-\psi(1)\\) 是数学中的一个基本常数, 称为 Euler 常数.

利用 \\(\psi\\) 函数, 可以方便地求出通项为有理式的无穷级数

\\[
\sum_{n=0}^{\infty} u_{n}=\sum_{n=0}^{\infty} \frac{p(n)}{d(n)}
\\]

之和, 其中 \\(p(n)\\) 和 \\(d(n)\\) 都是 \\(n\\) 的多项式. 为了保证级数收敛, \\(p(n)\\)的次数至少要比 \\(d(n)\\) 的次数低 2 , 即

\\[
\lim _{n \rightarrow \infty} u_{n}=\lim _{n \rightarrow \infty} n \cdot u_{n}=0
\\]

如果 \\(d(n)\\) 是 \\(n\\) 的 \\(m\\) 次多项式, 并且全部零点都是一阶零点,

\\[
d(n)=\left(n+\alpha_{1}\right)\left(n+\alpha_{2}\right) \cdots\left(n+\alpha_{m}\right)
\\]

即 \\(u_{n}\\) 只有一阶极点, 则可部分分式为

\\[
u_{n}=\frac{p(n)}{d(n)}=\sum_{k=1}^{m} \frac{a_{k}}{n+a_{k}}
\\]

利用 \\(\psi\\) 函数的递推关系, 即可求得

\\[
\begin{aligned}
\sum_{n=0}^{N} u_{n} & =\sum_{k=1}^{m} a_{k}\left[\psi\left(\alpha_{k}+N\right)-\psi\left(\alpha_{k}\right)\right] \\\\
& =\sum_{k=1}^{m} a_{k}\left[\psi\left(\alpha_{k}+N\right)-\ln N-\psi\left(\alpha_{k}\right)\right]
\end{aligned}
\\]

其中利用了 \\(\sum_{k=1}^{m} a_{k}=0\\). 取极限 \\(N \rightarrow \infty\\), 即得

\\[
\begin{aligned}
\sum_{n=0}^{\infty} u_{n} & =\lim _{N \rightarrow \infty} \sum_{k=1}^{m} a_{k}\left[\psi\left(\alpha_{k}+N\right)-\ln N-\psi\left(\alpha_{k}\right)\right] \\\\
& =\lim _{N \rightarrow \infty} \sum_{k=1}^{m} a_{k}\left[\psi\left(\alpha_{k}+N\right)-\ln N\right]-\sum_{k=:}^{m} a_{k} \psi\left(\alpha_{k}\right) \\\\
& =-\sum_{k=1}^{m} a_{k} \psi\left(\alpha_{k}\right)
\end{aligned}
\\]

> **例** 求无穷级数 \\(\sum_{n=0}^{\infty} \frac{1}{(3 n+1)(3 n+2)(3 n+3)}\\) 之和.

> **解** 因为

\\[
\frac{1}{(3 n+1)(3 n+2)(3 n+3)}=\frac{1}{6} \frac{1}{n+i / 3}-\frac{1}{3} \frac{1}{n+2 / 3}+\frac{1}{6} \frac{1}{n+1}
\\]

所以, 根据上面给出的求和公式, 有

\\[
\sum_{n=0}^{\infty} \frac{1}{(3 n+1)(3 n+2)(3 n+3)}=-\frac{1}{6}\left[\psi\left(\frac{1}{3}\right)-2 \psi\left(\frac{2}{3}\right)+\psi(1)\right]
\\]

代入 \\(\psi\\) 函数的特殊值, 即得

\\[
\sum_{n=0}^{\infty} \frac{1}{(3 n+1)(3 n+2)(3 n+3)}=\frac{1}{4}\left[\frac{\pi}{\sqrt{3}}-\ln 3\right]
\\]

> **例** 求无穷级数 \\(\sum_{n=0}^{\infty} \frac{1}{n^{2}+a^{2}}\\) 之和, 其中 \\(a>0\\).

> **解** 因为

\\[
\frac{1}{n^{2}+a^{2}}=\frac{\mathrm{i}}{2 a}\left(\frac{1}{n+\mathrm{i} a}-\frac{1}{n-\mathrm{i} a}\right),
\\]

所以

\\[
\sum_{n=0}^{\infty} \frac{1}{n^{2}+a^{2}}=-\frac{\mathrm{i}}{2 a}[\psi(\mathrm{i} a)-\psi(-\mathrm{i} a)]
\\]

利用上面列出的 \\(\psi\\) 函数的性质,

\\[
\psi(\mathrm{i} a)-\psi(-\mathrm{i} a)=-\frac{1}{\mathrm{i} a}-\pi \cot \mathrm{i} \pi a=\mathrm{i}\left[\frac{1}{a}+\pi \coth \pi a\right]
\\]

就可以求得

\\[
\sum_{n=0}^{\infty} \frac{1}{n^{2}+a^{2}}=\frac{1}{2 a^{2}}[1+\pi a \coth \pi a]
\\]
