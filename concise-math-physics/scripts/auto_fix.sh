#!/usr/bin/env bash
# Auto-fix all math in src/: expand lecture-backed chapters, fix_math, classification patch, lint.
set -e
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"
chmod +x scripts/fix_all_ordered.sh scripts/expand_one.sh

echo "=== Regenerate + fix (SUMMARY order) ==="
bash scripts/fix_all_ordered.sh

echo "=== Final pass: fix_math (classification handled separately) ==="
python3 scripts/fix_math.py src

echo "=== Lint all SUMMARY pages ==="
ERR=0
while IFS= read -r f; do
  rel="${f#src/}"
  if ! python3 scripts/lint_math.py "src/$rel" >/dev/null 2>&1; then
    python3 scripts/lint_math.py "src/$rel" 2>&1 | head -5
    ERR=1
  fi
done < <(grep -oP '\./\K[^)]+\.md' src/SUMMARY.md)

echo "=== mdbook build ==="
mdbook build

exit $ERR
