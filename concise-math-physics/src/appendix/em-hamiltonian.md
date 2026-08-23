## 电磁场与哈密顿力学（PX284 Appendix E）

势在经典电磁学中可选，在量子力学中则几乎不可或缺。本节据 PX284 Appendix E，给出由 Faraday 律到 Lorentz 力、再到 Lagrangian / Hamiltonian 的数学骨架；与第 [2 章](../ch02-variation/02-hamilton.md) 衔接。

### 由 Faraday 到时变标势

令 \\(\mathbf{B}=\nabla\times\mathbf{A}\\)，代入 Faraday 律 \\(\nabla\times\mathbf{E}=-\partial\_t\mathbf{B}\\) 得

\\[
\nabla\times\Bigl(\mathbf{E}+\frac{\partial\mathbf{A}}{\partial t}\Bigr)=\mathbf{0}.
\\]

故存在标量势 \\(\psi\\) 使

\\[
\mathbf{E}=-\nabla\psi-\frac{\partial\mathbf{A}}{\partial t}.
\\]

这是静电关系 \\(\mathbf{E}=-\nabla\psi\\) 的时变推广。

### Lorentz 力与总导数

带电粒子受力

\\[
\mathbf{F}=q\Bigl(-\nabla\psi-\partial\_t\mathbf{A}-\mathbf{v}\times(\nabla\times\mathbf{A})\Bigr).
\\]

用恒等式 \\(\mathbf{v}\times(\nabla\times\mathbf{A})=\nabla(\mathbf{A}\cdot\mathbf{v})-(\mathbf{v}\cdot\nabla)\mathbf{A}\\)（\\(\mathbf{v}\\) 视为与坐标无关的参数），整理得

\\[
\mathbf{F}=q\Bigl(-\nabla(\psi-\mathbf{A}\cdot\mathbf{v})-\frac{\mathrm{d}\mathbf{A}}{\mathrm{d}t}\Bigr),
\\]

其中 \\(\mathrm{d}\mathbf{A}/\mathrm{d}t=\partial\_t\mathbf{A}+(\mathbf{v}\cdot\nabla)\mathbf{A}\\) 为沿粒子轨迹的总导数。再由 \\(\mathbf{F}=\mathrm{d}\mathbf{p}/\mathrm{d}t\\) 得

\\[
\frac{\mathrm{d}}{\mathrm{d}t}(\mathbf{p}+q\mathbf{A})=-q\nabla(\psi-\mathbf{A}\cdot\mathbf{v}).
\\]

### Lagrangian 与正则动量

上述运动方程可由 Euler–Lagrange 方程从

\\[
L=\frac{p^2}{2m}+q\mathbf{A}\cdot\mathbf{v}-q\psi
\\]

导出。对位置共轭的**正则动量**（canonical momentum）为

\\[
\mathbf{p}\_0=\mathbf{p}+q\mathbf{A},
\\]

相应 Hamiltonian 为

\\[
H=\frac{1}{2m}(\mathbf{p}\_0-q\mathbf{A})^2+q\psi.
\\]

非相对论量子力学中把电磁相互作用并入 Schrödinger / Pauli 方程，即以该 \\(H\\) 为出发点（最小耦合替换 \\(\mathbf{p}\mapsto\mathbf{p}-q\mathbf{A}\\)）。

相关：[势与规范](em-potentials.md)、[哈密顿形式](../ch02-variation/02-hamilton.md)。
