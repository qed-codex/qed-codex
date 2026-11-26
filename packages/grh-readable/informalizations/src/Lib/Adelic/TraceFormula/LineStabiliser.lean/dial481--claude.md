---
{
  "module": "src/Lib/Adelic/TraceFormula/LineStabiliser.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Adelic/TraceFormula/LineStabiliser.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Adelic/TraceFormula/LineStabiliser.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The stabiliser of a line at a finite place

Let `w` be a finite place of the number field `E`, with local field `LocField w` (the `E_w` of
`GL_n(E_w)`), valuation `v`, ring of integers `𝒪`, uniformiser `ϖ` and residue field of `q`
elements. In the formulas, `n` also stands for the cardinality of the index type `n`, and the
exponent `n - 2` is an integer. Let `J_line ⊂ GL_n(𝒪)` be the stabiliser of the line of a basis
vector `e_i` modulo `w`. We write `diag (ϖ, 1, …, 1)` for the diagonal matrix with `ϖ` at the index
`i` and `1` elsewhere. Let `T⁺`, `T⁻` be the operators of the double cosets of this matrix and of
its inverse, and let `e_sph` be the mean over chosen lifts to `GL_n(𝒪)` of the elements of `GL_n` of
the residue field, which on vectors fixed by the kernel of the reduction modulo `w` is the mean over
`GL_n(𝒪)`. On the vectors fixed by `J_line`, `T⁻` is the adjoint of `T⁺` in a unitary representation
(`inner_lineRaise`), and `T⁺ T⁻ = q ^ (n - 2) (1 + (q ^ n - 1) e_sph)` (`lineRaise_lineLower`). The
positive powers of `lineHecke`, the element of the group algebra that acts as `T⁺`, are supported on
integral matrices whose characteristic polynomial has the simple root `0` modulo `w`
(`lineHecke_pow_mem_spanOn`).

Notions from other files:
* `localIntGL n w` is `GL_n(𝒪)`, and `reduceGL` is its reduction to `GL_n` of the residue field
  `ResField w`.
* `parabolic lev` is the subgroup of invertible matrices that are block upper triangular for the
  level function `lev`.
* `levelSpace ρ J` is the space of vectors fixed by `J` in the representation `ρ`.
* `heckeCoset ρ J t` is the sum of `ρ g` over chosen representatives `g` of the cosets in
  `J t J / J`.

## Relation to the literature

A relation in the Hecke algebra of a parahoric subgroup of `GL_n`, proved by a direct count of
cosets.


 ### Double cosets 

### `doubleCosetSum`

 The sum in the group algebra of the chosen representatives of the cosets in `J t J / J`. It is
zero if there are infinitely many of them. 

### `doubleCosetSum_eq_sum`

 If finitely many cosets of `J` meet `J t J`, the sum of their representatives is a finite
sum. 

### `doubleCosetSum_mem_spanOn`

 If finitely many cosets of `J` meet `J t J`, the sum of their representatives in the group
algebra is supported on `J t J`. 

### `asAlgebraHom_doubleCosetSum`

 If finitely many cosets of `J` meet `J t J`, the sum of their representatives acts in a
representation `ρ` as the operator `heckeCoset ρ J t` of the double coset. 

### `apply_eq_of_inv_mul_mem`

 The translate `ρ g y` of a vector fixed by `J` depends only on the coset `g J`. 

### `mul_mem_doubleCoset_iff_of_mem`

 Membership in `J t J` is unchanged by right multiplication with an element of `J`. 

### `heckeCoset_eq_sum`

 On a vector fixed by `J`, the operator of `J t J` is the sum over any family `r` in `J t J` that
meets each coset `j t J` exactly once. 

### `inner_sum_of_mem_doubleCoset`

 In a unitary representation `ρ` of a group `G`, let `x` and `y` be fixed by the subgroup `J` and
let the `r a` lie in `J t J`. Then each `⟪ρ (r a) x, y⟫` equals `⟪ρ t x, y⟫`, so the sum over
`a ∈ s` is this times `#s`. 

### `lineStabilizer`

 The stabiliser `J_line` in `GL_n(𝒪)` of the line of the basis vector `e_i` modulo `w`. 

### `hyperplaneStabilizer`

 The stabiliser in `GL_n(𝒪)` of the hyperplane spanned by the `e_j`, `j ≠ i`, modulo `w`. 

### `lineElement`

 The matrix `diag (ϖ, 1, …, 1)`, with the uniformiser `ϖ` of `w` at the index `i` and `1`
elsewhere. 

### `isOpen_lineStabilizer`

 The stabiliser of a line modulo `w` is open, as it contains the kernel of the reduction. 

### `isHeckeFunction_indicator_doubleCoset`

 For every `t`, the indicator function of `J t J`, where `J` is the stabiliser of a line modulo
`w`, is invariant under `J` on both sides and lives on finitely many cosets of `J`. 

### `coe_reduceGL`

 For `k` in `GL_n(𝒪)`, the entries of `reduceGL k` are the residues of those of `k`, computed by
`residueOrZero`, which reduces integral elements and is `0` elsewhere. 

### `reduceGL_apply_eq_zero_iff`

 An entry of the reduction of `k ∈ GL_n(𝒪)` vanishes exactly when that of `k` has valuation
less than `1`. 

### `coe_mem_lineStabilizer`

 An element of `GL_n(𝒪)` stabilises the line of `e_i` modulo `w` exactly when its reduction is
block upper triangular for `(· ≠ i)`. 

### `coe_mem_hyperplaneStabilizer`

 An element of `GL_n(𝒪)` stabilises the hyperplane of the `e_j`, `j ≠ i`, modulo `w` exactly
when its reduction is block upper triangular for `(· = i)`. 

### `mem_lineStabilizer`

 The stabiliser of the line of `e_i` modulo `w` consists of the elements of
`localIntGL n w = GL_n(𝒪)` whose column `i` has valuation `v` less than `1` off the diagonal. 

### `mem_hyperplaneStabilizer`

 The stabiliser of the hyperplane of the `e_j`, `j ≠ i`, modulo `w` consists of the elements of
`localIntGL n w = GL_n(𝒪)` whose row `i` has valuation `v` less than `1` off the diagonal. 

### `inv_mul_mem_lineStabilizer`

 The cosets `k J_line` and `l J_line` agree exactly when `l e_i` lies on the line of `k e_i`
modulo `w`. 

### `mul_inv_mem_hyperplaneStabilizer`

 The cosets `J k` and `J l` of the stabiliser `J` of the hyperplane agree exactly when the
`i`-th row of `l` is a multiple of that of `k` modulo `w`. 

### `v_mul_uniformizer_lt_one_iff`

 A product `x ϖ` with the uniformiser lies in the maximal ideal exactly when `x` is integral. 

### `forall_entries`

 A property `p` of index pairs holds everywhere if it holds at `(i, i)`, on the rest of row `i`
and of column `i`, and off both. 

### `conj_lineElement_mem_lineStabilizer_iff`

 Conjugation `g ↦ t⁻¹ g t` by `t = diag (ϖ, 1, …, 1)`, where the uniformiser `ϖ` is at the index
`i`, takes the stabiliser in `GL_n(𝒪)` of the hyperplane spanned by the `e_j`, `j ≠ i`, modulo `w`
onto the stabiliser of the line of `e_i`. 

### `liftMatrix`

 A chosen element of `GL_n(𝒪)` with reduction `M`, for an invertible matrix `M` over the residue
field. 

### `reduceGL_liftMatrix`

 For an invertible matrix `M` over the residue field, the chosen lift `liftMatrix M` reduces to
`M`. 

### `raiseCosetRep`

 The representative of the coset in `J_line diag (ϖ, 1, …, 1) J_line / J_line` that corresponds
to the hyperplane on which the linear form `ξ` with `ξ e_i = 1` vanishes. 

### `lowerCosetRep`

 The representative of the coset in `J_line diag (ϖ, 1, …, 1)⁻¹ J_line / J_line` that corresponds
to the line of a vector `z` with `z i = 1`. 

### `reduceGL_liftMatrix_updateRow`

 For `ξ i = 1`, the chosen lift of the identity with row `i` replaced by `ξ` has this matrix as
its reduction. 

### `reduceGL_liftMatrix_updateCol`

 For `z i = 1`, the chosen lift of the identity with column `i` replaced by `z` has this matrix
as its reduction. 

### `raiseCosetRep_mem_doubleCoset`

 For `ξ i = 1`, `raiseCosetRep i ξ` lies in the double coset of `diag (ϖ, 1, …, 1)` for the
stabiliser of the line of `e_i` modulo `w`. 

### `lowerCosetRep_mem_doubleCoset`

 For `z i = 1`, `lowerCosetRep i z` lies in the double coset of `diag (ϖ, 1, …, 1)⁻¹` for the
stabiliser of the line of `e_i` modulo `w`. 

### `eq_of_eq_smul_of_apply_eq_one`

 If two vectors with `i`-th coordinate `1` are proportional, they are equal. 

### `raiseCosetRep_inv_mul_mem_lineStabilizer_iff`

 For `ξ i = 1` and `k` in `GL_n(𝒪)`, the coset `k⁻¹ diag (ϖ, 1, …, 1) J_line` is that of the
representative `raiseCosetRep i ξ` exactly when `ξ` is a multiple of the `i`-th row of `k` modulo
`w`. Here `J_line` is the stabiliser of the line of `e_i` modulo `w`. 

### `lowerCosetRep_inv_mul_mem_lineStabilizer_iff`

 For `z i = 1` and `k` in `GL_n(𝒪)`, the coset `diag (ϖ, 1, …, 1)⁻¹ k J_line` is that of the
representative `lowerCosetRep i z` exactly when the `i`-th column of `k` modulo `w` is a multiple of
`z`. Here `J_line` is the stabiliser of the line of `e_i` modulo `w`. 

 ### The operators 

### `lineHecke`

 The sum in the group algebra of chosen representatives of the cosets in
`J_line diag (ϖ, 1, …, 1) J_line / J_line`. 

### `lineHeckeLower`

 The sum in the group algebra of chosen representatives of the cosets in
`J_line diag (ϖ, 1, …, 1)⁻¹ J_line / J_line`. It acts as `T⁻`. 

### `sphericalMeanElement`

 The mean in the group algebra of chosen lifts to `GL_n(𝒪)` of all elements of `GL_n` of the
residue field. 

### `lineRaise`

 The operator `T⁺`, the sum over the cosets in `J_line diag (ϖ, 1, …, 1) J_line / J_line`. 

### `lineLower`

 The operator `T⁻`, the sum over the cosets in `J_line diag (ϖ, 1, …, 1)⁻¹ J_line / J_line`. 

### `sphericalMean`

 The operator `e_sph`, the action of the mean of chosen lifts to `GL_n(𝒪)` of the elements of
`GL_n` of the residue field. 

### `lineTranslate`

 The translate `y[z]` of `y` by a chosen element of `GL_n(𝒪)` that takes `e_i` to `z` modulo
`w`. It is used for `z ≠ 0` and `y` fixed by `J_line`; then it depends only on the line of `z`
(`lineTranslate_eq_apply_of_col_eq_smul`). 

### `lineTranslate_eq_apply_of_col_eq_smul`

 For a vector `y` fixed by the stabiliser `J_line` of the line of `e_i` modulo `w` and `z ≠ 0`,
the vector `y[z] = lineTranslate i ρ y z` is the translate of `y` by any `k` in `GL_n(𝒪)` whose
reduction modulo `w` takes `e_i` to a multiple of `z`. 

### `lineTranslate_eq_self`

 For a vector `y` fixed by `J_line` and `z ≠ 0` on the line of `e_i`, the translate
`y[z] = lineTranslate i ρ y z` is `y` itself. 

### `apply_lineTranslate`

 For a vector `y` fixed by the stabiliser `J_line` of the line of `e_i` modulo `w`, a vector
`z ≠ 0` and `k` in `GL_n(𝒪) = localIntGL n w`, the translate of `y[z] = lineTranslate i ρ y z` by
`k` is `y[k z]`, where `k z` is taken modulo `w` by the reduction `reduceGL`. 

### `apply_sum_lineTranslate`

 Let `y` be fixed by `J_line`, let `k` be in `GL_n(𝒪)` and let `S`, `S'` be sets of vectors with
`0 ∉ S` such that `z ∈ S` exactly when `k z ∈ S'` modulo `w`. Then `k` takes the sum of the
translates `y[z] = lineTranslate i ρ y z` over `S` to the sum over `S'`. 

### `apply_liftMatrix_eq`

 On a vector fixed by `J_line`, the chosen lift of `g` to `GL_n(𝒪)` acts as any other lift
`k`. 

### `sphericalMean_apply`

 The operator `e_sph = sphericalMean ρ` is the mean of the actions of the chosen lifts to
`GL_n(𝒪)` of the elements of `GL_n` of the residue field. 

### `sphericalMean_mem`

 The operator `e_sph = sphericalMean ρ` takes a vector fixed by `J_line` to one fixed by
`GL_n(𝒪) = localIntGL n w`. 

### `sphericalMean_apply_translate`

 A vector fixed by `J_line` and its translates by `GL_n(𝒪)` have the same image under
`e_sph = sphericalMean ρ`. 

### `lineRaise_eq_sum`

 Let `y` be fixed by the stabiliser `J_line` of the line of `e_i` modulo `w`. Then
`T⁺ y = lineRaise i ρ y` is the sum of its translates by the coset representatives
`raiseCosetRep i ξ` of `J_line diag (ϖ, 1, …, 1) J_line`, over the forms `ξ` with `ξ e_i = 1`, that
is, over the hyperplanes modulo `w` that do not contain `e_i`. 

### `lineLower_eq_sum`

 Let `y` be fixed by the stabiliser `J_line` of the line of `e_i` modulo `w`. Then
`T⁻ y = lineLower i ρ y` is the sum of its translates by the coset representatives
`lowerCosetRep i z` of `J_line diag (ϖ, 1, …, 1)⁻¹ J_line`, over the vectors `z` with `z i = 1`,
that is, over the lines modulo `w` outside the hyperplane `z i = 0`. 

### `raiseCosetRep_apply_lineLower`

 For `y` fixed by `J_line` and a form `ξ` with `ξ e_i = 1`, the representative
`raiseCosetRep i ξ` of the coset of `T⁺` that corresponds to the hyperplane `ξ = 0` takes
`T⁻ y = lineLower i ρ y` to the sum of the translates `y[z] = lineTranslate i ρ y z` over the
vectors `z` with `ξ z = 1`, that is, over the lines outside the hyperplane `ξ = 0`. 

### `sum_lineTranslate`

 For `y` fixed by `J_line`, the sum of the translates `y[z] = lineTranslate i ρ y z` over all
`z ≠ 0`, in which each line occurs `q - 1` times, is `(q ^ n - 1) e_sph y`. Here `q` is the order
of the residue field, the exponent `n` stands for the number of indices and `e_sph` is
`sphericalMean ρ`. 

### `lineRaise_lineLower`

 Let `ρ` be a complex representation of `GL_n(E_w)` at a finite place `w` of the number field
`E`, and let `y` be a vector fixed by the stabiliser `J_line` in `GL_n(𝒪_w)` of the line of `e_i`
modulo `w`. Then `T⁺ T⁻ y = q ^ (n - 2) (y + (q ^ n - 1) e_sph y)`. Here `T⁺ = lineRaise i ρ` and
`T⁻ = lineLower i ρ` are the sums over the cosets in `J_line diag (ϖ, 1, …, 1) J_line / J_line` and
in `J_line diag (ϖ, 1, …, 1)⁻¹ J_line / J_line`, `e_sph = sphericalMean ρ` is the action of the mean
of chosen lifts to `GL_n(𝒪_w)` of all elements of `GL_n` of the residue field, `q` is the order of
the residue field, and the exponent `n` stands for the number of indices. 

### `inner_lineRaise`

 Let `W` carry a unitary representation of `GL_n` of the local field at `w`. On the vectors fixed
by the stabiliser `J_line` of the line of `e_i` modulo `w`, the operator `T⁻ = lineLower i ρ` of the
double coset of `diag (ϖ, 1, …, 1)⁻¹` is the adjoint of the operator `T⁺ = lineRaise i ρ` of the
double coset of `diag (ϖ, 1, …, 1)`. 

 ### The support of the powers of `lineHecke` 

### `KeepsLineMod`

 The matrix `g` is integral and keeps the line of `e_i` modulo `w`, with an invertible action on
the quotient by that line. 

### `KeepsLineMod.v_le_one`

 The entries are integral. 

### `KeepsLineMod.keepsLine`

 The reduction has the block shape `(∗ ∗; 0 g')` with `g'` invertible. 

### `KeepsLineMod.residue_mul_apply_self`

 If two matrices are integral and keep the line of `e_i` modulo `w`, with invertible actions on
the quotient, then the `(i, i)` entry of their product reduces to the product of the reduced
`(i, i)` entries. 

### `keepsLineMod_of_mem`

 An element of the stabiliser of the line of `e_i` modulo `w` is integral and keeps this line,
with an invertible action on the quotient. 

### `keepsLineMod_lineElement`

 The matrix `diag (ϖ, 1, …, 1)`, with the uniformiser at the index `i`, is integral and keeps the
line of `e_i` modulo `w`, with an invertible action on the quotient. 

### `keepsLineMod_of_mem_doubleCoset`

 An element `g` of the double coset of `diag (ϖ, 1, …, 1)` by the stabiliser of the line of
`e_i` is integral, and modulo `w` it has the shape `(0 ∗; 0 g')` with `g'` invertible. 

### `lineHecke_pow_mem_spanOn`

 For `m > 0`, the `m`-th power of the element `lineHecke w i` of the group algebra, which acts as
`T⁺`, is supported on the matrices `g` such that every element of `g J_line` is integral, with `0` a
simple root of its characteristic polynomial modulo `w`. Here `J_line` is the stabiliser of the line
of `e_i` modulo `w`. 
