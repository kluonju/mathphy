## 向量分析基础

### 标量与向量

**标量**仅由大小决定，如温度、质量。**向量**（如速度、力）既有大小又有方向，本书用粗体 \\(\mathbf{A}\\) 表示。在直角坐标系中

\\[
\mathbf{A} = A_x \mathbf{e}_x + A_y \mathbf{e}_y + A_z \mathbf{e}_z, \qquad
|\mathbf{A}| = \sqrt{A_x^2 + A_y^2 + A_z^2} .
\\]

单位向量常记 \\(\mathbf{e}_x,\mathbf{e}_y,\mathbf{e}_z\\)（或 \\(\mathbf{i},\mathbf{j},\mathbf{k}\\)）。采用**右手坐标系**：四指由 \\(x\\) 转向 \\(y\\)，拇指指向 \\(z\\)。

### 向量的线性运算

\\[
a\mathbf{A} = aA_x \mathbf{e}_x + aA_y \mathbf{e}_y + aA_z \mathbf{e}_z, \qquad
\mathbf{A} \pm \mathbf{B} = (A_x \pm B_x)\mathbf{e}_x + \cdots
\\]

几何上，\\(\mathbf{A} + \mathbf{B}\\) 对应平行四边形法则。

### 点积（数量积）

\\[
\mathbf{A} \cdot \mathbf{B} = |\mathbf{A}|\,|\mathbf{B}|\cos\theta = A_x B_x + A_y B_y + A_z B_z .
\\]

点积满足交换律 \\(\mathbf{A} \cdot \mathbf{B} = \mathbf{B} \cdot \mathbf{A}\\)。若 \\(\mathbf{A} \cdot \mathbf{B} = 0\\)，则两向量正交。

### 叉积（向量积）

\\[
|\mathbf{A} \times \mathbf{B}| = |\mathbf{A}|\,|\mathbf{B}|\sin\theta,
\\]

方向垂直于 \\(\mathbf{A},\mathbf{B}\\) 所在平面，由右手法则确定。分量形式：

\\[
\mathbf{A} \times \mathbf{B} = \begin{vmatrix}
\mathbf{e}_x & \mathbf{e}_y & \mathbf{e}_z \\\\
A_x & A_y & A_z \\\\
B_x & B_y & B_z
\end{vmatrix}, \qquad
\mathbf{A} \times \mathbf{B} = -\mathbf{B} \times \mathbf{A} .
\\]

指标记号：\\((\mathbf{A} \times \mathbf{B})_i = \varepsilon_{ijk} A_j B_k\\)（见上一节）。

### 标量三重积

\\[
(\mathbf{A} \times \mathbf{B}) \cdot \mathbf{C} = \mathbf{B} \cdot (\mathbf{C} \times \mathbf{A}) = \mathbf{C} \cdot (\mathbf{A} \times \mathbf{B})
\\]

其绝对值等于 \\(\mathbf{A},\mathbf{B},\mathbf{C}\\) 张成的平行六面体体积。

### 微分算符 \\(\nabla\\)

**梯度**（作用在标量场 \\(\varphi\\) 上）：

\\[
\nabla \varphi = \mathbf{e}_x \frac{\partial \varphi}{\partial x} + \mathbf{e}_y \frac{\partial \varphi}{\partial y} + \mathbf{e}_z \frac{\partial \varphi}{\partial z}, \qquad
\nabla \varphi = \left( \frac{\partial \varphi}{\partial x}, \frac{\partial \varphi}{\partial y}, \frac{\partial \varphi}{\partial z} \right) .
\\]

**散度**与**旋度**（作用在向量场 \\(\mathbf{A}\\) 上）：

\\[
\nabla \cdot \mathbf{A} = \frac{\partial A_x}{\partial x} + \frac{\partial A_y}{\partial y} + \frac{\partial A_z}{\partial z}, \qquad
\nabla \times \mathbf{A} = \begin{vmatrix}
\mathbf{e}_x & \mathbf{e}_y & \mathbf{e}_z \\\\
\partial/\partial x & \partial/\partial y & \partial/\partial z \\\\
A_x & A_y & A_z
\end{vmatrix} .
\\]

**Laplace 算符**：\\(\nabla^2 = \nabla \cdot \nabla\\)。在直角坐标中 \\(\nabla^2 \varphi = \partial^2 \varphi / \partial x^2 + \partial^2 \varphi / \partial y^2 + \partial^2 \varphi / \partial z^2\\)。

恒等式 \\(\nabla \times (\nabla \varphi) = \mathbf{0}\\)、\\(\nabla \cdot (\nabla \times \mathbf{A}) = 0\\) 及 Stokes、Gauss 定理等，见[附录：矢量恒等式](../appendix/vector-identities.md)。柱、球坐标中的 \\(\nabla\\) 形式见第 [7 章](../ch07-coordinates/index.md)与第 [9 章](../ch09-tensor/03-grad-del.md)。
