## 柱坐标与球坐标中的 \\(\nabla\\)

本节据 Warwick PX284 Appendix B 整理：在**正交曲线坐标**下写出梯度、散度、旋度与 Laplace 算符。记号与本书一致——柱坐标 \\((\rho,\phi,z)\\)，球坐标 \\((r,\theta,\phi)\\)（PX284 柱坐标径向有时写作 \\(r\\)，此处统一为 \\(\rho\\)）。公式不必背诵，重在会用。

![直角、柱、球三种正交坐标系](../figures/coords_three_systems.png)

### 为何需要非直角形式

直角坐标中 \\(\nabla=\hat{\mathbf{e}}\_x\partial\_x+\hat{\mathbf{e}}\_y\partial\_y+\hat{\mathbf{e}}\_z\partial\_z\\)。若场本身在柱/球坐标下最简单，先换成直角再算往往更繁。例如直导线沿 \\(z\\) 轴的磁场

\\[
\mathbf{B}=\frac{\mu\_0 I}{2\pi\rho}\,\hat{\mathbf{e}}\_\phi
\\]

在柱坐标下一目了然；要证 \\(\nabla\cdot\mathbf{B}=0\\)（\\(\rho\neq 0\\)），用下面的柱坐标散度公式比先写成 \\(B\_x,B\_y\\) 再求导更省事。

正交坐标的特征：沿各坐标增加方向的单位基 \\(\hat{\mathbf{e}}\_i\\) 在每一点彼此正交。柱、球坐标均属此类。一般推导见[一般曲线坐标](01-general.md)（尺度因子 \\(h\_i\\)）。

### 梯度：从 \\(\mathrm{d}f=\nabla f\cdot\mathrm{d}\boldsymbol{\ell}\\) 出发

#### 球坐标

线元

\\[
\mathrm{d}\boldsymbol{\ell}
= \mathrm{d}r\,\hat{\mathbf{e}}\_r
+ r\,\mathrm{d}\theta\,\hat{\mathbf{e}}\_\theta
+ r\sin\theta\,\mathrm{d}\phi\,\hat{\mathbf{e}}\_\phi .
\\]

又 \\(\mathrm{d}f=\partial\_r f\,\mathrm{d}r+\partial\_\theta f\,\mathrm{d}\theta+\partial\_\phi f\,\mathrm{d}\phi\\)，与 \\(\nabla f\cdot\mathrm{d}\boldsymbol{\ell}\\) 比较得

\\[
\nabla f
= \hat{\mathbf{e}}\_r\frac{\partial f}{\partial r}
+ \hat{\mathbf{e}}\_\theta\frac{1}{r}\frac{\partial f}{\partial\theta}
+ \hat{\mathbf{e}}\_\phi\frac{1}{r\sin\theta}\frac{\partial f}{\partial\phi} .
\\]

算子应写在基矢**右侧**，以免误作用到基矢本身。例：Coulomb 势 \\(\psi=q/(4\pi\varepsilon\_0 r)\\) 立刻给出 \\(\mathbf{E}=-\nabla\psi=(q/(4\pi\varepsilon\_0 r^2))\hat{\mathbf{e}}\_r\\)。

#### 柱坐标

\\[
\mathrm{d}\boldsymbol{\ell}
= \mathrm{d}\rho\,\hat{\mathbf{e}}\_\rho
+ \rho\,\mathrm{d}\phi\,\hat{\mathbf{e}}\_\phi
+ \mathrm{d}z\,\hat{\mathbf{e}}\_z ,
\\]

\\[
\nabla f
= \hat{\mathbf{e}}\_\rho\frac{\partial f}{\partial\rho}
+ \hat{\mathbf{e}}\_\phi\frac{1}{\rho}\frac{\partial f}{\partial\phi}
+ \hat{\mathbf{e}}\_z\frac{\partial f}{\partial z} .
\\]

### 散度：基矢随位置变化

设 \\(\mathbf{W}=W\_r\hat{\mathbf{e}}\_r+W\_\theta\hat{\mathbf{e}}\_\theta+W\_\phi\hat{\mathbf{e}}\_\phi\\)。**不可**把球坐标散度写成

