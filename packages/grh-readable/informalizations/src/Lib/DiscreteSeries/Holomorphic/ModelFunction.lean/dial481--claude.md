---
{
  "module": "src/Lib/DiscreteSeries/Holomorphic/ModelFunction.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/DiscreteSeries/Holomorphic/ModelFunction.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/DiscreteSeries/Holomorphic/ModelFunction.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The holomorphic model function and discrete series coefficients in the holomorphic chamber

For signs `ε` on the indices and weights `u τ`, the model function `New.holMinorsPi ε u` is a
product over τ of quotients of products of principal minors `New.weightMinors` with weights
`u τ + c τ` and `c τ`. Here `c τ` is a large constant on the indices of sign `1` and zero elsewhere.
In the main results the order `o` puts the signs `1` first and each weight `u τ` is K-dominant for
it. With the indices numbered `1, …, n` along `o` and `u τ (n + 1) = 0`, each quotient is then the
product of the leading minors of size `i` to the powers `u τ i - u τ (i + 1)`, and the model
function is holomorphic of weight `u` (`New.IsHolOfWeight`). Let `w` be a K-dominant weight that
jumps up by at least `γ > 500 n³ + A + n + 1` from the first block to the second, where `n` stands
for the number of indices and `A` is a given natural number. Then the discrete series coefficient of
the parameter `2 w + 2 ρ` (`New.twoRho`) is the model function `New.holMinors ε w`.

## Main definitions and results

* `New.isHolOfWeight_holMinorsPi`: `New.holMinorsPi ε u` is holomorphic of weight `u`.
* `New.IsHolOfWeight.circle_mean_holMinorsPi`: for `F` holomorphic of weight `u`, the mean over
  `|s| = 1` of `F (diag (s ^ o) * h)` divided by the character of weight `u` is
  `New.holMinorsPi ε u h * F 1`.
* `New.IsHolOfWeight.integral_mul_conj_holMinorsPi`: the reproducing formula
  `∫ F * conj m = (∫ |m|²) * F 1` for `m = New.holMinorsPi ε u`, if `F * conj m` is integrable.
* `New.IsHolOfWeight.eq_holMinorsPi_mul`: if `F g⁻¹ = conj (F g)`, then `F` is `F 1` times the model
  function.
* `New.dsCoeff_eq_holMinors`: for `w` as above, the parameter `2 w + 2 ρ` has gap `500 n³ + A`, and
  its coefficient `New.HCParam.dsCoeff` equals `New.holMinors ε w` on the unitary group. For the
  proof write a `g` near `1` as `x' * a * x` with `a` block diagonal and `x' - 1`, `x - 1` in the
  corner blocks; neither side sees `x'` and `x`, both agree at `a`, and both are analytic.

Notions from other files:
* `New.USign`: For a vector of signs ε, the unitary group U(J) of the diagonal matrix J = diag(ε).
* `New.IsHolOfWeight`: The function F on U(diag ε)^Φ extends analytically to products h b with b
  invertible and triangular for the order o, and the extension is the character of weight u at b
  times F(h). Optional signs ε' restrict h and b to block diagonal matrices; the default ε' = 1 is
  no restriction.
* `New.IsPosFirstOrder`, `New.IsKDominant`: The order o has distinct values and puts the signs +1
  first; the weight w satisfies w_j ≤ w_i whenever ε_i = ε_j and o_i < o_j.

## Relation to the literature

Known; see `Lib.DiscreteSeries.Holomorphic.HighestVectorExtension` for sources.


 ## Holomorphy of the model function, circle mean and reproducing formula 

### `holMinors_ite_sign`

 For the weight that is `a` on the indices of sign `1` and `b ≥ a` elsewhere, the quotient of
minors `New.holMinors` is `det ^ b` divided by the `(b - a)`-th power of the principal minor on
the indices of sign `1`. 

### `holMinorsPi_eq_div`

 `New.holMinorsPi ε u` is the quotient of the products over τ of the minors of weights
`u τ + c τ` and `c τ`, where `c τ` is `2 * ∑ j, |u τ j|` on the indices of sign `1` and zero
elsewhere. 

### `holMinorsPi_diagTorus_mul`

 Left translation by `diag t`, with `|t i| = 1`, multiplies `New.holMinorsPi ε u` (a product of
quotients of principal minors of weights `u τ`) by the character of weight `u` at `t`. 

### `IsPosFirstOrder.isKDominant_shift`

 Let the order `o` be injective with the signs `1` first and each `u τ` be K-dominant, that is,
decrease weakly along `o` within the indices of each sign. Let `c` be `2 * ∑ j, |u τ j|` on the
indices of sign `1` and zero elsewhere. Then the weights `u τ + c` and `c` of the numerator and
the denominator of `New.holMinors` both decrease weakly along the whole order `o`. 

### `isHolOfWeight_holMinorsPi`

 If the order o is injective with the indices of sign +1 first, and every u^τ is K-dominant
for o (decreases weakly within the indices of each sign), then `New.holMinorsPi ε u`, the product
of the quotients of principal minors of weights u^τ on U(diag ε)^Φ, is holomorphic of weight u:
it extends analytically with the character of weight u as factor under triangular matrices. 

### `IsHolOfWeight.circle_mean_holMinorsPi`

 Let `o` put the signs `1` first, let each `u τ` be K-dominant for `o` (decreasing weakly within
the indices of each sign), and let `F` be holomorphic of weight `u` (`New.IsHolOfWeight`:
analytically extensible with the character of weight `u` as factor under triangular matrices).
Translate `h` on the left by the diagonal matrix with entries `s ^ o i` and divide `F` by the
character of weight `u`. The mean over `s` in the unit circle is `holMinorsPi ε u h * F 1`, where
`holMinorsPi` is the product of the quotients of principal minors of weights `u τ`. 

### `IsHolOfWeight.integral_mul_conj_holMinorsPi`

 The reproducing formula. Let `o` put the signs `1` first, let each `u τ` be K-dominant for `o`
(decreasing weakly within the indices of each sign), and let `F` be holomorphic of weight `u` on
U(diag ε)^Φ (analytically extensible with the character of weight `u` under triangular matrices).
If `F * conj m` is integrable for the invariant measure, where `m = holMinorsPi ε u` is the
product of quotients of principal minors of weight `u`, then its integral is `F 1` times the
integral of `|m|²`. 

### `IsHolOfWeight.eq_holMinorsPi_mul`

 Let the order `o` be injective with signs `1` first, each `u τ` K-dominant (decreasing weakly
within the indices of each sign), and `F` holomorphic of weight `u` on U(diag ε)^Φ (analytically
extensible with the character of weight `u` under triangular matrices) with `F g⁻¹ = conj (F g)`.
Then `F` is `F 1` times `New.holMinorsPi ε u`, the product of quotients of principal minors. 


## Discrete series coefficients in the holomorphic chamber

Parameters are doubled, `l = 2 λ`.


 ### Matrices in a corner block 

### `IsInCornerBlock`

 The matrix `y` lies in the corner block with rows of sign `s` and columns of sign `-s`: all
other entries vanish. If the signs `1` come first, this is the upper right block for `s = 1` and the
lower left block for `s = -1`. 

### `IsInCornerBlock.mul_mul`

 A corner block is stable under multiplication by block diagonal matrices on both sides. 

### `IsInCornerBlock.conj_sub_one`

 If `x - 1` lies in a corner block, then so does `kᴴ * x * k - 1` for `k` in
`K = U(diag ε) ∩ U(n)`. 

### `IsInCornerBlock.isBorelMatrix_and_diagChar_eq_one`

 Let `x - 1` lie in the corner block with rows of sign `s`, and let the injective order `o` put
the signs `s` before the signs `-s`. Then `x` is upper unipotent for `o`: it is invertible and upper
triangular (`New.IsBorelMatrix`), and every character `diagChar w x = ∏ i, x i i ^ w i` of the
diagonal is `1`. 

### `IsBorelMatrix.of_mem_blockDiagAlg`

 A block diagonal matrix that is invertible and upper triangular for the order `o`
(`New.IsBorelMatrix`) is so for every order `o'` whose strict inequalities inside the blocks hold
for `o` too. 

 ### Factorisations near the identity 

### `eventually_exists_eq_lower_mul_borel`

 Each block diagonal matrix `y` near `1` is `(1 + z) * b`, where `z` is block diagonal and
strictly lower triangular for the order `o`, and `b` is block diagonal, invertible and upper
triangular. Both factors lie in a given neighbourhood `P` of `1`. The order `o` may have ties. 

### `eventually_exists_eq_corner_mul_mul_corner`

 Each matrix `g` near `1` is `x' * a * x` with `a` block diagonal and in a given neighbourhood
`P` of `1`, with `x - 1` in the upper right block (rows of sign `1`, columns of sign `-1`) and
`x' - 1` in the lower left block. 

### `IsKDominant.weightMinors_mul_mul_of_isBorelMatrix`

 For a weight that decreases weakly along the injective order `o`, multiplying by an invertible
lower triangular `b'` on the left and an upper triangular `b` on the right multiplies
`weightMinors v` (the product of the leading minors of size `i` along `o` to the powers
`v i - v (i + 1)`, with `v (n + 1) = 0`) by the characters of the two diagonals. 

 ### The model function 

### `holMinors_oppBorel_mul_mul_borel`

 Let the order `o` put the signs `1` first and let `w` decrease weakly within each block. For
invertible `b'`, `y`, `b` with `b'` lower and `b` upper triangular for `o`, the model function
`holMinors ε w` at `b' * y * b` is its value at `y` times `∏ i, b' i i ^ w i` and
`∏ i, b i i ^ w i`. 

### `analyticAt_holMinors`

 With `c = 2 * ∑ j, |w j|` on the indices of sign `1` and zero elsewhere, `holMinors ε w` is the
quotient of the products of principal minors of weights `w + c` and `c`. It is analytic at each
point of `U(diag ε)`, for every weight `w`. 

### `USign.eq_of_analyticAt_of_eventually_eq`

 Let `f` and `f'` be functions of a matrix that are analytic at each point of `U(diag ε)`. If
they agree on a neighbourhood of `1` in the group, they agree on the whole group. 

 ### The coefficient in the holomorphic chamber 

### `HCParam.HasGap.isKDominant_lowestKType_of_order`

 If the parameter `l`, of some gap `h` (its entries are distinct, of the parity of `n - 1`, and
those of `l / 2` at opposite signs are at least `h` apart), decreases along the order `o` within
each block of equal signs, then the highest weight `l.lowestKType` of its lowest `K`-type decreases
weakly along `o` in each block. 

### `flenstedJensen_corner_mul_mul_corner`

 Let `l` be a parameter of some gap `h` (in particular with distinct entries) whose entries at
the signs `1` lie below those at the signs `-1`. Let `a` be invertible, `x' - 1` in the lower left
and `x - 1` in the upper right block. Then Flensted-Jensen's integral `l.flenstedJensen 1` (an
integral over `k` in `K` whose integrand has denominator
`weightMinors (-paramAddRho l) (kᴴ * g * k)`), based at the identity, has the same value at
`x' * a * x` and at `a`. 

