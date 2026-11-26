---
{
  "module": "src/New/Derivatives/Sharpness/Cases.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Derivatives/Sharpness/Cases.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Derivatives/Sharpness/Cases.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The valuation bound `v(l!) + val₁₂(l) ≤ S_p + 2 ∑ v(B_τ)` for every prime

Let `w` be a tight frame of length `M` with a linear form of unit coefficients, and let `val₆` and
`val₁₂` be the least valuations on six and twelve copies along `w`. This file proves the bound
`v(l!) + val₁₂(l) ≤ S_p + 2 ∑ v(B_τ)` for every prime `p` and every degree `l` near the weights,
that is, with `κ(τ) ≤ l_τ ≤ κ(τ) + x ^ 42` at all places `τ`. Here `v` is the `p`-adic valuation,
`l! = ∏ l_τ!`, and `x = D.x` is the length of the prime sum.

## Main definitions and results

* `New.Parameters.resolutionForms`: the linear forms of a resolution, read in `ℂ_p`.
* `New.Data.isResolution_resolutionVectors`: a tight frame of length `M`, divided by an integer of
  `K` of norm `M`, is a resolution of the identity.
* `New.Data.leastValLE_six_zero_of_inert`: at an inert prime, `val₆(ν) ≤ 0` in all degrees.
* `New.Data.exists_hasNormalForm_resolutionForms`: at an inert prime the theta product along the
  frame has a normal form with unit leading coefficients.
* `New.Data.leastValLE_twelve`: `v(l!) + val₁₂(l) ≤ S_p + 2 ∑ v(B_τ)` for every prime `p`.

Notions from other files:
* `IsTightFrame w c M`: the `w_i` lie in the lattice `𝔞₀` of `E` and satisfy
  `∑ c_i σ(w_i) conj (τ(w_i)) = M δ_(σ τ)` for all places `σ`, `τ` of the CM type.
* `C.LeastValLE μ c n ν r`: `val_n(ν) ≤ r`, where `val_n(ν)` is the least valuation of a coefficient
  of degree `ν` in a product of `n` copies of `Θ = ∏ θ(μ_i z) ^ c_i` times integral series.
* `chiK P.d p`: the character of `K = ℚ(√-d)`; it is `1`, `-1`, `0` for split, inert, ramified `p`.
* `gammaPrime P.d p`, `partnerExponents P.d p`: the rate `γ_p`, and the set `I_p°` of exponents (the
  odd numbers if `p` is inert, all numbers if `p = d`); `I_p` consists of its positive elements.
* `D.weight τ`, `P.partner D.towerExp p e τ`: the weight `κ(τ)` and the partner `-p ^ e * τ` of a
  place `τ`.
* `l₀ = New.l₀ D.towerExp`: the range of exponents in which the `b`-places are sparse.
* `D.localPrimeSumTotal p`, `D.lossProduct l_τ`: the predicted valuation
  `S_p = ∑ D.localPrimeSum p κ(τ) τ`, and the product `B_τ` of the `n♯ = D.lossFactorCount` integers
  after `(l_τ - n♯)₊`.
* `P.cmCurve`: the curve `ℂ / Ω₀ 𝓞_K`, whose theta series is `θ`.



## Least valuations along a tight frame at non-split primes

A prime that does not split in `K` does not divide `q₁ M`, where `q₁ = D.q₁`.


### `isIntegralAbove_of_isIntegral_mul`

 If `N y` is an algebraic integer for a natural number `N` prime to `p`, then `y` is integral at
all places above `p`. 

### `CMLattice.thetaProd_smul`

 Multiplying the linear forms `μ_j` by `s` turns the product `Θ(z) = ∏ θ(μ_j z) ^ m j` of copies
of the theta series of `C` into `Θ(s z)`. 

### `Parameters.resolutionForms`

 For a family `w` in the field `E = P.E s`, the linear forms `μ_i z = ∑ μ_(i τ) z_τ` with the
coefficients `μ_(i τ) = periodFactor * conj (τ (w i))` at the places `τ`, read in `ℂ_p` by the
homomorphism `ιₚ : ℂ → ℂ_p`. The complex number `periodFactor = P.periodFactor s` normalises the
Taylor series of theta functions. For a tight frame `w` of length `π π̄` these are the forms
`𝔰 u† z = 𝔰 ∑ conj (τ u) z_τ` of the resolution `u = w / π̄`, with `𝔰 = π * periodFactor`. 

### `resolutionVectors`

 The vectors `u = w / π̄_M` of `E¹`, where the integer `π̄_M = D.piMBar` of `K` has norm
`M = D.M`. 

### `taylorScale`

 The scale `𝔰 = periodFactor * π_M` of the Taylor series, read in `ℂ_p`, where `π_M` is the
conjugate of `D.piMBar`. 

### `norm_conj_piMBar_mul_jetScale_sq`

 The period scale `π_M * jetScale` has the squared modulus `M / Ω`. Here `π_M` is the complex
conjugate of `D.piMBar`, `jetScale = periodFactor * √(2π / √d) / Ω₀` is the scale of the Taylor
series of theta functions, `M = D.M` is the level, and
`Ω = P.bigOmega D.towerExp = exp (γ - Re L′/L(1, χ_K)) * 2π / rd_E`, with `γ` Euler's constant and
`rd_E` the root discriminant of `E`. 

### `isResolution_resolutionVectors`

 Let `D` be admissible data for the parameters `P`, with the CM field `E = D.E`, a cyclotomic
extension of the imaginary quadratic field `K = ℚ(√-d)` (`d = P.d`), and the places `τ ∈ D.Φ` of
its CM type. Let `w` be a tight frame of length `M = D.M` with multiplicities `c`: the `w_i` lie in
the lattice `𝔞₀` of `E`, and `∑ c_i σ(w_i) conj (τ(w_i)) = M δ_(σ τ)` for all `σ, τ ∈ D.Φ`. Then
the vectors `u_i = w_i / π̄_M`, where the integer `π̄_M = D.piMBar` of `K` has norm `M`, are a
resolution of the identity: `z = ∑ c_i (u_i† z) u_i` for all complex vectors `z` indexed by the
places, where `u_i† z = ∑ conj (τ u_i) z_τ` is a sum over the places `τ`. 

### `resolutionForms_eq_smul`

 The forms of `w` are the scale `𝔰 = D.taylorScale` times the forms `z ↦ u† z` of the vectors
`u_i = w_i / π̄_M`. 

### `not_dvd_q₁_mul_M`

 A prime `p` that does not split in `K` (`χ_K(p) ≠ 1`) does not divide `q₁ M`, where `q₁ = D.q₁`
is the order of the root of unity that generates `E` over `K` and the level `M = D.M` is the
product of the two primes `D.levelPrime i`. 

### `isIntegralAbove_resolutionVectors`

 Let `D` be admissible data for the parameters `P`, with the CM field `E = D.E` over the
imaginary quadratic field `K = ℚ(√-d)` (`d = P.d`). Let `w` be a tight frame of length `M = D.M`
with multiplicities `c`: the `w_i` lie in the lattice `𝔞₀` of `E`, and
`∑ c_i σ(w_i) conj (τ(w_i)) = M δ_(σ τ)` for all places `σ`, `τ` of the CM type. Let `p` be a prime
that does not split in `K` (`χ_K(p) ≠ 1`). Then `u_i = w_i / π̄_M`, where `π̄_M = D.piMBar` has norm
`M`, is integral at every finite place `v` of `E` above `p`, that is, its `v`-adic absolute value is
at most `1`. 

### `norm_taylorScale_eq_one_of_not_dvd`

 Let `D` be admissible data for the parameters `P`: the CM field `E = D.E` is generated over
`K = ℚ(√-d)` by a root of unity of order `q₁ = D.q₁`, and the level `M = D.M` is the product of the
two primes `D.levelPrime i`. For every prime `p` that does not divide `q₁ M` the scale
`𝔰 = D.taylorScale` is a `p`-adic unit. The scale is the complex number `periodFactor * π_M`, read
in `ℂ_p` by the homomorphism `ιₚ : ℂ → ℂ_p` of `PadicPlace p`. 

### `norm_taylorScale`

 The scale `𝔰 = D.taylorScale` is a `p`-adic unit for every prime `p` that does not split in `K`
(`χ_K(p) ≠ 1`). 

### `leastValLE_six_zero_of_inert`

 Let `D` be admissible data for the parameters `P`, `p` a prime that is inert in `K = ℚ(√-d)`,
and `w` a tight frame of length `M = D.M` with multiplicities `c`. Then `val₆(ν) ≤ 0` for every
degree `ν`, a multi-index over the places `τ ∈ D.Φ`. 

### `exists_hasNormalForm_resolutionForms`

 Let `D` be admissible data for the parameters `P` and `p` a prime that is inert in `K = ℚ(√-d)`.
For a tight frame `w` of length `M = D.M` with multiplicities `c`, the theta product
`Θ = ∏ θ(μ_i z) ^ c_i` of the curve `P.cmCurve` along the linear forms
`μ = P.resolutionForms D.towerExp w` has a normal form `Θ(ϖ z) = W exp (c_ϖ ∑ λ_(e j) Γ_e ^ p ^ j)`:
the series `W` in the variables `z_τ` and the numbers `λ_(e j) = lam e j` are integral,
`c_ϖ = ϖ ^ (p + 1) / p`, and `Γ_e` is the coupling `∑ z_τ ^ p ^ e * z_(-p ^ e * τ)` of the places
`τ` with their partners, for `e` in `partnerExponents P.d p`, the set of odd numbers. Moreover `ϖ`
has valuation `ρ_p = varpiValuation P.d p = 1 / (p² - 1)`, and `λ_(e 0)` is a unit for odd `e`. 

### `norm_resolutionForms_le_one`

 If `w`, taken `c i` times, is a tight frame with frame bound `M = D.M` (`IsTightFrame w c D.M`),
then every coefficient of the forms `P.resolutionForms D.towerExp w` has `p`-adic norm at most `1`,
for every prime `p`. 


## The valuation bound on twelve copies

For non-split `p`, six copies carry couplings and six supply the remaining degrees. The three cases
are split `p`, inert `p > k` (all places are coupled with exponent `1`) and non-split `p ≤ k` (the
couplings follow the near pairs `D.IsNearPair`). They cover all primes, as the ramified prime `d` is
at most `k = D.k`.


### `IsNearWeights`

 The degree `l` is near the weights: `κ(τ) ≤ l_τ ≤ κ(τ) + x ^ 42` at every place `τ`, where
`l_τ = l (τ, ())`, `κ(τ) = D.weight τ` and `x = D.x`. 

### `IsNearWeights.weight_le`

 The degree at `τ` is at least the weight `κ(τ)`. 

### `IsNearWeights.le_weight_add`

 The degree at `τ` exceeds the weight `κ(τ)` by at most `x ^ 42`. 

### `le_two_mul_b`

 If the degree `l` is near the weights, that is, `κ(τ) ≤ l_τ ≤ κ(τ) + x ^ 42` at all places `τ`,
then each `l_τ` is at most `2 b`, where `b = D.b` is the weight at the `b`-places. 

### `div_le_lossFactorCount`

 Let `p` be a prime with `D.k < p`, and let the degree `l` be near the weights. Then at each
place `τ` the number `⌊(l_τ - n♯)₊ / p⌋` is at most `n♯ = D.lossFactorCount = ⌈6 * D.b / D.k⌉`. 

### `posPart_le_localPrimeSum`

 At a prime `p` that is inert in `ℚ(√-d)`, `d = P.d` (`χ_K(p) = -1`), the local prime sum
`D.localPrimeSum p κ(τ) τ = ∑ (κ(τ) / p ^ e - κ(-p ^ e * τ))₊` over odd `e` at a place `τ ∈ D.Φ` of
the CM type is at least its term for `e = 1`. 

### `padicValNat_factorial_sub_min_le`

 Let `p > D.k` be a prime that is inert in `ℚ(√-d)` and let the degrees `l_τ` lie between the
weights `κ(τ) = D.weight τ` and `κ(τ) + D.x ^ 42`. Put `i_τ = ⌊(l_τ - n♯)₊ / p⌋` with
`n♯ = D.lossFactorCount = ⌈6 b / k⌉`, and `j_τ = min i_τ l_(-p τ)` with the partner `-p τ` of `τ`.
Then `v(l_τ!) - j_τ` exceeds the local prime sum `D.localPrimeSum p κ(τ) τ = ∑ (κ(τ) / p ^ e - κ(-p
^ e τ))₊` (over odd `e`) by at most `2 v(B_τ)`. 

### `sum_padicValNat_factorial_le_add`

 The errors in Legendre's formula. Let `p ≥ 3` be prime, `v` the `p`-adic valuation, and let
`l = ν' + ν'' + η` be a degree within `D.x ^ 42` above the weights `D.weight`. Then `v(l!)` exceeds
`v(ν'! ν''! η!)` by at most `3 f (log b + 2)`, where `f = D.f` is the number of infinite places and
`log b = D.logB` is the logarithm of the weight `b = D.b` at the `b`-places; the number
`3 (log b + 2)` bounds the valuation of a multinomial coefficient. 

### `gammaPrime_mul_degree_sub_le_localPrimeSumTotal_add`

 Comparison with the predicted valuation `S_p = D.localPrimeSumTotal p`, the sum over the
places `τ` of `v(π_p) ∑ (κ(τ) / p ^ e - κ(-p ^ e τ))₊` over `e ∈ I_p`, where `κ = D.weight` and
`v(π_p)` is `1/2` for `p = d` and `1` otherwise. The set `I_p` consists of the odd numbers if `p`
is inert in `ℚ(√-d)`, of all positive numbers if `p = d`, and is empty if `p` splits. Let
`p ≤ k = D.k` be a prime and `l` a degree with `κ(τ) ≤ l_τ ≤ κ(τ) + x ^ 42`, `x = D.x`. Suppose
every near pair `(τ, e')` has `e' = e τ` and `j τ = ⌊l_τ / p ^ e'⌋`; near means that `e' ∈ I_p`,
that `e' < l₀ / 2`, where `l₀` is the least power of `3` above `27 * D.towerExp`, and that `τ`
and its partner `-p ^ e' * τ` are `b`-places, that is, lie in `D.bPlaces`, where the weight is
`b = D.b`. Then `γ_p |l| - |j| + 3 f (log b + 2) ≤ S_p + ∑ v(B_τ)`, where
`γ_p = gammaPrime P.d p` is `0`, `p / (p² - 1)`, `1 / (2 p - 2)` for split, inert, ramified `p`,
`f = D.f` is the number of infinite places, `log b = D.logB` and `B_τ = D.lossProduct l_τ` is the
product of the `n♯ = D.lossFactorCount` integers after `(l_τ - n♯)₊`. 

### `isCouplingFamily_of_isNearPair`

 Let `p` be a prime that does not split in `ℚ(√-d)` and is at most `k = D.k = r + 1 - m` (the
rank of the source, for the ranks `m`, `r` of the data), and let `(τ, e τ)` be a near pair for each
`τ ∈ Φ₀`: `e τ < l₀ / 2`, with `l₀` the least power of `3` above `27 * D.towerExp`; `e τ` lies in
the set `I_p`; and `τ` and its partner `-p ^ e τ * τ` are `b`-places. Then `Φ₀` and `e` are a family
of couplings: the exponents are odd, and no other pair `(τ₁, e')` with `τ₁ ∈ Φ₀` and odd `e' ≤ e τ`
has the partner of `(τ, e τ)`. 

### `powerDegree_add_partnerDegree_le_of_isNearPair`

 Let `p ≤ k = D.k` be a prime that does not split in `ℚ(√-d)` and `l` a degree between the
weights `κ(τ) = D.weight τ` and `κ(τ) + x ^ 42`, `x = D.x`. For each `τ ∈ Φ₀` let `(τ, e τ)` be a
near pair. Then the couplings `z_τ ^ p ^ e τ * z_(-p ^ e τ * τ)`, each used `j τ = ⌊l_τ / p ^ e τ⌋`
times, have total degree at most `l`; `powerDegree` and `partnerDegree` are the degrees of the first
and of the second factors. 

### `partner_bijective`

 The map `τ ↦ -p ^ e * τ` from a place to its partner is a bijection. 

### `powerDegree_add_partnerDegree_le_of_k_lt`

 Let `p` be a prime greater than `k = D.k`, and `l` a degree between the weights
`κ(τ) = D.weight τ` and `κ(τ) + x ^ 42`, `x = D.x`. The couplings `z_τ ^ p * z_(-p τ)` at all places
`τ` are used `j τ = min ⌊(l_τ - n♯)₊ / p⌋ l_(-p τ)` times each. Together they have total degree at
most `l`. 

### `leastValLE_twelve_of_split`

 Let `D` be admissible data for the parameters `P`, `p` a prime that splits in `ℚ(√-d)`
(`d = P.d`), `w` vectors of `D.E` with multiplicities `c`, and suppose that the linear form of
`w i₀` has unit coefficients in `ℂ_p` at all places `τ ∈ D.Φ`. Then `v(l!) + val₁₂(l) ≤ S_p` for
every degree `l`, and `S_p = D.localPrimeSumTotal p` is zero. 

### `leastValLE_twelve_of_lt`

 Let `D` be admissible data for the parameters `P` and `p` a prime above `k = D.k = r + 1 - m`
that is inert in `ℚ(√-d)`, `d = P.d`. Let `w` be a tight frame of length `M = D.M` with
multiplicities `c`, and `l` a degree between the weights `κ(τ) = D.weight τ` and `κ(τ) + x ^ 42`.
Then `v(l!) + val₁₂(l) ≤ S_p + 2 ∑ v(B_τ)`. 

### `_root_.New.chiK_eq_neg_one_of_ne`

 For primes `p ≠ d`, the Legendre symbol `chiK d p = (p / d)` is `-1` unless it is `1`. 

### `leastValLE_six_of_isNearPair`

 Let `D` be admissible data for the parameters `P`, `p` a prime with `2 < p ≤ k = D.k` that does
not split in `ℚ(√-d)`, `w` a tight frame of length `M = D.M` with multiplicities `c`, and `(τ, e τ)`
a near pair for each `τ ∈ Φ₀`: `e τ` lies in `I_p`, `e τ < l₀ / 2` with `l₀` the least power of `3`
above `27 * D.towerExp`, and `τ` and its partner `-p ^ e τ * τ` lie in the set `D.bPlaces` of places
of weight `b`. Let `ν'`, `ν''` be the degrees of the two factors of the couplings
`z_τ ^ p ^ e τ * z_(-p ^ e τ * τ)`, used `j τ` times. Let `val₆(ν)` be the least valuation of a
coefficient of total degree `ν = ν' + ν''` in a product of six copies of series `H Θ`, with `Θ` the
theta product along the forms `P.resolutionForms D.towerExp w` and `H` integral. Then
`v(ν'! ν''!) + val₆(ν) ≤ γ_p |ν| - |j|`. 

### `leastValLE_twelve_localPrimeSumTotal_of_le`

 Let `D` be admissible data for the parameters `P`, with the CM field `E = D.E` and its places
`τ ∈ D.Φ`, and `p ≤ k = D.k` a prime that does not split in `ℚ(√-d)`, `d = P.d`, with `ℂ` read in
`ℂ_p` by the homomorphism `ιₚ` of `PadicPlace p`. Let `w` be a tight frame of length `M = D.M` with
multiplicities `c` such that the form of `w i₀` has unit coefficients, and `l` a degree between the
weights `κ(τ) = D.weight τ` and `κ(τ) + x ^ 42`. Then `v(l!) + val₁₂(l) ≤ S_p + ∑ v(B_τ)`. 

### `leastValLE_twelve`

 Let `w` be a tight frame of length `M = D.M` with multiplicities `c` such that the form of
`w i₀` has unit coefficients, and let `l` be a degree between the weights `κ(τ) = D.weight τ` and
`κ(τ) + x ^ 42`. Then `v(l!) + val₁₂(l) ≤ S_p + 2 ∑ v(B_τ)`. 
