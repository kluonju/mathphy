## 势与规范（PX284 Appendix D）

静电问题常用标量势 \\(\psi\\)（\\(\mathbf{E}=-\nabla\psi\\)）；磁静问题一般不能写 \\(\mathbf{B}=-\nabla\psi\_M\\)（因 \\(\nabla\times\mathbf{B}=\mu\_0\mathbf{J}\\) 可非零），而用**矢势** \\(\mathbf{B}=\nabla\times\mathbf{A}\\)。本节据 PX284 Appendix D 抽取与 Laplace / 分离变量 / 规范相关的数学骨架。

### Laplace 边值与唯一性

无体电荷区 \\(\nabla^2\psi=0\\)。导体表面常为等势面。给定边界上的 \\(\psi\\)（Dirichlet）时解唯一：若找到一个满足方程与边界的函数，即是解。

**平行板.** 板在 \\(x=0\\)（\\(\psi=0\\)）与 \\(x=d\\)（\\(\psi=V\\)）。试探

\\[
\psi=\frac{V}{d}x
\\]

满足边界条件，且 \\(\nabla^2\psi=0\\)，故正确；其间 \\(\mathbf{E}=-(V/d)\hat{\mathbf{e}}\_x\\)。

### 球坐标分离变量与 Legendre

轴对称（与 \\(\phi\\) 无关）时球坐标 Laplace 方程为

\\[
\frac{1}{r^2}\frac{\partial}{\partial r}\Bigl(r^2\frac{\partial\psi}{\partial r}\Bigr)
+\frac{1}{r^2\sin\theta}\frac{\partial}{\partial\theta}\Bigl(\sin\theta\frac{\partial\psi}{\partial\theta}\Bigr)=0.
\\]

分离变量 \\(\psi=R(r)\Theta(\theta)\\) 得通解（\\(P\_n\\) 为 Legendre 多项式）

\\[
\psi(r,\theta)=\sum\_{n=0}^\infty\bigl(A\_n r^n+B\_n r^{-(n+1)}\bigr)P\_n(\cos\theta).
\\]

前几项：\\(P\_0=1\\)，\\(P\_1=\cos\theta\\)，\\(P\_2=\frac{1}{2}(3\cos^2\theta-1)\\)，……

**例（均匀外场中的介质球，数学骨架）.** 无穷远处 \\(\psi\to -E\_0 r\cos\theta\\)。球内外分别取

\\[
\psi\_-=A r\cos\theta,\qquad
\psi\_+=\bigl(-E\_0 r+B r^{-2}\bigr)\cos\theta.
\\]

由 \\(r=a\\) 上 \\(\psi\\) 连续及法向 \\(\mathbf{D}\\) 条件（涉及介电常数 \\(\varepsilon\_r\\)）定 \\(A,B\\)。这是第 7 章球坐标分离变量的标准应用；完整电磁结果见原讲义。

### 磁矢势与库仑规范

因 \\(\nabla\cdot\mathbf{B}=0\\)，可写 \\(\mathbf{B}=\nabla\times\mathbf{A}\\)。**规范自由**：

\\[
\mathbf{A}\mapsto\mathbf{A}+\nabla\zeta
\\]

不改变 \\(\mathbf{B}\\)（因 \\(\nabla\times\nabla\zeta=\mathbf{0}\\)）。

静磁、取**库仑规范** \\(\nabla\cdot\mathbf{A}=0\\) 时，由 \\(\nabla\times\mathbf{B}=\mu\_0\mathbf{J}\\) 与恒等式 \\(\nabla\times(\nabla\times\mathbf{A})=\nabla(\nabla\cdot\mathbf{A})-\nabla^2\mathbf{A}\\) 得

\\[
\nabla^2\mathbf{A}=-\mu\_0\mathbf{J},
\\]

即矢势分量满足 Poisson 方程，特解

\\[
\mathbf{A}(\mathbf{r})=\frac{\mu\_0}{4\pi}\int\frac{\mathbf{J}(\mathbf{r}')}{|\mathbf{r}-\mathbf{r}'|}\,\mathrm{d}V'.
\\]

线电流回路：\\(\mathbf{A}(\mathbf{r})=\frac{\mu\_0 I}{4\pi}\oint \frac{\mathrm{d}\boldsymbol{\ell}'}{|\mathbf{r}-\mathbf{r}'|}\\)。远场可用多极展开（偶极主导）。

动态情形见下节：\\(\mathbf{E}=-\nabla\psi-\partial\_t\mathbf{A}\\)。与经典力学的衔接见[电磁场与哈密顿力学](em-hamiltonian.md)。

相关：第 [5 章电磁学中的数学方法](../ch05-math-physics-eq/06-em-methods.md)、[柱/球坐标中的 ∇](../ch07-coordinates/04-del-cylindrical-spherical.md)、第 6–7 章分离变量。
