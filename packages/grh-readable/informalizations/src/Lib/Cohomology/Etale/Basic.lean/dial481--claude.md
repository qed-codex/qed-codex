---
{
  "module": "src/Lib/Cohomology/Etale/Basic.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Cohomology/Etale/Basic.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Cohomology/Etale/Basic.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Cohomology of functors as Ext: test rings, points, functoriality, coefficients

Fix a category `C` of test objects and a coefficient functor `F : C ⥤ Ab`. A space is a functor
`Y : C ⥤ Type 1`, and its cohomology is `New.Variety.H N F n = Extⁿ(N, F)` with `N = ℤ[Y]`, computed
in the category `New.Variety.AbFunctor C` of functors `C ⥤ Ab`. Here `H.map` is pull-back in `N` and
`H.push` is push-forward in `F`. In the main case `C` is the category of test rings, a scheme is
replaced by its functor of points, and `F` sends `A` to the locally constant functions `Spec A → Λ`
for an abelian group `Λ`. The file proves stability properties of test rings, formal functoriality
of `H` and the additive Yoneda lemma, and it fixes vocabulary for fixed point formulas and
congruence relations with Frobenius.

## Main definitions and results

* `New.Variety.H N F n = Extⁿ(N, F)` and `New.Variety.freeAb` (the functor `Y ↦ ℤ[Y]`), with
  pull-back `New.Variety.H.map` in `N` and push-forward `New.Variety.H.push` in `F`.
* `New.Variety.IsCohomEquiv F α`: `α` is bijective on all `Extⁿ(-, F)`.
  `New.Variety.IsCohomDense F U`: the subfunctor `U` gives such an equivalence over every point
  `New.Variety.pointMap y`.
* `New.Variety.IsTest`, `New.Variety.TestRing`: test rings and their category. A test ring is
  reduced and absolutely integrally closed, and divisibility in it is total after a partition by an
  idempotent.
* `New.Variety.locConstCoeff`, `New.Variety.TestCohomology.map`: the coefficients A ↦ {locally
  constant Spec A → Λ} on test rings, and pull-back on cohomology.
* `New.Variety.IsTest.pi`, `New.Variety.IsTest.localization`, `New.Variety.IsTest.quotient`:
  products, localisations and quotients by radical ideals of test rings are test rings.
* `New.Variety.H.dimension_shift_induction`: induction on classes by dimension shifting. Identities
  between maps of `Ext` groups are checked in degree zero and on connecting maps.

Notions from other files:
* `New.Variety.IsAbsIntegrallyClosed`: A is absolutely integrally closed: every monic polynomial
  over A of positive degree has a root in A.

## Relation to the literature

Known; see `Lib.Cohomology.Etale.FilteredLimits` and `Lib.Cohomology.WoodsHole` for sources.



## Cohomology as Ext, comparisons and Zariski descent

* `New.Variety.Comparison`: a comparison of two theories, with the induced map
  `New.Variety.Comparison.pull`.
* `New.Variety.HasPartitions` and `New.Variety.HasZariskiDescent`: for tests with rings `ι A`,
  cutting along idempotents, and Zariski descent (a subfunctor that holds near every maximal ideal,
  `New.Variety.IsZariskiLocallyTop`, is dense).


### `scoped instance : CoeFun (D ⥤ T) fun _ ↦ D → T`

 A functor is applied to an object. 

### `scoped instance {F G : D ⥤ T} : CoeFun (F ⟶ G) fun _ ↦ ∀ A : D, F A ⟶ G A`

 A map of functors is applied to an object. 

### `scoped instance {F : D ⥤ Type _} : CoeFun (Subfunctor F) fun _ ↦ ∀ A : D, Set (F A)`

 A subfunctor is applied to an object. 

### `AbFunctor`

 The category of covariant functors from C to abelian groups. 

### `HasAbFunctorExt`

 The assertion that Ext groups in the category of functors from C to abelian groups exist,
with values in a larger universe. 

 ### Fibre powers and disjoint unions 

### `cech`

 For p: E → Y, the (m+1)-fold fibre power of E over Y: tuples of m+1 points of E(A) with the
same image in Y(A). 

### `cech.proj`

 The projection from the (m+1)-fold fibre power of p: E → Y to E taking the j-th coordinate. 

### `sigma`

 For a family X_i of set-valued functors on C, the functor sending A to the disjoint union of
the X_i(A). 

### `sigma.ι`

 The inclusion of X_i into the disjoint union of the family of functors X. 

 ### Cohomology, equivalences and comparisons 

### `H`

 The group Ext^n(N,F) in the category of functors from C to abelian groups; for N = Z[Y] it
is the cohomology H^n(Y,F). 

### `freeAb`

 The functor sending a set-valued functor Y to Z[Y], whose value at A is the free abelian group
on Y(A). 

### `liftCoeff`

 A functor from C to small abelian groups, regarded as taking values in abelian groups of the
next universe. 

### `reprFunctor`

 The contravariant functor sending an object A of C to the set-valued functor h_A = Hom(A,−),
lifted to the next universe. 

### `reprBy`

 The functor h_A = Hom(A,−) represented by the object A. 

### `reprMap`

 For a morphism f: A → B of C, the map of representable functors h_B → h_A given by
precomposition with f. 

### `restrictAlong`

 For φ: C' → C, the functor N ↦ N∘φ from functors on C to functors on C', with values in D. 

### `H.map`

 For α: N' → N, the homomorphism Ext^n(N,F) → Ext^n(N',F) given by precomposition with α. 

