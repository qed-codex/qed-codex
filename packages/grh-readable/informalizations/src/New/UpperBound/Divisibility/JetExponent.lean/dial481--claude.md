---
{
  "module": "src/New/UpperBound/Divisibility/JetExponent.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Divisibility/JetExponent.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Divisibility/JetExponent.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# A lower bound for the divisibility bound by the gain

Fix a prime `p`. The divisibility bound of stage `j` at `p` measures the `p`-divisibility of a lift;
it depends on a set `S` (also written `ev`) of places whose long rows are removed.

This file defines it and bounds it from below by the gain at `p` when `p < x₁` is non-split. Apart
from an error term, only collisions lose; a collision is a pair `(τ, e)` with `e ∈ I_p` (`e` odd, or
`p = d`) such that `τ` and `(-p ^ e) τ` are `a`-places outside `ev`. In `lowColumns` and `lowBoxes`
a column is a column of a diagram; they count the columns of height below `n_{j+1}` and different
from `1`, and the boxes in them.

## Main definitions and results

* `New.Data.divisibilityBound`: the divisibility bound at `p` of stage `j`, for a set `S` of places.
* `New.Data.le_divisibilityBound`: the lower bound for the divisibility bound by the gain at `p`.

Notions from other files:
* `New.Data.aPlaces`: The `a`-places: the infinite places of `E` whose class in `(ℤ/q₁)ˣ` is `1`
  modulo `q₀`.
* `New.Data.IsExceptional`, `New.Data.ceilLogLifts`: A condition on `p` alone: `(p/d) = -1`,
  `p ≢ ±1` modulo `m`, and the order `o₀` of `-p` modulo `q₀` is odd and at most `𝔯`, the least
  natural number with `m ≤ p^𝔯`.
* `New.Data.placeOfInt`: The infinite place of E named by the class of the integer ν modulo q₁ if ν
  is prime to q₁, and the identity place otherwise.


### `lowColumns`

 The number of columns at τ of height below n_{j+1} and different from 1: the sum of
`columnCount τ h` over h < n_{j+1}, h ≠ 1. 

### `lowBoxes`

 The number of boxes in the columns counted by `New.Data.lowColumns` j τ: the sum of
h·`columnCount τ h` over h < n_{j+1}, h ≠ 1. 

### `divisibilityBound`

 The divisibility bound at `p` of stage `j`, for a set `ev` of places. Remove the columns of
height one at the places of `ev` from the diagrams `D.columnCount`, read at heights below
`n = D.n (j + 1)`. The bound is the predicted divisibility of what remains, plus the full gain
`γ_p = gammaPrime P.d p` for each removed box, less `f n ^ 3 (1 + log_p (max B 1))`. Here `B` is the
number of boxes before the removal. 

### `longRow`

 The length of the long row at `τ` (the `a` columns of height one at an `a`-place) after removing
the long rows at the places of `ev`. 

### `partnerTerm`

 The term of the place `τ` and the exponent `e` in the predicted divisibility of stage `j`, after
removing the long rows at the places of `ev` and without the factor `v(π_p)`. It is zero unless
`e ∈ I_p = positivePartnerExponents P.d p`, and `P.partner D.towerExp p e τ` is the place
`(-p ^ e) τ`. 

### `summable_partnerTerm`

 The terms `partnerTerm p j S τ e = (L τ / p ^ e - L τ' - c τ')₊ + (l τ / p ^ e - l τ')₊ - c
τ / p ^ e`, where `τ' = (-p ^ e) τ`, `L = longRow S`, `c = lowColumns j` and `l = lowBoxes j` (zero
unless `e ∈ positivePartnerExponents P.d p`), are summable over `e`. 

### `heightOneColumns_eraseHeightOne`

 After removing the long rows at the places of `S`, the number of columns of height one at `τ`
below `n_{j+1}` is `longRow S τ`. 

### `lowColumnCount_eraseHeightOne`

 Erasing the columns of height one at the places of `S` from `D.columnCount` keeps the number of
low columns: `lowColumnCount` at height bound `D.n (j + 1)` equals `D.lowColumns j τ`. 

### `lowBoxCount_eraseHeightOne`

 Erasing the columns of height one at the places of `S` from `D.columnCount` keeps the number of
boxes in the low columns: `lowBoxCount` at height bound `D.n (j + 1)` equals `D.lowBoxes j τ`. 

### `le_loss`

 The loss `D.loss p` is at least `f * logB ^ 2 * (a / p)`: for `p ≡ ±1` modulo `m` it carries
the additional factor `m ≥ 1`. 

### `placeOfInt_mul_mem_aPlaces_iff`

 For odd `e` and an `a`-place `τ`, the place `D.placeOfInt (-p ^ e) * τ` is an `a`-place if and
only if `D.o₀ p` divides `e`. 

### `IsCollision.ne_and_odd_and_dvd`

 If `(τ, e)` is a collision at `p` outside `S`, that is, `τ` and `placeOfInt (-p ^ e) * τ` are
`a`-places outside `S` and `e ∈ I_p` (it is odd, or `p = d`), then `p ≠ d`, and `e` is odd and
divisible by the order `o₀ p` of `-p` modulo `q₀`. 

### `collisionSum_le`

 Let `p` be a prime and `S` a set of infinite places of `E` (`D.Φ` is the type of these places,
`f` their number). If every collision has `e ≥ o`, then `collisionSum p S`, the sum of `a / p ^ e`
over the collisions, is at most `2 f a / p ^ o`; here `a = D.a` is the length of a long row. 

### `mul_collisionSum_le_loss`

 Let the prime `p` be below the cut-off `x₁`, non-split in `K = ℚ(√-d)` and not exceptional. Then
`m * collisionSum p ∅ ≤ loss p`, where `loss p` is `m f a (log b)² / p` if `p ≡ ±1` modulo `m` and
`f a (log b)² / p` otherwise. Here `m` is the number of lifts, `f` the number of infinite places of
`E`, and `a = x b` is the product of the scales `x` and `b` of the data. 

### `k_mem_range_n_succ`

 The least height `k` of a low column is below `n_{j+1}`. 

### `mul_weight_le_lowBoxes`

 The number `lowBoxes j σ` of boxes in the low columns at `σ` is at least `k w`, where
`w = D.weight σ` and `k` is the least height of a low column: the columns of height `k` alone have
that many boxes. 

### `lowColumns_le`

 Let `j < m`, with `m = D.m` the number of lifts, and `σ : D.Φ` an infinite place of `E`. The
number `D.lowColumns j σ` of columns at `σ` of height below `n_{j+1}` and other than `1` is at most
`D.weight σ + x ^ 60`, where `x` is the scale `D.x`: there are about `D.weight σ` of height `k` and
at most `D.gap` of every other height. 

### `lowBoxes_le`

 For `j < D.m`, the number `D.lowBoxes j σ` of boxes in the columns at `σ` of height below
`n_{j+1}` and different from `1` is at most `D.k * D.weight σ + D.x ^ 60`. 

### `lowColumns_lowBoxes_bounds`

 For `j < m` and an infinite place `σ` of weight `w = D.weight σ` (that is `a / x` at a `b`-place
and `a / x₁` at any other): the number of boxes in the low columns lies between `k w` and
`k w + x ^ 60`, and the number of low columns is at most `w + x ^ 60`. 

### `boxes_eq_aPlaces_add_low`

 For `j < D.m`, the number `boxes D.columnCount (D.n (j + 1))` of boxes in the columns of height
below `D.n (j + 1)` equals `D.a` times the number of a-places `D.aPlaces`, plus the sum over `σ` of
`D.lowBoxes j σ`, the boxes in columns at `σ` of height below `D.n (j + 1)` other than `1`. 

### `boxes_sub_boxes_eraseHeightOne`

 For `j < m` the boxes removed with the columns of height one at the places of `S` are the `a`
boxes at each a-place in `S`. 

### `one_add_logb_boxes_le`

 Let `p` be a prime and `j < m`, the number of lifts. The diagram at an infinite place `τ` of `E`
has `D.columnCount τ h` columns of height `h`. Let `B` be the number of boxes of these diagrams, at
all places, in the columns of height below the rank `n_{j+1} = D.n (j + 1)`. Then
`1 + log_p (max B 1)` is at most `(log b) ^ 2`, where `b` is the largest scale of the data and
`log b = D.logB`. 

### `posPart_sub_weight_le_posPart_longRow`

 Let `j < m`, let the prime `p` be below the cut-off `x₁` and non-split in `K = ℚ(√-d)`, let
`e ∈ positivePartnerExponents P.d p`, let `S` be a set of infinite places of `E`, and let
`τ' = D.placeOfInt (-p ^ e) * τ` be the product of `τ` with the place of the class of `-p ^ e`
modulo `q₁`. With `a = x b` the product of the scales `x` and `b`, the weight `w = D.weight` is
`a / x` at the b-places and `a / x₁` elsewhere. Let `L = longRow S` be `a` at the a-places outside
`S` and `0` elsewhere, and let `c = lowColumns j` count the columns of height below `n_{j+1}` other
than `1`. For an a-place `τ` the number `(a / p ^ e - w τ')₊` is at most
`(L τ / p ^ e - L τ' - c τ')₊ + x ^ 60`, plus `a / p ^ e` if `τ ∈ S` or if `(τ, e)` is a collision.
For `τ ∈ S` and `e = 1` the bound still holds with `a / x₁` added on the left. 

### `mul_posPart_weight_le`

 For `j < m` and `z > 0`, the second term of the gain, `k (w(τ) / z - w(τ'))₊` with `w` the
weight and `k` the least height of a column other than `1`, exceeds the same expression in the boxes
of the low columns by at most `x ^ 60`. 

### `min_longRow_add_lowColumns_add_min_lowBoxes_le`

 Let `j < m`, the number of lifts, let `S` be a set of places, and let
`-τ = P.partner D.towerExp P.d 0 τ` be the product of `τ` with the place named by `-1`. Let
`L = longRow S` be `a = D.a` at the a-places outside `S` and `0` elsewhere, let `c = lowColumns j`
count the columns of height below `n_{j+1}` other than `1`, and let `l = lowBoxes j` count the boxes
in these columns. Then `min (L τ) (L (-τ) + c (-τ)) + c τ + min (l τ) (l (-τ))` is at most
`3 a / (d m)`, because `τ` and `-τ` are neither both a-places nor both b-places (class `-1`). 

### `sub_le_predictedDivisibility`

 Let `p` be a prime, `j < m` (the number of lifts) and `S` a set of infinite places of `E`.
Remove from the diagrams `D.columnCount` the columns of height one at the places of `S`, and read
them at heights below `n_{j+1}`. Their `predictedDivisibility` at `p`, for the partner map
`P.partner D.towerExp p e τ = (-p ^ e) τ`, is by definition `v(π_p) = piPrimeValuation P.d p` times
the sum over all `e` and `τ` of `partnerTerm p j S τ e`, the term that compares the diagram at `τ`
with that at its partner, less a correction if `p = d`. The correction is at most `2 a / (p m)` for
each of the `f` places, where `a = D.a` is the length of a long row. 

### `gammaPrime_mul_lowColumns_le`

 For `j < D.m` and a place `τ`, the number `γ_p = gammaPrime P.d p` times the number
`D.lowColumns j τ` of columns at `τ` of height below `n_{j+1}` and different from `1` is at most
`D.a / p / D.m`. 

### `localPrimeSum_add_le_mul_tsum_partnerTerm_add`

 The bound for the gain `D.gain p` at one infinite place `τ` of `E`. Let `j < m`, let the prime
`p` be below the cut-off `x₁` and non-split in `K = ℚ(√-d)`, and let `S` be a set of places whose
long rows are removed. Let `I_p = positivePartnerExponents P.d p`, `v = piPrimeValuation P.d p` and
`γ_p = gammaPrime P.d p = v ∑_{e ∈ I_p} 1 / p ^ e`. The weight `w = D.weight` is `a / x` at the
b-places and `a / x₁` elsewhere, `a = x b` being the product of two scales of the data, and
`s_p = localPrimeSum p` is the series `s_p(y, τ) = v ∑_{e ∈ I_p} (y / p ^ e - w((-p ^ e) τ))₊`. The
left side is the share of `τ` in `gain p / m`, namely `s_p(a, τ)` (for an a-place only, that is, of
class `1` modulo `q₀`) plus `k s_p(w(τ), τ)` with `k` the rank of the source, increased by
`v a / x₁` if `τ` is an a-place in `S`. It is at most `v` times the sum of three terms, plus `γ_p`
times the number `lowColumns j τ` of columns of height below `n_{j+1}` other than `1`, plus `γ_p a`
if `τ` is an a-place in `S`. The three terms are the series of `partnerTerm p j S τ e`, the series
of `a / p ^ e` over the `e ∈ I_p` such that `τ` and `(-p ^ e) τ` are a-places outside `S`
(collisions), and `2 x ^ 60` for each of the `clog p ⌈x₁⌉₊` exponents `e` with `p ^ e < x₁`. 

### `le_divisibilityBound`

 **Only collisions lose.** Let the prime `p` be below the cut-off `x₁` and non-split in
`K = ℚ(√-d)`, let `j < m`, the number of lifts, and let `S` be any set of infinite places of `E`.
The bound `divisibilityBound p j S` is the predicted divisibility at `p` of the diagrams
`D.columnCount`, read below height `n_{j+1}` and with the columns of height one at `S` removed, plus
`γ_p` for each removed box, less a logarithmic term. It is at least
`gain p / m = ∑_τ s_p(a, τ) + k ∑_σ s_p(w(σ), σ)` (with `τ` an a-place, that is, of class `1` modulo
`q₀`, `σ` any place, `s_p = localPrimeSum p` and `w = D.weight`), less `collisionSum p S`, the sum
of `a / p ^ e` over the pairs `(τ, e)` with `e ∈ I_p` and both `τ` and `(-p ^ e) τ` a-places outside
`S`, plus `v(π_p) a / x₁` for each a-place in `S`, less `f a (log b)² / (m p)`. Here
`v(π_p) = piPrimeValuation P.d p`, `a = x b` is the length of a long row, `log b = D.logB`, and `f`
is the number of infinite places of `E`. 
