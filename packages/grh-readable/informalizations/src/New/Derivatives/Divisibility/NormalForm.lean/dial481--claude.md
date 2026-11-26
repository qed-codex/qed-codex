---
{
  "module": "src/New/Derivatives/Divisibility/NormalForm.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Derivatives/Divisibility/NormalForm.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Derivatives/Divisibility/NormalForm.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Couplings and the normal form

* `New.coupling`, `New.couplingSum`, `New.HasNormalForm`: the couplings `Γ_e` and the normal form
  `F(ϖ z) = W exp (c_ϖ Ξ)` with `W` integral, `c_ϖ = ϖ ^ (p + 1) / p` and
  `Ξ = ∑_{e ∈ S} ∑_j λ_{e j} Γ_e ^ p ^ j`, for any rule that assigns partners to places.
* `New.HasNormalForm.rescale`: the normal form is kept, with other numbers `λ_{e j}`, under
  `z ↦ α z` with `α` integral; so its existence depends only on the valuation of `ϖ`
  (`New.HasNormalForm.exists_of_norm_eq`).
* `New.HasNormalForm.norm_coeff_subst_le_one`: if `F` has the normal form and `Z` is integral
  without constant term, then `F(ϖ Z)` is integral in degrees at most `B` if the couplings `Γ_e(Z)`
  with `e ∈ S`, `e ≤ log_p B` are divisible by some `π` with `‖c_ϖ π‖ ≤ p ^ (-1 / (p - 1))`.
* `New.HasNormalForm.of_dvd_sub`: it is enough to know the exponent modulo such a `π`.
* `New.dvd_pderiv_couplingSum_sub`: the derivatives of `Ξ` modulo `p`, if `0 ∉ S`. They are not
  needed for the divisibility bound, only for its sharpness.

## Notation

* `valRingCp p` is the valuation ring `𝒪` of `ℂ_[p]`; a series over it is called integral.
* `seriesToCp W` is the series `W` over `𝒪`, seen as a series over `ℂ_[p]`.
* `expSubst g` is the series `exp g`, for `g` without constant term.
* The variables `z_x` are indexed by pairs `x = (τ, i)` in `Φ × c`, for finite types `Φ` and `c`;
  the elements `τ` of `Φ` are called places.


### `coupling`

 The coupling `Γ_e = ∑ z_(τ,i) ^ p ^ e * z_(τ',i)`, summed over all `(τ, i) : Φ × c`, where
`τ' = pr e τ` is the partner of `τ`. 

### `couplingSum`

 The series `Ξ = ∑_{e ∈ S} ∑_j λ_{e j} Γ_e ^ p ^ j`, where `λ_{e j} = l e j` and `Γ_e` is the
coupling for the partner rule `pr`. 

### `HasNormalForm`

 `F` has the normal form with the given numbers `ϖ` and `λ_{e j} = l e j`:
`F(ϖ z) = W exp (c_ϖ ∑_{e ∈ S} ∑_j λ_{e j} Γ_e ^ p ^ j)` with `W` integral and
`c_ϖ = ϖ ^ (p + 1) / p`. 

### `subst_expSubst`

 A substitution `Z` that is allowed (`HasSubst Z`) commutes with the exponential:
`(exp g)(Z) = exp (g(Z))` if `g(0) = 0`. 

### `subst_coupling`

 The coupling after a substitution: `Γ_e(Z) = ∑ Z_(τ,i) ^ p ^ e * Z_(pr e τ, i)`. 

### `rescale_coupling`

 The coupling `Γ_e` is homogeneous of degree `p ^ e + 1`. 

### `le_order_coupling`

 The coupling `Γ_e` has order at least `p ^ e + 1`. 

### `hasSum_couplingSum`

 The sum `∑_{e ∈ S} ∑_j λ_{e j} Γ_e ^ p ^ j` that defines `couplingSum S pr l` converges, as the
orders of its terms tend to infinity. 

### `constantCoeff_couplingSum`

 The series `couplingSum S pr l = ∑_{e ∈ S} ∑_j λ_{e j} Γ_e ^ p ^ j` has no constant term. 

### `hasSum_subst_couplingSum`

 A substitution of series `Z_x` without constant term into
`couplingSum S pr l = ∑_{e ∈ S} ∑_j λ_{e j} Γ_e ^ p ^ j`, where `λ_{e j} = l e j` and
`Γ_e = coupling pr e`, may be carried out term by term. 

### `rescale_couplingSum`

 Let `Ξ = couplingSum S pr l` be the series `∑_{e ∈ S} ∑_j λ_{e j} Γ_e ^ p ^ j`. As `Γ_e` is
homogeneous of degree `p ^ e + 1`, the series `Ξ(α z)` is the same sum with `λ_{e j}` multiplied by
`α ^ ((p ^ e + 1) p ^ j)`. 

### `norm_coeff_expSubst_smul_le_one`

 If `‖a π‖ ≤ p ^ (-1 / (p - 1))` and the integral series `G` has no constant term and
coefficients divisible by `π` in degrees at most `B`, then `exp (a G)` is integral in these
degrees. 

### `HasNormalForm.of_dvd_sub`

 To prove that `F` has the normal form `F(ϖ z) = W exp (c_ϖ Ξ₀)`, where `W` is integral,
`c_ϖ = ϖ ^ (p + 1) / p` and `Ξ₀ = couplingSum S pr l`, it is enough to know the exponent modulo a
`π` with `‖c_ϖ π‖ ≤ p ^ (-1 / (p - 1))`: it suffices that `F(ϖ z) = W exp (c_ϖ Ξ)` with `W`, `Ξ`
integral, `Ξ(0) = 0` and `Ξ ≡ Ξ₀` modulo `π`. 

### `HasNormalForm.exists_subst_eq_mul_expSubst`

 Let `F` have the normal form `F(ϖ z) = W exp (c_ϖ ∑_{e ∈ S} ∑_j λ_{e j} Γ_e ^ p ^ j)` with `W`
integral. If the series `Z_x` are integral without constant term, then `F(ϖ Z)` is an integral
series times `exp (c_ϖ ∑_{e ∈ S} ∑_j λ_{e j} Γ_e(Z) ^ p ^ j)`. 

### `HasNormalForm.rescale`

 Let `F` have the normal form `F(ϖ z) = W exp (c_ϖ ∑_{e ∈ S} ∑_j λ_{e j} Γ_e ^ p ^ j)` with `W`
integral. Then, for integral `α`, the series `F(α z)` has the normal form with the same `ϖ` and with
`λ_{e j}` multiplied by `α ^ ((p ^ e + 1) p ^ j)`. 

### `HasNormalForm.exists_of_norm_eq`

 Let `F` have the normal form `F(ϖ z) = W exp (c_ϖ ∑_{e ∈ S} ∑_j λ_{e j} Γ_e ^ p ^ j)` with `W`
integral. The existence of such a form depends only on the valuation of `ϖ`: if `ϖ ≠ 0` and
`‖ϖ'‖ = ‖ϖ‖`, then `F` has it for `ϖ'`, with other numbers `λ'_{e j} = l' e j` in place of the
`λ_{e j}`. 

### `le_order_subst_coupling_pow`

 Let `Γ_e = coupling pr e` be the coupling `∑ z_(τ,i) ^ p ^ e * z_(pr e τ, i)`, homogeneous of
degree `p ^ e + 1`. A substitution of series `Z_x` without constant term does not lower orders, so
`Γ_e(Z) ^ p ^ j` has order at least `p ^ e + 1`. 

### `dvd_coeff_subst_couplingSum`

 Let `Ξ = couplingSum S pr l` be the series `∑_{e ∈ S} ∑_j λ_{e j} Γ_e ^ p ^ j`. If the series
`Z_x` have no constant term and `π` divides `Γ_e(Z)` for all `e ∈ S` with `e ≤ log_p B`, then `π`
divides the coefficients of `Ξ(Z)` in degrees at most `B`. 

### `HasNormalForm.norm_coeff_subst_le_one`

 Let `F` have the normal form `F(ϖ z) = W exp (c_ϖ ∑_{e ∈ S} ∑_j λ_{e j} Γ_e ^ p ^ j)`. Let
`‖c_ϖ π‖ ≤ p ^ (-1 / (p - 1))`, and let the series `Z_x` be integral without constant term, with `π`
dividing `Γ_e(Z)` for all `e ∈ S` with `e ≤ log_p B`. Then the coefficients of `F(ϖ Z)` in degrees
at most `B` have norm at most `1`. 

### `partnerPowerSum`

 The sum of the powers `z_x ^ p ^ e` over the `x = (τ, i)` whose partner `(pr e τ, i)` in the
coupling `Γ_e` is `y`. 

### `dvd_pderiv_pow_pow`

 The derivatives of a `p ^ e`-th power vanish modulo `p`, for `e > 0`. 

### `dvd_pderiv_coupling_sub`

 For `e > 0`, only the linear factors of the coupling
`Γ_e = coupling pr e = ∑_{(τ, i)} z_(τ,i) ^ p ^ e * z_(pr e τ, i)` have a derivative modulo `p`:
`∂Γ_e / ∂z_y` is congruent to `partnerPowerSum pr e y`, the sum of the `z_x ^ p ^ e` over the
`x = (τ, i)` whose partner `(pr e τ, i)` is `y`. 

### `coeff_partnerPowerSum_self`

 If `y` is the partner of `x` for `e`, then `z_x ^ p ^ e` has coefficient `1` in
`partnerPowerSum pr e y`. 

### `exists_single_of_coeff_partnerPowerSum_ne_zero`

 The only monomials of `partnerPowerSum pr e y` are the `z_x ^ p ^ e` with `y` the partner of
`x` for `e`. 

### `le_order_partnerPowerSum`

 The series `partnerPowerSum pr e y` has order at least `p ^ e`. 

### `summable_smul_partnerPowerSum`

 The sum `∑_{e ∈ S} λ_{e 0} * partnerPowerSum pr e y`, where `λ_{e 0} = l e 0` and
`partnerPowerSum pr e y` is the sum of the `z_x ^ p ^ e` over the `x = (τ, i)` with partner
`(pr e τ, i) = y`, converges, as the term `e` has order at least `p ^ e`. 

### `dvd_pderiv_couplingSum_sub`

 Let `Ξ = couplingSum S pr l` be the series `∑_{e ∈ S} ∑_j λ_{e j} Γ_e ^ p ^ j`. If `0 ∉ S`, then
modulo `p` only the linear factors in the terms `j = 0` count in the derivatives:
`∂Ξ / ∂z_y ≡ ∑_{e ∈ S} λ_{e 0} * partnerPowerSum pr e y`. 

### `residue_coeff_pderiv_couplingSum_eq`

 Let `Ξ = couplingSum S pr l` be the series `∑_{e ∈ S} ∑_j λ_{e j} Γ_e ^ p ^ j`. If `0 ∉ S`, then
modulo the maximal ideal of `valRingCp p` the coefficients of `∂Ξ / ∂z_y` are those of
`∑_{e ∈ S} λ_{e 0} * partnerPowerSum pr e y`. 

### `residue_coeff_pderiv_couplingSum`

 Let `Ξ = couplingSum S pr l` be the series `∑_{e ∈ S} ∑_j λ_{e j} Γ_e ^ p ^ j`. Let `0 ∉ S` and
`e ∈ S`, and let `y = (pr e τ, i)` be the partner of `x = (τ, i)` for `e`. Modulo the maximal ideal
of `valRingCp p`, the coefficient of the one monomial `z_x ^ p ^ e` in `∂Ξ / ∂z_y` is `λ_{e 0}`. 

### `exists_eq_single_of_residue_coeff_pderiv_ne_zero`

 Let `Ξ = couplingSum S pr l` be the series `∑_{e ∈ S} ∑_j λ_{e j} Γ_e ^ p ^ j`. If `0 ∉ S`, then
modulo the maximal ideal of `𝒪 = valRingCp p` the series `∂Ξ / ∂z_y` has only monomials
`z_x ^ p ^ e` with `e ∈ S` and `y = (pr e τ, i)` the partner of `x = (τ, i)` for `e`. 
