---
{
  "module": "src/New/Determinant/AuxiliaryForms/FirstPath.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Determinant/AuxiliaryForms/FirstPath.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Determinant/AuxiliaryForms/FirstPath.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The maps `Θ^♭` and `res^♭`, and the first path

The first path consists of the spaces `Ỹ^m_0, …, Ỹ^0_0` and `Y₀, …, Y_m`, which are hermitian spaces
over the CM field `D.E`. These are the nodes `(z, 0, i)`, the first columns of the two grids:
`(false, 0, i)` is `Y_i` and `(true, 0, i)` is `Ỹ^i_0`. The iterated transposed lifts
`New.Data.transposedChain` along such a column are the transposes of the chain of theta lifts
`New.Exchange.weightedChain`. In the grid of the `Ỹ` the composite of all `m` of them is
`Θ^♭ = D.transposedChain 1 true 0`. The letter `ϑ` stands for an `m`-fold twist (`D.MFoldTwist`): a
tame character whose powers up to the `m`-th are non-trivial at each place of its modulus `Q`.

Notions from other files:
* `New.Data.GridForm` and `New.Data.TriangleForm`: in the grid of the `Y` (the Boolean `false`) the
  conjugate forms and the forms at a node; in the grid of the `Ỹ` (the Boolean `true`) the forms and
  the conjugate forms.
* `New.Data.triangleModulus`: the modulus of the point data along the first column of a grid. It is
  `𝔪₀ = π_M Q` for the `Y` and `𝔟 = π_M ^ b` for the `Ỹ`, with `π_M = D.piM`.
* `New.Data.triangleGLCard`: the index `n_𝔪₀(Y_i)` or `n_𝔟(Ỹ^i_0)` of the level of that modulus.
  Each lift and each transposed lift along the column is multiplied by the index of its smaller
  space; for the `Ỹ` these factors are constants.
* `New.Data.principalForms`: the forms of the level `J_M = D.chosenLevel`, here on `Y₀`.
* `New.Data.lowerChainUpTo`: the chain of twisted lifts from `Y₀` to `Y_j`; for `j = m` it is `Θ_ϑ`.

## Main definitions and results

* `New.Data.eq_zero_of_weightedChain_triangleLift_eq_zero`,
  `New.Data.gridLevelForms_eq_map_transposedChain`: the chain of the `Ỹ` is injective on level `𝔟`,
  and its transpose `Θ^♭` is onto that level.
* `New.Data.IsFlatRestriction`: the map `res^♭`, given by its pairings;
  `New.Data.exists_isFlatRestriction_range_eq_top`: at a suitable real point it is onto.
* `New.Data.exists_isPathDatum_integral_eq`: the pairing with the lifts of a restriction is a
  constant multiple of a period of path data on the first path.

## Relation to the literature

See `New.Determinant.AuxiliaryForms.DeepLevelVanishing` for related work.


 ## Transposes of the chains of lifts, and surjectivity of `Θ^♭` 

### `gridChar_detFin_eq_one`

 Grid `z` is the grid of the `Y` for `z = false` and that of the `Ỹ` for `z = true`; its first
column has the nodes `0, …, m`. Let `χ = gridChar ϑ (!z) i n'` be the idele class character of
`U(1)` attached to the edge between the nodes `i` and `i + 1` of this column. It carries the twist
`ϑ ^ (i + 1)` for the `Y` and no twist for the `Ỹ`; the type `n'` enters only through the exponent
of the restriction `upsilonU1` to `U(1)` of the splitting character of the Weil representation.
Then `χ` is trivial on the determinant `detFin s u` of every finite integral point `u` of a unitary
group that is trivial modulo `triangleModulus z ϑ`, the ideal `π_M Q` for the `Y` and
`π_M ^ D.natB` for the `Ỹ`. The signs `s` are those of the hermitian form at the infinite places
and do not matter at the finite ones. 

### `pairWeil_gridChar_modDatum_eq_self`

 Let `S` and `T` be the hermitian spaces `D.gridSpace 0 z 0 i` and `D.gridSpace 0 z 0 (i + 1)` at
the nodes `i` and `i + 1` of the first column of the grid of the `Y` (`z = false`) or of the `Ỹ`
(`z = true`); the first argument `0`, the offset, selects the grids themselves. The product of their
adelic unitary groups acts on the data on `Hom(S, T)` by `New.pairWeil`, the Weil representation
times the characters `gridChar` of the edge on the two determinants. A pair `(u, u')` of finite
integral points that are trivial modulo the ideal `𝔫 = triangleModulus z ϑ` fixes the datum
`New.modDatum S T 𝔫 Ψ v`. This is the product of `v` at the infinite places, a vector of the Fock
model for the signs of `Hom(S, T)`, the function `Ψ` of matrices modulo `𝔫` at the places of `𝔫`,
and the vacuum elsewhere. 

### `formRep_transposedChain_eq_self`

 Let `φ` be an element of `GridForm z 0 D.m`: a conjugate form on `Y_m` for `z = false`, a form
on `Ỹ^m_0` for `z = true`. For a node `i < m` of that column, `transposedChain ϑ z i φ` is the image
of `φ` at the node `i` under the composite of the transposed theta lifts between neighbouring nodes,
a form with the weight `gridKernel z 0 i true`. Right translation `formRep` by a finite integral
point `u` that is trivial modulo `triangleModulus z ϑ` fixes this image. 

### `triangleRep_weightedChain_eq_self`

 The space `TriangleForm z 0 i` consists of forms on `Y_i` for `z = false` and of conjugate forms
on `Ỹ^i_0` for `z = true`. For `0 < i ≤ m` let `y` be such a form at the node `0`. Its image under
the weighted chain of the `i` theta lifts `triangleLift` between neighbouring nodes, the one from
the node `b` multiplied by `triangleGLCard z ϑ b`, is fixed under right translation `triangleRep` by
every finite integral point `u` of the unitary group at the node `i` that is trivial modulo
`triangleModulus z ϑ`. 

### `integral_transposedChain_mul_weightedChain`

 For a node `i ≤ m`, let `U` be the image of `y` under the weighted chain of the `i` theta lifts
`triangleLift`, the one from the node `b` multiplied by `triangleGLCard z ϑ b`, the index at `b` of
the level of modulus `triangleModulus z ϑ`. Let `T b = transposedChain ϑ z b` be the composite of
the transposed lifts, equally weighted, from the node `m` to the node `b`; it acts on `φ`, which has
the conjugate weight to that of `y`. Then `∫ T i φ * U = ∫ T 0 φ * y`, each integral over the adelic
unitary group `New.G` of the node with its measure `quotMeasure` on the automorphic quotient. 

### `eq_zero_of_weightedChain_triangleLift_eq_zero`

 The grid of the `Ỹ` (the Boolean `true`) has the weight of the `Y` with the opposite sign, so
its `TriangleForm`s are conjugate forms; `D.triangleBase true` consists of those on `Ỹ^0_0` of level
`𝔟 = D.piM ^ D.natB`. The weighted chain of all `D.m` theta lifts `New.Data.triangleLift` from
`Ỹ^0_0` to `Ỹ^m_0`, for the trivial twist `1`, is injective on this space. 

### `map_transposedChain_le_gridLevelForms`

 Let `Ỹ^i_0` be the hermitian space at the node `(0, i)` of the grid of the `Ỹ` (the Boolean
`true`), and `D.gridLevelForms i` the forms of level `𝔟` on it: those fixed under right translation
by the finite integral points congruent to `1` modulo `𝔟 = D.piM ^ D.natB`, a power of the generator
of the product of the chosen places. For `i < m` the transposed theta lift from `Ỹ^(i+1)_0` to
`Ỹ^i_0` is weighted by the index of that level on `Ỹ^i_0`. The composite
`Θ^♭ = D.transposedChain 1 true 0` of all `D.m` of them, for the trivial twist `1`, maps forms of
level `𝔟` on `Ỹ^m_0` to forms of level `𝔟` on `Ỹ^0_0`. 

### `gridLevelForms_eq_map_transposedChain`

 Take the transposed theta lifts from `Ỹ^(i+1)_0` to `Ỹ^i_0` for `i < D.m`. Their composite
`Θ^♭ = D.transposedChain 1 true 0`, for the trivial twist `1`, maps the forms of level `𝔟` on
`Ỹ^m_0` onto those on `Ỹ^0_0`. 


## The first path

Restrictions of forms that come from the definite space `Ỹ^m_0` reach every form of level `J_M` on
`Y₀`, and the pairing with the chain of lifts of such a restriction is a period of path data on the
first path.


### `exists_forall_diagonalPeriodForm_ne_zero`

 Every form is reached. Here `Y₀ = D.spaceY 0`, and `Ỹ^0_0` is its orthogonal sum with a line.
The level `J_M` consists of the finite integral points that are congruent to `1` modulo every chosen
place, that is, modulo every prime divisor of `π_M = D.piM`; `principalForms` are the forms of this
level. There is a real point `g₀` of `U(Ỹ^0_0)` such that for every such form `y ≠ 0` on `Y₀` there
is a form `φ` of level `𝔟 = π_M ^ D.natB` on the definite space `Ỹ^m_0` (`gridLevelForms D.m`) with
a nonzero pairing `diagonalPeriodForm` of the conjugate `conjForm` of `y` and `Θ^♭ φ` at `g₀`: the
integral of `star (y h)` times `(Θ^♭ φ) (h g₀)` over `U(Y₀)`. Here `Θ^♭` is
`D.transposedChain 1 true 0`, the composite of the transposed theta lifts whose datum at the places
of `𝔟` is the indicator of the inclusion matrix (`pointDatum`), each weighted by the index of the
level `𝔟` on its target. 

### `IsFlatRestriction`

 `r` is a restriction map `res^♭` at the real point `g` of the unitary group of `Ỹ^0_0`, the sum
of `Y₀` and a line, in the sense of its pairings: every form `y` on `Y₀` of level `𝔪₀ = π_M Q`,
where `Q` is the modulus of some twist, has the same pairing with `r φ` as with the function
`h ↦ (Θ^♭ φ) (h g)` on `U(Y₀)`. Here `φ` is a form of level `𝔟` on `Ỹ^m_0` and `Θ^♭` is
`D.transposedChain 1 true 0`. The forms `y` of the level `J_M` (that of the prime divisors of
`π_M`) are among these, and their pairings determine `r`. 

### `exists_isFlatRestriction`

 Let `g` be a real point (`GInf`) of the unitary group of `Ỹ^0_0`, the sum of `Y₀ = D.spaceY 0`
and a line. Some linear map `r` from the forms of level `𝔟 = π_M ^ D.natB`, where `π_M = D.piM`, on
`Ỹ^m_0` (`gridLevelForms D.m`) to the forms on `Y₀` of level `J_M` (`principalForms`: integral
points congruent to `1` modulo the prime divisors of `π_M`) satisfies `IsFlatRestriction g`. 

### `exists_isFlatRestriction_range_eq_top`

 Let `Ỹ^0_0` be the orthogonal sum of `Y₀` and a line. There are a real point `g` of its unitary
group and a surjective linear map `r` from the forms of level `𝔟 = π_M ^ D.natB` on `Ỹ^m_0` to the
forms on `Y₀` of level `J_M` with `IsFlatRestriction g r`: every form `y` on `Y₀` of level
`𝔪₀ = π_M Q`, for an `m`-fold twist with modulus `Q`, has the same Petersson product with `r φ` as
with the function `h ↦ (Θ^♭ φ) (h g)` on `U(Y₀)`. 

### `IsFlatRestriction.integral_lowerChainUpTo`

 Let `r` be a restriction map at `g` (`IsFlatRestriction`): it sends a form `φ` of level `𝔟` on
`Ỹ^m_0` to the form on `Y₀` with the Petersson products of `h ↦ (Θ^♭ φ) (h g)`. Let `y'` be in
`GridForm false 0 D.m`, a form on `Y_m` of the conjugate weight, and `ϑ` an `m`-fold twist. Then the
integral of `y'` times `lowerChainUpTo` of `r φ`, its image under the theta lifts twisted by `ϑ` and
weighted by level indices, is the period `diagonalPeriodForm` at `g`: the integral over `U(Y₀)` of
`y'Lift h * (Θ^♭ φ) (h g)`, where `y'Lift = transposedChain ϑ false 0 y'`. 

### `exists_isPathDatum_integral_eq`

 The twisted edges are those that carry a power of the twist `ϑ` (`IsVerticalEdge`). There are
functions `Ψ ϑ`, one for each twist `ϑ`, of tuples `EdgeTuple ϑ` and a constant `α` as follows.
* `Ψ ϑ` is a path datum (`IsPathDatum`) on the first path: a function of the matrices on its edges,
  invariant up to the edge characters under admissible families of group elements at the nodes, zero
  unless those on twisted edges have left inverses, with values sums of at most
  `edgeMatrixCountBound ϑ ^ (2 * D.m)` roots of unity.
* Whenever `r` is a restriction map at `g`, the pairing of a conjugate form `y'` on `Y_m` with the
  chain `lowerChainUpTo` of theta lifts of `r φ` is `α` times `gridPeriod`: the sum over the tuples
  `S` on the path of `Ψ ϑ S` times the period `diagonalPeriodForm` at `g` of the images of `y'` and
  `φ` under the transposed lifts with the matrices of `S` along the two halves. 

### `exists_isPathDatum_first`

 There are functions `Ψ ϑ`, one for each twist `ϑ`, of tuples `EdgeTuple ϑ`, a real point `g`, a
constant `α` and a map `r` from the forms of level `𝔟` on `Ỹ^m_0` onto the forms on `Y₀` of level
`J_M` as follows.
* `Ψ ϑ` is a path datum (`IsPathDatum`) on the first path: a function of the matrices on its edges,
  invariant up to the edge characters under admissible families of group elements at the nodes, zero
  unless those on twisted edges have left inverses, with values sums of at most
  `edgeMatrixCountBound ϑ ^ (2 * D.m)` roots of unity.
* The pairing of a conjugate form `y'` on `Y_m` with the chain `lowerChainUpTo` of theta lifts of
  `r φ` is `α` times `gridPeriod`: the sum over the tuples `S` on the path of `Ψ ϑ S` times the
  period `diagonalPeriodForm` at `g` of the images of `y'` and `φ` under the transposed lifts with
  the matrices of `S` along the two halves. 
