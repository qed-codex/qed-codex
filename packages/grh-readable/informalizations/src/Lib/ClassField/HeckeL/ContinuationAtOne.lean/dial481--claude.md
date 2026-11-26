---
{
  "module": "src/Lib/ClassField/HeckeL/ContinuationAtOne.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/ClassField/HeckeL/ContinuationAtOne.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/ClassField/HeckeL/ContinuationAtOne.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Analyticity at 1 of L-functions of nontrivial Hecke characters

This file proves that partial Hecke `L`-functions `New.eulerProd (heckeCoeff ψ S)` of nontrivial
characters extend analytically to `s = 1`. Here `ψ` satisfies `New.IsHeckeOfType ψ n`, `S` is a
finite set of primes, and only real `s ≥ 1` is treated. The file combines the theta-sum estimate
of `Lib.ClassField.HeckeL.IdelicThetaSum` with the finite-place half of Tate's thesis. This yields
three results: analyticity at `1`, a prime density statement and, for `ψ ^ 2 ≠ 1`, nonvanishing
on `[1, ∞)`. Valuations are multiplicative: `v x ≤ 1` means integral.

## Main definitions and results

* `New.IsHeckeOfType.integral_mul_finIdeleAbs_rpow_eq_eulerProd_mul`: the integral of `f ψ |·| ^ s`
  over the finite ideles is the partial `L`-function of `ψ` times a volume;
  `New.IsHeckeOfType.tate_integral` adds that this volume is nonzero.
* `New.IsHeckeOfType.exists_analyticAt_one_eulerProd`: for `ψ ≠ 1` the partial `L`-function extends
  analytically to a neighbourhood of `1`.
* `New.IsHeckeOfType.exists_hasPrimeDensity`: for `ψ ≠ 1` the partial `L`-function is continuous on
  `[1, ∞)`, and the values of `ψ` have mean `-m` over the primes of degree one, for some natural
  number `m`.
* `New.IsHeckeOfType.eulerProd_ne_zero`: for `ψ ^ 2 ≠ 1` the partial `L`-function has no zero on
  `[1, ∞)`.

Notions from other files:
* `New.finIdeleAbs`: The module |x| of a finite idele x: the adelic absolute value of the idele with
  finite part x and component 1 at infinity. `New.ZetaIntegral.ideleModule`: the module of an idele.
* `New.Ô`: The subring Ô of finite adeles of K that are integral at every finite place.
  `New.ZetaIntegral.adelicTent r d`: a tent of radius `r` at `1` times the indicator of
  `d * (x - 1) ∈ Ô`.
* `New.eulerProd`: The Euler product `∏ (1 - a v * q ^ (-s))⁻¹` over the primes `v` of `K`, with
  `q = v.q` the norm of `v`, as a function of real `s > 1`; at `s = 1` it is the limit from the
  right, if that exists.
* `New.IsHeckeOfType ψ n`: the character `ψ` of the finite ideles is the finite part of a Hecke
  character of type `n`: its kernel is open and `ψ x * ∏_w (Φ_w x / |Φ_w x|) ^ (n w) = 1` on `Kˣ`.
* `New.heckeCoeff ψ S`: the function on finite places sending `v ∉ S` to the value of `ψ` at the
  local idele of the chosen uniformiser at `v`, and `v ∈ S` to `0`.

## Relation to the literature

Known result: Hecke L-functions with Euler product, continuation to s = 1, non-vanishing and prime
densities. Only real s is treated, and a non-trivial character of integral angular type is continued
to a neighbourhood of 1 from Tate's integral by a Riemann sum instead of Poisson summation.
Non-vanishing is proved only when the square of the character is non-trivial, and densities are
taken over primes of degree one, with bounded error. Source: J. Tate, Fourier analysis in number
fields and Hecke's zeta-functions, 1950, in Cassels–Fröhlich ch. XV, §4.4–4.5; J. Milne, Class Field
Theory, VI 4.8–4.9 (finite order); S. Lang, Algebraic Number Theory (non-vanishing); Titchmarsh,
Theory of the Riemann zeta-function, §2.11 (the Riemann-sum continuation is Müntz's formula over ℚ).


### `CharUnramifiedAt.apply_locIdele_eq_zpow`

 If `ψ` is unramified at `w`, its value at the local idele of `x` is its value at the uniformiser
raised to the order `-log (v x)` of `x`. 

### `measureReal_idelesUnitOff_empty_inter_ne_zero`

 For a Haar measure `μ` and an open set `V` containing `1`, the volume of `Ô^× ∩ V` is nonzero.
Here `Ô^× = idelesUnitOff ∅` is the group of unit ideles. 

### `_root_.MeasureTheory.integral_tsum_mul_indicator_mul_left_of_hasSum`

 Let `μ` be a left-invariant measure on a group `G`, and `W` a measurable set with
`μ.real W ≠ 0`. If `c` has sum `a` over a countable type `ι`, then for all `t : ι → G` the function
`x ↦ ∑' i, c i * W.indicator 1 (t i * x)` has integral `a * μ.real W`: every translate of the
indicator of `W` has integral `μ.real W`. 

### `mul_finIdeleAbs_rpow_locIdele_uniformizer_mul`

 Let `f` vanish unless `x` is integral outside `S` and a unit at `S`, let `f` take equal values
at integral ideles with the same components at `S`, and let `χ` take the value `heckeCoeff ψ S w` at
each prime `w`. Then multiplying an integral `x` by the uniformiser at `w` (keeping it integral)
multiplies `f x * ψ x * |x| ^ s` by `χ w * w.q ^ (-s)`. 

### `exists_eq_coeIdeal_of_count_nonneg`

 A nonzero fractional ideal `J` of `𝓞 K` whose exponent `count K w J` is nonnegative at every
prime `w` is an integral ideal. 

### `exists_divisor_eq_coeIdeal_of_supp`

 Let `K` be a number field and `d` a homomorphism from the finite ideles `(𝔸f K)ˣ` to the group
of nonzero fractional ideals of `𝓞 K`. Suppose that an idele `a` is integral at a finite place `w`
exactly when the exponent `count K w (d a)` of the prime `w` in `d a` is nonnegative. Let `S` be a
set of finite places and `x` an idele that is integral at each `w ∉ S` and a unit at each `w ∈ S`.
Then the fractional ideal `d x` is an ideal of `𝓞 K`. Here `a.val w` is the component of `a` in the
completion of `K` at `w`, and the valuation `Valued.v` is multiplicative: `≤ 1` means integral and
`= 1` means a unit. 

### `apply_principalIdele_mul_prod_eq_one`

 The defining identity of `IsHeckeOfType ψ n` at `x ∈ Kˣ`. 

### `norm_eq_one`

 Let `ψ` satisfy `IsHeckeOfType ψ n`: its kernel is open, and
`ψ x * ∏ w, (Φ w x / ‖Φ w x‖) ^ n w = 1` for `x ∈ Kˣ`. Then `ψ x` has absolute value one for
every finite idele `x`. 

### `pow`

 The `d`-th power of a Hecke character of type `n` is a Hecke character of type `d • n`. 

### `ne_one`

 Over a CM field, a Hecke character of nonzero type `n` is nontrivial. 

### `exists_monoidHom_asIdeal_eq_heckeCoeff`

 Let `ψ` satisfy `IsHeckeOfType ψ n`. The values `heckeCoeff ψ S` at the primes extend to a
completely multiplicative function `χ` on the ideals of `𝓞 K` with `χ ⊥ = 0` and `‖χ I‖ ≤ 1`. 

### `integral_mul_finIdeleAbs_rpow_eq_eulerProd_mul`

 Tate's zeta integral over the finite ideles. Let `ψ` be the finite part of a Hecke character of
type `n`, `μ` a Haar measure on the finite ideles, and `V ∋ 1` open. Let `f` be supported on the
ideles integral outside `S` and units at `S`, with `f ψ` the indicator of `V` on the unit ideles
`Ô^× = idelesUnitOff ∅`, and with `f` depending only on the components at `S` of integral ideles.
Then for real `s > 1` the function `f x * ψ x * |x| ^ s` is integrable, with integral
`eulerProd (heckeCoeff ψ S) s * μ (Ô^× ∩ V)`, where `|x| = finIdeleAbs x` and
`eulerProd (heckeCoeff ψ S) s` is the partial Euler product `∏_{v ∉ S} (1 - ψ(ϖ_v) q_v^(-s))⁻¹`,
with `ϖ_v` the chosen uniformiser and `q_v` the norm of `v`. 

### `tate_integral`

 Tate's zeta integral with the volume. Let `ψ` satisfy `IsHeckeOfType ψ n`, let `μ` be a Haar
measure on the finite ideles, and let `V` be an open set containing `1`. Let `f` satisfy three
conditions: it vanishes unless `x` is integral outside `S` and a unit at the places of `S`;
`f u * ψ u` is the indicator of `V` on the unit ideles `Ô^× = idelesUnitOff ∅`; and its value on
integral ideles depends only on their components at `S`. Then `μ (Ô^× ∩ V) ≠ 0`, and for every real
`s > 1` the function `f x * ψ x * |x| ^ s` is `μ`-integrable with integral
`eulerProd (heckeCoeff ψ S) s * μ (Ô^× ∩ V)`. 

### `exists_continuousAlgHom_mixedEmbedding_eq`

 The embedding `Φ w : K →+* ℂ` that `PlaceEmbedding K` chooses at the infinite place `w` extends
to a continuous `ℝ`-algebra map `p` on `K ⊗ ℝ = mixedEmbedding.mixedSpace K`:
`p (mixedEmbedding K x) = Φ w x` for `x : K`. 

### `exists_level`

 Let `ψ` satisfy `IsHeckeOfType ψ n`. There is a finite idele `d`, a level of `ψ`, such that
every idele `y` with `d * (y - 1) ∈ Ô K` is integral (`Ô K`: the finite adeles that are integral
everywhere) and, if `y` is a unit idele (`y ∈ idelesUnitOff ∅`), satisfies `ψ y = 1`. 

### `exists_idele_character`

 Let `ψ ≠ 1` be the finite part of a Hecke character of type `n` (`IsHeckeOfType ψ n`): its
kernel is open, and `ψ x * ∏ w, (Φ w x / ‖Φ w x‖) ^ n w = 1` for `x ∈ Kˣ`. Then `ψ` extends to a
homomorphism `X` to `ℂ` from the idele group `(K ⊗ ℝ)ˣ × (𝔸f K)ˣ` with four properties. `X` is
trivial on the principal ideles `principalIdeles K` (the diagonal image of `Kˣ`),
`X (t, a) = X (t, 1) * ψ a`, `X` is continuous in the infinite component, and `X c ≠ 1` for some
idele `c` with `ideleModule c = 1`. 

### `exists_radius_tent_integral_ne_zero`

 The zeta integral at infinity. Let `χ` be a continuous function on the units of `K ⊗ ℝ` (the
mixed space) with `χ 1 = 1`, and integrate `χ t * |t| ^ s` against the tent `max (ρ - dist t 1) 0`,
where `|t| = ideleModule (t, 1)` is the absolute value of the norm of `t`. There is `0 < r < 1` such
that for every `ρ ≤ r` the integrand is integrable for all real `s`, and for `0 < ρ ≤ r` the
integral does not vanish at `s = 1`. 

### `_root_.Valuation.map_eq_one_of_one_lt_of_mul_map_sub_one_le`

 Let `v` be a valuation and `a`, `x` elements with `1 < v a` and `v a * v (x - 1) ≤ 1`. Then
`v x = 1`, because the second hypothesis forces `v (x - 1) < 1`. 

### `_root_.Valuation.mul_map_sub_one_le_one_of_map_le_one`

 Let `v` be a valuation and `a`, `x` elements with `v a ≤ 1` and `v x ≤ 1`. Then
`v a * v (x - 1) ≤ 1`. 

### `exists_level_tate_integral`

 The zeta integral at the finite places. Let `ψ` be the finite part of a Hecke character of type
`n` (`IsHeckeOfType ψ n`). There are a level `d`, a finite set `T` of finite places and a constant
`κ ≠ 0` such that, for real `s > 1`, the function `ψ x * |x| ^ s` times the indicator
`adelicTent 1 d (1, x)` of `1 + d⁻¹ Ô` is integrable on the finite ideles, and its integral is `κ`
times the Euler product `eulerProd (heckeCoeff ψ T) s` over the places outside `T`. Here
`|x| = finIdeleAbs x` is the module of `x`. 

### `integral_tsum_adelicTent_eq_mul`

 Unfolding. Let `X` be a character of the ideles `a = (t, x)` (`t` at infinity, `x` at the
finite places) that is trivial on the principal ideles, and suppose that `X a` times the tent
`adelicTent ρ d a` times `|a| ^ s` is `A t * B x`, with `A` and `B` integrable. Here
`|a| = ideleModule a` is the module of `a`. Translate by an idele `g` of module one.
Then `X g * X a` times the theta sum `∑' γ, adelicTent ρ d (γ * g * a)` over the principal ideles
`γ` times `|a| ^ s` is integrable on the idele classes (the quotient of the Haar measure), with
integral `(∫ A) * ∫ B`. 

### `integral_tsum_adelicTent_eq_integral_mul`

 Unfolding for the tent of radius `ρ` at infinity and the level tent at the finite places. Let
`X` be trivial on the principal ideles with `X (t, x) = X (t, 1) * ψ x`, `g` of module one, and the
integrands at infinity and at the finite places integrable. Then `X g * X a` times the theta sum
`∑' γ, adelicTent ρ d (γ * g * a)` times `|a| ^ s` is integrable on the idele classes, and its
integral is the integral at infinity times the integral `I` at the finite places. 

### `_root_.MeasureTheory.hasFiniteIntegral_mul_sub_mul_rpow_of_abs_sub_le`

 Finite integral of a difference, for a Mellin-type integrand. Let `N > 0` and suppose that
`|θ₁ a - θ₂ a| ≤ C * N a ^ δ * (|φ₁ a| + |φ₂ a|)` for all `a`, and that `u * φ₁ * N ^ (σ + δ)` and
`u * φ₂ * N ^ (σ + δ)` are integrable. Then `u * (θ₁ - θ₂) * N ^ σ` has finite integral. 

### `_root_.abs_sub_le_mul_rpow_of_forall_exists_abs_sub_le`

 Comparison through a common approximation. Suppose that for every `l > 0` some number `i` is
within `C * l ^ δ * |φ b|` of `θ b` for all `b` with `N b = l`. If `0 < N a` and `N b = N a`, then
`|θ a - θ b| ≤ C * N a ^ δ * (|φ a| + |φ b|)`. 

### `exists_analyticAt_one_mul_eulerProd`

 Let `ψ ≠ 1` be the finite part of a Hecke character of type `n` (`IsHeckeOfType ψ n`). There
are a finite set `T` of finite places and functions `F G : ℝ → ℂ`, both analytic at `1`, with
`G 1 ≠ 0` and `F s = G s * eulerProd (heckeCoeff ψ T) s` for real `s > 1`, where
`eulerProd (heckeCoeff ψ T)` is the Euler product of `ψ` over the places outside `T`. 

### `exists_analyticAt_one_eulerProd`

 Hecke's theorem at `s = 1`: let `ψ ≠ 1` be the finite part of a Hecke character of type `n`
(`IsHeckeOfType ψ n`) and `S` a finite set of finite places. Some function `F` of a real variable,
analytic at `1`, agrees with the partial `L`-function `eulerProd (heckeCoeff ψ S)` at all real
`s > 1` near `1`. 

### `continuousOn_eulerProd`

 Let `ψ ≠ 1` be the finite part of a Hecke character of type `n` (`IsHeckeOfType ψ n`: `ψ` has
open kernel and `ψ x * ∏ w, (Φ w x / ‖Φ w x‖) ^ n w = 1` for `x ∈ Kˣ`), and let `S` be a finite set
of finite places. The partial `L`-function `eulerProd (heckeCoeff ψ S)` is the Euler product
`∏ (1 - ψ(ϖ_v) * q_v ^ (-s))⁻¹` over `v ∉ S`, with `ϖ_v = uniformizer v`; its value at each `s ≥ 1`
is the limit of the product as `s' → s` with `s' > 1`. This function is continuous on `s ≥ 1`. 

### `exists_hasPrimeDensity_neg_natCast`

 Let `ψ ≠ 1` be the finite part of a Hecke character of type `n` (`IsHeckeOfType ψ n`), and let
`S` be a finite set of finite places. For some natural number `m`, the coefficients `heckeCoeff ψ S`
(the values of `ψ` at uniformisers) have mean `-m` over the primes of degree one outside `S`
(`HasPrimeDensity`: for `s → 1⁺`, `∑ heckeCoeff ψ S v * q ^ (-s) = -m * log (1 / (s - 1)) + O(1)`).
If `m = 0`, the partial `L`-function `eulerProd (heckeCoeff ψ S)` has no zero on real `s ≥ 1`, where
its value at `s = 1` is the limit of the Euler product as `s → 1⁺`. In the proof, `m` is the order
of vanishing at `1` of a function analytic at `1` that agrees with the `L`-function for `s > 1` near
`1`. 

### `exists_hasPrimeDensity`

 Let `ψ ≠ 1` be the finite part of a Hecke character of type `n` (`IsHeckeOfType ψ n`) and `S` a
finite set of finite places. The partial `L`-function `eulerProd (heckeCoeff ψ S)` is continuous on
`s ≥ 1`, and for some natural number `m` the values of `ψ` at the primes of degree one outside `S`
have mean `-m` (`HasPrimeDensity`), with no zero of the `L`-function on `s ≥ 1` if `m = 0`. 

### `eulerProd_ne_zero`

 Let `ψ` be the finite part of a Hecke character of type `n` (`IsHeckeOfType ψ n`) with
`ψ ^ 2 ≠ 1`, and let `S` be a finite set of finite places. The partial `L`-function
`eulerProd (heckeCoeff ψ S)` has no zero at real `s ≥ 1`, where its value at `s = 1` is the limit of
the Euler product as `s → 1⁺`.

A special case of the non-vanishing of Hecke L-functions. Only real s is covered, and ψ² ≠ 1 is
assumed even for s > 1. 
