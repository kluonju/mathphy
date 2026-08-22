#!/usr/bin/env python3
"""Generate key pedagogical figures for concise-math-physics."""
from __future__ import annotations

import os
from pathlib import Path

import numpy as np

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib import patches
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401

ROOT = Path(__file__).resolve().parent.parent
FIG = ROOT / "src" / "figures"
FIG.mkdir(parents=True, exist_ok=True)

# Clean, print-friendly style
plt.rcParams.update(
    {
        "font.size": 11,
        "axes.grid": True,
        "grid.alpha": 0.25,
        "figure.dpi": 140,
        "savefig.bbox": "tight",
        "axes.unicode_minus": False,
    }
)


def save(fig: plt.Figure, name: str) -> None:
    out = FIG / name
    fig.savefig(out, dpi=140)
    plt.close(fig)
    print("Saved", out.relative_to(ROOT))


def fig_delta_limit() -> None:
    x = np.linspace(-3, 3, 800)
    fig, ax = plt.subplots(figsize=(7.2, 4.0))
    for eps, c in zip([0.8, 0.35, 0.12], ["#4C78A8", "#F58518", "#E45756"]):
        g = np.exp(-(x**2) / (2 * eps**2)) / (np.sqrt(2 * np.pi) * eps)
        ax.plot(x, g, color=c, lw=2, label=rf"$\sigma={eps}$")
    ax.set_xlabel(r"$x$")
    ax.set_ylabel(r"$f_\sigma(x)$")
    ax.set_title(r"Gaussian sequence approaching $\delta(x)$")
    ax.legend()
    ax.set_ylim(0, None)
    save(fig, "delta_gaussian_limit.png")


def fig_delta_lorentz() -> None:
    x = np.linspace(-4, 4, 800)
    fig, ax = plt.subplots(figsize=(7.2, 4.0))
    for eps, c in zip([0.6, 0.25, 0.08], ["#54A24B", "#B279A2", "#E45756"]):
        g = (1 / np.pi) * eps / (eps**2 + x**2)
        ax.plot(x, g, color=c, lw=2, label=rf"$\varepsilon={eps}$")
    ax.set_xlabel(r"$x$")
    ax.set_ylabel(r"$\frac{1}{\pi}\frac{\varepsilon}{\varepsilon^2+x^2}$")
    ax.set_title(r"Lorentzian sequence approaching $\delta(x)$")
    ax.legend()
    save(fig, "delta_lorentz_limit.png")


def fig_gibbs_square() -> None:
    x = np.linspace(-np.pi, np.pi, 1200)
    f = np.sign(np.sin(x))
    fig, axes = plt.subplots(2, 2, figsize=(8.5, 6.2), sharex=True, sharey=True)
    for ax, N in zip(axes.flat, [1, 3, 7, 31]):
        s = sum((4 / (n * np.pi)) * np.sin(n * x) for n in range(1, N + 1, 2))
        ax.plot(x, f, "k--", lw=1.2, label="square wave")
        ax.plot(x, s, color="#4C78A8", lw=1.8, label=f"N={N}")
        ax.set_title(f"Odd harmonics up to n={N}")
        ax.set_ylim(-1.4, 1.4)
        ax.legend(loc="lower right", fontsize=8)
    fig.suptitle("Fourier series of a square wave (Gibbs phenomenon)", y=1.01)
    fig.tight_layout()
    save(fig, "fourier_gibbs_square.png")


def fig_ft_pairs() -> None:
    x = np.linspace(-6, 6, 800)
    k = np.linspace(-6, 6, 800)
    # rect <-> sinc, gaussian <-> gaussian
    fig, axes = plt.subplots(2, 2, figsize=(8.5, 5.8))
    a = 1.5
    rect = np.where(np.abs(x) <= a, 1.0, 0.0)
    sinc = 2 * a * np.sinc(k * a / np.pi)  # np.sinc = sin(pi x)/(pi x)
    axes[0, 0].plot(x, rect, color="#4C78A8", lw=2)
    axes[0, 0].set_title(r"$f(x)=\mathrm{rect}$")
    axes[0, 1].plot(k, sinc, color="#F58518", lw=2)
    axes[0, 1].set_title(r"$\tilde f(k)\propto\mathrm{sinc}$")
    sig = 0.8
    g = np.exp(-(x**2) / (2 * sig**2))
    gk = sig * np.sqrt(2 * np.pi) * np.exp(-(sig**2) * k**2 / 2)
    axes[1, 0].plot(x, g, color="#54A24B", lw=2)
    axes[1, 0].set_title(r"Gaussian $f(x)$")
    axes[1, 1].plot(k, gk, color="#E45756", lw=2)
    axes[1, 1].set_title(r"Gaussian $\tilde f(k)$ (wider$\leftrightarrow$narrower)")
    for ax in axes.flat:
        ax.set_xlabel(r"$x$ or $k$")
    fig.suptitle("Fourier transform pairs (schematic)", y=1.01)
    fig.tight_layout()
    save(fig, "fourier_transform_pairs.png")


