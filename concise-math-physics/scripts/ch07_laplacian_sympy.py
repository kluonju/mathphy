#!/usr/bin/env python3
"""Symbolic Laplacian in spherical/cylindrical coordinates."""
try:
    import sympy as sp

    r = sp.symbols("r", positive=True)
    u = sp.Function("u")(r)
    lap_r = (1 / r**2) * sp.diff(r**2 * sp.diff(u, r), r)
    print("Spherical symmetric Laplacian:", lap_r)
    print("ODE solutions:", sp.dsolve(lap_r, u))

    rho, phi, z = sp.symbols("rho phi z", real=True)
    u_cyl = rho**2 * sp.sin(phi)
    lap_cyl = (1 / rho) * sp.diff(rho * sp.diff(u_cyl, rho), rho) + \
              (1 / rho**2) * sp.diff(u_cyl, phi, 2) + sp.diff(u_cyl, z, 2)
    print("Laplacian of rho^2 sin(phi):", sp.simplify(lap_cyl))
except ImportError:
    print("Spherical u(r): nabla^2 u = (1/r^2) d/dr(r^2 du/dr) = 0 => u = A/r + B")
    print("Install sympy for full symbolic verification")
