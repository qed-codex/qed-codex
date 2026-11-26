---
{
  "module": "src/Lib/Cohomology/TorsionTheories.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Cohomology/TorsionTheories.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Cohomology/TorsionTheories.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Tensoring degree-two classes; cohomology theories with ℓ-torsion coefficients

The file works in categories of functors to abelian groups. First, a class in `Ext² (N, K)` between
functors with flat values is restricted along any functor and tensored with any abelian-group-valued
functor, compatibly (`New.Variety.exists_isTensorClass`). Then the cohomology of a space over `X` is
computed on the category of elements of `X`. Last, the file treats cohomology theories with
`ℓ`-torsion coefficients on categories over the test rings, families of ideals, and the theory of
locally constant functions.

## Main definitions and results

* `New.Variety.IsTensorClass`, `New.Variety.exists_isTensorClass`: a family of classes that extends
  `S ⊗ ξ` from functors `S` with flat values to all functors, and its existence.
* `New.Variety.hasUniversalPoints_elements`,
  `New.Variety.isBijective_relFreeAb_tautologicalSection`, `New.Variety.sliceEquiv`: cohomology of a
  space over `X` is computed on the category of elements of `X` (`New.Variety.elementsProj`).
* `New.Variety.InvertsPrime`, `New.Variety.TestOver`: a local absolutely integrally closed ring `A`
  in which `ℓ` is invertible, and the category of test rings over `A`.
* `New.Variety.TorsionCoeff`, `New.Variety.Theory`: coefficients with Zariski descent, and theories,
  where classes also extend from closed loci. `New.Variety.Theory.locallyConstant` is the theory of
  locally constant functions.
* `New.Variety.IdealFamily`, `New.Variety.Theory.onZeros`: a compatible family of ideals, and the
  coefficient that sees only the locus where it is zero.
* `New.Variety.IdealFamily.isCohomEquiv_constToZeros`,
  `New.Variety.TorsionCoeff.pullbackAlong_oneLocConst_surjective`: the map from `ℤ/ℓ` relative to
  the locus where the ideal is the unit ideal to the locally constant functions on the zero locus is
  an equivalence for coefficients with Zariski descent, provided the locally constant functions
  along `g` underlie a theory `Θ`; hence every class on the constant functor `ℤ` with coefficients
  in a `TorsionCoeff g` (killed by `ℓ`, with Zariski descent) comes from one on the locally constant
  functions to `ℤ/ℓ`.

Notions from other files:
* `New.Variety.HasFlatValues F`: every value of `F` is a flat `ℤ`-module.
* `New.Variety.restrictAlong φ`, `New.Variety.freeAb`: the functor `N ↦ N ∘ φ`, and the functor
  sending a set-valued functor `Y` to `ℤ[Y]`, the free abelian group on `Y(A)` at each `A`.
* `New.Variety.relFreeAb U`, `New.Variety.abCoker α`: the functor `ℤ[V]/ℤ[U]` for `U ⊆ V`, whose Ext
  groups are the relative cohomology of `(V, U)`; the cokernel of `α`, formed objectwise.
* `New.Variety.IsTest`: a test ring A is reduced and absolutely integrally closed, and any a, b ∈ A
  admit an idempotent e with a ∣ eb and b ∣ (1 − e)a.
* `New.Variety.Comparison`: a functor φ : C' → C with a map F∘φ → F'; it `IsBijective` along α :
  N' → N∘φ if Ext^n(N, F) → Ext^n(N', F') is bijective for all n. `HasUniversalPoints u`, a
  sufficient condition: the fibres of u over points are representable, with the same coefficients.
* `New.Variety.IsCohomDense`, `New.Variety.HasZariskiDescent`: `U ⊆ Y` is dense for `F` if, for
  every point `h_A → Y`, the inclusion of the preimage of `U` induces bijections on Ext with
  coefficients `F`; `F` has Zariski descent if every `U` that contains `Y` near each maximal ideal
  (`New.Variety.IsZariskiLocallyTop`) is dense for `F`.

## Relation to the literature

Known result: Cup product with a degree-two class and closed supports, for mod-ℓ cohomology as Ext.
Only the formal set-up is given, for Ext on test rings. It consists of ℓ-torsion coefficient
theories with closed supports cut out by families of ideals, and a degree-two class between flat
functors tensored with every functor. No Chern class, Künneth formula, Gysin map or Poincaré duality
is stated here. Source: for the setting, Milne, Étale Cohomology, Ch. VI.

See also `Lib.Cohomology.Etale.FilteredLimits` and `Lib.PadicComparison.Duality.GoodPairs`.



## Tensoring a degree 2 class between flat functors with every functor

A class `ξ` in `Ext² (N, K)` between functors with flat values is written as a product of two
extension classes of short exact sequences that stay exact after tensoring, and a map.

Conventions: `New.Variety.AbFunctor` is the category of covariant functors to abelian groups,
`New.Variety.H` is `Ext` in it, `New.Variety.TotalH` the sum over all degrees with the Yoneda
product `New.Variety.TotalH.comp`, and `New.Variety.abTensor` the pointwise tensor product.


### `onePointFunctor`

 The constant functor on C with value the one-point set. 

### `tensorPoint`

 For `ρ : ℤ[pt] ⟶ K`, that is, a family of elements `ρ [pt]` of the values of `K` compatible
with the maps of `K`, the map `S ⟶ S ⊗ K`, `x ↦ x ⊗ ρ [pt]`, natural in `S`. 

### `TensorClassFamily`

 A family of classes in `Ext² (S ⊗ φ^* N, S ⊗ φ^* K)`, one for every functor `φ : D ⥤ C` and
every functor `S` from `D` to abelian groups; `φ^* N` is `φ ⋙ N`. 

### `IsTensorClass`

 The family `h` extends `(φ, S) ↦ S ⊗ φ^* ξ` from flat `S` to all `S`, compatibly with classes
between the functors `S` and with restriction. The equations are in total cohomology. 

### `IsTensorClass.comm`

 For a class `y` from `S` to `S'`, `y ⊗ φ^* N` followed by `h D φ S'` is `h D φ S` followed
  by `y ⊗ φ^* K`. 

### `IsTensorClass.eq_of_flat`

 For flat `S` the class is `ξ`, restricted along `φ` and tensored with `S`. 

### `IsTensorClass.restrict`

 The classes are compatible with restriction along a further functor `ψ : E ⥤ D`. 

### `exists_isTensorClass`

 Let `N` and `K` be functors with flat values and `ξ` a class in `Ext² (N, K)`. Then `ξ` can
be tensored with every functor, flat or not, compatibly: there is a family of classes in
`Ext² (S ⊗ φ^* N, S ⊗ φ^* K)`, for every functor `φ : D ⥤ C` and every `S` on `D`, that commutes
with classes between the `S`, is the restricted and tensored `ξ` for `S` with flat values, and is
compatible with restriction (`New.Variety.IsTensorClass`). 

 ## Slices, torsion coefficients, families of ideals and theories 

 ### A sieve cut out by a map to an acyclic object 

### `surjective_restrict_of_quotient_sieve`

 Let `φ : C' ⥤ C` be full and faithful, `q : φ A ⟶ b`, and `R` a sieve on `A` such that a map `f`
out of `A` lies in `R` exactly when `φ f` factors through `q`, and then it factors uniquely. Let `b`
be acyclic for `F` along `φ` (`New.Variety.IsAcyclicAt`: with coefficients `φ ⋙ F`, `Hom (b, φ –)`
has cohomology `F b` in degree `0` only). If `F.map q` is onto, then in every degree `n` restriction
`H^n (h_A, φ ⋙ F) → H^n (R, φ ⋙ F)` is onto; here `h_A = reprBy A` is the functor `Hom (A, –)`,
lifted to a higher universe. 

### `map_eq_zero_of_dies_along_quotient_sieve`

 Let `φ : C' ⥤ C` be full and faithful, `q : φ A ⟶ b`, and `R` a sieve on `A` that
contains every `f` such that `φ f` factors through `q`. Let `b` be acyclic for `F` along `φ`
(`New.Variety.IsAcyclicAt`). Then a section `x` of `F` at `φ A` that dies along every map in `R`
dies along `q`. 

### `surjective_and_map_eq_zero_of_quotient_sieve`

 Let `φ : C' ⥤ C` be full and faithful, `q : φ A ⟶ b`, and `R` the sieve of the maps `f` out of
`A` such that `φ f` factors, uniquely, through `q`. Let `b` be acyclic for `F` along `φ`
(`New.Variety.IsAcyclicAt`: with coefficients `φ ⋙ F`, `Hom (b, φ –)` has cohomology `F b` in
degree `0` only). (a) If `F.map q` is onto, restriction `H^n (h_A, φ ⋙ F) → H^n (R, φ ⋙ F)` is
onto for all `n`. (b) A section of `F` at `φ A` that dies along every map in `R` dies along `q`.
Part (a) is `New.Variety.surjective_restrict_of_quotient_sieve`, part (b) is
`New.Variety.map_eq_zero_of_dies_along_quotient_sieve`. 

 ### Slices: the category of elements of a set-valued functor 

### `sectionLift`

 For φ: C' → C and a section q of X∘φ, the functor a ↦ (φ(a), q(a)) from C' to the category
of elements of X. 

### `sectionMap`

 For a section q of a set-valued functor X, the morphism from the constant one-point functor
to X sending the point at c to q(c). 

### `elementsProj`

 For a set-valued functor X on C, the projection (c, x) ↦ c to C from the category of elements of
X, whose objects are the pairs (c, x) with x ∈ X(c). 

### `Comparison.HasUniversalPoints.on_elements`

 Universal points pass to categories of elements. Let `u : E' ⟶ c.functor ⋙ E` have universal
points (`New.Variety.Comparison.HasUniversalPoints`) for the comparison `c` from `F` to `F'`, and
let `X` be a set-valued functor on `C`. Then `u`, pulled back to the category of elements of
`c.functor ⋙ X`, has universal points for the comparison that `c` induces from the elements of `X`
(coefficient `F` restricted there) to those of `c.functor ⋙ X`. 

### `hasUniversalPoints_reprBy_elements`

 For an element a = (c, x) of E, the forgetful map from morphisms out of a to morphisms out of c
has universal points (`New.Variety.Comparison.HasUniversalPoints`) for the restriction of G to the
category of elements of E. 

### `tautologicalSection`

 The tautological section (c, x) ↦ x of the pull-back of X to its own category of elements. 

### `hasUniversalPoints_elements`

 The tautological section `New.Variety.tautologicalSection` has universal points
(`New.Variety.Comparison.HasUniversalPoints`) for the restriction of any coefficient G to the
category of elements of X. 

### `isBijective_relFreeAb_tautologicalSection`

 The relative cohomology of a pair `U ⊆ X` is computed on the category of elements of `X`, as
that of the point relative to the preimage of `U`: restricting to the elements of `X` and pulling
back along the tautological section (`New.Variety.tautologicalSection`) gives bijections
`Ext^n (ℤ[X]/ℤ[U], G) → Ext^n (ℤ[pt]/ℤ[U'], G')` for all `n`, where `U'` is the preimage of `U`
and `G'` is `G` restricted to the elements of `X`. 

 ### Total cohomology over a slice 

### `bijective_totalH_iff_isBijective`

 A comparison is bijective on total cohomology (restrict along `c.functor`, push along
`c.coeffHom`, then pull back along `α`) if and only if it is bijective in each degree. 

### `sliceEquiv`

 The additive isomorphism from total Ext(N ⊗ ℤ[X], F) to total Ext between the pull-backs of N
and F to the category of elements of X: restrict there, then precompose with
n ↦ n ⊗ [tautological point]. 

### `InvertsPrime`

 The ring `A` is local and absolutely integrally closed, and the prime `ℓ` is invertible in it.
Instance search finds `ℓ` from `A`. 

### `InvertsPrime.isUnit_prime`

 The prime `ℓ` is invertible in `A`. 

 ### Tests over a ring, coefficients, families of ideals, theories 

### `TestOver`

 The category of tests over A: the full subcategory of commutative A-algebras whose
underlying rings are test rings. 

### `TestOver.toTest`

 The functor from tests over A to test rings that forgets the A-algebra structure. 

### `ringOf`

 For a functor g from C to tests over A, the functor sending c to the commutative ring underlying
g(c), where `testIncl` is the inclusion of test rings (`TestRing`) into commutative rings. 

### `locConstAlong`

 For g from C to tests over A, the functor sending c to the abelian group of locally constant
functions Spec g(c) → ℤ/ℓ. 

### `TorsionCoeff`

 A coefficient along g: a functor F (the field `functor`) to abelian groups, killed by ℓ, that
satisfies Zariski descent (`New.Variety.HasZariskiDescent`) for the rings g(c). 

### `TorsionCoeff.functor`

 The coefficient, a functor from `C` to abelian groups. 

### `TorsionCoeff.prime_smul_eq_zero`

 Every value of `F` is killed by `ℓ`. 

### `TorsionCoeff.zariski_descent`

 `F` satisfies Zariski descent for the rings `(ringOf g).obj c`. 

### `IdealFamily`

 For a functor ι from C to commutative rings, ideals I_c (the field `ideal c`) of ι(c) such that
I_b is generated by the image of I_a for every morphism a → b. 

### `IdealFamily.ideal`

 The ideal `ideal c` (I_c) of the ring `ι.obj c`. 

### `IdealFamily.map_eq`

 For every morphism `f : a ⟶ b`, the image of `ideal a` generates `ideal b`. 

### `killingMaps`

 For an ideal I of ι(c), the subfunctor of Hom(c, −) of the morphisms f: c → d such that ι(f)
sends I to zero. 

### `Theory`

 A theory: an `ℓ`-torsion coefficient `F` (the field `functor`) with Zariski descent
(`New.Variety.TorsionCoeff`) that behaves well on closed loci. For an ideal `I` of the ring at `c`,
let `Z ⊆ Hom (c, -)` be the maps that kill `I` (`New.Variety.killingMaps`). Then
`H^n (Hom (c, -), F) → H^n (Z, F)` is onto, and a section of `F` over `c` that dies along `Z`
vanishes near every maximal ideal containing `I`. 

### `Theory.restrict_surjective`

 In every degree `n`, restriction of cohomology from all maps out of `c` to the maps that kill
  the ideal `I` is onto. 

### `Theory.dies_near`

 A section `x` of `F` over `c` that dies along every map killing `I` (hypothesis `h_dies`)
  vanishes near each maximal ideal `m ⊇ I`: for some `a ∉ m`, it dies along every map `c ⟶ d`
  that makes `a` invertible. 

### `IdealFamily.whisker`

 The pull-back of a compatible family of ideals I along a functor φ: C' → C, with ideal
I_{φ(c')} at the object c'. 

### `IdealFamily.botLocus`

 For a compatible family of ideals I, the subfunctor of the one-point functor that is
non-empty exactly at the objects c with I_c = 0. 

### `IdealFamily.topLocus`

 For a compatible family of ideals I, the subfunctor of the one-point functor that is
non-empty exactly at the objects c where I_c is the unit ideal. 

### `IdealFamily.exists_notMem_eq_top`

 Let `I` be a compatible family of ideals of the rings `ι c`, for `ι` a functor on the category
`C`. Off the closed locus of `I c` the family becomes the unit ideal: if `m` does not contain
`I c`, some `a ∉ m` has `I d = ⊤` along every map `c ⟶ d` that inverts `a`. 

### `IdealFamily.zerosCoeff`

 The quotient of G whose value at c is G(c) modulo the sections killed by every map c → d with
I_d = 0. 

### `IdealFamily.toZerosCoeff`

 The quotient morphism from G to `New.Variety.IdealFamily.zerosCoeff`, sending each section to
its class. 

### `IdealFamily.bijective_toZerosCoeff`

 Let `G` be a functor from the category `C` to abelian groups and `I` a family of ideals on `C`.
At an object `d` where the ideal `I.ideal d` is zero, the quotient map from `G d` to
`I.zerosCoeff G d` is bijective: a section that dies along every map to an object where `I` is zero
dies along the identity of `d`. 

### `IsCohomDense.isCohomEquiv_of_bijective_on`

 Let `V` be a subfunctor of the one-point functor that is dense for `F`
(`New.Variety.IsCohomDense`); it picks the objects `c` with `⟨⟩ ∈ V c`. A map `α : M ⟶ N` of
functors to abelian groups that is bijective at each of these objects is an equivalence for `F`:
`Ext^n (N, F) → Ext^n (M, F)` is bijective for all `n`. 

 ### The theory of locally constant functions 

### `TestOver.exists_quotient`

 For an ideal `I` of the ring of a test `B` over `A`, there is a test `D` over `A` with a map
`π : B ⟶ D` such that (a) the ring map of `π` is onto and its kernel is the radical of `I`,
(b) every map out of `B` that kills `I` factors uniquely through `π`, and (c) `π` kills `I`. 

### `exists_locConst_eq_const`

 Let `g` be a functor from a category `C` to tests over `A`, `s` a locally constant function
from Spec of the ring `g(c)` to `ℤ/ℓ`, and `P` a prime of that ring. Then there is `a ∉ P` such that
along every map `c ⟶ d` that makes `a` invertible, `s` becomes the constant function with value
`s P`. 

### `Theory.locallyConstant`

 The theory (`New.Variety.Theory`) on the category of tests over A whose coefficient sends B to
the locally constant functions Spec B → ℤ/ℓ. 

### `oneLocConst`

 The morphism from ℤ[pt], the constant functor ℤ, to the locally constant ℤ/ℓ-valued
functions on Spec g(c), sending the generator to the constant function 1. 

### `TorsionCoeff.onElements`

 For a coefficient M along g and a set-valued functor X on C, the restriction of M to the
category of elements of X along the projection (c, x) ↦ c. 

### `Theory.onElements`

 The restriction of a theory Θ on C to the category of elements of a set-valued functor X on
C, along the projection to C. 

### `Theory.isZariskiLocallyTop_ker_toZerosCoeff`

 Zero sections of the kernel of `I.toZerosCoeff Θ.functor`, together with the objects where `I`
is the unit ideal (the preimage of `I.topLocus` under the map `toUnit _` to the one-point functor),
are locally everything (`New.Variety.IsZariskiLocallyTop`). So if a section `x` of `Θ.functor` over
`c` dies along every map `c ⟶ d` with `I_d = 0`, then each maximal ideal `m` of the ring of `c`
misses some `a` such that every map `c ⟶ d` inverting `a` kills `x` or makes `I_d` the unit
ideal. 

### `Theory.isCohomDense_botLocus`

 Let `Θ` be a theory and `I` a family of ideals on the category `C`. The locus `I.botLocus` of
the objects where `I` is zero is dense for the coefficient `I.zerosCoeff Θ.functor`
(`New.Variety.IsCohomDense`): for every object `c`, restriction from all maps out of `c` to the maps
into that locus is bijective on `Ext^n` for all `n`. 

### `Theory.onZeros`

 The coefficient obtained from the theory Θ by dividing by the sections at c that are killed
by every map c → d with I_d = 0 (`New.Variety.IdealFamily.zerosCoeff`). 

### `TorsionCoeff.nsmul_totalH_eq_zero`

 For a coefficient `M` along `g` (its values are killed by `ℓ`) and a functor `N` from `C` to
abelian groups, `ℓ` kills the total cohomology `TotalH N M.functor`, the sum over `n` of
`Ext^n (N, M.functor)`. 

### `shortExact_nsmul_abCoker`

 For `ℓ ≠ 0` and a functor `N` from `C` to abelian groups with flat values, the sequence
`0 → N → N → N / ℓN → 0` is short exact; its maps are multiplication by `ℓ` and the quotient map
`abCoker.π`. 

### `TorsionCoeff.pullbackAlong_abCoker_pi_surjective`

 For a coefficient `M` along `g` and a functor `N` with flat values, pull-back along the quotient
map `N → N / ℓN` is onto, from the total cohomology of `N / ℓN` to that of `N`, both with
coefficients `M.functor`. 

### `IdealFamily.constToZeros`

 The map from (ℤ[pt]/ℤ[O])/ℓ, O the locus where I is the unit ideal, to locally constant
ℤ/ℓ-valued functions modulo those dying where I = 0, sending the point to 1. 

### `IdealFamily.constToZeros_zsmul_mk`

 The map `New.Variety.IdealFamily.constToZeros` sends the class of `n` times the generator to the
class of the constant function `n`. 

### `IdealFamily.isCohomEquiv_constToZeros`

 Let `g` be a functor from a category `C` to tests over `A`, with a theory `Θ` whose coefficient
is the locally constant `ℤ/ℓ`-valued functions, and `I` a family of ideals of the rings `g(c)`.
Then for every functor `φ : C' ⥤ C` and every coefficient `F'` on `C'` with Zariski descent for the
rings of `φ ⋙ g`, the map `New.Variety.IdealFamily.constToZeros`, restricted along `φ`, is an
equivalence for `F'` (`New.Variety.IsCohomEquiv`). 

### `TorsionCoeff.pullbackAlong_oneLocConst_surjective`

 For a coefficient `M` along `g` (`M.functor` is `ℓ`-torsion with Zariski descent, `ℓ ≠ 0`), let
L(c) be the group of locally constant functions Spec g(c) → ℤ/ℓ, and let `oneLocConst : ℤ → L` send
the generator to the constant function 1. Then pull-back along `oneLocConst`, from total Ext(L,
M.functor) to total Ext(ℤ, M.functor), is surjective. 