### `H.push`

 For β: F → F', the homomorphism Ext^n(N,F) → Ext^n(N,F') given by postcomposition with β. 

### `H.pushHom`

 The additive map sending a morphism β: F → G to the induced homomorphism
Ext^n(N,F) → Ext^n(N,G). 

### `CoeffAction`

 An action of the ring R on the functor F, that is, a ring homomorphism from R to the
endomorphism ring of F. 

### `CoeffAction.act`

 The ring homomorphism from `R` to the endomorphisms of `F`. 

### `IsCohomEquiv`

 α: N' → N is an equivalence for F: the pull-back Ext^n(N,F) → Ext^n(N',F) is bijective for
every n. 

### `Comparison`

 A comparison from F on C to F' on C': a functor φ: C' → C (the field `functor`) with a natural
transformation (the field `coeffHom`) β: F∘φ → F'. 

### `Comparison.functor`

 The functor `C' ⥤ C` between the categories of tests. 

### `Comparison.coeffHom`

 The map from the restriction of `F` along `functor` to `F'`. 

### `Comparison.id`

 The comparison from F to itself given by the identity functor of C and the identity of F. 

### `Comparison.pull`

 For a comparison (φ,β) and α: N' → N∘φ, the homomorphism Ext^n(N,F) → Ext^n(N',F') obtained
by restricting along φ, pushing by β and pulling by α. 

 ### Fibre products, points and dense subfunctors 

### `toArrowFunctor`

 The functor sending a natural transformation p between functors D → T to the functor A ↦ p_A
from D to the category of arrows of T. 

### `cechFunctor`

 The functor sending a map p: E → Y of set-valued functors on C to the (m+1)-fold fibre power
of E over Y. 

### `fibreProd`

 For u: W → Y and p: E → Y, the fibre product of W and E over Y. 

### `fibreProd.fst`

 The first projection from the fibre product of W and E over Y to W. 

### `fibreProd.snd`

 The second projection from the fibre product of W and E over Y to E. 

### `pointMap`

 The map h_A → Y corresponding to a point y of Y(A) by the Yoneda lemma. 

### `sigma.desc`

 For maps f_i: X_i → Y of set-valued functors, the map from the disjoint union of the X_i to
Y that is f_i on X_i. 

### `_root_.CategoryTheory.Subfunctor.whisker`

 For a subfunctor U of Y and φ: C' → C, the subfunctor U∘φ of Y∘φ. 

