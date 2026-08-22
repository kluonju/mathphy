#!/usr/bin/env python3
"""Discrete brachistochrone: compare straight line vs parabola."""
import numpy as np


def functional(y, x):
    y = np.concatenate([[0], y, [0]])
    dy = np.diff(y) / np.diff(x)
    integrand = np.sqrt((1 + dy**2) / (y[1:] + 1e-8))
    return np.trapezoid(integrand, x[1:])


def main():
    n = 50
    x = np.linspace(0, 1, n)
    y_line = np.zeros(n - 2)
    y_para = 0.5 * x[1:-1] * (1 - x[1:-1])  # smooth descent, y > 0
    j_line = functional(y_line, x)
    j_para = functional(y_para, x)
    print(f"Straight line: J = {j_line:.6f}")
    print(f"Parabola candidate: J = {j_para:.6f} (lower is faster descent)")


if __name__ == "__main__":
    main()
