## 指标记号习题

下列习题改编自 PX286 Methods of Mathematical Physics 第 8 章 Problems。建议先独立完成，再对照解答（若有）。

### 习题 1（Pauli 矩阵）

三个 Pauli 矩阵为

\\[
\sigma^x = \begin{pmatrix} 0 & 1 \\\\ 1 & 0 \end{pmatrix},
\qquad
\sigma^y = \begin{pmatrix} 0 & -\mathrm{i} \\\\ \mathrm{i} & 0 \end{pmatrix},
\qquad
\sigma^z = \begin{pmatrix} 1 & 0 \\\\ 0 & -1 \end{pmatrix}.
\\]

用**指标记号**（勿直接做矩阵乘法）求：

1. \\([\sigma^x\sigma^y]\_{11}\\)、\\([\sigma^x\sigma^y]\_{12}\\) 与 \\([\sigma^y\sigma^x]\_{11}\\)；
2. \\(\operatorname{tr}(\sigma^y)^2\\) 与 \\(\operatorname{tr}(\sigma^x\sigma^y)\\)；
3. \\(\det\sigma^x\\)、\\(\det\sigma^y\\) 与 \\(\det(\sigma^x\sigma^y)\\)。

### 习题 2（行列式与 \\(\varepsilon\\)）

1. \\(2\times 2\\) 矩阵的行列式为 \\(\det M=\varepsilon\_{ij}M\_{1i}M\_{2j}\\)。
   - (a) 证明若 \\(a=b\\)，则 \\(\varepsilon\_{ij}M\_{ai}M\_{bj}=0\\)；
   - (b) 确定 \\(\varepsilon\_{ij}M\_{ai}M\_{bj}\\) 的值；
   - (c) 由此证明对任意两矩阵 \\(M,N\\) 有 \\(\det(MN)=\det M\\,\det N\\)。
2. 对 \\(3\times 3\\) 矩阵重复上述论证。
3. 给出五维 Levi-Civita 符号 \\(\varepsilon\_{ijklm}\\) 的定义。

### 习题 3（液晶序参量）

液晶是光学各向异性材料，可用无迹、对称的 \\(3\times 3\\) 矩阵 \\(Q\\) 描述。

1. 用指标记号写出 \\(Q\\) 无迹与对称的条件。
2. 自由能取形式

\\[
F = \frac{A}{2}\operatorname{tr}(Q^2) - \frac{B}{3}\operatorname{tr}(Q^3) + \frac{C}{4}\bigl(\operatorname{tr}(Q^2)\bigr)^2 .
\\]

将其改写成指标记号。

3. 在旋转（旋转矩阵 \\(R\\)）下 \\(Q\mapsto RQR^{\mathsf{T}}\\)。用指标记号验证 \\(\operatorname{tr}(Q^2)\\) 与 \\(\operatorname{tr}(Q^3)\\) 在该变换下不变，从而自由能对旋转不变。

### 习题 4（矢量微积分恒等式）

用指标记号建立下列恒等式：

1. \\(\nabla\cdot(\nabla\times\mathbf{u})=0\\)；
2. \\(\mathbf{u}\times(\nabla\times\mathbf{u})=\nabla\bigl(\tfrac{1}{2}|\mathbf{u}|^2\bigr)-(\mathbf{u}\cdot\nabla)\mathbf{u}\\)；
3. \\(\nabla\cdot(\mathbf{u}\times\mathbf{v})=\mathbf{v}\cdot(\nabla\times\mathbf{u})-\mathbf{u}\cdot(\nabla\times\mathbf{v})\\)；
4. \\(\nabla\times(\mathbf{u}\times\mathbf{v})=\mathbf{u}(\nabla\cdot\mathbf{v})-\mathbf{v}(\nabla\cdot\mathbf{u})+(\mathbf{v}\cdot\nabla)\mathbf{u}-(\mathbf{u}\cdot\nabla)\mathbf{v}\\)。

<details>
<summary>提示 / 解答要点</summary>

\\[
\begin{aligned}
\nabla\cdot(\nabla\times\mathbf{u})
&= \partial\_i(\varepsilon\_{ijk}\partial\_j u\_k)
= \varepsilon\_{ijk}\partial\_j\partial\_i u\_k
= -\varepsilon\_{jik}\partial\_j\partial\_i u\_k
= -\nabla\cdot(\nabla\times\mathbf{u}),
\end{aligned}
\\]

