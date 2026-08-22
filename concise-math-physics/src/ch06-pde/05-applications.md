# 应用与数值实验

```python
# scripts/ch06_ode_solver.py
import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

def harmonic(t, y):
return [y[1], -y[0]]

sol = solve_ivp(harmonic, [0, 10], [1.0, 0.0], t_eval=np.linspace(0, 10, 200))
plt.plot(sol.t, sol.y[0], label="y")
plt.plot(sol.t, sol.y[1], label="y'")
plt.legend()
plt.title("y'' + y = 0")
plt.savefig("assets/figures/ch06_ode.png", dpi=120)
print("Period check: y(2pi) ≈", sol.y[0, -1])
```

```python
# scripts/ch06_sturm_liouville.py
import numpy as np

L = np.pi
n = 5
x = np.linspace(0, L, 100)
for k in range(1, n + 1):
lam = (k * np.pi / L) ** 2
y = np.sin(k * x)
print(f"n={k}: lambda_n={lam:.4f}, orthogonality check integral ~",
np.trapz(np.sin(k * x) * np.sin((k + 1) * x), x))
```
