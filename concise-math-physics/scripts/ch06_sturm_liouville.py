#!/usr/bin/env python3
"""Sturm-Liouville eigenvalues on [0, pi]."""
import numpy as np

L = np.pi
x = np.linspace(0, L, 1000)
for k in range(1, 6):
    lam = (k * np.pi / L) ** 2
    integral = np.trapezoid(np.sin(k * x) ** 2, x)
    print(f"n={k}: lambda={lam:.4f}, norm^2 integral={integral:.4f}")
