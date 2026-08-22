#!/usr/bin/env bash
set -e
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
LEC="$(cd "$ROOT/../lecture" && pwd)"
PY="$ROOT/scripts/tex2md.py"
SRC="$ROOT/src"

run() { python3 "$PY" "$1" "${@:2}"; }

# Ch01 复变
run "$SRC/ch01-complex/01-complex-numbers.md" \
  "$LEC/complex/complex_variable.tex"
run "$SRC/ch01-complex/02-analytic.md" \
  "$LEC/complex/complex_function.tex" \
  "$LEC/complex/complex_derivate.tex" \
  "$LEC/complex/complex_analytic.tex" \
  "$LEC/complex/multivalued_functions.tex"
run "$SRC/ch01-complex/03-cauchy.md" \
  "$LEC/complex/complex_integral.tex" \
  "$LEC/complex/cauchy_theorem.tex" \
  "$LEC/complex/cauchy_formula.tex"
run "$SRC/ch01-complex/04-series.md" \
  "$LEC/complex/series.tex" \
  "$LEC/complex/convergence_test.tex" \
  "$LEC/complex/power_series.tex" \
  "$LEC/complex/taylor_laurent_series.tex" \
  "$LEC/complex/singular_points.tex"
run "$SRC/ch01-complex/05-residue.md" \
  "$LEC/complex/residue_theorem.tex" \
  "$LEC/complex/residue_theorem_applications.tex" \
  "$LEC/complex/trigonometric_integrals.tex"
run "$SRC/ch01-complex/06-applications.md" \
  "$LEC/complex/integral_demo.tex" \
  "$LEC/complex/feynman_technique.tex"
cat >> "$SRC/ch01-complex/06-applications.md" << 'EOF'

---

## 数值实验

```bash
python scripts/ch01_residue_integral.py
julia scripts/ch01_residue_integral.jl
```
EOF

# Ch02 变分
run "$SRC/ch02-variation/01-functional.md" "$LEC/calculus_variation/functional.tex"
run "$SRC/ch02-variation/02-hamilton.md" "$LEC/calculus_variation/hamilton_equations.tex"
run "$SRC/ch02-variation/03-constrained.md" "$LEC/calculus_variation/constrained.tex"

# Ch03 傅里叶
run "$SRC/ch03-fourier/01-fourier-series.md" "$LEC/fourier/fourier_series.tex"
run "$SRC/ch03-fourier/02-fourier-transform.md" "$LEC/fourier/fourier_transform.tex"
run "$SRC/ch03-fourier/03-laplace.md" "$LEC/fourier/laplace_transform.tex"
run "$SRC/ch03-fourier/04-inverse-laplace.md" "$LEC/fourier/inverse_laplace_transform.tex"
APP03="$SRC/ch03-fourier/05-applications.md"
NUM03=$(sed -n '/^## 数值实验/,$p' "$APP03" 2>/dev/null || true)
run "$APP03" "$LEC/fourier/applications.tex"
if [ -n "$NUM03" ]; then
  printf '\n%s\n' "$NUM03" >> "$APP03"
fi

# Ch04 特殊函数
run "$SRC/ch04-special/01-delta.md" "$LEC/special/delta_function.tex"
run "$SRC/ch04-special/02-gamma-psi.md" "$LEC/special/gamma.tex" "$LEC/special/psi.tex"
run "$SRC/ch04-special/03-zeta.md" "$LEC/special/zeta.tex"

# Ch05 数理方程
run "$SRC/ch05-math-physics-eq/01-derivation.md" "$LEC/mathphyequations/equations.tex"
run "$SRC/ch05-math-physics-eq/02-classification.md" \
  "$LEC/mathphyequations/classification.tex" "$LEC/mathphyequations/stationary.tex"
run "$SRC/ch05-math-physics-eq/03-separation.md" \
  "$LEC/mathphyequations/varsep.tex" "$LEC/mathphyequations/cartesian.tex"
run "$SRC/ch05-math-physics-eq/04-inhomo-boundary.md" \
  "$LEC/separation/inhomo_boundary.tex"

# Ch06 ODE
run "$SRC/ch06-pde/01-first-order.md" "$LEC/diffeq/first_order.tex"
run "$SRC/ch06-pde/02-second-order.md" "$LEC/diffeq/second_order.tex"
run "$SRC/ch06-pde/03-sturm-liouville.md" "$LEC/diffeq/sturm_liouville.tex"
run "$SRC/ch06-pde/04-generating-function.md" "$LEC/diffeq/generating_function.tex"

# Ch07 坐标
run "$SRC/ch07-coordinates/01-general.md" "$LEC/curvedcoordinates/coordinates.tex"
run "$SRC/ch07-coordinates/02-cylindrical-spherical.md" \
  "$LEC/curvedcoordinates/cylindrical.tex" "$LEC/curvedcoordinates/spherical.tex"

# Ch08 数值方法
run "$SRC/ch08-numerical/01-finding-zeros.md" "$LEC/numerical/finding_zeros.tex"
run "$SRC/ch08-numerical/02-integration.md" "$LEC/numerical/num_integration.tex"

# Ch09 矢量与张量
run "$SRC/ch09-tensor/01-vector-algebra.md" "$LEC/tensor/vector_algebra.tex"
run "$SRC/ch09-tensor/02-coordinates.md" "$LEC/tensor/coordinate.tex"
run "$SRC/ch09-tensor/03-grad-del.md" "$LEC/tensor/grad_del.tex"

# 附录
run "$SRC/appendix/series.md" "$LEC/appendix/series_expansion.tex"
run "$SRC/appendix/vector-identities.md" "$LEC/appendix/vector_identities.tex"

echo "Fixing math environments for MathJax..."
python3 "$ROOT/scripts/fix_math.py"

echo "All chapters expanded from lecture/"
