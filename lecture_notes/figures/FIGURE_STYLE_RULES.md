# Figure Generation Rules (Final Reproducible Spec)

This file is the single source of truth for regenerating the vector figures in this chapter.

## 1) Scope and Target Files
- Apply these rules to:
	- `vec_sum_diff.png`
	- `vec_dot_product.png`
	- `vec_cross_product.png`
	- `vec_water_bond_angle.png`
- Keep filenames unchanged so LaTeX links remain valid.

## 2) Final Visual Style
- Style: clean hand-drawn technical sketch.
- No decorative background scribble lines.
- Use monochrome linework with light gray fills/hatching where needed.
- Background color: `#fdfcf9`.
- Main ink color: `#151515`.
- Auxiliary color (axes/construction/dashed): `#666666`.

## 3) Global Matplotlib Settings
- Use:
	- `font.family = DejaVu Sans`
	- `font.size = 12`
	- `text.color = #111111`
	- `path.sketch = (0.5, 50, 1.0)`
- Rationale: preserves hand-drawn feel but reduces vector wiggle.

## 4) Geometry and Stroke Rules
- Keep vector geometry mathematically correct (straight segment intent).
- Main vector arrows:
	- `arrowstyle='->'`
	- `lw` around `2.6` to `2.9`
	- `mutation_scale` around `20` to `22`
	- `capstyle='round'`, `joinstyle='round'`
- Auxiliary axes and guides:
	- thinner (`lw` around `1.2` to `2.1`)
	- dashed for projection guides.

## 5) Fill and Shading Consistency
- If one subpanel in a figure uses shading, all comparable subpanels must use shading.
- In `vec_sum_diff.png`, both panel (a) and panel (b) are shaded/hatched.
- Recommended hatch: `'///'` or `'////'`.

## 6) Label Typography (Slim)
- Labels should not look heavy.
- Use slimmer text than earlier versions:
	- vector labels and symbols: `fontweight='semibold'` or `normal`
	- avoid heavy/bold-black oversized labels.
- Typical sizes:
	- vector names (`A`, `B`, `u`, `v`): ~20
	- compound labels (`A + B`, `B - A`, `A × B`, `|B|cosθ`): ~20 to 22
	- axis symbols (`x`, `z`) and angle symbols (`θ`, `α`): ~18 to 20.

## 7) Label Placement Rules (Mandatory)
- Labels must not overlap:
	- vector lines,
	- dashed guides,
	- hatching,
	- points/nodes,
	- other labels.
- Place labels in nearby whitespace with clear visual gap.
- Use a light text background patch to guarantee readability:
	- `bbox=dict(facecolor=PAPER, edgecolor='none', pad≈0.30)`.

## 8) Angle Arc Rules
- Angle arcs must remain visible (draw above relevant strokes when necessary).
- `θ` and `α` should be placed near the angle bisector region, but not covering the arc stroke.
- For the dot-product figure, `θ` should be farther from the vertex than initial drafts (expanded radial offset).

## 9) Projection and Right-Angle Marker (Dot Product)
- Keep the dashed perpendicular from the tip of `B` to the projection foot on `A`.
- Include a right-angle rectangle marker at the projection foot.
- Keep projection foot dot small and unobtrusive.

## 10) Node/Point Sizes
- Projection dot: very small (`s` around `10`).
- Hydrogen nodes in water-angle figure: moderate (`s` around `70`).
- Origin node in water-angle figure: moderate (`s` around `95`).

## 11) Figure-Specific Constraints
- `vec_sum_diff.png`
	- panel labels `(a)` and `(b)` must not collide.
	- `A + B` and `B - A` labels must be off the vector strokes.
- `vec_dot_product.png`
	- `B` label stays away from slanted `B` arrow.
	- `θ` sits away from angle vertex.
	- right-angle rectangle marker is required.
- `vec_cross_product.png`
	- `A × B` label in clear upper region.
- `vec_water_bond_angle.png`
	- `u` and `v` labels must not sit on vectors.
	- `α` label should not block arc.

## 12) Export Rules
- Output format: PNG.
- DPI: `240`.
- Save with `bbox_inches='tight'` and `facecolor=PAPER`.

## 13) Reproducibility Checklist
- Same rcParams and palette applied before plotting.
- Same filename outputs used.
- No new decorative lines introduced.
- All label overlap constraints pass visual check.
- If any overlap appears, adjust label coordinates only; do not change concept geometry.
