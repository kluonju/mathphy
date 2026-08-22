### 拉普拉斯积分变换的应用

拉普拉斯变换有很多应用,这里从三个方面的例子来说明.
#### 计算级数和

有时,拉普拉斯变换可以用来计算某些级数的和.以下面的例子说明.

如计算级数和

\\[
\sum_{n=1} ^{\infty}  \frac{1}{n^2},
\\]

由前面例题

\\[
\int_0^{\infty} t e^{-p t} d t=\frac{1}{p^2},   \Re p>0
\\]

将级数化为

\\[
\begin{aligned}
\sum_{n= 1}^{\infty} \frac{1}{n^2} & =\sum_{n=1}^{\infty} \int_0^{\infty} t e^{-n t} d t \\\\
& =\int_0^{\infty} t\left[\sum_{n=1}^{\infty} e^{-n t}\right] d t=\int_0^{\infty} \frac{t}{e^t-1} d t
\end{aligned}
\\]

查表可得

\\[
\sum_{n=1} ^{\infty}  \frac{1}{n^2} = \frac{\pi^2}{6}.
\\]

> **注** Use Parseval's identity (applied to the function \\(f(x)=x\\) ) to obtain



\\[
\sum_{n=-\infty}^{\infty}\left|c_n\right|^2=\frac{1}{2 \pi} \int_{-\pi}^\pi x^2 d x
\\]


where



\\[
\begin{aligned}
c_n & =\frac{1}{2 \pi} \int_{-\pi}^\pi x e^{-i n x} d x \\\\
& =\frac{n \pi \cos (n \pi)-\sin (n \pi)}{\pi n^2} i \\\\
& =\frac{\cos (n \pi)}{n} i \\\\
& =\frac{(-1)^n}{n} i
\end{aligned}
\\]


for \\(n \neq 0\\), and \\(c_0=0\\). Thus,



\\[
\left|c_n\right|^2= \begin{cases}\frac{1}{n^2}, & \text{for} n \neq 0 \\ 0, & \text{for} n=0\end{cases}
\\]


and



\\[
\sum_{n=-\infty}^{\infty}\left|c_n\right|^2=2 \sum_{n=1}^{\infty} \frac{1}{n^2}=\frac{1}{2 \pi} \int_{-\pi}^\pi x^2 d x
\\]



Therefore,



\\[
\sum_{n=1}^{\infty} \frac{1}{n^2}=\frac{1}{4 \pi} \int_{-\pi}^\pi x^2 d x=\frac{\pi^2}{6}
\\]


as required.

#### 求解定积分

如果 \\(\int_v^{\infty} \bar{f}(q) d q\\) 存在, 且当\\(t\to 0\\)时, \\(|f(t)/t|\\)有界,则

\\[
\int_{p}^{\infty} \bar{f}(q) dq  \Leftrightarrow  \frac{f(t)}{t} .
\\]

比如

\\[
\frac{\sin \omega t}{t}  \Leftrightarrow  \int_p^{\infty} \frac{\omega}{q^2+\omega^2} d q=\frac{\pi}{2}-\arctan \frac{p}{\omega}.
\\]

当\\(p\to 0\\)时, 有

\\[
\int_0^{\infty} \bar{f}(p) d p=\int_0^{\infty} \frac{f(t)}{t} d t
\\]

一个例子如

\\[
\int_0^{\infty} \frac{\sin t}{t} d t=\int_0^{\infty} \frac{1}{p^2+1} d p=\frac{\pi}{2}
\\]

不仅如此, 有些积分无法用留数定理计算,如

\\[
\int_0^{\infty} \frac{\cos a t-\cos b t}{t} d t   a>0, b>0
\\]

使用以上等式可得

\\[
\begin{gathered}
\int_0^{\infty} \frac{\cos a t-\cos b t}{t} d t  \Leftrightarrow  \int_0^{\infty}\left(\frac{p}{p^2+a^2}-\frac{p}{p^2+b^2}\right) d p \\ =\left.\frac{1}{2} \ln \frac{p^2+a^2}{p^2+b^2}\right|^{\infty}=\ln b-\ln a .
\end{gathered}
\\]

#### 求解微分方程

给一个例子,利用拉普拉斯变换求解简谐振子方程的解.

> **例** 利用拉普拉斯变换求解简谐振子方程的解.

> **解** 质量为\\(m\\)的质点在弹性系数为\\(k\\)的弹簧牵引下做简谐运动,满足方程为


\\[
m \frac{d^2 X(t)}{d t^2}+k X(t)=0
\\]

初始条件取

\\[
X(0)=X_0,   X^{\prime}(0)=0
\\]

应用拉氏变换到该方程上得到

\\[
m \mathcal{L}\left\{\frac{d^2 X}{d t^2}\right\}+k \mathcal{L}\{X(t)\}=0
\\]

用\\(x(p)\\)表示未知变换\\(\mathcal{L\{ X(t)\}\\),于是根据导数定理有

\\[
m p^2 x(p)-m p X_0+k x(p)=0,
\\]

化简为

\\[
x(p)=X_0 \frac{p}{p^2+\omega_0^2},   \omega_0^2 \equiv \frac{k}{m} .
\\]

查表得

\\[
X(t)=X_0 \cos \omega_0 t.
\\]

## 数值实验

### 方波傅里叶级数逼近

```python
# scripts/ch03_fourier_square_wave.py
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-np.pi, np.pi, 500)
f = np.sign(np.sin(x))
N_terms = [1, 3, 5, 21]
fig, axes = plt.subplots(2, 2, figsize=(8, 6))
for ax, N in zip(axes.flat, N_terms):
s = sum((4 / (n * np.pi)) * np.sin(n * x) for n in range(1, N + 1, 2))
ax.plot(x, f, "k--", label="方波")
ax.plot(x, s, label=f"N={N}")
ax.legend()
ax.set_title(f"奇次谐波至 n={N}")
plt.tight_layout()
plt.savefig("assets/figures/ch03_square_wave.png", dpi=120)
print("Saved assets/figures/ch03_square_wave.png")
```

```julia
# scripts/ch03_fourier_square_wave.jl
using Plots
x = range(-π, π, length=500)
f = sign.(sin.(x))
for N in [1, 3, 5, 21]
s = sum((4/(n*π)) * sin.(n*x) for n in 1:2:N)
plot(x, f, ls=:dash, label="方波", title="N=$N") plot!(x, s, label="部分和")
end
savefig("assets/figures/ch03_square_wave_julia.png")
println("Saved assets/figures/ch03_square_wave_julia.png")
```

### Laplace 变换验证（SymPy）

```python
# scripts/ch03_laplace_oscillator.py
from sympy import symbols, cos, laplace_transform, inverse_laplace_transform, simplify
t, p, X0, m, k = symbols("t p X0 m k", positive=True)
omega0 = (k / m) ** 0.5
x_p = X0 * p / (p**2 + omega0**2)
x_t = inverse_laplace_transform(x_p, p, t)
print("X(t) =", simplify(x_t))  # 应为 X0*cos(omega0*t)
```

运行：

```bash
cd concise-math-physics
pip install numpy matplotlib sympy
python scripts/ch03_fourier_square_wave.py
python scripts/ch03_laplace_oscillator.py
julia scripts/ch03_fourier_square_wave.jl
```
