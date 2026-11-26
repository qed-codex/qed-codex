---
{
  "module": "src/Lib/Cohomology/Etale/BijectiveComparisons.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Cohomology/Etale/BijectiveComparisons.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Cohomology/Etale/BijectiveComparisons.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Criteria for comparison maps of Ext cohomology of functors of points to be bijective

For a set-valued functor of points `Y` on a category `C` with coefficients `F`, cohomology is
`Hⁿ(Y, F) = New.Variety.H (freeAb.obj Y) F n`, an `Ext` group in functors to abelian groups, where
`ℤ[Y]` is the free abelian functor on `Y`; `reprBy A` is the functor `B ↦ (A ⟶ B)` (lifted), and a
point `y` of `Y A` gives `pointMap y : reprBy A ⟶ Y`, `f ↦ Y.map f y`. A comparison `c = (φ, β)`
with `φ : C' ⥤ C` and `β : φ ⋙ F ⟶ F'`, together with a map `u : Y' ⟶ φ ⋙ Y`, gives maps
`c.pull (freeAbMap u) n : Hⁿ(Y, F) → Hⁿ(Y', F')`. The file gives criteria for these maps to be
bijective. The tools are dévissage and Čech descent along covers, and pointwise descriptions of
bijections and pull-back squares. The file also builds cocycle classes from witnesses of a relation
`R ⊆ V × L`, relative to a subfunctor `U ⊆ V`, by a Čech-type complex.

## Main definitions and results

* `New.Variety.witnessed.universalClass`, `New.Variety.witnessed.cocycleClass`: splicing the short
  exact sequences into which the complex of points with witnesses splits gives a universal class;
  its push-forward along a cocycle with values in `F` is a class in `Extⁿ(ℤ[V]/ℤ[U], F)`.
* `New.Variety.cech_descent_step`, `New.Variety.Devissage.allBijective_freeAb_range_of_cech`: Čech
  descent of bijectivity from `E` and its fibre powers `New.Variety.cech p m` to the image of
  `p : E ⟶ Y`.
* `New.Variety.IsCover`: `p` is a cover for `F`, that is, the inclusion of its image induces
  bijections on all `Extⁿ(ℤ[-], F)`; pointwise surjections are covers
  (`New.Variety.IsPointwiseSurjective.isCover`).
* `New.Variety.Comparison.IsBijective`: for a natural map `α : N' ⟶ c.functor ⋙ N`, the maps
  `c.pull α n : Extⁿ(N, F) → Extⁿ(N', F')` are bijective in all degrees; for `α = freeAbMap u` these
  are the maps `Hⁿ(Y, F) → Hⁿ(Y', F')`.
* `New.Variety.Comparison.isBijective_of_fibres`: it is enough to test on the fibres over the points
  of `Y`; the proof is Čech descent (`New.Variety.Comparison.bijectiveUpTo_of_cech_pred`), one
  condition of `New.Variety.BijectiveUpTo` at a time.
* `New.Variety.Comparison.HasUniversalPoints.isBijective`: representable fibres with equal
  coefficients (`New.Variety.Comparison.IsUnivPoint`) suffice;
  `New.Variety.Comparison.isBijective_of_adj` is the case of an adjunction.

Notions from other files:
* `New.Variety.H`: The group Ext^n(N,F) in the category of functors from C to abelian groups;
  `H.map F α n` is the pull-back along α: N' → N and `H.push N β n` the push-forward along β:
  F → F'.
* `New.Variety.Comparison`: A comparison from F on C to F' on C' is a functor φ: C' → C with a map
  β: F∘φ → F'. For α: N' → N∘φ, `Comparison.pull` is the map Ext^n(N,F) → Ext^n(N',F') that
  restricts along φ, pushes by β and pulls by α.
* `New.Variety.BijectiveUpTo`: For maps f_n: A_n → B_n, the first r of the conditions: f₀ injective,
  f₀ surjective, f₁ injective, f₁ surjective, and so on.
* `New.Variety.IsCohomEquiv`: α: N' → N is an equivalence for F: the pull-back
  Ext^n(N,F) → Ext^n(N',F) is bijective for every n.
* `New.Variety.freeAbMap`: For u: Y' → Y∘φ, the induced map of free abelian group functors
  Z[Y'] → Z[Y]∘φ.

## Relation to the literature

Known; see `Lib.Cohomology.Hodge.FixedPointFormula` and `Lib.Cohomology.Etale.FilteredLimits` for
sources.



## Witnesses, a Čech-type resolution and the universal cocycle class

Cohomology classes from witnesses. A relation `R ⊆ V × L` between functors of points gives each
point `x` of `V` a set of witnesses `l`. A subfunctor `U ⊆ V` consists of points that have one. The
chains on tuples `(x, l₁, …, lₘ)` form a Čech-type complex, exact in positive degrees.


 ### The complex of points with witnesses 

### `witnessed`

 The functor of points with `m` witnesses: a point `x` of `V` together with `m` points `l i`
of `L` such that each pair `(x, l i)` lies in `R`. 

### `reindexWitness`

 Reindexing the witnesses of a point along `g`: the `i`-th new witness is the `g i`-th old
one. 

### `boundary`

 The boundary map from chains with `m + 1` witnesses to chains with `m` witnesses: the
alternating sum of the maps that drop one witness. 

### `boundary_comp_boundary`

 The boundary of a boundary is zero. 

### `boundaryFromCoker`

 The map induced by the boundary, from the chains with `m + 1` witnesses modulo boundaries to
the chains with `m` witnesses. 

### `noWitness`

 The natural isomorphism from points with `0` witnesses to points of `V` that forgets the empty
tuple of witnesses. 

### `proj_boundary_of_eq_zero`

 A point of `V` that has a witness is a boundary, as a chain without witnesses. 

### `shortExact_boundaryFromCoker`

 With `Cₘ` the chains on points with `m` witnesses, the sequence
`0 → Cₘ₊₁/∂Cₘ₊₂ → Cₘ → Cₘ/∂Cₘ₊₁ → 0` is short exact. 

 ### The class of a cocycle 

### `fromRel`

 The map `x ↦ [x]` from `ℤ[V]/ℤ[U]` to the chains without witnesses modulo boundaries. It is
well defined because every point of `U` has a witness. 

### `universalClass`

 The universal class in degree `n`, with coefficients in the chains with `n` witnesses modulo
boundaries. In degree `0` it is the map `fromRel hU`; each further degree composes with the
extension class of the short exact sequence `shortExact_boundaryFromCoker`. 

### `cocycleClass`

 The class of a cocycle. A cocycle of degree `n` is a map `y` to `F` from the chains with `n`
witnesses modulo boundaries. Its class in `Extⁿ(ℤ[V]/ℤ[U], F)` is the push-forward of
`universalClass hU n` along `y`. 

 ### Naturality 

### `exists_map_extClass_comp`

 Let `γ` and `y` be compatible maps between the last two terms of short exact sequences `S`
and `T`, let `β : T.X₁ ⟶ F`, and let `x` be a class in `Extⁿ(N, S.X₃)`. Then there is a map
`z : S.X₁ ⟶ F` with `z s = β t` whenever `t` and `s` have the same image in `T.X₂`, and the
product of `y_* x` with `β_* [T]` equals `z_*` of the product of `x` with `[S]`. Here `[S]` and
`[T]` are the extension classes. 

### `map_cocycleClass`

 Classes of cocycles are carried along an exact functor `Φ`. Let the maps `q m` send chains
with `m` witnesses for `R'` to the image under `Φ` of the chains with `m` witnesses for `R`,
compatibly with reindexing and, in degree `0`, with `α`. Then a cocycle `y` for `R` induces a
cocycle `y'` for `R'`, and the class of `y`, moved along `Φ`, `β` and `α`, is the class of `y'`. 

### `pull_cocycleClass`

 Pull-back of the class of a cocycle along a comparison `c`. Let `u` map points and `v` map
witnesses so that the relation `R'` goes to `R`, and let `α` be induced by `u`. If the cocycle
`y'` is `y` read through `u` and `v` and followed by the coefficient map of `c`, then the class of
`y` pulls back to the class of `y'`. 


## Closed classes, dévissage, Čech descent and covers

* `New.Variety.IsClosedClass`: the class P of functors D → Ab contains 0 and, along a short exact
  sequence whose subobject is in P, contains the middle term exactly when it contains the quotient.
* `New.Variety.Devissage`: the five and four lemmas for a family of maps f_{N,n};
  `New.Variety.Comparison.devissage` shows that comparison maps of Ext groups have them.

`New.Variety.cech p m` is the (m+1)-fold fibre power of `E` over `Y`.


 ### Closed classes 

### `IsClosedClass`

 A closed class P of functors D → Ab: (a) P contains every zero functor N (written `𝟙 N = 0`);
(b) for a short exact sequence 0 → X₁ → X₂ → X₃ → 0 with X₁ in P, the middle term X₂ is in P exactly
when the quotient X₃ is. Nothing is asked about X₁ when X₂ and X₃ are in P. 

### `IsClosedClass.iff_of_isIso`

 A closed class P is invariant under isomorphism: for an isomorphism g : M → N, P holds for M
exactly when it holds for N. Proof: apply (b) to 0 → ker g → M → N → 0, whose kernel is zero. 

### `H.subsingleton_of_id_eq_zero`

 If N is a zero object (its identity is zero), then every group Extⁿ(N, F) has at most one
element. 

### `StepwiseFourLemma`

 The stepwise four lemma for the family f: along every short exact sequence 0 → X₁ → X₂ → X₃ → 0,
the first r conditions of `New.Variety.BijectiveUpTo` at X₂ and the first r − 1 at X₁ give the first
r at X₃. 

### `StepwiseFourLemma.bijectiveUpTo_quotient`

 The first r conditions at X₂ and the first r − 1 at X₁ give the first r at X₃. 

 ### Dévissage 

### `Devissage`

 The five and four lemmas for a family of maps f_{N,n} : A N n → B N n, indexed by functors N :
D → Ab and degrees n, as for a map of contravariant δ-functors. In `bijectiveUpTo_quotient`, `r - 1`
is subtraction of natural numbers; for r = 0 there is no condition. 

### `Devissage.isClosedClass`

 Five lemma: the functors on which `f` is bijective in all degrees form a closed class. 

### `Comparison.devissage`

 For a comparison (φ,β) from F to F', exact functors Φ, Φ' and a natural map η: Φ'N → (ΦN)∘φ,
the induced maps Ext^n(ΦN,F) → Ext^n(Φ'N,F') have the five- and four-lemma properties
`New.Variety.Devissage`. 

### `instance : IsIso (proj p 0 0)`

 The projection from the one-fold fibre power `cech p 0` to E is an isomorphism. 

### `cech_descent_step`

 Čech descent, for a family of maps f_{N,n} : A N n → B N n indexed by functors N : D → Ab and
degrees n. Suppose that, in short exact sequences, r conditions of
`New.Variety.BijectiveUpTo` on the middle term and r − 1 on the kernel give r on the quotient. Then
r on Z[E] and r − 1 on all fibre powers of p give r on Z[im p]. 

### `Devissage.allBijective_freeAb_range_of_cech`

 Čech descent: if the maps f obey the five and four lemmas (`New.Variety.Devissage`) and are
bijective in all degrees on ℤ[-] of every fibre power of p: E → Y, E included, then they are so
on ℤ[im p]. 

### `IsCover`

 p: E → Y is a cover for F: the inclusion of the image of p in Y induces bijections on
Ext^n(Z[−],F) for all n. 


## Pointwise bijections and pull-back squares of set-valued functors

* `New.Variety.IsCohomEquiv.of_bijective`: a map that is bijective at every object induces
  bijections on all `Extⁿ(ℤ[-], F)`.
* `New.Variety.isPullback_iff`: a square is a pull-back exactly when it commutes and is a pull-back
  of sets at every object; fibre products and fibre powers give such squares.


### `IsCohomEquiv.of_bijective`

 A map `p : E ⟶ Y` that is bijective at every object is an isomorphism, so `ℤ[E] ⟶ ℤ[Y]` is an
equivalence for every coefficient functor `F`. 

### `isPullback_iff`

 A square of functors is a pull-back if and only if it commutes and is a pull-back on points at
every object. 

### `isPullback_fibreProd`

 The fibre product of `u : W ⟶ Y` and `p : E ⟶ Y` with its two projections is a pull-back
square. 

### `isPullback_cech`

 The fibre power with `m + 2` factors is the pull-back of `p` along the fibre power with `m + 1`
factors, by the first coordinate `proj p (m + 1) 0` (`proj p m i` is the `i`-th coordinate map of
`cech p m` to `E`) and the map that drops the first coordinate: a tuple is its first coordinate
together with the remaining ones. 

 ## Bijective comparisons: representable case, fibres, universal points 

 ### Bijective comparisons and representable functors 

### `Comparison.IsBijective`

 For a comparison (φ,β) from F to F' and α: N' → N∘φ, the property that Ext^n(N,F) →
Ext^n(N',F') is bijective for every n. 

### `isCohomEquiv_iff_isBijective`

 A map α: N → G of functors from C to abelian groups is an equivalence for F if and only if
the identity comparison from F to itself is bijective along α in every degree. 

### `projective_and_eval_bijective`

 If `Y` is represented by `B` through the point `z`, then `freeAb.obj Y` is projective and
maps from it to `F` are determined bijectively by the image of `z` in `F.obj B`. 

### `pointMap_id_bijective_of_fullyFaithful`

 For a fully faithful functor `ψ : C ⥤ C'` and an object `c`, the functor
`d ↦ (ψ c ⟶ ψ d)` is represented by `c` through the identity of `ψ c`: the point map of the
identity is bijective at every object. 

### `homOfValue`

 For `u : Y' ⟶ c.functor ⋙ reprBy A`, which sends a point `y` of `Y' B` to a map
`A ⟶ c.functor B`, the homomorphism `F A → (ℤ[Y'] ⟶ F')` that sends `x` (via the Yoneda bijection
`homReprEquiv A F : (ℤ[reprBy A] ⟶ F) ≃ F A`) to the section taking `y` to
`c.coeffHom B (F.map (u y) x)`. 

### `IsBijective.trans_iff`

 Let c, c' be comparisons from F to F' and F' to F'', with c' bijective in all degrees along α'.
Then c is bijective along α exactly if the composite comparison is bijective along γ, the composite
of α' with α whiskered by `c'.functor`. 

### `IsBijective.trans`

 Bijective comparisons compose: if `c` is bijective along `α` and `c'` along `α'`, the composite
comparison is bijective along the composite `γ` of `α'` with `α` whiskered by `c'.functor`. 

### `isBijective_iff_of_coeff_iso`

 Let `γ : F ⟶ G` and `γ' : F' ⟶ G'` be isomorphisms of coefficient functors. Let
`β : c.functor ⋙ G ⟶ G'` satisfy `β ∘ γ = γ' ∘ c.coeffHom`. Then `c` is bijective along `α` in all
degrees if and only if the comparison `(c.functor, β)` from `G` to `G'` is. 

### `isBijective_reprBy_iff`

 For `u : Y' ⟶ c.functor ⋙ reprBy A`, the comparison `Hⁿ(ℤ[reprBy A], F) → Hⁿ(ℤ[Y'], F')` is
bijective for all `n` if and only if `c.homOfValue u : F A → (ℤ[Y'] ⟶ F')` is bijective and
`Hⁿ(ℤ[Y'], F') = 0` for all `n ≥ 1`. 

### `isBijective_of_repr`

 Let `Y'` be represented by `B` through the point `z`, and let `u z : A ⟶ φ B` (the map under
`ULift`). If `c.coeffHom B ∘ F.map (u z) : F A → F' B` is bijective, the comparison along `u` is
bijective in all degrees. 

### `IsBijective.precomp_of_bijective`

 If the comparison is bijective along `u` and `p' : E' ⟶ Y'` is bijective at every object,
then it is bijective along `v = p' ≫ u`. 

 ### Descent: covers and fibres 

### `bijectiveUpTo_of_cech_pred`

 The Čech step. Let `p : E ⟶ Y` and `p' : E' ⟶ Y'` be covers for `F` and `F'`, and let
`v : E' ⟶ c.functor ⋙ E` lift `u : Y' ⟶ c.functor ⋙ Y` to them (`w : p' ≫ u = v ≫ p`). Suppose that
(a) the comparison along `v` is bijective in all degrees and (b) on every fibre power `cech p m`
(`m + 1` factors) the comparison along the map `cech p' m ⟶ c.functor ⋙ cech p m` induced by
`(v, u)` satisfies the first `r - 1` conditions of `New.Variety.BijectiveUpTo`. Then the comparison
along `u` satisfies the first `r`. 

### `isBijective_of_fibres`

 Let `u : Y' ⟶ c.functor ⋙ Y` and `t : E ⟶ Y`, and let `v : E' ⟶ c.functor ⋙ E`, with
`p' : E' ⟶ Y'`, be the pull-back of `u` along `t`. Suppose that for every point `x` of `E A` the
comparison is bijective in all degrees along the projection to `c.functor ⋙ reprBy A` of the fibre
product of `u` with the point `reprBy A ⟶ Y` given by `t x`. Then it is bijective along `v`. 

 ### Universal points 

### `IsUnivPoint`

 Let `u : Y' ⟶ c.functor ⋙ Y` and let `y` be a point of `Y A`. A pair `(z, f)` of a point `z` of
`Y' D` and a map `f : A ⟶ c.functor D` lies over `y` if `u z = f y`. The pair `(x, s)` over `B` is a
universal point if it is universal among these pairs, so that `B` represents the fibre of `u` over
`y`, and the coefficients `F A` and `F' B` agree along `s`. 

### `IsUnivPoint.apply_eq_map`

 The pair `(x, s)` lies over `y`. 

### `IsUnivPoint.existsUnique_hom`

 Every pair `(z, f)` that lies over `y` comes from `(x, s)` by exactly one map `g`. 

### `IsUnivPoint.coeff_bijective`

 The map `F A → F (c.functor B) → F' B` on coefficients is bijective. 

### `HasUniversalPoints`

 The map `u : Y' ⟶ c.functor ⋙ Y` has universal points: over every point of `Y` there is a
universal point (`New.Variety.Comparison.IsUnivPoint`), at which the coefficients agree. 

### `HasUniversalPoints.isBijective_of_isPullback`

 If u: Y' → Y∘φ has universal points (`New.Variety.Comparison.HasUniversalPoints`), then for
every t: E → Y the comparison is bijective in all degrees along the pull-back v: E' → E∘φ of u along
t, with p': E' → Y'. Indeed, for every point y of E the fibre of v over y is the fibre of u over
t y, which is represented by a universal point over t y. 

### `HasUniversalPoints.isBijective`

 If there are universal points on which the coefficients agree, the comparison along `u` is
bijective in all degrees. 

### `HasUniversalPoints.isBijective_subfunctor`

 If the comparison c has universal points for u: Y' → Y∘φ
(`New.Variety.Comparison.HasUniversalPoints`), then for every subfunctor U of Y the comparison is
bijective in all degrees along the restricted map u⁻¹(U∘φ) → U∘φ. 

### `HasUniversalPoints.isCohomEquiv_incl_iff`

 With universal points, a subfunctor `U` of `Y` has the cohomology of `Y` for `F` if and only
if its preimage `S` in `Y'` has the cohomology of `Y'` for `F'`. 

### `isBijective_of_adj`

 For an adjunction `φ ⊣ U`, restriction along `U` followed by the counit identifies the
cohomology of `Y'` with coefficients `φ ⋙ F` and that of `U ⋙ Y'` with coefficients `F`. 

### `bijectiveUpTo_congr`

 If `p` and `p'` are equivalences for `F` and `F'` and `v` lifts `u` along them
(`w : p' ≫ u = v ≫ p`), the comparisons along `u` and along `v` satisfy the same conditions of
`New.Variety.BijectiveUpTo`. 

### `isBijective_congr`

 If `p` and `p'` are equivalences for `F` and `F'` and `v` lifts `u` along them
(`w : p' ≫ u = v ≫ p`), the comparison is bijective along `u` if and only if it is along `v`. 
