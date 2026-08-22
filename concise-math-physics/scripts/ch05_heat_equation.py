#!/usr/bin/env python3
"""1D heat equation explicit finite difference."""
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
    L, T_final, nx, nt = 1.0, 0.1, 100, 500
    kappa = 0.01
    dx = L / (nx - 1)
    dt = T_final / nt
    r = kappa * dt / dx**2
    assert r <= 0.5, f"Unstable: r={r}"

    x = np.linspace(0, L, nx)
    u = np.sin(np.pi * x)
    u[0] = u[-1] = 0

    for _ in range(nt):
        u_new = u.copy()
        u_new[1:-1] = u[1:-1] + r * (u[2:] - 2 * u[1:-1] + u[:-2])
        u = u_new

    print(f"t={T_final}: max u = {u.max():.6f} (exact decay factor exp(-kappa*pi^2*t) ~ {np.exp(-kappa * np.pi**2 * T_final):.6f})")

    if HAS_MPL:
        plt.plot(x, u)
        plt.xlabel("x")
        plt.ylabel("u")
        plt.title("1D heat equation")
        plt.savefig(os.path.join(FIG_DIR, "ch05_heat.png"), dpi=120)


if __name__ == "__main__":
    main()
