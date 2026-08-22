# 应用与数值实验

```python
# scripts/ch04_special_functions.py
import numpy as np
import matplotlib.pyplot as plt
from scipy.special import gamma as Gamma, digamma

x = np.linspace(0.1, 5, 200)
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4))
ax1.plot(x, Gamma(x), label=r"$\Gamma(x)$")
ax1.set_title("Gamma function")
ax2.plot(x, digamma(x), label=r"$\psi(x)$")
ax2.set_title("Digamma function")
for ax in (ax1, ax2):
ax.legend()
ax.grid(True)
plt.savefig("assets/figures/ch04_gamma_psi.png", dpi=120)
print("Saved assets/figures/ch04_gamma_psi.png")

# Gaussian delta limit
eps_vals = [0.5, 0.2, 0.05]
x = np.linspace(-2, 2, 500)
for eps in eps_vals:
g = np.exp(-x**2 / (2 * eps**2)) / (np.sqrt(2 * np.pi) * eps)
plt.figure()
plt.plot(x, g, label=f"eps={eps}")
plt.savefig("assets/figures/ch04_delta_limit.png", dpi=120)
print("delta limit plot saved")
```
