#!/usr/bin/env python3
"""Fourier series approximation of square wave."""
import os
import numpy as np

try:
    import matplotlib.pyplot as plt
    HAS_MPL = True
except ImportError:
    HAS_MPL = False

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FIG_DIR = os.path.join(ROOT, "assets", "figures")
os.makedirs(FIG_DIR, exist_ok=True)


def main():
    x = np.linspace(-np.pi, np.pi, 500)
    f = np.sign(np.sin(x))
    for N in [1, 3, 5, 21]:
        s = sum((4 / (n * np.pi)) * np.sin(n * x) for n in range(1, N + 1, 2))
        err = np.max(np.abs(f - s))
        print(f"N={N}: max error = {err:.4f}")

    if HAS_MPL:
        fig, axes = plt.subplots(2, 2, figsize=(8, 6))
        for ax, N in zip(axes.flat, [1, 3, 5, 21]):
            s = sum((4 / (n * np.pi)) * np.sin(n * x) for n in range(1, N + 1, 2))
            ax.plot(x, f, "k--", label="square wave")
            ax.plot(x, s, label=f"N={N}")
            ax.legend()
            ax.set_title(f"Odd harmonics up to n={N}")
        plt.tight_layout()
        out = os.path.join(FIG_DIR, "ch03_square_wave.png")
        plt.savefig(out, dpi=120)
        print("Saved", out)


if __name__ == "__main__":
    main()
