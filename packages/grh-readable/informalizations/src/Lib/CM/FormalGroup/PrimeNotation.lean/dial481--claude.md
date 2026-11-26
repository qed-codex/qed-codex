---
{
  "module": "src/Lib/CM/FormalGroup/PrimeNotation.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/CM/FormalGroup/PrimeNotation.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/CM/FormalGroup/PrimeNotation.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Notation at a prime, and elements of prime-power norm at split primes

For primes `p` and `d ≡ 7 mod 8`, the file defines the numbers and sets of exponents attached to `p`
and the imaginary quadratic field `K = ℚ(√-d)`, and computes them when `p` is split, inert or
ramified. For a prime `p` that splits in `K`, it then finds an element whose norm is a power of `p`
and whose conjugate is a unit at the `p`-adic place.

The statements use the following notions, for primes `p` and `d`; from `piPrime_mem_quadInt` on,
`d ≡ 7 mod 8` is assumed, and `quadInt d` is the ring of integers of `K` inside `ℂ`.

* `chiK d p`: the Legendre symbol `(p / d)`; for `d ≡ 7 mod 8` it is `1`, `-1`, `0` when `p` is
  split, inert, ramified in `K`.
* `primeNorm d p`, also written `q_p`: `p ^ 2` if `(p / d) = -1`, and `p` otherwise.
* `ιₚ : ℂ →+* ℂ_[p]`: the embedding given by an instance `PadicPlace p`; the valuation `v` of
  `ℂ_[p]` with `v(p) = 1` is expressed by `‖x‖ = p ^ (-v(x))`.

## Main definitions and results

* `New.piPrime`, `New.piPrimeValuation`: the number `π_p`, which is `√-d` for `p = d` and `p`
  otherwise, and its valuation `v(π_p)`, which is `1 / 2` for `p = d` and `1` otherwise.
* `New.varpiValuation`, `New.gammaPrime`: the numbers `ρ_p = v(π_p) / (q_p - 1)` and
  `γ_p = 1 / (p - 1) - ρ_p`.
* `New.partnerExponents`, `New.positivePartnerExponents`: the sets `I_p°` and `I_p`. The set `I_p°`
  consists of the odd numbers if `p` is inert, of all numbers if `p = d`, and is empty if `p`
  splits; `I_p` consists of its positive elements.
* `New.hasSum_gammaPrime`: `γ_p = v(π_p) ∑_{e ∈ I_p} p⁻ᵉ`.
* `New.piPrime_mul_conj`, `New.norm_piPrime`, `New.norm_piPrime_eq_rpow_pow`: the norm of `π_p` at a
  non-split prime, its valuation, and the relation `v(π_p) = (q_p - 1) ρ_p`.
* `New.exists_mul_conj_eq_pow`: for a prime `p` that splits in `K` there is an `α` in the ring of
  integers with `α ᾱ` a positive power of `p` and `ᾱ` a `p`-adic unit; the proof takes a generator
  of a power of the prime of `K` induced by the `p`-adic place.

## Relation to the literature

Known result: decomposition of primes in `ℚ(√-d)` and elements of prime-power norm at split primes.
The existence of `α` follows from the finiteness of the class group. The numbers `ρ_p`, `γ_p` and
the sets of exponents are notation, and the sum for `γ_p` is a geometric series.


### `piPrime`

 The number `π_p`, as a complex number: `√-d = I * √d` if `p = d`, and `p` otherwise. 

### `coprime_primeNorm_sub_one`

 For primes `d` and `p`, the prime `p` is coprime to `q_p - 1`, where `q_p = primeNorm d p`. 

 ### The numbers `v(π_p)`, `ρ_p` and `γ_p` 

### `piPrimeValuation`

 The valuation `v(π_p)` of the number `π_p = piPrime d p`, with `v(p) = 1`: it is `1 / 2` if
`p = d`, and `1` otherwise (see `New.norm_piPrime`). 

### `varpiValuation`

 The number `ρ_p = v(π_p) / (q_p - 1)`, where `v(π_p) = piPrimeValuation d p` and
`q_p = primeNorm d p`. For primes `p` and `d ≡ 7 mod 8` it is `1 / (p - 1)`, `1 / (p² - 1)`,
`1 / (2 p - 2)` when `p` is split, inert, ramified in `ℚ(√-d)`. 

### `varpiValuation_le_one_div_sub_one`

 For primes `d` and `p`, the number `ρ_p = varpiValuation d p` is at most `1 / (p - 1)`. 

### `gammaPrime`

 The number `γ_p = 1 / (p - 1) - ρ_p`, where `ρ_p = varpiValuation d p`. For primes `p` and
`d ≡ 7 mod 8` it is `0`, `p / (p² - 1)`, `1 / (2 p - 2)` when `p` is split, inert, ramified in
`ℚ(√-d)`. 

### `gammaPrime_of_inert`

 If the prime `p` is inert, that is, `chiK d p = (p / d) = -1`, then `γ_p = p / (p² - 1)`. 

 ### The sets `I_p°` and `I_p` of exponents 

### `partnerExponents`

 The set `I_p°` of exponents at a prime `p`: the odd numbers if the Legendre symbol `chiK d p` is
`-1`, all numbers if `p = d`, and none otherwise; for `d ≡ 7 mod 8` these cases are `p` inert,
ramified, split in `ℚ(√-d)`. The partners of an infinite place `τ` are the places `-p ^ e τ`
(`New.Parameters.partner`) with `e` in this set. 

### `positivePartnerExponents`

 The set `I_p` of the positive elements of `I_p° = partnerExponents d p`: the odd numbers if
`chiK d p = -1`, all positive numbers if `p = d`, and none otherwise. 

### `one_sub_chiK_pow_div_two`

 For primes `d` and `p`, the number `(1 - χ_K(p) ^ e) / 2` is `v(π_p)` if `e ∈ I_p`, and `0`
otherwise. Here `χ_K(p) = chiK d p` is the Legendre symbol `(p / d)`,
`v(π_p) = piPrimeValuation d p` and `I_p = positivePartnerExponents d p`. 

### `hasSum_gammaPrime`

 For primes `d` and `p`, the number `γ_p = gammaPrime d p` (defined as
`1 / (p - 1) - varpiValuation d p`) equals the sum of `v(π_p) p⁻ᵉ` over
`e ∈ I_p = positivePartnerExponents d p`. Here `v(π_p) = piPrimeValuation d p` is `1/2` if `p = d`
and `1` otherwise. `I_p` consists of the positive odd numbers if `chiK d p = -1`, of all positive
numbers if `p = d`, and is empty otherwise (for `d ≡ 7 mod 8`: `p` inert, ramified, split in
`ℚ(√-d)`). 

### `hasSum_div_pow_positivePartnerExponents`

 For primes `d` and `p` and a real number `c`, the sum of `c p⁻ᵉ` over
`e ∈ I_p = positivePartnerExponents d p` is `c γ_p / v(π_p)`, where `γ_p = gammaPrime d p` and
`v(π_p) = piPrimeValuation d p`. 

 ### The norm and the valuation of `π_p` 

### `piPrime_mul_conj`

 For primes `p` and `d ≡ 7 mod 8` such that `p` does not split in `K = ℚ(√-d)`, that is,
with Legendre symbol `chiK d p = (p / d) ≠ 1`, the number `π_p = piPrime d p` (which is `√-d` if
`p = d` and `p` otherwise) has the norm `q_p = primeNorm d p`, which is `p ^ 2` if `p` is inert
and `p` if it ramifies. 

### `norm_piPrime`

 Under the embedding `ιₚ : ℂ →+* ℂ_[p]` given by a `PadicPlace p`, the number `π_p` (`√-d` if
`p = d`, else `p`) has valuation `piPrimeValuation d p`, which is `1 / 2` for `p = d` and `1`
otherwise. 

### `norm_piPrime_eq_rpow_pow`

 With `v` the valuation given by the `p`-adic embedding `ιₚ`, so that `‖ιₚ x‖ = p ^ (-v(x))`,
one has `v(π_p) = (q_p - 1) ρ_p`. Here `π_p = piPrime d p` is `√-d` if `p = d` and `p` otherwise,
`q_p = primeNorm d p` is `p ^ 2` if `p` is inert in `ℚ(√-d)` and `p` otherwise, and
`ρ_p = varpiValuation d p`, for a prime `d ≡ 7 mod 8`. 

### `piPrimeInt`

 The image `ιₚ π_p` of the number `π_p` in the ring of integers of `ℂ_p`, for the `p`-adic
place that is given by the instance `PadicPlace p`. 

### `piPrimeInt_dvd_natCast`

 In `valRingCp p`, the ring of integers of `ℂ_p`, the image `piPrimeInt d` of the number `π_p`
(`√-d` if `p = d`, and `p` otherwise; the prime `p` is implicit in the notation) divides `p`. 

 ## An element of prime-power norm at a split prime 

### `QuadField.star_ne_of_chiK_eq_one`

 Let `d ≡ 7 mod 8` and `p` be primes with Legendre symbol `chiK d p = (p / d) = 1`, and let `w`
be a prime of `K = QuadField d = ℚ(√-d)` that contains `p`. Then `w` differs from its complex
conjugate `star w`. Here `FinPlace` is the type of nonzero prime ideals of the ring of integers. 

### `exists_mul_conj_eq_pow`

 Let `d ≡ 7 mod 8` and `p` be primes with Legendre symbol `chiK d p = (p / d) = 1`, and let
`ιₚ : ℂ →+* ℂ_[p]` be the embedding given by a `p`-adic place. Then there are an exponent `h` and
a number `α` such that `h ≠ 0`, `α` lies in `quadInt d` (the ring of integers of `K = ℚ(√-d)`
inside `ℂ`), `α` has norm `p ^ h`, and `ιₚ (conj α)` is a unit: take a generator of the `h`-th
power of the prime of `K` that `ιₚ` induces. 
