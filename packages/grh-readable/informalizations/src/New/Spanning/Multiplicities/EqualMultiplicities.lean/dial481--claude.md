---
{
  "module": "src/New/Spanning/Multiplicities/EqualMultiplicities.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Multiplicities/EqualMultiplicities.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Multiplicities/EqualMultiplicities.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Equality of multiplicities

The spaces `Y_0, W_1, …, W_m` share the group `G_fin`, the level and the parameter, and differ only
in their signs at the real places. Let `V`, `V'` be two hermitian spaces for whose signs the
parameter `New.Data.paramW` has gap `D.gap`. Then a spherical Hecke operator away from the level `M`
has the same trace on their good forms. The equality of traces is deduced from the comparison of
traces for a test function that is cuspidal at one split place (`New.trace_eq_of_isCuspidalAt`).

## Main definitions and results

* `New.Data.exists_heckeAlgebra_eq_mul_inner_of_hasSum_rallisTerm`: the sums of scalar multiples of
  the Rallis series on two spaces are the same multiples of matrix coefficients of one element of
  the Hecke algebra.
* `New.Data.trace_heckeOnGood_eq`, `New.Data.charpoly_heckeOnGood_eq`,
  `New.Data.det_heckeOnGood_eq`: equal traces, characteristic polynomials and determinants.
* `New.Data.rallisOnGood`, `New.Data.det_rallisOnGood_eq`: the Rallis series preserves the good
  forms and has the same determinant on the good forms of both spaces.
* `New.Data.finrank_goodForms_inf_eigenPart_eq`: each eigensystem has the same multiplicity.
* `New.Data.targetDim_eq_finrank_goodForms_spaceW`: the good forms on `Y_0` and on `W_j` have the
  same dimension.

Notions from other files:
* `New.Data.principalForms`: the forms fixed by the principal level `D.chosenLevel` at the chosen
  places above `M`.
* `New.Data.principalRep`: the action on them of `D.chosenGL = ∏ GL_r(𝔽_w)`, over the chosen places
  w.
* `New.Data.goodForms`: the image of the idempotent `D.e₀` on these forms.
* `New.Data.heckeAlgebra`, `New.Data.eigenPart`: the spherical Hecke operators away from `M`, and
  the part with a given eigensystem.
* `New.HCParam.HasGap`: entries of the parameter with different signs are at least `h` apart.

## Relation to the literature

The equality of traces is the analogue of the Jacquet–Langlands correspondence for a quaternion
algebra that is ramified exactly at the real places. Related work: Harris–Labesse, Conditional base
change for unitary groups, 2004; Labesse, Changement de base CM et séries discrètes, 2011.


### `exists_isPrimitivePolynomial`

 A family `c` in `D.goodTupleFamilies` consists of a polynomial `c x` over the residue field of
each chosen place `x`. Above each of the primes `p₀`, `p₁` these polynomials are monic of degree
`r = card D.RowIndex`, all allowed (`New.IsAllowedPolynomial`), and one of them is primitive. In
particular, some `c x` is primitive: irreducible, with a root that generates the units of the
extension of degree `r` of the residue field. 

### `exists_heckeAlgebra_inner_eq_inner_translate`

 Let `γ` be a finite point of the unitary group whose component is `1` at each place
`D.chosenPlace x`. There is a spherical Hecke operator `p` away from these places with
`⟪z, p y⟫ = ⟪z, γ y⟫` for every space `W` and all forms `z`, `y` on `W` of principal level. 

### `exists_rallisTerm_eq_inner`

 A term `D.rallisTerm ϑ j W z y i` of Rallis' inner product formula is a vacuum coefficient of
the Weil representation times `⟪z, γ y⟫`, for a representative `γ` of `i`, over the number of
matrices modulo the modulus of the twist. It is a matrix coefficient `⟪z, p y⟫` of a spherical Hecke
operator `p` away from the level `D.M`, the same for all spaces `W`. 

### `exists_heckeAlgebra_eq_mul_inner_of_hasSum_rallisTerm`

 Let the doubled parameter `D.paramW` have gap `D.gap` for the signs of `V` and of `V'`: at each
infinite place its entries are distinct and have the parity of `card D.RowIndex - 1`, and entries
with different signs are at least `2 * D.gap` apart. Let `D.rallisTerm ϑ j` be the terms of Rallis'
inner product formula for the tame character `ϑ` and the descent pair `D.descentPair ϑ j`. Suppose
that for all forms `z`, `y` of principal level the series of these terms times `a` sums to `B z y`
on `V`, and times `a'` sums to `B' z y` on `V'`. Then one spherical Hecke operator `p` gives
`B z y = a ⟪z, p y⟫` on `V` and `B' z y = a' ⟪z, p y⟫` on `V'`. 

### `trace_heckeOnGood_eq_sum`

 Let the parameter `D.paramW` have gap `D.gap` for the signs of `V`. As `e₀` projects onto the
good forms and is the sum of the idempotents `e_c = tupleIdem D.RowIndex c` of the good families `c`
of labels, the trace of a spherical Hecke operator `T` on good forms is the sum of the traces of
`T e_c` on all forms of principal level. 

### `trace_mul_tupleIdem_eq`

 Let the doubled parameter `D.paramW` have gap `D.gap` for the signs of `V` and of `V'`: at each
infinite place its entries are distinct and have the parity of `card D.RowIndex - 1`, and entries
with different signs are at least `2 * D.gap` apart. Let `c` be a good family of
labels: a polynomial `c x` of degree `r = card D.RowIndex` over the residue field of each chosen
place `x`, subject to the conditions of `D.goodTupleFamilies`. The product of the label idempotents
of the `c x` is an idempotent `e_c = tupleIdem D.RowIndex c` in the group algebra of the product of
the finite groups `GL_r`. For a spherical Hecke operator `T`, the operator `T e_c` has the same
trace on the forms of principal level of `V` and of `V'`: its test function is cuspidal at a place
`x` where the polynomial `c x` is primitive. 

### `trace_heckeOnGood_eq`

 Let the parameter `D.paramW` have gap `D.gap` for the signs of `V` and of `V'`. Then a spherical
Hecke operator away from `M` has the same trace on the good forms of `V` and of `V'`. 

### `charpoly_heckeOnGood_eq`

 Let the parameter `D.paramW` have gap `D.gap` for the signs of `V` and of `V'`. Then a spherical
Hecke operator away from `M` has the same characteristic polynomial on the good forms of `V` and of
`V'`, as the traces of all its powers agree. 

### `det_heckeOnGood_eq`

 Let the parameter `D.paramW` have gap `D.gap` for the signs of `V` and of `V'`. Then a spherical
Hecke operator away from `M` has the same determinant on the good forms of `V` and of `V'`. 

### `exists_hecke_eq_rallisOperator`

 Let the parameter `D.paramW` have gap `D.gap` for the signs of `V` and of `V'`. One spherical
Hecke operator acts on the forms of principal level of both spaces as `D.rallisOperator ϑ j`, the
operator whose matrix coefficient `⟪z, R y⟫` is the series of Rallis' formula for the tame
character `ϑ` and the descent pair `D.descentPair ϑ j` without its normalisation: the sum over the
cosets `i` of `N` times `D.rallisTerm ϑ j V z y i`, where `N` is the number of matrices over the
residue ring of `D.twistModulus ϑ 1` with rows `D.Y 1` and columns `D.RowIndex`. 

### `rallisOnGood`

 Let the parameter `D.paramW` have gap `D.gap` for the signs of `V`. The series of Rallis'
formula (`New.Data.rallisOperator`) preserves the good forms of `V`, as it acts as a spherical Hecke
operator. This is its restriction to the good forms. 

### `det_rallisOnGood_eq`

 Let `V`, `V'` be hermitian spaces with signs `s`, `s'`, and let the parameter `D.paramW` have
gap `D.gap` for both. Let `D.rallisOnGood V ϑ j` be the series of Rallis' formula for the tame
character `ϑ` and the descent pair `D.descentPair ϑ j`, restricted to the good forms of `V`. It has
the same determinant as the corresponding operator on the good forms of `V'`. 

### `trace_heckeOnGood_eq_finrank`

 Let `V` be a hermitian space with signs `s`, such that for each `v : D.Φ` the doubled parameter
`toHCParam s (D.paramW v)` has gap `D.gap` (`HasGap`). If `T` in `D.heckeAlgebra`, a spherical Hecke
operator away from the level, is `1` on `D.eigenPart V q` and `0` on `D.eigenPart V d` for `d ≠ q`,
then its trace on the good forms is the dimension of the good forms in `D.eigenPart V q`. 

### `finrank_goodForms_inf_eigenPart_eq`

 Let `V`, `V'` be hermitian spaces with signs `s`, `s'`, which may differ, and let the parameter
`D.paramW` have gap `D.gap` for both. For each eigensystem `q`, the good forms with eigensystem `q`
on `V` and on `V'` make up spaces of the same dimension. 

### `goodForms_inf_eigenPart_eq_bot_of_eq_bot`

 Let the parameter `D.paramW` have gap `D.gap` for the signs of `V` and of `V'`. An eigensystem
`q` that does not occur in the good forms of `V'` does not occur in those of `V`. 

### `targetDim_eq_finrank_goodForms_spaceW`

 For `1 ≤ j ≤ m` the good forms on `W_j = D.spaceW j` have dimension `D.targetDim`, which is the
dimension of the good forms on `Y_0 = D.spaceY 0`: the identity has the same trace on both. 