### `IsCohomDense`

 The subfunctor U of Y is dense for F: for every point h_A → Y, the inclusion of the preimage
of U in h_A is an equivalence for F. 

 ### Tests with rings: idempotents and Zariski descent 

### `IsQuotientByElem`

 The map `π : A ⟶ B` cuts `A` along the element `e` of the ring `ι A`: (a) `ι π` kills `e`;
(b) every `f : A ⟶ B'` such that `ι f` kills `e` factors uniquely through `π`; (c) `ι π` is
surjective; (d) its kernel lies in the ideal `(e)`. By (a), (c), (d), `ι B = ι A ⧸ (e)`. 

### `HasPartitions`

 The tests `C`, with rings `ι A`, can be cut along idempotents, compatibly with the coefficients
`F`: each idempotent e ≠ 1 of ι(A) has a `New.Variety.IsQuotientByElem` A → B, and
ι(A) ≅ ι(B₁) × ι(B₂) via maps A → B₁, B₂ implies F(A) ≅ F(B₁) × F(B₂). 

### `HasPartitions.exists_quotient`

 Every idempotent `e ≠ 1` of the ring of `A` is killed by a universal map `π : A ⟶ B`, and the
  ring of `B` is the quotient by `e`. 

### `HasPartitions.bijective_prod`

 If two maps from `A` make the ring of `A` the product of the rings of `B₁` and `B₂`, they make
  the group `F.obj A` the product of `F.obj B₁` and `F.obj B₂`. 

### `IsZariskiLocallyTop`

 The subfunctor `U` of `Y` is locally everything for the rings `ι A`: for every `y ∈ Y(A)` and
maximal ideal `m` of the ring `ι A` there is `a ∉ m` such that `y` maps into `U` along every
`A ⟶ B` that makes `a` invertible. 

### `HasZariskiDescent`

 Zariski descent for `F`: a subfunctor `U` of `Y` that is locally everything
(`New.Variety.IsZariskiLocallyTop`) is dense for `F` (`New.Variety.IsCohomDense`). 

### `IsZariskiLocallyTop.whisker`

 If the subfunctor `U` of `Y` is locally everything for the rings `ι A`
(`New.Variety.IsZariskiLocallyTop`), then its restriction `U.whisker φ` along `φ : C' ⥤ C` is
locally everything for the rings `ι (φ A')`. 

 ### Pointwise surjections, integer relations and products of coefficients 

### `IsPointwiseSurjective`

 The property of p: E → Y that E(A) → Y(A) is surjective for every object A. 

### `freeAbMap`

 For u: Y' → Y∘φ, the induced map of free abelian group functors Z[Y'] → Z[Y]∘φ. 

### `IsComparableRing`

 For a ring `R` and a map f: A → R, any a, b in R have an idempotent e of A with a ∣ f(e)b and
b ∣ (1 − f(e))a: on one part of the partition given by f(e), a divides b, and on the other part b
divides a. 

### `Cancels`

 The integers `m i` add up to zero on every fibre of `v`, that is, `∑ m i • [v i] = 0` in the
free abelian group on `V`. 

### `Cancels.mono`

 If the integers `m i` cancel on the fibres of `v` and `v'` factors through `v` (equal values
of `v` give equal values of `v'`), then they cancel on the fibres of `v'`. 

### `piAbFunctor`

 For a family `F : ι → AbFunctor C` of abelian-group-valued functors on C (here `ι` is an index
type), the functor sending A to the product of the groups F_i(A). 

### `piAbFunctor.π`

 The projection from the product of the family `F : ι → AbFunctor C` of functors to its i-th
factor F_i. 

### `AllBijective`

 For a family of maps f_i : A_i → B_i, the assertion that every f_i is bijective. 

### `isoOfAppBijective`

 A natural transformation with values in a concrete category whose forgetful functor reflects
isomorphisms is an isomorphism if it is bijective at every object. 


## Test rings, functors of points and locally constant coefficients

