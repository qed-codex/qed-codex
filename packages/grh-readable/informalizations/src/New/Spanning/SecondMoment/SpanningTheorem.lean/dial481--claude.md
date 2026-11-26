---
{
  "module": "src/New/Spanning/SecondMoment/SpanningTheorem.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/SecondMoment/SpanningTheorem.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/SecondMoment/SpanningTheorem.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The dimension of the target and one good translate of the Poincaré map

For admissible data `D`, the finite group `Ḡ = D.chosenGL` acts on the forms on `Y₀`, and `e₀`
projects them onto the target `D.targetForms`, the good forms, of dimension `D.targetDim`. The
source `D.SourceForm` is the space of the forms that the Poincaré map `P = D.poincare` sends to
forms on `Y₀`. This file supplies the hypotheses of the lemma on one translate,
`New.isSpread_of_second_moment`, for `P` and draws its conclusion. The spanning theorem itself,
`New.Data.enough_forms`, is deduced in `New.Reduction.ShortAndEnough`.

## Main definitions and results

* `New.Data.targetDim_le_card_mul_besselDegree_mul_mass`: the target has dimension at most
  `#Ḡ · deg · mass_r`. It is counted on the definite space `D.spaceW D.m`, where the level is free.
* `New.Data.hasAmplitudeBlocks_scaledPoincare`: the blocks of `P* s P`, once `P` is scaled
  (`New.Data.scaledPoincare`).
* `New.Data.bad_types_rare`: `e₀` is a product of two central idempotents, one for each level prime,
  and their complements have a small coefficient at `1`.
* `New.Data.isNearIsometry_e₀_comp_scaledPoincare`,
  `New.Data.targetDim_mul_sum_hilbertSchmidtNorm_sq_le`: the two hypotheses of the lemma on one
  translate.
* `New.Data.isSpread_goodPoincare`: for every space of target forms, with share `α` of the
  dimension, some translate `s e₀ P` has a preimage of dimension at most about `(1 + α) / 2` times
  the dimension of the source.

Notions from other files:
* `New.Data.filling`: the data `New.Filling` attached to `D`: the level `N`, the two level primes
  with their chosen places, and Bessel systems chosen from `New.Data.exists_besselSystem`.
* `New.Filling.besselDegree`: the product `deg` of the formal degrees at the infinite places.
* `New.mass`: the mass `mass_r` of the genus of the standard lattice of rank `r`.
* `New.Data.paramW`: twice the parameter `New.Data.targetParameter`, indexed by the basis of `Y₀`.
* `New.Data.RowIndex`: the index set of the basis of `Y₀`.

## Relation to the literature

For every space `F` of target forms, with share `α` of the dimension, some translate `s e₀ P` has
rank modulo `F` at least nearly `(1 - α) / 2` times the dimension of the source. Spanning by
Poincaré series and the link between least second moment and tight frames are known in the
literature. Related work: Petersson, Über die Entwicklungskoeffizienten der automorphen Formen,
1932; Benedetto–Fickus, Finite normalized tight frames, 2003; Muić, Spectral decomposition of
compactly supported Poincaré series and existence of cusp forms, 2010.


 ## The dimension of the target 

### `decreasingPosition_paramW`

 At every infinite place `v`, the parameter `D.paramW v` decreases along the numbering
`D.basisNumber` of the basis of `Y₀`: exactly `D.basisNumber i` of its entries exceed the entry at
`i` (`decreasingPosition` is the number of larger entries). 

### `finrank_principalForms_spaceW`

 The forms of principal level on the definite space `D.spaceW D.m`, where the level is free, have
dimension `#Ḡ · mass_r` times the product over the infinite places of the formal degrees of the
parameter `D.paramW v` for the definite signs. Here `Ḡ = D.chosenGL` and `mass_r = mass D.E D.r`. 

### `targetDim_le_card_mul_besselDegree_mul_mass`

 **Dimension of the target.** For admissible data `D`, the dimension `D.targetDim` of the space
of good forms on `Y₀` is at most `#Ḡ · deg · mass_r`. 

 ## One translate of the Poincaré map 

### `goodPoincare`

 The map `#Ḡ · e₀ s P` from all source forms to the target forms. Here `Ḡ = D.chosenGL`, the map
`P = D.poincare` is the unscaled Poincaré map and `e₀ = D.e₀` projects onto the good forms. As `e₀`
is central, it is the translate by `s` of `#Ḡ · e₀ P`. 

### `levelRepresentation`

 The action of the finite group `Ḡ` on the forms of principal level, with the chosen places
sorted by the level prime below them. 

### `levelRepresentation_apply`

 The representation `D.levelRepresentation` sends an element `s` of `D.filling.ResidueGL`, the
finite group with the chosen places sorted by the level prime below them, to the action under
`D.principalRep (D.spaceY 0)` of its uncurried form `Sigma.uncurry s`. 

### `inner_levelRepresentation`

 The representation `D.levelRepresentation` is unitary. 

### `poincareScale`

 The factor `(vol J · ν) ^ (-1/2)` that makes the Poincaré map almost an isometry. Here `J` is
the principal level and `ν` the covolume of its unipotent points. 

### `poincareScale_pos`

 The scale of the Poincaré map is positive, as the principal level has positive volume. 

### `scaledPoincare`

 The Poincaré map times `D.poincareScale`, in the coordinates `D.sourceFormCoords` of the source
forms, whose standard inner product serves as the inner product of the source. 

### `hasAmplitudeBlocks_scaledPoincare`

 **Unfolding.** Let `S = D.filling` and let `P = D.scaledPoincare` be the scaled Poincaré map.
Let `s` lie in `S.ResidueGL`, the product of the general linear groups over the residue fields at
the chosen places above each of the two level primes. For classes `c, c'` and Bessel coordinates
`i, j`, with basis vectors `e` of the source, `⟪s P e_(c', j), P e_(c, i)⟫ = ν⁻¹ ∑_γ A_γ(i, j)`. The
sum is over the rational `γ` such that `h_c⁻¹ γ h_c'` is integral with reduction `s` (`S.termsOver`,
where `h_c = S.classRep c`). The amplitude `A_γ = S.amplitude .full c c' γ` is an integral over the
infinite places of `W(y) ⊗ W(γ⁻¹ y)^*` against cutoffs, where `.full` selects the Bessel function
`W` itself and not its cut. The explicit number `ν = S.unipotentCovolume` is the covolume, the same
for all `c`, of the group `S.classUnipotent c` of rational unipotent points in the real unipotent
group. 

### `goodIdempotentAbove`

 The idempotent `e_{p_i}` for the level prime `p_i = D.levelPrime i`: the sum of the
`⊗_w e_{c_w}` over the tuples `c` of allowed polynomials of degree `r` at the chosen places above
`p_i` that have a primitive member. 

### `isCentralProj_goodIdempotentAbove`

 The element `e_{p_i} = D.goodIdempotentAbove i` is a central idempotent of the group algebra at
the level prime `p_i`. 

### `levelRepresentation_goodIdempotentAbove_eq`

 The tensor product of the two idempotents `D.goodIdempotentAbove i` acts through
`D.levelRepresentation` as the projector `D.e₀` onto the good forms. 

### `re_coeff_one_sub_goodIdempotentAbove_le`

 The share of the bad types, those that the idempotent `e_{p_i} = D.goodIdempotentAbove i` kills,
is small at the level prime `p_i = D.levelPrime i`: the coefficient of `1 - e_{p_i}` at the identity
has real part at most `b⁻⁸ / 2`, where `b = D.b` is the weight at the places `D.bPlaces`. 

### `bad_types_rare`

 **Bad types are rare.** The two elements `e_{p_i} = D.goodIdempotentAbove i` of the group
algebras at the level primes `p_i` are central idempotents. Their tensor product
`piTensorElem D.goodIdempotentAbove` acts through `D.levelRepresentation` as the projector `D.e₀`
onto the good forms. The share of the bad types, those that `e_{p_i}` kills, is small: the
coefficient of `1 - e_{p_i}` at the identity has real part at most `b⁻⁸ / 2`, where `b = D.b`. 

### `isNearIsometry_e₀_comp_scaledPoincare`

 **Good forms.** The composite `e₀ P` of the scaled Poincaré map `P = D.scaledPoincare` with the
projector `e₀ = D.e₀` onto the good forms on `Y₀` is almost an isometry in mean square
(`IsNearIsometry`): `‖e₀ P pr_U‖² ≥ dim U - 5 b⁻⁴ D_X` for every subspace `U` of the source. Here
`‖·‖` is the Hilbert–Schmidt norm, `pr_U` the orthogonal projection onto `U`, `b = D.b`, and `D_X`
is the dimension of the source. 

### `sum_hilbertSchmidtNorm_scaledPoincare_sq_le`

 **Second moment.** For the scaled Poincaré map `P = D.scaledPoincare`, the sum over `s` in
`Ḡ = D.chosenGL` of the squared Hilbert–Schmidt norm `hilbertSchmidtNorm` of `P* s P` is at most
`1 + 9 b⁻⁴` times `D.filling.mainSecondMoment = D_X² / (deg · mass_r)`, where `D_X` is the dimension
of the source. 

### `targetDim_mul_sum_hilbertSchmidtNorm_sq_le`

 The second moment with the bound for the dimension of the target: `D.targetDim` times the sum
over `s` in `D.chosenGL` of `‖L* s L‖²` is at most
`#D.chosenGL (1 + 9 / D.b ^ 4) D.filling.sourceDim²`. Here `L = D.scaledPoincare` is the Poincaré
map times `D.poincareScale`, and `L*` is its adjoint. `‖·‖` is the Hilbert–Schmidt norm, `D.b` is
the scale `b` of the data, and `D.filling.sourceDim` is the dimension of the source. 

### `finrank_targetForms_ne_zero`

 The target is not zero, as the almost isometry `e₀ P` from the source has a range of positive
dimension. 

### `comap_scaledPoincare_eq_comap_goodPoincare`

 Let `s` lie in the finite group `D.chosenGL`, let `e₀ = D.e₀` be the projector onto the target
forms and let `P = D.scaledPoincare` be the scaled Poincaré map. A space `F` of target forms has the
same preimage under `e₀ s P` as under `D.goodPoincare s` read in the coordinates
`D.sourceFormCoords` of the source: the two maps differ only by nonzero factors. 

### `isSpread_goodPoincare`

 **One translate.** For `s` in the finite group `Ḡ = D.chosenGL`, the map `D.goodPoincare s` is
`#Ḡ · e₀ s Π`: the unscaled Poincaré map `Π = D.poincare` from the source forms `D.SourceForm` to
the forms on `Y₀`, then the translation by `s`, then the projector `e₀ = D.e₀` onto the target
forms. These maps spread (`IsSpread`): for every space `F` of target forms, with share `α` of the
dimension of the target, the preimage of `F` under one of them has dimension at most
`(1 + α + 3 ε₀) / 2 · D_X`, where `ε₀ = b⁻² / 8`. Here `b = D.b` is the weight at the places
`D.bPlaces`, and `D_X` is the dimension of `D.SourceForm`. 
