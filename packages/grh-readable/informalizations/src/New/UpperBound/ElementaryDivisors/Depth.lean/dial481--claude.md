---
{
  "module": "src/New/UpperBound/ElementaryDivisors/Depth.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/ElementaryDivisors/Depth.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/ElementaryDivisors/Depth.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Few forms have only deep translates

Let `T` be a Frobenius cycle over a field `K` of characteristic `p`. The space
`New.FrobeniusCycle.deepForms` consists of the forms all of whose translates have only monomials of
depth at least `δ`. Such a form vanishes to order `δ` at many points, which are cut out by equations
with small leading powers, so it has a monomial of large weighted degree. The sum of the weighted
degrees of all monomials therefore bounds the sum of the dimensions of these spaces. With
`New.FrobeniusCycle.exists_originFunctions_factorization_det_dvd`, the bound leads to the theorem on
elementary divisors, `New.FrobeniusCycle.elementary_divisors`.

Notions from other files:
* `New.FrobeniusCycle N W K`: a prime `p` with a power `P`, ring maps `embedding s : W → K` for the
  letters `s` in `ZMod N`, which are alternately even and odd, and a residue field of `W` with
  `q = P ^ N` elements.
* `New.FrobeniusCycle.deepIndicator`: the indicator of the variables `(b, s)` that are deep for `r`,
  that is, `s` is even and `r ≤ b`, or `s` is odd and `b < r`.
* `New.Exponents N k n`, `New.polyOfCoeffs`: the exponents of the monomials in the variables
  `(b, s)` of degree `n` in each letter, and the polynomial with given coefficients at them.
* `New.FrobeniusCycle.polyAction`: the action of `GL_k(W)` on polynomials in the variables `(b, s)`.

## Main definitions and results

* `New.FrobeniusCycle.entryRow`, `New.FrobeniusCycle.entryCol`: for `k = 2 r + m`, the row `< r` and
  the column `≥ r` of the position in a `k × k` matrix named by `t` in `Fin r × Fin (m + 1)`.
* `New.FrobeniusCycle.entryFormValue`: the point attached to residues `y t` at the positions. Its
  coordinates are linear forms in lifts of the `y t`, with coefficients
  `New.FrobeniusCycle.entryCoeff`, each zero or a variable up to sign.
* `New.FrobeniusCycle.exists_le_weight_of_mem_deepForms`: a non-zero form in
  `New.FrobeniusCycle.deepForms` has a monomial of large weight.
* `New.FrobeniusCycle.sum_finrank_deepForms_le`: the dimensions of the spaces of forms all of whose
  translates have depth at least `1, 2, …, M` add up to at most `New.FrobeniusCycle.divisorConstant`
  times the number of exponents.

## Relation to the literature

See `New.UpperBound.ElementaryDivisors.DefectCount` for related work.


 ## Deep forms have a monomial of large weight 

### `sum_deepIndicator`

 For every `r` and every index `b`, the variable `(b, s)` is deep for half of the letters `s` in
`ZMod N`: even and odd letters (`T.isEven`) alternate, and `T.deepIndicator r (b, s)` is `1` if `s`
is even and `r ≤ b`, or `s` is odd and `b < r`, and `0` otherwise. 

### `exists_div_two_eq_and_isEven_sub`

 Even and odd letters alternate, so for every `b` the letter `i - j` is even for one of
`j = 2 b` and `j = 2 b + 1`. 

### `residue_eq_of_embedding_eq`

 Elements of the local ring `W` with the same image under the ring map `T.embedding s` to the
field `K` have the same residue. 

### `deepOrder`

 The degree given to the variable `v = (b, s)` in the count of common zeros behind
`New.FrobeniusCycle.exists_le_weight_of_mem_deepForms`, a power of `P = T.P`: it is `P ^ (2 r)` if
`v` is deep for `r` (`T.deepIndicator r v = 1`) and `2 r ≤ b`, `P` if `v` is deep and `b < 2 r`, and
`1` if `v` is not deep. 

### `prod_deepOrder_le`

 For `k = 2 r + m`, the product of the degrees `T.deepOrder r v` over all variables is at most
`q ^ (r (m + 1))`, the number of families of `r (m + 1)` residues of `W`, whose residue field has
`q = T.q = P ^ N` elements. 

### `letterRep_mulVec_eq_zero_of_mem_deepForms`

 If `F` lies in `T.deepForms k n r τ`, the coefficient of its translate by `g` (the matrix of `g`
on coefficient vectors is `T.letterRep n g`) vanishes at every monomial `β` whose degree in the
variables that are deep for `r` is below `τ`. 

### `map_polyOfCoeffs_mem_pow_of_mem_deepForms`

 Let `F` lie in `T.deepForms k n r τ`. If a ring map `ψ` sends the translates by `g⁻¹` of the
deep variables into an ideal `𝔪`, then it sends the form with coefficients `F` into `𝔪 ^ τ`. 

### `specializeShallow`

 For a ring map `x` from the polynomials to `L`, the ring map to polynomials over `L` that keeps
the variables that are deep for `r` and sends the constants and the other variables to their images
under `x`. 

### `specializeShallow_injective`

 If `x` is injective, so is `T.specializeShallow r x`. This is the ring map that keeps the
variables deep for `r` and reads the constants and the other variables in `L` through `x`. A
variable `X (b, s)` is deep for `r` if `T.isEven s` and `r ≤ b`, or if `s` is odd and `b < r`. 

### `specializeShallow_polyOfCoeffs_ne_zero`

 If `x` is injective, the ring map `T.specializeShallow r x` does not send the polynomial with
coefficients `F ≠ 0` to zero. 

### `exists_eq_of_mem_support_specializeShallow`

 The ring map `T.specializeShallow r x` keeps the deep variables and reads the others in `L`
through `x`. Each monomial `α` of its value at the polynomial with coefficients `F` is the deep part
(the exponents at the variables with `T.deepIndicator r v ≠ 0`) of the exponent vector
`exponentOf β` of a monomial `β` with `F β ≠ 0`. 

### `_root_.New.det_X_pow_ne_zero`

 Let the variable `v u b` determine `b`, and let the exponents `e u` be positive and distinct.
The determinant of the matrix of the powers `X (v u b) ^ e u` is a signed sum of distinct
monomials, so it is not zero. 


The pairs in `Fin r × Fin (m + 1)` name the positions where a `k × k` matrix `A` over `W` may have
non-zero entries.


### `entryRow`

 For `k = 2 r + m`, the pair `t = (a, l)` with `a < r` and `l ≤ m` names a position of a `k × k`
matrix in the row `a`. 

### `entryCol`

 For `k = 2 r + m`, the pair `t = (a, l)` names a position of a `k × k` matrix in the column
`a + r` if `l = 0`, and in the column `k - l ≥ 2 r` otherwise. 

### `entryCoeff`

 Let the position `t = (a, l)` lie in the row `a` and the column `c`, which is `a + r` if
`l = 0` and `k - l` otherwise
(`entryRow`, `entryCol`), and let `s` be the letter (second component) of `v`. This polynomial is
`X (a, s)` if `s` is even and `v = (c, s)`, it is `-X (c, s)` if `s` is odd and `v = (a, s)`, and it
is `0` otherwise; `T.rootVar` picks the index by the parity of `s`. For a matrix `A` over `W`
supported on the positions, the translate of `X v` by `(1 + A)⁻¹` is `X v` minus a linear form in
the entries of `ι_s(A)`, where `ι_s = T.embedding s`, and this is its coefficient at `t`. 

### `lowPowerForms`

 The span over `L` of the vectors `t ↦ x (T.entryCoeff hm v t) ^ P ^ j`, for the variables
`v = (b, s)` and the `j` with `s + j = i` and `P ^ j < T.deepOrder r v`. Let `A` be a matrix over
`W` supported on the positions `t`, and `ι_s = T.embedding s`. In characteristic `p`, the `P ^ j`-th
power of the linear form with coefficients `T.entryCoeff hm v` in the entries of `ι_s(A)` is a
linear form in the entries of `ι_i(A)`, and such a vector holds its coefficients, read in `L`
through `x`. 

### `single_mem_lowPowerForms_of_ne_zero`

 If `x` embeds the polynomials over `K` in a field `L` and `l ≠ 0`, the space
`T.lowPowerForms hm x i` contains the unit vector at `(b, l)`. 

### `single_zero_mem_lowPowerForms`

 If `x` embeds the polynomials over `K` in a field `L`, the space `T.lowPowerForms hm x i`
contains the unit vector at `(b, 0)`. 

### `mem_lowPowerForms`

 If `x` embeds the polynomials over `K` in a field `L`, the space `T.lowPowerForms hm x i`
contains every vector. 

### `entryFormValue`

 The point attached to the matrix `A` whose entries `(y t).out` at the positions `t` lift the
residues `y t`: its coordinate `v = (b, s)` is the linear form with coefficients `T.entryCoeff hm v`
in the entries of `ι_s(A)`, where `ι_s = T.embedding s`, read in `L` through `x`. 

### `entryFormValue_pow`

 In characteristic `p`, raising a coordinate of the point `T.entryFormValue hm x y` to the power
`P ^ j` raises its coefficients to that power and moves its letter `s` to `s + j`.

The Frobenius cycle `T` gives a power `P = T.P` of the prime `p = T.p`, ring maps
`ι_s = T.embedding s : W → K` on the local ring `W` for the letters `s` in `ZMod N`, and a parity
`T.isEven s` that alternates with `s`. For `k = 2 r + m`, a pair `t = (a, l)` in
`Fin r × Fin (m + 1)` names the position of a `k × k` matrix in the row `a` and the column `a + r`
if `l = 0` and `k - l` otherwise. 

### `exists_specializeShallow_polyAction_X_eq_sub`

 There is `g` in `GL_k(W)` such that the ring map `T.specializeShallow r x`, which keeps the deep
variables and reads the constants and the other variables in `L` through `x`, sends the translate by
`g⁻¹` of each deep variable `X v` to `X v - z v`.

The Frobenius cycle `T` gives a power `P = T.P` of the prime `p = T.p`, ring maps
`ι_s = T.embedding s : W → K` on the local ring `W` for the letters `s` in `ZMod N`, and a parity
`T.isEven s` that alternates with `s`. An element `g` of `GL_k(W)` translates polynomials by the
substitution `T.polyAction g`, which sends `X (b, s)` to `∑ c, g_s c b * X (c, s)`, where `g_s` is
`ι_s` applied to the entries of `g` for even `s` and of its inverse transpose for odd `s`.

For `k = 2 r + m`, a pair `t = (a, l)` in `Fin r × Fin (m + 1)` names the position of a `k × k`
matrix in the row `a` and the column `a + r` if `l = 0` and `k - l` otherwise. For residues `y t` of
`W` with lifts `(y t).out`, the point `z = T.entryFormValue hm x y` has the coordinate
`x (∑ t, C (ι_s (y t).out) * T.entryCoeff hm v t)` at `v = (b, s)`. 

### `_root_.New.exists_eval_eq_dotProduct_of_mem_span`

 Suppose that for each `u` in `S` there are `v` and `e < o v` with `u ⬝ᵥ a y = z y v ^ e` for
all `y`. Then for each `u` in the span of `S` one polynomial has the value `u ⬝ᵥ a y` at `z y` for
all `y`, and its monomials have cost below `1`, where the variable `v` costs `1 / o v`. 

### `exists_eval_entryFormValue_eq_dotProduct`

 Let `x` embed the polynomials over `K` in a field `L`, both fields of characteristic `p`. Each
linear form `∑ t, u t * x (C (ι_i (y t).out))` is the value at the point `z` of a polynomial that
does not depend on `y` and whose monomials cost less than `1`, where the variable `v` costs
`1 / T.deepOrder r v`.

The Frobenius cycle `T` gives a power `P = T.P` of the prime `p = T.p`, ring maps
`ι_s = T.embedding s : W → K` on the local ring `W` for the letters `s` in `ZMod N`, and a parity
`T.isEven s` that alternates with `s`.

For `k = 2 r + m`, a pair `t = (a, l)` in `Fin r × Fin (m + 1)` names the position of a `k × k`
matrix in the row `a` and the column `a + r` if `l = 0` and `k - l` otherwise. For residues `y t` of
`W` with lifts `(y t).out`, the point `z = T.entryFormValue hm x y` has the coordinate
`x (∑ t, C (ι_s (y t).out) * T.entryCoeff hm v t)` at `v = (b, s)`. 

### `exists_eval_entryFormValue_eq_pow_deepOrder`

 Let `x` embed the polynomials over `K` in a field `L`, both fields of characteristic `p`. For
each variable `v` there is a polynomial that does not depend on `y`, has the value
`z v ^ T.deepOrder r v` at the point `z`, and whose monomials cost less than `1`, where the variable
`w` costs `1 / T.deepOrder r w`.

The Frobenius cycle `T` gives a power `P = T.P` of the prime `p = T.p`, ring maps
`ι_s = T.embedding s : W → K` on the local ring `W` for the letters `s` in `ZMod N`, and a parity
`T.isEven s` that alternates with `s`.

For `k = 2 r + m`, a pair `t = (a, l)` in `Fin r × Fin (m + 1)` names the position of a `k × k`
matrix in the row `a` and the column `a + r` if `l = 0` and `k - l` otherwise. For residues `y t` of
`W` with lifts `(y t).out`, the point `z = T.entryFormValue hm x y` has the coordinate
`x (∑ t, C (ι_s (y t).out) * T.entryCoeff hm v t)` at `v = (b, s)`. 

### `entryFormValue_injective`

 Let `x` embed the polynomials over `K` in a field `L`, both fields of characteristic `p`. Then
the point `z` determines the residues `y t`.

The Frobenius cycle `T` gives a power `P = T.P` of the prime `p = T.p`, ring maps
`ι_s = T.embedding s : W → K` on the local ring `W` for the letters `s` in `ZMod N`, and a parity
`T.isEven s` that alternates with `s`. For `k = 2 r + m`, a pair `t = (a, l)` in
`Fin r × Fin (m + 1)` names the position of a `k × k` matrix in the row `a` and the column `a + r`
if `l = 0` and `k - l` otherwise. For residues `y t` of `W` with lifts `(y t).out`, the point
`z = T.entryFormValue hm x y` has the coordinate `x (∑ t, C (ι_s (y t).out) * T.entryCoeff hm v t)`
at `v = (b, s)`. 

### `specializeShallow_polyOfCoeffs_mem_vanishingIdeal_pow`

 If `F` lies in `T.deepForms k n r τ`, its form vanishes to order `τ` at the point `z` once
`T.specializeShallow r x` keeps the deep variables and reads the constants and the other variables
in `L` through `x`.

The Frobenius cycle `T` gives a power `P = T.P` of the prime `p = T.p`, ring maps
`ι_s = T.embedding s : W → K` on the local ring `W` for the letters `s` in `ZMod N`, and a parity
`T.isEven s` that alternates with `s`. The variable `X (b, s)`, of index `b < k` and letter `s`, is
deep for `r` if `s` is even and `r ≤ b`, or `s` is odd and `b < r`; `T.deepIndicator r` is the
indicator of these `(b, s)`. An element `g` of `GL_k(W)` translates polynomials by the substitution
`T.polyAction g`, which sends `X (b, s)` to `∑ c, g_s c b * X (c, s)`, where `g_s` is `ι_s` applied
to the entries of `g` for even `s` and of its inverse transpose for odd `s`. A function `F` on
`Exponents N k n` is the coefficient vector of the form `polyOfCoeffs F` over `K`, of degree `n` in
the `k` variables of each letter. It lies in `T.deepForms k n r τ` if all translates of the form
have only monomials of degree at least `τ` in the deep variables.

For `k = 2 r + m`, a pair `t = (a, l)` in `Fin r × Fin (m + 1)` names the position of a `k × k`
matrix in the row `a` and the column `c`, where `c = a + r` if `l = 0` and `c = k - l` otherwise.
The polynomial `T.entryCoeff hm v t` is `X (a, s)` if `v = (c, s)` with `s` even, `-X (c, s)` if
`v = (a, s)` with `s` odd, and `0` otherwise. For residues `y t` of `W` with lifts `(y t).out`, the
point `z = T.entryFormValue hm x y` has the coordinate
`x (∑ t, C (ι_s (y t).out) * T.entryCoeff hm v t)` at `v = (b, s)`. 

### `exists_le_weight_of_mem_deepForms`

 Let `K` have characteristic `p` and `2 r ≤ k`. A non-zero `F` in `T.deepForms k n r τ` has
`F β ≠ 0` for a monomial `β` of weight at least `τ`. The weight is the sum over the variables of the
exponent (`exponentOf β`) times `P ^ (-2 r)` for a deep variable with `2 r ≤ b`, `1 / P` for a deep
one with `b < 2 r`, and `0` for the others. 

 ## Dimension counts for forms of large depth 

### `New.FrobeniusCycle.divisorConstant`

 The number `N n (P ^ (-2 r) + r ^ 2 / (k P))`, for `N` letters, `k` variables and degree `n` in
each letter, the prime power `P = T.P`, and the index `r` at which deep and shallow variables change
places. In `New.FrobeniusCycle.sum_finrank_deepForms_le`, over a field of characteristic `p` and for
`0 < 2 r ≤ k`, it bounds, up to the factor of the number of exponents, the sum of the dimensions of
the spaces of forms all of whose translates are deep. 

### `New.FrobeniusCycle.divisorConstant_map`

 `T.divisorConstant k n r` depends on `T` only through `P`, so it is unchanged when the Frobenius
cycle is pushed forward along a ring map. 

### `New.mul_sum_exponentOf`

 By symmetry in the variables, the entry at any variable `x = (b, s)` has the mean `n / k` over
all exponents (`New.Exponents`: `N`-tuples of exponents of monomials of degree `n` in `k` variables,
read at `x` by `New.exponentOf`). 

### `New.finrank_le_card_of_forall_exists_ne_zero`

 If every nonzero vector of a subspace `S` of functions on `ι` is nonzero at some point of a
finite set `s`, then `dim S ≤ #s`. 

### `New.FrobeniusCycle.sum_deepIndicator_div_le`

 The variable `x = (b, s)` is deep if `s` is even and `r ≤ b`, or `s` is odd and `b < r`. Give a
deep variable the cost `1 / P ^ (2 r)` if `2 r ≤ b` and `1 / P` otherwise, and the other variables
the cost `0`. For `0 < 2 r ≤ k` the costs add up to at most `N (k / P ^ (2 r) + r ^ 2 / P)`. 

### `New.FrobeniusCycle.sum_finrank_deepForms_le`

 Let `K` have characteristic `p` and `0 < 2 r ≤ k`. For every `M` the dimensions of the spaces
`T.deepForms k n r δ` for `1 ≤ δ ≤ M` add up to at most `T.divisorConstant k n r = N n (P ^ (-2
r) + r ^ 2 / (k P))` times the number of `N`-tuples of monomials of degree `n` in `k` variables. 
