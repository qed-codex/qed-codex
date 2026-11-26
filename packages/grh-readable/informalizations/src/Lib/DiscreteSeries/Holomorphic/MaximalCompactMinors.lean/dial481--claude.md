---
{
  "module": "src/Lib/DiscreteSeries/Holomorphic/MaximalCompactMinors.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/DiscreteSeries/Holomorphic/MaximalCompactMinors.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/DiscreteSeries/Holomorphic/MaximalCompactMinors.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Maximal compact subgroup, block diagonal matrices and equivariance of minors

For signs `ε`, let `J = New.signMatrix ε`. `New.USign ε` is the unitary group of `J`,
`New.maxCompactU ε` is its subgroup of unitary matrices, `New.blockDiagAlg ε` is the algebra of
matrices that commute with `J`, and `New.blockDiagPart ε x` is the block diagonal part of `x`.

## Main definitions and results

* `New.mem_blockDiagAlg`, `New.blockDiagPart_eq`: `New.blockDiagAlg ε` consists of the block
  diagonal matrices, and `New.blockDiagPart ε x` is `(x + J * x * J) / 2`.
* `New.mem_maxCompactU`: an element of the group is unitary exactly when it is block diagonal.
* `New.fderiv_eq_on_blockDiagAlg`: a complex derivative at `1` is determined on `New.blockDiagAlg ε`
  by the derivatives along one-parameter subgroups of `New.maxCompactU ε`.
* `New.IsKDominant.weightMinors_mul_borel`, `New.IsKDominant.weightMinors_oppBorel_mul`: let `o` be
  an injective order, `w` dominant within each block of `ε` (`New.IsKDominant`), `x` invertible and
  `b` invertible and block diagonal (`New.blockDiagAlg ε`). Multiplying `x` on the right by an upper
  triangular `b`, or on the left by a lower triangular `b`, multiplies `weightMinors w x` by
  `diagChar w b`.

Notions from other files:
* `New.weightMinors w g`: the coefficient of a highest vector of weight `w`, that is the product
  over all integers `t` of the principal minor of `g` on `{i | t ≤ w i}`, each factor with `t ≤ 0`
  divided by `det g`.

## Relation to the literature

Known; see `Lib.DiscreteSeries.Holomorphic.HighestVectorExtension` for sources.


### `blockDiagPart_eq`

 With `J = signMatrix ε`, the diagonal matrix with entries `ε i`, the block diagonal part of `x`,
that is the matrix of the entries `x i j` with `ε i = ε j`, is `(x + J * x * J) / 2`. 

### `mem_blockDiagAlg`

 A matrix lies in `New.blockDiagAlg ε` exactly when its entry at `(i, j)` vanishes whenever
`ε i ≠ ε j`. 

### `mem_blockDiagAlg_one`

 For the constant signs `1` there is one block, so every matrix is block diagonal. 

### `U.inv_coe_eq_mul_conjTranspose_mul`

 The matrix inverse of an element `g` of `U(diag ε)` is `J * gᴴ * J`, where
`J = signMatrix ε`. 

### `maxCompactU.coe_inv`

 The matrix inverse of an element `k` of `New.maxCompactU ε`, the group of unitary matrices in
`U(diag ε)`, is its conjugate transpose. 

### `conjTranspose_mul_self_eq_one_iff_commute`

 If `J` is an involution and `A` preserves the form of `J`, that is `Aᴴ * J * A = J`, then `A` is
unitary exactly when it commutes with `J`. 

### `mem_maxCompactU`

 An element `g` of `U(diag ε)` lies in the subgroup `New.maxCompactU ε` of unitary matrices
exactly when it is block diagonal, that is, commutes with `signMatrix ε`. 

### `fderiv_eq_on_blockDiagAlg`

 Let `Φ` have the complex derivative `D` at `1`, and let `φ` be a complex linear form. If for
every `Y` in the Lie algebra `unitaryLie (signMatrix ε)` of `U(diag ε)` whose one-parameter group
`expU (t • Y)` lies in `New.maxCompactU ε` the derivative of `t ↦ Φ (exp (t • Y))` at `0` is `φ Y`,
then `D` and `φ` agree on the block diagonal matrices `New.blockDiagAlg ε`. 

### `diagTorusK`

 For a tuple `t` of complex numbers of modulus one, the diagonal matrix `diag(t)` as an element
of the compact group `U(diag ε) ∩ U(n)`. 

### `continuous_diagTorus`

 The map sending a tuple of complex numbers of modulus one to its diagonal matrix in
`U(diag ε)` is continuous. 

### `instance : IsProbabilityMeasure (haarK ε)`

 The Haar measure `New.haarK ε` on `New.maxCompactU ε` has total mass one. 

 ### Products with a block diagonal matrix 

### `blockDiagPart_mul_left`

 Taking the block diagonal part commutes with left multiplication by a block diagonal matrix
`x`. 

### `blockDiagPart_mul_right`

 Taking the block diagonal part commutes with right multiplication by a block diagonal matrix
`x`. 

### `blockDiagPart_mul`

 Taking the block diagonal part commutes with left and with right multiplication by a block
diagonal matrix `x`. 


## Holomorphic functions of a weight and products of minors

`New.IsHolOfWeight ε o u F` says that `F`, a function of a family of elements of `U(diag ε)` indexed
by `Φ`, extends analytically to the products `h * b` with `b` invertible and triangular for the
order `o` (`New.IsBorelMatrix`) and block diagonal for optional signs `ε'` (by default `1`, which
imposes no condition). The extension is `F h` times `∏ τ, New.diagChar (u τ) (b τ)`, where
`New.diagChar w b = ∏ i, b i i ^ w i`.


### `IsHolOfWeight.sum`

 A finite linear combination with complex coefficients of functions holomorphic of weight `u` for
the order `o` is holomorphic of weight `u`. Here `New.IsHolOfWeight ε o u F` says that some `F'` is
analytic at every product `g * b`, with each `b τ` invertible and upper triangular for `o`, block
diagonal for optional signs `ε'` (by default `1`, no condition), and equals
`(∏ τ, diagChar (u τ) (b τ)) * F g` there, where `diagChar w b = ∏ i, b i i ^ w i`. 

### `IsHolOfWeight.mul`

 For an injective order `o`, the product of holomorphic functions of weights `u` and `v` is
holomorphic of weight `u + v`. Here `New.IsHolOfWeight ε o u F` says that some `F'` is analytic at
every product `h * b`, with each `b τ` invertible and upper triangular for `o`, block diagonal for
optional signs `ε'` (by default `1`, no condition), and equals `(∏ τ, diagChar (u τ) (b τ)) * F h`
there, where `diagChar w b = ∏ i, b i i ^ w i`. 

### `IsKDominant.weightMinors_mul_borel`

 Let `o` be injective and `w` dominant within each block of `ε` (`New.IsKDominant ε o w`:
`w j ≤ w i` whenever `ε i = ε j` and `o i < o j`). Here `weightMinors w g` is the product over
integers `t` of the principal minor of `g` on `{i | t ≤ w i}`, divided by `det g` when `t ≤ 0`.
Right multiplication of an invertible `x` by an invertible block diagonal `b`, upper triangular for
`o` (`New.IsBorelMatrix o b`), multiplies `weightMinors w x` by
`diagChar w b = ∏ i, b i i ^ w i`. 

### `IsKDominant.weightMinors_oppBorel_mul`

 Let `o` be injective and `w` dominant within each block of `ε` for `o`, not `-o`
(`New.IsKDominant ε o w`: `w j ≤ w i` whenever `ε i = ε j` and `o i < o j`). Left multiplication of
an invertible `x` by an invertible block diagonal `b`, lower triangular for `o`
(`New.IsBorelMatrix (-o) b`), multiplies the product of principal minors `weightMinors w` by
`diagChar w b = ∏ i, b i i ^ w i`. 