* `New.Variety.PointFunctor`, `New.Variety.pointsToBase`: spaces, and the map from the functor of
  points of a scheme over Spec R to h_R.


 ### Test rings 

### `IsAbsIntegrallyClosedLocal`

 A is an absolutely integrally closed local domain: a local domain in which every monic
polynomial of positive degree has a root. 

### `IsTest`

 A is a test ring: reduced, absolutely integrally closed, and any a, b admit an idempotent e
with a ∣ eb and b ∣ (1 − e)a. 

### `IsTest.isComparableRing`

 Any two elements of `A` are comparable for divisibility after a partition by an idempotent
  (`New.Variety.IsComparableRing` for the identity map of `A`). 

### `IsTest.isReduced`

 The ring `A` has no nonzero nilpotent elements. 

### `TestRing`

 The category of test rings (`New.Variety.IsTest`), as a full subcategory of commutative
rings. 

### `testIncl`

 The inclusion functor from the category of test rings into the category of commutative
rings. 

 ### Spaces and their cohomology 

### `PointFunctor`

 The category of covariant functors from (small) commutative rings to sets of the next
universe. 

### `locConstSpec`

 For an abelian group Λ, the functor on commutative rings sending A to the group of locally
constant functions Spec A → Λ. 

### `locConstCoeff`

 For an abelian group Λ, the coefficient functor on test rings sending A to the group of
locally constant functions Spec A → Λ. 

### `mapOnTests`

 For a map u: X → Y of set-valued functors on rings, its restriction to a map of functors on
test rings. 

### `TestCohomology.map`

 For u: X → Y and each degree n, the pull-back homomorphism Hⁿ(Y, Λ) → Hⁿ(X, Λ) on
cohomology computed on test rings. 

### `IsTestCohomEquiv`

 The map u: X → Y of functors on rings induces isomorphisms Hⁱ(Y, Λ) → Hⁱ(X, Λ) in each degree i,
for cohomology computed on test rings with locally constant coefficients. 

### `HasCohomDenseImage`

 The image of u: X → Y, restricted to test rings, is cohomologically dense in Y for the
coefficient functor of locally constant functions Spec A → Λ. 

 ### Spaces over a ring 

### `pointsToBase`

 For a morphism s: X → Spec R, the map from the functor of points of X to h_R sending a
point x ∈ X(A) to the ring map R → A whose spectrum is s∘x. 

### `baseRingMap`

 For s: X → h_R and a point x ∈ X(B), the ring homomorphism R → B that is the image of x
under s. 

### `reprBy_map_down`

 The map of `h_R` along `f : B ⟶ B'` sends a ring map `R ⟶ B` to its composite with `f`. 

### `zeroPoints`

 For s: X → h_R and a subset I of R, the subfunctor of points x ∈ X(B) whose structure map
R → B sends I to 0. 

### `unitPoints`

 For s: X → h_R and a subset I of R, the subfunctor of points x ∈ X(B) whose structure map
R → B sends every element of I to a unit. 

### `baseChangeOf`

 For s: X → h_R and a ring map φ: R → B, the base change X_B = X ×_{h_R} h_B. 


## Stability of test rings; local rings as valuation rings

Stability properties of test rings, the rings on which points and cohomology are evaluated.

* `New.Variety.isTest_of_preValuationRing`: an absolutely integrally closed domain in which of any
  two elements one divides the other is a test ring.
* `New.Variety.IsTest.pi`, `New.Variety.IsTest.localization`, `New.Variety.IsTest.quotient`:
  products, localisations and quotients by radical ideals of test rings are test rings.
* `New.Variety.IsTest.exists_valuationSubring_atPrime`: the local rings of a test ring are valuation
  rings of algebraically closed fields.


### `instance : IsAbsIntegrallyClosedLocal K`

 An algebraically closed field is an absolutely integrally closed local domain. 

### `instance (V : ValuationSubring K) : IsAbsIntegrallyClosedLocal V`

 A valuation subring of an algebraically closed field is an absolutely integrally closed local
