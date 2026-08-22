# 应用与数值实验

## 一维热传导 FDM

```python
# scripts/ch05_heat_equation.py
import numpy as np
import matplotlib.pyplot as plt

L, T_final, nx, nt = 1.0, 0.1, 100, 500
kappa = 0.01
dx = L / (nx - 1)
dt = T_final / nt
r = kappa * dt / dx**2
if r > 0.5:
raise ValueError("Unstable: r > 0.5")

x = np.linspace(0, L, nx)
u = np.sin(np.pi * x)
u[0] = u[-1] = 0
for _ in range(nt):
u_new = u.copy()
u_new[1:-1] = u[1:-1] + r * (u[2:] - 2 * u[1:-1] + u[:-2])
u = u_new
plt.plot(x, u, label=f"t={T_final}")
plt.xlabel("x")
plt.ylabel("u")
plt.title("1D heat equation (explicit FDM)")
plt.savefig("assets/figures/ch05_heat.png", dpi=120)
print("max u =", u.max())
```

```julia
# scripts/ch05_wave_equation.jl
# 1D wave equation explicit scheme
L, c, nx, nt = 1.0, 1.0, 100, 200
dx = L / (nx - 1)
dt = 0.5 * dx / c
x = range(0, L, length=nx)
u = sin.(π * x)
u_prev = copy(u)
for _ in 1:nt
u_next = similar(u)
u_next[1] = u_next[end] = 0.0
for i in 2:nx-1
u_next[i] = 2u[i] - u_prev[i] + (c*dt/dx)^2 * (u[i+1] - 2u[i] + u[i-1])
end
u_prev, u = u, u_next
end
println("Wave simulation done, u midpoint = ", u[nx÷2])
```
