---
{
  "module": "src/New/OneLift/ComparisonOperator/LineCoordinates.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/OneLift/ComparisonOperator/LineCoordinates.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/OneLift/ComparisonOperator/LineCoordinates.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The polynomial map ζ, the datum Ψ^add and the series Υ; norm, degree and denominator of ζ

Fix admissible data `D`, a tame character `ϑ` and an index `1 ≤ j ≤ m`. Write `E^n` for the standard
definite space of rank `n`, V″ for the one on `New.Data.FirstFactorIndex` and
W^add = E^{3m−j} ⊕ W♭ ⊕ E^{3m} for the one on `New.Data.AddedIndex`. Throughout, k = `D.k`,
m = `D.m`, M = `D.M`, and W_j is the space on `D.RowIndex` with r₊ = `D.posRank j` = k + j − 1 plus
signs. This file defines the constant rows 𝖼, the datum Ψ^add and the series Υ, which is built from
theta kernels of definite spaces. It also defines the polynomial map ζ to the Weyl module of μ⁺ with
P_V = P_{ζ(z)}(X). Here P_V has one determinant det(𝖼; X z) for each column of μ⁺, with variables X
in the positive basis vectors of W_j and variables z in W^add. This file bounds the norm, the degree
and the denominator of ζ.

## Main definitions and results

* `New.HasWeightNormSqLe`, `New.HasWeightNormSqLeIf`: "F has weight κ and squared norm at most b",
  outright or under a condition. Under finite products the weights add and the bounds multiply.
* `New.Data.constantRows`, `New.Data.stackedDetProdCoords`: the matrices 𝖼 of 2m constant rows, one
  for each column of μ⁺ at each infinite place (`New.Data.DetIndex`), and the coordinates of ζ.
* `New.Data.addedDatum`, `New.Data.leftSideSeries`: the datum Ψ^add on W^add and the series Υ.
* `New.Data.toPoly_stackedDetProdCoords`, `New.Data.weylNormSq_comp_eval_stackedDetProdCoords_le`:
  P_V is the polynomial of ζ, and when the entries of Y and the values of z are small, the squared
  norm of ζ(z) is bounded.
* `New.Data.exists_isHomogeneousOverEntries_smul_stackedDetProdCoords`: ζ is homogeneous of one
  degree `d`, and one integer `H ≤ (d ^ d) ^ 3` clears its denominators.

Notions from other files:
* `New.toPoly`, `New.weylNormSq`: the polynomial of a coordinate vector of weight κ, and the squared
  norm of the vector for the Gram matrix of κ. Here `κ τ h` counts the columns of height `h` at `τ`.
* `New.Data.DetIndex`: the columns of μ⁺ at the place τ. The number of those of height h < r₊ is
  `(untwistedDescentPair j).colsPlus τ h`, and Δ′ = `D.reducedHalfGap` have height r₊.
* `New.Data.FirstFactorIndex`: the indices of W_j, (E^j)⁻, E^{3m−j} and W♭ = E^{6m+1}.
* `New.Data.ChoiceIndex`: the choices, each a matrix Λ modulo ϖ² with a class h♭ of U(W♭) and rows
  for the columns of height r₊ (`New.Data.RowChoice`).
* `New.Data.TameChar`, `New.Data.twistModulus`: a character `ϑ` of U(1)(𝔸) of weight 0 with tame
  part on a finite set Q = `ϑ.Q` of places, and the moduli ϖ^c Q.

## Relation to the literature

See `New.OneLift.ComparisonOperator.FirstFactors` for related work.


 ## Norm bounds for products of semi-invariants 

### `New.HasWeightNormSqLe`

 `F` is the polynomial (`toPoly`) of a coordinate vector `ξ` of weight `κ` whose squared norm for
the Gram matrix of `κ` (`weylNormSq`) is at most `b`. 

### `New.HasWeightNormSqLe.nonneg`

 A bound on the squared norm of a coordinate vector is nonnegative. 

### `New.HasWeightNormSqLe.mul`

 If `F` is the polynomial of a vector of the Weyl module of weight `κ` with squared norm for the
Gram matrix at most `b` (`HasWeightNormSqLe`), and likewise `G` for `κ'` and `c`, then `F * G` has
weight `κ + κ'` and squared norm at most `b * c`. 

### `New.HasWeightNormSqLe.prod`

 Under a finite product the weights add and the bounds on the squared norm multiply. 

### `New.HasWeightNormSqLeIf`

 `F` is the polynomial of a coordinate vector `ξ` of weight `κ`, and if the condition `p` holds,
the squared norm of `ξ` is at most `b`. 

### `New.hasWeightNormSqLeIf_iff`

 `F` has weight `κ` and, under `p`, squared norm at most `b` exactly when it has weight `κ` and
squared norm at most some `c` with `c ≤ b` under `p`. 

### `New.HasWeightNormSqLeIf.prod`

 If each `F i` has weight `κ i` and, under `p`, squared norm at most `b i`, then the product has
weight `∑ κ i` and, under `p`, squared norm at most `∏ b i`. 

### `New.eval_weylKernel_single_eq_det`

 For the weight with one column of height `h < card N` at `τ`, the kernel `weylKernel` at `y`
(the highest weight polynomial at `yᵀ x`) is the leading `h × h` minor of `yᵀ x` in block `τ`. 

### `New.exists_toPoly_single_eq`

 Let a function `F` of `h` columns be the sum, over the `h`-subsets `S` of `N`, of the minor on
`S` times the value of `F` at the unit columns on `S`. Take the weight whose diagram is one column
of height `h < card N` at the place `τ` in `Φ` and is empty at the other places; `WeylIndex` indexes
a basis of its Weyl module. Then `F` is the polynomial `toPoly ξ` = ∑ (G ξ)ᵢ bᵢ of a vector `ξ`,
where G is the Gram matrix and the bᵢ are the basis products of minors, and the squared norm
`weylNormSq ξ` = ξ* G ξ is the sum of the squared moduli of these values. 

### `New.exists_toPoly_eq_det_and_weylNormSq_le`

 Take the weight whose diagram is one column of height `h < card N` at the place `τ` in `Φ` and
is empty at the other places; `WeylIndex` indexes a basis of its Weyl module. The determinant of the
matrix `((0; X) | Z)`, with variables `X` in `h` columns and with columns indexed through `e`, is
the polynomial `toPoly ξ` = ∑ (G ξ)ᵢ bᵢ of a vector `ξ`, where G is the Gram matrix and the bᵢ are
the basis products of minors. The squared norm `weylNormSq ξ` = ξ* G ξ is at most the product of the
squared lengths of the columns of `Z`. 


## Index sets, constant rows, datum and series

`modKernelStdSpace S a b 𝔪 Ψ P` is the theta kernel of a space `S` and a standard definite space,
with characters `a`, `b`, a function `Ψ` on matrices modulo `𝔪` and a polynomial `P`.
`New.stdClassSum K` is the class sum of level `K` on a standard definite space. `New.inclMatrix` is
the matrix of a map of index sets.


### `RowChoice.classRep`

 The chosen representative h♭ in U(W♭)(𝔸_f) of the class in `i`. 

### `RowChoice.rows`

 The row indices chosen in `i`: `i.rows τ k` is the k-th list of 2m rows at the place τ. 

### `ChoiceIndex.matrix`

 The matrix Λ modulo ϖ² of the choice `i`. 

### `ChoiceIndex.rowChoice`

 The class h♭ and the rows of the choice `i`. 

### `AddedIndex`

 The index set of the definite space W^add = E^{3m−j} ⊕ W♭ ⊕ E^{3m}, with W♭ = E^{6m+1}. 

### `regroupEquiv`

 The two groupings of the summands of W: as W_j ⊕ (E^j)⁻ ⊕ W^add, and as E^{3m} ⊕ W′, where
E^{3m} is on `D.CarrierIndex` and W′ = W_j ⊕ (E^j)⁻ ⊕ E^{3m−j} ⊕ W♭ is on `D.FirstFactorIndex j`. 

### `posEquiv`

 A bijection, chosen from equality of cardinalities, from 2m indices together with those of V″
to `D.posRank j = k + j − 1` indices together with those of W^add. 

### `constantRows`

 The constant rows: a matrix 𝖼 with 2m rows for each column of μ⁺ at the place τ
(`DetIndex j τ`). Its columns are the r₊ = `D.posRank j` positive indices of W_j and the indices of
W^add. For a column of height h < r₊, row a is the basis vector of W_j at the positive index h + a
if h + a < r₊, and the basis vector number a of E^{3m−j} otherwise. For the l-th column of height
r₊, the rows are the rows `i.rows τ l` of τ(Y), placed in the columns of W♭. 

### `stackedDetProdCoords`

 The polynomial map ζ: the coordinates, in the columns X at the positive indices of W_j
(`firstColsCoord`), of the product P_V of the determinants det(𝖼; X z), with 𝖼 from
`constantRows j i Y` and the rows of variables indexed by V″. Here `firstColsCoord` reads P_V as a
polynomial in X with coefficients in z (`inFirstCols`) and takes its coordinate at a basis index of
weight μ⁺ (`WeylIndexFamily`). So each coordinate is a polynomial in the variables z in the columns
of W^add. 

### `forgetTwist`

 The reduction homomorphism O_E/ϖ²Q → O_E/ϖ², where ϖ is the product of the chosen places and Q
the product of the places in `ϑ.Q`. 

### `addedDatum`

 The datum Ψ^add on matrices `z` modulo ϖ²Q with columns in W^add, for the matrix Λ = `u` modulo
ϖ² (`D.untwistedModulus 2`, ϖ the product of the chosen places). It is `0` unless
the columns on E^{3m−j} and W♭ are those of the identity matrix on `FirstFactorIndex j`. In that
case it is ψ_Λ^inv(z′), the sum over `g` in GL_{3m}(O_E/ϖ²) of ψ_Λ (`New.Rows.traceChar u`,
y ↦ ψ(tr(y Λ)) for a primitive additive character ψ) at z′ g, where z′ consists of the columns on
E^{3m} modulo ϖ². 

### `leftSideSeries`

 The coordinate l of the series Υ at h, for the choice `i`: the kernel of ((E^j)⁻, V″)
at (1, h), whose datum is the indicator of the columns of the identity matrix, times the class sum
over h′ in U(E^{3m}) of 𝖺(h′) χ′(h′) 𝖪[ζ_l]((1, h♭, h′), h). Here 𝖺χ′ is `New.Rows.carrierCoeff` at
the character χ′ = χ^j ϑ (`twistedChiMPow`), a class sum of theta kernels of (E^m, E^{3m}). 𝖪 is the
kernel of (W^add, V″) with both characters ν″ = `firstFactorChar` and the datum Ψ^add =
`New.Data.addedDatum` for the matrix Λ of `i`, and ζ = `New.Data.stackedDetProdCoords` is formed
with the short basis `D.shortRows` at the class h♭ of `i`. The first kernel has characters
`upsilonU1 ^ j` (υ on the norm-one ideles) and ν″, and `blockSumOne` forms the block diagonal point
(1, h♭, h′). 


## The polynomial map ζ

The polynomial P_V, which is `New.Rows.stackedDetProd` for the constant rows at `j`, `i` and `Y`, is
a product of determinants det(𝖼; X z). Each has `2 m` constant rows `𝖼` stacked over rows of
variables, one row for each index in `D.FirstFactorIndex j`.


### `card_detIndex_eq_sum`

 Let μ⁺ be the diagram with `(untwistedDescentPair j).colsPlus τ h` columns of height `h` at the
infinite place `τ`, from the data of the `j`-th theta lift of `D`. The set `DetIndex j τ`, which
indexes the determinants at `τ`, has one element for each column of μ⁺: its cardinality is the sum
of the column counts over the heights below the rank `card (FirstFactorIndex j)` of V″. 

### `card_detIndex_le`

 The number of determinants at the infinite place `τ` is at most `natB + offWeight + Δ + m Δ`:
`D.natB` is the weight b at the b-places as a natural number, `D.offWeight` the weight at the other
places, and Δ = `D.gap` = 2 r⁸ the gap of the data. 

### `card_detIndex`

 The number `card (DetIndex j τ)` of determinants at the infinite place `τ` is the number of
columns of μ⁺. This is the sum of `(untwistedDescentPair j).colsPlus τ h` over heights
`h < card (FirstFactorIndex j)`. It is at most `D.natB + D.offWeight + D.gap + D.m * D.gap`. 

### `prod_sum_norm_sq_le_M_pow`

 Let `Z` have the `2 m + card (FirstFactorIndex j)` rows of a determinant det(𝖼; X z) at `j`, and
as columns the last `D.posRank j - h ≤ j` of the `D.posRank j` positive indices of W_j and the
indices `AddedIndex j` of W^add = E^{3m−j} ⊕ W♭ ⊕ E^{3m}, at most `12 m + 1` columns in all. If its
entries are at most `M ^ 4`, for the integers `m = D.m` and `M = D.M` of the data, the product of
the squared lengths of its columns is at most `(M ^ 9) ^ (12 m + 1)`. 

### `IsSmallSpecialization`

 The entries that a specialisation by `z` and `φ` puts into the determinants have norm at most
`M ^ 4`, where `M = D.M`. 

### `IsSmallSpecialization.norm_entry_le`

 `φ` of every conjugate of an entry of `Y` has norm at most `M ^ 4`. 

### `IsSmallSpecialization.norm_value_le`

 `φ` of every value of `z` has norm at most `M ^ 4`. 

### `hasWeightNormSqLeIf_stackedDet`

 Let `l` be a column of μ⁺ and `h` its height. The factor `stackedDet` for `l` is the determinant
of the constant rows `constantRows j i Y τ l` stacked over rows of variables, with `posEquiv j`
matching rows and columns; `inFirstCols` reads it as a polynomial in the first r₊ columns X with
coefficients in the others, z. Specialised by `z` and `φ`, it is the polynomial of a vector whose
weight is one column of height `h` at `τ`, and the squared norm of this vector is at most
`(M ^ 9) ^ (12 m + 1)` if the values of `φ` at the conjugates of the entries of `Y` and at the
values of `z` are at most `M ^ 4`. 

### `hasWeightNormSqLeIf_stackedDetProd`

 At the `j`-th lift, take the product of the determinants of the constant rows
`constantRows j i Y` stacked over variables with rows `FirstFactorIndex j`, as a polynomial in the
first `D.posRank j` columns. Specialise the columns on `AddedIndex j` by `z` and apply `φ`. The
result is the polynomial of a vector of weight μ⁺, the diagram with
`(untwistedDescentPair j).colsPlus τ h` columns of height `h` at `τ`, whose squared norm is at most
`(M ^ 9) ^ ((12 m + 1) N)` if the specialised entries of `Y` and `z` are at most `M ^ 4`. Here `i`
chooses the rows of `Y`, `M = D.M`, and `N` is the total number of determinants over all places. 

### `comp_eval_stackedDetProdCoords_eq_of_toPoly_eq`

 Take the product of the determinants of the constant rows `constantRows j i Y`, some of them
rows of the matrix `Y` chosen by `i`, stacked over rows of variables. Its coordinates in the first
`D.posRank j` columns of variables form the vector `stackedDetProdCoords j i Y` of polynomials in
the other columns. Give these other variables the values `z` and apply the ring map `φ`. If the
product becomes the polynomial (`toPoly`) of a vector `ξ`, then the vector of coordinates becomes
`ξ`. 

### `toPoly_comp_eval_stackedDetProdCoords`

 Specialise the coordinates `stackedDetProdCoords j i Y` by values `z` for the remaining
variables and a ring map `φ`. The polynomial of the result is the specialised product of
determinants. 

### `weylNormSq_comp_eval_stackedDetProdCoords_le`

 Specialise the coordinates `stackedDetProdCoords j i Y` by values `z` for the remaining
variables and a ring map `φ`. Suppose `φ` of every image `Φ τ (Y a b)` of an entry of `Y` and of
every value `z x` has norm at most `M ^ 4`. Then the squared norm `weylNormSq` of the result is at
most `(M ^ 9) ^ ((12 m + 1) · ∑ τ, card (DetIndex j τ))`. 

### `weylNormSq_stackedDetProdCoords_le`

 Specialise the coordinates `stackedDetProdCoords j i Y` by values `z` for the remaining
variables and a ring map `φ`. Then `toPoly` of the result is the specialised product of
determinants. Assume `IsSmallSpecialization j Y φ z`: the images under `φ` of the conjugates of the
entries of `Y`, and of the values of `z`, are at most `M ^ 4` in size. Then `weylNormSq` of the
result is at most `(M ^ 9) ^ ((12 D.m + 1) N)`, where `N` is the sum over `τ` of
`card (DetIndex j τ)`, the total number of determinants. 

### `toPoly_stackedDetProdCoords`

 Take the product of the determinants of the constant rows `constantRows j i Y`, some of them
rows of the matrix `Y` chosen by `i`, stacked over rows of variables (`stackedDetProd`). Read it as
a polynomial in the first `D.posRank j` columns of variables, with coefficients polynomials in the
other columns (`inFirstCols`). It is the polynomial (`toPoly`) of its vector of coordinates
`stackedDetProdCoords j i Y`, of weight `(untwistedDescentPair j).colsPlus`. 

### `aeval_smul_X_stackedDetProdCoords`

 Replacing the variables `x` by `c • x` multiplies each coordinate `stackedDetProdCoords j i Y l`
at the `j`-th lift by `c ^ d` for the degree `d = ∑ τ, ∑ h, (N - h) κ(τ, h)`, where `N` is the
number of rows of variables, indexed by `FirstFactorIndex j`, and `κ` the weight
`(untwistedDescentPair j).colsPlus`. 

### `inFirstCols_stackedDetProd_mem_range`

 Take the product of the determinants of the constant rows `constantRows j i Y` stacked over
variables, with `posEquiv j` matching rows and columns. Read as a polynomial in the first
`D.posRank j` columns over the polynomials in the others (`inFirstCols`), it has coefficients in
every subring `A` of `ℂ` that contains all the conjugates `Φ τ (Y a b)`. 

### `IsHomogeneousOverEntries`

 The polynomial `Q` in the variables of the columns of W^add is homogeneous of degree `d`, and
its coefficients lie in the ring generated by the conjugates of the entries of `Y`. 

### `IsHomogeneousOverEntries.aeval_smul_X`

 `Q` is multiplied by `c ^ d` when the variables are multiplied by `c ≠ 0`. 

### `IsHomogeneousOverEntries.mem_range`

 `Q` has its coefficients in every subring of `ℂ` that contains all the `Φ τ (Y a b)`. 

### `exists_isHomogeneousOverEntries_smul_stackedDetProdCoords`

 There are a degree `d`, at most `10 m + 1` times the number of determinants over the infinite
places `D.Φ` of the CM field `D.E`, and an integer `0 < H ≤ (d ^ d) ^ 3`, both independent of `i`
and `Y`, such that every `H • stackedDetProdCoords j i Y l` is homogeneous of degree `d` and has its
coefficients in every subring of `ℂ` that contains all the conjugates `Φ τ (Y a b)`. 