故该量等于其相反，必为零。

\\[
\begin{aligned}
\bigl[\mathbf{u}\times(\nabla\times\mathbf{u})\bigr]\_i
&= \varepsilon\_{ijk}u\_j(\varepsilon\_{klm}\partial\_l u\_m)
= (\delta\_{il}\delta\_{jm}-\delta\_{im}\delta\_{jl})u\_j\partial\_l u\_m \\\\
&= u\_j\partial\_i u\_j - u\_j\partial\_j u\_i
= \partial\_i\bigl(\tfrac{1}{2}u\_j u\_j\bigr) - u\_j\partial\_j u\_i .
\end{aligned}
\\]

\\[
\nabla\cdot(\mathbf{u}\times\mathbf{v})
= \partial\_i(\varepsilon\_{ijk}u\_j v\_k)
= \varepsilon\_{ijk}(\partial\_i u\_j)v\_k + \varepsilon\_{ijk}u\_j\partial\_i v\_k
= \mathbf{v}\cdot(\nabla\times\mathbf{u}) - \mathbf{u}\cdot(\nabla\times\mathbf{v}) .
\\]

\\[
\begin{aligned}
\bigl[\nabla\times(\mathbf{u}\times\mathbf{v})\bigr]\_i
&= \varepsilon\_{ijk}\partial\_j(\varepsilon\_{klm}u\_l v\_m)
= (\delta\_{il}\delta\_{jm}-\delta\_{im}\delta\_{jl})\partial\_j(u\_l v\_m) \\\\
&= \partial\_j(u\_i v\_j) - \partial\_j(u\_j v\_i)
= v\_j\partial\_j u\_i + u\_i\partial\_j v\_j - v\_i\partial\_j u\_j - u\_j\partial\_j v\_i .
\end{aligned}
\\]

</details>

### 习题 5（Navier–Stokes 与积分定理）

1. 将 Navier–Stokes 方程与连续性方程写成指标记号：

\\[
\rho\Bigl(\frac{\partial\mathbf{u}}{\partial t}+(\mathbf{u}\cdot\nabla)\mathbf{u}\Bigr)
= -\nabla p + \mu\nabla^2\mathbf{u},
\qquad
\frac{\partial\rho}{\partial t}+\nabla\cdot(\rho\mathbf{u})=0 .
\\]

2. 涡量 \\(\boldsymbol{\omega}=\nabla\times\mathbf{u}\\)。用指标记号证明

\\[
\varepsilon\_{ijk}\omega\_k = \partial\_i u\_j - \partial\_j u\_i .
\\]

3. 将 Stokes 定理与散度定理写成指标记号：

\\[
\int\_S (\nabla\times\mathbf{u})\cdot\mathrm{d}\mathbf{A}
= \int\_{\partial S}\mathbf{u}\cdot\mathrm{d}\mathbf{s},
\qquad
\int\_\Omega \nabla\cdot\mathbf{u}\\,\mathrm{d}V
= \int\_{\partial\Omega}\mathbf{u}\cdot\mathrm{d}\mathbf{A} .
\\]

<details>
<summary>提示 / 解答要点</summary>

1. \\(\rho(\partial\_t u\_i + u\_j\partial\_j u\_i)=-\partial\_i p + \mu\partial\_j\partial\_j u\_i\\)，以及 \\(\partial\_t\rho + \partial\_i(\rho u\_i)=0\\)。
2. \\(\varepsilon\_{ijk}\omega\_k=\varepsilon\_{ijk}\varepsilon\_{klm}\partial\_l u\_m=(\delta\_{il}\delta\_{jm}-\delta\_{im}\delta\_{jl})\partial\_l u\_m=\partial\_i u\_j-\partial\_j u\_i\\)。
3. \\(\displaystyle\int\_S \varepsilon\_{ijk}\partial\_j u\_k\\,\mathrm{d}A\_i=\int\_{\partial S}u\_i\\,\mathrm{d}s\_i\\)；\\(\displaystyle\int\_\Omega \partial\_i u\_i\\,\mathrm{d}V=\int\_{\partial\Omega}u\_i\\,\mathrm{d}A\_i\\)。

</details>

### 习题 6（各向同性张量）

在三维中：

