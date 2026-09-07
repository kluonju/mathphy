#!/usr/bin/env python3
"""Generate vector-figure assets for lecture_notes chapter 2.

Outputs are written to ../figures with fixed filenames:
- vec_sum_diff.png
- vec_dot_product.png
- vec_cross_product.png
- vec_water_bond_angle.png
"""

from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Arc, Polygon, Rectangle, Circle

FIG_DIR = Path(__file__).resolve().parent.parent / "figures"
FIG_DIR.mkdir(parents=True, exist_ok=True)

PAPER = "#fdfcf9"
INK = "#151515"
AUX = "#666666"


def _setup_style(sketch=(0.5, 50.0, 1.0)):
    plt.rcParams.update(
        {
            "font.family": "DejaVu Sans",
            "font.size": 12,
            "text.color": "#111111",
            "path.sketch": sketch,
        }
    )


def _pen_arrow(ax, p0, p1, lw=2.8, ms=21, color=INK, style="->"):
    ax.annotate(
        "",
        xy=p1,
        xytext=p0,
        arrowprops=dict(
            arrowstyle=style,
            lw=lw,
            color=color,
            mutation_scale=ms,
            capstyle="round",
            joinstyle="round",
        ),
        zorder=5,
    )


def gen_sum_diff():
    _setup_style()
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(8.2, 3.8), facecolor=PAPER)
    for ax in (ax1, ax2):
        ax.set_facecolor(PAPER)
        ax.set_xlim(-0.3, 3.2)
        ax.set_ylim(-0.3, 2.4)
        ax.set_aspect("equal")
        ax.axis("off")

    O = np.array([0.0, 0.0])
    A = np.array([1.2, 1.8])
    B = np.array([2.2, 0.8])

    # (a) Addition by parallelogram
    ax1.add_patch(
        Polygon([O, A, A + B, B], closed=True, facecolor="#eceae2", edgecolor="none", hatch="///", zorder=1)
    )
    _pen_arrow(ax1, O, A)
    _pen_arrow(ax1, O, B)
    _pen_arrow(ax1, A, A + B, lw=2.1, ms=18, color=AUX)
    _pen_arrow(ax1, B, A + B, lw=2.1, ms=18, color=AUX)
    _pen_arrow(ax1, O, A + B, lw=3.0, ms=22)
    bbox = dict(facecolor=PAPER, edgecolor="none", pad=0.25)
    ax1.text(0.50, 1.02, r"$\mathbf{A}$", bbox=bbox)
    ax1.text(1.22, 0.25, r"$\mathbf{B}$", bbox=bbox)
    ax1.text(1.62, 1.40, r"$\mathbf{A}+\mathbf{B}$", bbox=bbox)
    ax1.text(0.05, 2.08, "(a)", color=AUX)

    # (b) Subtraction by head-to-tail
    C = np.array([2.4, 1.8])
    D = np.array([1.0, 0.4])
    ax2.add_patch(
        Polygon([O, C, D], closed=True, facecolor="#eceae2", edgecolor="none", hatch="///", zorder=1)
    )
    _pen_arrow(ax2, O, C)
    _pen_arrow(ax2, O, D)
    _pen_arrow(ax2, D, C, lw=3.0, ms=22)
    ax2.text(1.18, 1.05, r"$\mathbf{A}$", bbox=bbox)
    ax2.text(0.34, 0.18, r"$\mathbf{B}$", bbox=bbox)
    ax2.text(1.62, 1.06, r"$\mathbf{A}-\mathbf{B}$", bbox=bbox)
    ax2.text(0.05, 2.08, "(b)", color=AUX)

    fig.tight_layout(pad=0.3)
    fig.savefig(FIG_DIR / "vec_sum_diff.png", dpi=240, bbox_inches="tight", facecolor=PAPER)
    plt.close(fig)


