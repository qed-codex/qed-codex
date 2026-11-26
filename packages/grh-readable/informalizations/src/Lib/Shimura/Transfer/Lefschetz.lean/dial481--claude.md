---
{
  "module": "src/Lib/Shimura/Transfer/Lefschetz.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Shimura/Transfer/Lefschetz.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Shimura/Transfer/Lefschetz.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# h-null Hecke elements and the Lefschetz formula as a sum over marked pairs

Translates the geometric vanishing of local terms on a tower of Kuga–Sato varieties into a vanishing
of a sum over marked pairs, which involves only the Hecke function.

* `New.Variety.IsNullHecke`: h-nullity of a Hecke element, a condition on regular elements.
* `New.Variety.OccursInWeight`: a system of eigenvalues θ occurs in weight h.
* `New.Variety.Model.isNullHecke_of_isNullFamily`: h-null on deep levels of the tower implies
  h-null.

Idea: coincidences of two maps to the base are grouped by their marked pair; each fibre has (number
of lattice solutions) · (order of the deck group) points, and the number of solutions cancels the
denominator of the local term.

Notions from other files:
* `New.Variety.GUPlus`: the monoid of similitudes `g` whose inverse has integral entries, that is,
  which enlarge the standard lattice.
* `New.Variety.heckeAlgebra`: the Hecke algebra, the subalgebra of elements ∑ a_g [g] of k[G]
  supported on `GUPlus E n` whose function ∑ a_g 1_{g·levelGU n 𝔑} is left `levelGU n 𝔑`-invariant.
* `New.Variety.levelGU`: the principal level K(𝔑), the similitudes in `GL_n(Ô E)` that are congruent
  to `1` modulo `𝔑`.
* `New.Variety.Model`: the tower of Kuga–Sato varieties over `R`, given by a list of properties.
* `New.Variety.IsNeat`: the level 𝔑 is neat: 𝔑 ≠ 0 and, whenever `x` is a signed frame with `ℓ` for
  some form (`New.Variety.IsSignedFrame`), every y in GL_n(E) with x⁻¹yx in `levelGU n 𝔑` that fixes
  ℓ under `New.Variety.ratConj` equals 1.

## Relation to the literature

Known; see `Lib.Shimura.Transfer.WeightOccurs` for sources.


### `IsNullHecke`

 `b` is `h`-null; the condition is void if `b` is not regular. For every `α : Fin ν → 𝓞 E`:
finitely many classes of marked triples (flag `True` of `New.Variety.countTerm`) have a non-zero
term with weight 1 (this part does not depend on `α`), and the sum over the classes of the value of
`b` times the coefficient of `X ^ h` in the local term `New.Variety.localTerm` at `2 α` is 0. Only
even multipliers `2 α` are used: for them the determinant of `1 - 2 α y` on the lattice is odd,
hence non-zero. 

### `OccursInWeight`

 θ occurs in weight h: for every linear combination p of words in the operators `tauHecke` with
p(θ) = 1, some b·p with b in the Hecke algebra is not `h`-null in the sense of
`New.Variety.IsNullHecke`. 

### `relIndex_comap_one_sub_two_smul`

 Let the rational matrix `z` be integral in the frame `x`, and let `β` be an integer of `E`. Then
`B = 1 - 2 β z` maps the lattice `frameLattice x` into itself, `det B ≠ 0`, and the index of the
lattice in its preimage under `B` is the product of the `σ (det B)` over the complex embeddings
`σ`. 

### `tripleClass`

 The class under `GL n E` of the marked triple `(x · levelGU n 𝔑, t)`: the coset of `x` and the
pair `t`. 

### `triple_class_eq_iff`

 Let the reflections of `p` and `p'` be those of the marked elements `t` and `t'`. The triples of
`(p.frame, t)` and `(p'.frame, t')` have the same class if and only if some `w` conjugates `t'` to
`t` and is an isomorphism from `p'` to `p`, once the vectors of `p` are replaced by the `w P'_j`. 

### `Model.point_comp_deck_injective`

 At a neat level, let the vectors of `p` run through representatives `u` of the groups `L j`
modulo the lattice of `p.frame`, and let `δ` run through the deck group. The points so obtained on
level `i` are distinct. 

### `solutionLattice`

 The group of vectors `P` with `(1 - 2 β z) P` in the lattice `frameLattice x`: the solutions of
`P ≡ 2 β z P` modulo the lattice of `x`. 

### `SolutionQuotient`

 The solutions of `P ≡ 2 β z P` modulo the lattice of `x`. 

### `frameLattice_le_solutionLattice_and_card`

 If the Hecke function of `b` is non-zero at `invAutInFrame z x` and `β` is an integer of `E`,
then the lattice of `x` lies in `solutionLattice x z β`, `det (1 - 2 β z) ≠ 0`, and the number of
solutions modulo the lattice is the product of the `σ (det (1 - 2 β z))` over the complex
embeddings `σ`. 

### `IsFixedPair`

 The pair `t = (z, μ)` is fixed at the point `p` for the Hecke element `b` and the multipliers
`2 α`: the Hecke function of `b` is non-zero at `invAutInFrame z p.frame`, the reflection of `p` is
the reflection of `z` marked by `μ`, and every vector `p.markedPoint j` lies in
`solutionLattice p.frame z (α j)`. 

### `IsFixedPair.heckeCosetFn_ne_zero`

 The Hecke function of `b` is non-zero at `invAutInFrame t.fst p.frame`. 

### `IsFixedPair.reflection_eq`

 The reflection of `p` is the reflection of `t.fst` marked by `t.snd`. 

### `IsFixedPair.mem_solutionLattice`

 Every vector of `p` is a solution of `P ≡ 2 α_j t.fst P` modulo the lattice. 

### `IsFixedPair.conj`

 An isomorphism `z` from `p` to `p'` carries a fixed pair `t` of `p` to the fixed pair
`(z t.fst z⁻¹, t.snd)` of `p'`. 

### `existsUnique_isFixedPair`

 At a neat level and for a regular `b`, let `invAutInFrame z p.frame` (that is,
`p.frame⁻¹ z⁻¹ p.frame`) lie in the coset `γ`, at which the Hecke function of `b` is non-zero, and
let `z` fix the reflection of `p` and make the vectors of `p` solutions. Then exactly one pair `t`
is fixed at `p` with `invAutInFrame t.fst p.frame` in `γ`: `t.fst` is `z` by neatness, and the mark
`t.snd` is unique by regularity. 

### `eval_one_localTerm`

 At a fixed pair `t` of `p`, the value at `1` of the local term at `2 α` is the number of
solutions modulo the lattice: the Lagrange factor of `localTerm` is `1` at `1`, and the other
factors multiply to `∏ j, ∏ σ, σ (det (1 - 2 α_j t.fst))`. 

### `isLevelIso_act_iff`

 For `γ` with representative in `GUPlus E n`, the point `p · (γ, 2 α)` is isomorphic to `p` by
`z` exactly when `invAutInFrame z p.frame` lies in the coset `γ`, `z` fixes the reflection of `p`,
and the vectors of `p` are solutions of `P ≡ 2 α_j z P` modulo the lattice. 

### `eval_one_localTerm_ne_zero`

 At a fixed pair `t` of `p`, the local term at `2 α` does not vanish at `1`. 

### `IsFixedPair.isSignedFrame`

 At a fixed pair `t` of `p`, the frame of `p` is signed for the reflection of `t.fst` marked by
`t.snd`. 

### `exists_isFixedPair_of_countTerm_ne_zero`

 A class `c` of marked triples whose term for `b` is non-zero is the class of a fixed pair: the
pair of `c` at the point with the frame of `c`, the reflection of the pair, and the vectors `0`. 

### `Model.comp_leg_eq_of_comp_deck_eq`

 Moving a point of level `i` by a deck transformation does not change its image under
`X.leg i ⟦1⟧`. 

### `Model.point_mem_range_of_class_eq`

 Let `t` be a fixed pair of `p` and `t'` one of `p'`, with the same class of triples. Then the
point of `p'` on level `i` is the point of `p` with its vectors replaced by solutions `u`, moved
by a deck transformation `δ`. 

### `Model.exists_isFixedPair_of_point_eq`

 Let `t` be a fixed pair of `p`. If the point of `p'` on level `i` is the point of `p` with its
vectors replaced by solutions, moved by a deck transformation, then some fixed pair `t'` of `p'`
has the class of triples of `t`. 

### `eq_of_isFixedPair_of_class_eq`

 At a neat level, two fixed pairs of the same point with the same class of triples are equal:
the isomorphism between them given by the class is `1`. 

### `IsFixedPair.ratConj_reflection_eq`

 At a fixed pair `t` of `p`, `t.fst` fixes the reflection of `p`. 

### `Model.isTangentPoly_localTerm`

 Let `t` be a fixed pair of `p` with `invAutInFrame t.fst p.frame` in the coset `γ`, whose
representative `γ.out` lies in `GUPlus E n` and in `X.legIndices i`. Then at the point of `p` on
level `i`, the local term at `2 α` is a tangent polynomial at `y = X.point i p` for `X.leg i ⟦1⟧`
and `X.leg i γ.out ≫ X.mulMap (2 α)` (`X.tangent`). 

### `Model.bijOn_points_setOf_class_eq`

 The fibres of the classes of coincidences. Let `q` lift the points of level `i`, `S` be a set
of pairs `⟨c, y⟩` (coset, point) as in `mem_S_iff`, and `r s` the fixed pair of `s` (`hr`,
`r_unique`). For a fixed pair `t` of `p`, the pairs in `S` with the class of `t` correspond, by
their points, to the points of `p` with solutions as vectors, moved by a deck transformation. 

### `Model.isNullHecke_of_isNullFamily`

 The Lefschetz formula as a sum over marked pairs. Let `𝔑` be neat. If on all large levels `i`
and for all `α` the combination of the maps `X.leg i q ≫ X.mulMap α`, `q` a coset with coefficient
the value of `b` at `q`, is `h`-null in the geometric sense (`New.Variety.IsNullFamily`, dimension
`X.dimension`), then `b` is `h`-null in the sense of `New.Variety.IsNullHecke`. 
