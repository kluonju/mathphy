## 线性代数基础

### 向量空间与线性无关

设 \\(V\\) 为域 \\(\mathbb{R}\\)（或 \\(\mathbb{C}\\)）上的**向量空间**。向量 \\(\mathbf{v}_1,\ldots,\mathbf{v}_n \in V\\) **线性无关**，是指

\\[
c_1 \mathbf{v}_1 + \cdots + c_n \mathbf{v}_n = \mathbf{0} \quad \Rightarrow \quad c_1 = \cdots = c_n = 0 .
\\]

若 \\(V\\) 中任意向量均可唯一表示为 \\(\mathbf{v}_1,\ldots,\mathbf{v}_n\\) 的线性组合，则称 \\(\{\mathbf{v}_i\}\\) 为 \\(V\\) 的一组**基**（basis），\\(n\\) 为维数。

### 矩阵与行列式

\\(m \times n\\) 矩阵 \\(A = (a_{ij})\\) 与向量 \\(\mathbf{x} \in \mathbb{R}^n\\) 的乘积给出 \\(\mathbb{R}^m\\) 中的像。方阵的行列式 \\(\det A\\) 满足 \\(\det(AB) = \det A \cdot \det B\\)；\\(\det A \neq 0\\) 当且仅当 \\(A\\) 可逆。

\\(2 \times 2\\) 与 \\(3 \times 3\\) 行列式：

\\[
\det \begin{pmatrix} a & b \\ c & d \end{pmatrix} = ad - bc,
\\]

\\[
\det \begin{pmatrix} a_1 & a_2 & a_3 \\ b_1 & b_2 & b_3 \\ c_1 & c_2 & c_3 \end{pmatrix}
= a_1(b_2 c_3 - b_3 c_2) - a_2(b_1 c_3 - b_3 c_1) + a_3(b_1 c_2 - b_2 c_1) .
\\]

后者与向量叉积 \\(\mathbf{a} \times \mathbf{b}\\) 的分量展开一致。

### 内积与正交

欧氏空间 \\(\mathbb{R}^n\\) 上的标准内积 \\(\langle \mathbf{u}, \mathbf{v} \rangle = \mathbf{u} \cdot \mathbf{v} = \sum_i u_i v_i\\)。若 \\(\langle \mathbf{u}, \mathbf{v} \rangle = 0\\)，称 \\(\mathbf{u},\mathbf{v}\\) **正交**。

函数空间上可定义内积，例如 \\(\langle f, g \rangle = \int_a^b f(x) g(x)\,\mathrm{d}x\\)。正交函数族在傅里叶级数展开中起核心作用（见第 [3 章](../ch03-fourier/01-fourier-series.md)）。

### 特征值与特征向量

对方阵 \\(A\\)，若存在非零向量 \\(\mathbf{v}\\) 与标量 \\(\lambda\\) 使得

\\[
A\mathbf{v} = \lambda \mathbf{v},
\\]

则 \\(\lambda\\) 为**特征值**，\\(\mathbf{v}\\) 为对应的**特征向量**。特征值由特征方程 \\(\det(A - \lambda I) = 0\\) 确定。对称实矩阵的特征值均为实数，且不同特征值对应的特征向量正交。

### 线性方程组

方程组 \\(A\mathbf{x} = \mathbf{b}\\) 当 \\(\det A \neq 0\\) 时有唯一解 \\(\mathbf{x} = A^{-1}\mathbf{b}\\)。Sturm–Liouville 本征值问题、偏微分方程分离变量等，均可归结为线性算符的本征值问题（见第 [5](../ch05-math-physics-eq/index.md)、[6](../ch06-pde/index.md) 章）。

### Gram–Schmidt 正交化（简述）

给定线性无关组 \\(\{f_1,\ldots,f_n\}\\)，可递推构造正交组 \\(\{g_1,\ldots,g_n\}\\)：

\\[
g_1 = f_1, \qquad
g_k = f_k - \sum_{j=1}^{k-1} \frac{\langle f_k, g_j \rangle}{\langle g_j, g_j \rangle}\, g_j .
\\]

归一化后得到标准正交基，用于函数空间的级数展开。
