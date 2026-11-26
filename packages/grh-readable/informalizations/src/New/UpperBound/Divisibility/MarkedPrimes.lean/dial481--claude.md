---
{
  "module": "src/New/UpperBound/Divisibility/MarkedPrimes.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Divisibility/MarkedPrimes.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Divisibility/MarkedPrimes.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Marked primes above `p`, full marks and the scaled Hecke operator

Fix a prime `p` and an embedding `ι : ℂ → ℂ_[p]`. Each infinite place of `E` then induces a prime
above `p`. A finite set `Λ` of such primes is marked if it is disjoint from its conjugate and each
member is induced by an a-place; the definition also asks that `p` be exceptional and below `x₁`.
A *full mark* is a marked set that contains, for each a-place, the prime it induces or the
conjugate of that prime.
This file shows that a full mark exists and defines, with `A_𝔩` the number
`New.Data.heckeScalingExponent` of a prime `𝔩`, a scaled Hecke operator on the space
`D.SourceForm` of source forms.

## Main definitions and results

* `New.Data.IsFullMark`: a marked set that meets each pair of a prime induced by an a-place and its
  conjugate.
* `New.Data.exists_isFullMark`: a full mark exists for every exceptional `p < x₁`.
* `New.Data.IsMarked.scaledHeckeOperator`: the operator `p ^ A_𝔩 • T_{𝔩,𝔯}` at a marked prime, on
  the space of source forms.

Notions from other files:
* `New.Data.aPlaces`: The `a`-places: the infinite places of `E` whose class in `(ℤ/q₁)ˣ` is `1`
  modulo `q₀`.
* `New.Data.IsExceptional`, `New.Data.ceilLogLifts`: A condition on `p` alone: `(p/d) = -1`,
  `p ≢ ±1` modulo `m`, and the order `o₀` of `-p` modulo `q₀` is odd and at most `𝔯`, the least
  natural number with `m ≤ p^𝔯`.
* `New.placeOfEmb`: The prime of `E` induced by an embedding `σ : E →+* F` into an ultrametric
  normed field over `ℚ_p`: the centre on the integers of `E` of the valuation ring
  `{x : E | ‖σ x‖ ≤ 1}`.
* `New.Data.placeOfInt`: The infinite place of E named by the class of the integer ν modulo q₁ if ν
  is prime to q₁, and the identity place otherwise.
* `New.Data.lowColumns`: the number of columns at `τ` of height below `n_{j+1}` and different
  from `1`.


 ## Induced primes and marked sets 

### `inducedPlace`

 The prime of `E` above `p` induced by the embedding `ι ∘ σ` of `E` into `ℂ_p`, where the
infinite place `σ` is read as the embedding of `E` into `ℂ` that the CM type selects. 

### `IsMarked`

 A marked set of primes of `E` at `ι`: `Λ` is disjoint from its complex conjugate, and each prime
of `Λ` is induced by an a-place. Moreover `p` is exceptional and below `x₁`. 

### `IsMarked.star_notMem`

 `Λ` is disjoint from its complex conjugate. 

### `IsMarked.isExceptional`

 `p` is exceptional. 

### `IsMarked.induced_by_aPlace`

 Each prime of `Λ` is induced by an a-place. 

### `IsMarked.isSmallNonsplit`

 `p` is below `x₁` and `χ_K(p) ≠ 1`. 

### `IsFullMark`

 A full mark: a marked set that contains, for each a-place `τ`, the prime induced by `τ` or its
conjugate. 

### `IsFullMark.mem_or_star_mem`

 For each a-place, `Λ` contains its induced prime or the conjugate of that prime. 

### `integralSourceForms`

 The module of integral source forms: the elements of `D.SourceForm` of gauge at most `1`. 

### `placesInducing`

 The places inducing a prime of `Λ`: the infinite places of `E` whose induced prime above `p`
lies in `Λ`. 

### `placesInducingConj`

 The places inducing the conjugate of a prime of `Λ`: the infinite places of `E` whose induced
prime above `p` is conjugate to a prime of `Λ`. 

### `heckeScalingExponent`

 The number `A_𝔩`: the integer `D.a` times the number of a-places (places of class `1` modulo
`q₀`) that induce the prime `𝔩` at `ι`. 

### `sum_heckeScalingExponent`

 The numbers `A_𝔩` for `𝔩 ∈ Λ` add up to `a` times the number of a-places whose induced prime
lies in `Λ`. 

 ## Existence and properties of marked sets above a non-split prime 

### `IsExceptional.chiK_eq_neg_one`

 An exceptional prime is inert in `K`: its Legendre symbol `(p/d)` is `-1`. 

### `IsExceptional.odd_o₀`

 For an exceptional prime `p` the order `o₀` of `-p` modulo `q₀` is odd. 

### `ceilLogLifts_le_towerExp`

 `D.ceilLogLifts p`, the least natural number `k` with `m ≤ p ^ k`, is at most `D.towerExp`, the
exponent `s` with `2 ^ s = m ^ 22`. 

### `ceilLogLifts_le_l₀`

 The least `r` with `m ≤ p ^ r` is at most `l₀`, the least power of `3` above `27 s`, because
`m ≤ 2 ^ l₀`. 

### `instance : D.HasLogUpper (D.ceilLogLifts p) (Real.log D.logX₁)`

 The number `ceilLogLifts p`, the least `𝔯` with `m ≤ p ^ 𝔯`, is bounded in order of magnitude by
`log (log x₁)`: it is at most `s` (`ceilLogLifts_le_towerExp`). 

### `two_pow_dvd_right_of_dvd_mul`

 If `2 ^ s` divides a product of two natural numbers, where `2 * e < s`, and `2 ^ (e + 1)` does
not divide the first factor, then `2 ^ (e + 1)` divides the second. 

### `IsExceptional.m_dvd_orderOf`

 Let `p` be an exceptional prime: inert in `K = ℚ(√-d)`, not congruent to `±1` modulo the number
`m` of lifts, and such that the order `o₀` of `-p` modulo `q₀` is odd and at most `ceilLogLifts p`,
the least `r` with `m ≤ p ^ r`. Then the power of two `m` divides the order of `D.placeOfInt (-p)`,
the class of `-p` in the group `Gal(E/K) = (ℤ/q₁)ˣ` of infinite places of `E = K(ζ_{q₁})`. 

### `IsExceptional.q_eq_pow_orderOf`

 For an exceptional prime `p`, every prime `w` of `E` above `p` has norm `p ^ o`, where `o` is
the order of the place named by `-p`. 

### `IsExceptional.star_ne`

 For an exceptional prime `p`, no prime `w` of `E` above `p` is equal to its complex
conjugate. 

### `IsSmallNonsplit.not_dvd_M_mul_N`

 A non-split prime `p < x₁` divides neither `D.M` (the product of the two level primes
`D.levelPrime i`) nor `D.M * D.N`, and differs from `N`: the prime factors of `D.M * D.N` are at
least `x₁`. 

 ### Induced primes and the existence of a marked set 

### `p_mem_inducedPlace`

 The prime induced by an infinite place lies above `p`. 

### `inducedPlace_mul`

 Multiplying `σ` by `τ` pulls the induced prime back along `τ` in `Gal(E/K)`, that is, moves it
by `τ⁻¹`. The action `•` of infinite places on primes is this pullback. 

### `inducedPlace_neg_pow_mul_of_odd`

 For p inert in K and e odd, the prime induced by (−p^e)σ is the conjugate of the prime
induced by σ. 

### `exists_isFullMark`

 Let `p` be a prime below the cut-off `x₁` that is exceptional: `(p/d) = -1`, `p ≢ ±1` modulo
`m`, and the order of `-p` modulo `q₀` is odd and at most `ceilLogLifts p`, the least `r` with
`m ≤ p ^ r`. Then there is a full mark: a finite set of primes of `E` induced by a-places and
disjoint from its conjugate, which contains `𝔩` or its conjugate for each prime `𝔩` induced by an
a-place. 

### `inducedPlace_eq_or_star_iff`

 Let `p` be a prime with `(p/d) = -1`. Two places induce the same prime or conjugate primes
exactly when they differ by a power of `D.placeOfInt (-p)`, the place of the class of `-p` modulo
`q₁`. 

### `HasExceptionalOrbits`

 The properties of the orbits of the place named by `-p` that hold at an exceptional prime `p`.
Write `o₀ = D.o₀ p` for the order of `-p` modulo `q₀`, `o` for the order of the place named by `-p`,
`r = D.ceilLogLifts p` for the least number with `m ≤ p ^ r`, `l₀` for the least power of `3` above
`27 s`, where `2 ^ s = m ^ 22`, and `w_τ` for the prime above `p` induced by the infinite place
`τ`. 

### `HasExceptionalOrbits.odd_o₀`

 `o₀` is odd. 

### `HasExceptionalOrbits.o₀_le_ceilLogLifts`

 `o₀ ≤ r`. 

### `HasExceptionalOrbits.ceilLogLifts_le_l₀`

 `r ≤ l₀`. 

### `HasExceptionalOrbits.m_dvd_orderOf`

 `m` divides `o`. 

### `HasExceptionalOrbits.q_inducedPlace`

 Each `w_τ` has norm `p ^ o`. 

### `HasExceptionalOrbits.inducedPlace_neg_pow_mul`

 For odd `e`, the place `(-p ^ e) τ` induces the conjugate of `w_τ`. 

### `HasExceptionalOrbits.star_ne`

 The conjugate of `w_τ` differs from `w_τ`. 

### `HasExceptionalOrbits.eq_or_star_iff`

 The places that induce `w_τ` or its conjugate are the `(-p) ^ i τ`. 

### `IsExceptional.hasExceptionalOrbits`

 Let `p` be an exceptional prime: `(p/d) = -1`, `p ≢ ±1` modulo `m`, and the order `o₀` of `-p`
modulo `q₀` is odd and at most `r = ceilLogLifts p`, the least number with `m ≤ p ^ r`. Then the
properties of `New.Data.HasExceptionalOrbits` hold: `o₀ ≤ r ≤ l₀`, the least power of `3` above
`27 s` with `2 ^ s = m ^ 22`. The order `o` of the place named by `-p` is a multiple of `m`. The
prime `w_τ = inducedPlace τ` of `E` above `p` induced by an infinite place `τ` has absolute norm
`p ^ o` and differs from its conjugate, which is induced by `(-p ^ e) τ` for odd `e`. The places
that induce `w_τ` or its conjugate are the `(-p) ^ i τ`. 

 ### Properties of marked sets 

### `IsMarked.card_le`

 A marked set has at most `f` primes, `f` being the number of infinite places of `E`: each of its
primes is induced by one of them. 

### `IsMarked.not_dvd_M_mul_N`

 For a marked set `Λ`, the prime `p` divides neither `D.M` nor `D.M * D.N`, and differs
from `N`. 

### `IsMarked.inducedPlace_placeOfInt_neg_mul`

 If `Λ` is a marked set above `p`, multiplying a place by the place named by `-p` conjugates the
induced prime, because `p` is inert in `K`. 

### `IsMarked.neg_pow_mul_mem_placesInducing_iff`

 For a marked set `Λ` and odd `e`, multiplication by the place named by `-p ^ e` carries the
places whose conjugate induced prime lies in `Λ` onto the places whose induced prime lies in `Λ`. 

### `IsMarked.neg_pow_mul_mem_placesInducingConj_iff`

 For a marked set `Λ` and odd `e`, multiplication by the place named by `-p ^ e` carries the
places whose induced prime lies in `Λ` onto the places whose conjugate induced prime lies in `Λ`. 

### `IsMarked.notMem_bPlaces`

 Let `Λ` be a marked set of primes of `E`: in particular each prime of `Λ` is induced by an
a-place, and `p` is exceptional, so it is inert in `K` and `-p` has odd order modulo `q₀`. If
`inducedPlace σ` or its conjugate lies in `Λ`, then `σ` is not a b-place. 

### `IsMarked.cast_weight_eq`

 At a place whose induced prime, or its conjugate, lies in a marked set, the weight is `a / x₁`,
because such a place is not a b-place. 

### `IsMarked.sum_inducedPlace_eq_sum_star`

 Let `l` be a prime of a set `Λ` that is marked: it is disjoint from its conjugate, its primes
are induced by a-places, and `p < x₁` is exceptional. For any function `G`, the sum of
`G (D.liftWeight j τ)` over the places `τ` that induce `l` equals the sum over the places that
induce the conjugate of `l`. Here `D.liftWeight j τ = D.weight τ + (j + 1/2) D.gap` is the weight at
`τ` of the character of the `j`-th lift in the chain. 

### `IsMarked.sum_placesInducing_eq_sum_placesInducingConj`

 Let the set `Λ` of primes of `E` be marked: it is disjoint from its conjugate, its primes are
induced by a-places, and `p < x₁` is exceptional. Let `w_j(τ) = D.liftWeight j τ` be the weight at
`τ` of the character of the `j`-th lift. For any function `G` of a weight and a prime, the sum of
`G (w_j(τ), 𝔩)` over the places `τ` whose induced prime `𝔩` lies in `Λ` (`placesInducing Λ`) equals
the sum of `G (w_j(τ), 𝔩̄)` over the places `τ` for which the conjugate `𝔩̄` of the induced prime
lies in `Λ`. 

### `IsMarked.sum_inducedPlace_sub_star_eq_zero`

 The balance `IsMarked.sum_placesInducing_eq_sum_placesInducingConj` as one sum over all infinite
places `τ`: with `𝔩 = inducedPlace τ`, add `G (D.liftWeight j τ) 𝔩` if `𝔩 ∈ Λ` and subtract
`G (D.liftWeight j τ) (star 𝔩)` if `star 𝔩 ∈ Λ`. The total is zero. 

### `IsMarked.natCast_mem_asIdeal`

 A prime of a marked set lies above `p`. 

### `IsMarked.valuation_natCast_eq_exp_neg_one`

 For a marked set `Λ` (`D.IsMarked Λ`) and `l ∈ Λ`, `p` is a uniformiser at `l`: its `l`-adic
valuation is `exp (-1)`. The reason is that the prime `p` of a marked set divides neither `q₁` nor
`d`. 

### `IsMarked.isSplit`

 Every prime `l` of a marked set `Λ` (disjoint from its complex conjugate, each prime induced by
an a-place) is split (`l.IsSplit`): `l` differs from its complex conjugate. 

### `IsMarked.maxCompactAt_le_levelX`

 Let `Λ` be a marked set of primes of `E` above `p` and `l ∈ Λ`. In the finite adelic unitary
group with basis indexed by `D.X 0`, the group `maxCompactAt (D.X 0) l` of elements of the standard
maximal compact subgroup that are trivial away from `l` and `star l` lies in `D.levelX 0`, the level
that fixes the forms of `D.SourceForm`. 

### `IsMarked.scaledHeckeOperator`

 The operator `p ^ A_𝔩 • T_{𝔩,𝔯}` on `D.SourceForm`, as an endomorphism over `embValRing`; here
`T_{𝔩,𝔯}` is the Hecke operator at the marked prime `𝔩` of index `𝔯 = D.ceilLogLifts p`, which
preserves `D.SourceForm`. 

 ### Collisions and full marks 

### `IsFullMark.collisionSum_placesInducing_eq_zero`

 Let `Λ` be a full mark: a marked set that contains, for each a-place, the induced prime or its
conjugate. A collision outside `placesInducing Λ` is a pair `(τ, e)` with `e` odd such that `τ` and
its product with the place `D.placeOfInt (-p ^ e)` are a-places that induce no prime of `Λ`. Then
`collisionSum`, the sum of `D.a / p ^ e` over these collisions, is zero. 

 ## The cost of the low columns at the places inducing `Λ` 

### `IsMarked.card_mul_transferExponent_add_sum_lowColumns_le`

 Let `j < m`, the number of lifts, and let the set `Λ` of primes of `E` be marked: it is disjoint
from its conjugate, its primes are induced by a-places, and `p < x₁` is exceptional. Let `L` be the
number of low columns, those of height below the rank `n_{j+1}` and other than `1`, in the diagrams
`D.columnCount` at the places that induce a prime of `Λ`. Let `r = ceilLogLifts p` be least with
`m ≤ p ^ r`, and `ν_p = transferExponent p = r f (n_m + r)`, where `f` is the number of infinite
places and `n_i = D.n i`. Then `#Λ ν_p + r L` is at most `loss p / m`, plus `a / x₁` for each
a-place inducing a prime of `Λ`. Here `a = x b` is the product of two scales of the data, and
`loss p` is `f a (log b)² / p`, times `m` if `p ≡ ±1` modulo `m`. 
