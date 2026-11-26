---
{
  "module": "src/New/OneLift/HeckeValues/CentralAction.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/OneLift/HeckeValues/CentralAction.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/OneLift/HeckeValues/CentralAction.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Central action on lifts from U(1) and a rank-one denominator bound

For a lift from the definite `U(1)` to the definite `U(n)` (data `New.LValueData`, kernel
`New.LValueData.kernelForm`, lift `New.LValueData.trivialLift` of the trivial character), the finite
adelic `U(1)` acts on forms on `U(n)` through the centre. This file defines this action,
`New.LValueData.centralRep`, and its twist `New.LValueData.normalizedCentralOp`, which fixes the
lift. The central translations commute with Hecke polynomials at split places off the level. The
file uses this action to bound the denominator of the product of the projections of two test forms
to the line of the lift, given a bound `New.Selmer.DenominatorLe` on that line.

## Main definitions and results

* `New.Selmer.DenominatorLe.norm_inner_starProjection_le`: a bound `New.Selmer.DenominatorLe` on the
  line of the lift bounds the denominator of the product of the projections of two test forms to
  that line, at the cost of the class number of `U(1)` at the chosen level.
* `New.LValueData.normalizedCentralOp_trivialLift`: the twisted central translations fix the lift
  of the constant function.

## Relation to the literature

See `New.OneLift.HeckeValues.TwistedValueHeights` for related work.


### `LValueData.centralRep`

 The finite points of `U(1)` act on the forms on `U(n)` for the lift data `Y` through translation
by scalar matrices. 

### `LValueData.normalizedCentralOp`

 Translation by the scalar `z`, multiplied by the value at `det z` of `Y.descentPair.charV`, the
character by which the kernel of the lift twists the action of `U(1)`. 

### `LValueData.coe_centralRep_apply`

 Under `Y.centralRep`, an element `z` of `Gf D.E Unit` acts on the underlying algebraic forms by
right translation (`algFormRep`) by the scalar matrix `scalarFin n` of `det z`. 

### `LValueData.inner_centralRep_centralRep`

 Translation by a scalar preserves the inner product of forms on `U(n)`. 

### `LValueData.inner_normalizedCentralOp`

 For data `Y` of a lift from `U(1)` to `U(n)` and `z` in `U(1)(𝔸_f)`, the adjoint of the
normalized translation `T z = Y.normalizedCentralOp z` is `T z⁻¹`: `⟪x, T z y⟫ = ⟪T z⁻¹ x, y⟫`. 

### `LValueData.normalizedCentralOp_kernelForm`

 For lift data `Y` and `z`, `g` in `Gf D.E Unit` (the finite adelic `U(1)`), the normalized
translation `normalizedCentralOp` at `z⁻¹` carries the theta kernel at `g`, as a form on `U(n)`
(`kernelForm`), to the kernel at `g * z`. 

### `LValueData.normalizedCentralOp_trivialLift`

 The normalized central translations fix the lift of the constant function. 

### `LValueData.commute_algFormRep_scalarFin`

 On algebraic forms of the weight of `Y`, translation by a scalar matrix commutes with every
translation. 

### `LValueData.algFormRep_scalarFin_apply_comm`

 On an algebraic form `φ` of the weight of `Y`, translation (`algFormRep`) by the scalar matrix
`scalarFin n ν` commutes with translation by `g`: applying the two in either order gives the same
form. 

### `LValueData.centralRep_mem_range_groupAlgAction`

 Central translations preserve the image of an element `e` of the group algebra of the residue
units at the chosen places. 

### `LValueData.centralRep_heckePolyOnForms`

 Let `Y` be data for a theta lift from `U(1)` to the definite `U(n)` over the CM field `D.E`,
with space of algebraic forms `Y.descentPair.FormV` on `U(n)`. Translation `Y.centralRep z` by a
scalar `z ∈ U(1)(𝔸_f)` commutes with the operator
`heckePolyOnForms = ∑ i, (-X) ^ i q ^ (i (i - 1) / 2) T_{w,i}`, for any number `X` and any split
place `w` of norm `q` such that `w` and its conjugate are off the level. 

### `LValueData.normalizedCentralOp_inv_mem_integralForms`

 Let `Y` be data for a theta lift from `U(1)` to the definite `U(n)` over the CM field `D.E`,
with space of algebraic forms `Y.descentPair.FormV` on `U(n)`, and `T z = Y.normalizedCentralOp z`
the translation by the scalar `z ∈ U(1)(𝔸_f) = Gf D.E Unit` times the value of the character
`Y.descentPair.charV` at `z`. Let `j : ℂ → ℂ_ℓ` be an embedding for a prime `ℓ`. If `z` is integral
at the places above `ℓ`, then `T z⁻¹` preserves the forms whose values are all integral at `j`
(`integralForms j`). 

### `LValueData.sum_normalizedCentralOp_mem_ker_normalizedDescent`

 Let `Y` be data for a theta lift from `U(1)` to the definite `U(n)` over the CM field `D.E`,
with space of algebraic forms `Y.descentPair.FormV` on `U(n)`, lift `Y.trivialLift`, and
`T z = Y.normalizedCentralOp z` the translation by the scalar `z ∈ U(1)(𝔸_f) = Gf D.E Unit` times
the value of the character `Y.descentPair.charV` at `z`. Let all stabilisers `classAut` of `U(1)` at
the chosen level be trivial, and let `s c` represent the class `c` modulo the rational points `Γf`
and that level. If `y` is orthogonal to `Y.trivialLift`, then the descent
`Y.descentPair.normalizedDescent` from `U(n)` to `U(1)`, the adjoint of the lift, kills
`∑ c, T (s c) y`. 

### `LValueData.isOrthogonalToFalseLifts_sum_normalizedCentralOp_inv`

 Let `Y` be data for a theta lift from `U(1)` to the definite `U(n)` over the CM field `D.E`,
with space of algebraic forms `Y.descentPair.FormV` on `U(n)`, lift `Y.trivialLift`, and
`T z = Y.normalizedCentralOp z` the translation by the scalar `z ∈ U(1)(𝔸_f) = Gf D.E Unit` times
the value of the character `Y.descentPair.charV` at `z`. Let all stabilisers of `U(1)` at the chosen
level be trivial and let `s c` represent the class `c`. Let `e` be an element of the group algebra
of the residue units at the chosen places. For a subspace `Z` the false lifts at a split place `w`
off the level are the forms in `Z` and in the image of `e` that the Hecke polynomial
`heckePolyOnForms` of `w`, evaluated at `liftHeckeRoot w`, kills. Let `Ξ` be orthogonal to them at
all such `w` for `Z` the kernel of the descent `normalizedDescent` to `U(1)`. Then
`∑ c, T (s c)⁻¹ Ξ` is orthogonal to them for `Z` the orthogonal complement of the line
`ℂ ∙ Y.trivialLift`. 

### `Selmer.DenominatorLe.norm_card_mul_inner_starProjection_le`

 Let `Y` be data for a theta lift from `U(1)` to the definite `U(n)` over the CM field `D.E`,
with space of algebraic forms `Y.descentPair.FormV` on `U(n)` and lift `φ = Y.trivialLift`, let `ℓ`
be a prime and `ι : ℂ ≃ ℚ̄_ℓ`. Let the projection to the line `ℂ φ` have denominator at most `exp β`
at `ι` (`DenominatorLe`): an operator on the line, of determinant at least `exp (-β)` in norm, makes
integral the projection of every integral form that is orthogonal to the false lifts. Let all
stabilisers of `U(1)` at the chosen level be trivial. Let `Ξ`, `Ξ'` be integral above `ℓ` and
orthogonal to the false lifts in the kernel of the descent (`IsTestForm`). Then the class number of
`U(1)` at that level times the inner product of `Ξ` with the projection of `Ξ'` to the line has norm
at most `exp β` under `ι`. 

### `Selmer.DenominatorLe.norm_inner_starProjection_le`

 Let `Y` be data for a theta lift from `U(1)` to the definite `U(n)` over the CM field `D.E`,
with space of algebraic forms `Y.descentPair.FormV` on `U(n)` and lift `φ = Y.trivialLift`, let `ℓ`
be a prime and `ι : ℂ ≃ ℚ̄_ℓ`. Let the projection to the line `ℂ φ` have denominator at most `exp β`
at `ι` (`DenominatorLe`): an operator on the line, of determinant at least `exp (-β)` in norm, makes
integral the projection of every integral form that is orthogonal to the false lifts. Let all
stabilisers of `U(1)` at the chosen level be trivial. Let `Ξ`, `Ξ'` be integral above `ℓ` and
orthogonal to the false lifts in the kernel of the descent (`IsTestForm`). Then the inner product of
their projections to the line has norm under `ι` at most `exp β` times the `ℓ`-part of the class
number of `U(1)` at that level. 
