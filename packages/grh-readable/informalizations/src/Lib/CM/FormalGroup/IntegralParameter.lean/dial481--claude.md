---
{
  "module": "src/Lib/CM/FormalGroup/IntegralParameter.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/CM/FormalGroup/IntegralParameter.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/CM/FormalGroup/IntegralParameter.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Integral series rings 𝔬[[T]], congruence parts of power series, a functional equation

Let `𝔬` (`New.valRingCp p`) be the valuation ring of `ℂ_[p]`, and let `𝔬[[X]]` be the range of the
inclusion `New.seriesToCp` into `ℂ_[p]⟦X⟧`. For a series `T = X + ⋯`, the file studies the ring
`𝔬[[T]]` of integral series in `T`. For the coordinate `y` of a CM curve, it shows that `𝔬[[y]]`
contains `x` and is stable under `d/dz`. It then treats the part of a series in the degrees of one
class mod `m`, and the integrality of the solutions of a functional equation `Y(π z) = π G(Y)`.

## Main definitions and results

* `New.IsSeriesGenerator A T`: the series `T = X + ⋯` generates `A`, that is, `A = 𝔬[[T]]`. Such a
  ring is closed under integral scalars. It is closed under `f ↦ f(a X)` when it contains `T(a X)`.
  Its elements whose constant term has norm `1` are invertible. Any series `f = X + ⋯` in `A`
  generates it too (`New.IsSeriesGenerator.of_mem`).
* `New.CMLattice.integralSeriesRing C`: the ring `𝔬[[y]]`. Here `y` (`New.CMLattice.translatedY`)
  and `x` (`New.CMLattice.translatedX`) are the coordinates of the CM curve `y² + a₁ x y = x³ + x`.
  `New.taylorVia ιₚ f` is the Taylor series of `f` at `0` with the p-adic place `ιₚ : ℂ →+* ℂ_[p]`
  applied to the coefficients.
* `New.CMLattice.taylorVia_translatedX_mem_integralSeriesRing`,
  `New.CMLattice.derivative_mem_integralSeriesRing`: `𝔬[[y]]` contains `x` and is stable under
  `d/dz`.
* `New.congruencePart_eq_sum`: for `m ≠ 0`, the part of a series in the degrees of one class mod `m`
  is a mean over the `m`-th roots of unity; `New.congruencePart_subst`: taking it commutes with the
  substitution of a series `T` with `T(0) = 0` that has only degrees `≡ 1` mod `m`.
* `New.exists_seriesToCp_eq_of_rescale_eq`: for `0 < |π| < 1`, `q > 1` and `E` integral of order at
  least two, a solution `Y = z + ⋯` of `Y(π z) / π = Y - Y ^ q + π E(Y)` is integral, by induction
  on the degree (`New.mem_range_seriesToCp_of_rescale_eq_X_sub_X_pow`), and `Y - Y ^ q ≡ z` modulo
  `π` (`New.C_dvd_sub_pow_sub_X_of_rescale_eq`).
* `New.dvd_coeff_sub_of_C_dvd_sub_pow_sub_X`: let `π` be a non-unit dividing `p` and `q > 1` a power
  of `p`. If `Y(0) = 0` and `Y - Y ^ q ≡ z` modulo `π`, then `Y ≡ ∑ z ^ q ^ j` modulo `π`.

Notions from other files:
* `New.CMLattice d`: a lattice `Λ` stable under the integers of `ℚ(√-d)`, with a point `t` of order
  two modulo `Λ` such that `ω t`, `ω̄ t ∉ Λ` for `ω = (1 + √-d) / 2`, scaled so that `℘''(t) = 2`,
  and a square root `a₁` of `12 ℘(t)`.
* `New.PrimeSevenModEight d`: the number `d` is a prime congruent to `7` modulo `8`.

## Relation to the literature

Known result: elementary facts on power series; the induction is that of the functional equation of
a Lubin–Tate group. Source: Lubin–Tate, Formal complex multiplication in local fields.

The statements on the CM curve use only that `a₁` is integral; `x ∈ 𝔬[[y]]` is Hensel's lemma for
the cubic.


 ## Rings of integral series in a generating parameter 

### `IsSeriesGenerator`

 The series `T = X + ⋯` generates the subring `A` of `ℂ_[p]⟦X⟧`: `A = 𝔬[[T]]` consists exactly
of the `g(T)` with `g` a series over the valuation ring `𝔬` of `ℂ_[p]`. 

### `IsSeriesGenerator.constantCoeff_eq_zero`

 The constant term of `T` is `0`. 

### `IsSeriesGenerator.coeff_one`

 The linear coefficient of `T` is `1`. 

### `IsSeriesGenerator.mem_iff`

 The elements of `A` are the series `g(T)` with `g` integral. 

### `constantCoeff_subst_eq`

 The series `f(T)` and `f` have the same constant term, if `T(0) = 0`. 

### `coeff_one_subst`

 The linear coefficient of `f(T)` is the product of those of `f` and `T`, if `T(0) = 0`. 

### `rescale_subst`

 Substituting `a X` in `f(T)` gives `f(T(a X))`, if `T(0) = 0`. 

### `subst_seriesToCp_subst`

 For integral series `F`, `G` and a series `T` with `F(0) = T(0) = 0`, the composite `G ∘ F`
formed over `𝔬` satisfies `(G ∘ F)(T) = G(F(T))`. 

### `continuous_subst`

 If `T` may be substituted into series, the substitution `f ↦ f(T)` is continuous for the
topology of coefficientwise convergence. 

 ### Properties of `𝔬[[T]]` 

### `exists_subst_inverse`

 Let `B = 𝔬[[T]]`, with `𝔬` the valuation ring of `ℂ_[p]`. The generator `T` has a
compositional inverse `Z`, and `f ∈ B` exactly when `f(Z)` has integral coefficients. 

### `smul_mem`

 Let `B = 𝔬[[T]]` be the ring of series in `T` over the valuation ring `𝔬` of `ℂ_[p]`. If
`c` has norm at most one and `f ∈ B`, then `c • f ∈ B`. 

### `norm_constantCoeff_le_one_and_norm_coeff_one_le_one`

 The constant term and the linear coefficient of an element of `B = 𝔬[[T]]` have norm at most
one. 

### `of_mem`

 Let `B = 𝔬[[T]]` be the ring of series in `T` over the valuation ring `𝔬` of `ℂ_[p]`. Any
`f = X + ⋯` in `B` generates the same ring: `𝔬[[f]] = B`. 

### `exists_mul_eq_one`

 An element of `B = 𝔬[[T]]`, the ring of series in `T` over the valuation ring `𝔬` of `ℂ_[p]`,
whose constant term has norm `1` is invertible in `B`. 

### `rescale_mem`

 Let `B = 𝔬[[T]]` be the ring of series in `T` over the valuation ring `𝔬` of `ℂ_[p]`. If
`T(a X)` lies in `B`, then `B` is stable under `f ↦ f(a X)`. 

 ### The ring `𝔬[[y]]` of a CM curve 

### `integralSeriesRing`

 The subring `𝔬[[y]]` of `ℂ_[p]⟦X⟧` of integral power series in the Taylor series of the
coordinate `y = C.translatedY`, with the `p`-adic place `ιₚ` applied to its coefficients. 

### `mem_integralSeriesRing`

 The elements of `𝔬[[y]]` are the series `g(y)` with `g` integral. 

### `isSeriesGenerator_translatedY`

 The Taylor series of `y = C.translatedY` in `ℂ_[p]⟦X⟧` begins with `X` and generates
`𝔬[[y]]`. 

### `_root_.New.exists_isRoot_cubic_constantCoeff_eq_zero`

 For `a` in the valuation ring `𝔬` of `ℂ_[p]`, the cubic `Y³ + (1 - a X) Y - X²` over `𝔬[[X]]`
has a root without constant term, by Hensel's lemma. 

### `taylorVia_translatedX_mem_integralSeriesRing`

 For a `CMLattice` `C`, consisting of a lattice `Λ`, a point `t` of order two modulo `Λ` and `a₁`
with `a₁² = 12 ℘(t)`, let `x(z) = ℘(z + t) − ℘(t)` be `C.translatedX` and `y = C.translatedY` the
companion coordinate, with Taylor series `y = X + ⋯` and `y' = 1 + 3 x² - a₁ y`, so that `(x, y)`
lies on the CM curve `y² + a₁ x y = x³ + x`. Then the Taylor series of `x` at `z = 0`, with the
`p`-adic place `ιₚ` applied to its coefficients, lies in `C.integralSeriesRing`. That is, it is a
power series in the likewise expanded `y` with coefficients in the ring of integers `𝔬` of
`ℂ_[p]`. 

### `derivative_mem_integralSeriesRing`

 For a `CMLattice` `C` (a lattice `Λ` with a point `t` of order two modulo `Λ`), let
`y = C.translatedY` be the `y`-coordinate of the CM curve `y² + a₁ x y = x³ + x`, where
`x(z) = ℘(z + t) − ℘(t)`. Expand `y` at `z = 0` and apply the `p`-adic place `ιₚ` to its
coefficients to get a series in `ℂ_[p]⟦X⟧`. The ring `C.integralSeriesRing` is the ring `𝔬[[y]]` of
power series in this `y` with coefficients in the ring of integers `𝔬` of `ℂ_[p]`. This ring is
stable under the derivative `d/dz`. 

 ## Congruence parts and integral solutions of a functional equation 

### `congruencePart`

 The part of `f` in degrees `≡ r` mod `m`. 

### `congruencePart_rescale`

 The substitution `f ↦ f(a X)` commutes with taking the part in degrees `≡ r` mod `m`. 

### `rescale_congruencePart_of_pow_eq_one`

 If `ζ ^ m = 1`, then replacing `X` by `ζ X` multiplies the part of a series in degrees `≡ r`
mod `m` by `ζ ^ r`. 

### `congruencePart_eq_sum`

 For `m ≠ 0` and a primitive `m`-th root of unity `ζ`, the part of `f` in degrees `≡ r` mod `m`
is the mean over `i < m` of the series `η ^ (-r) f(η z)` with `η = ζ ^ i`. 

### `congruencePart_subst`

 Let `m ≠ 0`. If `T` has constant term `0` and only degrees `≡ 1` mod `m`, then substituting `T`
commutes with taking the part of a series in the degrees `≡ r` mod `m`. 

### `IsSeriesGenerator.subst_injective`

 If `T` generates `B`, that is `B = 𝔬[[T]]` with `T = X + ⋯`, then `f ↦ f(T)` is injective. 

### `integralBelow`

 The ring of the power series whose coefficients in degrees below `n` are integral. 

### `subst_seriesToCp_mem_integralBelow`

 For `T : ℂ_[p]⟦X⟧` and `n : ℕ`: if `T(0) = 0`, the coefficients of `T` in degrees below `n` have
norm at most one and `g` is a series over the valuation ring of `ℂ_[p]`, then the coefficients of
`g(T)` in degrees below `n` have norm at most one. 

### `mem_range_seriesToCp_of_rescale_eq`

 Let `0 < |π| < 1` and let `G = z + ⋯` be a series over the valuation ring of `ℂ_[p]`, which
`seriesToCp` maps to `ℂ_[p]⟦X⟧`. A series `Y = z + ⋯` with `Y(π z) = π G(Y)` has coefficients in
the valuation ring, that is, lies in the range of `seriesToCp`. 

### `exists_rescale_eq_smul_X_sub_X_pow`

 Let `m ≠ 0` and let `π ≠ 0` lie in the valuation ring `𝔬` of `ℂ_[p]`. Let
`g = π z + b₁ z ^ (1 + m) + ∑_{i ≥ 2} bᵢ z ^ (1 + i m)` have coefficients in `𝔬`, with `b₁` a unit,
and let `ϖ ^ m = -π / b₁`. Then `g(ϖ z) = ϖ π (z - z ^ (1 + m) + π E)` for an integral series `E`
of order at least two. 

### `C_dvd_sub_X_of_rescale_eq`

 Let `π ≠ 0` be an element of a domain. If `Y = z + ⋯` and `Y(π z) = π W`, then `W ≡ z`
modulo `π`. 

### `C_dvd_sub_pow_sub_X_of_rescale_eq`

 Let `π ≠ 0` be an element of a domain. If `S = z + ⋯` and
`S(π z) = π (S - S ^ q + π E(S))`, then `S - S ^ q ≡ z` modulo `π`. 

### `mem_range_seriesToCp_of_rescale_eq_X_sub_X_pow`

 Let `0 < |π| < 1`, `q > 1` and let `E` be integral of order at least two. A series `Y = z + ⋯`
with `Y(π z) / π = Y - Y ^ q + π E(Y)` is integral. 

### `exists_seriesToCp_eq_of_rescale_eq`

 Let `0 < |π| < 1`, `q > 1` and let `E` be integral of order at least two. A series `Y = z + ⋯`
with `Y(π z) / π = Y - Y ^ q + π E(Y)` comes from an integral series `S`, and `S - S ^ q ≡ z`
modulo `π`. 

### `eq_sum_pow_of_sub_pow_eq`

 In characteristic `p`, if `s - s ^ q = x` with `q = p ^ e`, then
`s = ∑_{l < B} x ^ q ^ l + s ^ q ^ B` for every `B`. 

### `coeff_eq_of_sub_pow_eq_X`

 In prime characteristic `p`, let `q = p ^ e` with `e ≠ 0`. If `S(0) = 0` and `S - S ^ q = z`,
then `S = ∑ z ^ q ^ j`: the coefficient of degree `n` is `1` if `n` is a power of `q`, else `0`. 

### `dvd_coeff_sub_of_C_dvd_sub_pow_sub_X`

 If `π` is a non-unit that divides `p`, `q = p ^ e` with `e ≠ 0`, `S(0) = 0` and
`S - S ^ q ≡ z` modulo `π`, then `S ≡ ∑ z ^ q ^ j` modulo `π`. 
