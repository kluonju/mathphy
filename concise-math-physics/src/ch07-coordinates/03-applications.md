# 应用与数值实验

```python
# scripts/ch07_laplacian_sympy.py
import sympy as sp

r, theta, phi = sp.symbols("r theta phi", positive=True)
u = sp.Function("u")(r)
laplacian_r = (1 / r**2) * sp.diff(r**2 * sp.diff(u, r), r)
print("Spherical symmetric Laplacian:", laplacian_r)
print("Solutions of Laplacian=0:", sp.dsolve(laplacian_r, u))

# Cylindrical: u = rho^2 sin(phi)
rho, ph, z = sp.symbols("rho phi z", real=True)
u_cyl = rho**2 * sp.sin(phi)
lap_cyl = (1 / rho) * sp.diff(rho * sp.diff(u_cyl, rho), rho) +
(1 / rho**2) * sp.diff(u_cyl, phi, 2) + sp.diff(u_cyl, z, 2)
print("Laplacian of rho^2 sin(phi):", sp.simplify(lap_cyl))
```
