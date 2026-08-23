## 程函方程与几何光学（PX284 Appendix I）

几何光学可从 Maxwell 方程在短波长极限下导出。本节据 PX284 Appendix I 压缩为数学骨架；与第 [1 章鞍点/WKB](../ch01-complex/07-saddle-point.md)、第 [5 章波动方程](../ch05-math-physics-eq/06-em-methods.md) 同构。

### 高频 ansatz

设单色场 \\(\mathbf{E}(\mathbf{r},t)=\mathbf{E}\_0(\mathbf{r})e^{-\mathrm{i}\omega t}\\)（\\(\mathbf{H}\\) 同理），并抽出快速相位：

\\[
\mathbf{E}\_0(\mathbf{r})=\mathbf{e}(\mathbf{r})\,e^{\mathrm{i}k\_0\tau(\mathbf{r})},\qquad
k\_0=\omega/c,
\\]

其中实函数 \\(\tau\\) 称**光程**（optical path）或**程函**（eikonal），振幅 \\(\mathbf{e},\mathbf{h}\\) 假定相对波长缓变。平面波特例：\\(\tau=n\,\mathbf{r}\cdot\hat{\mathbf{s}}\\)。

将 ansatz 代入无源介质中的 Maxwell 方程，并取 \\(k\_0\to\infty\\)（波长远小于几何尺度），主导项给出

\\[
\mathbf{e}\cdot\nabla\tau=0,\qquad
\nabla\tau\times\mathbf{e}=\mu c\,\mathbf{h},\qquad
\nabla\tau\times\mathbf{h}=-\varepsilon c\,\mathbf{e}.
\\]

消去 \\(\mathbf{h}\\) 并用 \\(n^2=c^2\mu\varepsilon\\) 得**程函方程**

\\[
(\nabla\tau)^2=n^2
\quad\Leftrightarrow\quad
\Bigl(\frac{\partial\tau}{\partial x}\Bigr)^2+\Bigl(\frac{\partial\tau}{\partial y}\Bigr)^2+\Bigl(\frac{\partial\tau}{\partial z}\Bigr)^2=n^2.
\\]

注意：不能写成 \\(\nabla\tau=\pm n\\)（左边是向量）。等相面 \\(\tau=\mathrm{const}\\) 即波前；光线沿 \\(\nabla\tau\\)（垂直于波前）。

### 光线方程

沿弧长 \\(s\\) 的光线 \\(\mathbf{r}(s)\\) 满足 \\(n\,\mathrm{d}\mathbf{r}/\mathrm{d}s=\nabla\tau\\)。再对 \\(s\\) 求导并用程函方程得

\\[
\frac{\mathrm{d}}{\mathrm{d}s}\Bigl(n\frac{\mathrm{d}\mathbf{r}}{\mathrm{d}s}\Bigr)=\nabla n.
\\]

\\(n\\) 为常数时化为直线；\\(\nabla n\neq\mathbf{0}\\) 时射线弯曲（如蜃景）。能量流（时间平均 Poynting）在此近似下沿射线方向，且 \\(\langle\mathbf{S}\rangle=v\_\phi\langle u\rangle\,\hat{\mathbf{s}}\\)。

### 与渐近方法的联系

程函 \\(\tau\\) 扮演 WKB / 鞍点相位的角色：高频极限把波动方程约化为一阶非线性 PDE（Hamilton–Jacobi 型）。下一阶振幅沿射线的输运方程给出几何光学强度；转折点/焦散处需均匀渐近或衍射修正——见[鞍点近似](../ch01-complex/07-saddle-point.md)与[衍射积分](diffraction-kirchhoff.md)。

相关：Born & Wolf《Principles of Optics》第 3 章；原讲义 Appendix I。
