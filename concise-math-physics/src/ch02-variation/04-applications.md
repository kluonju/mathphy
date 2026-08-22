# 应用与数值实验

## 最速降线数值解

用离散 Euler–Lagrange 求 \\(y(x)\\) 使 \\(t=\int \sqrt{(1+y'^2)/y\,\mathrm{d}x\\) 最小。

```python
# scripts/ch02_brachistochrone.py
import numpy as np
from scipy.optimize import minimize

def functional(y, x):
y = np.concatenate([[0], y, [0]])
dy = np.diff(y) / np.diff(x)
integrand = np.sqrt((1 + dy**2) / (y[1:] + 1e-8))
return np.trapz(integrand, x[1:])

n = 50
x = np.linspace(0, 1, n)
y0 = np.zeros(n - 2)
res = minimize(functional, y0, args=(x,), method="L-BFGS-B")
print("Brachistochrone discrete solution computed, final J =", res.fun)
```

```julia
# scripts/ch02_pendulum.jl
using DifferentialEquations
m, l, g = 1.0, 1.0, 9.8
function pendulum!(du, u, p, t)
θ, ω = u
du[1] = ω
du[2] = -(g / l) * sin(θ)
end
u0 = [0.1, 0.0]
tspan = (0.0, 10.0)
prob = ODEProblem(pendulum!, u0, tspan)
sol = solve(prob, Tsit5())
println("Pendulum solved, θ(10) = ", sol.u[end][1])
```