\\[
\frac{\partial W\_r}{\partial r}+\frac{1}{r}\frac{\partial W\_\theta}{\partial\theta}+\frac{1}{r\sin\theta}\frac{\partial W\_\phi}{\partial\phi}
\quad\text{（错误）},
\\]

因为非直角坐标中单位基随坐标改变（例如 \\(\phi\\) 增加 \\(\pi\\) 时 \\(\hat{\mathbf{e}}\_\phi\\) 反向），\\(\nabla\\) 作用时必须对基矢求导。

球坐标下非零的基矢导数包括（\\(\partial\_\theta=\partial/\partial\theta\\) 等）：

\\[
\begin{aligned}
\partial\_\theta\hat{\mathbf{e}}\_r&=\hat{\mathbf{e}}\_\theta,
&
\partial\_\phi\hat{\mathbf{e}}\_r&=\sin\theta\,\hat{\mathbf{e}}\_\phi, \\\\
\partial\_\theta\hat{\mathbf{e}}\_\theta&=-\hat{\mathbf{e}}\_r,
&
\partial\_\phi\hat{\mathbf{e}}\_\theta&=\cos\theta\,\hat{\mathbf{e}}\_\phi, \\\\
\partial\_\phi\hat{\mathbf{e}}\_\phi&=-\sin\theta\,\hat{\mathbf{e}}\_r-\cos\theta\,\hat{\mathbf{e}}\_\theta .
\end{aligned}
\\]

由此整理得标准形式

\\[
\nabla\cdot\mathbf{W}
= \frac{1}{r^2}\frac{\partial}{\partial r}(r^2 W\_r)
+ \frac{1}{r\sin\theta}\frac{\partial}{\partial\theta}(W\_\theta\sin\theta)
+ \frac{1}{r\sin\theta}\frac{\partial W\_\phi}{\partial\phi} .
\\]

对 Coulomb 场 \\(W\_r\propto 1/r^2\\)、其余分量为零，上式立刻给出 \\(r\neq 0\\) 时 \\(\nabla\cdot\mathbf{E}=0\\)。

柱坐标：

\\[
\nabla\cdot\mathbf{W}
= \frac{1}{\rho}\frac{\partial}{\partial\rho}(\rho W\_\rho)
+ \frac{1}{\rho}\frac{\partial W\_\phi}{\partial\phi}
+ \frac{\partial W\_z}{\partial z} .
\\]

对导线磁场 \\(W\_\phi\propto 1/\rho\\)，同样可见 \\(\rho\neq 0\\) 时散度为零。

### Laplace 算符

若 \\(\mathbf{W}=\nabla\psi\\)，则 \\(\nabla\cdot\mathbf{W}=\nabla^2\psi\\)。

**球坐标**

\\[
\nabla^2\psi
= \frac{1}{r^2}\frac{\partial}{\partial r}\Bigl(r^2\frac{\partial\psi}{\partial r}\Bigr)
+ \frac{1}{r^2\sin\theta}\frac{\partial}{\partial\theta}\Bigl(\sin\theta\frac{\partial\psi}{\partial\theta}\Bigr)
+ \frac{1}{r^2\sin^2\theta}\frac{\partial^2\psi}{\partial\phi^2} .
\\]

（氢原子径向/角向分离、静电边值问题常用此式。）

**柱坐标**

\\[
\nabla^2\psi
= \frac{1}{\rho}\frac{\partial}{\partial\rho}\Bigl(\rho\frac{\partial\psi}{\partial\rho}\Bigr)
+ \frac{1}{\rho^2}\frac{\partial^2\psi}{\partial\phi^2}
+ \frac{\partial^2\psi}{\partial z^2} .
\\]

注意：不能猜成“各向二阶导简单相加”；正确形式来自先取梯度再取散度，尺度因子会进入求导。

### 旋度

**球坐标**（行列式便于记忆）

