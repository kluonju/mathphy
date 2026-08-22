#!/usr/bin/env python3
"""Laplace transform solution of harmonic oscillator."""
try:
    from sympy import symbols, simplify
    from sympy.integrals.laplace import inverse_laplace_transform

    t, p, X0, m, k = symbols("t p X0 m k", positive=True)
    omega0 = (k / m) ** 0.5
    x_p = X0 * p / (p**2 + omega0**2)
    x_t = inverse_laplace_transform(x_p, p, t)
    print("X(t) =", simplify(x_t))
except ImportError:
    print("X(t) = X0*cos(omega0*t)  [install sympy for symbolic check]")
