---
{
  "module": "src/Lib/Cohomology/Etale/ProperFunctors.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Cohomology/Etale/ProperFunctors.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Cohomology/Etale/ProperFunctors.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Local-to-global principle, density criteria and proper functors for cohomology on test rings

This file studies the cohomology `Hⁿ(Y) = Extⁿ(ℤ[Y], F)` of set-valued functors `Y` on rings,
computed on test rings, with `F = New.Variety.locConstCoeff Λ` the locally constant `Λ`-valued
functions. Two criteria for density, for affine maps and for finitely many affine subfunctors, are
tested on points in valuation rings of algebraically closed fields.

## Main definitions and results

* `New.Variety.IsTestCohomEquiv.of_connected`: the local-to-global principle. A map
  `u : X ⟶ Y` that induces isomorphisms on cohomology (`New.Variety.IsTestCohomEquiv`) over every
  connected piece of `Y` induces them over `Y`. This needs `X` and `Y` cohomologically continuous
  (`New.Variety.IsCohomContinuous`). The pieces are loci `U a` of a zero-locus family `U` with
  `U (span {e}) ⊔ U (span {1 - e})` dense for every idempotent `e`.
* `New.Variety.IsRelAffine.hasCohomDenseImage_of_lifts`: an affine map that is onto on such points
  has dense image.
* `New.Variety.IsCohomDense.of_affine_cover`: `U` is dense if each such point lies in one of
  finitely many affine subfunctors whose points in test rings belong to `U`.
* `New.Variety.IsProperOver.hasCohomDenseImage_of_surjective`: a map of proper functors, onto on
  geometric points, has dense image (`New.Variety.IsCohomDense`) for locally constant coefficients
  `New.Variety.locConstCoeff Λ`.
* A density criterion for finitely many maps `P i : Y ⟶ Z` into a proper functor:
  `New.Variety.IsProperOver.isCohomDense_of_coincidences`. It is
  `New.Variety.IsCohomDense.of_affine_cover` for the closed loci on which prescribed pairs of the
  maps agree.
* `New.Variety.ellAdicCohom.transfer`: let `c : W ⟶ Y` be a Galois covering of proper schemes with
  finite group `Δ`. Then the `ℓ`-adic cohomology of `Y` embeds in that of `W` and reaches all
  `Δ`-invariant classes.

Notions from other files:
* `New.Variety.IsRelAffine`: The property of a map X → Y of set-valued functors on rings that its
  pull-back along every point h_A → Y is representable, of the form h_B → h_A.
* `New.Variety.IsCohomDense`: The subfunctor U of Y is dense for F: for every point h_A → Y, the
  inclusion of the preimage of U in h_A is an equivalence for F.
* `New.Variety.reprBy`: The functor h_A = Hom(A,−) represented by the object A.
* `New.Variety.IsTest`: a test ring A is reduced and absolutely integrally closed, and any a, b ∈ A
  admit an idempotent e with a ∣ eb and b ∣ (1 − e)a.
* `New.Variety.IsProperOver`: The functor Z on rings is proper over D: its diagonal is closed, and
  it satisfies a valuative criterion for valuation rings of algebraically closed fields.
* `New.Variety.locConstCoeff`: For an abelian group Λ, the coefficient functor on test rings sending
  A to the group of locally constant functions Spec A → Λ.

## Relation to the literature

Known; see `Lib.Cohomology.Etale.FilteredLimits` and `Lib.Cohomology.ProperBaseChange.Theorem` for
sources.



## Zorn's lemma, Mayer–Vietoris and reduction to connected pieces

The local-to-global principle is proved by Zorn's lemma over the ideals of a ring `R` and by
Mayer–Vietoris for subfunctors `U, V ≤ W` of a set-valued functor `Y` with `U ⊔ V` dense in `W`.
Here `U.whisker testIncl` is `U` restricted to test rings, `homOfLe h` is the inclusion map given
by `h : U ≤ W`, and `TestCohomology.map Λ f n` is the pull-back `Hⁿ(W) → Hⁿ(U)` along `f`.


### `IsRelAffine.preimage`

 If the inclusion of the subfunctor `U` into `Y` is relatively affine (`New.Variety.IsRelAffine`:
its pull-back along every point is representable), so is the inclusion of its preimage under any
`f : X ⟶ Y`. 

### `map_biprod_lift_neg_biprodAddEquiv_symm`

 Pull-back along `(f, -g) : M ⟶ N ⊞ N'` sends the class with components `x`, `y` to
`f^* x - g^* y`. 

### `TestCohomology.isCohomEquiv_sup_of_isCohomDense`

 On test rings, let `U ⊔ V ≤ W` (this is `h_le`), and let `U ⊔ V`, seen as a subfunctor of `W`,
be dense in `W` for the locally constant `Λ`-valued coefficients. Then the inclusion `U ⊔ V → W`
induces isomorphisms `Hⁿ(W) → Hⁿ(U ⊔ V)` in every degree. 

### `TestCohomology.prod_map_homOfLe_eq_comp`

 The restriction `Hⁿ(W) → Hⁿ(U) × Hⁿ(V)` on test rings is the restriction to `U ⊔ V`, followed by
the pull-back along `ℤ[U] ⊞ ℤ[V] → ℤ[U ⊔ V]` and the splitting of the cohomology of the sum. 

### `TestCohomology.mayer_vietoris_injective_of_sub_surjective`

 Mayer–Vietoris for subfunctors `U, V ≤ W` of `Y`, in the cohomology `H` of the free abelian
functors `ℤ[−]` restricted to test rings (`testIncl`), with coefficients `locConstCoeff Λ`
(A ↦ locally constant functions Spec A → Λ). Assume `U ⊔ V` is dense in `W` for these coefficients
(`IsCohomDense`: for every point h_A → W on test rings, the inclusion of the preimage of `U ⊔ V`
into h_A induces bijections on all `Ext^n(−, locConstCoeff Λ)`). If in each degree `m < n` every
class on `U ⊓ V` is a difference of restrictions of classes on `U` and on `V`, then the restriction
`Hⁿ(W) → Hⁿ(U) × Hⁿ(V)` is injective. 

### `TestCohomology.mayer_vietoris_bijective`

 Mayer–Vietoris for subfunctors `U, V ≤ W` of `Y` with `U ⊔ V` dense in `W`, on test rings with
locally constant `Λ`-valued coefficients: if `U ⊓ V` has points only over the zero ring, then the
restriction `Hⁿ(W) → Hⁿ(U) × Hⁿ(V)` is bijective. 

### `TestCohomology.mayer_vietoris_injective`

 Mayer–Vietoris for `U, V ≤ W` with `U ⊔ V` dense in `W`, on test rings with coefficients `Λ`,
with `U ⊓ V` given as `T` and `hT`: `Hⁿ(W) → Hⁿ(U) × Hⁿ(V)` is injective if in each degree `m < n`
every class on `T` is a difference of restrictions from `U` and `V`, and bijective if `T` has
points only over the zero ring. The two halves are `mayer_vietoris_injective_of_sub_surjective`
and `mayer_vietoris_bijective`. 

### `forall_gt_of_chain_counterexample`

 Downward induction by Zorn's lemma. Let `P` be a property of the elements above `a`. If every
nonempty chain of counterexamples has an upper bound that is a counterexample, and `P` holds at `m`
as soon as it holds strictly above `m`, then `P` holds everywhere above `a`. 

### `injective_of_isFilteredColimit_of_map_eq_zero`

 Downward induction, injective half. Let `π` be a natural map (`h_nat`) between functors `G`, `K`
from a partial order `α` to abelian groups, such that every nonempty directed subset has a cocone
whose images under `G` and `K` are filtered colimits (`h_colim`). If each element of the kernel of
any `π a` that dies at all `b > a` is zero (`h_step`), then `π a` is injective. 

### `surjective_of_isFilteredColimit_of_exists_lift`

 Downward induction, surjective half. Let `G, K : α ⥤ Ab` be functors on a partial order `α`,
with homomorphisms `π a : G a → K a` natural in `a` (`h_nat`). Suppose that every nonempty directed
subset of `α` has a cocone in `α` that both `G` and `K` send to filtered colimits in the elementwise
sense, where every element of the vertex comes from some stage and an element vanishing in the
vertex already vanishes at a later stage (`h_colim`). If every `y ∈ K a` whose images in `K b` lift
along `π b` for all `b > a` itself lifts along `π a` (`h_step`), then `π a` is surjective. 

### `IsZeroLocusFamily`

 The subfunctors `U a ⊆ Y`, for ideals `a` of `R`, behave like the zero loci `V(a)` of the
ideals in `Spec R`. 

### `IsZeroLocusFamily.isRelAffine`

 Each inclusion `U a ⊆ Y` is relatively affine. 

### `IsZeroLocusFamily.mem_sSup_iff`

 The zero locus of a sum of ideals is the intersection of their zero loci. 

### `IsZeroLocusFamily.subsingleton_of_mem_top`

 The zero locus of the unit ideal has points only over the zero ring. 

### `mem_bot`

 Every point lies in the zero locus of the zero ideal. 

### `mem_sup_iff`

 The zero locus of `a ⊔ b` is the intersection of the zero loci of `a` and `b`. 

### `antitone`

 Larger ideals have smaller zero loci. 

### `antitone_preimage`

 The preimages of the zero loci under `p : Z ⟶ Y` also shrink as the ideal grows. 

### `subsingleton_of_mem_span_of_mem_span_one_sub`

 The zero loci of `(e)` and `(1 - e)` meet only over the zero ring. 

### `isZeroLocusFamily_zeroPoints`

 Let `s : X ⟶ reprBy S` be a map to the functor `h_S` represented by the ring `S`. The
subfunctors `zeroPoints s J` of points whose ring map `S → A` kills the ideal `J` form a family
of zero loci (`New.Variety.IsZeroLocusFamily`). 

### `bijective_prod_map_sup_span_of_isCohomDense`

 Mayer–Vietoris for the two pieces that an element `e` cuts out of a zero locus `U a`, pulled
back along `p : Z ⟶ Y`. If `U (e) ⊔ U (1 - e)` is dense in `Y` on test rings, then the restriction
`Hⁿ(U a) → Hⁿ(U (a ⊔ (e))) × Hⁿ(U (a ⊔ (1 - e)))` of the preimages is bijective: the union of the
two pieces is dense in `U a`, and they meet only over the zero ring. 

### `bijective_map_fromPreimage_or_exists_isIdempotentElem`

 Over a zero locus `U a`, either the pull-back `Hⁿ(U a) → Hⁿ(u⁻¹(U a))` along `u : X ⟶ Y` is
bijective, or an idempotent `e` splits `a`: neither `e` nor `1 - e` lies in `a`. The first case
holds for `a = ⊤`, where both groups vanish, and, by `h_conn`, for proper `a` that no idempotent
splits. 

### `IsTestCohomEquiv.of_connected`

 Local-to-global principle. Let `X`, `Y` have continuous cohomology with coefficients `Λ`
(`IsCohomContinuous`), and let the `U a ⊆ Y`, `a` an ideal of `R`, be zero loci
(`IsZeroLocusFamily`). Assume that for every idempotent `e`, `U (e) ⊔ U (1 - e)` is dense for
locally constant `Λ`-coefficients (`IsCohomDense`): for each point `h_A → Y` with `A` a test ring
(`testIncl`), the inclusion of its preimage in `h_A` is a cohomology equivalence. If `u : X ⟶ Y`
induces isomorphisms on cohomology (`IsTestCohomEquiv`) over `U a` for each proper ideal `a`
containing `e` or `1 - e` for every idempotent `e` (each connected piece), then so does `u`. 


## Density criteria tested on points in valuation rings

Each local ring of a test ring is a valuation ring of an algebraically closed field
(`New.Variety.IsTest.exists_valuationSubring_atPrime`). This is why it suffices to test the
criteria on points in such valuation rings.


### `IsRelAffine.hasCohomDenseImage_of_lifts`

 Let `p : X ⟶ Y` be a map of functors on rings that is relatively representable (`IsRelAffine`:
its pull-back along every point `reprBy A ⟶ Y` is representable). Suppose that `p` is onto on
`O`-points for every valuation subring `O` of every algebraically closed field. Then the image of
`p`, restricted to test rings, is cohomologically dense in `Y` (`HasCohomDenseImage`) for the
coefficients sending `A` to the locally constant functions `Spec A → Λ`: over every point
`reprBy A ⟶ Y`, the inclusion of the preimage of the image into `reprBy A` is an equivalence for
these coefficients. 

### `IsCohomDense.of_affine_cover`

 Let `V i`, for `i` in a finite type `J`, be subfunctors of a functor `Y` on rings whose
inclusions are relatively representable, and let `U` be a subfunctor of the restriction
`testIncl ⋙ Y` of `Y` to test rings. Suppose that every point of `Y` in a valuation ring of an
algebraically closed field lies in some `V i` whose restriction to test rings is contained in `U`.
Then `U` is dense (`IsCohomDense`) for `locConstCoeff Λ` (`A ↦` locally constant functions
`Spec A → Λ`): for every point `reprBy A ⟶ Y` with `A` a test ring, the inclusion of the preimage of
`U` into `reprBy A` is an equivalence for these coefficients. 


## Proper functors on rings: base change, dense images, continuity

Formal properties of proper functors on rings. `New.Variety.IsProperOver s`, for `s : Z ⟶ reprBy D`,
says that equality of two points is cut out by an ideal (`diagonal_closed`), and that one point of
`Z` specialises to every geometric point whose structure map lands in a valuation ring, through that
ring (`valuative_cover`).


### `isRelAffine_pointMap`

 Let `Z` be proper over `D` and `y ∈ Z(T)` a point. The map `reprBy T ⟶ Z` given by `y` is
relatively representable (`IsRelAffine`): its pull-back along every point `reprBy A ⟶ Z` is
representable. 

### `of_isPullback`

 Let `V` be the fibre product of `u : Z ⟶ W` and `p : Y ⟶ W`, with projections `q : V ⟶ Z` and
`v : V ⟶ Y`. Let `Z` be proper over `D` (through `s`), `W` proper over `T` (through `b`) and `Y`
proper over `T` (through `p ≫ b`). If `u` is compatible with the structure maps along a ring map
`ψ : T ⟶ D`, then `V` is proper over `D` (through `q ≫ s`). 

### `_root_.New.Variety.isProperOver_id_reprBy`

 The functor represented by a ring `R` is proper over `R`, through the identity map. 

### `baseChange`

 The base change of a proper functor along a ring map `φ : D ⟶ T` is proper over `T`. 

### `hasCohomDenseImage_of_surjective`

 Let `c : Y ⟶ Z` be a map over `D`, with `Y` and `Z` proper over `D`, that is onto on points in
every algebraically closed field. Then `c` has dense image, for locally constant `Λ`-valued
coefficients. 

### `exists_valuativeLift_hasCohomDenseImage`

 Let `Z` be proper over `D` via `s`. Then there are a ring `P`, a point `ξ ∈ Z(P)` and a
valuative lift `z` of `ξ`, meaning a point of `Z` over the product of the valuation rings of all
places of `P` (a place is a prime of `P` with a valuation ring of its residue field containing the
image of `D` under `baseRingMap s ξ`) that agrees with `ξ` over the product of their residue fields.
For these, `placeSpaceMap z` has cohomologically dense image (`HasCohomDenseImage`) for the
coefficients sending `A` to the locally constant functions `Spec A → Λ`; this is the map to `Z` from
the space of places of `z`, sending the class of `f` to `f z`, and dense image means that its image,
restricted to test rings, is dense in `Z`. 

### `isCohomContinuous`

 A functor of points that is proper over `D` has the continuity property `IsCohomContinuous`
for filtered limits, with locally constant `Λ`-valued coefficients. 

 ## Density of subfunctors holding the points that keep the coincidences at a geometric point 

### `New.Variety.IsProperOver.isCohomDense_of_coincidences`

 Let `Z` be proper over `D` via `s` (`IsProperOver`: closed diagonal plus a uniform valuative
criterion), let `P i : Y ⟶ Z` be finitely many maps, and let `U` be a subfunctor of `Y` restricted
to test rings (`TestRing`, via `testIncl`). Suppose that for every point `z` of `Y` over an
algebraically closed field, `U` contains every point `x` of `Y` over a test ring that keeps the
coincidences of `z`: whenever `P i` and `P j` agree at `z` they agree at `x`. Then `U` is dense
(`IsCohomDense`) for the coefficients `locConstCoeff Λ` (A ↦ locally constant functions Spec A → Λ):
for every point h_A → Y, the inclusion of the preimage of `U` into h_A induces bijections on all
`Ext^n(−, locConstCoeff Λ)`. 

 ## Transfer for Galois coverings 

### `New.Variety.IsGaloisCovering.hasCohomDenseImage_geomPoints`

 Let `c : W ⟶ Y` be a Galois covering of proper `R`-schemes (`IsGaloisCovering`: `Δ` acts on `W`
over `Y` through `a`, `c` is onto, and `Δ` acts simply transitively on fibres over fields of
characteristic zero), and `Ω` the fixed algebraic closure of `ℚ` as an `R`-algebra. After base
change to `Ω` (`geomPoints`), `c` has dense image for locally constant `Λ`-valued coefficients. 

### `New.Variety.IsGaloisCovering.isCohomDense_permutedPairs`

 Let `c : W ⟶ Y` be a Galois covering of `R`-schemes with finite group `Δ` and `W` proper. After
base change to `Ω` (`geomPoints`), the pairs in `W ×_Y W` whose `Δ`-orbits agree up to a permutation
of `Δ` (`permutedPairs`) are dense, for locally constant `Λ`-valued coefficients. 

### `New.Variety.ellAdicCohom.transfer`

 Let `c : W ⟶ Y` be a Galois covering of proper `R`-schemes with finite group `Δ` acting through
`a` (`IsGaloisCovering`: `Δ` acts over `Y`, `c` is onto, and `Δ` acts simply transitively on the
fibres over fields of characteristic zero), `Ω` the fixed algebraic closure of `ℚ` as an `R`-algebra
and `ℓ` a prime. Then pull-back along `c` on `ℓ`-adic cohomology `ellAdicCohom R Ω n` is (a)
injective, and (b) every class on `W` fixed by `Δ` lies in its image. 
