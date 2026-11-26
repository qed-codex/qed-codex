---
{
  "module": "src/Lib/General/LinearAlgebra/PartnerAlgebra.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/General/LinearAlgebra/PartnerAlgebra.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/General/LinearAlgebra/PartnerAlgebra.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Rows and columns of integral matrices, primitive matrices and the law of partners

This file develops linear algebra over a subring `O` of a commutative ring `R`, for the local
computations with partner functions. The index set `n` is split by `e : b ⊕ a ≃ n`. For
`k ∈ GL n R`, `New.firstCols e k` is the matrix of the columns `b` of `k`, and
`New.invLastRows e k`, `New.invFirstRows e k` are the matrices of the rows `a` and `b` of `k⁻¹`.

## Main definitions and results

* `New.AreMatched`: two functions `Φ`, `Ψ` supported on the blocks `New.invLastRows e k` and
  `New.firstCols e k` of `k ∈ GL n O`, whose values differ by the factor `χ (det k)`.
* `New.IsPrimitiveMatrix.mul_iff`: for primitive `y`, the matrix `y * x` is primitive exactly if `x`
  is primitive.
* `New.exists_firstCols_eq_mul`: multiplying `firstCols e k` by an element of `GL b O` and
  `invLastRows e k` by an element of `GL a O` gives the blocks of another element of `GL n O`,
  whose determinant is computed.
* `New.IsValuationPair.exists_firstCols_iff`: if `New.IsValuationPair O` holds, the primitive
  matrices are the `firstCols e k` with `k` in `GL n O`.
* `New.AreMatched.lift_of_reduction`: partners over `R` lift along a surjective local homomorphism
  `O → R`; here `O` is a subring of another ring `F`.
* `New.AreMatched.left_mul`, `New.AreMatched.right_mul`: the transformation laws of two partner
  functions.

Notions from other files:
* `New.intGL n O`: the group `GL n O` as a subgroup of `GL n R`.
* `New.IsPrimitiveMatrix O y`: the matrix `y` and some left inverse of it have entries in `O`.
* `New.HasLeftInv X`: the matrix `X` has a left inverse over `R`.
* `New.liftIntegralFn π f`: the function that is `f` at the image under `π` of a matrix over `O`
  and zero at every other matrix.
* `New.IsValuationPair O`: for all `u`, `v` in `R` there is an idempotent `ε` in `O` such that `u`
  and `v` are `O`-multiples of `(1 - ε) u + ε v`.

## Relation to the literature

Known; see `Lib.SiegelWeil.Tower.LargeSideConstantTerm` for sources.


 ## Invertibility detected after a local ring homomorphism 

### `New.isUnit_of_mapMatrix`

 A square matrix is invertible if its image under a local ring homomorphism is invertible. 

 ### Blocks of an invertible matrix and partners 

### `invLastRows`

 For `k` invertible and the indices split by `e : b ⊕ a ≃ n`, the rows of `k⁻¹` indexed by the
block `a`. 

### `firstCols`

 For `k` invertible and the indices split by `e : b ⊕ a ≃ n`, the columns of `k` indexed by the
block `b`. 

### `AreMatched`

 The functions `Φ` on `a × n` matrices and `Ψ` on `n × b` matrices are partners for the
multiplicative character `χ` over `O` if `Φ` vanishes off the matrices `invLastRows e k` and `Ψ` off
the matrices `firstCols e k`, for `k` in `GL_n(O)`, and
`Φ (invLastRows e k) = χ (det k) * Ψ (firstCols e k)` for all such `k`. 

### `AreMatched.supp_left`

 `Φ` vanishes off the matrices `invLastRows e k`, the rows `a` of `k⁻¹`, for `k` in
  `GL_n(O)`. 

### `AreMatched.supp_right`

 `Ψ` vanishes off the matrices `firstCols e k`, the columns `b` of `k`, for `k` in
  `GL_n(O)`. 

### `AreMatched.apply_eq`

 For `k` in `GL_n(O)` the values of `Φ` and `Ψ` differ by the factor `χ (det k)`. 

 ### Left inverses and primitive matrices 

### `invFirstRows`

 For `k ∈ GL n R` and the indices split as `b ⊕ a`, the rows of `k⁻¹` indexed by `b`. 

### `invFirstRows_mul_firstCols`

 The rows `b` of `k⁻¹` form a left inverse of the columns `b` of `k`. 

### `invLastRows_invTransposeGL`

 The rows `a` of the inverse of `invTransposeGL k = (kᵀ)⁻¹` are the transposed columns `a` of
`k`. 

### `transpose_invLastRows`

 The transposed rows `a` of `k⁻¹` are the columns `a` of `invTransposeGL k = (kᵀ)⁻¹`. 

### `IsPrimitiveMatrix.mul_iff`

 Let `y` be primitive over `O`, that is, integral with an integral left inverse. Then `y * x` is
primitive if and only if `x` is. 

### `isPrimitiveMatrix_iff_mem_intGL`

 An invertible matrix is primitive over `O` if and only if it lies in `GL n O`. 

### `isPrimitiveMatrix_firstCols`

 A block of columns of a matrix in `GL n O` is primitive over `O`. 

 ### Columns of a matrix and rows of its inverse 

### `exists_invLastRows_iff_transpose`

 A matrix consists of the rows `a` of `k⁻¹` for some `k ∈ GL n O` exactly if its transpose
consists of the columns `a` of some `k ∈ GL n O`. 

### `invLastRows_mul_firstCols`

 The rows `a` of `k⁻¹` kill the columns `b` of `k`. 

### `det_fromRows_invLastRows`

 Complete the rows `invLastRows e k` by rows `s` to a square matrix. Its determinant times
`det k` is the determinant of `s * firstCols e k`. 

### `firstCols_mul_invFirstRows_mul`

 A matrix `y` that is killed by `invLastRows e k` is a combination of the columns
`firstCols e k`, with coefficients `invFirstRows e k * y`. 

### `exists_firstCols_eq_mul`

 For `g ∈ GL b O`, `f ∈ GL a O` and `k ∈ GL n O`, the matrices `firstCols e k * g` and
`f * invLastRows e k` come from one `j ∈ GL n O`, with `det j * det f = det k * det g`. 

### `exists_mul_eq_invLastRows_iff`

 The set of the matrices `invLastRows e k` (rows `a` of `k⁻¹`) with `k ∈ GL n O` is stable under
left multiplication by `GL a O`. 

### `exists_mul_eq_firstCols_iff`

 The set of the matrices `firstCols e k` (columns `b` of `k`) with `k ∈ GL n O` is stable under
right multiplication by `GL b O`. 

### `_root_.New.IsValuationPair.exists_firstCols_iff`

 If the subring `O` of `R` satisfies `New.IsValuationPair` (any two elements `u`, `v` of `R` are
`O`-multiples of `(1 - ε) u + ε v` for an idempotent `ε` of `O`), then an `n × b` matrix `y` is the
block of the columns `b` of an element of `GL n O` exactly when `y` has entries in `O` and a left
inverse over `O`. 

 ### Lifting along a local homomorphism 

### `liftIntegralFn_map_coe`

 At a matrix `M` over the subring `O`, the lift `liftIntegralFn π f` takes the value of `f` at
the image of `M` under `π`. 

### `exists_map_coe_eq_of_liftIntegralFn_ne_zero`

 If the lift `liftIntegralFn π f` does not vanish at `S`, then `S` comes from a matrix `M` over
the subring `O`, and `f` does not vanish at the image of `M` under `π`. 

### `exists_map_coe_eq_firstCols`

 Let `π : O → R` be a surjective local homomorphism from a subring `O` of `F`. If the image under
`π` of a matrix `y` over `O` is the block `firstCols e k` of columns of some `k ∈ GL n R`, then `y`
is the block `firstCols e j` of columns of some `j ∈ GL n O`. 

 ### The laws of partners 

### `lift_of_reduction`

 Let `π : O → R` be a surjective local homomorphism from a subring `O` of `F`, and let `χ'` agree
with `χ ∘ π` on the units of `O`. If `Φ`, `Ψ` are partners for `χ` over all of `R` (supported on the
rows `a` of `k⁻¹` and the columns `b` of `k` for `k ∈ GL n R`, with values differing by the
factor `χ (det k)`), then their lifts `New.liftIntegralFn` (read through `π` on matrices over `O`,
zero on other matrices) are partners for `χ'` over `O`. 

### `left_mul`

 If `Φ`, `Ψ` are partners for `χ` over `O` (supported on the rows `a` of `k⁻¹` and the columns
`b` of `k` for `k ∈ GL n O`, with values differing by the factor `χ (det k)`), then
`χ (det g) * Φ (g * x) = Φ x` for all `g ∈ GL a O` and all `a × n` matrices `x`. 

### `right_mul`

 If `Φ`, `Ψ` are partners for `χ` over `O` (supported on the rows `a` of `k⁻¹` and the columns
`b` of `k` for `k ∈ GL n O`, with values differing by the factor `χ (det k)`), then
`Ψ (y * g) * χ (det g) = Ψ y` for all `g ∈ GL b O` and all `n × b` matrices `y`. 