1. 验证下列各量均为各向同性：
   - (a) \\(\varepsilon\_{ijk}\\)；
   - (b) \\(\delta\_{ij}\delta\_{kl}\\)；
   - (c) \\(\delta\_{ik}\delta\_{jl}\\)；
   - (d) \\(\delta\_{il}\delta\_{jk}\\)。
2. 证明任意三秩各向同性张量必与 \\(\varepsilon\_{ijk}\\) 成比例。

<details>
<summary>提示 / 解答要点</summary>

张量各向同性意味着对一切旋转矩阵 \\(R\\) 有 \\(R\_{ia}R\_{jb}\cdots T\_{ab\cdots}=T\_{ij\cdots}\\)。

1. (a) \\(R\_{ia}R\_{jb}R\_{kc}\varepsilon\_{abc}=\varepsilon\_{ijk}\det R=\varepsilon\_{ijk}\\)（因旋转满足 \\(\det R=1\\)）。
   (b) \\(R\_{ia}R\_{jb}R\_{kc}R\_{ld}\delta\_{ab}\delta\_{cd}=R\_{ia}R\_{ja}R\_{kc}R\_{lc}=\delta\_{ij}\delta\_{kl}\\)（正交性）。(c)(d) 同理。
2. 绕 3 轴旋转 \\(\pi\\) 给出 \\((x\_1,x\_2,x\_3)\mapsto(-x\_1,-x\_2,x\_3)\\)，由此可证凡有重复指标的分量（如 \\(T\_{111}\\)、\\(T\_{112}\\)）必为零，故仅当 \\((ijk)\\) 为 \\((123)\\) 的排列时分量可能非零。再绕 1 轴旋转 \\(\pi/2\\)（\\((x\_1,x\_2,x\_3)\mapsto(x\_1,-x\_3,x\_2)\\)）得 \\(T\_{123}=-T\_{132}\\)；对其余轴同理，遂知 \\(T\_{ijk}=\pm T\_{123}\\)，符号由排列奇偶决定，即与 \\(\varepsilon\_{ijk}\\) 成比例。

</details>

### 习题 7（奇弹性，二维）

考虑二维各向同性弹性材料，其四秩各向同性张量 \\(C\_{ijkl}\\) 对 \\((ij)\\) 与对 \\((kl)\\) 分别对称：\\(C\_{ijkl}=C\_{jikl}\\)、\\(C\_{ijkl}=C\_{ijlk}\\)。

1. 证明其一般形式可写为

\\[
\begin{aligned}
C\_{ijkl}
&= B\delta\_{ij}\delta\_{kl} + G\Bigl(\delta\_{ik}\delta\_{jl}+\delta\_{il}\delta\_{jk}-\tfrac{1}{2}\delta\_{ij}\delta\_{kl}\Bigr) \\\\
&\quad + E^{\mathrm{odd}}\bigl(\delta\_{ik}\varepsilon\_{jl}+\delta\_{jk}\varepsilon\_{il}+\delta\_{il}\varepsilon\_{jk}+\delta\_{jl}\varepsilon\_{ik}\bigr) .
\end{aligned}
\\]

2. 证明前两项在交换 \\((ij)\leftrightarrow(kl)\\) 下为偶，第三项为奇。
3. 若材料由 Hookean 弹性储能 \\(E=\tfrac{1}{2}C\_{ijkl}u\_{ij}u\_{kl}\\) 描述，其中应变 \\(u\_{ij}=\tfrac{1}{2}(\partial\_i u\_j+\partial\_j u\_i)\\) 对称，说明为何预期 \\(C\_{ijkl}\\) 为偶（即不应出现奇项）。

<details>
<summary>提示 / 解答要点</summary>

1. 可能的基包括 \\(\delta\delta\\)、\\(\delta\varepsilon\\)、\\(\varepsilon\delta\\)、\\(\varepsilon\varepsilon\\) 各类乘积；利用 \\(\varepsilon\_{ij}\varepsilon\_{kl}=\delta\_{ik}\delta\_{jl}-\delta\_{il}\delta\_{jk}\\) 消冗余，再对 \\((ij)\\)、\\((kl)\\) 分别对称化，即得上述三项结构。
2. 对奇项：\\(\delta\_{ik}\varepsilon\_{jl}+\cdots\\) 在 \\((ij)\leftrightarrow(kl)\\) 下因 \\(\varepsilon\\) 反号而整体变号。
3. 乘积 \\(u\_{ij}u\_{kl}\\) 在 \\((ij)\leftrightarrow(kl)\\) 下对称，故只有 \\(C\\) 的偶部对能量有贡献；标准 Hookean 能量不含奇弹性项。

