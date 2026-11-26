---
{
  "module": "src/Lib/Cohomology/Hodge/CupProduct.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Cohomology/Hodge/CupProduct.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Cohomology/Hodge/CupProduct.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Pointwise tensor product of functors, total Ext with Yoneda composition, external products

Products in the cohomology `New.Variety.H N F n = Ext^n(N, F)` of functors from `C` to abelian
groups (`New.Variety.AbFunctor C`).

* `New.Variety.abTensor`, `New.Variety.HasFlatValues`: the pointwise tensor product, exact for flat
  values.
* `New.Variety.TotalH`: the direct sum of all `Ext^n(N, F)`, with the Yoneda product
  `New.Variety.TotalH.comp` and the action `New.Variety.TotalH.map` of exact functors
  (`IsExactFunctor`: sending exact sequences to exact sequences). Pull-back and push-forward become
  products with classes of degree zero, so degrees need no tracking.
* `New.Variety.TotalH.exact_triangle`: the long exact sequence, as an exact triangle.
* `New.Variety.cup`: the external product, natural in the spaces (`New.Variety.cup_map`) and in the
  site (`New.Variety.Comparison.pull_cup`).

`comp x y` is written in diagram order: `x` in `TotalH M N`, `y` in `TotalH N F`.

Notions from other files:
* `New.Variety.H.map`, `New.Variety.H.push`: the maps Ext^n(N,F) → Ext^n(N',F) and
  Ext^n(N,F) → Ext^n(N,F') given by α: N' → N and β: F → F'.
* `New.Variety.Comparison`: a comparison from F on C to F' on C' is a functor φ: C' → C with a
  natural transformation β: F∘φ → F' (the field `coeffHom`).
* `New.Variety.Comparison.pull`: for a comparison (φ,β) and α: N' → N∘φ, the homomorphism
  Ext^n(N,F) → Ext^n(N',F') obtained by restricting along φ, pushing by β and pulling by α.
* `New.Variety.restrictAlong`: for a functor φ: C' → C and a category D, the functor N ↦ N∘φ from
  functors C → D to functors C' → D.

## Relation to the literature

Known; see `Lib.Cohomology.Hodge.FixedPointFormula` for sources.


 ### The pointwise tensor product and flat functors 

### `abTensorMap`

 For homomorphisms f: A → A' and g: B → B' of abelian groups, the homomorphism f ⊗ g: A ⊗ B →
A' ⊗ B' of tensor products over ℤ. 

### `abTensor`

 The pointwise tensor product over ℤ of two functors from C to abelian groups, as a
bifunctor. 

### `abTensor_hom_ext`

 Two maps out of a pointwise tensor product `F ⊗ G` are equal if at each object `c` they agree
on the pure tensors `a ⊗ b`. 

### `HasFlatValues`

 Every value F(c) of the functor F from C to abelian groups is a flat ℤ-module. 

### `HasFlatValues.flat`

 Each value of `F` is a flat `ℤ`-module. 

 ### Total cohomology and the Yoneda product 

### `H.add`

 The sum `x + y` of two classes in `Ext^a(N, F)`, as a named constant for
`New.Variety.addCommGroupH`. 

### `addCommGroupH`

 The abelian group structure of `Ext^a(N, F)`, equal to Mathlib's by definition. The addition is
written through `New.Variety.H.add` for elaboration only: without the named constant,
definitional equality checks on sums of classes time out in later files. 

### `TotalH`

 The total Ext group, the direct sum of the Ext^n(N,F) over all n ≥ 0. 

### `TotalH.comp`

 The biadditive map from total `Ext(M, N)` and total `Ext(N, F)` to total `Ext(M, F)` that
extends the Yoneda composition of homogeneous classes. The `choose` makes no real choice: it only
keeps the formula from unfolding. See `TotalH.comp_def` and `TotalH.comp_of`. 

### `TotalH.comp_def`

 `comp` is the biadditive extension to the direct sums of the Yoneda compositions
`Ext^a(M, N) × Ext^b(N, F) → Ext^(a + b)(M, F)`. 

### `TotalH.comp_of`

 On homogeneous classes `comp` is the Yoneda composition. 

### `_root_.CategoryTheory.Abelian.Ext.toTotalH`

 A class x in Ext^n(N,F), as the element of the total group ⊕_m Ext^m(N,F) concentrated in
degree n. 

### `map`

 For an exact functor `Φ`, the additive map from total `Ext(N, F)` to total `Ext(Φ N, Φ F)`
obtained by applying `Φ` in each degree. See `TotalH.map_def` and `TotalH.map_of`. 

### `map_def`

 `map Φ` is the direct sum of the maps induced by `Φ` on `Ext` in each degree. 

### `mapThenComp`

 For an exact functor Φ and u in total Ext(ΦF,K), the additive map x ↦ Φx·u (Yoneda product)
from total Ext(N,F) to total Ext(ΦN,K). 

### `homClass`

 A morphism f: N → F as a degree-zero element of total Ext(N,F). 

### `pullbackAlong`

 For f: N → F, the additive map from total Ext(F,G) to total Ext(N,G) given by precomposition
with f. 

### `map_of`

 On a homogeneous class `map Φ` is the image of the class under `Φ`. 

### `map_pullbackAlong`

 An exact functor commutes with the pull-back along a morphism `f`. 

### `homClass_comp`

 The class of a composite `f ≫ g` is the Yoneda product of the classes. 

### `map_extClass`

 An exact functor sends the extension class of a short exact sequence `S` to the extension class
of the image sequence. 

### `pullbackAlong_of`

 Pulling a homogeneous class back along `f` is `New.Variety.H.map` in its degree. 

### `of_comp_homClass`

 Composing a homogeneous class with the class of `f` is the push-forward along `f` in its
degree. 

### `pullbackAlong_eq_map`

 Pulling back along `f` is `New.Variety.H.map` in every degree. 

### `naturality`

 For a natural transformation `η : Φ ⟶ Ψ` of exact functors, pushing `Φ x` along `η F` equals
pulling `Ψ x` back along `η N`. 

### `smul_eq_comp`

 The action of a scalar `r` of `R` on the coefficients `F` (`CoeffAction R F` gives each `r` an
endomorphism `CoeffAction.act r` of `F`) is the product with the class of its action map. 

### `comp_smul`

 The Yoneda product is linear in the second factor over the scalars acting on `F`. 

 ### Reassociated forms 

### `comp_assoc_of_eq`

 Associativity, with the product `comp x y` given by an equation `h`. 

### `pullbackAlong_pullbackAlong`

 Pulling back along `g` and then along `f` is pulling back along `f ≫ g`. 

### `map_comp_assoc`

 An exact functor Φ respects Yoneda products: Φ(x·y)·u = Φx·(Φy·u) in total Ext. 

### `mapThenComp_comp`

 `New.Variety.TotalH.mapThenComp` of a product `comp x y`, with `map Φ x` given by an
equation `h`. 

### `comp_assoc_of_sq`

 If `comp x y = comp z w`, then the same holds after a product with any `u` on the right. 

 ### The exact triangle and representable functors 

### `exact_precomp`

 Exactness on total classes is tested degree by degree. Let `ξ` be a class in `Ext^e(M, N)` and
`ζ` a class in `Ext^b(G, M)` with `ζ · ξ = 0`, and suppose that every homogeneous class `y` in
`Ext(M, F)` with `ζ · y = 0` is zero or of the form `ξ · x`. Then composition with `ξ` followed by
composition with `ζ` is exact at total `Ext(M, F)`. 

### `exact_triangle`

 The long exact sequence of a short exact sequence `S` in the first variable, as an exact
triangle of total groups: pull-back along `S.g`, pull-back along `S.f` and composition with the
extension class are exact at each of the three vertices. 

### `bijective_directSum_of_zero_reprBy`

 The cohomology Ext(`freeAb (reprBy c)`, G) of the free abelian functor ℤ[Hom(c, −)] on a
representable functor is concentrated in degree zero. 

### `sectionEquiv`

 The Yoneda isomorphism from G(c) to the total Ext(ℤ[h_c], G), which is concentrated in
degree 0; here h_c = Hom(c, −). 

### `IsCohomEquiv.bijective_pullbackAlong`

 A cohomological equivalence `f` (each pull-back `H.map G f n` is bijective) gives a bijection on
total cohomology with coefficients in `G`. 

 ### External products 

### `TotalH.cup`

 For x in total Ext(M,F), y in total Ext(N,G), with M, G of flat values, the Yoneda composite
of M ⊗ y and x ⊗ G in total Ext(M ⊗ N, F ⊗ G). 

### `TotalH.cup_comp_homClass_left`

 Pushing the first factor along `β` pushes the external product along `β ⊗ G`. 

### `TotalH.cup_comp_homClass_right`

 Pushing the second factor along `γ` pushes the external product along `F ⊗ γ`. 

### `cup`

 For x in Ext^a(M,F), y in Ext^b(N,G), M and G of flat values, the product in Ext^{a+b}(M ⊗
N, K): their external product pushed along μ: F ⊗ G → K. 

### `TotalH.cup_of`

 On homogeneous classes, the external product of total classes followed by `μ` is
`New.Variety.cup`. 

### `cup_map`

 The product `New.Variety.cup` is natural in both spaces. Here `H N F n` is `Ext^n(N, F)` for
functors from `C` to abelian groups, `⊗` is their pointwise tensor product `abTensor`, and `H.map`
is the pull-back of classes along a morphism. Let `x ∈ Ext^a(M, F)` and `y ∈ Ext^b(N, G)` with
`b + a = n`, let `μ : F ⊗ G ⟶ K`, and let `M`, `M'`, `G` have flat values. Let `α : M' ⟶ M` and
`β : N' ⟶ N`, and let `γ : L ⟶ M ⊗ N` be `γ' : L ⟶ M' ⊗ N'` followed by `α ⊗ β` (`h`). Then in
`Ext^n(L, K)` the pull-back along `γ` of the product of `x` and `y` is the pull-back along `γ'` of
the product of `α^* x` and `β^* y`. 

### `TotalH.pull_twist`

 Let y be the pull-back of a class x along a comparison c = (ψ, β) and A: N' → N∘ψ. Let φ be an
endofunctor of C', with s: F' → F'∘φ and α: N' → N'∘φ. If σ: ψ → ψ∘φ satisfies βφ∘Fσ = s∘β and
Aφ∘α = Nσ∘A, then restricting y along φ and pulling back along α gives the push-forward s_*y in
total Ext. 

### `Comparison.pull_comp_restrictAlong`

 For `x` in Ext^b(N ∘ Θ, F), pulling back along `c` and `η` commutes in total Ext with composing
by `ξ` in Ext^a(N', N) on `A`, restricted along `Θ` before and along `Θ'` after the pull-back. 

### `Comparison.pull_cup`

 Let `c` be a comparison from `F` on `C` to `F'` on `C'`, let `η : Θ' ⟶ c.functor ⋙ Θ` be a
natural transformation, and let `x ∈ H (Θ ⋙ N) F a` and `y ∈ H (Θ ⋙ N') F b` be Ext classes with
`b + a = n`. Suppose `c` carries the multiplication `μ : F ⊗ F ⟶ F` to `μ' : F' ⊗ F' ⟶ F'` (`hμ`),
and `F`, `F'`, `N` have flat values. Then pulling back the product `cup μ x y` along `c` and `η`
gives the `μ'`-product of the pull-backs of `x` and `y` along `c` and `η`. 
