## 电磁学中的数学方法

本节从 Warwick PX284《Electromagnetic Theory and Optics》中，抽取与本书**数学物理方法**直接相关的部分：连续方程、静电势的 Poisson/Laplace 方程、由 Maxwell 方程导出波动方程，以及平面波的复指数表示。物理动机从简；完整电磁学/光学内容请参阅原讲义。

### 电荷守恒与连续方程

设体积 \\(V\\) 内总电荷 \\(Q=\int\_V\rho\,\mathrm{d}V\\)。若电荷不凭空产生，则 \\(Q\\) 的减少率等于穿出封闭面 \\(S=\partial V\\) 的电流：

\\[
\frac{\mathrm{d}Q}{\mathrm{d}t}
= \frac{\mathrm{d}}{\mathrm{d}t}\int\_V\rho\,\mathrm{d}V
= -\oint\_S \mathbf{J}\cdot\mathrm{d}\mathbf{S} .
\\]

对右端用 Gauss 定理，并把时间导数移入积分（\\(V\\) 固定），得

\\[
\int\_V\Bigl(\frac{\partial\rho}{\partial t}+\nabla\cdot\mathbf{J}\Bigr)\mathrm{d}V=0 .
\\]

对任意区域成立，故被积函数为零，即**连续方程**

\\[
\frac{\partial\rho}{\partial t}+\nabla\cdot\mathbf{J}=0 .
\\]

同类结构也出现在质量守恒（\\(\partial\_t\rho+\nabla\cdot(\rho\mathbf{v})=0\\)）、量子力学概率守恒等处：局域“密度变化”与“通量散度”相互抵消。

### 真空中的 Maxwell 方程（汇总）

在自由空间中（SI），Maxwell 方程组可写成

\\[
\begin{aligned}
\nabla\cdot\mathbf{E}
&= \frac{\rho}{\varepsilon\_0}, \\\\
\nabla\cdot\mathbf{B}
&= 0, \\\\
\nabla\times\mathbf{E}
&= -\frac{\partial\mathbf{B}}{\partial t}, \\\\
\nabla\times\mathbf{B}
&= \mu\_0\mathbf{J}+\mu\_0\varepsilon\_0\frac{\partial\mathbf{E}}{\partial t} .
\end{aligned}
\\]

最后一项 \\(\varepsilon\_0\partial\_t\mathbf{E}\\) 称为**位移电流密度**。它保证与连续方程相容：若仅写 \\(\nabla\times\mathbf{B}=\mu\_0\mathbf{J}\\)，两边取散度会得到 \\(\nabla\cdot\mathbf{J}=0\\)，与 \\(\partial\_t\rho\neq 0\\) 矛盾；用 \\(\rho=\varepsilon\_0\nabla\cdot\mathbf{E}\\) 代入连续方程，可见必须把 \\(\mathbf{J}\\) 换成 \\(\mathbf{J}+\varepsilon\_0\partial\_t\mathbf{E}\\)。

积分形式经 Gauss / Stokes 定理“局域化”即得上述微分方程——这正是第 [0 章](../ch00-prerequisites/05-vector-analysis.md) 所练的向量分析。

### 静电学：Poisson 与 Laplace 方程

静止情形 \\(\partial\_t\equiv 0\\) 时，非平凡方程为

\\[
\nabla\cdot\mathbf{E}=\frac{\rho}{\varepsilon\_0},
\qquad
\nabla\times\mathbf{E}=\mathbf{0} .
\\]

\\(\nabla\times\mathbf{E}=\mathbf{0}\\) 意味着静电场是**保守场**，可写为标量势的负梯度：

\\[
\mathbf{E}=-\nabla\psi .
\\]

代入 Gauss 定律得 **Poisson 方程**

\\[
\nabla^2\psi = -\frac{\rho}{\varepsilon\_0} .
\\]

无电荷区域 \\(\rho=0\\) 则化为 **Laplace 方程**

\\[
\nabla^2\psi = 0 .
\\]

熟悉的特解包括匀强场势 \\(\psi=-Ex\\)，以及 Coulomb 势 \\(\psi=q/(4\pi\varepsilon\_0 r)\\)。导体边界上电位给定时，求解静电边值问题即是在相应区域解 Laplace/Poisson 方程——这与第 5 章椭圆型方程、第 7 章分离变量法直接衔接。

**例（正弦边界的衰减解）** 平面 \\(z=0\\) 上给定 \\(\psi(x,0)=V\_0\cos kx\\)，且与 \\(y\\) 无关，\\(z\to+\infty\\) 时势趋于有界。Laplace 方程化为

\\[
\frac{\partial^2\psi}{\partial x^2}+\frac{\partial^2\psi}{\partial z^2}=0 .
\\]