</details>

### 习题 8（Riemann 曲率的独立分量）

四秩 Riemann 曲率张量 \\(R\_{ijkl}\\) 具有对称性

\\[
R\_{ijkl}=-R\_{jikl},
\qquad
R\_{ijkl}=-R\_{ijlk},
\qquad
R\_{ijkl}=R\_{klij} .
\\]

问在下列维数下它有多少个独立分量？

1. 二维；
2. 三维。

<details>
<summary>提示 / 解答要点</summary>

指标对 \\((ij)\\) 与 \\((kl)\\) 各自可取 \\(\tfrac{1}{2}n(n-1)\\) 个不同值；再计及 \\((ij)\leftrightarrow(kl)\\) 对称，独立分量数为

\\[
\frac{1}{2}\cdot\frac{n(n-1)}{2}\Bigl(\frac{n(n-1)}{2}+1\Bigr) .
\\]

\\(n=2\\) 时为 1；\\(n=3\\) 时为 6。

</details>

### 习题 9（与叉积相伴的矩阵）

设三维矩阵由向量 \\(\mathbf{a}\\) 定义为 \\(A\_{jk}=\varepsilon\_{jkl}a\_l\\)。

1. 用爱因斯坦记号写出 \\(\mathbf{v}=A\mathbf{b}\\) 的分量形式，并说明 \\(\mathbf{v}\\) 与 \\(\mathbf{a}\times\mathbf{b}\\) 的关系。
2. 证明 \\(\varepsilon\_{mjk}A\_{jk}=(\delta\_{kk}\delta\_{ml}-\delta\_{kl}\delta\_{km})a\_l\\)。
3. 由此证明 \\(a\_m=\tfrac{1}{2}\varepsilon\_{mjk}A\_{jk}\\)。
4. 用爱因斯坦记号写出 \\(\det A\\)（并说明所用符号）。
5. 用爱因斯坦记号证明 \\(\operatorname{tr}(BC)=\operatorname{tr}(CB)\\)。
6. 变换 \\(x^{\prime}\_i=L\_{ij}x\_j\\) 中 \\(L\\) 正交。证明向量长度在该变换下不变。

<details>
<summary>提示 / 解答要点</summary>

1. \\(v\_j=A\_{jk}b\_k=\varepsilon\_{jkl}a\_l b\_k\\)。因 \\((\mathbf{a}\times\mathbf{b})\_j=\varepsilon\_{jkl}a\_k b\_l\\) 且 \\(\varepsilon\_{jkl}=-\varepsilon\_{jlk}\\)，故 \\(\mathbf{v}=-\mathbf{a}\times\mathbf{b}\\)（或写 \\(v\_j=-\varepsilon\_{jkl}a\_k b\_l\\)）。
2. \\(\varepsilon\_{mjk}A\_{jk}=\varepsilon\_{mjk}\varepsilon\_{jkl}a\_l\\)，再利用缩并恒等式。
3. \\(\delta\_{kk}=3\\)，故 \\(\varepsilon\_{mjk}A\_{jk}=2\delta\_{ml}a\_l\\)，除以 2 并对 \\(l\\) 求和即得。
4. \\(\det A=\varepsilon\_{jkl}A\_{1j}A\_{2k}A\_{3l}=\varepsilon\_{jkl}\varepsilon\_{1jn}a\_n\varepsilon\_{2kp}a\_p\varepsilon\_{3lt}a\_t\\)。
5. \\(\operatorname{tr}(BC)=B\_{ab}C\_{ba}=C\_{ba}B\_{ab}=\operatorname{tr}(CB)\\)。
6. \\(x^{\prime}\_i x^{\prime}\_i=(L\_{ij}x\_j)(L\_{ik}x\_k)=L\_{ij}L\_{ik}x\_j x\_k=\delta\_{jk}x\_j x\_k=x\_j x\_j\\)，故 \\(|\mathbf{x}^{\prime}|=|\mathbf{x}|\\)。

</details>

正文中的定义与恒等式见[指标记号与爱因斯坦求和约定](04-index-notation.md)。