domain. 

### `locallyConstant_mem_of_indicator`

 The group of locally constant functions `Spec A → Λ` is generated by the functions equal to
a constant `a` on the basic open set `D(e)` of an idempotent `e` and to `0` elsewhere: a subgroup
that contains these functions contains every locally constant function. 

### `exists_map_dvd_of_mem_map`

 If divisibility in `A` is total, every element of the extension of an ideal `J` along
`f : A →+* B` is a multiple of `f i` for a single `i ∈ J`. 

### `isTest_of_preValuationRing`

 An absolutely integrally closed domain `A` in which of any two elements one divides the other
(`PreValuationRing A`) is a test ring: the idempotent `e` can be taken to be `1` or `0`. 

 ### Products, localisations and quotients of test rings 

### `IsTest.pi`

 A product of test rings is a test ring. 

### `IsTest.isComparableRing_of_associated`

 Let `A` be a test ring and `f : A →+* B` a ring map such that every element of `B` is
associated to (a unit times) the image of an element of `A`. Then any `y`, `z` in `B` have an
idempotent `e` of `A` with `y ∣ f e * z` and `z ∣ (1 - f e) * y` (`IsComparableRing f`). 

### `IsComparableRing.id`

 If any two elements of `B` are comparable by an idempotent `e` of `A` through `f`, then they are
comparable by the idempotent `f e` of `B` itself. 

### `exists_associated_localization`

 Every element of the localisation of `A` at `M` is associated to the image of an element
of `A`. 

### `IsTest.localization`

 The localisation of a test ring `A` at a submonoid `M` is a test ring. 

### `IsTest.quotient`

 The quotient of a test ring by a radical ideal is a test ring. 

### `IsTest.exists_valuationSubring_atPrime`

 Let `A` be a test ring, `p` a prime ideal of `A` and `L` the localisation of `A` at `p`. Then
`L` is an absolutely integrally closed local domain (`IsAbsIntegrallyClosedLocal`), of any two
elements of `L` one divides the other (`PreValuationRing`), and there are an algebraically closed
field `K`, a valuation subring `O` of `K` and an `A`-algebra structure on `O` for which `O` is a
localisation of `A` at `p`. 

### `instance [IsAbsIntegrallyClosedLocal A] : IsAlgClosed (ResidueField A)`

 The residue field of an absolutely integrally closed local domain is algebraically closed. 


## Functoriality of cohomology and induction by dimension shifting

For a comparison `c = (φ, β)` (`New.Variety.Comparison`), `c.pull α` restricts along the functor
`φ`, pushes by `β` and pulls by `α`.

* `New.Variety.Comparison.map_pull_eq_pull_map`, `New.Variety.Comparison.pull_push`,
  `New.Variety.Comparison.pull_trans`: comparisons commute with pull-back and push-forward, and they
  compose.


 ### Induction on classes and exact functors 

### `abbrev`

 The functor is exact: it is additive and preserves finite limits and finite colimits. 

### `H.smul_eq_push`

 A ring `R` acting on `F` acts on `Ext^n(N,F)` by push-forward along the endomorphism of `F`
by which `r` acts. 

### `instance : IsGrothendieckAbelian.{1} (AbFunctor C)`

 Functors from `C` to abelian groups form a Grothendieck abelian category. 

### `H.dimension_shift_induction`

 Induction on Ext classes out of `N`: a property `P` holds for every class `x` in `Ext^n(N,F)` if
it holds for the classes `mk₀ f` of morphisms `f : N ⟶ F` (`h₀`) and, for each short exact
sequence `S` of functors `0 → S.X₁ → S.X₂ → S.X₃ → 0` and each `y` in `Ext^n(N,S.X₃)`, passes from
`y` to its image in `Ext^{n+1}(N,S.X₁)` under the connecting class (`h`). 

### `mapExactFunctor_naturality`

 For a natural transformation η: Φ → Ψ of exact functors and x in Ext^n(N,F), pushing Φ(x)
