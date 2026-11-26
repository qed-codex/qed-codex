---
{
  "module": "src/Lib/Cohomology/Etale/FilteredLimits.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Cohomology/Etale/FilteredLimits.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Cohomology/Etale/FilteredLimits.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Continuity of cohomology along filtered limits, via test rings and relatively affine maps

The cohomology of a set-valued functor `Y` on rings is Hⁿ(Y) = Extⁿ(ℤ[Y], F). Here ℤ[Y] is the free
abelian group functor, and h_A = Hom(A, −) is the functor represented by `A`. The question is when
Hⁿ turns a cofiltered limit of functors into a filtered colimit of groups. Cohomology is computed on
test rings, with coefficients the locally constant functions to an abelian group Λ. Test rings have
no higher cohomology, and their cohomology commutes with filtered colimits. Relatively affine maps
are maps whose pull-backs to representable functors are representable.

## Main definitions and results

* `New.Variety.ContinuousUpTo`: for a cone `c` over a cofiltered diagram `D` of set-valued functors,
  the maps colim_j Hⁿ(D j) → Hⁿ(c.pt) satisfy the first `r` conditions of
  `New.Variety.BijectiveUpTo`.
* `New.Variety.ContinuousUpTo.of_cech`: the property descends along covers, by
  `New.Variety.cech_descent_step`.
* `New.Variety.continuousUpTo_locConstCoeff`: the cohomology of test rings, with locally constant
  coefficients, commutes with filtered colimits.
* `New.Variety.Envelope.exists_natTrans_isTest_and_factors`: a functorial map θ : A → E(A) to a test
  ring through which, for A in a given family, every map to a test ring factors.
* `New.Variety.IsCohomContinuous`: continuity over X, for coefficients Λ. On a filtered inverse
  system of functors affine over X, the cohomology of the limit is the colimit of the cohomologies.
  `New.Variety.IsCohomContinuous.of_isRelAffine` passes it to functors affine over X.
* `New.Variety.IsCohomContinuous.of_hasCohomDenseImage`: continuity holds over Y if a representable
  functor h_T maps to Y by a map that is affine and has dense image.

Notions from other files:
* `New.Variety.IsTest`: A is a test ring: reduced, absolutely integrally closed, and any a, b admit
  an idempotent e with a ∣ eb and b ∣ (1 − e)a. `New.Variety.TestRing` is their category.
* `New.Variety.IsCover`: p: E → Y is a cover for F: the inclusion of the image of p in Y induces
  bijections on Ext^n(Z[−],F) for all n.
* `New.Variety.locConstCoeff`: For an abelian group Λ, the coefficient functor on test rings sending
  A to the group of locally constant functions Spec A → Λ.
* `New.Variety.BijectiveUpTo`: for maps f_n : A_n → B_n, the first r of the conditions f₀
  injective, f₀ surjective, f₁ injective, f₁ surjective, and so on.

## Relation to the literature

Known result: Descent of torsion étale cohomology along v-covers, with excision, transfer and
limits. Here cohomology is defined as Ext of presheaves on test rings. The local rings of a test
ring are valuation rings of algebraically closed fields. Descent, excision, transfer and limits are
proved from this definition, while equality with étale cohomology is neither proved nor used.
Source: Scholze, Berkovich Motives, arXiv 2412.03382 (2024), Thm 4.1 and Lemmas 4.7, 4.8 (descent
and limits from finitary functors on test rings); Bhatt, Mathew, The arc-topology, Duke Math. J. 170
(2021), Prop 5.2, Thm 5.4; Stacks project, Tag 09YQ; Scholze, Étale cohomology of diamonds,
7.15-7.16.

See also `Lib.Cohomology.ProperBaseChange.Theorem`.



## The colimit condition for cohomology along cofiltered systems

* `New.Variety.IsFilteredColimit`: a cocone of abelian groups is a filtered colimit, stated on
  elements; by `New.Variety.isFilteredColimit_iff_bijective` this holds exactly when the map from
  the colimit to the vertex is bijective.
* `New.Variety.ContinuousUpTo` and `New.Variety.ContinuousUpTo.of_cech`: continuity of
  cohomology up to a level, and its descent along covers.


### `IsFilteredColimit`

 A cocone of abelian groups is a filtered colimit elementwise: an element mapping to 0 in the
vertex dies at a later stage, and every element of the vertex comes from some stage. 

### `cohomologyFunctor`

 The contravariant functor sending Φ: T → (functors from C to abelian groups) to the
contravariant functor t ↦ Ext^n(Φ(t),F) from T to abelian groups. For Φ = `freeAb` its value
`(cohomologyFunctor F n).obj ⟨freeAb⟩` is Y ↦ Hⁿ(Y) = Ext^n(ℤ[Y],F). 

### `ContinuousUpTo`

 Continuity of cohomology up to a level. For a cone `c` over a cofiltered system `D j` of
set-valued functors, `ContinuousUpTo F c : ℕ → Prop` is a predicate on the level `r`:
`ContinuousUpTo F c r` says that the canonical maps colim_j Extⁿ(ℤ[D j], F) → Extⁿ(ℤ[c.pt], F)
satisfy the first `r` of the conditions of `New.Variety.BijectiveUpTo` (injective in degree 0,
surjective in degree 0, injective in degree 1, …). 

### `isFilteredColimit_iff_bijective`

 A cocone `c` of abelian groups over a filtered diagram `X` is a filtered colimit in the sense of
`New.Variety.IsFilteredColimit` if and only if the canonical map from the colimit of `X` to the
vertex of `c` is bijective. 

### `ContinuousUpTo.of_cech`

 Cover lemma for continuity. Let `a` be a cone over a cofiltered system `A` of maps `E j ⟶ Y j`
of set-valued functors, each a cover for the coefficients `F` (`hp`), whose vertex `E ⟶ Y` is a
cover too (`hq`). If `New.Variety.ContinuousUpTo` holds at level `r` for the sources `E j`
(`leftFunc`) and at level `r - 1` for each of their fibre powers over the `Y j` (`cechFunctor m`),
then it holds at level `r` for the targets `Y j` (`rightFunc`). For a cone over a system `X j`,
level `r` means that the maps colim_j Extⁿ(ℤ[X j], F) → Extⁿ(ℤ[vertex], F) meet the first `r`
conditions: injective in degree 0, surjective in degree 0, injective in degree 1, and so on. 


## Acyclicity of test rings and filtered colimits of test rings

* `New.Variety.isFilteredColimit_locConstSpec`: locally constant functions on the spectrum commute
  with filtered colimits of rings.
* `New.Variety.IsAcyclicOver.of_bijective`: `q : T ⟶ testIncl ⋙ reprBy B` is acyclic over `B` if `B`
  is a test ring and `q` is bijective on points.
* `New.Variety.IsTest.filtered_colimit`: a filtered colimit of test rings is a test ring.


### `isFilteredColimit_locConstSpec`

 Locally constant `Λ`-valued functions on the prime spectrum commute with filtered colimits of
rings: if the cocone `c` of rings over `L` is a colimit on elements (every element of `c.pt` comes
from some stage, `h_surj`; an element killed in `c.pt` is killed at a later stage, `h_zero`), then
a function vanishing on the spectrum of `c.pt` vanishes at a later stage, and every function on it
comes from some stage. 

### `locConstClass`

 For q: T → h_B on test rings, the map from locally constant functions Spec B → Λ to
Hⁿ(T, Λ): pull-back along q for n = 0, zero for n > 0. 

### `IsAcyclicOver`

 Property of q: T → h_B on tests: pull-back of locally constant functions Spec B → Λ is a
bijection onto H⁰(T, Λ), and Hⁿ(T, Λ) = 0 for n > 0 (there `locConstClass` is zero and onto). 

### `map_locConstClass`

 Naturality of `New.Variety.locConstClass`. Let `q : T ⟶ h_B`, `q' : T' ⟶ h_B'` and `e : T' ⟶ T`.
If `f` on `Spec B` and `f'` on `Spec B'` have the same pull-back at every point `x` of `T'` (along
`q (e x)` and `q' x`), then `e` pulls the class of `f` back to the class of `f'`. 

### `bijective_const_of_isDomain`

 On the spectrum of a domain, the locally constant `Λ`-valued functions are the constants. 

### `IsAcyclicOver.isCohomEquiv`

 If `T` over the domain `B` and `T'` over the domain `B'` both satisfy
`New.Variety.IsAcyclicOver`, then every map `u : T' ⟶ T` induces bijections on cohomology: both have
`H⁰ = Λ` and no higher groups. No compatibility of `u` with the maps to `h_B` and `h_B'` is
needed. 

### `IsTest.filtered_colimit`

 A filtered colimit of test rings, taken in commutative rings, is a test ring: absolutely
integrally closed, comparable for divisibility after splitting by an idempotent, and reduced. 

### `IsAcyclicOver.of_bijective`

 If B is a test ring and q : T → h_B is bijective on points in every test ring, then H⁰(T, Λ)
is, via q, the group of locally constant functions Spec B → Λ, and Hⁿ(T, Λ) = 0 for n > 0. 

### `onTests`

 The functor restricting a set-valued functor on commutative rings to the full subcategory of
test rings, by precomposition with the inclusion. 

### `continuousUpTo_locConstCoeff`

 Let `L` be a filtered diagram of test rings A_j, and A its colimit as a ring (a test ring by
`New.Variety.IsTest.filtered_colimit`). Then the Λ-cohomology Hⁿ(h_A) on test rings is the colimit
of the Hⁿ(h_{A_j}), for every n: `New.Variety.ContinuousUpTo` holds at every level `r` for the
cone of the functors h_{A_j} restricted to test rings. 


## A functorial test-ring envelope

There are too many test rings to take the product of all of them, so the maps from a given ring to
test rings are cut down to a small family.

* `New.Variety.Envelope.IsSolution`, `New.Variety.Envelope.IsSolutionClosed`: a list of equations,
  and the injective ring maps whose image holds a solution of each solvable equation with
  coefficients in the image.
* `New.Variety.Envelope.exists_isSolutionClosed`: every map B → V factors through such a subring of
  V, which is a quotient of one polynomial ring over B (its variables
  `New.Variety.Envelope.SolutionName` name solutions).
* `New.Variety.Envelope.IsSolutionClosed.isTest`: such a subring of a test ring is a test ring.


### `IsSolution`

 x solves equation number o with coefficients a.
* o = 0: x is idempotent, a₀ ∣ xa₁ and a₁ ∣ (1 − x)a₀.
* o = 1: a₀ⁿ ∣ a_{n+1} − x for all n.
* o = n + 2: Σ_{k<n} a_k x^k = 0. 

### `SolutionName`

 Formal names for solutions over B: a term is an equation number o with a sequence of
coefficients, each a polynomial over B in finitely many earlier terms. 

### `SolutionName.op`

 Builds a solution name from an equation number `o` and, for each `k`, a polynomial `P k` over
  `B` in `n k` variables together with the `n k` solution names `t k` substituted into it. 

### `IsSolutionClosed`

 g: W → V is injective, and every equation `New.Variety.Envelope.IsSolution` with coefficients in
g(W) that has a solution in V has one in g(W). 

### `exists_isSolutionClosed`

 Every ring map φ : B → V extends to a ring map g from the polynomial ring over B in the names
`New.Variety.Envelope.SolutionName`, such that the induced injection of the quotient by ker g into V
satisfies the closure condition `New.Variety.Envelope.IsSolutionClosed`. 

### `IsSolutionClosed.map_dvd_iff`

 If g : W → V is solution-closed (`New.Variety.Envelope.IsSolutionClosed`), then g x divides
g y in V exactly when x divides y in W. 

### `IsSolutionClosed.isTest`

 If `g : W →+* V` is solution-closed (`IsSolutionClosed`: `g` is injective, and every equation of
the kind `IsSolution` with coefficients in `g(W)` that has a solution in `V` already has one in
`g(W)`), and `V` is a test ring (`IsTest`: reduced, absolutely integrally closed, and any `a, b`
admit an idempotent `e` with `a ∣ e b` and `b ∣ (1 − e) a`), then `W` is a test ring. The reason is
that roots of monic polynomials, the idempotents that compare two elements, and reducedness all pull
back along `g`. 

### `exists_natTrans_isTest_and_factors`

 For any family of commutative rings R o there are an endofunctor E of commutative rings and a
natural map θ : A → E(A) such that (a) every E(A) is a test ring, and (b) every ring map φ from
some R o to a test ring factors through θ at R o (the source of φ is written as the identity functor
applied to R o, which is R o). 


## Relatively affine maps, zero loci and unit loci

Relative representability for functors from rings to sets (`New.Variety.PointFunctor`):
`New.Variety.IsRelAffine p` says that the pull-back of `p` along each point `reprBy A ⟶ Y` is
representable. This is the analogue of an affine morphism.

* It is stable under pull-back and composition (`New.Variety.IsRelAffine.baseChange`,
  `New.Variety.IsRelAffine.comp`).
* `New.Variety.unitPoints_le_range_reprMap`: for a localisation `L` of `R` at `M`, the unit locus of
  `M` lies in the image of `reprBy L`.
* `New.Variety.isRelAffine_zeroPoints`: the inclusion of a zero locus is relatively representable.


### `IsRelAffine`

 The property of a map X → Y of set-valued functors on rings that its pull-back along every
point h_A → Y is representable, of the form h_B → h_A. 

### `IsRelAffine.baseChange`

 Relative representability is stable under pull-back: if `p : X ⟶ Y` is relatively
representable and the square of `v : V ⟶ X`, `q : V ⟶ W`, `p` and `u : W ⟶ Y` is a pull-back,
then `q` is relatively representable. 

### `unitPoints_le_range_reprMap`

 Let `L` be a localisation of `R` at `M`. Every ring map out of `R` that sends each element of
`M` to a unit factors through `R → L`. In other words, the unit locus of `M` in `reprBy R` lies in
the image of `reprBy L`. 

### `isRelAffine_ι_of_forall_map_mem_iff`

 Let `U` be a subfunctor of `Y`. Suppose that for each point `y ∈ Y(R)` there are subsets `A`,
`N` of `R` such that `f : R ⟶ B` carries `y` into `U` exactly when it kills `A` and inverts
`N`. Then the inclusion of `U` is relatively representable. 

### `isRelAffine_zeroPoints`

 For `s : X ⟶ h_R` and a subset `I` of `R`, the inclusion of the zero locus
`New.Variety.zeroPoints s I` (the points whose ring map `R → B` kills `I`) is relatively
representable. 


## Continuity of cohomology from an affine atlas

* `New.Variety.IsCohomContinuous.isFilteredColimit_antitoneFamily`,
  `New.Variety.IsCohomContinuous.isFilteredColimit_adjoin`: the two forms used later, for a
  decreasing family of subfunctors and for base change to the finitely generated subalgebras of an
  algebra.


### `TestCohomology.map_comp`

 Pull-back on cohomology (`New.Variety.TestCohomology.map`) is contravariantly functorial:
pulling back along `u ≫ s` is pulling back along `s`, then along `u`. Here x lies in Hⁿ(Y,
Λ) = Extⁿ(ℤ[Y restricted along the inclusion `testIncl` of test rings], `locConstCoeff Λ`). 

### `baseChangeOf.ext`

 Two points of a base change X ×_{h_R} h_A with values in B are equal if they have the same
point of X and the same ring map A → B. 

### `pullbackOver`

 For s: X → Y, the base change functor from functors over Y to functors over X, sending E → Y
to X ×_Y E → X. 

 ### Continuity and its first consequences 

### `IsCohomContinuous`

 Continuity over X: for every filtered inverse system of functors relatively representable
(affine) over X, the cohomology on test rings with locally constant Λ-valued coefficients of the
limit is the colimit of the cohomologies. 

### `IsCohomContinuous.of_isRelAffine`

 If q: X → Y is relatively representable (affine) and Λ-cohomology is continuous over Y, that is,
turns filtered limits of functors affine over Y into colimits (`New.Variety.IsCohomContinuous`),
then it is continuous over X. 

### `TestCohomology.antitoneFamily`

 For a decreasing family V of subfunctors of Y, the direct system a ↦ H^n(V_a, Λ) with
restriction maps, computed on test rings with locally constant Λ-valued coefficients. 

### `IsCohomContinuous.isFilteredColimit_antitoneFamily`

 Let V be a decreasing family of subfunctors of Y, indexed by a preorder, whose inclusions are
relatively representable, and let cohomology be continuous over Y. If D is a filtered diagram of
indices with a cocone m such that V at the vertex of m contains the intersection of the V(D j),
then Hⁿ(V(m.pt), Λ) is the colimit of the Hⁿ(V(D j), Λ). 

### `baseChangeFunctor`

 For s: X → h_R, the contravariant functor sending an R-algebra S to the functor X ×_{h_R}
h_S, forgetting its projection to X. 

### `baseChangeTransition`

 For X over h_R and a homomorphism f: S → T of R-algebras, the induced map of base changes
X_T → X_S. 

### `IsCohomContinuous.isFilteredColimit_adjoin`

 Let s : X → h_R, let Λ-cohomology be continuous over X (`New.Variety.IsCohomContinuous`), let a
: R → S be a ring map and T an S-algebra. Then in each degree the cohomology of the base change X_T
is the colimit of the cohomologies of the X_{T'}, where T' runs over the S-subalgebras of T
generated by finite subsets. 

### `isCorepresentable_cech`

 The `(m + 1)`-fold fibre power, as a functor on maps of sets, is corepresented by the map from
`m + 1` points to one point; in particular it preserves limits. 

### `IsCohomContinuous.of_hasCohomDenseImage`

 Let `q : h_T → Y` be relatively affine: its pull-back along every point h_A → Y is
representable. Suppose the image of `q` on test rings is cohomologically dense in `Y` for the
coefficient functor of locally constant functions Spec A → Λ (`HasCohomDenseImage`). Then, for every
filtered inverse system of functors affine over `Y`, the Λ-cohomology of the limit is the colimit of
the cohomologies (`New.Variety.IsCohomContinuous`). 
