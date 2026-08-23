#!/usr/bin/env python3
"""Pedagogical figures for Ch.8 numerical methods."""
from __future__ import annotations

from pathlib import Path

import numpy as np

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon

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


def fig_bisection() -> None:
    def f(x):
        return x**3 - x - 2

    xs = np.linspace(0.8, 2.2, 400)
    fig, ax = plt.subplots(figsize=(6.2, 3.8))
    ax.axhline(0, color="#888", lw=0.8)
    ax.plot(xs, f(xs), color=C_A, lw=2, label=r"$f(x)=x^3-x-2$")
    intervals = [(1.0, 2.0), (1.0, 1.5), (1.375, 1.5), (1.375, 1.4375)]
    for k, (a, b) in enumerate(intervals):
        m = 0.5 * (a + b)
        ax.plot([a, b], [0, 0], color=C_B, lw=3.5 - 0.5 * k, alpha=0.55 + 0.1 * k, solid_capstyle="butt")
        ax.plot(m, 0, "o", color=C_S, ms=6)
    ax.plot(1.521, 0, "s", color=C_G, ms=7, label=r"root $\approx 1.521$")
    ax.set_xlabel(r"$x$")
    ax.set_ylabel(r"$f(x)$")
    ax.set_title("Bisection: nested brackets")
    ax.legend(loc="upper left", fontsize=9)
    ax.set_xlim(0.8, 2.2)
    save(fig, "num_bisection.png")


def fig_newton() -> None:
    def f(x):
        return x**2 - 2

    def fp(x):
        return 2 * x

    x0 = 1.8
    x1 = x0 - f(x0) / fp(x0)
    xs = np.linspace(0.6, 2.4, 400)
    fig, ax = plt.subplots(figsize=(6.2, 3.8))
    ax.axhline(0, color="#888", lw=0.8)
    ax.plot(xs, f(xs), color=C_A, lw=2, label=r"$f(x)=x^2-2$")
    # tangent
    t = np.linspace(x0 - 0.5, x1 + 0.3, 50)
    ax.plot(t, f(x0) + fp(x0) * (t - x0), color=C_B, lw=1.6, label="tangent")
    ax.plot([x0, x0], [0, f(x0)], "--", color="#666", lw=1)
    ax.plot([x1, x1], [0, 0], "o", color=C_S, ms=7)
    ax.plot(x0, f(x0), "o", color=C_B, ms=6)
    ax.annotate(r"$x_k$", (x0, -0.25), ha="center", color=C_B)
    ax.annotate(r"$x_{k+1}$", (x1, -0.25), ha="center", color=C_S)
    ax.set_xlabel(r"$x$")
    ax.set_ylabel(r"$f(x)$")
    ax.set_title("Newton: root of tangent")
    ax.legend(loc="upper left", fontsize=9)
    ax.set_ylim(-2.2, 4.0)
    save(fig, "num_newton.png")


def fig_trapezoid_simpson() -> None:
    def f(x):
        return np.exp(-x**2)

    a, b = 0.0, 1.5
    xs = np.linspace(a, b, 400)
    fig, axes = plt.subplots(1, 2, figsize=(8.8, 3.6), sharey=True)

    # trapezoid n=4
    ax = axes[0]
    n = 4
    nodes = np.linspace(a, b, n + 1)
    ax.plot(xs, f(xs), color=C_A, lw=2)
    for i in range(n):
        poly = Polygon(
            [[nodes[i], 0], [nodes[i], f(nodes[i])], [nodes[i + 1], f(nodes[i + 1])], [nodes[i + 1], 0]],
            closed=True,
            facecolor=C_B,
            edgecolor=C_B,
            alpha=0.25,
            lw=1,
        )
        ax.add_patch(poly)
        ax.plot([nodes[i], nodes[i + 1]], [f(nodes[i]), f(nodes[i + 1])], color=C_B, lw=1.4)
    ax.plot(nodes, f(nodes), "o", color=C_B, ms=5)
    ax.set_title("Composite trapezoid")
    ax.set_xlabel(r"$x$")
    ax.set_ylabel(r"$f(x)=e^{-x^2}$")

    # simpson one panel with parabolas n=4 (even)
    ax = axes[1]
    ax.plot(xs, f(xs), color=C_A, lw=2)
    for i in range(0, n, 2):
        xx = np.linspace(nodes[i], nodes[i + 2], 80)
        # unique parabola through 3 points
        A = np.vstack([nodes[i : i + 3] ** 2, nodes[i : i + 3], np.ones(3)]).T
        coef = np.linalg.solve(A, f(nodes[i : i + 3]))
        yy = coef[0] * xx**2 + coef[1] * xx + coef[2]
        ax.fill_between(xx, 0, yy, color=C_S, alpha=0.25)
        ax.plot(xx, yy, color=C_S, lw=1.4)
    ax.plot(nodes, f(nodes), "o", color=C_S, ms=5)
    ax.set_title("Composite Simpson")
    ax.set_xlabel(r"$x$")

    fig.suptitle(r"Quadrature of $\int e^{-x^2}\,dx$", y=1.02)
    save(fig, "num_quadrature.png")


