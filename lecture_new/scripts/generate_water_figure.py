#!/usr/bin/env python3
"""Regenerate only the water bond-angle figure used in chapter 2."""

from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Arc, Circle

out = Path(__file__).resolve().parent.parent / "figures" / "vec_water_bond_angle.png"
out.parent.mkdir(parents=True, exist_ok=True)

plt.rcParams.update(
    {
        "font.family": "DejaVu Sans",
        "font.size": 12,
        "font.weight": "normal",
        "axes.edgecolor": "#222222",
        "text.color": "#111111",
        "path.sketch": (1.2, 120.0, 2.0),
    }
)

PAPER = "#fcfbf7"
INK = "#181818"
AUX = "#6b6b6b"
ACCENT = "#5d7a60"

fig, ax = plt.subplots(figsize=(6.1, 3.8), facecolor=PAPER)
ax.set_facecolor(PAPER)
ax.set_xlim(-2.7, 3.45)
ax.set_ylim(-0.95, 2.85)
ax.axis("off")

O = np.array([0.0, 0.0])
H1 = np.array([1.85, 1.40])
H2 = np.array([-1.85, 1.40])


def pen_arrow(p0, p1, lw=2.8, ms=20, color=INK):
    ax.annotate(
        "",
        xy=p1,
        xytext=p0,
        arrowprops=dict(arrowstyle="-|>", lw=lw, color=color, shrinkA=0, shrinkB=0, mutation_scale=ms),
        zorder=4,
    )


pen_arrow(O, H1, lw=3.0, ms=21)
pen_arrow(O, H2, lw=3.0, ms=21)

ax.add_patch(Circle((O[0], O[1]), radius=0.085, facecolor=ACCENT, edgecolor=INK, lw=1.0, zorder=6))
ax.add_patch(Circle((H1[0], H1[1]), radius=0.07, facecolor="#f1d9bc", edgecolor=INK, lw=0.9, zorder=6))
ax.add_patch(Circle((H2[0], H2[1]), radius=0.07, facecolor="#f1d9bc", edgecolor=INK, lw=0.9, zorder=6))

bbox = dict(boxstyle="round,pad=0.14", facecolor=PAPER, edgecolor="none", alpha=0.98)
ax.text(H1[0] + 0.07, H1[1] + 0.09, r"${\rm H}_1$", fontsize=11, bbox=bbox)
ax.text(H2[0] - 0.44, H2[1] + 0.09, r"${\rm H}_2$", fontsize=11, bbox=bbox)
ax.text(O[0] + 0.08, O[1] - 0.25, r"${\rm O}$", fontsize=11, bbox=bbox)

# Keep labels close to lines but not on them.
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
ax.text(u_pos[0], u_pos[1], r"$\mathbf{u}$", fontsize=12, bbox=bbox)
ax.text(v_pos[0], v_pos[1], r"$\mathbf{v}$", fontsize=12, bbox=bbox)

a1 = np.degrees(np.arctan2(H1[1], H1[0]))
a2 = np.degrees(np.arctan2(H2[1], H2[0]))
theta1, theta2 = sorted([a1, a2])
arc_r = 0.50
arc = Arc((0, 0), width=2 * arc_r, height=2 * arc_r, theta1=theta1, theta2=theta2, lw=1.8, color=INK, zorder=5)
ax.add_patch(arc)

mid = np.radians((theta1 + theta2) / 2.0)
alpha_pos = np.array([0.60 * np.cos(mid), 0.60 * np.sin(mid) + 0.02])
ax.text(alpha_pos[0], alpha_pos[1], r"$\alpha$", ha="center", va="center", fontsize=12, bbox=bbox)
ax.text(alpha_pos[0] + 0.28, alpha_pos[1] + 0.10, r"$\approx 104.5^\circ$", fontsize=10.5, color=AUX, bbox=bbox)

ax.text(1.18, 2.00, r"$(0.757,\,0,\,0.586)$", color=AUX, fontsize=10.5, bbox=bbox)
ax.text(-2.58, 2.00, r"$(-0.757,\,0,\,0.586)$", color=AUX, fontsize=10.5, bbox=bbox)

fig.tight_layout(pad=0.3)
fig.savefig(out, dpi=240, bbox_inches="tight", facecolor=PAPER)
plt.close(fig)
print(f"Wrote {out}")
