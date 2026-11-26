---
{
  "module": "src/New/UpperBound/Size/Estimates.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Size/Estimates.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Size/Estimates.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Numerical inequalities between the parameters of the data

This file proves explicit identities and inequalities between the parameters of the data `D`,
which are used to bound heights and indices. It groups the von Mangoldt sum prime by prime,
bounds the rows of the diagrams and the size of jets, computes the norm of `D.piMBar`, bounds the
number of classes at levels that contain a principal level, and bounds the sum of the allowed
losses. Here `s_p(y, σ)` is `New.Data.localPrimeSum p y σ`, and `κ(τ)` is the weight `D.weight τ`
of an infinite place `τ` (not the column count `D.columnCount τ h`).

## Main definitions and results

* `New.Data.localPrimeSum_eq_tsum`, `New.Data.primeSum_eq_sum_localPrimeSum`: the local sum at `p`
  as a sum over the powers of `p`, and the von Mangoldt sum `New.Data.primeSum` grouped prime by
  prime.
* `New.Data.card_stdClasses_le_exp_mul_log`, `New.Data.card_stdClasses_le_exp`: bounds for the
  number of classes of the definite unitary group at a level `K` that contains a given principal
  level.
* `New.Data.sum_allowedLoss_mul_log_le`: the losses `New.Data.allowedLoss p`, weighted by `log p`,
  add up to at most `New.Data.errorUnit`.

Notions from other files:
* `New.StdClasses K`: the double cosets `Γ \ G_f / K` of the finite adelic unitary group `G_f` of
  the form `∑ x_i \bar x_i` by its rational points `Γ` and a subgroup `K`.
* `New.Data`: the parameters `x`, `x₁`, `a`, `b`, `m`, `N`, … of the construction; `D.E` is its CM
  field, which contains `P.K = ℚ(√-d)` and has `D.f` infinite places.
* `New.Data.loss`: `f a (log b)² / p`, times `m` if `p ≡ ±1` mod `m`.

## Relation to the literature

See `Lib.Adelic.Reduction.FiniteVolume` for sources. See
`New.UpperBound.Divisibility.LocalDivisibility` for related work.


 ### The von Mangoldt sum, prime by prime 

### `smallNonsplitPrimes`

 The set of primes `p < x₁` with Legendre symbol `(p / d) ≠ 1`, that is the primes below `x₁`
that do not split in `K = ℚ(√-d)`. 

### `localPrimeSum_eq_tsum`

 The admissible data `D : Data P` give a CM field `E = D.E`, a modulus `q₁`, the group `D.Φ` of
infinite places of `E`, identified with `(ℤ/q₁)ˣ`, and a weight `κ = D.weight` on `D.Φ`. For an
integer `ν`, `D.placeOfInt ν` is the place of the class of `ν` if `ν` is prime to `q₁`, and the
identity place otherwise; `ν σ` stands for the product `D.placeOfInt ν * σ` of places. Let `χ_K` be
the Legendre symbol modulo the prime `d = P.d`, attached to `K = ℚ(√-d)`. For a prime `p`, a real
`y` and a place `σ`, the local term `s_p(y, σ) = D.localPrimeSum p y σ` equals `∑_{e ≥ 1} (1 - χ_K(p
^ e)) / 2 · (y / p ^ e - κ(-p ^ e σ))₊`. 

### `posPart_div_sub_weight_eq_zero`

 For `y ≤ a` and `x₁ ≤ t` we have `(y / t - κ(τ))₊ = 0`, since the weight `κ(τ)` of every
infinite place `τ` is at least `a / x₁`. 

### `localPrimeSum_eq_zero`

 For a natural number `p ≥ x₁` and `y ≤ a` the local term `D.localPrimeSum p y σ` vanishes,
since every weight is at least `a / x₁`. 

### `gain_eq_zero`

 The gain `D.gain p`, which is `m` times a sum of local terms `s_p`, is zero if `p` splits in
`K`, that is `χ_K(p) = 1`, or if `p ≥ x₁`. 

### `primeSum_eq_sum_localPrimeSum`

 The prime sum `D.primeSum y σ = ∑_{1 ≤ ν ≤ a} Λ(ν) (1 - χ_K(ν)) (y / ν - κ(-ν σ))₊`, grouped by
primes. The admissible data `D` give an integer `a`, a real number `x₁` and a weight `κ ≥ a / x₁` on
the group `D.Φ` of infinite places of the field `D.E`, identified with `(ℤ/q₁)ˣ`. Here `-ν σ` is
`D.placeOfInt (-ν) * σ`, where `D.placeOfInt (-ν)` is the place of the class of `-ν` if `ν` is prime
to `q₁` and the identity place otherwise, and `χ_K` is the Legendre symbol modulo the prime
`d = P.d`. For `y ≤ a` the terms with `ν ≥ x₁` vanish, and for `U ≥ x₁` the sum is that of
`2 s_p(y, σ) log p` over the primes `p < U`. 

### `localPrimeSumTotal_nonneg`

 The number `D.localPrimeSumTotal p`, the sum over the infinite places `τ` of the local terms
`D.localPrimeSum p (D.weight τ) τ`, is nonnegative. 

### `sum_localPrimeSumTotal_mul_log_le`

 The admissible data `D` give an integer `a` and a weight `κ = D.weight` on the group `D.Φ` of
infinite places of the field `D.E`, identified with `(ℤ/q₁)ˣ`. Let `χ_K` be the Legendre symbol
modulo the prime `d = P.d`, and for a place `τ` put `g_τ(ν) = (1 - χ_K(ν)) (κ(τ) / ν - κ(-ν τ))₊`.
For a prime `p` the number `F(p) = D.localPrimeSumTotal p` is `∑_τ ∑_{e ≥ 1} g_τ(p ^ e) / 2`, and
`D.primeSum κ(τ) τ` is `∑_{1 ≤ ν ≤ a} Λ(ν) g_τ(ν)`. For every finite set `T` of primes,
`∑_{p ∈ T} 2 F(p) log p ≤ ∑_τ D.primeSum κ(τ) τ`. 

 ### Rows of the diagrams, the norm of `piMBar` and the size of jets 

### `rowMainLength`

 The main length of row `i` of a lift diagram at the place `τ`: the number `D.columnCount τ 1` of
columns of height `1` for the first row (`i = 0`), the weight `κ(τ) = D.weight τ` for the next
`k - 1` rows, and `0` for the others. 

### `rowSlack`

 The number of boxes by which row `i` of a lift diagram may exceed its main length:
`b + offWeight + halfGap ^ 2` for the first row (`i = 0`) and `halfGap ^ 2` for the others. Here
`b = D.natB`, `offWeight = ⌊a / ⌊x₁⌋⌋` and `halfGap = D.r ^ 8` is half the gap `D.gap`. 

### `diagramWeight_le_rowMainLength_add_rowSlack`

 The admissible data `D` give the number `m` of lifts, the rank `k` of the first space, index
sets `D.X j` of sizes `n_j = k + j (t + 1)`, and a weight `κ = D.weight` on the set `D.Φ` of
infinite places of the field `D.E`, with values at least `a / x₁`. For a place `τ` the number
`D.columnCount τ h` is the number of columns of height `h` in the highest weight at `τ` of the forms
on the definite space of rank `n_j`. Let `j < m`, and take the Young diagram at `τ` with these
columns for all `h < n_{j+1}`. Then row `i`, counted from `0`, has length at most
`D.rowMainLength τ i + D.rowSlack i`. 

### `norm_map_star_piMBar_sq`

 The integer `D.piMBar` of `K ⊆ ℂ` has norm `M = D.M`, so the image of its conjugate under any
automorphism `σ` of `ℂ` has squared absolute value `M`. 

### `jetSize_le_add`

 Let `M = D.M = p₀ p₁` be the product of the two level primes of the data, let `E = D.E` and let
`Ω = P.bigOmega D.towerExp = exp (γ - Re L'/L(1, χ_K)) · 2π / rd_E`, with `γ` Euler's constant and
`rd_E` the root discriminant of `E`. For `l ≤ r + e` the jet size
`D.jetSize l = log l! + l log (M / Ω)`, which measures a derivative of order `l`, is at most
`D.jetSize r + e (log (r + e + 1) + log (M / Ω))`. 

 ### Class counts 

### `card_stdClasses_le_exp_mul_log`

 The admissible data `D` give a CM field `E = D.E`, the length `x = D.x` of the prime sum, the
number `m = D.m` of lifts and the rank `n_m = D.n D.m` of the last lift. Let `G ≥ 1` be an integer,
`n` an index set of size at most `2 n_m`, and `G_f` the finite adelic unitary group over `E` of the
form `∑_{i ∈ n} z_i \bar z_i`. If a subgroup `K` of `G_f` contains the principal congruence subgroup
of level `G`, then there are at most `exp (x ^ 29 (1 + log G))` double cosets `Γ \ G_f / K`. 

### `card_stdClasses_le_exp`

 The admissible data `D` give a CM field `E = D.E`, the length `x = D.x` of the prime sum, the
level primes with product `M = D.M`, a further prime level `N = D.N`, and integers `D.piM`, `D.piN`
of `E` whose products with their conjugates are `M` and `N`. Let `n` be an index set with at most
`n_m = D.n D.m` elements and `G_f` the finite adelic unitary group over `E` of the form
`∑_{i ∈ n} z_i \bar z_i`, with group `Γ` of rational points. If a subgroup `K` of `G_f` contains the
principal congruence subgroup of level `D.piM * D.piN`, then there are at most `exp (x ^ 30)` double
cosets `Γ \ G_f / K`. 

 ### The sum of the allowed losses 

### `allowedLoss`

 The allowed loss at `p`: it is `2 · D.loss p` for a non-split prime `p < x₁`, else `2 m f b` if
`p` is the level `N`, and `0` otherwise. 

### `exists_mul_sub_one_eq_or_mul_add_one_eq`

 If `p ≥ 2` satisfies `D.IsPlusMinusOneModLifts p`, that is `p ≡ ±1` modulo the number `m = D.m`
of lifts, then `p = m c ± 1` for some `c` with `1 ≤ c ≤ p` and `m ≤ 2 p / c`. 

### `sum_allowedLoss_mul_log_le`

 The admissible data `D` give a real number `x₁`, integers `x`, `b`, `a = x b`, `m`, a prime `N`
and a field `D.E` with `f` infinite places that contains `K = ℚ(√-d)`, for the prime `d = P.d`. For
every finite set `U` of natural numbers, the sum over `p ∈ U` of the allowed loss at `p` times
`log p` is at most `D.errorUnit = f a (log b)³`. 