def fig_lagrange_contours() -> None:
    # Contour of f = -x^2 - 4 y^2 with constraint x - y + 4 = 0
    xs = np.linspace(-1, 6, 300)
    ys = np.linspace(-2, 3, 300)
    X, Y = np.meshgrid(xs, ys)
    F = -(X**2) - 4 * Y**2
    fig, ax = plt.subplots(figsize=(6.8, 5.2))
    cs = ax.contour(X, Y, F, levels=12, cmap="viridis")
    ax.clabel(cs, inline=True, fontsize=8, fmt="%.0f")
    # constraint line: y = x + 4
    xc = np.linspace(-1, 6, 200)
    yc = xc - 4  # wait: x - y + 4 = 0 => y = x + 4
    yc = xc + 4
    # Actually constraint x - y + 4 = 0 => y = x + 4
    # But that is above - for visible region use x - y - something
    # PX286: x - y + 4 = 0 => y = x + 4. Point (3.2, 0.8): 3.2 - 0.8 + 4 = 6.4 ≠ 0
    # Recheck: "x - y + 4 = 0" and point (3.2, 0.8): 3.2-0.8+4=6.4. Wrong.
    # Perhaps x - 4y or constraint x/ something.
    # From Lagrange for f=-x^2-4y^2, c=x-y+4:
    # ∇f = (-2x, -8y), ∇c=(1,-1)
    # -2x = λ, -8y = -λ => 2x = 8y => x=4y
    # x - y + 4 = 0 => 4y - y + 4 = 0 => 3y=-4 => y=-4/3, x=-16/3
    # PDF said (3.2, 0.8) - maybe different constraint. Use our consistent solution.
    # Use constraint x - y - 1 = 0 for nicer point in first quadrant with max of -x^2-4y^2
    # Maximize f=-x^2-4y^2 on x-y=0? Let's use c = x + 4y - 1 or stick to PDF geometry intent:
    # density plot with constraint line crossing contours where gradients align.

    # Use f = -x^2 - 4y^2, c = x - 4y + 0? 
    # ∇f=(-2x,-8y)=λ(1,-4) => -2x=λ, -8y=-4λ => 2x=2λ? -8y=-4λ => 2y=λ= -2x => y=-x
    # Better: recreate PDF figure intent with f=-x^2-4y^2, c=x-y+1=0
    # ∇f=λ∇c: -2x=λ, -8y=-λ => 2x=8y => x=4y; x-y+1=0 => 4y-y+1=0 => y=-1/3, x=-4/3

    # For a nicer plot in positive region use f = x^2 + 4 y^2 minimize on x+y=1
    # Or stick with maximizing -x^2-4y^2 on line x-y+4=0 (even if point is outside [0,1])

    ax.clear()
    xs = np.linspace(-6, 2, 300)
    ys = np.linspace(-3, 2, 300)
    X, Y = np.meshgrid(xs, ys)
    F = -(X**2) - 4 * (Y**2)
    cs = ax.contour(X, Y, F, levels=14, cmap="viridis")
    ax.clabel(cs, inline=True, fontsize=7, fmt="%.0f")
    xc = np.linspace(-6, 2, 200)
    yc = xc + 4  # c = x - y + 4 = 0
    # clip to axes
    mask = (yc >= -3) & (yc <= 2)
    ax.plot(xc[mask], yc[mask], color="#E45756", lw=2.5, label=r"$x-y+4=0$")
    # critical point: x=4y, x-y+4=0 => 4y-y+4=0 => y=-4/3, x=-16/3
    px, py = -16 / 3, -4 / 3
    ax.plot([px], [py], "o", color="#E45756", ms=9, zorder=5)
    # gradient arrows at critical point
    # ∇f = (-2x, -8y), ∇c = (1, -1)
    gf = np.array([-2 * px, -8 * py])
    gc = np.array([1.0, -1.0])
    gf = 0.35 * gf / np.linalg.norm(gf)
    gc = 0.9 * gc / np.linalg.norm(gc)
    ax.annotate(
        "",
        xy=(px + gf[0], py + gf[1]),
        xytext=(px, py),
        arrowprops=dict(arrowstyle="->", color="#4C78A8", lw=2),
    )
    ax.annotate(
        "",
        xy=(px + gc[0], py + gc[1]),
        xytext=(px, py),
        arrowprops=dict(arrowstyle="->", color="#F58518", lw=2),
    )
    ax.text(px + gf[0], py + gf[1] + 0.15, r"$\nabla f$", color="#4C78A8")
    ax.text(px + gc[0] + 0.1, py + gc[1], r"$\nabla c$", color="#F58518")
    ax.set_xlabel(r"$x$")
    ax.set_ylabel(r"$y$")
    ax.set_title(r"Lagrange: $\nabla f \parallel \nabla c$ on the constraint")
    ax.legend(loc="upper right")
    ax.set_aspect("equal", adjustable="box")
    save(fig, "lagrange_contour_constraint.png")


