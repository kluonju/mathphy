#!/usr/bin/env bash
# Regenerate + fix all lecture-backed chapters in SUMMARY order
set -e
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"
chmod +x scripts/expand_one.sh

TEX_FILES=(
  ch01-complex/01-complex-numbers.md
  ch01-complex/02-analytic.md
  ch01-complex/03-cauchy.md
  ch01-complex/04-series.md
  ch01-complex/05-residue.md
  ch01-complex/06-applications.md
  ch02-variation/01-functional.md
  ch02-variation/02-hamilton.md
  ch02-variation/03-constrained.md
  ch03-fourier/01-fourier-series.md
  ch03-fourier/02-fourier-transform.md
  ch03-fourier/03-laplace.md
  ch03-fourier/04-inverse-laplace.md
  ch03-fourier/05-applications.md
  ch04-special/01-delta.md
  ch04-special/02-gamma-psi.md
  ch04-special/03-zeta.md
  ch05-math-physics-eq/01-derivation.md
  ch05-math-physics-eq/02-classification.md
  ch05-math-physics-eq/03-separation.md
  ch05-math-physics-eq/04-inhomo-boundary.md
  ch06-pde/01-first-order.md
  ch06-pde/02-second-order.md
  ch06-pde/03-sturm-liouville.md
  ch06-pde/04-generating-function.md
  ch07-coordinates/01-general.md
  ch07-coordinates/02-cylindrical-spherical.md
  ch08-numerical/01-finding-zeros.md
  ch08-numerical/02-integration.md
  ch09-tensor/01-vector-algebra.md
  ch09-tensor/02-coordinates.md
  ch09-tensor/03-grad-del.md
  appendix/series.md
  appendix/vector-identities.md
)

FIX_ONLY=(
  intro.md
  ch00-prerequisites/index.md
  ch00-prerequisites/01-sets-and-logic.md
  ch00-prerequisites/02-trigonometry.md
  ch00-prerequisites/03-calculus.md
  ch00-prerequisites/04-index-notation.md
  ch00-prerequisites/05-vector-analysis.md
  ch00-prerequisites/06-linear-algebra.md
  ch01-complex/index.md
  ch02-variation/index.md
  ch02-variation/04-applications.md
  ch03-fourier/index.md
  ch04-special/index.md
  ch04-special/04-applications.md
  ch05-math-physics-eq/index.md
  ch05-math-physics-eq/05-applications.md
  ch06-pde/index.md
  ch06-pde/05-applications.md
  ch07-coordinates/index.md
  ch07-coordinates/03-applications.md
  ch08-numerical/index.md
  ch09-tensor/index.md
)

for f in "${TEX_FILES[@]}"; do
  bash scripts/expand_one.sh "$f"
done

for f in "${FIX_ONLY[@]}"; do
  python3 scripts/fix_math.py "src/$f"
done

python3 scripts/fix_classification_md.py
python3 scripts/fix_math.py src/ch02-variation/01-functional.md

echo "=== Lint summary ==="
ERR=0
while IFS= read -r f; do
  if ! python3 scripts/lint_math.py "src/$f" 2>/dev/null; then
    ERR=1
  fi
done < <(grep -oP '\./\K[^)]+\.md' src/SUMMARY.md)

exit $ERR
