# 公式修复进度（按 SUMMARY 顺序）

验收：`python3 scripts/lint_math.py src/<file>` 无 error；`mdbook build` 通过。

| 状态 | 文件 | 备注 |
|------|------|------|
| [x] | intro.md | 符号表 |
| [x] | ch01-complex/index.md | |
| [x] | ch01-complex/01-complex-numbers.md | complex_variable.tex |
| [x] | ch01-complex/02-analytic.md | 4 tex |
| [x] | ch01-complex/03-cauchy.md | 3 tex |
| [x] | ch01-complex/04-series.md | 5 tex |
| [x] | ch01-complex/05-residue.md | +trigonometric_integrals.tex |
| [x] | ch01-complex/06-applications.md | +数值实验 |
| [x] | ch02-variation/index.md | |
| [x] | ch02-variation/01-functional.md | |
| [x] | ch02-variation/02-hamilton.md | |
| [x] | ch02-variation/03-constrained.md | |
| [x] | ch02-variation/04-applications.md | 代码为主 |
| [x] | ch03-fourier/index.md | |
| [x] | ch03-fourier/01-fourier-series.md | |
| [x] | ch03-fourier/02-fourier-transform.md | |
| [x] | ch03-fourier/03-laplace.md | |
| [x] | ch03-fourier/04-inverse-laplace.md | |
| [x] | ch03-fourier/05-applications.md | +数值实验 |
| [x] | ch04-special/index.md | |
| [x] | ch04-special/01-delta.md | |
| [x] | ch04-special/02-gamma-psi.md | |
| [x] | ch04-special/03-zeta.md | |
| [x] | ch04-special/04-applications.md | |
| [x] | ch05-math-physics-eq/index.md | |
| [x] | ch05-math-physics-eq/01-derivation.md | |
| [x] | ch05-math-physics-eq/02-classification.md | fix_classification_md.py |
| [x] | ch05-math-physics-eq/03-separation.md | varsep+cartesian |
| [x] | ch05-math-physics-eq/04-inhomo-boundary.md | inhomo_boundary.tex |
| [x] | ch05-math-physics-eq/05-applications.md | 数值实验 |
| [x] | ch06-pde/index.md | diffeq 章首 |
| [x] | ch06-pde/01-first-order.md | |
| [x] | ch06-pde/02-second-order.md | |
| [x] | ch06-pde/03-sturm-liouville.md | 全量重转 |
| [x] | ch06-pde/04-generating-function.md | generating_function.tex |
| [x] | ch06-pde/05-applications.md | 数值实验 |
| [x] | ch07-coordinates/index.md | |
| [x] | ch07-coordinates/01-general.md | |
| [x] | ch07-coordinates/02-cylindrical-spherical.md | |
| [x] | ch07-coordinates/03-applications.md | |
| [x] | ch08-numerical/index.md | |
| [x] | ch08-numerical/01-finding-zeros.md | finding_zeros.tex |
| [x] | ch08-numerical/02-integration.md | num_integration.tex |
| [x] | ch09-tensor/index.md | |
| [x] | ch09-tensor/01-vector-algebra.md | vector_algebra.tex |
| [x] | ch09-tensor/02-coordinates.md | coordinate.tex |
| [x] | ch09-tensor/03-grad-del.md | grad_del.tex |
| [x] | appendix/series.md | |
| [x] | appendix/vector-identities.md | |

**全书**：SUMMARY 所列 48 篇 `lint_math.py` 均为 0 error；`mdbook build` 通过。
