#!/usr/bin/env python3
"""Figures for saddle-point / Laplace / stationary-phase pedagogy."""
from __future__ import annotations

from pathlib import Path

import numpy as np

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, Arc

ROOT = Path(__file__).resolve().parent.parent
FIG = ROOT / "src" / "figures"
FIG.mkdir(parents=True, exist_ok=True)

plt.rcParams.update(
    {
        "font.size": 11,
        "axes.unicode_minus": False,
        "figure.dpi": 140,
        "savefig.bbox": "tight",
    }
)

C_A = "#4C78A8"
C_B = "#E45756"
C_S = "#54A24B"
C_G = "#B279A2"


def save(fig: plt.Figure, name: str) -> None:
    fig.savefig(FIG / name, dpi=160, facecolor="white")
    plt.close(fig)
    print("Saved", name)


def fig_laplace_real() -> None:
    """Laplace method: integrand concentrates near max of f."""
    x = np.linspace(0, 3, 600)
    f = 2 * x - x**2  # max at x=1, f=1
    fig, axes = plt.subplots(1, 2, figsize=(8.6, 3.5))

    ax = axes[0]
    ax.plot(x, f, color=C_A, lw=2, label=r"$f(x)=2x-x^2$")
    ax.axvline(1, color=C_B, ls="--", lw=1)
    ax.plot(1, 1, "o", color=C_B, ms=7)
    ax.set_xlabel(r"$x$")
    ax.set_ylabel(r"$f(x)$")
    ax.set_title("phase / exponent")
    ax.legend(fontsize=9)

    ax = axes[1]
    for lam, c in zip([2, 6, 20], [C_G, C_A, C_B]):
        g = np.exp(lam * f)
        g = g / g.max()
        ax.plot(x, g, color=c, lw=1.8, label=rf"$\lambda={lam}$")
    ax.set_xlabel(r"$x$")
    ax.set_ylabel(r"normalized $e^{\lambda f}$")
    ax.set_title(r"mass concentrates at $x=1$")
    ax.legend(fontsize=8)

    fig.suptitle("Laplace's method on the real line", y=1.03)
    save(fig, "asymp_laplace_real.png")


def fig_saddle_contour() -> None:
    """Steepest descent: saddle of Re(f) and descent/ascent directions."""
    # f(z) = z^2/2  has saddle at 0? f'=z, saddle at 0, Re(f)= (x^2-y^2)/2
    # Better classic: f(z) = i z^3/3 + i z  for Airy-like, or f(z)=z-z^2/2 for Gamma-like
    # Use f(z) = z^2 : saddle at 0, Re = x^2-y^2 — valleys on imag axis
    # Standard demo: f(z) = i(z^3/3 - z) Airy saddle at z=±1
    # Simpler for teaching: f(z) = -z^2 + a, saddle at 0 along steepest = real axis? 
    # f(z)=z^2/2: f'=z, at 0. Re f = (x^2-y^2)/2. Steepest descent of Re: along imag axis.
    
    u = np.linspace(-2.2, 2.2, 200)
    v = np.linspace(-2.2, 2.2, 200)
    U, V = np.meshgrid(u, v)
    # f(z) = z^2 / 2
    Re = 0.5 * (U**2 - V**2)
    Im = U * V

    fig, ax = plt.subplots(figsize=(5.8, 5.2))
    cs = ax.contour(U, V, Re, levels=np.linspace(-2, 2, 17), colors="#999", linewidths=0.7)
    ax.clabel(cs, inline=True, fontsize=7, fmt="%.1f")
    # steepest descent of Re through 0: V axis (x=0)
    ax.plot([0, 0], [-2.1, 2.1], color=C_B, lw=2.4, label=r"steepest descent ($\mathrm{Re}\,f\downarrow$)")
    # steepest ascent: U axis
    ax.plot([-2.1, 2.1], [0, 0], color=C_S, lw=2.0, ls="--", label=r"steepest ascent")
    ax.plot(0, 0, "o", color=C_A, ms=9, zorder=5)
    ax.annotate(r"saddle $z_0$", (0.12, 0.12), color=C_A, fontsize=11)
    # original real-axis contour sketch
    ax.annotate(
        "",
        xy=(1.8, 0.05),
        xytext=(-1.8, 0.05),
        arrowprops=dict(arrowstyle="->", color=C_G, lw=1.5),
    )
    ax.text(0, 0.35, "deform toward valleys", color=C_B, ha="center", fontsize=9)
    ax.set_xlabel(r"$\mathrm{Re}\,z$")
    ax.set_ylabel(r"$\mathrm{Im}\,z$")
    ax.set_title(r"Saddle of $f(z)=z^2/2$: contours of $\mathrm{Re}\,f$")
    ax.set_aspect("equal")
    ax.set_xlim(-2.1, 2.1)
    ax.set_ylim(-2.1, 2.1)
    ax.legend(loc="upper right", fontsize=8, framealpha=0.92)
    save(fig, "asymp_saddle_contour.png")


