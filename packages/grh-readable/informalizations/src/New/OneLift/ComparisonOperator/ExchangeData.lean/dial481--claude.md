---
{
  "module": "src/New/OneLift/ComparisonOperator/ExchangeData.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/OneLift/ComparisonOperator/ExchangeData.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/OneLift/ComparisonOperator/ExchangeData.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Data of the three exchanges: the carrier, the choices and the functions 𝖥_i

For admissible data `D`, the element `ϖ = New.Data.piM` of 𝓞_E generates the product of the primes
at the places `New.Data.chosenPlace`. The file defines the objects of the three exchanges that turn
a twist into a number on `W_j = New.Data.spaceW`, `1 ≤ j ≤ m`: the carrier φ° with its coefficients
𝖺, the modulus `ϖ^c`, the index sets of the spaces, the characters, the choices `i`, the fixed
polynomial `P` and the functions `𝖥_i`.

The standard definite space `E^n` is also written `I_n`, and `υ = New.WeilData.upsilonU1` is the
character `ν_η` of weight 1 and trivial tame part. The letter `ϑ` denotes a tame character
(`New.Data.TameChar`); it is a twist only where this is said.

| object | Lean name | object | Lean name |
|---|---|---|---|
| `S = E^{2m,m}` | `CarrierIndex` | `χ′` | `twistedChiMPow` |
| `W♭ = E^{6m+1}` | `FlatIndex` | `ν″` | `firstFactorChar` |
| `V″`, `W′` | `FirstFactorIndex` | `ν♭ υ^m` | `carrierChar` |
| `V°` | `SecondFactorIndex` | `φ°`, `𝖺 χ′` | `carrierForm`, `carrierCoeff` |
| columns of `μ⁺`, plus Δ′ indices | `DetIndex` | `P`, `𝖥_i` | `paddedMinorProd`, `choiceFn` |
| choices `i` | `ChoiceIndex` | `u`, `u°` | `conjHolomorphicWeight`, `kernelWeight` |

## Main definitions and results

* `New.Rows.carrierForm`: the carrier φ°, the theta lift of the constant function from the unitary
  group of a negative definite space to that of a space with signs `+1` on `2 m` and `−1` on `m`
  coordinates.
* `New.Rows.carrierCoeff`: the coefficients 𝖺 times a character, a class sum of theta kernels
  between two definite spaces.
* `New.Data.choiceFn`: the function `𝖥_i` on `U(W_j)`, the integral of the carrier against a theta
  kernel.
* `New.Data.isTameFor_of_hasWeight`, `New.Data.isTameFor_twistedChiMPow`: let `ϑ` be a twist,
  `c ≠ 0`, and take a character whose tame part is `ψ * ϑ.tamePart`, with `ψ` non-trivial exactly at
  the chosen places. It ramifies exactly at the places dividing `D.twistModulus ϑ c`, that is, the
  chosen places and the places in `ϑ.Q` (`New.Exchange.IsTameFor`). This applies to
  `New.Data.twistedChiMPow`.
* `New.Rows.exists_int_weylRep_invariant_fockPoly_eq_smul_monomial`: for a monomial of the right
  degrees there is an integral vector whose Fock polynomial is a nonzero multiple of the monomial.
  The vector is fixed by the elements that act trivially on the rows of the monomial.

Notions from other files:
* `New.Modulus`: a nonzero ideal of 𝓞_E that is never divisible by both a place w and its conjugate
  w̄.
* `New.Data.spaceW`: the diagonal hermitian space `W_j` of rank r over E with signs `D.signsW j`.
* `New.Data.liftWeight`: the natural number `κ_j`, a function of the infinite place; the character
  `New.Data.liftChar` of the `j`-th lift has weight `−κ_j`.
* The numbers of `D`: the rank `r` of `W_j`, the number `m` of lifts, `k = r + 1 − m`, `t = 5 r`,
  the gap `Δ = New.Data.gap = 2 r ^ 8` and `Δ′ = New.Data.reducedHalfGap = Δ / 2 − (t + 1) / 2`.
* `New.Data.descentPair`: the data (`New.DescentPair`) of the lift from `W_j` to `I_{r+t}`. They
  include a `numbering` of the basis vectors of `W_j` and, at each infinite place, two partitions
  `μ⁺`, `μ⁻` given by their numbers `colsPlus`, `colsMinus` of columns of each height.
* `New.Data.TameChar`, `New.Data.Twist`: a character of U(1)(𝔸) of weight 0 whose tame part is
  trivial outside a finite set Q of places; it is a twist if the tame part is non-trivial on all of
  Q.

## Use in the argument

* The carrier φ° and the coefficients 𝖺: the class sum of a twisted square kernel against 𝖺 is a
  multiple of φ°. See `New.OneLift.ComparisonOperator.ThreeExchanges`.
* Moduli, index sets, polynomial and functions `𝖥_i`: the third exchange and its left side as a
  theta series. See `New.OneLift.ComparisonOperator.ThreeExchanges` and
  `New.OneLift.ComparisonOperator.FirstFactors`.
* Order, weights and gaps on `W_j`: the functions `𝖥_i` separate good forms. See
  `New.OneLift.ComparisonOperator.ProductsSpan`.
* Integral vectors with a monomial Fock polynomial: the height bound for inverse ratios of twisted
  to untwisted Hecke L-values. See `New.OneLift.HeckeValues.TwistedValueHeights`.


 ## The ideal generated by ϖ 

### `New.Rows.span_piM`

 Let `D` be admissible data and `ϖ = D.piM` the integer of E whose prime divisors are the
chosen places. The ideal generated by `ϖ` is the product of the primes `D.chosenPlace i`, over all
pairs `i = (k, w)` with `w` a chosen place above the prime `p_k = D.levelPrime k`. 

 ## Stacked determinants, the trivial modulus, the carrier φ° and the coefficients 𝖺 

### `stackedDet`

 The determinant of the square matrix formed by the columns `j` of the constant matrix `η` (rows
`l`) stacked over the matrix of variables `X (τ, a, b)` (rows `n'`), both with columns `n`. 

### `unitModulus`

 The modulus of E whose ideal is the whole ring of integers. 

### `carrierForm`

 The carrier φ°: the theta lift of the constant function 1 from the unitary group of the negative
definite space I_m⁻ to that of the space S with signs +1 on `Fin (2 * m)` and −1 on `Fin m`. The
theta kernel is taken with trivial modulus, function 1 and the polynomial ∏_τ det(y⁻_τ)^{2m}, where
y⁻_τ is the m × m block of variables in the rows of sign −1. Its characters are υ^m and 1, so it is
υ(det g′)^m times the kernel with standard characters, for g′ in the group of I_m⁻. 

### `carrierCoeff`

 The function `𝖺(h) c(det h)` on the finite adelic points of `U(I_{n'})`: the class sum over
`U(I_m)` at the level `New.stdLevel` of the theta kernel with characters `c` and `1`, trivial
modulus, constant finite datum and polynomial `1`, taken at archimedean component `1` on both
groups. The coefficient `𝖺(h)` is the value for `c = 1`. 


## Moduli, index sets, polynomial and functions of the third exchange

The objects of the third exchange for admissible data `D` (`New.Data`), a tame character `ϑ`
(`New.Data.TameChar`) and an index `j`. The spaces `V″` and `V°` are the standard definite spaces
(all signs `+1`) on the index sets `New.Data.FirstFactorIndex` and `New.Data.SecondFactorIndex`.


### `untwistedModulus`

 The modulus ϖ^c, the c-th power of the product of the chosen places above p₀, p₁. It is the
modulus `D.twistModulus` of the trivial character; the argument `false` leaves out the factor Q, the
product of the places of the character. 

 ### Index sets and the numbering of the basis 

### `CarrierIndex`

 The index set with 2m + m elements, in two blocks, of the space S of signature (2m, m). 

### `FlatIndex`

 The index set, with 6m + 1 elements, of the definite space W♭ = I_{6m+1}. 

### `SecondFactorIndex`

 The index set of V°: the r indices of W_j and t − 9m − 1 − r further ones. 

### `SecondFactorClasses`

 The set of classes of U(V°) at principal level ϖ²: double cosets of U(V°)(𝔸_f) by the
rational points and the congruence subgroup modulo ϖ². 

### `rowIndexOfNumber`

 The inverse of the numbering `New.Data.basisNumber`: the index in `New.Data.RowIndex` that has
number min(i, r − 1). 

 ### Choices of classes and rows 

### `RowChoice`

 The part of a choice that lives on W♭ = I_{6m+1}: a class of U(W♭) at principal level ϖ² and,
for each infinite place, Δ′ lists of 2m row indices among 6m + 1. Here
Δ′ = `D.reducedHalfGap` = r⁸ − (t + 1)/2 is the size of the second block of `New.Data.DetIndex`:
the number of columns of the partition μ⁺ of the greatest height k + j − 1. 

### `shortRows`

 A chosen invertible matrix over E whose rows lie in the lattice at the class `i.1` and whose
entries are small at every complex embedding (`New.Space.exists_short_basis_stdSpace`). 

 ### Characters, padding, the polynomial and the functions `𝖥_i` 

### `twistedChiMPow`

 The character χ′ = χ^j·ϑ of [U(1)], for the fixed weight-zero character χ of tame part ω and
a tame character ϑ. 

### `twistedChiMPow_hasWeight`

 The character `twistedChiMPow ϑ j = D.chiM ^ j * ϑ` has weight `0` at every infinite place. Its
tame part is `D.liftTamePart ϑ j = D.chiMLocal ^ j * ϑ.tamePart`, where `D.chiMLocal` is the tame
part of `D.chiM`. 

### `PadIndex`

 The index set of the padding I_j⁻ ⊕ I_{3m−j} of W_j: a block of j elements and a block of
2m + (m − j) elements. 

### `FirstFactorIndex`

 The index set of V″ and of W′: the r indices of W_j, the padding `New.Data.PadIndex` and the
indices of W♭. 

### `padSigns`

 The signs of the padded space W_j ⊕ I_j⁻ ⊕ I_{3m−j}: those of W_j, then −1 on j indices and +1
on 2m + (m − j) indices. 

### `negIndex`

 The m chosen negative rows of the padded W_j: i < m goes to the i-th index of the padding block
of size j if i < j, and to `New.Data.rowIndexOfNumber`(k + i − 1) otherwise. 

### `posRowIndex`

 The 2m constant rows for a column of height h < r₊ = k + j − 1, all basis vectors: i < 2m goes
to the basis vector number h + i of W_j if h + i < r₊, and otherwise to index i of the positive
padding block. 

### `untwistedDescentPair`

 The j-th descent pair `New.Data.descentPair` at the trivial character: the data of the lift from
W_j to I_{r+t}, with a `numbering` of the basis vectors of W_j and the numbers `colsPlus τ h`,
`colsMinus τ h` of columns of height h of two partitions μ⁺, μ⁻ at each infinite place τ. 

### `DetIndex`

 The index set of the determinants at the place τ, one for each column of the partition μ⁺.
Let r₊ = `D.posRank j` = k + j − 1, with k = r + 1 − m, be the number of plus signs of W_j. For each
height h < r₊ there are `(untwistedDescentPair j).colsPlus τ h` indices, the number of columns of
height h that the data of the j-th lift assign to μ⁺; for the height r₊ there are
Δ′ = `D.reducedHalfGap` indices. 

### `paddedMinorProd`

 The fixed polynomial P = ∏_τ det(y⁻_τ)^{e′(τ)} ∏_{h<k+j−1} det(y_{τ,h})^{k⁺(τ,h)}, with
e′(τ) = #`New.Data.DetIndex`(τ) + #`New.Data.FirstFactorIndex` + m and k⁺ the column counts
`colsPlus` of `New.Data.untwistedDescentPair`. Here y⁻_τ is the m × m block of variables in the rows
`New.Data.negIndex` and the negative columns, and y_{τ,h} the 2m × 2m block in the rows
`New.Data.posRowIndex` for h and the positive columns. 

### `firstFactorCharExp`

 The natural number j + ⌊(t + k − 1)/2⌋, the exponent of υ in `New.Data.firstFactorChar`. 

### `carrierChar`

 The character μ♭·υ^{m + j + ⌊(t+k−1)/2⌋ − jΔ} of [U(1)]. Here μ♭ = `D.chiZero` is a fixed
character of weight −κ_0 = `-D.liftWeight 0` and trivial tame part, υ = `upsilonU1` has weight 1,
and Δ = `D.gap` = 2r⁸ is the difference κ_{j+1} − κ_j. It is ν♭·υ^m, where ν♭ = ν″/χ′ is the
quotient of `New.Data.firstFactorChar` by `New.Data.twistedChiMPow`, which is free of the twist. 

### `carrierChar_hasWeight`

 Let `j` with `1 ≤ j ≤ m` be the index of a lift. The character `carrierChar j` of `U(1)(𝔸)` has
weight `m + firstFactorCharExp j - κ_j` and trivial tame part, where `κ_j = D.liftWeight j`. 

### `firstFactorChar`

 The character ν″ = μ_j⁰ϑ·υ^{j + ⌊(t+k−1)/2⌋} of [U(1)], with μ_j⁰ϑ = `New.Data.liftChar` the
character of the j-th lift. 

### `ChoiceIndex`

 The choices: pairs of a 3m × rk V″ matrix Λ modulo ϖ² and an element of `New.Data.RowChoice`,
which is a class at level ϖ² of U(W♭) with selections of rows. 

### `choiceFn`

 The function `𝖥_i(g)` on `U(W_j)`, for a choice `i`: a matrix `Λ = i.1` modulo `ϖ²`, and a class
and rows `i.2`. It is the integral, for the measure `New.Space.quotMeasure` on the unitary group
of the space `S` of signature `(2m, m)` modulo its rational points, of the carrier
`New.Rows.carrierForm` times the theta kernel of `S` and `W′ = W_j ⊕ padding ⊕ W♭`, taken at
`(g, 1, h♭)` with `h♭` the representative of the class. The characters are `υ^m` and
`carrierChar j = ν♭ υ^m`, so the kernel is that with standard characters divided by `ν♭` on `U(S)`.
The finite datum is the additive character `traceChar Λ` of the matrices modulo `ϖ²`. The
polynomial is `P = New.Data.paddedMinorProd` on the padded `W_j` times the product of determinants
`P♭ = New.pairedDetProd` on `W♭`, which pairs the chosen rows of `New.Data.shortRows` with the
variables in the positive columns. 

 ## Determinant count and character exponent at each infinite place 

### `New.Data.card_detIndex_add_firstFactorCharExp`

 Let `D` be admissible data, `1 ≤ j ≤ m` and `τ` an infinite place. The `j`-th lift goes from the
unitary group of `W_j`, of rank `r`, to the definite unitary group of rank `r + t`; its character
has weight `-κ_j` at `τ`, with `κ_j = D.liftWeight j τ`. The set `DetIndex j τ` has one element for
each column of the partition `μ⁺` that belongs to the plus signs of `W_j` at `τ`, so its cardinality
is the largest part `μ₁⁺`. Then `μ₁⁺ + firstFactorCharExp j = κ_j`, where
`firstFactorCharExp j = j + ⌊(t + k - 1) / 2⌋` with `t = D.t = 5 r` and `k = D.k = r + 1 - m`. 


## Order, kernel weight and gaps for the separation argument on W_j

Weights and numerical facts for the separation argument on the space `W_j`, whose signs are
`New.Data.signsW` and whose doubled parameter is `New.Data.paramW`; here `1 ≤ j ≤ m`.


### `nStar`

 The natural number n_* = 2ft³, where f is the number of infinite places of E and t = 5r. 

### `two_mul_r_le_b`

 Twice the rank `r` of `W_j` is at most the real number `b = D.b`, the size parameter of the
weights `D.liftWeight j`. 

### `mul_nStar_add_t_le_halfGap`

 The number `300 n_* + t`, with `n_* = nStar D = 2 f t ^ 3`, is at most `D.halfGap = r ^ 8`. 

### `_root_.New.staircaseWeight_of_eq_one`

 The staircase weight at a column `c` of sign `s c = 1`. The staircase has `k η i` minors of
size `i` and sign `η`, the number `o c` is the place of `c` among the columns of its sign, and `γ`
is the shift. The weight is `γ` minus the number of minors of sign `+1` and size `i < card n` that
contain `c`, those with `o c < i`. 

### `_root_.New.staircaseWeight_of_eq_neg_one`

 The staircase weight at a column `c` of sign `s c = -1`. The staircase has `k η i` minors of
size `i` and sign `η`, the number `o c` is the place of `c` among the columns of its sign, and `γ`
is the shift. The weight is `γ + card n` plus the number of minors of sign `-1` and size
`i < card n` that contain `c`, those with `o c < i`. 

### `orderW`

 The integer-valued order on the basis of W_j, for an index 1 ≤ j ≤ m of a lift. Let o(c) be
`(untwistedDescentPair j).numbering c`: the number `D.basisNumber c` for a positive vector c and
r − 1 − `D.basisNumber c` for a negative one. The order is −1 − o(c) on positive and o(c) on
negative vectors. Positive vectors come first, in reversed order. 

### `conjHolomorphicWeight`

 The weight u of the conjugates of good forms: the highest weight of the lowest K-type
(`New.HCParam.lowestKType`) of the parameter with the signs of W_j and the negated doubled parameter
−`New.Data.paramW` at τ. 

### `kernelWeight`

 The weight u° on W_j of the kernel of the pair (W_j, V°), a `New.staircaseWeight`. Its diagram
in the negative letters is μ⁻ = `(untwistedDescentPair j).colsMinus τ`, that of the j-th descent
pair at τ. Its shift is j − ⌊m/2⌋. 

### `kernelWeight_of_eq_neg_one`

 The kernel weight `kernelWeight j τ c` at a basis vector `c` of `W_j` with `D.signsW j c = -1`
is the sum of three terms. The first is the shift `j - D.m / 2`. The second is the rank
`card D.SecondFactorIndex` of `V°`. The third is the number of columns of μ⁻ of height `x` with
`numbering c < x < card D.SecondFactorIndex`. 

### `six_mul_r_le_n`

 Six times the rank `r` of `W_j` is at most the largest rank `n_m = D.n m`. 

### `hundred_mul_m_add_nine_lt_k`

 The rank `k` of the source exceeds `100 m + 9`. 

### `t_eq_five_mul_r`

 The number `t = D.t` is five times the rank `r` of `W_j`. 

### `card_firstFactorIndex`

 The index set of `V″` has `r + 9 m + 1` elements: `r` for `W_j`, `3 m` for the padding and
`6 m + 1` for `W♭`. 

### `two_mul_card_detIndex_add_le`

 Twice the sum of the number of determinants in the positive columns at `τ` (`DetIndex j τ`), the
rank of `V″` and `m` is at most `5 b`, with `b = D.b` the size parameter of the weights
`D.liftWeight j`. 

### `conjHolomorphicWeight_eq_add_kernelWeight`

 Let `D` be admissible data, `1 ≤ j ≤ m`, `τ` an infinite place and `W_j` the hermitian space
with signs `D.signsW j`. The weight `conjHolomorphicWeight j τ` on the basis of `W_j`, the highest
weight of the lowest `K`-type for the parameter `-D.paramW τ`, is the sum of two staircase weights.
Here `staircaseWeight n s o k γ` takes at a vector `c` the value `γ - N` if `s c = 1` and
`γ + card n + N` if `s c = -1`, with `N` the sum of `k (s c) i` over `o c < i < card n`. In both
weights `o` is the `numbering` of the vectors within each sign by `untwistedDescentPair j`, the data
of the lift from `W_j` to the definite space of rank `r + t`. The first has `n = FirstFactorIndex j`
of cardinality `r + 9 m + 1`, the column counts `colsPlus τ` in sign `+1`, none in sign `-1`, and
`γ = D.liftWeight j τ - firstFactorCharExp j`. The second, `kernelWeight j τ`, has
`n = D.SecondFactorIndex`, the column counts `colsMinus τ` in sign `-1` and `γ = j - ⌊m / 2⌋`. 

### `conjHolomorphicWeight_of_eq_one`

 At a basis vector `c` of `W_j` of sign `+1`, the weight `conjHolomorphicWeight j τ` is the
integer `κ_j - firstFactorCharExp j + j - ⌊m / 2⌋` minus the number of columns of the partition `μ⁺`
whose height `x` lies strictly between the number of `c` and the cardinality `r + 9 m + 1` of
`FirstFactorIndex j`. Here `(untwistedDescentPair j).colsPlus τ x` counts the columns of `μ⁺` of
height `x`, `κ_j = D.liftWeight j τ`, and all subtractions are in `ℤ`. 

### `conjHolomorphicWeight_of_eq_neg_one`

 At a basis vector `c` of `W_j` of sign `−1`, the weight `conjHolomorphicWeight j τ c` equals
`kernelWeight j τ c` plus `D.liftWeight j τ - firstFactorCharExp j + card (FirstFactorIndex j)`, an
amount that does not depend on `c`. 

### `mul_nStar_le_sum_colsMinus`

 At a basis vector `c` of `W_j` of sign `−1` in `D.signsW j`, consider the sum of
`(untwistedDescentPair j).colsMinus τ x`, the number of columns of height `x` of `μ⁻`. The sum runs
over `x` strictly between `(untwistedDescentPair j).numbering c` and the cardinality of
`SecondFactorIndex`. It is at least `300 * nStar D`. 

### `abs_conjHolomorphicWeight_le`

 The entries of the weight `conjHolomorphicWeight j τ` are at most `5 b` in modulus, with
`b = D.b`. 

### `isKDominant_kernelWeight`

 For `1 ≤ j ≤ m` and an infinite place `τ`, the weight `kernelWeight j τ` on the basis of `W_j`
is `K`-dominant for the order `orderW j`. That is, on basis vectors of one sign `D.signsW j`, it
decreases weakly along this order. 

### `isKDominant_conjHolomorphicWeight`

 Let `1 ≤ j ≤ m`, let `τ` be an infinite place and `D.signsW j` the signs of the basis vectors of
the hermitian space `W_j`. The weight `conjHolomorphicWeight j τ` is `K`-dominant for the order
`orderW j`, which lists the basis vectors by decreasing `D.basisNumber` within each sign: it
decreases weakly along this order on vectors of one sign. 

### `hasHolGap_kernelWeight`

 Every entry of the weight `kernelWeight j τ` at an index of sign `-1` in `D.signsW j` exceeds
every entry at an index of sign `+1` by at least `300 * nStar D`. 

### `hasHolGap_conjHolomorphicWeight`

 Every entry of the weight `conjHolomorphicWeight j τ` at a vector of sign `-1` exceeds every
entry at a vector of sign `+1` by at least `300 n_*`. Here `n_* = nStar D = 2 f t ^ 3`, with
`f = D.f` the number of infinite places of `D.E` and `t = D.t = 5 r` for the rank `r` of `W_j`. 

### `isPosFirstOrder_orderW`

 The order `orderW j` on the basis of `W_j` has distinct values and puts every vector of sign
`+1` before every vector of sign `−1` (`IsPosFirstOrder`). 

### `paramW_lt_of_orderW_lt`

 If two basis vectors of W_j have the same sign under `New.Data.signsW` and the first comes
before the second in `New.Data.orderW`, then the doubled row parameter `New.Data.paramW` at τ is
smaller at the first. 


## Places of the modulus of a twist and tameness of twisted characters

For a twist `ϑ` and `c ≠ 0`, the modulus `D.twistModulus ϑ c` is the `c`-th power of the product of
the chosen places (`New.Data.IsChosen`) times the product of the places in `ϑ.Q`.


### `fact_piM_pow_ne_zero`

 The powers of `ϖ = D.piM` are not zero. 

### `places_twistModulus`

 For c ≠ 0 and a tame character ϑ, the finite places of E dividing the modulus
`D.twistModulus ϑ c` are exactly the chosen places (`New.Data.IsChosen`) together with the places in
the set Q of ϑ. 

### `isTameFor_of_hasWeight`

 Let `ϑ` be a twist: a character of `U(1)(𝔸)` of weight `0` whose tame part, a family of
characters of the residue fields, is non-trivial exactly on the finite set of places `ϑ.Q`. Let
`c ≠ 0` and let `D.twistModulus ϑ c` be the `c`-th power of the product of the chosen places
`D.IsChosen` times the product of the places in `ϑ.Q`. Let `ν` be a character of `U(1)(𝔸)`, trivial
on rational points, of weight `γ` and tame part `ψ * ϑ.tamePart`, where `ψ` is non-trivial exactly
at the chosen places. Then `ν` is tame for this modulus: its tame part is non-trivial exactly at the
places dividing it. 

### `isTameFor_twistedChiMPow`

 Let `j : D.LiftIndex`, that is `1 ≤ j ≤ m`, let `c ≠ 0` and let `ϑ` be a twist, ramified exactly
on the set of places `ϑ.Q`. The modulus `D.twistModulus ϑ c` is the `c`-th power of the product of
the chosen places times the product of the places in `ϑ.Q`. The character `twistedChiMPow ϑ j` =
χ^j·ϑ, with χ = `D.chiM` of tame part ω = `D.chiMLocal`, has weight 0 and ramifies exactly at the
places dividing this modulus, with the character ∏_w ω_w^j ϑ_w of the residue ring. 


## Integral vectors with a monomial Fock polynomial

Here `X` is lift data from `U(1)` to a definite unitary group. For a monomial, an integral vector is
found whose Fock polynomial (`New.DescentPair.fockPoly` of `X.descentPair`) is a multiple of
that monomial.


### `New.toPoly_coeff_nablaBasis`

 For each `τ` in `Φ` take variables in rows `n τ` and columns `ℕ`, and the partition with `κ τ h`
columns of height `h < rankAt n τ = card (n τ)`. The space `nablaFamily ℂ n κ` of polynomials that
are semi-invariant of this weight under the Borel subgroup acting on columns has the basis
`nablaBasis` of products of minors, one minor for each column. The map `toPoly` sends `ξ` to
`∑ i, (G ξ) i • nablaBasis i` with `G` the Gram matrix `weylGram`. If the monomial with exponent `δ`
is semi-invariant, then `toPoly` sends the vector of its coefficients in the basis polynomials to
the monomial times `hookNumber κ (rankAt n) / δ!`. 

### `New.schur_mulVec_coeff_nablaBasis`

 Let `R` be a field of characteristic zero and `g τ` square matrices over `R`, one for each
`τ`. Suppose the substitution `y ↦ gᵀ y` of the rows of variables (`rowSubst`) fixes the monomial
with exponent `δ`. Then the Schur matrix `schur κ g` for the weight `κ` fixes the vector whose
entry at `i` is the coefficient of that monomial in the basis polynomial `nablaBasis R n κ i`, a
product of minors. 

### `New.Rows.exists_int_weylRep_invariant_fockPoly_eq_smul_monomial`

 Let `X` be lift data from `U(1)` to a definite unitary group with index set `n`. They give a
natural number `X.rowLength τ` for each infinite place `τ`, and the weight of the lift at `τ` is the
partition with one row of that length. Let `α` be the exponent of a monomial in `r` rows, placed in
`n` by `e`, of degree `X.rowLength τ` at each `τ`. Then there is an integer vector `v` such that
`fockPoly` of its complex conjugate is `∏_τ (X.rowLength τ)! / α!` times that monomial in the rows
`e`. Over every field of characteristic zero, `weylRep` fixes `v` under every family `g` whose
columns `e` are those of the identity. 
