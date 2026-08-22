#!/usr/bin/env python3
"""Solve y'' + y = 0 with scipy."""
import os
import numpy as np

try:
    from scipy.integrate import solve_ivp
    HAS_SCIPY = True
except ImportError:
    HAS_SCIPY = False

try:
    import matplotlib.pyplot as plt
    HAS_MPL = True
except ImportError:
    HAS_MPL = False

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FIG_DIR = os.path.join(ROOT, "assets", "figures")
os.makedirs(FIG_DIR, exist_ok=True)


def harmonic(t, y):
    return [y[1], -y[0]]


def euler_solve(y0, t_end, n=2000):
    dt = t_end / n
    y = np.array(y0, dtype=float)
    ts = [0.0]
    ys = [y.copy()]
    for _ in range(n):
        dydt = np.array([y[1], -y[0]])
        y = y + dt * dydt
        ts.append(ts[-1] + dt)
        ys.append(y.copy())
    return np.array(ts), np.array(ys).T


def main():
    if HAS_SCIPY:
        sol = solve_ivp(harmonic, [0, 10], [1.0, 0.0], t_eval=np.linspace(0, 10, 200))
        t, y = sol.t, sol.y
    else:
        t, y = euler_solve([1.0, 0.0], 10.0)  # y shape (2, n_steps)
    idx = np.argmin(np.abs(t - 2 * np.pi))
    print(f"y(2π) ≈ {y[0, idx]:.6f} (expect ~1)")
    if HAS_MPL:
        plt.plot(t, y[0], label="y")
        plt.plot(t, y[1], label="y'")
        plt.legend()
        plt.savefig(os.path.join(FIG_DIR, "ch06_ode.png"), dpi=120)


if __name__ == "__main__":
    main()
