---
{
  "module": "src/New/Derivatives/FormalGroup/ThetaProducts.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Derivatives/FormalGroup/ThetaProducts.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Derivatives/FormalGroup/ThetaProducts.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The normal form of theta products at non-split primes

The file treats products of theta functions at a prime `p` that is not split in `K = ℚ(√-d)`. Here
`θ` is the theta function of the CM curve, `y` the parameter `C.translatedY` of the curve, composed
with the forms `u† z`, and `E` is `K` with a root of unity adjoined.

The vectors `u` of `Eⁿ` form a resolution of the identity and are integral above `p`. The partner of
an infinite place `τ` of `E` is `-p ^ e τ`, and `Γ_e` is the coupling of the places with their
partners. Congruences modulo `π_p` between powers at a place and conjugation at its partner lead to
a normal form for `∏ θ(u_j† z) ^ m j` times an integral series in the `y(u† z)`.

## Main definitions and results

* `New.Parameters.norm_pow_sub_conj_partner_le`: for `e` in `I_p°`, modulo `π_p`, the `p ^ e`-th
  power at a place `τ` is complex conjugation at its partner `-p ^ e τ`.
* `New.Parameters.piPrimeInt_dvd_sum_linearSeries_sub_coupling`: at a non-split `p`, for a
  resolution of the identity by vectors `u` integral above `p`, the sum
  `∑ m j * (u_j† z) ^ p ^ e * (u_j† z)` is the coupling `Γ_e` modulo `π_p` for `e` in `I_p°`.
* `New.Parameters.exists_hasNormalForm`: at a non-split prime `p`, for a resolution of the identity
  by vectors `u` integral above `p`, the product `∏ θ(u_j† z) ^ m j` times an integral series in the
  `y(u† z)` has the normal form.

Notions from other files:
* `New.piPrime`, `New.piPrimeInt`: the number `π_p`, which is `√-d` if `p = d` and `p` otherwise, in
  `ℂ` and in the valuation ring (through the embedding `ιₚ : ℂ → ℂ_p`).
* `New.chiK`, `New.partnerExponents`: the character `χ_K`, with `χ_K(p) ≠ 1` at non-split `p`, and
  the set `I_p°` of exponents `e`: the odd ones if `p` is inert, all if `p = d`, none if `p` splits.
* `New.IsResolution`: the vectors `u` with multiplicities `m` satisfy `z = ∑ m j (u_j† z) u_j`,
  where `u† z = ∑ conj (τ(u_c)) z_(τ,c)`.
* `New.coupling`, `New.HasNormalForm`: `Γ_e = ∑ z_(τ,c) ^ p ^ e * z_(τ',c)` with `τ'` the partner
  of `τ`, and `F(ϖ z) = W exp (c_ϖ ∑ λ_{e j} Γ_e ^ p ^ j)` with `W` integral.


 ## Substitution of a linear form 

### `coeff_subst_linearSeries`

 The coefficient of `z ^ D` in `g(∑ c_x z_x)` is `c ^ D g⁽ⁿ⁾(0) / D!` with `n = |D|`, where
`c ^ D = ∏ c_x ^ D_x`, `D! = ∏ D_x!` and `g⁽ⁿ⁾(0)` is `n!` times the `n`-th coefficient of `g`. 

### `rescale_subst_linearSeries`

 Scaling all variables of `g(∑ c_x z_x)` by `a` is scaling the variable of `g` by `a`. 


## Partners of places and couplings

The congruence for powers at partners compares two ring maps on generators of `𝓞 E`. It turns the
identity `∑ m_j τ(u_{j,c}) (u_j† z) = z_(τ,c)` into the congruence for the coupling.


### `piPrimeInt_dvd_iff`

 An element of the valuation ring of `ℂ_p` is divisible by `π_p` (`√-d` if `p = d`, else `p`)
exactly when its norm is at most that of `π_p`. 

### `partner`

 The partner `-p ^ e τ` of an infinite place `τ` of `E`. Here `P` fixes the prime `d` and the
modulus `q₀`, and `E = P.E s` is `K = ℚ(√-d)` with a root of unity of order `q₁ = P.q₁ s` adjoined,
`s` being the level in the tower of these fields. The infinite places `P.Φ s` of `E` form the group
`Gal(E/K) = (ℤ/q₁)ˣ`, and the partner is the product of `τ` with `P.placeOfInt s (-p ^ e)`, the
place of the class of `-p ^ e` modulo `q₁` (the identity if this class is not a unit). 

### `norm_pow_succ_div_mul_piPrimeInt`

 Let `p` be non-split in `K = ℚ(√-d)` (`χ_K(p) ≠ 1`) and let `ϖ` have valuation
`ρ_p = varpiValuation P.d p`, which is `1 / (p² - 1)` if `p` is inert and `1 / (2 p - 2)` if
`p = d`. Then `c_ϖ π_p` has valuation `1 / (p - 1)`, where `c_ϖ = ϖ ^ (p + 1) / p` and `π_p` is
`√-d` if `p = d` and `p` otherwise. 

### `norm_pow_sub_conj_partner_le`

 Let `E = P.E s` be `K = ℚ(√-d)` (`d = P.d`) with a root of unity of order `q₁ = P.q₁ s`
adjoined, `s` being the level in the tower of these fields. Let `e` be in
`I_p° = partnerExponents P.d p`. Let `τ : P.Φ s` be an infinite place of `E`, and
`τ' = -p ^ e τ = P.partner s p e τ` its partner: the product of `τ` with the class of `-p ^ e` in
the group `Gal(E/K) = (ℤ/q₁)ˣ` of places. Then `τ(α) ^ p ^ e ≡ conj (τ'(α))` modulo `π_p` for `α` in
`𝓞 E`. 

### `norm_conj_pow_sub_partner_le`

 Let `E = P.E s` be `K = ℚ(√-d)` (`d = P.d`) with a root of unity of order `q₁ = P.q₁ s`
adjoined, `s` being the level in the tower of these fields. Let `e` be in
`I_p° = partnerExponents P.d p`. Let `τ : P.Φ s` be an infinite place of `E`, and
`τ' = -p ^ e τ = P.partner s p e τ` its partner: the product of `τ` with the class of `-p ^ e` in
the group `Gal(E/K) = (ℤ/q₁)ˣ` of places. Then `conj (τ(y)) ^ p ^ e ≡ τ'(y)` modulo `π_p` for `y` in
`E` integral at all primes above `p`. 

### `dvd_pow_sub_sum_partner`

 Let `E = P.E s` be `K = ℚ(√-d)` with a root of unity of order `q₁ = P.q₁ s` adjoined, `e` in
`I_p° = partnerExponents P.d p` and `y` a vector over `E` integral above `p`. Then the `p ^ e`-th
power of the linear form `y† z = ∑ conj (τ(y_c)) z_(τ,c)` is `∑ τ'(y_c) z_(τ,c) ^ p ^ e` modulo
`π_p`; the sum runs over infinite places `τ` in `P.Φ s` and coordinates `c`.
`τ' = -p ^ e τ = P.partner s p e τ` is the product of `τ` with the class of `-p ^ e` in the group
`Gal(E/K) = (ℤ/q₁)ˣ` of places. `μ`, `ν` are the coefficients of the form and of the sum, read as
integers of `ℂ_p` through the embedding `ιₚ : ℂ → ℂ_p`. 

### `norm_daggerForms_le_one`

 For vectors `u_j` over `E = P.E s` integral above `p`, the linear forms `u_j† z`, whose
coefficient at `z_(τ,c)` is `conj (τ(u_{j,c}))` read in `ℂ_p` through the embedding `ιₚ` of `ℂ`,
have integral coefficients. 

### `piPrimeInt_dvd_sum_linearSeries_sub_coupling`

 Let `E = P.E s` be `K = ℚ(√-d)` (`d = P.d`) with a root of unity of order `q₁ = P.q₁ s`
adjoined, `s` being the tower level, and let `e` be in `I_p° = partnerExponents P.d p`. Let the
vectors `u_j` of `Eⁿ`, integral above `p` and each taken `m_j` times, be a resolution of the
identity: `z = ∑ m_j (u_j† z) u_j`. Then `∑ m_j (u_j† z) ^ p ^ e * (u_j† z)` is the coupling
`Γ_e = ∑ z_(τ,c) ^ p ^ e * z_(τ',c)` modulo `π_p`. 


## The normal form of products of theta functions

Each theta factor at `ϖ z` is an integral series times `exp (c_ϖ Ξ(u† z))`. Modulo `π_p` the
`p`-th power is additive, so the exponents add up to a combination of powers of the couplings.


### `dvd_sum_subst_sub_couplingSum`

 Let `π ∣ p`, let `Ξ` be a series in one variable congruent to
`∑ λ_{e j} (z ^ p ^ e * z) ^ p ^ j` modulo `π`, the sum over `e ∈ S` and `j` with
`λ_{e j} = l e j`, and let `partner e` be a self-map of the set `Φ` of places, with
`Γ_e = coupling partner e = ∑ z_(τ,c) ^ p ^ e * z_(partner e τ,c)` summed over `(τ, c)` in `Φ × n`.
If series `L_i` without constant term are such that `∑ m_i L_i ^ p ^ e * L_i` is `Γ_e` modulo `π`
for `e ∈ S`, then the `Ξ(L_i)`, each taken `m_i` times, add up to
`couplingSum S partner l = ∑ λ_{e j} Γ_e ^ p ^ j` modulo `π`. 

### `expSubst_nsmul`

 For a series `g` without constant term, `exp (n g) = exp(g) ^ n`. 

### `rescale_subst_linearSeries_coe`

 For a linear form `L = ∑ ν_x z_x` with integral coefficients, `g(L)` at `ϖ z` is the series
`g(ϖ t)` at `t = L`. 

### `seriesToCp_subst`

 The inclusion `seriesToCp` of integral series commutes with substituting a series `L` without
constant term into a series `G` in one variable. 

### `rescale_mem_range_of_mem_multiSeriesRing`

 Let `d ≡ 7 mod 8` be prime, `C` a lattice with complex multiplication by the integers of
`ℚ(√-d)` and a point `t` of order two with `a₁² = 12 ℘(t)`, and `y` the Taylor series at `0`, read
in `ℂ_p` by `ιₚ`, of `C.translatedY z = (℘'(z + t) - a₁ (℘(z + t) - ℘(t))) / 2`. Let `μ_i` be
integral linear forms and `v(ϖ) ≥ ρ_p = varpiValuation d p`. Then a series `H` in
`C.multiSeriesRing`, the ring of integral series in the `y(μ_i z)`, is integral at `ϖ z`: `H(ϖ z)`
is in the range of `seriesToCp`, the inclusion of series over the integers of `ℂ_p`. 

### `rescale_thetaProd_eq_mul_expSubst`

 Let `C` be a lattice with complex multiplication by the integers of `ℚ(√-d)` and a point of
order two, and `θ = taylorVia ιₚ C.θ` the Taylor series of its theta function, read in `ℂ_p` by the
embedding `ιₚ` of `ℂ`. Let `θ(ϖ z) = W exp (κ Ξ)` with integral series `W`, `Ξ` and `Ξ(0) = 0`. Then
`C.thetaProd`, the product `∏ θ(μ_i z) ^ m_i` for integral linear forms `μ_i`, is at `ϖ z` the
integral series `∏ W(μ_i z) ^ m_i` times `exp (κ ∑ m_i Ξ(μ_i z))`. 

### `exists_hasNormalForm`

 Let `E = P.E s` be `K = ℚ(√-d)` with a root of unity of order `q₁ = P.q₁ s` adjoined, `p` a
prime not split in `K` (`chiK P.d p ≠ 1`), `I_p° = partnerExponents P.d p`, and for an infinite
place `τ` of `E` let its partner `τ' = -p ^ e τ` be the product of `τ` with the class of `-p ^ e` in
the group `Gal(E/K) = (ℤ/q₁)ˣ` of places. There are `ϖ` of valuation `ρ_p = varpiValuation P.d p`
and integers `λ_{e j}` of `ℂ_p`, with the `λ_{e 0}` for odd `e` units if `p` is inert, such that the
following holds. Take any resolution of the identity by vectors `u_j` of `Eⁿ`, taken `m_j` times and
integral above `p`. Then the product `∏ θ(u_j† z) ^ m_j` times an integral series in the `y(u_j† z)`
has the normal form. 