### `eventually_flenstedJensen_eq_holMinors_of_mem_blockDiagAlg`

 Let the order `o` put the signs `1` first, and let the parameter `l` decrease along `o` within
each block. It has some gap `h`: its entries are distinct, of the parity of `n - 1`, and those of
`l / 2` at opposite signs are at least `h` apart. On block diagonal matrices `a` near `1`,
Flensted-Jensen's integral `l.flenstedJensen 1 a` (based at the identity; an integral over `k` in
`K` with denominator `weightMinors (-paramAddRho l) (kᴴ * a * k)`) is the model function
`holMinors`, a quotient of products of principal minors, for the highest weight `l.lowestKType` of
the lowest `K`-type. 

### `dsCoeff_eq_holMinors_lowestKType`

 Let the order `o` put the signs `1` first. Let the parameter `l` (distinct entries of the parity
of `n - 1`, with some gap `h` between opposite signs) decrease along `o` within each block, and let
its entries at the signs `1` lie below those at the signs `-1`. Then the coefficient `l.dsCoeff`,
the normalised integral of Flensted-Jensen, equals on `U(diag ε)` the model function `holMinors`,
a quotient of products of principal minors, for the highest weight `l.lowestKType` of the lowest
`K`-type. 

### `dsCoeff_eq_holMinors`

 The holomorphic chamber. Let the order `o` on the `n` indices put the signs `1` first. Let `w`
decrease weakly along `o` within each block of equal signs, and let `w i + γ ≤ w j` for `ε i = 1`,
`ε j = -1`, where `γ > 500 n³ + A + n + 1`. Let `l = 2 w + 2 ρ`, where
`2 ρ a = #{j | o a < o j} - #{j | o j < o a}`; so `l = 2 λ` with `λ a = w a + (n + 1) / 2 - r` for
`r = 1, …, n` the rank of `a` in `o`. Then (a) `l` satisfies `HCParam.HasLargeGap A`, i.e. it is a
parameter for the signs `ε` with gap `500 n³ + A`; (b) for every `g` in the unitary group
`U(diag ε)`, the coefficient `New.HCParam.dsCoeff l g` equals `New.holMinors ε w g`.

Here `dsCoeff` is the normalised integral of Flensted-Jensen and `holMinors` the quotient of
principal minors of weight `w`. 