forward along η_F equals pulling Ψ(x) back along η_N, in Ext^n(ΦN,ΨF). 

### `mapHom`

 The additive map sending a morphism α: M → N to the pull-back Ext^n(N,F) → Ext^n(M,F). 

### `mapₗ`

 For a ring R acting on F and α: M → N, the pull-back Ext^n(N,F) → Ext^n(M,F) as an R-linear
map. 

### `IsCohomEquiv.of_isIso`

 An isomorphism `α : M ⟶ N` induces bijections `Ext^n(N,F) → Ext^n(M,F)` in every degree. 

### `Comparison.pull_push`

 If `γ : F ⟶ G` and `γ' : F' ⟶ G'` intertwine the coefficient maps of two comparisons with the
same functor `c.functor`, then the comparison maps commute with push-forward along `γ` and `γ'`. The
target of `α` is `c.functor ⋙ N`, written through the comparison `⟨c.functor, β⟩`. 

### `Comparison.trans`

 The composite of comparisons (φ,β) from F to F' and (φ',β') from F' to F'': the functor φ∘φ'
with the map Fφφ' → F'φ' → F''. 

### `IsCohomEquiv.comp_iff`

 If `α' : K ⟶ M` induces bijections on cohomology with coefficients `F`, then `α' ≫ α` does if
and only if `α : M ⟶ N` does. 

### `pull_id_eq_push`

 The comparison map of `(𝟭 C, β)` along the identity of `N` is the push-forward along `β`. 

### `pull_whiskerRight`

 For `η : φ ⟶ ψ` and `β : ψ ⋙ F ⟶ F'`, moving `η` from the coefficient map (`η F` before
`β`) to the source map (`η N` after `α`) does not change the comparison map. The target of `α` is
`φ ⋙ N`, written through the comparison `⟨φ, whiskerRight η F ≫ β⟩`. 

 ### Squares and composites of comparisons 

### `map_pull_eq_pull_map`

 The comparison `c` is natural in the source of cohomology: if `a' : M' ⟶ N'` lies over
`α : M ⟶ N`, in the sense that the square formed with `a` and `b` commutes, then pulling a class
back by `c` along `a` and then along `a'` is pulling it back along `α` and then by `c` along `b`. 

### `pull_trans`

 Comparison maps compose. Applying the comparison map of c along a and then that of c' along α'
gives the comparison map of the composite `New.Variety.Comparison.trans` c c', taken along
`α' ≫ whiskerLeft c'.functor a`, the map `a` restricted along the functor of c'. 


## Module coefficients and points of an `R`-scheme in `k`-algebras

* `New.Variety.algPoints`: a scheme `X` over `R` gives the functor `A ↦ X(A)` on commutative
  `k`-algebras.


### `moduleCoeff`

 A functor F from C to k-modules, regarded as a functor to abelian groups, so that it can
serve as the coefficients of cohomology. 

### `instance : CoeffAction k (moduleCoeff F)`

 The ring `k` acts on `moduleCoeff F` through the action of `k` on the values of `F`. 

 ### Commutative algebras and functors of points 

### `CommAlg`

 The category of (small) commutative algebras over a commutative ring k. 

### `CommAlg.homOfRingHom`

 A ring map of k-algebras that respects the structure maps, as a morphism of k-algebras. 

### `restrictAlg`

 Restriction of scalars along k → k': the functor regarding a commutative k'-algebra as a
k-algebra. 

### `specAlg`

 For an R-algebra k, the contravariant functor from commutative k-algebras to schemes over
Spec R sending A to Spec A, with structure map given by R → k → A. 

### `algPoints`

 For an R-algebra k, the functor sending a scheme X over Spec R to its functor of points
A ↦ X(A) on commutative k-algebras A. 

### `algPointsOf`

 For an R-algebra k and a scheme X over Spec R, the functor sending a commutative k-algebra A
to the set X(A) of morphisms Spec A → X over Spec R. 


