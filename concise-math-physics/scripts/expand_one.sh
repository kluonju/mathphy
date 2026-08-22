#!/usr/bin/env bash
# Regenerate a single src/*.md from lecture/*.tex
set -e
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
LEC="$(cd "$ROOT/../lecture" && pwd)"
PY="$ROOT/scripts/tex2md.py"
FIX="$ROOT/scripts/fix_math.py"
SRC="$ROOT/src"

if [ -z "$1" ]; then
  echo "Usage: expand_one.sh <path-under-src> [path2 ...]"
  echo "Example: expand_one.sh ch01-complex/01-complex-numbers.md"
  exit 1
fi

run_tex() {
  local out="$SRC/$1"
  shift
  local tex_files=("$@")
  echo "==> $1"
  python3 "$PY" "$out" "${tex_files[@]}"
  python3 "$FIX" "$out"
}

preserve_tail() {
  local f="$SRC/$1"
  local marker="$2"
  if [ -f "$f" ] && grep -q "^${marker}" "$f" 2>/dev/null; then
    sed -n "/^${marker}/,\$p" "$f"
  fi
}

strip_prerequisite_from_complex_numbers() {
  local f="$SRC/ch01-complex/01-complex-numbers.md"
  python3 - "$f" <<'PY'
import re, sys
path = sys.argv[1]
text = open(path, encoding="utf-8").read()
text = re.sub(
    r"^### 预备知识\n.*?(?=^### 复数的定义)",
    "",
    text,
    count=1,
    flags=re.MULTILINE | re.DOTALL,
)
open(path, "w", encoding="utf-8").write(text)
PY
}

expand_file() {
  local rel="$1"
  local tail_marker=""
  case "$rel" in
    ch01-complex/06-applications.md)
      tail_marker="## 数值实验"
      local tail
      tail=$(preserve_tail "$rel" "$tail_marker")
      run_tex "$rel" \
        "$LEC/complex/integral_demo.tex" \
        "$LEC/complex/feynman_technique.tex"
      if [ -n "$tail" ]; then
        printf '\n%s\n' "$tail" >> "$SRC/$rel"
      else
        cat >> "$SRC/$rel" << 'EOF'

---

## 数值实验

