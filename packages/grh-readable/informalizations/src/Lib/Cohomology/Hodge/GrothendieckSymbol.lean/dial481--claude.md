---
{
  "module": "src/Lib/Cohomology/Hodge/GrothendieckSymbol.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Cohomology/Hodge/GrothendieckSymbol.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Cohomology/Hodge/GrothendieckSymbol.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Grothendieck's symbol [dT/T], cut-out loci and Hodge classes of points

Let `k` be a field (of characteristic zero for `symbolClass_succ`). Spaces are functors `X` from
`k`-algebras to sets. `New.Variety.HodgeH (relFreeAb U) d` is the Hodge cohomology of `X` relative
to a subfunctor `U`, and `New.Variety.offPoints s` is the complement of a set `s` of `k`-points;
`ComesFromPoints s K x` says that `x ∈ X(K)` is the image of some `z ∈ s`. Grothendieck's symbol
`New.Variety.symbolClass` is a class in the Hodge cohomology of affine d-space relative to the
complement of the origin. `[dg / g]` denotes its pull-back along a tuple of functions `g`.

## Main definitions and results

* `New.Variety.CutsOutLocus X P x f` says that the elements `f i` of `R` cut out the locus of
  `Spec R` where the point `x` of `X(R)` satisfies `P`.
* `New.Variety.symbolClass`: the class, given by the cocycle (v, l_1, …, l_d) ↦ det(l) · dT(v).
* `New.Variety.symbolClass_transformation`: the transformation law between the pull-backs along two
  tuples.
* `New.Variety.symbolClass_succ`: the class in degree d + 1 restricts to the product of the classes
  in degrees d and 1.
* `New.Variety.IsPointSum`: near each `z ∈ s`, a relative class is `n z • [dg / g]` for functions
  `g` that cut out `z`; `New.Variety.pointClass` is the image of a chosen class of multiplicity `1`.
* `New.Variety.IsPointSum.map_eq_smul_pointClass`, `New.Variety.IsPointSum.map_eq_sum_pointClass`:
  on a separated `X`, a class with support in a finite set `s` and multiplicities `n` maps to
  `∑ z ∈ s, n z • pointClass d z`. The proof is by excision for one point and by Mayer–Vietoris for
  several.

Notions from other files:
* `New.Variety.unimodular`: The subfunctor of affine d-space of vectors whose entries generate the
  unit ideal.
* `New.Variety.pointMap`: The map Hom(A, −) → Y given by a point y of Y(A) (Yoneda).
* `New.Variety.IsSeparatedFunctor`: X is separated: for x, y in X(A) there is an ideal J of A such
  that φ: A → B makes x and y equal exactly when φ kills J.
* `New.Variety.HodgeTest`: a test for Hodge cohomology over k, namely a commutative k-algebra A and
  a finite index set ι, standing for the pair (A, M) with M = A^ι.
* `New.Variety.HodgeTest.sqZeroExt`: The functor sending a pair (A, M) to the square-zero extension
  A ⊕ M, as a k-algebra.
* `New.Variety.hodgeCoeff`: The functor (A, M) ↦ ⋀_A M to abelian groups, the coefficients.
* `New.Variety.EtaleChart`: A chart of X: a k-algebra R with finitely many étale coordinates and a
  point of X(R) that embeds Spec R as an open subfunctor (its image is `a.locus`).
* `New.Variety.HodgeH`: Hodge cohomology: for a functor N from k-algebras to abelian groups, Ext^q
  from (A, M) ↦ N(A ⊕ M) to (A, M) ↦ ⋀_A M, in functors on pairs.

## Relation to the literature

Known; see `Lib.Cohomology.Hodge.FixedPointFormula` and
`Lib.Cohomology.PointClass.LinearIndependence` for sources.



## Functions cutting out a locus of points, and its complement

* `New.Variety.CutsOutLocus.preimage_fieldLocus_not`: the locus where `P` fails at every field point
  pulls back to the locus where `g` is a unimodular vector.


### `eq_comp_structureMap_of_ker_le`

 Let `ζ : R ⟶ k` be a `k`-point of `Spec R` and `φ : R ⟶ K` a map of `k`-algebras. If the
kernel of `ζ` lies in the kernel of `φ`, then `φ` is `ζ` followed by the structure map `k ⟶ K`. 

### `CutsOutLocus`

 The elements `f i` of `R` cut out the locus where the point `x` of `X(R)` satisfies `P`: a map
`α : R ⟶ C` kills every `f i` exactly when the image of `x` in `X(C)` satisfies `P`. 

### `mem_offPoints_iff`

 Let `X` be separated, `K` a field and `s` a set of `k`-points of `X`. A point `x` of `X(K)`
lies in `offPoints s`, the points none of whose images in fields comes from `s`, exactly when `x`
itself is not the image of a point of `s`. 

### `CutsOutLocus.preimage_fieldLocus_not`

 If `g` cuts out the locus where `x` satisfies `P`, then the preimage in `Spec R` of the locus
where `P` fails at every field point is the locus where the `g i` generate the unit ideal. 


## Grothendieck's symbol [dT/T] and its product formula

A point v of (A ⊕ M)^d off the origin has a witness: a linear form l ∈ A^d with value 1 on the
A-part of v (`New.Variety.jouanolouRel`). Points with several witnesses turn cocycles into relative
classes. The cocycle condition and the product formula are Laplace expansions
(`New.Variety.sum_minor_eq_mul_det`).

* `New.Variety.symbolClass_one`: in degree 1 the class is the boundary of dT/T.


 ### Witnesses and the cocycle of the symbol 

### `jouanolouRel`

 For f from V to d-tuples in A ⊕ M, the subfunctor of pairs (v, l), l ∈ A^d, with l · f̄(v) = 1,
where f̄ is the A-component of f. The second factor is the functor (A, M) ↦ A^d. 

### `exists_jouanolouRel_of_unimodular`

 A unimodular tuple v in A ⊕ M has a witness: some l ∈ A^d (a point of affine d-space over A)
has dot product 1 with the A-part of v. Here A ⊕ M is the square-zero extension of the test `c`. 

### `instance : Module c.baseAlg (hodgeCoeff.obj c)`

 The exterior algebra ⋀_A M of a test c = (A, M) as a module over A. 

### `detCochain`

 The map (v, l_1, …, l_d) ↦ det(l_1, …, l_d)·ω(v) from the free abelian group on points v with d
witnesses l_i ∈ A^d, that is, (v, l_i) ∈ R for each i (the functor `witnessed R d`), to ⋀_A M. 

### `sum_minor_eq_mul_det`

 If every row of t has dot product 1 with f, then the signed sum over j of the minors of t
without row j and column i is f i · det t. 

### `detCocycle`

 The map (v, l_1, …, l_d) ↦ det(l_1, …, l_d)·ω(v), on points with d witnesses for
`New.Variety.jouanolouRel` f, kills boundaries. This is the induced map on the cokernel. 

### `volumeForm`

 The natural map from the free abelian group on (A⊕M)^d to ⋀_A M sending a tuple (a_i,m_i) to
m_1∧…∧m_d. 

### `symbolClass`

 The class [dT/T], in the Hodge cohomology of degree d of 𝔸^d relative to 𝔸^d ∖ 0, of the
cocycle det(l_1, …, l_d)·dT_1 ∧ … ∧ dT_d on tuples of linear forms with l_j(T) = 1. 

### `IsInducedByCoords`

 For v ∈ A^d and a d-tuple f in A ⊕ A^ι, the map α of relative chains, defined relative to the
locus where some v i becomes a unit, sends each point σ of Hom(c, −) to the tuple σ f. 

### `unimodularLocus`

 For a test c = (A, A^ι) and a d-tuple g in A ⊕ A^ι, the subfunctor of Hom(c, −) of the maps
that make g unimodular. 

### `someUnitLocus_le_unimodularLocus`

 If v = M ḡ, a map that makes some v i a unit makes g unimodular. 

### `grothendieckSymbol`

 The symbol [η/ḡ] of a d-tuple g = (ḡ, η) in A ⊕ A^ι: the pull-back of [dT/T] along g, in the
cohomology of Hom(c, −) relative to a subfunctor U (`H N F d` is Ext^d from N to F in functors on
tests) on which g is unimodular. 

### `exists_jouanolouRel_of_le_unimodularLocus`

 On U, where f is unimodular, every point σ has a linear form l ∈ A^d with value 1 at σ f. 

### `formOfExteriorPower`

 A d-form x on A^ι, as the map σ ↦ σ x from Hom(c, −) to forms. 

### `fractionClass`

 The generalized fraction [x/f̄] of a d-form x: the class, relative to a subfunctor U on which
f is unimodular, of the cocycle (σ, l) ↦ det l • σ x, where the l j take the value 1 at σ f̄. 

### `smul_grothendieckSymbol_eq_fractionClass`

 For a test c = (A, A^ι), let `f` and `g` be d-tuples in A ⊕ A^ι with first components
f̄ = `fst ∘ f` and ḡ, and write g = (ḡ, η). Let `U` be a subfunctor of Hom(c, −) on which both `f`
and `g` are unimodular, and suppose f̄ = M ḡ for a d × d matrix `M` over A. Then for every a ∈ k,
the scaled Grothendieck symbol a • [η/ḡ] equals the generalized fraction
[a det M · η₁ ∧ ⋯ ∧ η_d / f̄], both taken in the cohomology of Hom(c, −) relative to `U`. 

### `fractionClass_smul_eq_zero`

 The fraction [x/f̄] vanishes when the coefficient of x lies in the ideal spanned by f̄. 

### `grothendieckSymbol_transformation`

 Transformation law for Grothendieck symbols. Let f = (f̄, ω) and g = (ḡ, η) be d-tuples in
A ⊕ A^ι, unimodular on U, and I the ideal spanned by f̄. If f̄ = M ḡ, ω ≡ N η modulo I
coordinatewise and det N ≡ a det M modulo I with a ∈ k, then [ω/f̄] = a [η/ḡ]. 

### `IsInducedByCoords.map_symbolClass`

 A map of relative chains induced by the tuple f = (f̄, ω) pulls [dT/T] back to [ω/f̄]. 

 ### Transformation law 

### `symbolClass_transformation`

 Transformation law for Grothendieck symbols, for maps α and β of relative chains induced by
f = (f̄, ω) and g = (ḡ, η). Let v = f̄ and let I be the ideal spanned by v. If v = M ḡ, ω ≡ N η
modulo I coordinatewise and det N ≡ a det M modulo I with a ∈ k, then the pull-back of [dT/T]
along α is a times its pull-back along β. 

 ### Product formula 

### `symbolClass_one`

 In degree 1 the symbol is a boundary: there is a form ω on the complement of the origin in 𝔸^1
with (a) ω(a + m) = w for some w with a w = m, that is ω = dT/T, and (b) `New.Variety.symbolClass`
of degree 1 is the image of ω under the connecting map of 0 → ℤ[𝔸^1 ∖ 0] → ℤ[𝔸^1] → ℤ[𝔸^1]/ℤ[𝔸^1 ∖
0] → 0. 

### `affineSpace.snoc`

 The natural map 𝔸^d × 𝔸^1 → 𝔸^{d+1} appending a last coordinate. 

### `unimodularSup`

 The subfunctor of 𝔸^d × 𝔸^1 of the pairs (v, x) in which v or x is unimodular, that is, has
entries that generate the unit ideal. 

### `unimodularSup_le_preimage_snoc`

 If v or x is unimodular, then so is the tuple (v, x) ∈ 𝔸^(d+1) obtained by appending x to v:
the entries of v, and the entry of x, are among its entries. 

### `snocRel`

 For a test (A, M) and a pair (v, x) ∈ 𝔸^d × 𝔸^1 with entries in A ⊕ M, the subfunctor of the
pairs ((v, x), l) in which l ∈ A^(d+1) has dot product 1 with the A-part of the tuple (v, x) and
the last entry of l is 0 unless x is unimodular. 

### `exists_snocRel`

 Every pair x = (v, x₁) over a test c = (A, M) in which v or x₁ is unimodular has a witness
l ∈ A^(d+1) for `snocRel`: a witness of v followed by 0 if v is unimodular, a witness of the tuple
(v, x₁) if x₁ is. 

### `relFreeAb.tmul_mk_congr`

 Let V be a functor from tests to sets, G a subfunctor, x a point of V over the test c, and [x]
its class in ℤ[V]/ℤ[G]. For a and b in an abelian group B, a ⊗ [x] = b ⊗ [x] as soon as x ∉ G
implies a = b, since [x] = 0 when x ∈ G. 

### `snocRel.firstPoint`

 The first d coordinates v of a point (v, x) ∈ 𝔸^d × 𝔸^1 with m witnesses for `snocRel`. 

### `snocRel.lastPoint`

 The last coordinate x of a point (v, x) ∈ 𝔸^d × 𝔸^1 with m witnesses for `snocRel`. 

### `snocRel.dropLast`

 Let t be a point (v, x) with m witnesses for `snocRel`. If x is not unimodular, the last entry
of each witness is 0, and dropping it gives m witnesses for v. 

### `snocRel.split`

 The map of chains that sends a point (v, x) with m witnesses l for `snocRel` to
(v, init l) ⊗ [x], where init l drops the last entry of each witness and [x] is the class of x in
ℤ[𝔸^1]/ℤ[unimodular points]. It is 0 when x is unimodular. 

### `snocRel.reindexWitness_comp_split`

 The maps `snocRel.split` commute with reindexing the witnesses along g : Fin m → Fin n. 

### `snocRel.detTensor`

 The cochain on points (v, x) with d witnesses l for `snocRel` that sends ((v, x), l) to
((-1)^d det(init l) · dT(v)) ⊗ [x]. Here init l drops the last entry of each witness, dT(v) is
`New.Variety.volumeForm` at v, and [x] is the generator of ℤ[𝔸^1] at x. 

### `snocRel.exists_detTensor_boundary_eq`

 Work over tests `(A, M)` and let ω be a form on the unimodular points x = a + m of 𝔸^1 with
ω(x) = w for some w with a • w = m, that is, the form dT/T. Let t be a point (v, x) ∈ 𝔸^d × 𝔸^1
with d + 1 witnesses l for `snocRel`: each l ∈ A^(d+1) has dot product 1 with the A-part of (v, x),
and its last entry is 0 unless x is unimodular. Apply `detTensor`, the cochain
((v, x), l) ↦ ((-1)^d det(init l) · dT(v)) ⊗ [x], to the boundary of t, the alternating sum over
dropping one witness. The result is the image of a tensor s in ⋀_A M ⊗ ℤ[unimodular points of 𝔸^1],
and applying ω to the second factor of s and multiplying in ⋀_A M gives det l · dT(v, x), with dT
the `volumeForm` on 𝔸^(d+1). 

### `symbolClass_succ`

 The symbol is multiplicative. On 𝔸^d × 𝔸^1, relative to the pairs (v, x) with v or x
unimodular, the product of [dT/T] in degrees d and 1 is the restriction of [dT/T] in degree
d + 1. 

### `map_cup_symbolClass_eq_map_symbolClass`

 The product formula in natural form: restricted to the pairs (v, x) with v or x unimodular,
the cup product of [dT/T] in degrees d and 1 is the pull-back of [dT/T] in degree d + 1 along
the map (v, x) ↦ (v, x) ∈ 𝔸^(d+1). 

 ## Point classes, excision and classes supported at finitely many points 

 ### Symbols on a chart and excision 

### `EtaleChart.exists_section_isCohomEquiv`

 Let `a` be a chart with ring `R` and `e` coordinates. Some ring map `μ : R → R ⊕ R ^ e` is a
section of the projection such that, for `f ∈ R ^ d` and `S` the locus of `Spec R` where `f` spans
the unit ideal, `μ` maps the test `(R, R ^ e)` relative to `someUnitLocus f` (where some `f i` is a
unit) into `Spec R` relative to `S`, by an inclusion `h`, bijectively on Hodge cohomology in all
degrees. 

### `EtaleChart.symbolClass_eq_of_cutsOutLocus`

 On a chart `a` of `X`, let `x` be a point of a functor `X'` with values in the coordinate ring,
and let `P` be a property of points of `X'`. Suppose two `d`-tuples `f`, `g` of functions both cut
out the locus where `x` satisfies `P`, meaning an algebra map kills all their entries exactly when
the image of `x` satisfies `P`. Then they have the same symbol, `[df / f] = [dg / g]`, relative to
the preimage of the complement of that locus. 

### `hodge_excision`

 Excision. Let `u : X' ⟶ X` be injective on points with open image, and let every point in a
field outside the image lie in an open subfunctor contained in `U`. Then pull-back along `u`
is bijective from the Hodge cohomology of `(X, U)` to that of `(X', u⁻¹ U)` in all degrees. 

### `HodgeH.map_comp`

 Pulling a Hodge class back along α ≫ β is pulling it back along β, then along α. 

 ### Local multiplicities and the class of a point 

### `IsLocalSymbol`

 Let `y ∈ X(R)` be a point, `P` a locus of `X`, and `g ∈ R ^ d` functions. Then
`IsLocalSymbol ξ y P g m` says three things. First, `g` cuts out `P` at `y`. Second, the point `y`
maps the part of `Spec R` off the preimage of `P` into `U`. Third, the pull-back of `ξ` along `y` is
`m • [dg / g]` in the Hodge cohomology of `Spec R` relative to that part. 

### `IsLocalSymbol.map`

 A local description `m • [dg / g]` at `y` is preserved by a ring map `φ : R ⟶ R'`. 

### `IsPointSum`

 The relative class `ξ` has multiplicity `n z` at each `z ∈ s`: some chart contains `z`,
some `d` functions `g` on it cut out `z`, and there `ξ` restricts to `n z • [dg / g]`
relative to the complement of `z`. Nothing is asked of `ξ` away from `s`. 

### `pointClass`

 The class of a `k`-point `z` in the Hodge cohomology of degree `d`: the image of a chosen
class with support `z` and multiplicity `1` at `z`; if there is no such class, the image of
an arbitrary class with support `z`. 

### `exists_isOpenSubfunctor_le_offPoints`

 Let X be separated and z a k-point of X that lies in U. A point x of X over a field K that is
not in U lies in an open subfunctor contained in the complement of z, namely that complement. 

### `EtaleChart.exists_isLocalSymbol`

 Let `X` be separated, `a` a chart of dimension `e` that contains `z`, and `g` functions on `a`
that cut out `z`. Some class with support `z` restricts to `[dg / g]` on `a`, and so has
multiplicity `1` at `z`. 

### `IsPointSum.map_eq_smul_pointClass`

 On a separated `X`, a class with support `z` and multiplicity `n z` at `z` maps to
`n z • pointClass d z` in the Hodge cohomology of `X`. 

### `IsPointSum.map_eq_pointClass`

 On a separated `X`, every class with support `z` and multiplicity `1` at `z` maps to
`pointClass d z`. So `pointClass d z` does not depend on the choice made in its definition. 

### `IsPointSum.map_eq_sum_pointClass`

 On a separated `X`, a class with support in a finite set `s` of `k`-points and
multiplicities `n` maps to `∑ z ∈ s, n z • pointClass d z` in the Hodge cohomology of `X`. 
