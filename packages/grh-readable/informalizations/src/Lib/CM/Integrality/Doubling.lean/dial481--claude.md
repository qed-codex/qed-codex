---
{
  "module": "src/Lib/CM/Integrality/Doubling.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/CM/Integrality/Doubling.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/CM/Integrality/Doubling.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Doubling formulas for θ and σ and the quartic forms of doubling

The file expresses `θ(2 z)` and `σ(2 z) ^ 2` in `θ(z)` and `σ(z)`. The quartic forms of doubling,
`doublingForms c`, are defined over any commutative ring; over `ℂ` with `c = a₁`, their values at
`(θ², σ²)` are the square of the formula for `θ(2 z)` and the formula for `σ(2 z) ^ 2`. These facts
serve to prove the cases of the theorem on Siegel units (integrality and units at torsion points)
that are used; see `Lib.CM.Integrality.TorsionValues` and `Lib.CM.Integrality.IntegralSections`.

Notions from other files:
* `C : CMLattice d`: a lattice `Λ = C.Λ` in `ℂ` with a point `t = C.t` of order two modulo `Λ`,
  scaled so that `℘''(t) = 2`, and a square root `a₁ = C.a₁` of `12 ℘(t)`.
* `C.σ`, `C.θ`: the sigma function of `Λ`, and its twisted translate by `t` normalised to `1` at
  `0`; the zeros of `θ` are the `z` with `z + t ∈ Λ`.
* `C.translatedX`: the function `x(z) = ℘(z + t) - ℘(t)`, equal to `σ² / θ²` off `t + Λ`.
* `C.twistedTranslate m y`: the translation `T_y` by `y`, twisted by the exponential factor of
  degree `m`.

## Main definitions and results

* `New.doublingForms c`: the pair of quartic forms of doubling.
* `New.CMLattice.sigma_two_mul_eq`: `σ(2 z) = x' θ ^ 4` off `t + Λ`.
* `New.CMLattice.theta_two_mul`, `New.CMLattice.sigma_two_mul_sq`: `θ(2 z)` and `σ(2 z) ^ 2` as
  polynomials in `θ` and `σ`.
* `New.norm_doublingForms`: if `c` is integral and `c ^ 4 - 64` is a unit, the forms raise the
  maximum norm of a pair to the fourth power.
* `New.norm_det_eq_one_of_iterate_doublingForms`: a criterion for two pairs to reduce to distinct
  points of the projective line over the residue field.

## Relation to the literature

Known result: the duplication formulas for theta and sigma functions. Source: DLMF, Chapters 20 and
23.

Known result: good reduction of the duplication map on the `x`-coordinate of an elliptic curve.
Source: Silverman, *The Arithmetic of Dynamical Systems* (GTM 241, Springer, 2007), Chapters 2 and
6.



## Doubling formulas for θ and σ

The formula `θ(2 z) = θ ^ 4 - σ ^ 4` is the addition formula for `θ` on the diagonal. The formula
`σ(2 z) = x' θ ^ 4` is the duplication formula of `σ` at `z + t`; it uses that the number
`c₀ = (T_t σ)(0)` is a fourth root of unity.


### `isIsogeny_two`

 Multiplication by `2` is an isogeny of degree `4` from the lattice of `C` to itself: it maps
`Λ` into `Λ`, and `2 * conj 2 = 4`. 

### `twistedTranslate_t_sigma_zero_ne_zero`

 For a CM lattice with point `t` of order two, the number `c₀ = (T_t σ)(0)` is nonzero. 

### `sigma_add_t`

 The identity `T_t σ = c₀ θ` with `c₀ = (T_t σ)(0)`, with the exponential factor of the twisted
translation `T_t` written out. 

### `theta_add_t`

 The identity `c₀ T_t θ = -σ` with `c₀ = (T_t σ)(0)`, with the exponential factor of the twisted
translation `T_t` written out. 

### `twistedTranslate_t_sigma_zero_pow_four`

 For a CM lattice `C` with point `t` of order two, the number `c₀ = (T_t σ)(0)` is a fourth root
of unity: `c₀ ^ 4 = 1`. Here `T_t` is the twisted translation of degree `1` by `t`, so
`c₀ = exp(−π |t|² / (2A)) σ(t)`, where `A` is the area of `Λ`. 

### `theta_two_mul`

 Doubling for the normalised twisted translate `θ` of the sigma function `σ` of `C`:
`θ(2 z) = θ(z) ^ 4 - σ(z) ^ 4`. 

### `sigma_two_mul_eq`

 Doubling for the sigma function `σ` of `C`: `σ(2 z) = x'(z) θ(z) ^ 4` away from the poles
`t + Λ` of `x(z) = ℘(z + t) - ℘(t)`, where `θ` is the normalised twisted translate of `σ` by `t`. 

### `sigma_two_mul_sq`

 Doubling for the sigma function `σ` of `C`, in terms of `σ` and its normalised twisted translate
`θ` by `t`: `σ(2 z)² = θ² σ² (4 θ ^ 4 + a₁² θ² σ² + 4 σ ^ 4)` at `z`. 


## The quartic forms of doubling over ℂ_p

If `c` is integral and `c ^ 4 - 64` is a unit, the two forms have no nontrivial common zero over
the residue field of `ℂ_p`.


### `doublingForms`

 The pair of quartic forms `B₀ = (w₀² - w₁²)²` and `B₁ = w₀ w₁ (4 w₀² + c² w₀ w₁ + 4 w₁²)` at
`w = (w₀, w₁)`. 

### `doublingForms_smul`

 The forms `doublingForms c` are homogeneous of degree `4`. 

### `iterate_doublingForms_smul`

 The `j`-th iterate of `doublingForms c` is homogeneous of degree `4 ^ j`. 

### `map_doublingForms`

 The forms `doublingForms` commute with ring homomorphisms. 

### `map_iterate_doublingForms`

 The iterates of `doublingForms` commute with ring homomorphisms. 

### `eq_zero_of_doublingForms_eq_zero`

 Over a field with `c ^ 4 ≠ 64`, the two quartic forms `doublingForms c` have no common zero
other than `0`. 

### `exists_eq_smul_of_det_eq_zero`

 Over a field, if the determinant of the pairs `w`, `w'` vanishes and `w' ≠ 0`, then `w` is a
multiple of `w'`. 

### `map_residue_eq_zero_iff`

 A pair over the valuation ring `valRingCp p` of `ℂ_p` reduces to `0` over the residue field if
and only if its maximum norm in `ℂ_p × ℂ_p` is less than one. 

### `exists_eq_map_subtype`

 A pair in `ℂ_p × ℂ_p` of maximum norm at most one comes from a pair over the valuation ring. 

### `norm_map_subtype_le_one`

 A pair over the valuation ring of `ℂ_p` has maximum norm at most one. 

### `norm_map_subtype_eq_one_iff_map_residue_ne_zero`

 A pair over the valuation ring of `ℂ_p` has maximum norm `1` in `ℂ_p × ℂ_p` if and only if its
reduction to the residue field is nonzero. 

### `norm_doublingForms_eq_one`

 If `c ∈ ℂ_p` is integral and `c ^ 4 - 64` is a unit, the quartic forms `doublingForms c` take
pairs of maximum norm `1` to pairs of maximum norm `1`. 

### `norm_doublingForms`

 If `c ∈ ℂ_p` is integral and `c ^ 4 - 64` is a unit, the quartic forms `doublingForms c` raise
the maximum norm of a pair to the fourth power. 

### `norm_det_eq_one_of_iterate_doublingForms`

 Let `c ∈ ℂ_p` be integral and let `w`, `w'` be pairs of maximum norm `1`. Let `doublingForms c`
send `(w₀, w₁)` to `((w₀² - w₁²)², w₀ w₁ (4 w₀² + c² w₀ w₁ + 4 w₁²))`. If `j` applications of this
map take `w` to a pair `(0, *)` of norm `1` and `w'` to a pair `(*, 0)`, then `w` and `w'` reduce to
distinct points of the projective line over the residue field, that is, their determinant
`w.1 w'.2 - w.2 w'.1` is a unit. 
