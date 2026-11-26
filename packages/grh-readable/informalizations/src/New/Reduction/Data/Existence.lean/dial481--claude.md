---
{
  "module": "src/New/Reduction/Data/Existence.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Reduction/Data/Existence.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Reduction/Data/Existence.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Admissible data exist at every large x

For every large integer `x`, this file constructs the data `New.Data`. It builds the ranks and the
field, the places, the scales and the primes in turn.

## Main definitions and results

* `New.Parameters.IsAdmissibleData`: admissible data, with explicit values of the ranks and scales
  and any `b`-places and primes that have the required properties.
* `New.eventually_exists_data_of_isAdmissibleData`: at every large `x` such data are the fields
  (`New.Data.HasFields`) of the data `New.Data`.
* `New.eventually_exists_data`: admissible data exist at every large `x`.

Notions from other files:
* `P : Parameters` fixes `q₀` and the prime `d` with `K = ℚ(√-d)`; at the exponent `s` it gives
  `P.q₁ s = q₀ * towerDeg s`, where `towerDeg s = 3 l₀ 2 ^ s` and `l₀ = 3 ^ (⌊log₃ s⌋ + 4)` is, for
  `s ≥ 1`, the least power of `3` above `27 s`.
* `P.Φ s` is the set of infinite places of the field `E = P.E s`, a group identified with `(ℤ/q₁)ˣ`;
  `P.placeOfInt s ν` is the place of the class of `ν`, and `P.placeClass` reduces this class modulo
  a divisor of `q₁`.
* `P.IsSparse s L T`: no places `σ, τ, ρ` in `T` have `τ / σ ≡ ± ℓ ^ i` and `ρ / σ ≡ ± ℓ ^ j` modulo
  the part of `q₁` prime to `ℓ`, for a prime `ℓ ≤ L` and `0 < i < j < l₀`.
* `P.q₂ s = (q₀ d) ^ (s + 6)`; its square, written `q₂²`, is the modulus of the primes to be found.
* `P.logLevelMin s m κ M L` is `log N₋`, where `N₋ = κ̄ ^ m (M rd_E / 2π) ^ (m - 1) b ^ (-15 / 2)`,
  `κ̄` being the geometric mean of the weights `κ`, `rd_E` the root discriminant and `L = log b`.

## Relation to the literature

Known result: Behrend's construction for several equations at once. Source: Shapira, Behrend-type
constructions for sets of linear equations, Acta Arith. 2006 (after Behrend, PNAS 32, 1946); compare
Alon–Shapira, A characterization of easily testable induced subgraphs (2006), Lemma 4.1 (preprint
numbering). Form here: all weights up to a given bound are avoided at once, modulo an
integer, with a fixed number of digits and the explicit count of points on a sphere. This concerns
`exists_three_term_free`.



## Existence of admissible data at every large integer x

The ranks `m`, `r`, the exponent `s`, the field and the scales `x₁`, `b` come from `x`. The places
of weight `b` are `-g ^ e` with `g = 1 + 3 l₀ q₀` and `e` in a set of Behrend's type. The primes
`p₀`, `p₁` and `N` come from windows for primes in progressions, the element of norm `p₀ p₁` from
a pigeonhole argument in the class group of `K`, and the element of norm `N` from a sum of two
squares. The windows are those of `exists_prime_modEq_one_log_mem`, a consequence of the
Siegel–Walfisz theorem. That lemma needs an upper bound for the start of a window, so the upper
bound for `log N₋` is used as well.


### `eq_of_add_mul_eq_of_sum_sq_eq`

 A sphere is strictly convex: if three integer vectors of equal squared length satisfy
`(α + α') v = α u + α' w` with `α, α' > 0`, they are equal. 

### `exists_three_term_free`

 **Behrend's sets.** If `0 < L` and `(L H) ^ n ≤ o`, there is a set `S` of at least
`H ^ n / (n H ^ 2)` integers in `[0, o)` such that a congruence `(α + α') e₂ ≡ α e₁ + α' e₃`
modulo `o`, with `e₁, e₂, e₃ ∈ S`, `α, α' > 0` and `α + α' ≤ L`, forces `e₁ = e₂ = e₃`. 

### `Parameters.exists_orderOf_placeClass_eq`

 The infinite places `P.Φ s` of `E = P.E s` form the group `(ℤ/q₁)ˣ`, `q₁ = P.q₁ s`;
`P.placeOfInt s ν` is the place of the residue of an integer `ν` prime to `q₁`, and `P.placeClass`
reduces a place modulo a divisor of `q₁`. The place of `g = 1 + 3 l₀ q₀`, where `q₀ = P.q₀` and
`l₀ = 3 ^ (⌊log₃ s⌋ + 4)`, has order `2 ^ s` modulo some power `2 ^ (s + v)` that divides `q₁`. 

### `Parameters.placeClass_sq_eq`

 Let `y` be a place whose class modulo the part of `q₁` prime to the prime `ℓ` is `± ℓ ^ i`.
Then the square of its class modulo every divisor of `q₁` prime to `ℓ` is `ℓ ^ (2 i)`. 

### `modEq_orderOf_of_div_pow_eq`

 In a commutative group, `(g ^ e₂ / g ^ e₁) ^ (a + b) = (g ^ e₃ / g ^ e₁) ^ b` forces
`(a + b) e₂ ≡ a e₁ + b e₃` modulo the order of `g`. 

### `Parameters.exists_large_isSparse`

 If `(2 l₀ H) ^ n ≤ 2 ^ s` and `2 l₀ (L + 1) < 2 ^ s`, there is a set of at least
`H ^ n / (n H ^ 2)` places of class `-1` modulo `q₀` that is sparse for the primes `ℓ ≤ L`: it has
no places `σ, τ, ρ` with `τ / σ ≡ ± ℓ ^ i` and `ρ / σ ≡ ± ℓ ^ j`, `0 < i < j < l₀`, modulo the part
of `q₁` prime to `ℓ`. 

### `Parameters.exists_isSparse`

 **A large sparse set of places.** The infinite places `P.Φ s` of `E = P.E s` form the group
`(ℤ/q₁)ˣ`. Let `0 < n`, `1 ≤ W ≤ 2 ^ s ≤ W ^ n`, `(2 l₀) ^ n ≤ W`, `3 l₀ n 2 ^ n ≤ W ^ 3` and
`2 l₀ (L + 1) < 2 ^ s`. There is a set of at least `towerDeg s / W ^ 6` places of class `-1` modulo
`q₀` that is sparse for the primes `ℓ ≤ L`: it has no places `σ, τ, ρ` with `τ / σ ≡ ± ℓ ^ i` and
`ρ / σ ≡ ± ℓ ^ j`, `0 < i < j < l₀`, modulo the part of `q₁` prime to `ℓ`. 

### `exists_ne_isPrincipal_mul`

 Pigeonhole in the class group: given `h + 1` pairs `(I i, J i)` of finite places with
`I i * J i` principal, `h` the class number, there are `i ≠ j` with `I i * J j` principal. 

### `Parameters.IsPrincipalLevelPrime`

 The conditions on each of the two primes `p₀`, `p₁` of admissible data, whose product
`M = p₀ p₁` is called the principal level: `p` is a prime `≡ 1` modulo `q₂² = P.q₂ s ^ 2` in
`[b ^ 10, b ^ 11]`, where `b = exp L`. 

### `Parameters.IsPrincipalLevelPrime.prime`

 `p` is prime. 

### `Parameters.IsPrincipalLevelPrime.modEq_one`

 `p ≡ 1` modulo `q₂²`. 

### `Parameters.IsPrincipalLevelPrime.mem_Icc`

 `p` lies in `[b ^ 10, b ^ 11]`. 

### `Parameters.IsPrincipalLevelPrime.mul_mem_Icc`

 The product `M = p₀ p₁` of the two primes of the principal level lies in `[b ^ 20, b ^ 22]`,
where `b = exp L`. 

### `Parameters.exists_prime_pair_norm`

 The primes `p₀`, `p₁`. Let `0 < W` and `(2 h + 2) W ≤ L`, with `h` the class number of `K`.
If each window `[U, U + W]` with `10 L ≤ U ≤ 11 L` holds the logarithm of a prime `≡ 1` modulo
`q₂² = P.q₂ s ^ 2`, there are two distinct such primes `p₀`, `p₁` in `[b ^ 10, b ^ 11]`,
`b = exp L`, whose product is the norm `α ᾱ` of an integer `α` of `K`. 

### `Parameters.exists_mul_star_eq_prime`

 A prime `N ≡ 1` modulo `4` is a sum `a ^ 2 + b ^ 2` of two squares (Fermat), hence the norm
`y ȳ` of `y = a + b i` in the CM field `E = P.E s`, which contains `i`. 

### `exists_isLeast_pow`

 For `1 < q` and `1 < z`, the least power of `q` that is at least `z` is some `q ^ (e + 1)` with
`q ^ e < z`. 

### `exists_isLeast_two_pow_three_pow`

 The ranks at `x = exp y`, `y ≥ 2`. The least power `m` of `2` with `m ≥ √x` is at most `2 √x`,
and the least power `r` of `3` with `r ≥ x⁵` is at most `3 x⁵`. Both have a positive exponent, and
for `m = 2 ^ (e + 1)` the exponent `s = 22 (e + 1)` is at most `32 log x`. 

### `mul_rank_lt_two_pow`

 The inequality `2 l₀ (k t + 1) < 2 ^ s` for `k = r + 1 - m`, `t = 5 r` and
`l₀ = 3 ^ (⌊log₃ s⌋ + 4)`, the bound on the exponents in `Parameters.IsSparse`. It holds when
`0 < y`, `10⁶ y ≤ exp y`, `exp (y / 2) ≤ m`, `r ≤ 3 exp (5 y)`, `2 ^ s = m ^ 22` and
`l₀ ≤ 2592 y`. 

### `Parameters.q₂_sq_le`

 The modulus `q₂² = P.q₂ s ^ 2` is at most `W ^ n` if `2 ≤ y`, `0 < W`, `s ≤ 32 y` and
`99 q₀ d y ≤ n log W`. 

### `log_floor_exp_mem_Icc`

 For `0 ≤ W`, the logarithm of the integer `⌊exp W⌋` lies in `[W - 1, W]`. 

### `exists_isLeast_dvd_and_exp_lt`

 The least multiple of `q` that exceeds `exp U` has logarithm in `[U, U + 1]` if `q ≤ exp U`. 

### `pow_mul_exp_le_exp_pow_six`

 `W ^ n exp W ≤ exp (W ^ 6)` if `1 ≤ W` and `n + 1 ≤ W`. 

### `exists_isLeast_dvd_log_log_mem_Icc`

 The scale `b`, the least multiple of `q x₁` above `exp (W ^ 6)`, where `x₁ = ⌊exp W⌋` and
`q ≤ W ^ n`: `log b` lies in `[W ^ 6, W ^ 6 + 1]`, and `log log b` in `[6 log W, 6 log W + 1]`. 

### `Parameters.exists_isSparse_of_ranks`

 Let `2 ≤ y`, `0 < n`, `10⁶ y ≤ W ≤ exp (y / 2) ≤ m`, `r ≤ 3 exp (5 y)`,
`2 ^ s = m ^ 22 ≤ W ^ n`, `s ≤ 32 y`, `(5184 y) ^ n ≤ W` and `7776 y n 2 ^ n ≤ W`. At least
`towerDeg s / W ^ 6` places of class `-1` modulo `q₀` form a set that is sparse for the primes
`ℓ ≤ k t`, where `k = r + 1 - m` and `t = 5 r`: it has no places `σ, τ, ρ` with `τ / σ ≡ ± ℓ ^ i`
and `ρ / σ ≡ ± ℓ ^ j`, `0 < i < j < l₀`, modulo the part of `q₁` prime to `ℓ`
(`Parameters.IsSparse`). 

### `Parameters.exists_prime_log_mem_Icc_mul_star_eq`

 The level `N`. Let `E = P.E s = K(ζ_{q₁})` with `K = ℚ(√-d)`, `d = P.d` and `q₁ = P.q₁ s`. Let
`b = exp L` with `7 ≤ L` and `W ^ 2 ≤ L`, let `2 ≤ m`, let the weights `κ τ` at the infinite places
`τ` of `E` lie in `[1, b]` and `M` in `[b ^ 20, b ^ 22]`, and let `q₁ d ≤ b`. Let each window
`[U, U + W]` with `m L ≤ U ≤ 24 m L` hold the logarithm of a prime `≡ 1` modulo `q₂²`. There is such
a prime `N` with `log N₋ ≤ log N ≤ log N₋ + √L` and `N = y ȳ` for an integer `y` of `E`. 

### `ite_mul_div_mem_Icc`

 For any proposition `p`, the value `if p then b else x * b / x₁` (natural-number division) lies
in `[1, b]` if `1 ≤ x ≤ x₁ ≤ b`. 

 ### Admissible data 

### `Parameters.IsAdmissibleData`

 The admissible data at the integer `x` and the real `W`. The ranks `m`, `r`, the exponent `s`
and the scales `x₁ = ⌊exp W⌋` and `b` are determined by `x` and `W`; the set `T` of `b`-places (the
infinite places of `P.E s` that get the weight `b`), the
primes `p₀ = g 0`, `p₁ = g 1`, `N` and the elements `α`, `β` with `α ᾱ = p₀ p₁` and `β β̄ = N` are
any with the listed properties. 

### `Parameters.IsAdmissibleData.isLeast_m`

 `m` is the least power of `2` with `m ≥ √x`. 

### `Parameters.IsAdmissibleData.isLeast_r`

 `r` is the least power of `3` with `r ≥ x⁵`. 

### `Parameters.IsAdmissibleData.two_pow_eq`

 `s = 22 log₂ m`. 

### `Parameters.IsAdmissibleData.isLeast_b`

 `b` is the least multiple of `q₁ x₁` that exceeds `exp (W ^ 6)`. 

### `Parameters.IsAdmissibleData.placeClass_eq_neg_one`

 The `b`-places are `≡ -1` modulo `q₀`. 

### `Parameters.IsAdmissibleData.towerDeg_le`

 There are at least `towerDeg s / log b` of them. 

### `Parameters.IsAdmissibleData.sparse`

 The `b`-places are sparse for the primes up to `k t`, where `k = r + 1 - m` and `t = 5 r`. 

### `Parameters.IsAdmissibleData.levelPrime_prime`

 `p₀` and `p₁` are prime. 

### `Parameters.IsAdmissibleData.levelPrime_modEq_one`

 `p₀, p₁ ≡ 1` modulo `q₂²`. 

### `Parameters.IsAdmissibleData.levelPrime_injective`

 `p₀ ≠ p₁`. 

### `Parameters.IsAdmissibleData.levelPrime_mem`

 `p₀` and `p₁` lie in `[b¹⁰, b¹¹]`. 

### `Parameters.IsAdmissibleData.α_mul_star`

 The norm of `α` is `p₀ p₁`. 

### `Parameters.IsAdmissibleData.N_prime`

 The level `N` is prime. 

### `Parameters.IsAdmissibleData.N_modEq_one`

 `N ≡ 1` modulo `q₂²`. 

### `Parameters.IsAdmissibleData.log_N_mem`

 `log N₋ ≤ log N ≤ log N₋ + √(log b)`, for the weights `b` on `T` and `x b / x₁` elsewhere. 

### `Parameters.IsAdmissibleData.β_mul_star`

 `β` times its complex conjugate is `N`. 

### `Data.HasFields`

 The fields of the admissible data `D` are the given values, with `x₁ = ⌊exp W⌋`. The arguments
are those of `Parameters.IsAdmissibleData`. The heterogeneous equality `≍` is used where the type of
a field depends on `D.towerExp`. 

### `Data.HasFields.natX_eq`

 The length of the prime sum is `x`. 

### `Data.HasFields.natX₁_eq`

 The scale `x₁` is `⌊exp W⌋`. 

### `Data.HasFields.natB_eq`

 The scale `D.natB` is `b`. 

### `Data.HasFields.m_eq`

 The rank `D.m` is `m`. 

### `Data.HasFields.r_eq`

 The rank `D.r` is `r`. 

### `Data.HasFields.towerExp_eq`

 The exponent of the tower is `s`. 

### `Data.HasFields.bPlaces_heq`

 The set of `b`-places is `T`. 

### `Data.HasFields.levelPrime_eq`

 The primes `p₀`, `p₁` are `g 0`, `g 1`. 

### `Data.HasFields.piMBar_eq`

 The integer of `K` of norm `p₀ p₁` is `α`. 

### `Data.HasFields.N_eq`

 The level is `N`. 

### `Data.HasFields.piN_heq`

 The integer of `E` whose product with its conjugate is the level is `β`. 

### `Parameters.IsLargeScale`

 `W` is a large scale for `y` with exponent `n`: `W` is small against `x = exp y` and large
against the parameters, `n` and the multiples of `y` and `y ^ n` listed below; `n` is so large that
`q₂² ≤ W ^ n` for `s ≤ 32 y` (`Parameters.q₂_sq_le`). 

### `Parameters.IsLargeScale.log_W_le`

 `(e W ^ 6) ^ 100 ≤ x`. 

### `Parameters.IsLargeScale.const_le`

 `log W` is large against `P.constantBound`, a bound for the constants that depend on `q₀` and
  `d` only. 

### `Parameters.IsLargeScale.mul_y_le_W`

 `W` is large against `y`. 

### `Parameters.IsLargeScale.classNumber_le`

 `W` is large against the class number of `K`. 

### `Parameters.IsLargeScale.n_pos`

 `n` is positive. 

### `Parameters.IsLargeScale.add_one_le`

 `n` is small against `W`. 

### `Parameters.IsLargeScale.le_mul_log_W`

 `n log W` is large against `log q₂²`. 

### `Parameters.IsLargeScale.pow_le`

 Room for a set of Behrend's type. 

### `Parameters.IsLargeScale.mul_two_pow_le`

 The loss in the size of that set. 

### `Parameters.exists_eventually_isLargeScale`

 For `0 < ε < 1 / 100` there is an `n` such that `W = x ^ (ε / 6)` is a large scale for
`y = log x` with exponent `n` at every large integer `x`: `0 < n`, `100 (6 log W + 1) ≤ y`,
`99 q₀ d y ≤ n log W`, and `W` is at least `2 · 10⁶ y`, `(5184 y) ^ n`, `7776 y n 2 ^ n`, `n + 1`,
`2 h + 2` with `h` the class number of `K = P.K`, and `exp (10¹² c)`, where `c = P.constantBound`
bounds the constants that depend on `q₀ = P.q₀` and `d = P.d` only. 

### `one_le`

 A large scale `W` (`Parameters.IsLargeScale`) is at least `1`. 

### `hundred_le`

 If `W` is a large scale for `y` (`Parameters.IsLargeScale`), then `100 ≤ y`. 

### `q₂_sq_le`

 At a large scale `W`, the modulus `q₂² = P.q₂ s ^ 2` is at most `W ^ n` for `s ≤ 32 y`. 

### `q₁_mul_d_le`

 At a large scale `W`, `q₁ d ≤ W ^ n` for `s ≤ 32 y`, as `q₁ d` divides `q₂²`. 

### `two_pow_le`

 At a large scale `W`, `2 ^ s ≤ W ^ n` for `s ≤ 32 y`, as `2 ^ s` divides `q₁ d`. 

### `q₁_mul_d_le_exp`

 Let `W` be a large scale for `y` with exponent `n` under the parameters `P`
(`Parameters.IsLargeScale`). If `s ≤ 32 y` and `W ^ 6 ≤ L`, then `P.q₁ s * P.d ≤ exp L`. 

### `exists_isLeast_dvd_log_log_mem_Icc`

 Let the real `W` be a large scale for the real `y`, and let `s` be a natural number with
`s ≤ 32 y`. The least multiple `b` of `P.q₁ s * ⌊exp W⌋` above `exp (W ^ 6)` is positive, in the
form `exp (log b) = b`; it has `log b` in `[W ^ 6, W ^ 6 + 1]` and `log log b` in
`[6 log W, 6 log W + 1]`. 

### `Parameters.IsAdmissibleData.exists_hasFields`

 Let `W` be a large scale for `log x`, and let admissible data at `x` and `W` be given. A term
`D : Data P` bundles such objects and scales `x`, `x₁` with the inequalities `(log b) ^ 100 ≤ x`,
`x ^ 10⁶ ≤ x₁`, `x₁ ^ 10⁶ ≤ b`, `(log x₁) ^ 6 ≤ log b`, `10¹² P.constantBound ≤ log log b`,
`m ∈ [√x, 2 √x]` and `r ∈ [x⁵, 3 x⁵]`. There is a `D` whose fields equal the given objects, with
`x₁ = ⌊exp W⌋` (`Data.HasFields`). Moreover `W - 1 ≤ log x₁` and `W ^ 6 ≤ log b ≤ W ^ 6 + 1`. 

### `eventually_exists_data_of_isAdmissibleData`

 **Admissible data are fields of the data.** Let `0 < ε < 1 / 100`. For every large enough
integer `x`, any admissible data (`Parameters.IsAdmissibleData`) at `x` and `W = x ^ (ε / 6)` are
the fields of some `D : Data P` (`Data.HasFields`). This `D` has `x ^ (ε / 6) - 1 ≤ D.logX₁`, and
`D.logB` lies in `[x ^ ε, x ^ ε + 1]`. 

### `Parameters.IsLargeScale.exists_isAdmissibleData`

 Let `W` be a large scale for `y = log x` with exponent `n`. Let the windows `[U, U + W]` with
`W ≤ U ≤ W ^ (n + 7)` hold logarithms of primes `≡ 1` modulo the powers `(q₀ d) ^ k ≤ W ^ (n + 7)`,
`k > 1`. Then admissible data exist at `x` and `W`: the least powers `m ≥ √x` of `2` and `r ≥ x⁵` of
`3`; `s` with `2 ^ s = m ^ 22`; the least multiple `b > exp (W ^ 6)` of `P.q₁ s * ⌊exp W⌋`; a sparse
set `T` of at least `towerDeg s / log b` infinite places of `E = P.E s` of class `-1` modulo `q₀`;
distinct primes `g 0`, `g 1` in `[b¹⁰, b¹¹]` and a prime `N` with `log N` in the interval of length
`√(log b)` that starts at `P.logLevelMin`, all `≡ 1` modulo `(q₀ d) ^ (2 (s + 6))`; and integers `α`
of `K = P.K = ℚ(√-d)` and `β` of `E` with `α ᾱ = g 0 * g 1` and `β β̄ = N`. 

### `eventually_exists_data`

 **Existence of the data.** A term `D : Data P` consists of integer scales `x`, `x₁`, `b` with
`(log b) ^ 100 ≤ x`, `x ^ 10⁶ ≤ x₁` and `x₁ ^ 10⁶ ≤ b`, ranks `m`, `r`, the exponent `s` with
`2 ^ s = m ^ 22`, a large sparse set of infinite places of `E = K(ζ_{q₁})`, and primes `p₀ ≠ p₁`,
`N` of prescribed size and residue with `p₀ p₁ = α ᾱ` in `K = P.K` and `N = β β̄` in `E`. For
`0 < ε < 1 / 100` such a `D` exists at every large integer `x`, with `x₁ = ⌊exp (x ^ (ε / 6))⌋` and
`b` the least multiple of `q₁ x₁` that exceeds `exp (x ^ ε)`; `m` is the least power of `2` with
`m ≥ √x` and `r` the least power of `3` with `r ≥ x⁵`. Then `x ^ (ε / 6) - 1 ≤ log x₁` and
`x ^ ε ≤ log b ≤ x ^ ε + 1`. 