def fig_interpolation_runge() -> None:
    def f(x):
        return 1 / (1 + 25 * x**2)

    xs = np.linspace(-1, 1, 500)
    fig, axes = plt.subplots(1, 2, figsize=(8.8, 3.6), sharey=True)
    for ax, n, title in zip(axes, [6, 12], ["$n=6$ equispaced", "$n=12$ equispaced"]):
        nodes = np.linspace(-1, 1, n + 1)
        # Lagrange via polyfit (OK for demo)
        coef = np.polyfit(nodes, f(nodes), n)
        ax.plot(xs, f(xs), color=C_A, lw=2, label=r"$1/(1+25x^2)$")
        ax.plot(xs, np.polyval(coef, xs), color=C_B, lw=1.6, label="Lagrange")
        ax.plot(nodes, f(nodes), "o", color=C_S, ms=5)
        ax.set_title(title)
        ax.set_xlabel(r"$x$")
        ax.set_ylim(-0.5, 1.3)
        ax.legend(fontsize=8, loc="upper right")
    axes[0].set_ylabel(r"$y$")
    fig.suptitle("Runge phenomenon", y=1.02)
    save(fig, "num_runge.png")


def fig_euler_rk() -> None:
    # y' = -y, y(0)=1 → e^{-t}
    t_end = 4.0
    h = 0.5
    t = np.arange(0, t_end + 1e-12, h)
    # Euler
    y_e = np.zeros_like(t)
    y_e[0] = 1.0
    for i in range(len(t) - 1):
        y_e[i + 1] = y_e[i] + h * (-y_e[i])
    # RK4
    y_r = np.zeros_like(t)
    y_r[0] = 1.0
    for i in range(len(t) - 1):
        yi, ti = y_r[i], t[i]

        def f(tt, yy):
            return -yy

        k1 = f(ti, yi)
        k2 = f(ti + 0.5 * h, yi + 0.5 * h * k1)
        k3 = f(ti + 0.5 * h, yi + 0.5 * h * k2)
        k4 = f(ti + h, yi + h * k3)
        y_r[i + 1] = yi + (h / 6) * (k1 + 2 * k2 + 2 * k3 + k4)
    tt = np.linspace(0, t_end, 400)
    fig, ax = plt.subplots(figsize=(6.4, 3.8))
    ax.plot(tt, np.exp(-tt), "k-", lw=2, label=r"$e^{-t}$")
    ax.plot(t, y_e, "o--", color=C_B, lw=1.4, ms=6, label=rf"Euler $h={h}$")
    ax.plot(t, y_r, "s--", color=C_A, lw=1.4, ms=6, label=rf"RK4 $h={h}$")
    ax.set_xlabel(r"$t$")
    ax.set_ylabel(r"$y(t)$")
    ax.set_title(r"IVP $y'=-y$, $y(0)=1$")
    ax.legend(fontsize=9)
    save(fig, "num_ode_methods.png")


def main() -> None:
    fig_bisection()
    fig_newton()
    fig_trapezoid_simpson()
    fig_interpolation_runge()
    fig_euler_rk()


if __name__ == "__main__":
    main()
