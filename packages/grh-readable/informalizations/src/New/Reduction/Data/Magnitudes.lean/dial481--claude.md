---
{
  "module": "src/New/Reduction/Data/Magnitudes.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Reduction/Data/Magnitudes.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Reduction/Data/Magnitudes.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Logarithmic bounds for the sizes of the data

The class `New.Data.HasLogBound D u F l` says `|F| ≤ exp l` for `u = true` (`New.Data.HasLogUpper`)
and `exp l ≤ F` for `u = false` (`New.Data.HasLogLower`). Instance search computes the exponent `l`
from the shape of `F`, and comparing exponents then proves inequalities between the numbers attached
to the data `D`. A table of the sizes is in `New.Reduction.Data.Sizes`.

## Main definitions and results

* `New.Data.HasLogBound.of_mem_Icc`: a quantity between two others inherits their exponents,
  weakened to a given one. `New.Data.HasLogBound.of_lower_of_upper` weakens the exponents of one
  quantity.
* `New.Data.lt_of_hasLogBound`, `New.Data.le_of_hasLogBound`, `New.Data.nat_lt_of_hasLogBound`,
  `New.Data.nat_le_of_hasLogBound`: an upper exponent of `F` below a lower exponent of `G` gives
  `F < G`, and so also `F ≤ G`. The comparison of exponents is a default argument, a linear problem
  in `log x`, `log x₁`, `log b`, `log log b`, `log log x₁` and `New.Parameters.constantBound` that
  `grind` decides from `New.Data.scale_inequalities`. So `D.le_of_hasLogBound` or
  `D.nat_le_of_hasLogBound` alone proves such an inequality.
* `New.Data.k_add_t_add_one_le_halfGap`: at the end, inequalities and parities of the ranks `m`,
  `k`, `r`, `t`, `n j` and of `halfGap`.

Notions from other files:
* `New.Data P`: the data for the parameters `P = (q₀, d)`, with `q₀` a modulus and `d` a prime,
  among them the scales `x`, `x₁`, `b` (`D.natX`, `D.natX₁`, `D.natB` as natural numbers) with their
  logarithms `logX`, `logX₁`, `logB`, the ranks `m`, `r`, the exponent `s = D.towerExp` with
  `2 ^ s = m ^ 22` and the primes `p₀`, `p₁` (`D.levelPrime`).
* `D.q₁ = q₀ * towerDeg s`: the order of the root of unity that generates the number field
  `E = P.E s` over `K = ℚ(√-d)`; `P.q₂ s = (q₀ d) ^ (s + 6)` is a multiple of `q₁ d`.
* `D.weight`: the weight at the places `D.Φ`; it is `b` on the set `D.bPlaces` of `b`-places and
  `offWeight = a / x₁` elsewhere, where `a = x b`.


### `HasLogBound`

 A bound on the size of the real `F` on a logarithmic scale: the upper bound `|F| ≤ exp l` if `u`
is `true` (see `hasLogUpper_iff`), the lower bound `exp l ≤ F` if `u` is `false` (see
`hasLogLower_iff`). An instance for general `u` gives both bounds; the exponent `if u then a else b`
is `a` in the upper bound and `b` in the lower bound. The inequality does not depend on `D`; the
argument lets instances and default proofs use the data. 

### `HasLogBound.out`

 The upper bound `|F| ≤ exp l` if `u` is `true`, the lower bound `exp l ≤ F` otherwise. 

### `le_constantBound`

 The constant `P.constantBound`, which bounds the constants that depend only on the parameters
`P` (a modulus `q₀ = P.q₀` and a prime `d = P.d`), is at least each of the four numbers `64`, `q₀`,
`d` and the totient `φ q₀`. 

### `scale_inequalities`

 The five inequalities between the scales of the data, as one statement. They say that
`10¹² P.constantBound ≤ log log b`, `(log b) ^ 100 ≤ x`, `x ^ 10⁶ ≤ x₁`, `x₁ ^ 10⁶ ≤ b` and
`(log x₁) ^ 6 ≤ log b`. 

### `cast_a`

 As a real number, `D.a` is the product of the scales `D.x` and `D.b`. 

### `q₁_mul_natX₁_dvd_a`

 `q₁ x₁` divides `a = x b`. Here `x₁ = D.natX₁` is the second scale of the data and
`q₁ = D.q₁` is the order of the root of unity that generates the field `E` of the data over `K`. 

### `cast_offWeight`

 The division in `offWeight = a / x₁` is exact, so `offWeight` is this quotient as a real
number. 

### `cast_natB`

 The natural number `D.natB` is the scale `D.b` as a real number. 

### `weight_eq_ite`

 At an infinite place `σ` of the number field `E` of the data (`D.Φ` is the type of these
places), the weight is `b` if `σ` lies in the set `D.bPlaces` of `b`-places and
`offWeight = a / x₁` otherwise. 

### `cast_weight`

 Let `σ` be an infinite place of the number field `E` of the data, let `x`, `x₁`, `b` be the
three scales of the data and `a = x b`. As a real number, the weight of `σ` is `a / x` if `σ` lies
in the chosen set `D.bPlaces` of places, the `b`-places, and `a / x₁` otherwise. 

### `weight_le_natB_add_offWeight`

 Every weight `D.weight σ` is at most `D.natB + D.offWeight`, the sum of its two possible values:
`D.natB` (the scale `b` as a natural number) and `D.offWeight`. 

### `q₁_dvd_weight`

 The weight `D.weight σ` of an infinite place `σ` of the number field `E` of the data is a
multiple of `q₁ = D.q₁`, the order of the root of unity that generates `E` over the imaginary
quadratic field `K = ℚ(√-d)`. 

### `liftWeight_eq`

 Let `σ` be an infinite place of the number field `E` of the data and `κ(σ) = D.weight σ` the
natural number that the data assign to it. The number `D.liftWeight j σ`, the weight at `σ` of the
character used in step `j` of the chain of theta lifts, is `κ(σ) + j Δ + Δ / 2`, where
`Δ = D.gap = 2 r ^ 8` and `Δ / 2 = D.halfGap`. 

### `levelPrime_modEq_one`

 The primes `p₀ = D.levelPrime 0`, `p₁ = D.levelPrime 1` are `≡ 1` modulo `q₁ d`. Here `q₀` and
`d` are the modulus and the prime of the parameters `P`, `s = D.towerExp` is the exponent of the
data with `2 ^ s = m ^ 22`, and `q₁ = P.q₁ s` is `q₀ * 3 ^ (Nat.log 3 s + 5) * 2 ^ s`. 

### `dvd_levelPrime_sub_one`

 For the exponent `s = D.towerExp` of the data, the square of `P.q₂ s = (q₀ d) ^ (s + 6)`
divides `p₀ - 1` and `p₁ - 1`, where `p₀`, `p₁` are the primes `D.levelPrime i`. 

### `r_odd`

 The rank `r` is odd, since it is a power of `3`. 

### `m_even`

 The rank `m` is even, since it is a power of `2` with positive exponent. 

 ### Upper and lower bounds, and the rules for arithmetic operations 

### `HasLogUpper`

 The upper bound `|F| ≤ exp l`; see `hasLogUpper_iff`. 

### `HasLogLower`

 The lower bound `exp l ≤ F`; see `hasLogLower_iff`. 

### `hasLogUpper_iff`

 `l` is an upper exponent of `F` if and only if `|F| ≤ exp l`. 

### `hasLogLower_iff`

 `l` is a lower exponent of `F` if and only if `exp l ≤ F`. 

### `HasLogBound.pos`

 A number with a lower bound `exp l` is positive. 

### `HasLogBound.of_mem_Icc`

 Let `G ≤ F ≤ H` with `exp l ≤ G` and `|H| ≤ exp l'`. The Boolean `u` selects the bound. If `u`
is `true` and `l' ≤ c`, then `c` is an upper exponent of `F`. If `u` is `false` and `c ≤ l`, then
`c` is a lower exponent of `F`. 

### `HasLogBound.of_lower_of_upper`

 Let `exp l ≤ F` and `|F| ≤ exp l'`. If `u` is `true` and `l' ≤ c`, then `|F| ≤ exp c`. If `u` is
`false` and `c ≤ l`, then `exp c ≤ F`. 

### `instance (priority`

 A non-zero natural number `A` lies between `exp 0` and `exp A`. 

### `instance (priority`

 A numeral `A ≥ 2` lies between `exp 0` and `exp A`. 

### `instance : HasLogBound D u 1 0`

 The exponent of `1` is `0`, in both directions. 

### `instance : HasLogBound D u (Real.exp c) c`

 The exponent of `exp c` is `c`, in both directions. 

### `instance : HasLogBound D u (F ^ A) (A * l)`

 Exponents are multiplied by `A` under taking `A`-th powers. 

### `instance : HasLogBound D u √F (l / 2)`

 Exponents are halved under taking square roots. 

### `hasLogBound_mul`

 Exponents of the same kind add under products: if `l` is an exponent of `F` and `l'` one of `G`,
then `l + l'` is an exponent of `F * G`. 

### `hasLogBound_add`

 For sums, the larger of the two exponents is a lower exponent of `F + G`, and that exponent plus
`1` is an upper exponent of `F + G`. 

### `instance [D.HasLogLower F l] : D.HasLogUpper F⁻¹ (-l)`

 The negative of a lower exponent of `F` is an upper exponent of `F⁻¹`. 

### `instance [D.HasLogUpper F l] [D.HasLogLower F l'] : D.HasLogLower F⁻¹ (-l)`

 The negative of an upper exponent of a positive `F` is a lower exponent of `F⁻¹`. 

### `instance [HasLogBound D u G⁻¹ l'] : HasLogBound D u (F / G) (l + l')`

 An exponent of `F` plus one of `G⁻¹` is one of `F / G`. 

### `instance [HasLogBound D u (A * B) l] : HasLogBound D u ↑(A * B) l`

 An exponent of the real product of `A` and `B` is one of the cast of `A * B`. 

### `instance [HasLogBound D u (A + B) l] : HasLogBound D u ↑(A + B) l`

 An exponent of the real sum of `A` and `B` is one of the cast of `A + B`. 

### `instance [HasLogBound D u (A ^ B) l] : HasLogBound D u ↑(A ^ B) l`

 An exponent of the real power `A ^ B` is one of the cast of `A ^ B`. 

### `instance [D.HasLogUpper (|F| + 1) c] : HasLogBound D u ⌈F⌉₊ (if u then c else l)`

 Let `l` be an exponent of `F` of kind `u` (the instance `HasLogBound D u F l` among the
variables) and `c` an upper exponent of `|F| + 1`. Then `⌈F⌉₊` has the upper exponent `c` if `u` is
`true`, and the lower exponent `l` otherwise. 

### `instance : HasLogBound D u D.logB (Real.log D.logB)`

 `log b` has the exponent `log log b`, in both directions. 

### `instance : HasLogBound D u D.logX₁ (Real.log D.logX₁)`

 `log x₁` has the exponent `log log x₁`, in both directions. 

### `instance : D.HasLogUpper D.towerExp (Real.log D.logX₁)`

 The exponent `s = D.towerExp`, which satisfies `2 ^ s = m ^ 22`, is at most `log x₁`, since
`s ≤ 32 log x` and `10⁶ log x ≤ log x₁`. 

### `hasLogUpper_of_abs_le`

 If `|F| ≤ exp l` and `|G| ≤ F`, then `|G| ≤ exp l`: an upper exponent of `F` is one of `G`. 

### `hasLogUpper_of_le_of_nonneg`

 If `|F| ≤ exp l` and `0 ≤ G ≤ F`, then `|G| ≤ exp l`: an upper exponent of `F` is one of
`G`. 

### `instance [D.HasLogUpper F l] : D.HasLogUpper |F| l`

 An upper exponent of `F` is one of `|F|`. 

### `instance [D.HasLogUpper F l] [D.HasLogUpper G l'] : D.HasLogUpper (F - G) (max l l' + 1)`

 The larger of the upper exponents of `F` and `G`, plus `1`, is an upper exponent of `F - G`. 

### `instance (priority`

 If `exp l' ≤ F ≤ exp l`, then `|log F| ≤ max l (-l')`. The upper exponent given here for
`log F` comes from the bound `max l (-l') ≤ 99 log b + exp (max l (-l') - 99 log b)`. 

### `hasLogUpper_of_le`

 If `|A| ≤ exp l` and `B ≤ A` for natural numbers, then `|B| ≤ exp l`: an upper exponent of `A`
is one of every `B ≤ A`. 

### `hasLogLower_of_le`

 If `exp l' ≤ G ≤ F`, then `exp l' ≤ F`: a lower exponent of `G` is one of `F`. 

 ### Comparing two quantities by their exponents 

### `lt_of_hasLogBound`

 If `|F| ≤ exp l`, `exp l' ≤ G` and `l < l'`, then `F < G`. 

### `le_of_hasLogBound`

 If `|F| ≤ exp l`, `exp l' ≤ G` and `l < l'`, then `F ≤ G`. 

### `nat_lt_of_hasLogBound`

 If natural numbers `A`, `B` satisfy `A ≤ exp l`, `exp l' ≤ B` and `l < l'`, then `A < B`. 

### `nat_le_of_hasLogBound`

 If natural numbers `A`, `B` satisfy `A ≤ exp l`, `exp l' ≤ B` and `l < l'`, then `A ≤ B`. 

### `instance : HasLogBound D u π (if u then 4 else 0)`

 `exp 0 ≤ π ≤ exp 4`. 

### `instance : HasLogBound D u D.m (D.logX / 2 + (if u then 2 else 0))`

 The number `m` of lifts lies between `x^(1/2)` and `2 x^(1/2)`. 

### `instance : HasLogBound D u D.r (5 * D.logX + (if u then 3 else 0))`

 The rank `r` lies between `x⁵` and `3 x⁵`. 

### `instance : D.HasLogUpper P.constantBound (Real.log D.logB)`

 The constant `P.constantBound` is at most `log b`, since `10¹² P.constantBound ≤ log log b`. 

 ### Sizes of the derived parameters 

### `ten_thousand_le_m`

 The rank `m` is at least `10000`. 

### `r_add_one`

 `r + 1 = k + m`, as the subtraction in `k = r + 1 - m` is exact. 

### `k_le_r`

 The rank `k = r + 1 - m` is at most the rank `r`. 

### `instance : HasLogBound D u D.k (5 * D.logX + (if u then 3 else -2))`

 The rank `k` lies between `e⁻² x⁵` and `e³ x⁵`. 

### `instance : HasLogBound D u D.t (5 * D.logX + (if u then 8 else 0))`

 The number `t = 5 r` lies between `x⁵` and `e⁸ x⁵`. 

### `instance [HasLogBound D u (D.m ^ 22) l] : HasLogBound D u (ofNat(2) ^ D.towerExp) l`

 The exponents of `m ^ 22` are those of `2 ^ s`, for the exponent `s = D.towerExp` of the data,
which satisfies `2 ^ s = m ^ 22`. 

### `instance : HasLogBound D u (towerDeg D.towerExp) (11 * D.logX + (if u then Real.log D.logB / 5 else 0))`

 `x¹¹ ≤ towerDeg s ≤ x¹¹ (log b)^{1/5}`, where `s = D.towerExp` and
`towerDeg s = 3 ^ (Nat.log 3 s + 5) * 2 ^ s` is the ratio `q₁ / q₀` of the orders of the roots of
unity. 

### `hasLogBound_f`

 `x¹¹ ≤ f ≤ exp P.constantBound * x¹¹ (log b)^{1/5}` for the number `f` of infinite places of
the number field `E = P.E D.towerExp` of the data. 

### `instance {S : Finset D.Φ} [D.HasLogUpper D.f l] : D.HasLogUpper #S l`

 An upper exponent of the number `f` of infinite places of `E` is one of `#S` for every set `S`
of such places. 

### `instance : HasLogBound D u (D.n D.m) (5.5 * D.logX + (if u then 12 else 0))`

 The last rank `n m = k + m (t + 1)` lies between `x^{5.5}` and `e^{12} x^{5.5}`. 

### `instance (i : Fin 2) : HasLogBound D u (D.levelPrime i) ((if u then 11 else 10) * D.logB)`

 The primes `p₀`, `p₁` lie between `b¹⁰` and `b¹¹`. 

### `M_mem_Icc`

 `b²⁰ ≤ M ≤ b²²` for `M = p₀ p₁`. 

### `instance : HasLogBound D u D.M ((if u then 22 else 20) * D.logB)`

 `D.M`, the product `p₀ p₁` of the two primes `D.levelPrime i`, lies between `b²⁰` and `b²²`. 

### `instance : HasLogBound D u D.halfGap (40 * D.logX + (if u then 25 else 0))`

 The half-gap `halfGap = r ^ 8` lies between `x⁴⁰` and `e²⁵ x⁴⁰`. 

### `instance : HasLogBound D u D.gap (40 * D.logX + (if u then 27 else 0))`

 The gap `Δ = 2 r ^ 8` lies between `x⁴⁰` and `e²⁷ x⁴⁰`. 

### `instance : HasLogBound D u D.a (D.logB + D.logX)`

 `a = x b` has the exponent `log b + log x`. 

### `instance : HasLogBound D u D.natB D.logB`

 The weight `D.natB` at the `b`-places, which is the scale `b`, has the exponent `log b`. 

### `instance : HasLogBound D u D.offWeight (D.logB - D.logX₁ + D.logX)`

 `offWeight = a / x₁` has the exponent `log b - log x₁ + log x`. 

### `instance {κ : Type*} {S : Finset κ} {v : κ → ℝ} [D.HasLogUpper #S l] [hv : ∀ y : κ, D.HasLogUpper (v y) l'] : D.HasLogUpper (∑ y ∈ S, v y) (l + l')`

 If `l` is an upper exponent of `#S` and `l'` one of every term `v y`, then `l + l'` is an upper
exponent of `∑ y ∈ S, v y`. 

### `instance [D.HasLogUpper (|log F| + |log G|) l] : D.HasLogUpper (Real.log (F * G)) l`

 An upper exponent of `|log F| + |log G|` is one of `log (F * G)`, also if `F` or `G` is zero. 

### `instance [D.HasLogUpper (A * log F) l] : D.HasLogUpper (Real.log (F ^ A)) l`

 An upper exponent of `A log F` is one of `log (F ^ A)`. 

### `instance [D.HasLogUpper (A * Real.log A) l] : D.HasLogUpper (Real.log A !) l`

 An upper exponent of `A log A` is one of `log A!`. 

 ### Inequalities and parities of the ranks 

### `hundred_mul_m_le_k`

 The rank `k = r + 1 - m` is at least `100 m`, for the number `m` of lifts. 

### `k_pos`

 The rank `k = r + 1 - m` is positive. 

### `n_mono`

 The ranks `n j = k + j (t + 1)` increase with `j`. 

### `k_even`

 `k = r + 1 - m` is even, as `r` is odd and `m` is even. 

### `t_odd`

 `t = 5 r` is odd, as `r` is. 

### `r_add_six_le_t`

 `r + 6 ≤ t`, as `t = 5 r` and `r` is a positive power of `3`. 

### `k_add_t_add_one_le_halfGap`

 The number `k + t + 1` is at most the half-gap `halfGap = r ^ 8`. 