def gen_dot_product():
    _setup_style()
    fig, ax = plt.subplots(figsize=(5.8, 3.8), facecolor=PAPER)
    ax.set_facecolor(PAPER)
    ax.set_xlim(-0.4, 3.3)
    ax.set_ylim(-0.3, 2.5)
    ax.set_aspect("equal")
    ax.axis("off")

    O = np.array([0.0, 0.0])
    A = np.array([2.8, 0.7])
    B = np.array([1.5, 1.9])
    Ah = A / np.linalg.norm(A)
    proj_len = np.dot(B, Ah)
    P = proj_len * Ah

    _pen_arrow(ax, O, A)
    _pen_arrow(ax, O, B)
    ax.plot([B[0], P[0]], [B[1], P[1]], "--", color=AUX, lw=1.7, zorder=3)
    ax.scatter([P[0]], [P[1]], s=10, color=INK, zorder=6)

    # Right-angle marker
    d = 0.12
    n = np.array([-Ah[1], Ah[0]])
    corner = P + d * Ah
    ax.add_patch(
        Rectangle((corner[0], corner[1]), d, d, angle=np.degrees(np.arctan2(n[1], n[0])), fill=False, lw=1.4, edgecolor=INK)
    )

    a_theta = np.degrees(np.arctan2(A[1], A[0]))
    b_theta = np.degrees(np.arctan2(B[1], B[0]))
    ax.add_patch(Arc((0, 0), 1.2, 1.2, theta1=a_theta, theta2=b_theta, lw=1.7, color=INK, zorder=5))
    bbox = dict(facecolor=PAPER, edgecolor="none", pad=0.25)
    ax.text(1.38, 0.16, r"$\mathbf{A}$", bbox=bbox)
    ax.text(1.05, 1.06, r"$\mathbf{B}$", bbox=bbox)
    ax.text(P[0] + 0.08, P[1] + 0.30, r"$|\mathbf{B}|\cos\theta$", bbox=bbox)
    ax.text(0.78, 0.56, r"$\theta$", bbox=bbox)

    fig.tight_layout(pad=0.3)
    fig.savefig(FIG_DIR / "vec_dot_product.png", dpi=240, bbox_inches="tight", facecolor=PAPER)
    plt.close(fig)


def gen_cross_product():
    _setup_style()
    fig, ax = plt.subplots(figsize=(5.8, 3.8), facecolor=PAPER)
    ax.set_facecolor(PAPER)
    ax.set_xlim(-0.4, 3.3)
    ax.set_ylim(-0.3, 2.5)
    ax.set_aspect("equal")
    ax.axis("off")

    O = np.array([0.0, 0.0])
    A = np.array([2.4, 0.8])
    B = np.array([1.0, 1.9])

    ax.add_patch(Polygon([O, A, A + B, B], closed=True, facecolor="#eceae2", edgecolor="none", hatch="////", zorder=1))
    _pen_arrow(ax, O, A)
    _pen_arrow(ax, O, B)
    _pen_arrow(ax, O, np.array([0.0, 2.3]), lw=3.0, ms=22)

    bbox = dict(facecolor=PAPER, edgecolor="none", pad=0.25)
    ax.text(1.20, 0.28, r"$\mathbf{A}$", bbox=bbox)
    ax.text(0.32, 1.00, r"$\mathbf{B}$", bbox=bbox)
    ax.text(0.10, 2.12, r"$\mathbf{A}\times\mathbf{B}$", bbox=bbox)

    fig.tight_layout(pad=0.3)
    fig.savefig(FIG_DIR / "vec_cross_product.png", dpi=240, bbox_inches="tight", facecolor=PAPER)
    plt.close(fig)


