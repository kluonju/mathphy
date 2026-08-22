#!/usr/bin/env bash
# Run all Python scripts (Julia scripts optional)
set -e
cd "$(dirname "$0")/.."
mkdir -p assets/figures

echo "=== Python scripts ==="
for s in scripts/ch*.py; do
  echo "Running $s ..."
  python3 "$s"
done

echo "=== Done ==="
