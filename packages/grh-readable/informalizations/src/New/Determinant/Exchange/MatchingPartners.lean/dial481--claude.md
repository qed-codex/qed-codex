---
{
  "module": "src/New/Determinant/Exchange/MatchingPartners.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Determinant/Exchange/MatchingPartners.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Determinant/Exchange/MatchingPartners.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Matched functions, sections over GL cosets and same-section pairs of matrix functions

This file studies functions on matrices over a finite product F of non-archimedean local fields with
integers O (`New.SemilocalField`). For k in GL_n(F) and n = b ⊔ a, write y_k = `New.firstCols e k`
for the block of columns b of k and x_k = `New.invLastRows e k` for the block of rows a of k⁻¹. A
matrix is primitive (`New.IsPrimitiveMatrix O`) if it is integral with an integral left inverse.

## Main definitions and results

* `New.Rows.areMatched_block`: the block determinant functions `New.Rows.blockRowDatum` and
  `New.Rows.blockColDatum` are matched functions.
* `New.localSection χ y`: a linear functional that is the sum of χ(det g) Ψ(y g) over
  representatives g of GL_b(F)/GL_b(O) (`New.IsCommonCosetRep`,
  `New.exists_linearMap_eq_sum_and_isCommonCosetRep`) when that sum is finite;
  `New.exists_isPrimitiveMatrix_localSection_eq` computes it for Ψ with primitive support.
* `New.sameSectionPairs`: the pairs (Φ, Ψ) of Schwartz–Bruhat functions, Φ(x) zero unless xᵀ has a
  left inverse and Ψ(y) zero unless y has one, such that the section of y ↦ Φ(yᵀ) at x_kᵀ is χ(det
  k) times that of Ψ at y_k; GL_n(F) acts on them (`New.sameSectionPairs.translate_mem`).
* `New.sameSectionPairs.exists_linear_factor`: a linear map of Φ that is invariant under Φ ↦ χ(det
  g) Φ(g ·) depends, on same-section pairs, only on Ψ.
* `New.AreMatched.mem_sameSectionPairs`: for tame `χ` (`New.TameLocalChar`) and locally constant
  `Ψ`, matched functions over O form a same-section pair (`New.sameSectionPairs`).

Notions from other files:
* `New.AreMatched`: Φ vanishes off the matrices x_k = `New.invLastRows` (last rows of k⁻¹), Ψ off
  the y_k = `New.firstCols` (first columns of k), k in GL_n(O), and Φ(x_k) = χ(det k) Ψ(y_k).
* `New.TameLocalChar`: A finite ring R, a surjection π: O → R with kernel ϖO, and a primitive
  character η (`New.Exchange.IsPrimitiveMulChar`) with η∘π equal to χ⁻¹ on units, 0 on non-units.
* `New.SemilocalField`: Conditions met by a finite product of non-archimedean local fields: a
  locally compact ring with Haar measure, compact open subring O of volume one, a topologically
  nilpotent ϖ in O that is invertible in F, and `New.IsValuationPair O`.

## Relation to the literature

See `New.Determinant.Exchange.ExplicitMatching` and `New.Determinant.Exchange.TheoremForPartners`
for related work. See `Lib.Adelic.Hecke.ClassSums` for sources.



## Matched functions from block determinant functions

On the open cell of matrices with invertible square block, Jacobi's identity for complementary
minors makes the block determinant functions matched functions.


### `New.Rows.blockRowDatum`

 Cut the `a × n` matrix `x = (x₁ x₂)` by columns along `e`, with `x₂` square. The value of this
function at `x` is `χ⁻¹(det x₂) f(x₂⁻¹ x₁)`; it is zero unless `x₂` is invertible. 

### `New.Rows.blockColDatum`

 Cut the `n × b` matrix `y = (y₁; y₂)` by rows along `e`, with `y₁` square. The value of this
function at `y` is `χ⁻¹(det y₁) f(-(y₂ y₁⁻¹))`; it is zero unless `y₁` is invertible. 

### `New.Rows.areMatched_block`

 The block determinant functions `Φ (x₁ x₂) = χ⁻¹(det x₂) f(x₂⁻¹ x₁)` (`blockRowDatum`) and
`Ψ (y₁; y₂) = χ⁻¹(det y₁) f(-(y₂ y₁⁻¹))` (`blockColDatum`) are matched functions for `χ` over the
whole ring `R` (`AreMatched ⊤`): `Φ` vanishes off the matrices `x_k` formed by the rows `a` of
`k⁻¹`, `Ψ` off the matrices `y_k` formed by the columns `b` of `k`, for `k` in `GL_n(R)`, and
`Φ(x_k) = χ(det k) Ψ(y_k)`. 

 ## Sections over GL cosets and the space of same-section pairs 

### `exists_linearMap_eq_sum`

 On the complex functions on a type `ι` there is a linear functional equal to `f ↦ ∑ i, f i` on
the functions with finitely many nonzero values. 

### `IsCommonCosetRep`

 Let `O` be the ring of integers of the semilocal field `F` (`SemilocalField.O`), and `intGL b O`
the subgroup `GL_b(O)` of `GL_b(F)`. The matrices `r q` represent the cosets `q` in
`GL_b(F)/GL_b(O)`, and each `n × b` matrix `y` with a left inverse has `y * r q` primitive (entries
in `O`, with a left inverse over `O`) for exactly one `q`, and likewise `y * (r q)⁻¹`. 

### `IsCommonCosetRep.coe_eq`

 `r q` lies in the coset `q`. 

### `IsCommonCosetRep.existsUnique_mul`

 If `y` has a left inverse, exactly one representative makes `y * r q` primitive. 

### `IsCommonCosetRep.existsUnique_mul_inv`

 If `y` has a left inverse, exactly one representative makes `y * (r q)⁻¹` primitive. 

### `exists_isCommonCosetRep`

 For a semilocal field `F` with ring of integers `O` there are representatives `r q` of the
cosets `q` in `GL_b(F)/GL_b(O)` such that, for every `n × b` matrix `y` with a left inverse, exactly
one `q` makes `y * r q` primitive and exactly one makes `y * (r q)⁻¹` primitive
(`IsCommonCosetRep n r`). 

### `exists_linearMap_eq_sum_and_isCommonCosetRep`

 There are representatives `r q` of the cosets `q` in `GL_b(F)/GL_b(O)` and a linear functional
`ℓ` on the complex functions on `GL_b(F)` such that `ℓ f = ∑ q, f (r q)` when only finitely many of
the values `f (r q)` are nonzero, and, for every `n × b` matrix `y` with a left inverse, exactly one
`q` makes `y * r q` primitive and exactly one makes `y * (r q)⁻¹` primitive. 

### `commonCosetSum`

 A linear functional on all functions on `GL b F`, chosen from
`exists_linearMap_eq_sum_and_isCommonCosetRep`. It extends the finite sum of the values at the
representatives `commonCosetRep` (`commonCosetSum_eq_sum`). 

### `commonCosetRep`

 The representatives of the cosets of `GL b O` in `GL b F` that are chosen from
`exists_linearMap_eq_sum_and_isCommonCosetRep` together with `commonCosetSum`
(`isCommonCosetRep_commonCosetRep`). 

### `commonCosetSum_eq_sum`

 `commonCosetSum f` is the sum of the values of `f` at the representatives, when the nonzero
values are indexed by a finite set `t` of cosets. 

### `isCommonCosetRep_commonCosetRep`

 The chosen matrices `commonCosetRep` represent the cosets of `GL_b(O)` in `GL_b(F)`. For each
`n × b` matrix `y` with a left inverse, exactly one of them, `r`, makes `y * r` primitive, and
exactly one makes `y * r⁻¹` primitive (`IsCommonCosetRep`). 

### `existsUnique_isPrimitiveMatrix_mul_commonCosetRep`

 For `y` with a left inverse, exactly one of the chosen coset representatives `r` makes `y * r`
primitive (integral with an integral left inverse). 

### `existsUnique_isPrimitiveMatrix_mul_inv_commonCosetRep`

 For `y` with a left inverse (`HasLeftInv y`), exactly one coset `q` of `GL b O` in `GL b F`
makes `y * (commonCosetRep F b n q)⁻¹` primitive (entries in `O`, with a left inverse that has
entries in `O`). 

### `localSection`

 For a character `χ` of `F` and an `n × b` matrix `y`, the section at `y` is the functional
sending `Ψ` to `commonCosetSum` of `g ↦ χ (det g) * Ψ (y * g)` on `GL b F`, that is, to the sum of
this function over representatives of `GL_b(F)/GL_b(O)` when the sum is finite
(`localSection_eq_sum`). 

### `localSection_eq_sum`

 The section of `Ψ` at `y` is the sum of `χ (det r) * Ψ (y * r)` over the chosen matrices `r`
indexed by `GL_b(F)/GL_b(O)` (`commonCosetRep`), when the indices with `Ψ (y * r) ≠ 0` lie in a
finite set `t`. 

### `sameSectionPairs`

 Same-section pairs (compare matched functions, `AreMatched`): pairs `(Φ, Ψ)` of
Schwartz–Bruhat functions, on the matrices `x` such that `xᵀ` has a left inverse and on the matrices
with a left inverse, such that for every `k` the section of `y ↦ Φ yᵀ` at `(invLastRows e k)ᵀ` is
`χ (det k)` times the section of `Ψ` at `firstCols e k` (`mem_sameSectionPairs_iff`). 

### `mem_sameSectionPairs_iff`

 `(Φ, Ψ)` is a same-section pair if and only if both functions are locally constant with compact
support, `Φ` in the `x` such that `xᵀ` has a left inverse and `Ψ` in the `y` with a left inverse,
and for each `k` the coset sum `localSection` of `y ↦ Φ yᵀ` at the transposed last rows of `k⁻¹` is
`χ (det k)` times that of `Ψ` at the first columns of `k`. 

### `mul_firstCols`

 Multiplying the columns `b` of `k` on the left by `g` gives the columns `b` of `g * k`. 

### `sameSectionPairs.translate_mem`

 Translation by `g` in `GL n F` preserves the same-section pairs of a character `χ` of `F` and a
splitting `e` of the indices: if `(Φ, Ψ)` is one, then so is
`(x ↦ χ (det g) * Φ (x * g), y ↦ Ψ (g⁻¹ * y))`. 

### `exists_isPrimitiveMatrix_localSection_eq`

 Let `y` have a left inverse. There is `g` in `GL b F` such that `y * g` is primitive and, for
every `Ψ` that vanishes off the primitive matrices, the section of `Ψ` at `y` is the one term
`χ (det g) * Ψ (y * g)`. 

### `isIntegralUnit_one_sub_uniformizer_mul`

 In a semilocal field with ring of integers `O` and uniformiser `ϖ`, the element `1 - ϖ t` is a
unit of `O` for every `t` in `O`. 

### `isOpen_setOf_isIntegralUnit`

 The units of the ring of integers `O` of a semilocal field `F` form an open subset of `F`. 

### `isClopen_setOf_isPrimitiveMatrix`

 The primitive `n × a` matrices over a semilocal field (entries in the ring of integers `O`, with
a left inverse over `O`) form a closed and open set. 

### `exists_eq_invLastRows_iff_isPrimitiveMatrix`

 A matrix `x` consists of the rows `a` of `k⁻¹` (`invLastRows`) for some `k` in `GL n O` exactly
when `xᵀ` is primitive (integral, with an integral left inverse). 

### `exists_finset_isPrimitiveMatrix_mul_inv_commonCosetRep`

 Let `Φ` be locally constant with compact support in the `x` such that `xᵀ` has a left inverse.
There is a finite set `t` of cosets `q` in `GL_a(F)/GL_a(O)` such that each `x` in the support has
`xᵀ * r⁻¹` primitive for the chosen representative `r = commonCosetRep F a n q` of some `q` in
`t`. 

### `sameSectionPairs.exists_linear_factor`

 Let `χ` be a character of `F`, and let `Λ` be a linear map on functions of `a × n` matrices with
`χ (det g) • Λ (x ↦ Φ (g * x)) = Λ Φ` for all `g` in `GL a F` and all locally constant `Φ` with
compact support in the `x` such that `xᵀ` has a left inverse. Then on same-section pairs `(Φ, Ψ)`
the value `Λ Φ` is a linear function `T` of `Ψ`. 

 ## Matched functions as same-section pairs 

### `apply_invLastRows_eq_of_isPrimitiveMatrix`

 Let `Φ` and `Ψ` be matched for `χ` over the subring `O` (`AreMatched`): they vanish off the
matrices `invLastRows e k` and `firstCols e k` respectively, and `Φ (invLastRows e k) = χ (det k) *
Ψ (firstCols e k)` for `k` in `intGL n O`. Let `i` be in `intGL n O` and `j` in `GL n R`. Suppose
`invLastRows e j = invLastRows e i`. Suppose also that `firstCols e j`, the columns of `j` in the
block `b`, is primitive. Then `Φ (invLastRows e j) = χ (det j) * Ψ (firstCols e j)`. 

### `isPrimitiveMatrix_of_apply_transpose_ne_zero`

 If `Φ` and `Ψ` are matched functions over the ring of integers `O` of `F` (`AreMatched`), then
`y ↦ Φ yᵀ` vanishes off the primitive matrices (integral, with an integral left inverse). 

### `isLocallyConstant_comp_transpose`

 Let `F` be a semilocal field with ring of integers `O` (`SemilocalField.O`), and `χ` a tame
character of `F`. Let `e : b ⊕ a ≃ n` mark `b` as the first and `a` as the last indices. Let `Φ` and
`Ψ` be matched functions over `O` (`AreMatched`): they vanish off the rows `a` of `k⁻¹`
(`invLastRows e k`) and off the columns `b` of `k` (`firstCols e k`), for `k` in `GL n O`, and `Φ
(invLastRows e k) = χ (det k) * Ψ (firstCols e k)`. If `Ψ` is locally constant, so is `y ↦ Φ yᵀ`. 

### `mem_sameSectionPairs`

 Let `F` be a semilocal field with ring of integers `O` (`SemilocalField.O`) and `χ` a tame
character of `F`. Let `Φ`, on `a × n` matrices, and a locally constant `Ψ`, on `n × b` matrices, be
matched functions over `O`. Then `(Φ, Ψ)` is a same-section pair (`sameSectionPairs`): both
functions are Schwartz–Bruhat, and for every `k` in `GL n F` the coset sum `localSection` of
`y ↦ Φ yᵀ` at `(invLastRows e k)ᵀ` is `χ (det k)` times that of `Ψ` at `firstCols e k`. 
