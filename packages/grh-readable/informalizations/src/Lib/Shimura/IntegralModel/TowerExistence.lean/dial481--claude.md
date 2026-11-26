---
{
  "module": "src/Lib/Shimura/IntegralModel/TowerExistence.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Shimura/IntegralModel/TowerExistence.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Shimura/IntegralModel/TowerExistence.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Existence of the model: the tower of Kuga–Sato covers with its congruence relation

The end of the construction of the moduli tower. It goes from a universal family of PEL type
(`New.Variety.UniversalFamily`) to the structure `New.Variety.Model`, which is all that the point
counts use.

* `New.Variety.exists_model`: the model exists.
* `New.Variety.UniversalFamily.GraphClosure.congruenceRelation`,
  `New.Variety.UniversalFamily.GraphClosure.isTangentPoly_localTerm_of_translate`: the congruence
  relation and the tangent map at a fixed point, for the legs of a cover.

Notions from other files:
* `New.Variety.UniversalFamily`: a universal family of PEL type over `R`: a base scheme with an
  abelian scheme over it and its standing hypotheses. `New.Variety.UniversalFamily.GraphClosure` is
  the reduced closure of the graph of finitely many translations `a ↦ a·(g_j, 1)` of complex points;
  `C.proj j` projects it to the factor `j`, sending `C.point a` to `U.datumPoint 𝔪 (a.act g)`, the
  complex point of level `𝔪`, when `γ j = (𝔪, g)`.
* `New.Variety.Model`: the tower of Kuga–Sato varieties over `R`, given by a list of properties.
* `New.Variety.Cancels`: The integers `m i` add up to zero on every fibre of `v`, that is,
  `∑ m i • [v i] = 0` in the free abelian group on `V`.
* `New.Variety.IsSafe`: Safe places w of E: the place u of ℚ(√−d₀) below w satisfies
  `New.GaloisRep.IsSplitPrimeToDisc`, and 𝔑 lies neither in w nor in any place above ū.
* `New.Variety.IsNeat`: The level 𝔑 is neat: 𝔑 ≠ 0 and, whenever `x` is a signed frame with `ℓ` for
  some form (`New.Variety.IsSignedFrame`), every y in GL_n(E) with x⁻¹yx in `levelGU n 𝔑` (the
  subgroup of level 𝔑 of GL_n(𝔸f E), inside `GUPlus E n`, whose elements translate moduli points by
  `a.act`) that fixes ℓ under `New.Variety.ratConj` equals 1.

## Relation to the literature

Known result: Integral Kuga–Sato models for GU(1,n−1) with level covers and the congruence relation.
Here the smooth proper base is a closure of theta values with no moduli property. The covers are
reduced projective closures of tuples of isogenous points. The model asks for smoothness of the base
only, and of the covers that they are Galois on points in characteristic zero. The congruence
relation at good split places is part of the statement.
Source: Harris, Taylor, The geometry and cohomology of some simple Shimura varieties, 2001, III.4;
Kottwitz, Points on some Shimura varieties over finite fields, JAMS 5 (1992), §5.


### `New.Variety.cancels_moebius_of_factorsThrough_sup`

 The Möbius coefficients `(-1) ^ r * q ^ (r.choose 2)`, with `r = Module.finrank (ResField w) A`
the dimension of `A`, of the subspaces `A` of `k ^ n`, `k` the residue field of `w`, cancel along
every map that depends only on `A ⊔ W` for some `W ≠ ⊥`. 

### `New.Variety.UniversalFamily.GraphClosure.congruenceRelation`

 Suppose `D.β` is the image of (1 + √−d₀)/2, and `c` sends the complex point of each `a` in the
closure `C` to `U.datumPoint 1 a`. Let `w` be a split finite place that is safe for `D.level` and at
which `D` is good, with residue field `k` of order `q = l ^ f`, and let `𝔭 ⊆ R` contain the image of
`w`. Let `u A`, for each subspace `A` of `k ^ n`, be maps from `C` to the base that translate the
complex points by the Hecke element `invHeckeIsogeny w A`. Then `u` satisfies the congruence
relation modulo `𝔭` (`New.Variety.CongruenceRelation`) with coefficients
`(-1) ^ r * q ^ (r.choose 2)` and `l`-power Frobenius exponents `(n - r) * f`, where `r` is the
dimension of `A`. 

### `New.Variety.UniversalFamily.GraphClosure.isTangentPoly_localTerm_of_translate`

 The tangent map at a fixed point. Let `c` send the complex point of `a` in the closure `C` to
that of `a` in the base (`U.datumPoint 1 a`), and let `v` send it to that of the translate
`a.act g α`. Suppose `z` in GL_n(E) relates this translate to `a` at level `D.level` (`IsLevelIso`),
the characteristic polynomial of `z` is separable, and `a.reflection` is the marked reflection
`markedReflection z μ` for the index `μ`. Then `localTerm α z.val.charpoly μ` is
`det (1 - X (dc)⁻¹ dv)` on the tangent space at the point of `a`, which has dimension
`card D.Index - 1 + ν * abelianDim E D.Index`, up to a constant factor
(`New.Variety.IsTangentPoly`). 

### `New.Variety.UniversalFamily.GraphClosure.exists_point_act_eq`

 Two moduli points `a` and `b` with the same complex point in the base (`hab`) have the same
complex point in the closure `C` after `a` is translated by `κ⁻¹` for some `κ` in
`levelGU D.Index D.level`. 

### `New.Variety.UniversalFamily.GraphClosure.exists_forall_eq_apply_mk_of_translate`

 A map `f` from the closure `C` to the base that translates the complex points by `g` is
determined by the coset of `g` modulo `levelGU D.Index D.level`: there is one map `u` on all cosets
with `f = u ⟦g⟧` for every such `f`. The map `c` serves only (the hypothesis `_hc` is unused) to
show that maps to the base exist. 

### `New.Variety.injective_of_subalgebra_of_charZero`

 Maps from a subring `R` of a number field that contains the integers to fields of
characteristic zero are injective, as `R` is algebraic over `ℤ`. 

### `TowerQuot`

 The finite quotient of `levelGU D.Index D.level` by the normal core of its subgroup of level
`M`: the deck group of a cover of the tower in `New.Variety.exists_model`. 

### `towerPairs`

 The pairs `(𝔪, κ * g)` that define the cover of level `i` in `New.Variety.exists_model`: `κ`
runs over `New.Variety.TowerQuot D M` (through the chosen representative `out`) and `(𝔪, g)` over
`i`, `(1, 1)` and `(M, 1)`. 

### `UniversalFamily.GraphClosure.point_comp_proj_towerPairs`

 On the cover `C` of level `i` with pairs `New.Variety.towerPairs D M i`, the factor `(⟦κ⟧, x)`
of the point of `a` may be computed with the representative `κ` instead of the chosen one: the two
differ by an element of level `M`, which `hM` conjugates into the level of every pair. 

### `UniversalFamily.GraphClosure.exists_deck_towerPairs`

 The element `κ` of `levelGU D.Index D.level` acts on the cover `C` of level `i` by a map `p`
that permutes the factors, `(q, x) ↦ (κ⁻¹ q, x)`, and translates complex points by `κ⁻¹`. 

### `UniversalFamily.GraphClosure.eq_of_point_comp_deck_eq`

 The deck maps `p κ` act freely on complex points: if `p κ` and `p κ'` agree at the point of `x`,
then `κ` and `κ'` have the same class in `New.Variety.TowerQuot D M`. Compare the factors
`(⟦κ * q⁻¹⟧, (M, 1))`: the isomorphism between the two translates is an automorphism of level
`D.level`, hence trivial as the level is neat. 

### `New.Variety.exists_model`

 Let `U` be a universal family over `R` for the PEL data `D` (`New.Variety.UniversalFamily`),
where `E` contains ℚ(√−d₀) with d₀ ≡ 3 mod 4. Suppose that `D.level` is neat and that `D.β` is the
image of (1 + √−d₀)/2. Suppose also that `D` is good (`New.PEL.IsGoodAt`) at every finite place `w`
that is safe for `D.level`, meaning that the place of ℚ(√−d₀) below `w` is split and prime to the
discriminant, and that `D.level` lies neither in `w` nor in any place above its conjugate. Then for
every ν ≠ 0 there is a model `New.Variety.Model D.Index d₀ D.level ν R`, that is, a tower of
Kuga–Sato varieties over `R` with base `base`, schemes `cover i` and legs `leg` to the base, finite
deck groups `deckGroup i`, maps `mulMap` and complex points, satisfying the listed properties. 