```bash
python scripts/ch01_residue_integral.py
julia scripts/ch01_residue_integral.jl
```
EOF
      fi
      ;;
    ch03-fourier/05-applications.md)
      tail_marker="## 数值实验"
      local tail
      tail=$(preserve_tail "$rel" "$tail_marker")
      run_tex "$rel" "$LEC/fourier/applications.tex"
      [ -n "$tail" ] && printf '\n%s\n' "$tail" >> "$SRC/$rel"
      ;;
    ch01-complex/01-complex-numbers.md)
      run_tex "$rel" "$LEC/complex/complex_variable.tex"
      strip_prerequisite_from_complex_numbers ;;
    ch01-complex/02-analytic.md)
      run_tex "$rel" \
        "$LEC/complex/complex_function.tex" \
        "$LEC/complex/complex_derivate.tex" \
        "$LEC/complex/complex_analytic.tex" \
        "$LEC/complex/multivalued_functions.tex" ;;
    ch01-complex/03-cauchy.md)
      run_tex "$rel" \
        "$LEC/complex/complex_integral.tex" \
        "$LEC/complex/cauchy_theorem.tex" \
        "$LEC/complex/cauchy_formula.tex" ;;
    ch01-complex/04-series.md)
      run_tex "$rel" \
        "$LEC/complex/series.tex" \
        "$LEC/complex/convergence_test.tex" \
        "$LEC/complex/power_series.tex" \
        "$LEC/complex/taylor_laurent_series.tex" \
        "$LEC/complex/singular_points.tex" ;;
    ch01-complex/05-residue.md)
      run_tex "$rel" \
        "$LEC/complex/residue_theorem.tex" \
        "$LEC/complex/residue_theorem_applications.tex" \
        "$LEC/complex/trigonometric_integrals.tex" ;;
    ch02-variation/01-functional.md)
      run_tex "$rel" "$LEC/calculus_variation/functional.tex" ;;
    ch02-variation/02-hamilton.md)
      run_tex "$rel" "$LEC/calculus_variation/hamilton_equations.tex" ;;
    ch02-variation/03-constrained.md)
      run_tex "$rel" "$LEC/calculus_variation/constrained.tex" ;;
    ch03-fourier/01-fourier-series.md)
      run_tex "$rel" "$LEC/fourier/fourier_series.tex" ;;
    ch03-fourier/02-fourier-transform.md)
      run_tex "$rel" "$LEC/fourier/fourier_transform.tex" ;;
    ch03-fourier/03-laplace.md)
      run_tex "$rel" "$LEC/fourier/laplace_transform.tex" ;;
    ch03-fourier/04-inverse-laplace.md)
      run_tex "$rel" "$LEC/fourier/inverse_laplace_transform.tex" ;;
    ch04-special/01-delta.md)
      run_tex "$rel" "$LEC/special/delta_function.tex" ;;
    ch04-special/02-gamma-psi.md)
      run_tex "$rel" "$LEC/special/gamma.tex" "$LEC/special/psi.tex" ;;
    ch04-special/03-zeta.md)
      run_tex "$rel" "$LEC/special/zeta.tex" ;;
    ch05-math-physics-eq/01-derivation.md)
      run_tex "$rel" "$LEC/mathphyequations/equations.tex" ;;
    ch05-math-physics-eq/02-classification.md)
      run_tex "$rel" \
        "$LEC/mathphyequations/classification.tex" \
        "$LEC/mathphyequations/stationary.tex" ;;
    ch05-math-physics-eq/03-separation.md)
      run_tex "$rel" \
        "$LEC/mathphyequations/varsep.tex" \
        "$LEC/mathphyequations/cartesian.tex" ;;
    ch05-math-physics-eq/04-inhomo-boundary.md)
      run_tex "$rel" "$LEC/separation/inhomo_boundary.tex" ;;
    ch06-pde/01-first-order.md)
      run_tex "$rel" "$LEC/diffeq/first_order.tex" ;;
    ch06-pde/02-second-order.md)
      run_tex "$rel" "$LEC/diffeq/second_order.tex" ;;
    ch06-pde/03-sturm-liouville.md)
      run_tex "$rel" "$LEC/diffeq/sturm_liouville.tex" ;;
    ch06-pde/04-generating-function.md)
      run_tex "$rel" "$LEC/diffeq/generating_function.tex" ;;
    ch07-coordinates/01-general.md)
      run_tex "$rel" "$LEC/curvedcoordinates/coordinates.tex" ;;
    ch07-coordinates/02-cylindrical-spherical.md)
      run_tex "$rel" \
        "$LEC/curvedcoordinates/cylindrical.tex" \
        "$LEC/curvedcoordinates/spherical.tex" ;;
    appendix/series.md)
      run_tex "$rel" "$LEC/appendix/series_expansion.tex" ;;
    appendix/vector-identities.md)
      run_tex "$rel" "$LEC/appendix/vector_identities.tex" ;;
    ch08-numerical/01-finding-zeros.md)
      run_tex "$rel" "$LEC/numerical/finding_zeros.tex" ;;
    ch08-numerical/02-integration.md)
      run_tex "$rel" "$LEC/numerical/num_integration.tex" ;;
    ch09-tensor/01-vector-algebra.md)
      run_tex "$rel" "$LEC/tensor/vector_algebra.tex" ;;
    ch09-tensor/02-coordinates.md)
      run_tex "$rel" "$LEC/tensor/coordinate.tex" ;;
    ch09-tensor/03-grad-del.md)
      run_tex "$rel" "$LEC/tensor/grad_del.tex" ;;
    intro.md|ch00-prerequisites/index.md|ch00-prerequisites/01-sets-and-logic.md|\
    ch00-prerequisites/02-trigonometry.md|ch00-prerequisites/03-calculus.md|\
    ch00-prerequisites/04-index-notation.md|ch00-prerequisites/05-vector-analysis.md|\
    ch00-prerequisites/06-linear-algebra.md|ch01-complex/index.md|ch02-variation/index.md|ch03-fourier/index.md|\
    ch04-special/index.md|ch05-math-physics-eq/index.md|ch06-pde/index.md|\
    ch07-coordinates/index.md|ch08-numerical/index.md|ch09-tensor/index.md|\
    ch02-variation/04-applications.md|ch04-special/04-applications.md|\
    ch05-math-physics-eq/05-applications.md|ch06-pde/05-applications.md|ch07-coordinates/03-applications.md)
      echo "Skip (no lecture tex mapping): $rel — run fix_math only"
      python3 "$FIX" "$SRC/$rel" 2>/dev/null || true
      ;;
    *)
      echo "Unknown file: $rel"
      exit 1
      ;;
  esac
}

for rel in "$@"; do
  rel="${rel#src/}"
  expand_file "$rel"
done

echo "Done."
