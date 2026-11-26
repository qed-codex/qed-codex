---
{
  "module": "src/Lib/General/Analysis/GaussianIntegral.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/General/Analysis/GaussianIntegral.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/General/Analysis/GaussianIntegral.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Matrix norm estimates, the Ostrowski–Taussky inequality, and the complex Gaussian integral

This file proves estimates for complex matrices and computes the complex Gaussian integral on
`ι → ℂ`. Here `‖A‖` is the `ℓ²` operator norm. For accretive `A`, the integral of
`exp (-x* A (x - a))` against normalised Lebesgue measure is `(det A)⁻¹`.

## Main definitions and results

* `New.norm_apply_le_l2_opNorm`, `New.l2_opNorm_le_of_apply`: the operator norm bounds the entries,
  and for an `m × n` matrix it is at most `|m| |n|` times a bound for the entries.
* `New.ostrowski_taussky`: the Ostrowski–Taussky inequality, in the form
  `|det H| ≤ 2 ^ card n |det Θ|` when `0 ≤ H ≤ Θ + Θᴴ`.
* `Matrix.IsAccretive`: the matrices `A` with `A + Aᴴ` positive definite. Positive definite matrices
  are accretive (`Matrix.PosDef.isAccretive`), and accretive matrices have nonzero determinant
  (`Matrix.IsAccretive.det_ne_zero`).
* `New.Fock.normalizedVolume`: Lebesgue measure divided by `π ^ card ι`, so that `exp (-|x|²)` has
  integral `1`.
* `New.Fock.map_mulVec_addHaar_eq_smul`, `New.lintegral_eq_norm_det_sq_mul_lintegral_mulVec`: the
  change of variables by an invertible complex matrix `u`, whose real Jacobian is `‖det u‖ ^ 2`.
* `New.Fock.integral_gauss`: if `A` is accretive, the integral of `exp (-x* A (x - a))` is
  `(det A)⁻¹`.

## Relation to the literature

The Ostrowski–Taussky inequality and the complex Gaussian integral are known results.


 ## Operator norm, matrix entries and the Ostrowski–Taussky inequality 

### `l2_opNorm_le_of_apply`

 If all entries of an `m × n` complex matrix `A` have norm at most `M`, then the `ℓ²` operator
norm of `A` is at most `|m| |n| M`. 

### `one_le_re_of_mem_roots_charpoly_inv_mul`

 If `H` is positive definite and `Θ + Θᴴ - H` is positive semidefinite, then every eigenvalue
`l` of `H⁻¹ (Θ + Θ)` has real part at least `1`. 

### `ostrowski_taussky`

 Ostrowski–Taussky inequality: if `H` and `Θ + Θᴴ - H` are positive semidefinite complex matrices
indexed by `n`, then `|det H| ≤ 2 ^ card n |det Θ|`. 

 ## Accretive matrices, normalised measure on `ι → ℂ` and the complex Gaussian integral 

### `Matrix.IsAccretive`

 A complex square matrix `A` is (strictly) accretive if `A + Aᴴ` is positive definite. 

### `normalizedVolume`

 Lebesgue measure on `ι → ℂ` divided by `π ^ card ι`. 

### `map_mulVec_addHaar_eq_smul`

 The image of an additive Haar measure `μ` on `ι → ℂ` under an invertible complex matrix `u` is
`|det u|⁻² μ`. 

### `_root_.New.lintegral_eq_norm_det_sq_mul_lintegral_mulVec`

 Change of variables on `ι → ℂ`: for a complex square matrix `u` with `det u ≠ 0` and any
`g : (ι → ℂ) → [0, ∞]`, one has `∫ g(y) dy = |det u|² ∫ g(u y) dy` (lower Lebesgue integrals). 

### `norm_sq_le_re_star_dotProduct_self`

 The square of the sup norm of `x : ι → ℂ` is at most `x* x = ∑ |x i|²`. 

### `exists_eq_conjTranspose_mul_diagonal_mul`

 An accretive matrix `A` (that is, `A + Aᴴ` is positive definite) is congruent to a diagonal
matrix whose entries have positive real part. 

### `integral_cexp_neg_star_mul`

 The complex Gaussian integral in one variable: if `0 < re d`, then `exp (-z̄ d (z - a))` has
integral `π / d` over `ℂ`. 

### `integral_gauss`

 The complex Gaussian integral: if `A` is accretive (that is, `A + Aᴴ` is positive definite),
then `exp (-x* A (x - a))` has integral `(det A)⁻¹` for `normalizedVolume ι`, Lebesgue measure on
`ι → ℂ` divided by `π ^ card ι`. 
