## Huygens–Fresnel–Kirchhoff 衍射（PX284 Appendix J）

几何光学的下一阶是标量衍射。本节据 PX284 Appendix J，由 Helmholtz 方程与 Green 恒等式导出 Kirchhoff 积分，并指出 Fraunhofer 极限与傅里叶变换的联系。

### Helmholtz 方程

单色标量波 \\(V=U(\mathbf{r})e^{-\mathrm{i}\omega t}\\) 满足

\\[
\nabla^2 U+k^2 U=0,\qquad k=\omega/c.
\\]

（极化效应在此近似中忽略。）

### Green 恒等式到 Kirchhoff 积分

对两标量场，Gauss 定理给出 Green 第二恒等式

\\[
\int\_V\bigl(\phi\nabla^2\psi-\psi\nabla^2\phi\bigr)\,\mathrm{d}V
=\oint\_S(\phi\nabla\psi-\psi\nabla\phi)\cdot\mathrm{d}\mathbf{S}.
\\]

若 \\(U\\) 与辅助场 \\(U'=e^{\mathrm{i}kr}/r\\) 均满足 Helmholtz 方程，体积项抵消；但 \\(U'\\) 在观察点 \\(P\\) 奇异，需挖去半径 \\(\varepsilon\\) 的小球。令 \\(\varepsilon\to 0\\) 得 **Helmholtz–Kirchhoff 积分定理**：

\\[
U(P)=\frac{1}{4\pi}\oint\_S\Bigl(U\frac{\partial}{\partial n}\Bigl(\frac{e^{\mathrm{i}kr}}{r}\Bigr)
-\frac{e^{\mathrm{i}kr}}{r}\frac{\partial U}{\partial n}\Bigr)\,\mathrm{d}S.
\\]

（\\(n\\) 取指向积分区域内部的法向约定时符号与上式一致。）

### 孔径近似与倾斜因子

实际问题中常假定孔径外 \\(U=\partial U/\partial n=0\\)，积分缩到波前/孔径 \\(A\\)。若入射为球波 \\(U=Ae^{\mathrm{i}kr\_0}/r\_0\\)，并在 \\(kr\gg 1\\) 时丢掉相对小的 \\(1/r\\) 项，得 Kirchhoff 衍射公式

\\[
U(P)\approx -\frac{\mathrm{i}A e^{\mathrm{i}kr\_0}}{2\lambda r\_0}
\int\_A\frac{e^{\mathrm{i}kr}}{r}(1+\cos\chi)\,\mathrm{d}S,
\\]

其中 \\(\chi\\) 为波前法向与到 \\(P\\) 的连线夹角。倾斜因子

\\[
K(\chi)=-\frac{\mathrm{i}}{2\lambda}(1+\cos\chi)
\\]

在 \\(\chi=0\\) 最大、\\(\chi=\pi\\) 为零，从而抑制 Huygens 构图中的“反向波”。

### Fraunhofer 与 Fourier

远场（Fraunhofer）下相位在孔径上近似对坐标**线性**，衍射振幅化为孔径透过函数的**傅里叶变换**——与第 [3 章](../ch03-fourier/02-fourier-transform.md) 直接衔接。近场（Fresnel）保留二次相位，积分更难，但仍是同一 Kirchhoff 骨架的近似。

相关：[程函与几何光学](eikonal.md)、[傅里叶变换](../ch03-fourier/02-fourier-transform.md)；细节见 Born & Wolf 第 8 章。
