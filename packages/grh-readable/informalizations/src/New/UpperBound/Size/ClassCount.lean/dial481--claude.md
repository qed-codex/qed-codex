---
{
  "module": "src/New/UpperBound/Size/ClassCount.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Size/ClassCount.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Size/ClassCount.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Explicit bound for the number of classes in the genus

This file gives a crude explicit bound `New.Space.card_stdClasses_le` for the number of classes
`New.StdClasses (New.stdLevel E n)` in the genus of the standard lattice. A class is determined
by the Gram matrix `G` of a short basis of its lattice and a rational approximation `X` of the
change of basis. Both `G` and `G X` have integral entries of bounded size, and such matrices are
counted.

## Main definitions and results

* `New.Space.card_stdClasses_le`: an explicit bound for the number of classes
  `New.StdClasses (New.stdLevel E n)`, for a CM field `E` with `f` infinite places and a natural
  number `N ≠ 0` in the different of `E`.
* `New.Space.stdClasses_eq_of_gram_eq`: two classes `g`, `g'` in `Γ \ G_f / K₀` are equal if
  there are `Y`, `Y'` in `GL n E` with the same Gram matrix such that `A' A⁻¹` has entries in
  `Ô E`, where `A = g.out⁻¹ Y` and `A' = g'.out⁻¹ Y'`.

Notions from other files:
* `New.StdClasses K`: the double cosets `Γ \ G_f / K` of the finite adelic unitary group `G_f` of
  the form `∑ x_i \bar x_i` by its rational points `Γ` and a subgroup `K`.
* `New.stdLevel`: the subgroup `K₀ = G_f ∩ GL_n(Ô)`, the stabiliser of the standard lattice `Ô^n`.

## Relation to the literature

See `New.UpperBound.Size.Estimates` for related work.


### `New.Space.norm_map_mul_apply_le`

 If the entries of `M` and `M'` have absolute values at most `a` and `b` under a complex
embedding `φ`, then those of `M M'` have absolute value at most `#n · a b`. 

### `New.Space.norm_gram_apply_le_cube`

 Let `c = shortBasisConst E n N = 6 N (f #n)²`, with `f` the number of infinite places of `E`.
If at the infinite place `w` (with embedding `Φ w`) the entries of `Y` have size at most `c` and
those of `X` at most `(2 f)² N`, then the entries of `Yᴴ Y` and `Yᴴ Y X` have size at most `c³`. 

### `New.Space.isIntegral_conjTranspose_mul_apply`

 Let `g` be a finite adelic unitary matrix and `Y`, `Z` matrices over `E` such that `g Y` and
`g Z` have entries in the integral finite adeles `Ô E`. Then the entries of `Yᴴ Z` are algebraic
integers. 

### `New.Space.stdClasses_eq_of_gram_eq`

 Let `g`, `g'` be double cosets in `StdClasses K₀ = Γ \ G_f / K₀`, with representatives `g.out`,
`g'.out`, and let `Y`, `Y'` in `GL n E` have the same Gram matrix. Put `A = g.out⁻¹ Y` and
`A' = g'.out⁻¹ Y'`. If `A' A⁻¹` has entries in `Ô`, then `g' = g`. 

### `New.Space.card_stdClasses_le`

 Let `E` be a CM field with `f` infinite places, `N ≠ 0` a natural number in the different of
`E`, and `r = #n`. Then the set `StdClasses K₀` of double cosets `Γ \ G_f / K₀` has at most
`(1 + 2 c³) ^ (4 f r²)` elements, where `c = shortBasisConst E n N = 6 N (f r)²`. 
