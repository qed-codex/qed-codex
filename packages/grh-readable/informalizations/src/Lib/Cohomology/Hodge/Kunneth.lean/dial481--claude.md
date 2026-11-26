---
{
  "module": "src/Lib/Cohomology/Hodge/Kunneth.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Cohomology/Hodge/Kunneth.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Cohomology/Hodge/Kunneth.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Künneth formula: Hodge classes on X × X are sums of external products

The Künneth formula for Hodge cohomology `New.Variety.HodgeH`, in the weak form that the fixed-point
formula needs: cross products span.

* `New.Variety.kunneth`: over a field of characteristic 0, if `X` has an atlas, every class on
  `X × X` is a sum of cross products of classes on `X`.

Hodge cohomology is an Ext group in functors on pairs `(A, M)`, where `M` is a finite free
`A`-module (`New.Variety.HodgeTest`). It is taken from `(A, M) ↦ ℤ[X(A ⊕ M)]` to the exterior
algebra `(A, M) ↦ ⋀ M` (`New.Variety.hodgeCoeff`).

The proof first treats a product of two represented functors through the Leray–Hirsch map. It then
passes to the general case by dévissage in each factor.

Notions from other files:
* `CategoryTheory.Functor.mulPairing`: For a functor Φ to k-algebras with underlying functor F to
  abelian groups, the pairing F ⊗ F → F given by multiplication.
* `New.Variety.exteriorAlg`: The functor sending a pair (A, M) to the exterior algebra ⋀_A M, as a
  k-algebra.
* `New.Variety.lerayHirsch`: For an exact functor Φ and classes θ_i in Ext^{d_i}(ΦG, F), the map
  w ↦ Σ θ_i∘Φ(w_i) from finitely supported families in total Ext(S, G) to total Ext(ΦS, F).
* `New.Variety.freeAb`: The functor sending a set-valued functor Y to Z[Y], whose value at A is the
  free abelian group on Y(A).
* `New.Variety.abTensor`: The pointwise tensor product over ℤ of two functors from C to abelian
  groups, as a bifunctor.
* `New.Variety.H`, `New.Variety.TotalH`: The group Ext^n(N, F) in functors to abelian groups, and
  the direct sum of these groups over n.

## Relation to the literature

Known; see `Lib.Cohomology.Hodge.FixedPointFormula` for sources.


### `formCoord`

 Coordinates for the classes on the functor represented by a test `a`: they all have degree `0`
and are the forms on `a` (`New.Variety.TotalH.sectionEquiv`), here written in the basis
`a.formBasis` of the forms, reindexed by `g` and with its vectors multiplied by the signs `η`. 

### `formTensor`

 For a basis `b` over `k` of the forms on a test `c`, the `k`-linear isomorphism from families,
indexed by `b`, of families of elements of the ring `A'` of `c'` indexed by subsets of the index set
of `c'`, to families of elements of `A' ⊗ A` indexed by pairs of subsets: each vector of `b` is
expanded in the basis `c.formBasis` of the forms on `c`, over the ring `A` of `c`, indexed by
subsets of the index set of `c`. 

### `pullbackAlong_cross_sectionEquiv`

 The cross product of two forms is their product. Let `l : c' ⟶ p` and `q : c ⟶ p` be maps of
tests, `x` a form on `c'` and `y` a form on `c`, read as classes of degree `0` on the represented
functors (`sectionEquiv`). The product of these classes, pulled back to `ℤ[h_p]` along the point
`(l, q)` of `h_c' × h_c`, is the class of the product of the images of `x` and `y` on `p`. 

### `exists_basis_forms_lerayHirsch`

 Some basis `b` over `k` of the forms on a test `c = (A, I)` (the exterior algebra `⋀_A A^I`) has
the Leray–Hirsch property: for every test `c'`, the Leray–Hirsch map for `Φ = – ⊗ ℤ[h_c]` and the
classes `θ j` (the product with the form `b j`, read as a class of degree `0` on `h_c`) is bijective
at `ℤ[h_c']`. So the products with the `b j` give all classes on the product of the functors `h_c'`
and `h_c` represented by `c'` and `c`, each in one way. 

### `cross_comp_eq_comp_cross`

 Moving an endomorphism `ρ` of the coefficients across a cross product. Let `μ : F ⊗ F → F` be a
pairing for which `ρ` on the second factor has the same effect as `ρ` on the first. Then the product
of a class `x` on `N` with `g = f ≫ ρ` is the product of `x` pushed along `ρ` with `f`. The left
side is written through the functor `N ⊗ –` and the right side through `– ⊗ M`. 

### `bijective_lerayHirsch_reprBy`

 The first factor of the Künneth formula, for a represented second factor. Let `N` be a functor
that lies in every closed class (`New.Variety.IsClosedClass`) containing the represented functors
(`h_devissage`), and let `θ` be the products with a basis of the classes of each degree on `N`.
Then the Leray–Hirsch map of `θ` for `Φ = N ⊗ –` is bijective at every represented functor. 

### `kunneth`

 Künneth: over a field `k` of characteristic `0`, if `X` has an atlas of dimension `d`
(`HasAtlas`: it yields a subfunctor that is locally all of `X` and is built from charts represented
on `HodgeTest k`), every class `z` in `HodgeH` of degree `n` on `X × X` is a finite sum of cross
products `x × y` of Hodge classes on `X` of degrees `a` and `b` with `b + a = n`. The cross product
is the cup product `cup` for the multiplication of exterior algebras, pulled back along
`ℤ[X × X] → ℤ[X] ⊗ ℤ[X]` (`New.Variety.freeAb.prod`). 