def gen_water_bond():
    # Keep the stronger sketch used in this session's hand-drawn variant.
    _setup_style(sketch=(1.2, 120.0, 2.0))

    fig, ax = plt.subplots(figsize=(6.1, 3.8), facecolor=PAPER)
    ax.set_facecolor(PAPER)
    ax.set_xlim(-2.7, 3.45)
    ax.set_ylim(-0.95, 2.85)
    ax.axis("off")

    O = np.array([0.0, 0.0])
    H1 = np.array([1.85, 1.40])
    H2 = np.array([-1.85, 1.40])

    _pen_arrow(ax, O, H1, lw=3.0, ms=21)
    _pen_arrow(ax, O, H2, lw=3.0, ms=21)

    ax.add_patch(Circle((O[0], O[1]), radius=0.085, facecolor="#5d7a60", edgecolor=INK, lw=1.0, zorder=6))
    ax.add_patch(Circle((H1[0], H1[1]), radius=0.07, facecolor="#f1d9bc", edgecolor=INK, lw=0.9, zorder=6))
    ax.add_patch(Circle((H2[0], H2[1]), radius=0.07, facecolor="#f1d9bc", edgecolor=INK, lw=0.9, zorder=6))

    bbox = dict(boxstyle="round,pad=0.14", facecolor=PAPER, edgecolor="none", alpha=0.98)
    ax.text(H1[0] + 0.07, H1[1] + 0.09, r"${\\rm H}_1$", fontsize=11, bbox=bbox)
    ax.text(H2[0] - 0.44, H2[1] + 0.09, r"${\\rm H}_2$", fontsize=11, bbox=bbox)
    ax.text(O[0] + 0.08, O[1] - 0.25, r"${\\rm O}$", fontsize=11, bbox=bbox)

    # Labels offset from the vectors via perpendicular displacement.
    u_vec = H1 - O
    v_vec = H2 - O
    u_mid = O + 0.62 * u_vec
    v_mid = O + 0.62 * v_vec
    u_perp = np.array([-u_vec[1], u_vec[0]])
    v_perp = np.array([v_vec[1], -v_vec[0]])
    u_perp = u_perp / np.linalg.norm(u_perp)
    v_perp = v_perp / np.linalg.norm(v_perp)
    u_pos = u_mid + 0.42 * u_perp + np.array([0.06, 0.06])
    v_pos = v_mid + 0.42 * v_perp + np.array([-0.06, 0.06])
    ax.text(u_pos[0], u_pos[1], r"$\\mathbf{u}$", fontsize=12, bbox=bbox)
    ax.text(v_pos[0], v_pos[1], r"$\\mathbf{v}$", fontsize=12, bbox=bbox)

    a1 = np.degrees(np.arctan2(H1[1], H1[0]))
    a2 = np.degrees(np.arctan2(H2[1], H2[0]))
    theta1, theta2 = sorted([a1, a2])
    arc_r = 0.50
    ax.add_patch(Arc((0, 0), width=2 * arc_r, height=2 * arc_r, theta1=theta1, theta2=theta2, lw=1.8, color=INK, zorder=5))

    mid = np.radians((theta1 + theta2) / 2.0)
    alpha_pos = np.array([0.60 * np.cos(mid), 0.60 * np.sin(mid) + 0.02])
    ax.text(alpha_pos[0], alpha_pos[1], r"$\\alpha$", ha="center", va="center", fontsize=12, bbox=bbox)
    ax.text(alpha_pos[0] + 0.28, alpha_pos[1] + 0.10, r"$\\approx 104.5^\\circ$", fontsize=10.5, color=AUX, bbox=bbox)

    ax.text(1.18, 2.00, r"$(0.757,\\,0,\\,0.586)$", color=AUX, fontsize=10.5, bbox=bbox)
    ax.text(-2.58, 2.00, r"$(-0.757,\\,0,\\,0.586)$", color=AUX, fontsize=10.5, bbox=bbox)

    fig.tight_layout(pad=0.3)
    fig.savefig(FIG_DIR / "vec_water_bond_angle.png", dpi=240, bbox_inches="tight", facecolor=PAPER)
    plt.close(fig)


def main():
    gen_sum_diff()
    gen_dot_product()
    gen_cross_product()
    gen_water_bond()
    print(f"Wrote figures to {FIG_DIR}")


if __name__ == "__main__":
    main()
