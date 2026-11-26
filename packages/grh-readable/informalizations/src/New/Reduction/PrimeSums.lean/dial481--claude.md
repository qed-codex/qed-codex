---
{
  "module": "src/New/Reduction/PrimeSums.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Reduction/PrimeSums.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Reduction/PrimeSums.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Prime sums: main amount, expected value and total remainder

For admissible data `D` this file defines the main amount (`D.mainAmount`), the expected value
`s_main` (`D.mainPrimeSum`) and the total remainder `rem` (`D.totalRemainder`). It expresses the
total remainder through the remainders `R_q` of prime sums (`totalRemainder_eq`) and bounds `s_fin`,
`s_∞`, the direction amount and the main amount (`primeSum_le`, `jetSize_mem_Icc`,
`directionAmount_mem_Icc`, `le_mainAmount`). The modulus `q₀` is `P.q₀`.

Notions from other files:
* `lambdaKResidueClass d q n` is `Λ_K(n) = Λ(n) (1 - chiK d n)` if `n ≡ 1` modulo `q`, and `0`
  otherwise; `Λ` is the von Mangoldt function and `chiK d` is the Legendre symbol `(·/d)`.
* `primeRemainder d q z` is `R_q(z) = ∑_{n ≤ z} λ(n) (1 / n - 1 / z) - log z / φ(q) - c_q` with
  `λ = lambdaKResidueClass d q` and `c_q = (logDerivMean d q 1).re`. The function `logDerivMean d q`
  is `(∑_ψ (L'/L(quadTwist ψ d) - L'/L(ψ)) - 1) / φ(q)`, summed over the Dirichlet characters `ψ`
  modulo `q`, where `L = entireL` is the `L`-function made entire.
* `D.Φ` is the group of the `D.f` infinite places; `D.aPlaces` (`Φ_a`, the `a`-places) are those
  `≡ 1` modulo `q₀`, and `D.bPlaces` (`Φ_b`, the `b`-places) is a set of places `≡ -1` modulo `q₀`.
  The class of a place modulo `q₀` is its image under `P.placeClass`, and `-n τ` stands for
  `D.placeOfInt (-n) * τ`. The weight `κ = D.weight` is `b = a / x` on `Φ_b` and `a / x₁` elsewhere.
* `D.primeSum y τ` is `s_fin(y, τ) = ∑_{n ≤ a} Λ_K(n) (y / n - κ(-n τ))₊`.
* `D.jetSize j` is `s_∞(j) = log j! + j log (M / Ω)` with `M = D.M` and `Ω = P.bigOmega D.towerExp`,
  and the direction amount `D.directionAmount` is `∑_τ (s_∞(κ(τ)) - s_fin(κ(τ), τ))`.


### `lambdaKResidueClass_eq_ite`

 The function `lambdaKResidueClass d q` is the restriction of `Λ_K = lambdaKResidueClass d 1` to
the integers `n ≡ 1` modulo `q`. 

### `sum_lambdaKResidueClass_mul_posPart`

 For `0 < z ≤ A` with `A` an integer, the sum of `Λ_K(n) (A / n - A / z)₊` over the `n ≤ A` with
`n ≡ 1` modulo `q` equals `A (R_q(z) + log z / φ(q) + c_q)`. 

### `mainAmount`

 The main amount `m k ∑_τ (s_∞(κ(τ)) - s_fin(κ(τ), τ))`, that is, `m k` times the direction
amount. Here `m = D.m` is the number of theta lifts in each chain; the source has rank
`k = D.k = r + 1 - m` and the target has rank `r = D.r`. 

### `mainPrimeSum`

 The expected value `s_main = a (log (a / κ̄) + c₁)` of the mean of the prime sums `s_fin(a, τ)`
over the `a`-places `τ`, that is, the main term of this mean (see `sum_aPlaces_primeSum` and
`card_aPlaces_mul_mainPrimeSum`). Here `log κ̄` is the mean of `log κ(τ)` over all `f` places, `κ`
is the weight, and `c₁ = (logDerivMean P.d 1 1).re`. 

### `totalRemainder`

 The total remainder `rem = ∑ (s_fin(a, τ) - s_main)`, summed over the `a`-places `τ`; `s_fin` is
`D.primeSum` and `s_main` is `D.mainPrimeSum`. 

### `card_aPlaces`

 The set `D.aPlaces` of places `≡ 1` modulo `q₀` has `towerDeg towerExp = q₁ / q₀` elements. Here
`towerExp = D.towerExp` is the exponent with `2 ^ towerExp = m ^ 22` that selects the field
`E = P.E towerExp`, and `q₁ = P.q₁ towerExp` is the order of the root of unity that generates `E`
over `K`. 

### `f_eq_card_aPlaces_mul`

 The number `f` of all places is the number of `a`-places times `φ(q₀)`. 

### `mem_aPlaces_iff_of_mul_mem_bPlaces`

 If `-n τ` is a `b`-place, hence `≡ -1` modulo `q₀`, then `τ` is an `a`-place (`τ ≡ 1`) if and
only if `n ≡ 1` modulo `q₀`. 

### `card_filter_mem_bPlaces`

 As `τ` runs over the `a`-places `D.aPlaces`, the place `-n τ = D.placeOfInt (-n) * τ` lies in
`D.bPlaces` for `#D.bPlaces` values of `τ` if `n ≡ 1` modulo `q₀`, and for none otherwise. 

### `sum_aPlaces_lambdaKResidueClass_mul_posPart`

 The contribution of one integer `n` to the sum of the prime sums `D.primeSum D.a τ` over the
places `τ ≡ 1` modulo `q₀` (the set `D.aPlaces`). So every `τ` gives the term of weight `a / x₁`,
and if `n ≡ 1` modulo `q₀` there is one correction to the weight `a / x` for each place of
`D.bPlaces`. 

### `sum_aPlaces_primeSum`

 The sum over the `a`-places `τ` of the prime sums `D.primeSum a τ = s_fin(a, τ) = ∑_{1 ≤ n ≤ a}
Λ_K(n) (a / n - κ(-n τ))₊` is `a` times the remainders `#Φ_b (R_{q₀}(x) - R_{q₀}(x₁)) + #Φ_a R₁(x₁)`
plus `a` times the main terms `#Φ_a (log x₁ + c₁) + #Φ_b log (x / x₁) / φ(q₀)`. 

### `sum_log_weight`

 The sum of `log κ(τ)` over all `D.f` places `τ` is `f log (a / x₁) - #Φ_b log (x / x₁)`. This
holds since the weight `κ = D.weight` is `a / x` on the set `Φ_b = D.bPlaces` of `b`-places and
`a / x₁` elsewhere. 

### `card_aPlaces_mul_mainPrimeSum`

 Let `s_main = D.mainPrimeSum = a (log a - f⁻¹ ∑_τ log κ(τ) + c₁)`, the sum running over all `f`
places with weights `κ = D.weight`. Then `#Φ_a s_main` equals
`a (#Φ_a (log x₁ + c₁) + #Φ_b log (x / x₁) / φ(q₀))`, the main term of the sum of `D.primeSum a τ`
over `τ ∈ Φ_a` in `sum_aPlaces_primeSum`. 

### `totalRemainder_eq`

 The total remainder `∑_{τ ∈ Φ_a} (D.primeSum a τ - D.mainPrimeSum)` is
`a (#Φ_b (R_{q₀}(x) - R_{q₀}(x₁)) + #Φ_a R₁(x₁))`. 

### `lambdaKResidueClass_mul_posPart_le_ite`

 For `0 ≤ y ≤ a = D.a`, `n ≥ 1` and a place `σ` (an element of `D.Φ`) of weight
`κ(σ) = D.weight σ`, the term `Λ_K(n) (y / n - κ(σ))₊` is at most `2 y Λ(n) / n` for `n` up to the
cut-off `x₁ = D.x₁`, and at most `0` for `n > x₁` because `κ(σ) ≥ a / x₁`. 

### `primeSum_le`

 For `0 ≤ y ≤ a = D.a` and every place `τ` (an element of `D.Φ`) the prime sum `s_fin(y,
τ) = ∑_{1 ≤ n ≤ a} Λ_K(n) (y / n - κ(-n τ))₊` is at most `4 y log x₁`, as only `n ≤ x₁` count. 

### `primeSum_mem_Icc`

 For `0 ≤ y ≤ a` and every place `τ` the prime sum `D.primeSum y τ = ∑_{1 ≤ n ≤ a} Λ_K(n)
(y / n - κ(-n τ))₊` lies between `0` and `y log b`. 

### `jetSize_mem_Icc`

 For an integer `y ≤ a` the quantity `s_∞(y) = D.jetSize y = log y! + y log (M / Ω)` satisfies
`20 y log b ≤ s_∞(y) ≤ 25 y log b`. Here `M = D.M = p₀ p₁` is the principal level, a product of two
primes in `[b¹⁰, b¹¹]`, `Ω = P.bigOmega D.towerExp = exp (γ - Re L'/L(1, χ_K)) 2π / rd_E` with `γ`
Euler's constant and `rd_E` the root discriminant of `E`, and `log b = D.logB`. 

### `jetSize_sub_primeSum_mem_Icc`

 For a place `τ` of weight `y = D.weight τ`, the difference `s_∞(y) - s_fin(y, τ)` lies between
`y log b` and `25 y log b`. 

### `directionAmount_mem_Icc`

 The direction amount `D.directionAmount = ∑_τ (s_∞(κ(τ)) - s_fin(κ(τ), τ))`, summed over all `f`
places with weights `κ`, lies between `b #Φ_a` and `25 f b log b`. 

### `le_mainAmount`

 The main amount `m k ∑_τ (s_∞(κ(τ)) - s_fin(κ(τ), τ))` is at least `x⁴ f a`. Here
`m ∈ [√x, 2 √x]` is the number of theta lifts, `k = r + 1 - m` is the rank of the source
(`r ∈ [x⁵, 3 x⁵]` that of the target), `x` is the first cut-off, `b` is the weight on `D.bPlaces`
and `a = x b`. 

### `mainAmount_nonneg`

 The main amount `D.mainAmount` is nonnegative. 