def fig_morse_surfaces() -> None:
    fig = plt.figure(figsize=(10, 3.6))
    titles = [
        (r"$x^2+y^2$ (min)", lambda X, Y: X**2 + Y**2, "#4C78A8"),
        (r"$x^2-y^2$ (saddle)", lambda X, Y: X**2 - Y**2, "#F58518"),
        (r"$-x^2-y^2$ (max)", lambda X, Y: -(X**2) - Y**2, "#54A24B"),
    ]
    u = np.linspace(-1.2, 1.2, 60)
    X, Y = np.meshgrid(u, u)
    for i, (title, fun, _c) in enumerate(titles):
        ax = fig.add_subplot(1, 3, i + 1, projection="3d")
        Z = fun(X, Y)
        ax.plot_surface(X, Y, Z, cmap="viridis", alpha=0.92, linewidth=0, antialiased=True)
        ax.set_title(title, fontsize=10)
        ax.set_xticks([])
        ax.set_yticks([])
        ax.set_zticks([])
    fig.suptitle("Nondegenerate critical points (Morse normal forms)", y=1.02)
    fig.tight_layout()
    save(fig, "lagrange_morse_surfaces.png")


def fig_complex_plane() -> None:
    fig, ax = plt.subplots(figsize=(5.5, 5.2))
    ax.axhline(0, color="k", lw=0.8)
    ax.axvline(0, color="k", lw=0.8)
    z1 = 2 + 1.2j
    z2 = 1 + 2j
    zs = z1 + z2
    ax.annotate("", xy=(z1.real, z1.imag), xytext=(0, 0), arrowprops=dict(arrowstyle="->", color="#4C78A8", lw=2))
    ax.annotate("", xy=(zs.real, zs.imag), xytext=(z1.real, z1.imag), arrowprops=dict(arrowstyle="->", color="#F58518", lw=2))
    ax.annotate("", xy=(zs.real, zs.imag), xytext=(0, 0), arrowprops=dict(arrowstyle="->", color="#E45756", lw=2.2))
    ax.plot([0, z1.real, zs.real, z2.real, 0], [0, z1.imag, zs.imag, z2.imag, 0], "--", color="0.6", lw=1)
    ax.text(z1.real + 0.1, z1.imag, r"$z_1$", color="#4C78A8")
    ax.text(z2.real - 0.5, z2.imag + 0.1, r"$z_2$", color="#F58518")
    ax.text(zs.real + 0.1, zs.imag, r"$z_1+z_2$", color="#E45756")
    # polar for z1
    ax.add_patch(patches.Arc((0, 0), 1.2, 1.2, theta1=0, theta2=np.degrees(np.angle(z1)), color="#54A24B", lw=1.5))
    ax.text(0.7, 0.15, r"$\arg z_1$", color="#54A24B")
    ax.set_xlim(-0.5, 4)
    ax.set_ylim(-0.5, 4)
    ax.set_aspect("equal")
    ax.set_xlabel(r"$\mathrm{Re}\,z$")
    ax.set_ylabel(r"$\mathrm{Im}\,z$")
    ax.set_title("Complex plane: addition of $z_1$ and $z_2$")
    save(fig, "complex_plane_addition.png")


def fig_spherical_coords() -> None:
    fig = plt.figure(figsize=(6.2, 5.5))
    ax = fig.add_subplot(111, projection="3d")
    # sphere wire
    u = np.linspace(0, np.pi, 40)
    v = np.linspace(0, 2 * np.pi, 60)
    x = np.outer(np.sin(u), np.cos(v))
    y = np.outer(np.sin(u), np.sin(v))
    z = np.outer(np.cos(u), np.ones_like(v))
    ax.plot_surface(x, y, z, color="#4C78A8", alpha=0.15, linewidth=0)
    # radius vector
    th, ph = np.deg2rad(55), np.deg2rad(40)
    r = 1.0
    P = np.array([r * np.sin(th) * np.cos(ph), r * np.sin(th) * np.sin(ph), r * np.cos(th)])
    ax.plot([0, P[0]], [0, P[1]], [0, P[2]], color="#E45756", lw=2.5)
    ax.scatter(*P, color="#E45756", s=40)
    # xy projection for phi
    ax.plot([0, P[0]], [0, P[1]], [0, 0], "--", color="#F58518", lw=1.5)
    ax.plot([P[0], P[0]], [P[1], P[1]], [0, P[2]], ":", color="0.4")
    ax.text(P[0] * 1.05, P[1] * 1.05, P[2] * 1.05, r"$\mathbf{r}$", color="#E45756")
    ax.text(0.35, 0.05, 0.0, r"$\varphi$", color="#F58518")
    ax.text(0.1, 0.1, 0.55, r"$\theta$", color="#54A24B")
    ax.set_xlim(-1, 1)
    ax.set_ylim(-1, 1)
    ax.set_zlim(-1, 1)
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_zlabel("z")
    ax.set_title("Spherical coordinates $(r,\\theta,\\varphi)$")
    save(fig, "coords_spherical.png")


def main() -> None:
    fig_delta_limit()
    fig_delta_lorentz()
    fig_gibbs_square()
    fig_ft_pairs()
    fig_lagrange_contours()
    fig_morse_surfaces()
    fig_complex_plane()
    # Coordinate-system figures: use scripts/generate_coord_systems.py (TikZ)
    print("Done. Figures in", FIG)


if __name__ == "__main__":
    main()