\\[
\nabla\times\mathbf{W}
= \frac{1}{r^2\sin\theta}
\begin{vmatrix}
\hat{\mathbf{e}}\_r & r\hat{\mathbf{e}}\_\theta & r\sin\theta\,\hat{\mathbf{e}}\_\phi \\\\
\partial/\partial r & \partial/\partial\theta & \partial/\partial\phi \\\\
W\_r & r W\_\theta & r\sin\theta\, W\_\phi
\end{vmatrix}
=
\begin{aligned}[t]
&\frac{1}{r\sin\theta}\Bigl(
\partial\_\theta(W\_\phi\sin\theta)-\partial\_\phi W\_\theta
\Bigr)\hat{\mathbf{e}}\_r \\\\
&+ \frac{1}{r}\Bigl(
\frac{1}{\sin\theta}\partial\_\phi W\_r-\partial\_r(r W\_\phi)
\Bigr)\hat{\mathbf{e}}\_\theta \\\\
&+ \frac{1}{r}\Bigl(
\partial\_r(r W\_\theta)-\partial\_\theta W\_r
\Bigr)\hat{\mathbf{e}}\_\phi .
\end{aligned}
\\]

**柱坐标**

\\[
\nabla\times\mathbf{W}
= \frac{1}{\rho}
\begin{vmatrix}
\hat{\mathbf{e}}\_\rho & \rho\hat{\mathbf{e}}\_\phi & \hat{\mathbf{e}}\_z \\\\
\partial/\partial\rho & \partial/\partial\phi & \partial/\partial z \\\\
W\_\rho & \rho W\_\phi & W\_z
\end{vmatrix} .
\\]

展开即

\\[
\begin{aligned}
(\nabla\times\mathbf{W})\_\rho
&= \frac{1}{\rho}\partial\_\phi W\_z-\partial\_z W\_\phi, \\\\
(\nabla\times\mathbf{W})\_\phi
&= \partial\_z W\_\rho-\partial\_\rho W\_z, \\\\
(\nabla\times\mathbf{W})\_z
&= \frac{1}{\rho}\partial\_\rho(\rho W\_\phi)-\frac{1}{\rho}\partial\_\phi W\_\rho .
\end{aligned}
\\]

直导线磁场 \\(B\_\phi\propto 1/\rho\\) 时，\\((\nabla\times\mathbf{B})\_z\propto\frac{1}{\rho}\partial\_\rho(\rho\cdot 1/\rho)=0\\)（\\(\rho\neq 0\\)），与第 [0 章](../ch00-prerequisites/05-vector-analysis.md) 的讨论一致。

### 速查表

| | 柱 \\((\rho,\phi,z)\\) | 球 \\((r,\theta,\phi)\\) |
|--|------------------------|---------------------------|
| 尺度因子 | \\(h\_\rho=1,\;h\_\phi=\rho,\;h\_z=1\\) | \\(h\_r=1,\;h\_\theta=r,\;h\_\phi=r\sin\theta\\) |
| \\(\nabla f\\) | \\(\partial\_\rho f\,\hat{\mathbf{e}}\_\rho+\rho^{-1}\partial\_\phi f\,\hat{\mathbf{e}}\_\phi+\partial\_z f\,\hat{\mathbf{e}}\_z\\) | \\(\partial\_r f\,\hat{\mathbf{e}}\_r+r^{-1}\partial\_\theta f\,\hat{\mathbf{e}}\_\theta+(r\sin\theta)^{-1}\partial\_\phi f\,\hat{\mathbf{e}}\_\phi\\) |
| \\(\nabla\cdot\mathbf{W}\\) | \\(\rho^{-1}\partial\_\rho(\rho W\_\rho)+\rho^{-1}\partial\_\phi W\_\phi+\partial\_z W\_z\\) | \\(r^{-2}\partial\_r(r^2 W\_r)+\cdots\\)（见上文） |
| \\(\nabla^2\psi\\) | \\(\rho^{-1}\partial\_\rho(\rho\partial\_\rho\psi)+\rho^{-2}\partial\_\phi^2\psi+\partial\_z^2\psi\\) | \\(r^{-2}\partial\_r(r^2\partial\_r\psi)+\cdots\\)（见上文） |

一般正交系中 \\(\nabla f=\sum\_i h\_i^{-1}(\partial f/\partial q\_i)\hat{\mathbf{e}}\_i\\)，散度/旋度/Laplace 的 \\(h\_i\\) 公式见[一般曲线坐标](01-general.md)。电磁学应用见[电磁学中的数学方法](../ch05-math-physics-eq/06-em-methods.md)。