## Tangent polynomials at coincidences and congruence relations

Maps `W ⟶ Z` of schemes over `R` are described through points with values in rings:
`New.Variety.PointsIn X A` is `X(A)`. A tangent vector at `y ∈ W(k)` is a point of `W(k[ε])` over
`y`.

* `New.Variety.IsTangentPoly`: a polynomial `P` with `P t = P 0 * det (1 - t (dc)⁻¹ du)` at a
  coincidence `c y = u y`.
* `New.Variety.IsNullFamily`: the local terms of a fixed point formula for a linear combination of
  maps add up to zero in weight `h`.
* `New.Variety.CongruenceRelation`: a congruence relation between maps and Frobenius powers modulo
  `𝔭`.


### `fst_surjective_and_kerIdeal_sq_eq_bot`

 The first projection `k ⊕ M → k` of the trivial square-zero extension is surjective, and its
kernel ideal squares to zero. 

### `SqZeroExt.fst`

 The k-algebra homomorphism k ⊕ M → k from the trivial square-zero extension, sending (a, m)
to a. 

### `PointsIn`

 The points X(A) of a scheme X over Spec R with values in the k-algebra A, that is, the
morphisms Spec A → X over Spec R. 

### `PointsIn.map`

 For a k-algebra homomorphism φ: A → B and a point y in W(A), the point in W(B) obtained by
composing y with Spec φ. 

### `IsTangentPoly`

 `P` is a tangent polynomial of the maps `c, u : W ⟶ Z` at the point `y ∈ W(k)`, the algebraic
form of `P t = P 0 * det (1 - t (dc)⁻¹ du)`; here `W` and `Z` are functors of points on
commutative `k`-algebras.
Precisely: there are a finitely generated `k`-module `T`, a point `v ∈ W(k ⊕ T^*)` (square-zero
extension by the dual), which turns each `x ∈ T` into a point `f x ∈ W(k[ε])` by evaluation
`T^* → k` at `x`, and `A ∈ End T`, with (a) `T` of rank `d`;
(b) `v` lifts `y`, so the `f x` are tangent vectors at `y`;
(c) `x ↦ c (f x)` is injective; (d) `u (f x) = c (f (A x))`; (e) `P(t) = P(0) det (1 - t A)`
for all `t ∈ k`. 

### `IsNullFamily`

 The formal sum `∑ a_i [u_i]` of maps `u_i : W ⟶ Z` is null in weight `h`, for tangent
polynomials of rank `d`: for every `c : W ⟶ Z`, let `S` be the set of coincidences `(i, y)` with
`a_i ≠ 0`, `y ∈ W(k)` and `c(y) = u_i(y)`. If each `(i, y)` in `S` is given a tangent polynomial
`P (i, y)` of rank `d` of `c, u_i` at `y` (`New.Variety.IsTangentPoly`) with `P(1) ≠ 0`, then `S`
is finite and the sum over `S` of `a_i · (coefficient of degree h of P) / P(1)` is zero. 

### `CongruenceRelation`

 A congruence relation between the maps `u_i : W ⟶ Z` and powers of Frobenius modulo `𝔭`: for
every field `k` of characteristic `p` and every point `x : Spec k ⟶ W` whose ring map `R → k`
sends every element of `𝔭` to zero, `∑ m_i [u_i(x) ∘ F^{a_i}] = 0` as a formal sum of points of `Z`
(`New.Variety.Cancels`), where `F^{a_i}` is the `a_i`-th iterate of the Frobenius `y ↦ y^p` of
`k`. 

### `IsGaloisCovering`

 `c : W ⟶ Z` is a Galois covering with the finite group `Δ`, which acts on `W` through `a`:
every `a δ` is an automorphism of `W` over `Z`, `c` is surjective, and on points with values in
fields of characteristic `0`, `Δ` acts simply transitively on each fibre of `c`. 

### `IsGaloisCovering.comp_eq`

 Every `δ ∈ Δ` acts over `Z`: `a δ` followed by `c` is `c`. 