分离变量或观察可得形如 \\(\psi=V\_0 e^{-|k|z}\cos kx\\)（取 \\(z>0\\)、衰减解）满足方程与边界条件：横向振荡伴随法向指数衰减——这是 Laplace 方程边值问题的典型行为。

### 由 Maxwell 方程导出波动方程

真空、无源（\\(\rho=0,\mathbf{J}=\mathbf{0}\\)）时，

\\[
\nabla\times\mathbf{E}=-\partial\_t\mathbf{B},
\qquad
\nabla\times\mathbf{B}=\mu\_0\varepsilon\_0\partial\_t\mathbf{E} .
\\]

对第一式取旋度，并交换 \\(\partial\_t\\) 与 \\(\nabla\\)：

\\[
\nabla\times(\nabla\times\mathbf{E})
= -\partial\_t(\nabla\times\mathbf{B})
= -\mu\_0\varepsilon\_0\partial\_t^2\mathbf{E} .
\\]

用恒等式 \\(\nabla\times(\nabla\times\mathbf{E})=\nabla(\nabla\cdot\mathbf{E})-\nabla^2\mathbf{E}\\)，且 \\(\nabla\cdot\mathbf{E}=0\\)，得

\\[
\nabla^2\mathbf{E}=\mu\_0\varepsilon\_0\frac{\partial^2\mathbf{E}}{\partial t^2} .
\\]

同理有 \\(\nabla^2\mathbf{B}=\mu\_0\varepsilon\_0\partial\_t^2\mathbf{B}\\)。与标准波动方程 \\(\nabla^2\psi=v^{-2}\partial\_t^2\psi\\) 比较，真空中电磁波相速为

\\[
c=\frac{1}{\sqrt{\mu\_0\varepsilon\_0}} .
\\]

（历史上 Maxwell 由此推断光是电磁波。）这与第 5 章弦/膜的波动方程同属双曲型；差别在于这里的未知量是向量场，且还受 \\(\nabla\cdot\mathbf{E}=0\\) 等约束。

### 平面波与复指数表示

设

\\[
\mathbf{E}=\mathbf{E}\_0\,e^{\mathrm{i}(\mathbf{k}\cdot\mathbf{r}-\omega t)},
\qquad
\mathbf{B}=\mathbf{B}\_0\,e^{\mathrm{i}(\mathbf{k}\cdot\mathbf{r}-\omega t)},
\\]

其中振幅 \\(\mathbf{E}\_0,\mathbf{B}\_0\\) 可为复数（吸收常相位），\\(\mathbf{k}\\) 为波矢，\\(\omega\\) 为角频率。对这种因式，

\\[
\partial\_t \;\longmapsto\; -\mathrm{i}\omega,
\qquad
\nabla \;\longmapsto\; \mathrm{i}\mathbf{k}
\\]

（作用在指数上）。代入无源 Maxwell 方程并约去公共因子后，得到代数关系

\\[
\mathbf{k}\cdot\mathbf{E}=0,\quad
\mathbf{k}\cdot\mathbf{B}=0,\quad
\mathbf{k}\times\mathbf{E}=\omega\mathbf{B},\quad
\mathbf{k}\times\mathbf{B}=-\mu\_0\varepsilon\_0\omega\mathbf{E} .
\\]

因此：平面电磁波是**横波**（\\(\mathbf{E},\mathbf{B}\perp\mathbf{k}\\)），且 \\(\mathbf{E},\mathbf{B},\mathbf{k}\\) 构成右手三元组；色散关系 \\(\omega=c|\mathbf{k}|\\)。等相位面 \\(\mathbf{k}\cdot\mathbf{r}-\omega t=\mathrm{const}\\) 是垂直于 \\(\mathbf{k}\\) 的平面，故称平面波。

复指数写法与第 [1 章](../ch01-complex/index.md)、第 [3 章](../ch03-fourier/index.md) 的 Fourier 方法一致：真实场取实部；线性叠加可构造波包。

### 小结

| 数学对象 | 电磁学中的角色 |
|----------|----------------|
| Gauss / Stokes | 积分定律 ↔ 微分形式的 Maxwell 方程 |
| 连续方程 | 电荷守恒；迫使引入位移电流 |
| Poisson / Laplace | 静电势边值问题 |
| 波动方程 | 真空中 \\(\mathbf{E},\mathbf{B}\\) 的传播 |
| 复平面波 \\(e^{\mathrm{i}(\mathbf{k}\cdot\mathbf{r}-\omega t)}\\) | 化 PDE 为代数约束 + 色散关系 |

材料中的色散、边界上的反射折射、几何光学与波动光学等超出本书范围，可在 PX284 后续章节继续阅读。
