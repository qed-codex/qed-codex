---
{
  "module": "src/New/Derivatives/Sharpness/NearPairs.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Derivatives/Sharpness/NearPairs.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Derivatives/Sharpness/NearPairs.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Near pairs of `b`-places and the losses in the sharpness bound

This file studies places at a prime `p` that does not split in `K = ℚ(√-d)`, their partners, and the
`b`-places among them. A near pair is a `b`-place whose partner at an exponent `e < l₀ / 2` in `I_p`
is a `b`-place; `I_p` is the set of odd numbers, or of all `e ≥ 1` if `p = d`. For non-split `p ≤ k`
the `b`-places are sparse along the powers `(-p) ^ j` with `j < l₀`. For `p = d` there are no near
pairs. Writing `v` for the `p`-adic valuation, the file then bounds the losses in the sharpness
bound: for `p ≤ k` the terms of the sums `R_τ = D.partnerMinSum p τ` not coming from a near pair are
covered by `v(B)` for a product `B` of consecutive integers.

Notions from other files:
* `New.Data P`: the data over the parameters `P = (q₀, d)`, with the size parameters `b`, `x`, `x₁`,
  `k`, the exponent `s` and the group `D.Φ` of infinite places of the field `E`.
* `l₀ = New.l₀ D.towerExp`: the least power of `3` above `27 s`, where `2 ^ s = m ^ 22`.
* `D.bPlaces`, `D.weight`: the set of `b`-places and the weight `κ` of a place, equal to `b` at the
  `b`-places and to `a / x₁` elsewhere, where `a = x b`.
* `D.placeOfInt ν`: the place named by the integer `ν`; the partner of `τ` at the exponent `e` is
  `P.partner D.towerExp p e τ = D.placeOfInt (-p ^ e) * τ`.
* `P.placeClass`: the class of a place modulo a divisor of `q₁ = towerDeg s * q₀`.
* `chiK d`: the character `χ_K = (· / d)`; `p` does not split in `K` if `χ_K(p) ≠ 1`.
* `positivePartnerExponents d p`, `piPrimeValuation d p`, `gammaPrime d p`: the set `I_p`, which is
  empty if `p` splits, and the numbers `v(π_p)` and `γ_p = v(π_p) ∑_{e ∈ I_p} p⁻ᵉ`.

## Main definitions and results

* `New.Data.summable_posPart_sub_weight`: the series in the predicted valuation `S_p` converges.
* `New.Data.notMem_bPlaces_of_two_partners`: sparseness of the `b`-places along the powers of `-p`.
* `New.Data.IsNearPair.exponent_unique`, `New.Data.IsNearPair.eq_and_eq_of_partner_eq`,
  `New.Data.IsNearPair.end_ne_start`: for non-split `p ≤ k` no place occurs twice among the starts
  and ends of near pairs; two pairs that share a place contradict sparseness.
* `New.Data.lossProduct`: a product `B` of `n♯ = ⌈6 b / k⌉` consecutive integers, the last ones up
  to `l` if `n♯ ≤ l`, with `v(n♯!) ≤ v(B)` and `v(l!) ≤ v((l - n♯)₊!) + v(B)`.
* `New.Data.mul_sum_weight_sub_localPrimeSumTotal`: `γ_p |κ| - S_p = v(π_p) ∑ R_τ`, where `|κ|` is
  the sum of the weights.
* `New.Data.partnerMinSum_le`, `New.Data.error_le_padicValNat_lossProduct`: for `p ≤ k` the terms of
  `R_τ` other than that of a near pair are covered by `v(B)`.

## Relation to the literature

Legendre's formula for `v(n!)` is classical.


 ## Partners of places at a non-split prime

For `p = d` a place and its partner lie in different classes modulo `q₀`. For a non-split `p ≤ k`
the `b`-places are sparse along the powers of `-p`.


### `ne_d_of_placeClass_eq`

 If the place `-p ^ e σ` has the same class modulo `q₀` as the place `σ`, then `p` is not the
prime `d` with `K = ℚ(√-d)`. The infinite places of `E` form the group `(ℤ/q₁)ˣ`. 

### `summable_posPart_sub_weight`

 The series of `(y / p ^ e - κ(-p ^ e σ))⁺` over `e ∈ I_p = positivePartnerExponents P.d p` (the
odd numbers if `p` is inert, all `e ≥ 1` if `p = d`, none if `p` splits) converges; `κ = D.weight`
is the weight of a place. 

### `notMem_bPlaces_of_two_partners`

 Sparseness along the powers of `-p`: for a prime `p ≤ k = D.k` that does not split in
`K = ℚ(√-d)`, that is `χ_K(p) = chiK P.d p ≠ 1`, and `0 < i < j < l₀`, the places `σ`, `(-p) ^ i σ`,
`(-p) ^ j σ`, distinct or not, are not all `b`-places. 

 ## Near pairs 

### `IsNearPair`

 `(τ, e)` is a near pair with start `τ` and end `-p ^ e τ`: the exponent `e` lies in `I_p` (odd
if `p` is inert, positive if `p = d`), `e < l₀ / 2`, and both places are `b`-places. 

### `IsNearPair.exponent_mem`

 The exponent lies in `I_p`. 

### `IsNearPair.two_mul_lt`

 The exponent is less than `l₀ / 2`. 

### `IsNearPair.start_mem`

 The start is a `b`-place. 

### `IsNearPair.end_mem`

 The end is a `b`-place. 

### `IsNearPair.ne_d`

 For `p = d` there are no near pairs, as all `b`-places have the same class modulo `q₀`. 

### `IsNearPair.inert_and_odd`

 Near pairs occur only at inert primes, and their exponents are odd, as there are none for
`p = d`. 

### `IsNearPair.partner_eq`

 The end `-p ^ e τ` of a near pair `(τ, e)` is `(-p) ^ e τ`, as `e` is odd. 

### `IsNearPair.pow_mul_mem`

 The end of a near pair, written as `(-p) ^ e τ`, is a `b`-place. 

### `IsNearPair.exponent_unique`

 For a prime `p ≤ D.k` that does not split in `K = ℚ(√-d)`, that is `χ_K(p) ≠ 1`, near pairs
`(τ, e)`, `(τ, e')` with the same start have the same exponent. 

### `IsNearPair.eq_and_eq_of_partner_eq`

 For a prime `p ≤ k = D.k` that does not split in `K = ℚ(√-d)`, two near pairs `(τ, e)`,
`(τ', e')` with the same end are equal. 

### `IsNearPair.end_ne_start`

 For a prime `p ≤ D.k` that does not split in `K = ℚ(√-d)`, that is `χ_K(p) ≠ 1`, the end
`-p ^ e τ` of a near pair `(τ, e)` is not the start `τ'` of a near pair `(τ', e')`. 

 ## The losses allowed in the sharpness bound 

### `padicValNat_mono_of_dvd`

 The `p`-adic valuation is monotone for divisibility of nonzero natural numbers. 

### `padicValNat_factorial_eq_div_add`

 One step of Legendre's formula: for the `p`-adic valuation `v = padicValNat p`,
`v(n!) = ⌊n / p⌋ + v(⌊n / p⌋!)`. 

### `div_sub_one_le_padicValNat_factorial`

 For a prime `p`, the first term of Legendre's formula gives `n / p - 1 ≤ v(n!)`, with
`v = padicValNat p` and `n / p` taken as real division. 

### `lossFactorCount`

 The number `n♯ = ⌈6 b / k⌉` of factors given up at each place, for the numbers `b` and `k` of
the data `D`. 

### `lossProduct`

 The product `B = (l⁻ + 1) ⋯ (l⁻ + n♯)` of the `n♯` integers after `l⁻ = (l - n♯)₊`, where
`n♯ = D.lossFactorCount`. 

### `padicValNat_factorial_lossFactorCount_le`

 `v(n♯!) ≤ v(B)` for the `p`-adic valuation `v = padicValNat p`, as the product
`B = D.lossProduct l` of `n♯ = D.lossFactorCount` consecutive integers is a multiple of `n♯!`. 

### `padicValNat_factorial_le_add_lossProduct`

 `v(l!) ≤ v(l⁻!) + v(B)` with `v = padicValNat p`, for `l⁻ = (l - n♯)₊`, `n♯ = D.lossFactorCount`
and the product `B = D.lossProduct l` of the `n♯` integers after `l⁻`, as `l!` divides
`(l⁻ + n♯)! = l⁻! B`. 

### `x_pow_le_lossFactorCount`

 `x ^ 42 ≤ n♯ = ⌈6 b / k⌉` for the numbers `x`, `b` and `k` of the data `D`, as `b` is far larger
than `x` and `k`. 

### `padicValNat_factorial_mem_Icc_of_le`

 Legendre's formula up to `O(log b)`: for `n ≤ 2 b` and `p ≥ 3`, the `p`-adic valuation
`v(n!) = padicValNat p n!` lies between `n / (p - 1) - (log b + 2)` and `n / (p - 1)`; here `b` is
the size parameter of the data `D` and `D.logB = log b`. 

### `padicValNat_factorial_add_add_le`

 For `p ≥ 3` and `n₁ + n₂ + n₃ ≤ 2 b`, the multinomial coefficient
`(n₁ + n₂ + n₃)! / (n₁! n₂! n₃!)` has valuation at most `3 (log b + 2)`.

This is a consequence of Legendre's formula for the `p`-adic valuation of factorials, applied
through two-sided bounds on `v(n!)` for `n ≤ 2 b`. 

### `lossFactorCount_div_sub_one_le`

 `n♯ / p - 1 ≤ v(n♯!) ≤ v(B)` for the `p`-adic valuation `v = padicValNat p`,
`n♯ = D.lossFactorCount` and the product `B = D.lossProduct l` of `n♯` consecutive integers. 

### `partnerMinTerm`

 The term `min (κ(τ) / p ^ e) (κ(-p ^ e τ))` for `e ∈ I_p = positivePartnerExponents P.d p`, and
`0` for the other `e`; `κ` is the weight of a place. 

### `partnerMinSum`

 The sum `R_τ` of `min (κ(τ) / p ^ e) (κ(-p ^ e τ))` over `e ∈ I_p` (the odd numbers if `p` is
inert, all `e ≥ 1` if `p = d`); `κ` is the weight of a place. 

### `partnerMinTerm_le_div`

 Each term `D.partnerMinTerm p τ e` is at most `κ(τ) / p ^ e`, where `κ(τ) = D.weight τ` is the
weight of `τ`. 

### `mul_sum_weight_sub_localPrimeSumTotal`

 The identity `γ_p |κ| - S_p = v(π_p) ∑ R_τ`, the last sum over the infinite places `τ` of `E`.
The weights are `κ = D.weight`, with sum `|κ|`. Then `S_p = D.localPrimeSumTotal p`, the predicted
valuation, is the sum over `τ` of `v(π_p) ∑ (κ(τ) / p ^ e - κ(-p ^ e τ))⁺` over `e ∈ I_p`, and
`R_τ = D.partnerMinSum p τ` is the sum of `min (κ(τ) / p ^ e) (κ(-p ^ e τ))` over the same `e`. 

### `weight_of_notMem`

 Off the `b`-places the weight of a place is `a / x₁`. 

### `weight_of_mem`

 A `b`-place has weight `a / x = b`, as `a = x b`. 

### `partnerMinTerm_add_le`

 For any `n` and `e`, the term of `R_τ` with exponent `e + n` is at most `b / (p ^ n 2 ^ e)`, the
general term of a geometric series with sum `2 b / p ^ n`. The term at an exponent `i` is
`D.partnerMinTerm p τ i`. 

### `summable_partnerMinTerm`

 The series of the terms `D.partnerMinTerm p τ e` over `e` converges, by comparison with a
geometric series. 

### `tsum_partnerMinTerm_add_le`

 Let `n ≥ l₀ / 2`, where `l₀ = l₀ D.towerExp` is the least power of `3` above `27 D.towerExp`.
Then the terms `D.partnerMinTerm p τ e`, `e ≥ n`, add up to at most `2 b / (k p)`. 

### `partnerMinTerm_le_of_not_isNearPair`

 If `e < l₀ / 2` and `(τ, e)` is not a near pair, then the term `D.partnerMinTerm p τ e` is at
most `a / x₁`. This term is `min (κ(τ) / p ^ e) (κ(-p ^ e τ))` if `e` lies in the set `I_p` and `0`
otherwise. 

### `partnerMinSum_le`

 Let `c ≥ 0`, and suppose that a near pair `(τ, e)` can occur only for `e = e₀`, and that
`κ(τ) / p ^ e₀ ≤ c + 1` if it occurs. Then `R_τ ≤ c + 1 + l₀ a / x₁ + 2 b / (k p)`: the term of the
near pair is at most `c + 1`, each other term with `e < l₀ / 2` at most `a / x₁`, and the rest add
up to at most `2 b / (k p)`. 

### `error_le_padicValNat_lossProduct`

 For a prime `p ≤ k` and any `l`, the errors at one place add up to at most
`3 b / (k p) ≤ n♯ / p - 1 ≤ v(B)`. There are three errors: `3 (log b + 2) + x ^ 42 + 1`, which is at
most the weight `a / x₁` off the `b`-places; `l₀` times that weight; and `2 b / (k p)`. 