### `IsGaloisCovering.surjective`

 The morphism of schemes underlying `c` is surjective. 

### `IsGaloisCovering.torsor`

 Two points with values in a field of characteristic 0 and with the same image under `c` differ
  by a unique element of `Δ` (`c.1` and `(a δ).1` are the underlying morphisms of schemes). 


## Additive Yoneda and objectwise exactness for functors to abelian groups

* `New.Variety.freeAb.desc`, `New.Variety.freeAb.hom_ext`: maps out of ℤ[Y] are natural families
  of elements indexed by the points of `Y`.
* `New.Variety.homReprEquiv`: the additive Yoneda lemma; it follows that ℤ[h_A] is projective.
* `New.Variety.exact_of_app`, `New.Variety.shortExact_of_app`: exactness is checked objectwise.


### `freeAb.desc`

 For maps `s A : Y(A) → F(A)` natural in `A` (this is `h`), the morphism ℤ[Y] → F sending each
generator [y] to `s A y`. 

### `freeAb.hom_ext`

 Two maps ℤ[Y] → F agree if they agree on every generator [y]. 

### `freeAb.homEquiv`

 The universal property of `freeAb`: for a functor `X` to sets and a functor `Y` to abelian
groups, the bijection between maps ℤ[X] → Y and maps X → Y. 

### `homReprEquiv`

 The additive Yoneda lemma: maps ℤ[h_A] → F correspond to elements of F(A), compatibly with
addition; here h_A = Hom(A, −) is the functor represented by `A` (`New.Variety.reprBy`). 

### `homReprEquiv_comp`

 The additive Yoneda bijection is natural in the target: composing with `e : E ⟶ F` corresponds
to applying `e` at `A`. 

### `instance : Projective (freeAb (reprBy A))`

 The free abelian group ℤ[h_A] on a represented functor is projective. 

### `sum_app_apply`

 The value at `x ∈ N(A)` of a finite sum of maps `N ⟶ F` is the sum of their values. 

 ### Cokernels and relative chains 

### `abCoker`

 The cokernel of a map α: M → N of functors to abelian groups, formed objectwise: A ↦
N(A)/α(M(A)). 

### `abCoker.π`

 The quotient map N → coker α, sending an element of N(A) to its class modulo α(M(A)). 

### `instance : Epi (abCoker.π α)`

 The quotient map `abCoker.π α` is an epimorphism. 

### `relFreeAb`

 For a subfunctor `U` of a set-valued functor `Y`, the functor to abelian groups ℤ[Y]/ℤ[U], the
cokernel of the map ℤ[U] → ℤ[Y]. 

### `relFreeAb.π`

 For a subfunctor `U` of `Y`, the quotient morphism ℤ[Y] → ℤ[Y]/ℤ[U]. 

### `relFreeAb.mk`

 For `x ∈ Y(A)`, the class of the generator [x] in ℤ[Y(A)]/ℤ[U(A)]. 

### `exact_of_app`

 If the maps `α : M ⟶ N` and `g : N ⟶ F` of functors to abelian groups give an exact sequence
`M(A) → N(A) → F(A)` at every object `A`, then `α ≫ g = 0` (the witness `w`) and the short complex
`M ⟶ N ⟶ F` is exact. 

### `shortExact_of_app`

 If at every object `A` the map `α A` is injective, the sequence `M(A) → N(A) → F(A)` is exact
in the middle and `g A` is surjective, then `α ≫ g = 0` (the witness `w`) and the short complex
`M ⟶ N ⟶ F` of functors to abelian groups is short exact. 

### `abCoker.desc`

 For `f : N ⟶ F` with `α ≫ f = 0`, the induced morphism `coker α ⟶ F` through which `f`
factors. 

### `relFreeAb.hom_ext`

 For a subfunctor `U` of `Y`, two maps ℤ[Y]/ℤ[U] → F agree if they agree on the class of every
generator [x]. 
