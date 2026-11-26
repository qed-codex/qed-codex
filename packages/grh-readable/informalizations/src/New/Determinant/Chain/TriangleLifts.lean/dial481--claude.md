---
{
  "module": "src/New/Determinant/Chain/TriangleLifts.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Determinant/Chain/TriangleLifts.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Determinant/Chain/TriangleLifts.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Theta lifts as a triangle of arrows: spaces, lifts, descents and the first lift

This file arranges the theta lifts between the hermitian spaces `D.gridSpace i z 0 n` in a triangle
of positions `(i, n)`. The flag `z` selects one of two chains of spaces; see
`New.Determinant.Chain.ChainNorms`. The lift and the transposed lift of forms along an edge
(`New.Exchange.IsEdgeFamily`) with a finite datum modulo a modulus are `New.Exchange.modLift` and
`New.Exchange.modTransposedLift`, and this file writes them as integrals and treats the opposite
space. It defines the spaces and lifts of the triangle, and it proves, for `i < m`, the injectivity
and the norm of the first lift of row `i` on the subspace of fixed level. It also defines the left
and reversed pairs, the descents `New.Data.triangleTransposedLift` from `(i, n + 1)` to `(i + 1, n)`
along a left pair, and the ascents `New.Data.triangleReversedLift` from `(i + 1, n)` to `(i, n + 1)`
along the reversed pair.

## Main definitions and results

* `New.Data.TriangleForm`, `New.Data.triangleLift`, `New.Data.triangleNegEquiv`,
  `New.Data.triangleBase`, `New.Data.triangleEmbedding`: the forms at `(i, n)`, the lift to
  `(i, n + 1)`, the copies at `(i, 0)` of the forms at `(0, 0)`, the subspace of fixed level, and
  its embedding at `(i, 0)`.
* `New.Data.triangleFirstLift`, `New.Data.exists_hasSum_inner_triangleFirstLift`: the first lift of
  a row, read on forms at `(0, 0)`; for `i < m`, its injectivity and norm on the subspace of fixed
  level, by Rallis' formula `New.SiegelWeil.rallis_inner_product_cosetTerm`.

Notions from other files:
* `New.Data.gridSpace`: The hermitian space at the node (i, j) of grid z with offset o, for the
  signs `New.Data.gridSigns`.
* `New.Data.chosenLevel`: The level J_M consists of the elements of K₀ = `New.stdLevel` that are 1
  modulo the chosen places `New.Data.chosenPlace`.
* `New.Data.triangleModulus`, `New.Data.triangleGLCard`: the modulus 𝔪 of the triangle, and the
  order of the general linear group of a node modulo 𝔪. A lift times this order is the lift for the
  measure that gives the principal level of 𝔪 the volume 1.

## Relation to the literature

See `New.Determinant.Chain.ChainNorms` for related work.


 ### The opposite space; lifts and transposed lifts as integrals 

### `integral_neg_quotMeasure`

 An integral over the automorphic quotient of the opposite space `S.neg` is the integral over
that of `S`, after pull-back along the identification `G.neg` of the two unitary groups. 

### `formNegEquiv`

 The linear isometry from forms of parameter `l` on `S` to forms of parameter `l` on the opposite
space `S.neg`, by the identification `G.neg` of the two unitary groups. 

### `formNegEquiv_formRep`

 The isometry `formNegEquiv` commutes with right translation by the finite adelic group. 

### `Exchange.modTransposedLift_eq_sum`

 The transposed lift `modTransposedLift S T α Φ Ψ e' e y` is linear in `Ψ`: it is the sum over
matrices `x` of `Ψ x` times the transposed lift for the indicator function `Pi.single x 1` of
`x`. 

### `Exchange.lift_modDatum_apply`

 The theta lift of a function `y`, with finite datum `Ψ` modulo `𝔪` and polynomial `Φ` at
infinity, is the integral of `y` against the theta kernel `modKernel`. 

### `Exchange.IsEdgeFamily.modTransposedLift_apply`

 Let `Φ` make an edge (`IsEdgeFamily`) with types `k` on `S`, `k'` on `T` and flag `d`. The
transposed lift to `S` of a form `x` on `T` of the conjugate type `k' !d` is the integral of `x`
over the quotient of `T` against the theta kernel `modKernel`. 

### `Exchange.IsEdgeFamily.modTransposedLift_formRep_inv_apply`

 Let the polynomial `Φ` make an edge (`IsEdgeFamily`) for the characters `α j`, `j : I`, and the
pairs `k`, `k'` of conjugate cuspidal types: its Fock vector matches the types `k d` and `k' d` in
the real Weil representation. Fix `j`, a function `Ψ` on matrices modulo `𝔪`, a finite adelic point
`u` of the group of `T` and a form `x` on `T` of type `k' !d`. The transposed lift to `S` of the
right translate (`formRep`) of `x` by `u⁻¹` is the integral of `x` over the automorphic quotient of
`T` against the right translate by `u` of `modKernel`, the theta kernel with characters `α j N`,
`α j N'` of the Schwartz function that is `Φ` at infinity, `Ψ` at `𝔪` and the vacuum elsewhere. 

### `pairWeil_flipScalar`

 The pair of central elements `𝔪.flipScalar` of the unitary groups of `S` and `T` acts on a datum
`φ`, in the Weil representation `pairWeil`, by the value of the character `pairChar`. 

### `oppositeChar`

 The character `(α M)⁻¹ υⁿ` on a space with index type `M` of cardinality `n`, where
`υ = upsilonU1` is the splitting character of the Weil data, restricted to the norm-one ideles. The
conjugate of a theta kernel with characters `α` is a multiple of a kernel from the opposite space
with these characters (`New.exists_conj_modKernel_eq_mul_modKernel_neg`). 

### `Exchange.IsEdgeFamily.exists_inner_modLift_eq_inner_modTransposedLift`

 Let `Φ` make an edge from `S` to `T` with characters `a j`, `j : I`, and flag `false`, and `Φ'`
an edge from the opposite space `S.neg` to `T` with the characters `oppositeChar (a j)` and flag
`true`. The pair on `S` and `S.neg` is `kernelPair l`, the discrete series kernels `typeKernel` of
the parameters `l` (at `false`) and `-l` (at `true`); the pair on `T` is `k'`. For every function
`Ψ` on matrices modulo `𝔪` there is a `Ψ'` such that the transposed theta lift `modTransposedLift`
from `T` to `S.neg` with `Φ'`, `Ψ'` is the adjoint of the theta lift `modLift` from `S` to `T` with
`Φ`, `Ψ`, once forms on `S` and on `S.neg` are identified by `formNegEquiv`. 

 ### The spaces and lifts of the triangle 

### `TriangleForm`

 The space of forms on the hermitian space `D.gridSpace i z 0 n` at position `(i, n)` of the
triangle. Their type at infinity is `typeKernel`, the product over the infinite places of the
discrete series kernels, for `D.gridParam z i 0 n`, which is twice the discrete series parameter. 

### `triangleRep`

 The action of the finite adelic unitary group by right translation on the forms at position
`(i, n)` of the triangle. 

### `triangleLift`

 The theta lift from the forms at position `(i, n)` of the triangle to those at `(i, n + 1)`,
for the twist `ϑ`. It adds the block `n + i + 1`. Its character `gridChar ϑ (!z) (n + i)` is the
character `liftChar` of index `n + i + 1`, twisted by `ϑ ^ (n + i + 1)` if `z` is false, times a
power of `upsilonU1`. Its polynomial at infinity `gridHarmonic` is the joint harmonic for the
weights of this character and the parameters of the two nodes, not negated (flag `false`). Its
finite datum is the point datum `New.Exchange.pointDatum` modulo `New.Data.triangleModulus`. 

### `triangleNegEquiv`

 For each `i`, the linear isometric isomorphism from forms at `(0, 0)` to forms at `(i, 0)`,
composed of `i` passages `New.formNegEquiv` to the opposite hermitian space. 

### `triangleNegEquiv_succ_apply`

 The isometry to row `i + 1` is the one to row `i` followed by passage to the opposite space. 

### `triangleBaseLevel`

 The level at the base corner of the triangle: the level `D.chosenLevel` on Y₀ if `z` is false;
if `z` is true, the principal level of `D.gridLevelGen`, the power `ϖ ^ D.natB` of the generator `ϖ`
of the product of the chosen places. 

### `triangleBase`

 The space of forms at the base corner of the triangle that are fixed by the level
`New.Data.triangleBaseLevel`. 

### `triangleEmbedding`

 The isometric embedding of `New.Data.triangleBase` in the forms at `(i, 0)`, through
`New.Data.triangleNegEquiv`. 

### `triangleNegEquiv_triangleRep`

 The isometries `New.Data.triangleNegEquiv` commute with right translation by the finite adelic
group. 

 ### The first lift 

### `triangleRep_triangleNegEquiv_of_mem_triangleBaseLevel`

 For a form `y` of `New.Data.triangleBase`, its image `D.triangleNegEquiv z i y` in row `i` is
fixed by `D.triangleRep z i 0 u` for every `u` in `New.Data.triangleBaseLevel`. 

### `levelOfSubgroup_bot_le_triangleBaseLevel`

 The principal level of the modulus of the triangle is contained in the base level. 

### `hasLevel_triangleNegEquiv`

 The copy in row `i` of a form of `New.Data.triangleBase` is fixed by the principal level of the
modulus `New.Data.triangleModulus z ϑ`. 

### `exists_triangleRep_triangleLift_eq_smul`

 Let `i < D.m`, the number of lifts of the data `D`, and let `triangleLift z ϑ i 0` be the theta
lift, for the twist `ϑ`, from forms at the node `(i, 0)` of the triangle `z` to forms at `(i, 1)`.
For an integral point `u` (`stdLevel`) of the finite adelic unitary group at `(i, 0)` there is a
finite adelic point `g` at `(i, 1)` such that the lift intertwines the right translations
`triangleRep` by `u` and `g` up to a scalar `c` of absolute value `1`. 

### `isSharp_pointDatum`

 Let `F` be the finite datum of the theta lift from the hermitian space `gridSpace` at the node
`(i, 0)` of the triangle `z` to that at `(i, 1)`: the indicator function `pointDatum` of the
inclusion matrix modulo `𝔪 = triangleModulus z ϑ`, and the vacuum off `𝔪` (`vacuumDatum`). For the
character `gridChar` of the lift on the target, `F` is sharp for the principal level
`J = 𝔪.levelOfSubgroup ⊥`: at the places of `𝔪` its matrix coefficient is `⟨F, F⟩` times the
indicator function of `J`. Its mass `⟨F, F⟩ / [K₀ : J]`, with `K₀ = stdLevel` the integral points,
is the inverse of the number of matrices of this size modulo `𝔪`, divided by `triangleGLCard z ϑ 0`,
the order of the general linear group of the source modulo `𝔪`. 

### `triangleFirstLift`

 The first lift of row `i`, read on forms at the base corner: the copy of `y` at `(i, 0)`
(`New.Data.triangleNegEquiv`) is lifted to `(i, 1)`. 

### `TriangleCoset`

 The cosets, in the finite adelic group at the base corner, of the points that are integral off
the places of `New.Data.triangleModulus z ϑ` and their conjugates. 

### `triangleRallisTerm`

 The term at the coset `γ` of the series for the inner product of two first lifts of row `i`.
It is `New.SiegelWeil.cosetTerm M b`, the number `⟪x, g y⟫` times `vacuumCoeff M b g` at the
representative `g` of `γ`, for the rank `M` and the character `b` of the target of the lift, divided
by the number of maps from `GridIndex z 0 1 × GridIndex z 0 0` to the residue ring of the
modulus. 

### `two_mul_card_gridIndex_zero_lt`

 For either grid `z`, the index set `D.GridIndex z 0 1` of the node `(0, 1)` has more than twice
as many elements as the index set of the node `(0, 0)`, so Rallis' formula applies to the first lift
of each row. 

### `mem_triangleBase_of_inner_eq_inner_triangleFirstLift`

 Let `i < D.m`, the number of lifts of the data `D`. Let `a = triangleFirstLift z ϑ i` copy a
form from the corner `(0, 0)` of the triangle `z` to `(i, 0)` and lift it to `(i, 1)`, and let `y`
lie in `triangleBase`, the forms at the corner fixed by `triangleBaseLevel`. A form `v` at the
corner with `⟪v, x⟫ = ⟪a y, a x⟫` for all `x` lies in `triangleBase`. 

### `eq_zero_of_triangleFirstLift_eq_zero`

 For `i < D.m`, the first lift of row `i` is injective on `New.Data.triangleBase`. 

### `exists_hasSum_triangleRallisTerm`

 The inner product formula for `a = triangleFirstLift z ϑ i`, which copies a form from the corner
`(0, 0)` of the triangle `z` to `(i, 0)` and lifts it to `(i, 1)`. Here `i < D.m`, the number of
lifts of the data `D`. There is a constant `C` such that for every twist `ϑ`, every form `y` at the
corner fixed by the base level (`triangleBase`) and every form `x` at the corner, the series of the
terms `C * triangleRallisTerm` converges to `triangleGLCard z ϑ 0 * ⟪a x, a y⟫`; the first factor is
the order of the general linear group of the corner modulo `𝔪 = triangleModulus z ϑ`. 

### `exists_hasSum_inner_triangleFirstLift`

 Injectivity and inner product formula for `a = triangleFirstLift z ϑ i`, which copies a form
from the corner `(0, 0)` of the triangle `z` to `(i, 0)` and lifts it to `(i, 1)`. Here `i < D.m`,
the number of lifts of the data `D`. There is a constant `C` such that for every twist `ϑ` and every
form `y` at the corner fixed by `triangleBaseLevel` (`triangleBase`) two statements hold. (a) If `v`
satisfies `⟪v, x⟫ = ⟪a y, a x⟫` for all `x`, then `v` lies in `triangleBase`, and `v = 0` implies
`y = 0`. (b) For every form `x` at the corner, the series of the terms `C * triangleRallisTerm`,
multiples of `⟪x, g y⟫`, over the cosets `TriangleCoset` of the finite points `g` modulo those
integral off `𝔪 = triangleModulus z ϑ` and its conjugate, converges to
`triangleGLCard z ϑ 0 * ⟪a x, a y⟫`; the first factor is the order of the general linear group of
the corner modulo `𝔪`. 

### `exists_flipPoly_map_conj_eq`

 Every polynomial `P` is the signed transpose `flipPoly s t` of the polynomial obtained from some
`Q` by conjugating the coefficients. 

 ### Left and reversed pairs, descents and ascents 

### `triangleKernel`

 The kernels at infinity of the node `(i, n)` of the triangle: that of the parameter `gridParam`
for `b = false`, and that of its negative for `b = true`. 

### `leftPairChar`

 The character of the left pairs that add the block `i + 1`, on a space with index type `M`: the
inverse of the character `gridChar ϑ (!z) (0 + i)` of the first lift `triangleLift z ϑ i 0` of row
`i`, times `upsilonU1` (the splitting character on the norm-one ideles) to the rank of the space. 

### `EdgePoly`

 Polynomial data at infinity for an edge from a node in column `n` to a node in column `n'`. 

### `EdgeDatum`

 Finite data for an edge from a node in column `n` to a node in column `n'`. 

### `IsLeftPair`

 The polynomial `Φ` makes an edge (`IsEdgeFamily`) along the left pair, from the node
`(i + 1, n)` to the node `(i, n + 1)`, with the characters `leftPairChar` of row `i`. 

### `IsReversedPair`

 The polynomial `Φ` makes an edge along the reversed pair, from the node `(i, n + 1)` to the
node `(i + 1, n)`, each space with its character in `IsLeftPair`. 

### `triangleTransposedLift`

 The transposed lift along the left pair, from forms at the node `(i, n + 1)` to forms at the
node `(i + 1, n)`, with polynomial `Φ` and finite datum `Ψ`. 

### `triangleReversedLift`

 The transposed lift along the reversed pair, from forms at the node `(i + 1, n)` to forms at the
node `(i, n + 1)`, with polynomial `Φ` and finite datum `Ψ`. 

### `triangleDatumLift`

 The theta lift from the node `(i, n)` to the node `(i, n + 1)` with an arbitrary finite datum
`Ψ`; `triangleLift` is the case of the point datum `pointDatum`. 

### `triangleTransposedLift_eq_sum`

 The transposed lift `triangleTransposedLift` with finite datum `Ψ` equals the sum, over matrices
`η` modulo `triangleModulus z ϑ`, of `Ψ η` times the lift with the datum `Pi.single η 1`. 

### `triangleReversedLift_eq_sum`

 The reversed lift `triangleReversedLift` with finite datum `Ψ` equals the sum, over matrices `η`
modulo `triangleModulus z ϑ`, of `Ψ η` times the lift with the datum `Pi.single η 1`. 

### `fourierDatum`

 The Fourier transform of the complex conjugate of a finite datum, a datum for the edge read
backwards. 

### `isEdgeFamily_triangleKernel`

 For `i + n < D.m`, the kernels, characters and polynomial of the lift from the node `(i, n)` to
the node `(i, n + 1)` form an edge (`IsEdgeFamily`). 
