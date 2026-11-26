---
{
  "module": "src/Lib/Cohomology/Hodge/Site.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Cohomology/Hodge/Site.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Cohomology/Hodge/Site.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Hodge cohomology on algebras with free modules; universal points of charts

This file makes the pairs (A, M) of a k-algebra A and a free module M = A^ι
(`New.Variety.HodgeTest`) into a category and defines Hodge cohomology on it. A morphism is a
k-algebra map a together with an a-semilinear map of the modules. A functor of points N on
k-algebras is evaluated on the square-zero extension A ⊕ M, which sees tangent vectors.

* `New.Variety.HodgeTest.sqZeroExt`, `New.Variety.exteriorAlg`: the functors (A, M) ↦ A ⊕ M
  and (A, M) ↦ ⋀_A M.
* `New.Variety.HodgeH`: Hodge cohomology, Ext^q from N(A ⊕ M) to ⋀_A M in functors on pairs, with
  pull-back `New.Variety.HodgeH.map`, scaling `New.Variety.HodgeH.scale` and base change
  `New.Variety.HodgeH.baseChange`.
* `New.Variety.HodgeTest.existsUnique_lift_away`: maps out of (A[1/g], A[1/g]^ι) are the maps
  out of (A, A^ι) that invert g.
* `New.Variety.EtaleChart.univPoint`, `New.Variety.EtaleChart.exists_univPoint`: for a chart with
  ring R and d étale coordinates, the point through which the pair (R, R^d) represents
  (A, M) ↦ Hom(R, A ⊕ M).

Notions from other files:
* `New.Variety.HodgeTest`: a pair (A, M) as above, given by A and a finite ordered index set ι.
* `New.Variety.moduleCoeff`: a functor F from C to k-modules, regarded as a functor to abelian
  groups, so that it can serve as the coefficients of cohomology.
* `New.Variety.Comparison`: a functor φ : C' ⥤ C with a map φ ⋙ F ⟶ F' of coefficients; its `pull`
  along α : N' ⟶ φ ⋙ N maps Ext^n(N, F) to Ext^n(N', F').
* `New.Variety.EtaleChart`: a chart of X: a k-algebra R with finitely many étale coordinates and a
  point y in X(R) that embeds Spec R as an open subfunctor.
* `New.Variety.pointMap`: the map h_A → Y corresponding to a point y of Y(A) by the Yoneda lemma;
  here h_A = `New.Variety.reprBy A` is the functor of maps out of A.

## Relation to the literature

Known; see `Lib.Cohomology.Hodge.FixedPointFormula` for sources.


 ### Semilinear maps on exterior algebras 

### `exteriorMap`

 For a ring map a: T → T' and an a-semilinear map m: M → M', the ring homomorphism ⋀_T M →
⋀_{T'} M' extending a and m. 

### `instance : Category (HodgeTest k)`

 Pairs form a category: a morphism (A, A^ι) → (B, B^κ) is a pair f = ⟨f.1, f.2⟩ of a
k-algebra map f.1 : A → B and an f.1-semilinear map f.2 : A^ι → B^κ. 

### `HodgeTest.comp_snd_apply`

 The semilinear map of a composite of morphisms of pairs is the composite of the semilinear
maps. 

 ### Functors on pairs: square-zero extension and exterior algebra 

### `HodgeTest.withIndex`

 For a finite set ι, the functor A ↦ (A, A^ι) from k-algebras to pairs; an algebra map acts
coordinatewise on A^ι. 

### `semilinearOfBasis`

 For a ring map a: T → T' and vectors v_i in M', the a-semilinear map T^ι → M', (t_i) ↦ Σ
a(t_i) v_i. 

### `HodgeTest.sqZeroExt`

 The functor sending a pair (A, M) to the square-zero extension A ⊕ M, as a k-algebra. 

### `exteriorAlg`

 The functor sending a pair (A, M) to the exterior algebra ⋀_A M, as a k-algebra. 

### `hodgeCoeff`

 The functor (A, M) ↦ ⋀_A M with values in abelian groups: the coefficient of Hodge
cohomology. 

### `_root_.CategoryTheory.Functor.mulPairing`

 For a functor Φ to k-algebras with underlying functor F to abelian groups, the pairing F ⊗ F
→ F given by multiplication. 

### `HodgeTest.formBasis`

 For a test (A, A^ι), the basis of the exterior algebra ⋀_A A^ι over A formed by the wedge
products of standard basis vectors. 

### `exteriorMap_formBasis`

 Let f : P → Q be a morphism of pairs whose semilinear map f.2 sends the i-th standard basis
vector to the (j i)-th one, for an order embedding j. Then the induced map of exterior algebras
sends the basis form of a set s of indices (the wedge of its basis vectors in increasing order) to
the basis form of j(s). 

### `HodgeTest.repr_withIndex_map`

 Let f : A → B be a map of k-algebras and x a form in ⋀_A A^ι. Under the map ⋀_A A^ι → ⋀_B B^ι
induced by f, the coordinate at a set s of indices in the basis of wedge products of standard basis
vectors (`formBasis`) is f applied to the coordinate of x at s. 

### `HodgeTest.baseProj`

 For a pair C = (A, M), the k-algebra projection A ⊕ M → A, (a, m) ↦ a, from the square-zero
extension. 

### `HodgeTest.hom_ext`

 Two morphisms of pairs P → Q are equal if their algebra maps f.1 and g.1 are equal and their
semilinear maps f.2 and g.2 agree on the standard basis vectors of P. 

 ### Hodge cohomology, scaling, localisation and base change 

### `HodgeH`

 Hodge cohomology: for a functor N from k-algebras to abelian groups, Ext^q from (A, M) ↦ N(A
⊕ M) to (A, M) ↦ ⋀_A M, in functors on pairs. 

### `HodgeH.map`

 For α: N' → N, the k-linear pull-back from the degree-q Hodge cohomology of N to that of N'. 

### `HodgeTest.scaleModule`

 For t in k and a functor F on pairs, the natural endomorphism of F induced on each pair (A, M)
by the identity of A and multiplication by t on M. 

### `HodgeH.scale`

 For t ∈ k, the endomorphism of the degree-q Hodge cohomology of N induced by (a, m) ↦ (a, tm) on
A ⊕ M. 

### `HodgeTest.existsUnique_lift_away`

 Objects of `HodgeTest k` are pairs (A, A^ι): a commutative k-algebra A with the free module on a
finite index set ι, and `withIndex ι` sends A to (A, A^ι). Let f : A → B be a map of k-algebras that
is a localisation at the powers of g. Then any morphism of pairs φ : (A, A^ι) → Z whose algebra map
φ.1 sends g to a unit factors uniquely through the morphism (A, A^ι) → (B, B^ι) induced by f. 

### `HodgeTest.baseComparison`

 For an E-algebra k, the comparison from Hodge coefficients over E to those over k, given by
restriction of scalars on pairs and the identity of ⋀_A M. 

### `HodgeH.baseChange`

 Base change: for an E-algebra k, the additive map from the Hodge cohomology over E of N to
that over k of N restricted to k-algebras. 

 ### The universal point of a chart 

### `EtaleChart.existsUnique_univPoint`

 Étale maps lift uniquely along square-zero extensions, so exactly one k-algebra map u :
a.coordRing → a.coordRing ⊕ a.coordRing^d lifts the identity and sends each coordinate x_i to (x_i,
e_i). 

### `EtaleChart.univPoint`

 The universal point of an étale chart a with ring R = a.coordRing and d coordinates x_i: the
k-algebra map u : R → R ⊕ R^d that lifts the identity of R and sends each x_i to (x_i, e_i), where
e_i is the i-th basis vector of R^d. These two conditions determine u. 

### `EtaleChart.bijective_pointMap_univPoint`

 Through the universal point u of a chart with ring R and d coordinates, the pair (R, R^d)
represents c = (A, M) ↦ (k-algebra maps R → A ⊕ M): at each pair c, `pointMap`, which sends a
morphism of pairs f : (R, R^d) → c to u followed by `sqZeroExt.map f`, is a bijection. 

### `EtaleChart.exists_univPoint`

 A chart with ring R and d coordinates has a section u of `fst : R ⊕ R^d → R` through which
(R, R^d) represents (A, M) ↦ (k-algebra maps R → A ⊕ M), namely `EtaleChart.univPoint`. 

### `instance [CharZero k] (F : C ⥤ ModuleCat k) : HasFlatValues (moduleCoeff (k`

 Over a field k of characteristic zero, the values of a functor F to k-vector spaces are flat
as abelian groups: k is flat over ℤ, and every k-vector space is flat over k. 
