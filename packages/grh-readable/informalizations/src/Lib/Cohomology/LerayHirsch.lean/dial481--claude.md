---
{
  "module": "src/Lib/Cohomology/LerayHirsch.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Cohomology/LerayHirsch.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Cohomology/LerayHirsch.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The Leray–Hirsch map as a map of δ-functors, and dévissage from representable functors

A family θ of classes θ_i in Ext^{d_i}(Φ G, F), for an exact functor Φ, defines the Leray–Hirsch map
w ↦ Σ Φ(w_i) · θ_i. The file shows that its bijectivity at S can be proved by dévissage in S.

* `New.Variety.lerayHirsch`, `New.Variety.IsLerayHirschBasis`: the map, from finitely supported
  families in Ext(S, G) to Ext(Φ S, F), and its bijectivity.
* `New.Variety.isLerayHirschBasis_iff_allBijective_truncMap`: it is bijective iff its truncations to
  total degree below n all are.
* `New.Variety.Devissage.allBijective_of_allBijective_sigma_reprBy`: from disjoint unions of
  representable functors to all functors.
* `New.Variety.isLerayHirschBasis_of_reprBy`: from representable functors to all functors, for
  finitely many classes and Φ the restriction along a functor.

Notions from other files:
* `New.Variety.H`: The group Ext^n(N,F) in the category of functors from C to abelian groups;
  `TotalH N F` is their direct sum over n, `x.toTotalH` is x placed in its degree, and
  `mapThenComp Φ t x` is the Yoneda product t ∘ Φ(x).
* `New.Variety.freeAb`: The functor sending a set-valued functor Y to ℤ[Y], whose value at A is the
  free abelian group on Y(A).
* `New.Variety.Devissage`: The five and four lemmas for a family of maps f_{N,n} : A N n → B N n,
  indexed by functors N : D → Ab and degrees n, as for a map of contravariant δ-functors.

## Relation to the literature

Known result: Leray–Hirsch theorem that a local basis of cohomology classes is a global basis. The
theorem is stated abstractly for Ext groups of functors and finitely many classes. It says that if
the Leray–Hirsch map is bijective on ℤ[h_c] for every representable functor h_c, then it is
bijective on every functor. Source: Leray, Hirsch; Hatcher, Algebraic Topology, Thm 4D.1; SGA 5 VII
(projective bundle formula).


 ### The map and its naturality 

### `lerayHirsch`

 For classes θ_i in Ext^{d_i}(ΦG, F), the Leray–Hirsch map w ↦ Σ θ_i∘Φ(w_i) from finitely
supported families in total Ext(S, G) to total Ext(ΦS, F). 

### `IsLerayHirschBasis`

 The Leray–Hirsch property for S: the Leray–Hirsch map `New.Variety.lerayHirsch` of θ at S is
bijective. 

### `lerayHirsch_naturality`

 Additive maps r, r' that intertwine the maps x ↦ Φ(x) · θ_i and x ↦ Φ'(x) · θ'_i for each i
intertwine the two Leray–Hirsch maps. 

### `lerayHirsch_mapRange_comp`

 The Leray–Hirsch map is natural in S for Yoneda products: precomposing each w_i with ξ
corresponds to precomposing the image with Φ(ξ). 

 ### Truncation by total degree 

### `degreeTrunc`

 The truncation of finitely supported families (w_i) in total Ext(S, G) to total degree below
n: in w_i, keep the components of degree e with e + d_i < n. It is a ℤ-linear endomorphism of the
families `I →₀ TotalH S G`. 

### `degreeTrunc_comp_precomp`

 Precomposition with a class ξ of degree e commutes with truncation, up to the shift by e: for
the map `φ` of families `(I →₀ TotalH N F) → (I →₀ TotalH M F)` given by `ξ`, truncating below `n`
and then applying `φ` is applying `φ` and then truncating below `n + e`. 

### `degreeTrunc_comp_lerayHirsch`

 The Leray–Hirsch map commutes with truncation. Its target is viewed as families indexed by one
point, with degree shift 0, so that `New.Variety.degreeTrunc` applies to it: `φ` is the map
`(I →₀ TotalH S G) → (Unit →₀ TotalH (Φ S) F)`. 

### `truncMap`

 For a linear map φ from families `I →₀ TotalH S G` to families `J →₀ TotalH N F`, commuting with
the truncations (below n with shifts d, below m with shifts b) `New.Variety.degreeTrunc`, its
restriction from families of total degree below n to families of total degree below m. 

### `isLerayHirschBasis_iff_allBijective_truncMap`

 The Leray–Hirsch map at S is bijective iff, for every n, its restriction to families of total
degree below n is a bijection onto the classes of degree below n. Here `S`, `G` are functors
`A ⥤ Ab`, `F` is a functor `C ⥤ Ab`, and the classes `θ i` are indexed by a type `I`. 

 ### Long exact sequences of truncated families 

### `truncMap.exact_of_exact`

 If precomposition with ξ and with ζ is exact on total Ext groups, it is exact on the truncated
families. Here `S`, `M`, `N`, `F` are functors `C ⥤ Ab`, and `ξ`, `ζ` are classes of degrees `e`
and `n`. 

### `truncMap.longExact`

 For a short exact sequence X, the long exact sequence whose n-th terms are the finitely
supported families in total Ext(X₃, G), Ext(X₂, G), Ext(X₁, G) of total degree below n; its maps A
n → B n → C n → A (n+1) are precomposition with X.g, with X.f, and with the extension class of X
(degree 1). 

### `lerayHirsch.longExact_hom`

 For a short exact sequence X, the Leray–Hirsch maps of θ, truncated to total degree below n,
form a morphism (the same maps t on all three kinds of terms, commuting with f, g and δ) from the
long exact sequence `New.Variety.truncMap.longExact` of families in Ext(X, G) to that of total
Ext(ΦX, F), truncated likewise. 

### `lerayHirsch.devissage`

 The Leray–Hirsch maps of θ, truncated to total degree below n, satisfy `New.Variety.Devissage`:
the five lemma and the four lemmas hold for them along short exact sequences of functors S. 

### `isClosedClass_isLerayHirschBasis`

 The functors `S` at which `θ` is a Leray–Hirsch basis form a closed class
(`New.Variety.IsClosedClass`): the class contains the zero functors, and along a short exact
sequence whose subobject is in it, the middle term is in it exactly when the quotient is. 

 ### Dévissage from representable functors 

### `Devissage.allBijective_of_allBijective_sigma_reprBy`

 Dévissage. Let f(S, n) be maps with the five- and four-lemma properties `New.Variety.Devissage`.
If f(S, n) is bijective for all n whenever S = ℤ[Y] with Y a disjoint union of representable
functors, then f(S, n) is bijective for every S and n. 

### `isLerayHirschBasis_of_reprBy`

 Let θ be a finite family of classes in Ext(G∘φ, F), for a functor φ. If the Leray–Hirsch map
`New.Variety.lerayHirsch` is bijective at ℤ[h_c], the free abelian functor on h_c = Hom(c, −), for
every object c of the target of φ, it is bijective at every S. Here `S`, `G` are functors `A ⥤ Ab`,
`F` is a functor `C ⥤ Ab`, and `I` is the finite index type of the classes. 
