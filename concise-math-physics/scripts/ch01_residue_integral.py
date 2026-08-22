#!/usr/bin/env python3
"""Verify int_0^{2pi} dθ/(1+a cos θ) = 2π/√(1-a²)."""
import numpy as np


def integrand(theta, a):
    return 1.0 / (1 + a * np.cos(theta))


def main():
    theta = np.linspace(0, 2 * np.pi, 10000)
    for a in [0.3, 0.5, 0.9]:
        numeric = np.trapezoid(integrand(theta, a), theta)
        exact = 2 * np.pi / np.sqrt(1 - a**2)
        print(f"a={a}: numeric={numeric:.8f}, exact={exact:.8f}, err={abs(numeric - exact):.2e}")


if __name__ == "__main__":
    main()
