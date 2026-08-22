#!/usr/bin/env python3
"""Plot Gamma and digamma; Gaussian delta limit."""
import os
import numpy as np

import math

try:
    import matplotlib.pyplot as plt
    HAS_MPL = True
except ImportError:
    HAS_MPL = False

try:
    from scipy.special import gamma as Gamma, digamma
    HAS_SCIPY = True
except ImportError:
    HAS_SCIPY = False

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FIG_DIR = os.path.join(ROOT, "assets", "figures")
os.makedirs(FIG_DIR, exist_ok=True)


def main():
    print("Gamma(0.5) = sqrt(pi) =", math.sqrt(math.pi))
    if not HAS_SCIPY:
        print("(Install scipy for plots)")
        return
    x = np.linspace(0.1, 5, 200)
    if HAS_SCIPY and HAS_MPL:
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4))
        ax1.plot(x, Gamma(x))
        ax1.set_title("Gamma(x)")
        ax2.plot(x, digamma(x))
        ax2.set_title("psi(x)")
        plt.tight_layout()
        plt.savefig(os.path.join(FIG_DIR, "ch04_gamma_psi.png"), dpi=120)
        print("Saved ch04_gamma_psi.png")


if __name__ == "__main__":
    main()
