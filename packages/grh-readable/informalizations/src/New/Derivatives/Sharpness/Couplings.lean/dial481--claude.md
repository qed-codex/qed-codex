---
{
  "module": "src/New/Derivatives/Sharpness/Couplings.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Derivatives/Sharpness/Couplings.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Derivatives/Sharpness/Couplings.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Least valuations along couplings

Throughout, `v` is the valuation of `ℂ_[p]` with `‖x‖ = p ^ (-v x)`, a series is integral if its
coefficients lie in the valuation ring `valRingCp p`, and `seriesToCp` views an integral series as a
series over `ℂ_[p]`.

## Main definitions and results

* `New.IsCouplingFamily`: each selected coupling `z_τ ^ p ^ e τ * z_(τ⁺)` has `e τ` odd and has
  strictly the lowest exponent among such couplings of selected places with the same partner.
* `New.powerDegree`, `New.partnerDegree`: the degrees `ν'` and `ν''` of the two parts of a product
  of couplings, with their values at a place and their total degrees.
* `New.pairExponent`, `New.couplingSubst`: the exponent of `z' ^ ν' * z'' ^ ν''`, and the
  substitution `z_0 = δ_0 z' + z''`, `z_c = δ_c z'`.
* `New.IsCouplingFamily.norm_coeff_pairExponent`: the valuation of the coefficient of
  `z' ^ ν' * z'' ^ ν''` in `F(z' + z'') ∏_(c ≠ 0) F(δ_c z')` for `F = W exp (κ Ξ)`, where `κ` is a
  scalar of negative valuation.
* `New.CMLattice.leastValLE_six_of_isCouplingFamily`: at an inert prime `p > 2` the least valuation
  `val₆` on six copies satisfies `val₆(ν) ≤ -|j|` and `v(ν'! ν''!) + val₆(ν) ≤ γ_p |ν| - |j|`, where
  `ν = ν' + ν''` and `γ_p = gammaPrime d p = 1 / (p - 1) - varpiValuation d p`.

The variable `z'` that is raised to the power `p ^ e` is separated from the variable `z''` that
occurs linearly; the term in which every derivative in `z''` brings down `κ` dominates.

Notions from other files:
* `couplingSum S pr l` is the series `Ξ = ∑ l a b • Γ_a ^ p ^ b` over `a ∈ S` and `b : ℕ`, where
  `Γ_a` is the sum of the couplings `z_τ ^ p ^ a * z_(pr a τ)` over all `τ`.
* `copySubst a` substitutes `z ↦ ∑ a_k z_k` in copies `z_k` of the variables.
* `C : CMLattice d` is a lattice with multiplication by the integers of `ℚ(√-d)` and a chosen point
  `t` of order two; `C.θ` is the twisted translate by `t` of its sigma function, normalized to `1`
  at `0`, and `C.thetaProd μ m = ∏ θ(μ_i z) ^ m i`, read over `ℂ_[p]` through the embedding of `ℂ`
  that `PadicPlace p` fixes.
* `C.LeastValLE μ m n ν r` says `val_n(ν) ≤ r` for the least valuation `val_n(ν)` of a coefficient
  of degree `ν` in a product `∏ (H_c Θ)(z_c)` over `n` copies, where `Θ = C.thetaProd μ m` and the
  `H_c` run through the ring `C.multiSeriesRing μ`.


 ## Families of couplings 

### `IsCouplingFamily`

 The couplings `z_τ ^ p ^ e τ * z_(τ⁺)`, `τ ∈ Φ₀`, `τ⁺ = pr (e τ) τ`, have `e τ` odd, and each
has strictly the lowest exponent among the couplings `z_τ₁ ^ p ^ e' * z_(τ⁺)` with `τ₁ ∈ Φ₀`,
`e'` odd and `pr e' τ₁ = τ⁺`. Here `pr e τ` is the partner of the place `τ` for the exponent `e`. 

### `IsCouplingFamily.odd`

 The exponents are odd. 

### `IsCouplingFamily.eq_of_partner_eq`

 For `τ, τ₁ ∈ Φ₀` and odd `e' ≤ e τ`, the equation `pr e' τ₁ = τ⁺` holds only for `τ₁ = τ`,
  `e' = e τ`. 

### `powerDegree`

 The degree `ν'` of the monomial `∏ z_τ ^ (p ^ e τ * j τ)` over `τ ∈ Φ₀`. 

### `partnerDegree`

 The degree `ν''` of the monomial `∏ z_(τ⁺) ^ j τ` over `τ ∈ Φ₀`, where `τ⁺ = pr (e τ) τ`. 

 ## The coefficient of a product of couplings in a product of copies 

### `exists_pderiv_mul_expSubst`

 For integral series `W`, `Ξ` with `W` a unit and `Ξ(0) = 0`, and for any scalar `κ ∈ ℂ_[p]`, the
logarithmic derivative of `W exp (κ Ξ)` in the variable `x` is `κ ∂Ξ + B` with `B = ∂W / W`
integral. Here `expSubst a` is the series `exp a` and `seriesToCp` views an integral series as a
series over `ℂ_[p]`. 

### `exists_pderiv_mul_eq_smul`

 Let `κ ∈ ℂ_[p]` have norm greater than `1`, and let `∂` be the derivative in the variable `y`.
If `∂G = (κ A + B) G` with `A`, `B` integral, then for integral `g` we have `∂(g G) = κ g' G` with
`g'` integral and congruent to `g A` modulo the maximal ideal. 

### `exists_jet_mul_prod_X`

 Let `κ ∈ ℂ_[p]` have norm greater than `1`. If `∂_(t i) G = (κ A_i + B_i) G` with `A_i`, `B_i`
integral, then `(∏_(i ∈ T) ∂_(t i)) G = κ ^ #T g G` with `g` integral and congruent to `∏ A_i`
modulo the maximal ideal. The identity is stated after applying each differential operator `f(∂)`
and evaluating at `0`: `jet ℂ_[p] f G` is `f(∂) G (0)`. 

### `pairExponent`

 The exponent of the monomial `z' ^ ν' * z'' ^ ν''` in two copies of the variables. 

### `mapDomain_fst_pairExponent`

 Identifying the two copies of the variables sends `z' ^ ν' * z'' ^ ν''` to `z ^ (ν' + ν'')`. 

### `prod_factorial_pairExponent`

 The product of the factorials of the entries of `pairExponent ν' ν''`, the exponent of
`z' ^ ν' * z'' ^ ν''`, is `(∏_x (ν' x)!) * (∏_x (ν'' x)!)`, computed in `ℂ_[p]`. 

### `IsCouplingFamily.isLowestTerm_pderiv_couplingSum`

 Let `Ξ = ∑ l a b • Γ_a ^ p ^ b` be the coupling sum over odd `a`. Let `τ ∈ Φ₀` for a coupling
family (`e τ₁` is odd on `Φ₀`, and no other pair of an odd `a ≤ e τ` and `τ₁ ∈ Φ₀` has
`pr a τ₁ = τ⁺ = pr (e τ) τ`). Put `z_τ₁ = 0` for `τ₁ ∉ Φ₀` and reduce modulo the maximal ideal. Then
`Ξ_τ = ∂Ξ / ∂z_(τ⁺)` agrees with `l (e τ) 0 • z_τ ^ p ^ e τ` in all total degrees up to
`p ^ e τ`. 

### `isLowestTerm_zero_one`

 A series with constant term `1` has lowest term `1 = 1 z ^ 0` for the total degree:
`IsLowestTerm w f m c` says that, in `w`-weight at most that of `m`, the coefficients of `f` are
those of `c z ^ m`, here with all weights `1`, `m = 0` and `c = 1`. 

### `IsCouplingFamily.norm_coeff_powerDegree`

 Let `Ξ = ∑ l a b • Γ_a ^ p ^ b` be the coupling sum over odd `a`, where `Γ_a` is the sum of all
`z_τ ^ p ^ a * z_(pr a τ)`, with units `l a 0`, and let `Ξ_τ = ∂Ξ / ∂z_(τ⁺)`, `τ⁺ = pr (e τ) τ`, for
`τ` in a coupling family `Φ₀` (each `z_τ ^ p ^ e τ * z_(τ⁺)` has `e τ` odd and strictly lowest
degree among the `z_τ₁ ^ p ^ a * z_(τ⁺)` with `τ₁ ∈ Φ₀`, `a` odd and `pr a τ₁ = τ⁺`). If
`g ≡ ∏ Ξ_τ ^ j τ` modulo the maximal ideal and `U` has constant term `1`, then the coefficient of
`z ^ ν'` in `g U` is a unit, where `ν' = powerDegree p Φ₀ e j` is the degree of
`∏ z_τ ^ (p ^ e τ * j τ)`. 

### `couplingSubst`

 The coefficients of the substitution `z_0 = δ_0 z' + z''`, `z_c = δ_c z'` for `c ≠ 0`, in two
copies `z'`, `z''` of the variables. 

### `norm_couplingSubst_le_one`

 The coefficients of `couplingSubst δ` are integral if the `δ_c` are. 

### `pderiv_prod_copySubst_couplingSubst`

 Let `δ 0 = 1` and let `G = ∏_c copySubst (couplingSubst δ c) F`, that is,
`G(z', z'') = F(z' + z'') ∏_(c ≠ 0) F(δ_c z')` in two copies `z'`, `z''` of the variables. Only the
first factor involves `z''`, so if `∂_x F = L F`, then the derivative of `G` in `z''_x` is
`L(z' + z'') G`. 

### `coeff_prod_copySubst_rescale`

 Scaling the variables by `ϖ` in each factor of `∏ F(∑ A c k z_k)` (product over `c`) multiplies
the coefficient of `z ^ γ` by `ϖ ^ γ.degree`, the total degree of `γ`. 

### `monomial_mul_prod_X_partner`

 The monomial `z' ^ ν'` times the product, over `τ ∈ Φ₀`, of `j τ` copies of `z''_(τ⁺)`, where
`τ⁺ = pr (e τ) τ`, is `z' ^ ν' * z'' ^ ν''` with `ν'' = partnerDegree pr Φ₀ e j`. 

### `exists_jet_prod_copySubst_couplingSubst`

 Let `κ ∈ ℂ_[p]` have norm greater than `1`, let `F = W exp (κ Ξ)` with `W`, `Ξ` integral, `W` a
unit and `Ξ(0) = 0`, let `δ 0 = 1` and let `G = F(z' + z'') ∏_(c ≠ 0) F(δ_c z')` in two copies `z'`,
`z''` of the variables. Differentiating `G` in the variables `z''_(t i)`, `i ∈ T`, gives
`κ ^ #T g G` with `g` integral and `g(z', 0) ≡ ∏ ∂_(t i) Ξ` modulo the maximal ideal. 

### `IsCouplingFamily.norm_coeff_pairExponent`

 Let `Ξ = ∑ l a b • Γ_a ^ p ^ b` be the coupling sum over odd `a`, where `Γ_a` is the sum of all
`z_τ ^ p ^ a * z_(pr a τ)`, and let `ν' = powerDegree p Φ₀ e j`, `ν'' = partnerDegree pr Φ₀ e j` be
the degrees of `∏ z_τ ^ (p ^ e τ * j τ)` and `∏ z_(τ⁺) ^ j τ`, `τ⁺ = pr (e τ) τ`, for a coupling
family (odd `e τ`, each coupling `z_τ ^ p ^ e τ * z_(τ⁺)`, `τ ∈ Φ₀`, of strictly lowest degree among
the `z_τ₁ ^ p ^ a * z_(τ⁺)` with `τ₁ ∈ Φ₀`, `a` odd and `pr a τ₁ = τ⁺`). Let `F = W exp (κ Ξ)` over
`ℂ_[p]`, with `W` integral and a unit, `l a 0` a unit for odd `a`, and `κ ∈ ℂ_[p]` of negative
valuation `v(κ)`. Let `δ 0 = 1` and let `∏_c F(δ_c z) = U` be integral with constant term `1`. Then
the coefficient of `z' ^ ν' * z'' ^ ν''` in the product `G = F(z' + z'') ∏_(c ≠ 0) F(δ_c z')` given
by `couplingSubst δ` has valuation `|j| v(κ) - v(ν''!)`, where `|j| = ∑ j τ` and
`ν''! = ∏ (ν'' x)!`. 

### `varpiValuation_mul_add_one_of_inert`

 Let `d` be a prime `≡ 7 mod 8` (the class `PrimeSevenModEight d`). At a prime `p` inert in
`ℚ(√-d)` (that is, `(p / d) = -1`), `ρ_p (p + 1) = 1 / (p - 1)` for
`ρ_p = varpiValuation d p = 1 / (p² - 1)`. 

### `norm_pow_div_of_inert`

 Let `d` be a prime `≡ 7 mod 8` and let the prime `p` be inert in `ℚ(√-d)`, that is, the Legendre
symbol `chiK d p = (p / d)` is `-1`. If `v(ϖ) = ρ_p = varpiValuation d p = 1 / (p² - 1)`, then
`ϖ ^ (p + 1) / p` has valuation `1 / (p - 1) - 1`. 

### `one_lt_norm_pow_div_of_inert`

 Let `d` be a prime `≡ 7 mod 8` and let the prime `p > 2` be inert in `ℚ(√-d)`. If `ϖ ∈ ℂ_[p]`
has valuation `ρ_p = varpiValuation d p = 1 / (p² - 1)`, then `ϖ ^ (p + 1) / p` has negative
valuation, that is, norm greater than `1`. 

### `isUnit_of_rescale_thetaProd_eq`

 Let `C : CMLattice d` be a CM lattice, let `θ` be the series over `ℂ_[p]` of its normalized
theta function `C.θ`, and suppose that `Θ = C.thetaProd μ m = ∏ θ(μ_i z) ^ m i` has the exponential
factorization `Θ(ϖ z) = W exp (κ Ξ)` with scalars `ϖ`, `κ ∈ ℂ_[p]`, integral series `W`, `Ξ` and
`Ξ(0) = 0`. Then `W` is a unit, since its constant term is `Θ(0) = 1`. 

### `exists_prod_rescale_rescale_thetaProd_eq`

 Let `C` be a CM lattice for a prime `d ≡ 7 mod 8`, let the linear forms `μ` be integral, let
`Θ = C.thetaProd μ m = ∏ θ(μ_i z) ^ m i`, where `θ` is the series over `ℂ_[p]` of the normalized
theta function `C.θ` (`PadicPlace p` fixes an embedding of `ℂ` in `ℂ_[p]`), and let `v(ϖ) ≥ ρ_p`,
where `ρ_p = varpiValuation d p` is `1 / (p - 1)`, `1 / (p² - 1)`, `1 / (2 p - 2)` for `p` split,
inert, ramified in `ℚ(√-d)`. There are six integral `δ_c` with `δ 0 = 1` such that `∏ Θ(δ_c ϖ z)`
is integral with constant term `1`. 

### `leastValLE_partnerDegree_of_isCouplingFamily`

 Let `C` be a CM lattice for a prime `d ≡ 7 mod 8`, and let `θ`, `y` be the series over `ℂ_[p]`
of the normalized theta function `C.θ` and of the function `C.translatedY` of `℘` and `℘'` at
`z + t`. Let `Θ = C.thetaProd μ m = ∏ θ(μ_i z) ^ m i` for integral linear forms `μ_i`. The ring
`C.multiSeriesRing μ` consists of the integral series in the `y(μ_i z)`.

Let `p > 2` be inert, and let `Θ` have the normal form `Θ(ϖ z) = W exp (ϖ ^ (p + 1) / p * ∑ l a b •
Γ_a ^ p ^ b)` with `W` integral, `a` odd in the sum, `Γ_a` the sum of all
`z_τ ^ p ^ a * z_(pr a τ)`, `v(ϖ) = ρ_p = varpiValuation d p` and with `l a 0` a unit for odd `a`.
For a coupling family (odd `e τ`, each coupling `z_τ ^ p ^ e τ * z_(τ⁺)`, `τ ∈ Φ₀`,
`τ⁺ = pr (e τ) τ`, of strictly lowest degree among the `z_τ₁ ^ p ^ a * z_(τ⁺)` with `τ₁ ∈ Φ₀`, `a`
odd and `pr a τ₁ = τ⁺`) let `ν = ν' + ν''` be the degree of `∏ (z_τ ^ p ^ e τ * z_(τ⁺)) ^ j τ`, with
`ν' = powerDegree p Φ₀ e j` and `ν'' = partnerDegree pr Φ₀ e j`. Let `val₆(ν)` be the least
valuation of a coefficient of degree `ν` in a product `∏ (H_c Θ)(z_c)` over six copies, with
`H_c ∈ C.multiSeriesRing μ`. Then `v(ν''!) + val₆(ν) ≤ |j| / (p - 1) - |j| - ρ_p |ν|` with
`|j| = ∑ j τ` and `ν''! = ∏ (ν'' x)!`. 

### `leastValLE_six_of_isCouplingFamily`

 Couplings. Let `C` be a CM lattice for a prime `d ≡ 7 mod 8`, let `θ` be the series over `ℂ_[p]`
of its normalized theta function `C.θ`, let `p > 2` be inert in `ℚ(√-d)`, let the linear forms `μ`
be integral, and let the theta product `Θ = C.thetaProd μ m = ∏ θ(μ_i z) ^ m i` have the normal form
`Θ(ϖ z) = W exp (ϖ ^ (p + 1) / p * ∑ l a b • Γ_a ^ p ^ b)` with `W` integral, `a` odd in the sum,
`Γ_a` the sum of all `z_τ ^ p ^ a * z_(pr a τ)`, `v(ϖ) = ρ_p = varpiValuation d p` and `l a 0` a
unit for odd `a`. For a coupling family (odd `e τ`, each coupling `z_τ ^ p ^ e τ * z_(τ⁺)`,
`τ ∈ Φ₀`, `τ⁺ = pr (e τ) τ`, of strictly lowest degree among those with the partner `τ⁺`) let `ν'`
and `ν''` be the degrees of `∏ z_τ ^ (p ^ e τ * j τ)` and `∏ z_(τ⁺) ^ j τ`, and `ν = ν' + ν''`. Let
`val₆(ν)` be the least valuation of a coefficient of degree `ν` in a product `∏ (H_c Θ)(z_c)` over
six copies, with `H_c` in the ring `C.multiSeriesRing μ` of integral series in the `y(μ_i z)`, where
`y` is the series of `C.translatedY`. Then `val₆(ν) ≤ -|j|` and
`v(ν'! ν''!) + val₆(ν) ≤ γ_p |ν| - |j|`, where `|j| = ∑ j τ` and
`γ_p = gammaPrime d p = 1 / (p - 1) - ρ_p = p / (p² - 1)`. 