def fig_stirling_compare() -> None:
    """n! vs Stirling approximation."""
    n = np.arange(1, 31)
    # log gamma
    from math import lgamma

    log_fact = np.array([lgamma(k + 1) for k in n])
    stirling = n * np.log(n) - n + 0.5 * np.log(2 * np.pi * n)
    rel = np.exp(stirling - log_fact)  # Stirling / n!

    fig, axes = plt.subplots(1, 2, figsize=(8.6, 3.5))
    ax = axes[0]
    ax.semilogy(n, np.exp(log_fact), "o-", color=C_A, ms=4, lw=1.2, label=r"$n!$")
    ax.semilogy(n, np.exp(stirling), "s--", color=C_B, ms=4, lw=1.2, label="Stirling")
    ax.set_xlabel(r"$n$")
    ax.set_ylabel(r"value (log scale)")
    ax.set_title(r"$n!$ vs Stirling")
    ax.legend(fontsize=9)

    ax = axes[1]
    ax.plot(n, rel, color=C_S, lw=2)
    ax.axhline(1, color="#888", ls=":", lw=1)
    ax.set_xlabel(r"$n$")
    ax.set_ylabel(r"Stirling$/\,n!$")
    ax.set_title("relative accuracy")
    ax.set_ylim(0.9, 1.02)

    fig.suptitle("Application: Stirling's approximation", y=1.03)
    save(fig, "asymp_stirling.png")


def fig_stationary_phase() -> None:
    """Stationary phase: rapid oscillation away from t_*."""
    t = np.linspace(-2, 2, 2000)
    phi = t**3 / 3 - t  # phi' = t^2-1, stationary at ±1
    fig, axes = plt.subplots(2, 1, figsize=(6.4, 4.8), sharex=True)

    ax = axes[0]
    ax.plot(t, phi, color=C_A, lw=2)
    ax.plot([-1, 1], [phi[np.argmin(np.abs(t + 1))], phi[np.argmin(np.abs(t - 1))]], "o", color=C_B, ms=7)
    ax.set_ylabel(r"$\phi(t)$")
    ax.set_title(r"phase $\phi(t)=t^3/3-t$ (stationary at $t=\pm 1$)")

    ax = axes[1]
    for lam, c, ls in zip([5, 20], [C_G, C_B], ["-", "-"]):
        ax.plot(t, np.cos(lam * phi), color=c, lw=0.9, alpha=0.85, label=rf"$\cos(\lambda\phi)$, $\lambda={lam}$")
    ax.set_xlabel(r"$t$")
    ax.set_ylabel(r"oscillatory factor")
    ax.legend(fontsize=8, loc="upper right")
    ax.set_title("cancellation away from stationary points")

    fig.tight_layout()
    save(fig, "asymp_stationary_phase.png")


def main() -> None:
    fig_laplace_real()
    fig_saddle_contour()
    fig_stirling_compare()
    fig_stationary_phase()


if __name__ == "__main__":
    main()
