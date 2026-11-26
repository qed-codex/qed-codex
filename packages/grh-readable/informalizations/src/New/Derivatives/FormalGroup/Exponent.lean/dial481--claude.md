---
{
  "module": "src/New/Derivatives/FormalGroup/Exponent.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Derivatives/FormalGroup/Exponent.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Derivatives/FormalGroup/Exponent.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The exponent on one curve

Let `d ≡ 7` mod `8` be a prime (`PrimeSevenModEight d`), let `p` be a prime that does not split in
`ℚ(√-d)`, and let `𝒪` (`valRingCp p`) be the ring of integers of `ℂ_p`; a series is integral if its
coefficients lie in `𝒪`.

* `New.CMLattice.exists_exponent_tsum`: for some `ϖ` of valuation `ρ_p` the series `θ(ϖ z)` is
  integral up to one exponential `exp (c_ϖ Ξ₁)`, where `c_ϖ = ϖ ^ (p + 1) / p`, the series `Ξ₁` is
  integral, and modulo `π_p` it has only terms `(z ^ p ^ e * z) ^ p ^ j` with `e ∈ I_p°`
  (`partnerExponents d p`: the odd numbers, and all numbers if `p = d`).

The proof has four steps.

1. Averaging `ζ ^ (-p - 1) g(ζ z)` over the `(q_p - 1)`-th roots of unity `ζ` replaces `g = -log θ`
   by its part `g^♭` in the degrees `≡ p + 1` mod `q_p - 1`.
2. The Frobenius congruence gives a functional equation for `Ξ₁ = -g^♭(ϖ z) / c_ϖ`.
3. The equation is solved degree by degree. With `Y = T(ϖ z) / ϖ ≡ ∑_j z ^ q_p ^ j` and a number
   `λ ∈ 𝒪` one has `Ξ₁ ≡ λ Y ^ (p + 1)` for inert `p` and `Ξ₁ ≡ λ (Y ^ 2 - z ^ 2 / 2)` for `p = d`.
   The coefficients of the terms are `λ` in the first case, and `λ / 2`, `λ` or `2 λ` in the second.
4. For inert `p` the coefficient of `z ^ (p + 1)` in `Ξ₁` is a unit, and so is `λ`.

Notions from other files:
* `chiK d p` is the Legendre symbol `(p / d)`; the prime `p` is non-split if `chiK d p ≠ 1`.
* `q_p = primeNorm d p` is the norm of a prime above `p`, `π_p = piPrime d p` is `√-d` if `p = d`
  and `p` otherwise, and `ρ_p = varpiValuation d p` is `v(π_p) / (q_p - 1)` with `v(p) = 1`.
* `C : CMLattice d` is a lattice in `ℂ` that is stable under the ring of integers of `ℚ(√-d)`, with
  a chosen point `t` of order two.
* `taylorVia ιₚ C.θ` is the Taylor series over `ℂ_p` of the theta function `θ` of `C`, along the
  embedding `ιₚ : ℂ →+* ℂ_[p]` fixed by `PadicPlace p`, and `C.negLogTheta` is `g = -log θ`.
* `C.integralSeriesRing` is the ring `𝒪[[y]] = 𝒪[[T]]`, where `y` is the Taylor series of
  `C.translatedY` and `T = C.formalParam` is the formal parameter.

## Relation to the literature

Earlier bounds for one curve at inert primes, which are not used: Bannai–Kobayashi, Algebraic theta
functions and the p-adic interpolation of Eisenstein–Kronecker numbers (first arXiv version, Theorem
4.1); Bannai–Kobayashi, Integral structures on p-adic Fourier theory; Bannai–Kobayashi–Yasuda, The
radius of convergence of the p-adic sigma function; Fujiwara, On divisibilities of special values of
real analytic Eisenstein series.


### `leastFlatDegree`

 The least positive degree `i₀ ≡ p + 1` mod `q_p - 1` at a non-split prime: `2` if `p = d`, and
`p + 1` if `p` is inert. 

### `exists_congruencePart_eq_smul_X_pow_add`

 Let `G` be a series over the ring of integers `𝒪 = valRingCp p` of `ℂ_p`, read over `ℂ_p` by
`seriesToCp`, and let `i < m`. The part `congruencePart m i` of `G` in the degrees `≡ i` mod `m` is
`l X ^ i + X ^ (i + m) H` with `l ∈ 𝒪` and `H ∈ 𝒪[[X]]`. 

### `ne_zero_of_norm_eq_rpow`

 A number of norm `p ^ r` is not zero. 

### `exists_seriesToCp_eq_and_C_dvd_sub`

 Let `𝒪 = valRingCp p` be the ring of integers of `ℂ_p`. A series `F` over `ℂ_p` whose
coefficients are congruent modulo `π ∈ 𝒪` to those of an integral series `G` comes from an integral
series `Ξ` by `seriesToCp`, and `Ξ ≡ G` modulo `π`. 

### `chiK_eq_zero_of_ramified`

 For a prime `d ≡ 7` mod `8` the Legendre symbol `chiK d p = (p / d)` vanishes at `p = d`. 

### `ramified_or_inert`

 Let `d ≡ 7` mod `8` be a prime. A prime `p` with Legendre symbol `chiK d p = (p / d) ≠ 1` is
ramified in `ℚ(√-d)`, with norm `q_p = primeNorm d p = p`, or inert, with `(p / d) = -1` and
`q_p = p²`. 

### `leastFlatDegree_lt`

 At a non-split prime `p` (one with `chiK d p ≠ 1`), the degree `i₀ = leastFlatDegree d p` is
less than `q_p - 1`, where `q_p = primeNorm d p`. 

### `add_one_modEq_leastFlatDegree`

 At a non-split prime `p` (one with `chiK d p ≠ 1`), one has `p + 1 ≡ i₀ = leastFlatDegree d p`
mod `q_p - 1`, where `q_p = primeNorm d p`. 

### `norm_piPrime_mul_pow_leastFlatDegree_div`

 Let `d ≡ 7` mod `8` be a prime and `p` a prime with Legendre symbol `chiK d p = (p / d) ≠ 1`.
The numbers `π_p = piPrime d p`, `q_p = primeNorm d p`, `i₀ = leastFlatDegree d p` are `√-d`, `p`,
`2` if `p = d`, and `p`, `p²`, `p + 1` if `p` is inert; `π_p` is read in `ℂ_p` by the embedding `ιₚ`
that `PadicPlace p` fixes. If `ϖ ≠ 0` and `‖ϖ‖ ^ (q_p - 1) = ‖π_p‖`, then `π_p ϖ ^ i₀ / (q_p c_ϖ)`
has norm one. 

### `norm_piPrime_pow_div_le`

 Let `d ≡ 7` mod `8` be a prime and `p` a prime that is non-split in `ℚ(√-d)`. Let
`π_p = piPrime d p` be `√-d` if `p = d` and `p` otherwise, mapped to `ℂ_p` by the place `ιₚ`, and
let `q_p = primeNorm d p` be the norm of a prime above `p`. For `n > 2` we have
`‖π_p ^ n / q_p‖ ≤ ‖π_p‖`: the number `π_p ^ n / q_p` is `p ^ (n - 2)` if `p` is inert, and
`-π_p ^ (n - 2)` if `p = d`. 

 ## Step 1: averaging 

### `negLogThetaPart`

 The series `g^♭`: the part of `g = -log θ` (`C.negLogTheta`) in the degrees `≡ p + 1` mod
`q_p - 1`, where `q_p = primeNorm d p` and `θ` is the theta function of `C`, a lattice with complex
multiplication by the ring of integers of `ℚ(√-d)`. 

### `exponentSeries`

 The exponent `Ξ₁ = -g^♭(ϖ z) / c_ϖ`, where `g^♭ = C.negLogThetaPart` and
`c_ϖ = ϖ ^ (p + 1) / p`. 

### `expSubst_negLogThetaPart_sub_mem`

 Let `g = -log θ` and let `g^♭` be its part in the degrees `≡ p + 1` mod `q_p - 1`. The series
`θ exp g^♭ = exp (g^♭ - g)`, with `exp a` written `expSubst a`, lies in the ring `𝒪[[y]]` of series
with coefficients of norm at most one in the Taylor series of `y = C.translatedY`. 

### `smul_exponentSeries`

 For `ϖ ≠ 0` the exponent `Ξ₁ = C.exponentSeries ϖ` satisfies `c_ϖ Ξ₁ = -g^♭(ϖ z)`, where
`c_ϖ = ϖ ^ (p + 1) / p` and `g^♭ = C.negLogThetaPart`. 

### `exists_rescale_theta_eq_mul_expSubst`

 Let `θ` be the Taylor series of `C.θ`, the twisted translate of the sigma function of `C` by the
point `C.t` of order two, normalised to `θ(0) = 1` and read in `ℂ_p` by the embedding `ιₚ`. Let
`ϖ ≠ 0` have valuation at least `ρ_p = v(π_p) / (q_p - 1)`. Then `θ(ϖ z) = W exp (c_ϖ Ξ₁)` for a
series `W` over the integers of `ℂ_p`. 

 ## Step 2: the functional equation 

### `exists_congruencePart_eq_smul_formalParam_pow_add`

 Let `T = C.formalParam` be the formal parameter, the part in the degrees `≡ 1` mod `q_p - 1` of
the Taylor series of `C.translatedY`, so that `C.integralSeriesRing = 𝒪[[T]]`. Let `i < q_p - 1`.
For `H ∈ 𝒪[[T]]` the part of `H` in the degrees `≡ i` mod `q_p - 1` has the form
`l T ^ i + T ^ (i + q_p - 1) H'` with `l ∈ 𝒪` and `H' ∈ 𝒪[[T]]`. 

### `exists_smul_negLogThetaPart_sub_rescale_eq`

 The Frobenius congruence for `g^♭ = C.negLogThetaPart`, the part of `g = -log θ` in the degrees
`≡ p + 1` mod `q_p - 1`. Let `d ≡ 7` mod `8` be a prime and `p` a prime that does not split in
`ℚ(√-d)`. The numbers `π_p = piPrime d p`, `q_p = primeNorm d p`, `i₀ = leastFlatDegree d p` are
`√-d`, `p`, `2` if `p = d`, and `p`, `p²`, `p + 1` if `p` is inert. The formal parameter
`T = C.formalParam` is the part in the degrees `≡ 1` mod `q_p - 1` of the Taylor series of the
coordinate function `y = C.translatedY`. Then `q_p g^♭(z) - g^♭(ιₚ π_p z) = ιₚ π_p (l T ^ i₀ + T ^
(i₀ + q_p - 1) H)` for some `l ∈ 𝒪` and `H ∈ 𝒪[[T]]`. 

### `exists_smul_rescale_negLogThetaPart_sub_rescale_eq`

 The Frobenius congruence for `f(z) = g^♭(ϖ z)`. Let `p` be a prime that does not split in
`ℚ(√-d)`. The numbers `π_p = piPrime d p`, `q_p = primeNorm d p`, `i₀ = leastFlatDegree d p`,
`ρ_p = varpiValuation d p` are `√-d`, `p`, `2`, `1 / (2 p - 2)` if `p = d`, and `p`, `p²`, `p + 1`,
`1 / (p² - 1)` if `p` is inert. If `‖ϖ‖ ≤ p ^ (-ρ_p)` and `T(ϖ z) = ϖ Y` with `Y ∈ 𝒪[[z]]`, then
`q_p f(z) - f(π_p z) = π_p ϖ ^ i₀ (λ' Y ^ i₀ + ϖ ^ (q_p - 1) R)` for some `λ' ∈ 𝒪` and
`R ∈ 𝒪[[z]]`. 

### `exists_functional_equation_exponentSeries`

 The functional equation, modulo `π_p`, for the exponent `Ξ₁`. Let `p` be a prime that does not
split in `ℚ(√-d)`. The numbers `π_p = piPrime d p`, `q_p = primeNorm d p`,
`i₀ = leastFlatDegree d p`, `ρ_p = varpiValuation d p` are `√-d`, `p`, `2`, `1 / (2 p - 2)` if
`p = d`, and `p`, `p²`, `p + 1`, `1 / (p² - 1)` if `p` is inert. If `‖ϖ‖ = p ^ (-ρ_p)` and
`T(ϖ z) = ϖ Y` with `Y ∈ 𝒪[[z]]`, then there is `λ ∈ 𝒪` with
`(1 - π_p ^ n / q_p) [z ^ n] Ξ₁ ≡ λ [z ^ n] Y ^ i₀` modulo `π_p 𝒪` for all `n`. 

 ## Step 3: solving the functional equation 

### `coeff_exponentSeries_eq_zero_of_lt`

 Let `p` be non-split in `ℚ(√-d)`, that is, `chiK d p ≠ 1`, and `q_p = primeNorm d p`. For any
`ϖ`, the exponent `Ξ₁ = C.exponentSeries ϖ` has no terms below the degree
`i₀ = leastFlatDegree d p`, the least positive degree congruent to `p + 1` mod `q_p - 1`. 

### `norm_coeff_exponentSeries_sub_le`

 Let `p` be non-split (`chiK d p ≠ 1`), `π_p = piPrime d p`, `q_p = primeNorm d p`, and let
`a ∈ valRingCp p` satisfy `(1 - π_p ^ n / q_p) [z ^ n] Ξ₁ ≡ a` modulo `π_p` (through `ιₚ`) for the
exponent `Ξ₁ = C.exponentSeries ϖ`. Then `[z ^ n] Ξ₁ ≡ a` if `n > 2`, where the factor is `≡ 1`, and
if `n < leastFlatDegree d p`, where `Ξ₁` has no term of degree `n`. 

### `exists_seriesToCp_eq_exponentSeries_of_inert`

 Let `p` be inert in `ℚ(√-d)`, that is, `chiK d p = (p / d) = -1`, so that `π_p = piPrimeInt d`
is `p`, `q_p = primeNorm d p` is `p²` and `ρ_p = varpiValuation d p` is `1 / (p² - 1)`. If
`‖ϖ‖ = p ^ (-ρ_p)` and `T(ϖ z) = ϖ Y` with `Y ∈ 𝒪[[z]]`, then `Ξ₁` comes from a series `Ξ ∈ 𝒪[[z]]`
by the inclusion `seriesToCp`, and `Ξ ≡ λ Y ^ (p + 1)` modulo `π_p` for some `λ ∈ 𝒪`. 

### `exists_seriesToCp_eq_exponentSeries_of_ramified`

 Let `p = d`, so that `π_p = piPrimeInt d` is `√-d`, `q_p = primeNorm d p` is `p` and
`ρ_p = varpiValuation d p` is `1 / (2 p - 2)`. Let `‖ϖ‖ = p ^ (-ρ_p)` and `T(ϖ z) = ϖ Y` with
`Y ∈ 𝒪[[z]]` and `[z ^ 2] Y ^ 2 ≡ 1` modulo `π_p`, and let `half` be the inverse of `2` in `𝒪`. Then
`Ξ₁` comes from a series `Ξ ∈ 𝒪[[z]]` by the inclusion `seriesToCp`, and `Ξ ≡ λ (Y ^ 2 - z ^ 2 / 2)`
modulo `π_p` for some `λ ∈ 𝒪`. 

### `reducePiPrime`

 The reduction map `𝒪 → 𝒪 / π_p`, where `𝒪 = valRingCp p` and `π_p = piPrimeInt d`. 

### `instance : Nontrivial (valRingCp p ⧸ Ideal.span {(piPrimeInt d : valRingCp p)})`

 The ring `𝒪 / π_p` is nontrivial, because `π_p` has norm less than one. 

### `instance : CharP (valRingCp p ⧸ Ideal.span {(piPrimeInt d : valRingCp p)}) p`

 The ring `𝒪 / π_p` has characteristic `p`, because `π_p` divides `p`. 

### `map_reducePiPrime_eq_primePowerSeries`

 Let `Y ≡ ∑_j z ^ q_p ^ j` modulo `π_p`, where `q_p = primeNorm d p` and `π_p = piPrimeInt d`.
If the powers of `q_p` are the `p ^ i` with `i ∈ I`, then `Y` reduces to `∑_{i ∈ I} z ^ p ^ i`. 

### `C_dvd_pow_sub_primePowerSeries_odd_mul_even`

 Let `Y ≡ ∑_j z ^ q_p ^ j` modulo `π_p`, where `q_p = primeNorm d p` and `π_p = piPrimeInt d`.
If `q_p = p ^ 2`, as for inert `p`, then `Y ^ p Y` is congruent to the product of
`∑_{i odd} z ^ p ^ i` and `∑_{i even} z ^ p ^ i`. 

### `C_dvd_sq_sub_primePowerSeries_univ_sq`

 Let `Y ≡ ∑_j z ^ q_p ^ j` modulo `π_p`, where `q_p = primeNorm d p` and `π_p = piPrimeInt d`.
If `q_p = p`, as for `p = d`, then `Y ^ 2` is congruent to the square of `∑_i z ^ p ^ i`. 


## Step 4: the unit

The coefficient of `z ^ (p + 1)` in `Ξ₁` is a unit multiple of that of `z ^ (p - 1)` in `x`, which
is a unit by `New.CMLattice.norm_coeff_taylorVia_translatedX_eq_one`.


### `CMLattice.norm_coeff_exponentSeries_eq_one`

 Let `d ≡ 7` mod `8` be a prime, `C` a lattice stable under the ring of integers of `ℚ(√-d)`, and
`p` a prime that is inert there. For `ϖ ≠ 0` the coefficient of `z ^ (p + 1)` in
`Ξ₁ = C.exponentSeries ϖ = -(p / ϖ ^ (p + 1)) g^♭(ϖ z)` has norm one. 

### `summable_smul_X_pow_mul_X_pow`

 For any set `S` of exponents and any coefficients `λ_{e j}` in the valuation ring of `ℂ_p`, the
family `λ_{e j} (X ^ p ^ e X) ^ p ^ j` over `e ∈ S` and `j ∈ ℕ` is summable in the topology of
coefficientwise convergence. 

### `CMLattice.exists_eq_exponentSeries_dvd_sub_tsum_of_inert`

 The exponent modulo `π_p` at an inert prime. Let `p` be inert in `ℚ(√-d)`, that is,
`chiK d p = (p / d) = -1`, so that `π_p = piPrimeInt d` is `p`, `q_p = primeNorm d p` is `p²` and
`ρ_p = varpiValuation d p` is `1 / (p² - 1)`. Let `‖ϖ‖ = p ^ (-ρ_p)` and `T(ϖ z) = ϖ Y` with
`Y ∈ 𝒪[[z]]` and `Y ≡ ∑_j z ^ q_p ^ j` modulo `π_p`. Then `Ξ₁` comes from a series `Ξ ∈ 𝒪[[z]]` by
the inclusion `seriesToCp`, and `Ξ ≡ ∑_{e odd} ∑_j λ (z ^ p ^ e z) ^ p ^ j` modulo `π_p` for a unit
`λ` of `𝒪`. 

### `CMLattice.exists_exponentSeries_tsum_of_ramified`

 The exponent modulo `π_p` at the ramified prime. Let `p = d`, so that `π_p = piPrimeInt d` is
`√-d`, `q_p = primeNorm d p` is `p` and `ρ_p = varpiValuation d p` is `1 / (2 p - 2)`. Let
`‖ϖ‖ = p ^ (-ρ_p)` and `T(ϖ z) = ϖ Y` with `Y ∈ 𝒪[[z]]` and `Y ≡ ∑_j z ^ q_p ^ j` modulo `π_p`, and
let `half` be the inverse of `2` in `𝒪`. Then `Ξ₁` comes from a series `Ξ ∈ 𝒪[[z]]` by the inclusion
`seriesToCp`, and there is `λ ∈ 𝒪` with `Ξ ≡ ∑_e ∑_j λ_{e j} (z ^ p ^ e z) ^ p ^ j` modulo `π_p`,
where `λ_{0 0} = λ / 2`, `λ_{0 j} = λ` for `j ≥ 1`, and `λ_{e j} = 2 λ` for `e ≥ 1`. 

### `CMLattice.exists_exponent_tsum`

 Let `d ≡ 7` mod `8` be a prime, `C` a lattice with complex multiplication by the ring of
integers of `ℚ(√-d)`, and `p` a prime that does not split there. There are `ϖ ∈ ℂ_p` with
`‖ϖ‖ = p ^ (-ρ_p)` (where `‖p‖ = p⁻¹`), series `Ξ`, `W` over the ring `𝒪 = valRingCp p` of integers
of `ℂ_p` with `Ξ(0) = 0`, and numbers `λ_{e j} ∈ 𝒪` such that `θ(ϖ z) = W exp (c_ϖ Ξ)` and
`Ξ ≡ ∑_e ∑_j λ_{e j} (z ^ p ^ e z) ^ p ^ j` modulo `π_p`. Here `θ` is the Taylor series of the theta
function of `C`, read in `ℂ_p` by the embedding `ιₚ` that `PadicPlace p` fixes,
`c_ϖ = ϖ ^ (p + 1) / p`, `exp a` is written `expSubst a`, and `e` runs over
`I_p° = partnerExponents d p`: the odd numbers, or all if `p = d`. If `p` is inert, the `λ_{e 0}`
with `e` odd are units. 
