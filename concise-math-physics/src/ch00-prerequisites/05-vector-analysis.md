## 向量分析基础

### 标量与向量

**标量**仅由大小决定，如温度、质量。**向量**（如速度、力）既有大小又有方向，本书用粗体 \\(\mathbf{A}\\) 表示。在直角坐标系中

\\[
\mathbf{A} = A\_x \mathbf{e}\_x + A\_y \mathbf{e}\_y + A\_z \mathbf{e}\_z, \qquad
|\mathbf{A}| = \sqrt{A\_x^2 + A\_y^2 + A\_z^2} .
\\]

单位向量常记 \\(\mathbf{e}\_x,\mathbf{e}\_y,\mathbf{e}\_z\\)（或 \\(\mathbf{i},\mathbf{j},\mathbf{k}\\)）。采用**右手坐标系**：四指由 \\(x\\) 转向 \\(y\\)，拇指指向 \\(z\\)。

### 向量的线性运算

\\[
a\mathbf{A} = aA\_x \mathbf{e}\_x + aA\_y \mathbf{e}\_y + aA\_z \mathbf{e}\_z, \qquad
\mathbf{A} \pm \mathbf{B} = (A\_x \pm B\_x)\mathbf{e}\_x + \cdots
\\]

几何上，\\(\mathbf{A} + \mathbf{B}\\) 对应平行四边形法则。

### 点积（数量积）

\\[
\mathbf{A} \cdot \mathbf{B} = |\mathbf{A}|\,|\mathbf{B}|\cos\theta = A\_x B\_x + A\_y B\_y + A\_z B\_z .
\\]

点积满足交换律 \\(\mathbf{A} \cdot \mathbf{B} = \mathbf{B} \cdot \mathbf{A}\\)。若 \\(\mathbf{A} \cdot \mathbf{B} = 0\\)，则两向量正交。

### 叉积（向量积）

\\[
|\mathbf{A} \times \mathbf{B}| = |\mathbf{A}|\,|\mathbf{B}|\sin\theta,
\\]

方向垂直于 \\(\mathbf{A},\mathbf{B}\\) 所在平面，由右手法则确定。分量形式：

\\[
\mathbf{A} \times \mathbf{B} = \begin{vmatrix}
\mathbf{e}\_x & \mathbf{e}\_y & \mathbf{e}\_z \\\\
A\_x & A\_y & A\_z \\\\
B\_x & B\_y & B\_z
\end{vmatrix}, \qquad
\mathbf{A} \times \mathbf{B} = -\mathbf{B} \times \mathbf{A} .
\\]

指标记号：\\((\mathbf{A} \times \mathbf{B})\_i = \varepsilon\_{ijk} A\_j B\_k\\)（见[指标记号与爱因斯坦求和约定](04-index-notation.md)）。

### 标量三重积

\\[
(\mathbf{A} \times \mathbf{B}) \cdot \mathbf{C} = \mathbf{B} \cdot (\mathbf{C} \times \mathbf{A}) = \mathbf{C} \cdot (\mathbf{A} \times \mathbf{B})
\\]

其绝对值等于 \\(\mathbf{A},\mathbf{B},\mathbf{C}\\) 张成的平行六面体体积。

### 微分算符 \\(\nabla\\)

**梯度**（作用在标量场 \\(\varphi\\) 上）：

\\[
\nabla \varphi = \mathbf{e}\_x \frac{\partial \varphi}{\partial x} + \mathbf{e}\_y \frac{\partial \varphi}{\partial y} + \mathbf{e}\_z \frac{\partial \varphi}{\partial z}, \qquad
\nabla \varphi = \left( \frac{\partial \varphi}{\partial x}, \frac{\partial \varphi}{\partial y}, \frac{\partial \varphi}{\partial z} \right) .
\\]

**散度**与**旋度**（作用在向量场 \\(\mathbf{A}\\) 上）：

\\[
\nabla \cdot \mathbf{A} = \frac{\partial A\_x}{\partial x} + \frac{\partial A\_y}{\partial y} + \frac{\partial A\_z}{\partial z}, \qquad
\nabla \times \mathbf{A} = \begin{vmatrix}
\mathbf{e}\_x & \mathbf{e}\_y & \mathbf{e}\_z \\\\
\partial/\partial x & \partial/\partial y & \partial/\partial z \\\\
A\_x & A\_y & A\_z
\end{vmatrix} .
\\]

**Laplace 算符**：\\(\nabla^2 = \nabla \cdot \nabla\\)。在直角坐标中 \\(\nabla^2 \varphi = \partial^2 \varphi / \partial x^2 + \partial^2 \varphi / \partial y^2 + \partial^2 \varphi / \partial z^2\\)。

恒等式 \\(\nabla \times (\nabla \varphi) = \mathbf{0}\\)、\\(\nabla \cdot (\nabla \times \mathbf{A}) = 0\\) 及 Stokes、Gauss 定理等，见[附录：矢量恒等式](../appendix/vector-identities.md)。柱、球坐标中的 \\(\nabla\\) 形式见第 [7 章](../ch07-coordinates/index.md)与第 [9 章](../ch09-tensor/03-grad-del.md)。
