## 爱因斯坦求和约定与指标记号

在矢量与张量分析、广义相对论及本书多处推导中，常采用**爱因斯坦求和约定**（Einstein summation convention）：同一项中出现两次的哑指标（dummy index）自动对取值范围求和。

例如在三维欧氏空间中，若指标 \\(i,j,k\\) 取 \\(1,2,3\\)（或 \\(x,y,z\\)），则

\\[
a_i b_i \equiv \sum_{i=1}^{3} a_i b_i = a_1 b_1 + a_2 b_2 + a_3 b_3 .
\\]

重复出现的指标称为**哑指标**，可随意改名而不改变表达式的值；只出现一次的指标称为**自由指标**。

### Kronecker 符号

**Kronecker delta** 定义为

\\[
\delta_{ij} =
\\[
\begin{cases}
1, & i = j, \\\\
0, & i \neq j .
\end{cases}
\\]
\\]

性质：

\\[
\delta_{ij} a_j = a_i, \qquad
\delta_{ij} \delta_{jk} = \delta_{ik}, \qquad
\delta_{ii} = 3 \quad \text{（三维）} .
\\]

在正交曲线坐标系中，单位基矢量满足 \\(\mathbf{e}_i \cdot \mathbf{e}_j = \delta_{ij}\\)（见第 [7 章](../ch07-coordinates/01-general.md)）。

### Levi-Civita 符号

**Levi-Civita 符号**（完全反对称单位张量）\\(\varepsilon_{ijk}\\) 在三维情形下定义为

\\[
\varepsilon_{ijk} =
\\[
\begin{cases}
+1, & (i,j,k) \text{ 为 } (1,2,3) \text{ 的偶排列}, \\\\
-1, & (i,j,k) \text{ 为 } (1,2,3) \text{ 的奇排列}, \\\\
0, & \text{其余情形（有重复指标）}.
\end{cases}
\\]
\\]

例如 \\(\varepsilon_{123} = \varepsilon_{231} = \varepsilon_{312} = 1\\)，\\(\varepsilon_{132} = -1\\)。置换两个指标变号：\\(\varepsilon_{ijk} = -\varepsilon_{jik}\\)。

### 用指标表示向量运算

设 \\(\mathbf{a} = (a_1,a_2,a_3)\\)，\\(\mathbf{b} = (b_1,b_2,b_3)\\)，则

\\[
\mathbf{a} \cdot \mathbf{b} = a_i b_i, \qquad
(\mathbf{a} \times \mathbf{b})_i = \varepsilon_{ijk} a_j b_k .
\\]

### 常用恒等式

\\[
\\[
\begin{aligned}
\varepsilon_{ijk} \varepsilon_{ijk} &= 6, \\\\
\varepsilon_{ijk} \varepsilon_{ilm} &= \delta_{jl}\delta_{km} - \delta_{jm}\delta_{kl}, \\\\
\varepsilon_{ijk} \delta_{jk} &= 0, \\\\
a_i \varepsilon_{ijk} b_j c_k &= \mathbf{a} \cdot (\mathbf{b} \times \mathbf{c}) .
\end{aligned}
\\]
\\]

最后一个式子即标量三重积的指标形式。更一般的矢量恒等式见[附录：矢量恒等式](../appendix/vector-identities.md)。

### 升降指标（欧氏情形）

在直角笛卡尔坐标中，度量张量为 \\(\delta_{ij}\\)，故协变分量与逆变分量一致：\\(a_i = a^i\\)。在曲线坐标或相对论中，需引入度量 \\(g_{ij}\\) 以升降指标；本书主体仍多采用分量与 \\(\delta_{ij}\\) 的欧氏约定。
