---
{
  "module": "src/Lib/Shimura/AbelianScheme/Basic.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Shimura/AbelianScheme/Basic.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Shimura/AbelianScheme/Basic.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Abelian schemes: base change, finite kernels and constant functions

This file sets up abelian schemes over a base `S` in terms of `T`-points `T ⟶ A` in `Over S`,
written additively. It shows how points, sections and `O`-linear homomorphisms pass to a base
change. It proves that the kernel of a finite homomorphism into a separated commutative group scheme
over `Spec R` is `Spec S` for a finite `R`-algebra `S` (`New.Variety.exists_finite_kernel_ring`). It
also proves that global functions on the base change of an integral abelian scheme over a field to
an affine base are constant on the fibres (`New.Variety.hasConstFunctions_of_isPullback`).

## Main definitions and results

* `New.AddObj`, `New.ModuleObj O`: commutative group objects, and actions of a ring `O` on points.
* `New.IsGroupBaseChange`: base change, compatible with the group structure and the `O`-action;
  Mathlib's pullback carries both structures.
* `New.IsAbelianScheme`: smooth and proper, with surjective multiplication by every `m ≠ 0`.
  Divisibility is asked for where one usually asks for connected fibres.
* `New.Pic.atPoint`, `New.Pic.pairing`, `New.Pic.ParallelogramLaw`: for a class `c` in the Picard
  group `New.Pic` (written additively), its pull-back along a point, the pairing of two points, and
  the parallelogram law.

Notions from other files:
* `New.Pic.pull`: For p: Y → X, the homomorphism Pic X → Pic Y sending the class of a line bundle to
  the class of its pull-back.

## Relation to the literature

Known; see `Lib.Shimura.AbelianScheme.IsogenyFlatness` for sources.


 ## Abelian schemes, group base change and the Picard pairing 

 ### Group objects, ring actions, base change, abelian schemes 

### `abbrev`

 A commutative group object in schemes over `S`: an additive group object whose addition is
commutative. 

### `ModuleObj`

 An action of the commutative ring O on a commutative group object A: O-module structures on
all groups Hom(T, A), functorial in T. 

### `ModuleObj.homModule`

 For each `T` over `S`, the group of `T`-points of `A` is an `O`-module. 

### `ModuleObj.comp_smul`

 The action is functorial in `T`: it commutes with pulling points back along `a : T' ⟶ T`. 

### `IsAbelianScheme`

 The commutative group scheme A over S is an abelian scheme: it is smooth and proper over S,
and multiplication by every m ≠ 0 is surjective. 

### `IsAbelianScheme.nsmul_surjective`

 Multiplication by every natural number `m ≠ 0` is surjective. 

### `IsGroupBaseChange`

 The morphism p : B → A makes B the base change of A along b : S' → S, and composing with p is
R-linear on T-points for every S'-scheme T. 

### `IsGroupBaseChange.isPullback`

 The square of `p`, `b` and the structure morphisms of `B` and `A` is cartesian. 

### `IsGroupBaseChange.linear`

 For each `U` over `S'`, the map `u ↦ (Over.map b).map u ≫ p` from `U`-points of `B` to
  `(Over.map b).obj U`-points of `A` is `R`-linear. 

 ### Homomorphisms 

### `IsAdditive`

 The morphism f : A → B of commutative group objects is a homomorphism: composing with f is
additive on U-points for every U. 

### `abbrev`

 An isogeny is a homomorphism f : A → B that is finite, flat and surjective as a morphism of
schemes. 

### `IsLinear`

 The morphism f : A → B of R-module objects is a homomorphism that commutes with R:
multiplication by c on A followed by f equals c times f, for every c in R. 

### `IsLinear.smul_id_comp`

 Multiplication by `c` on `A` followed by `f` equals `c • f`. 

### `isAdditive_of_universal`

 A morphism `f : A ⟶ B` of commutative group objects is a homomorphism if it is additive on the
universal pair of points, the two projections `fst A A` and `snd A A` of `A ⊗ A`. 

### `instance (priority`

 Every commutative group object is a `ℤ`-module object: the points form `ℤ`-modules through
integer multiples. 

### `instance [IsAdditive f] : IsAdditive (c • f)`

 A multiple `c • f` of a homomorphism `f` of commutative group objects is a homomorphism. 

 ### Structures on the pullback, and properties of morphisms over the base 

### `pullbackAddObj`

 The pull-back of a commutative group object A along b is a commutative group object. 

### `instance : ModuleObj R ((pullback b).obj A)`

 The pull-back along `b` of an `R`-module object `A` is an `R`-module object. 

### `instance [IsIso f] : IsIso f.left`

 An isomorphism over `S` is an isomorphism of schemes. 

### `instance [IsProper X.hom] [IsSeparated Y.hom] : IsProper f.1`

 A morphism `f` over `S` from a proper `S`-scheme to a separated `S`-scheme is proper; `f.1`
is the underlying morphism of schemes `f.left`. 

### `instance {X Y S : Scheme} {d : ℕ} (f : X ⟶ S) (g : Y ⟶ S) [SmoothOfRelativeDimension d f] : SmoothOfRelativeDimension d (Limits.pullback.snd f g)`

 Smoothness of relative dimension `d` is stable under base change: if `f : X ⟶ S` is smooth of
relative dimension `d`, so is the projection `X ×_S Y ⟶ Y` for any `g : Y ⟶ S`. 

### `specOver`

 The spectrum of an R-algebra B, as a scheme over Spec R. 

 ### Translations 

### `translation`

 Translation by a section z of A over S: the S-morphism x ↦ x + z from A to itself. 

### `instance : IsIso (translation z)`

 Translation by `z` is an isomorphism, with inverse the translation by `-z`. 

 ### Classes of line bundles at points 

### `atPoint`

 For c in Pic A and a T-point x of A, the pull-back x^*c in Pic T. 

### `pairing`

 For c in Pic A and T-points x, y of A, the class ⟨x, y⟩ = (x + y)^*c − x^*c − y^*c + 0^*c in
Pic T. 

### `ParallelogramLaw`

 The parallelogram law for a class c in Pic A: (x+y)^*c + (x−y)^*c + 2·0^*c = 2(x^*c + y^*c)
in Pic T for all T-points x, y of A and all S-schemes T. 

### `CategoryTheory.Over.left_comp_left_eq_of_map_comp_eq`

 For `b : X ⟶ Y` in a category, a commuting square `(Over.map b).map u ≫ p = p ≫ v` of morphisms
over `Y` gives the square `u.left ≫ p.left = p.left ≫ v.left` of the underlying morphisms. 


## Points, sections and homomorphisms under base change

Throughout, `h : New.IsGroupBaseChange b p` says that `p` presents the group object `A'` over `S'`
as the base change of `A` along `b : S' ⟶ S`.


### `pointEquiv`

 For an O-compatible base change p : A' → A and an S'-scheme T, the O-linear bijection
x ↦ (Over.map b).map x ≫ p from T-points of A' over S' to T-points of A over S. 

### `pullSection`

 For a base change A' of A along b : S' → S, the O-linear map pulling sections of A over S
back to sections of A' over S'. 

### `atPoint_picClass_pull`

 For a base change p : A' → A, a line bundle N on A and a T-point x of A', the pull-back of
the class of p*N along x equals the pull-back of the class of N along the point p∘x of A. 

### `smul_id_comp`

 `p` commutes with multiplication by `m` in `O` on `A'` and on `A`. 

### `nsmul_id_comp`

 `p` commutes with multiplication by a natural number `m` on `A'` and on `A`. 

### `translation_comp`

 `p` carries translation by the pulled-back section `New.IsGroupBaseChange.pullSection` of `z` to
translation by `z`. 

### `exists_hom_baseChange`

 Let `A'` be a base change of `A` along `b` and `B'` one of `B` along `c`, with `b c : S' ⟶ S`,
and let `F : map c ⟶ map b` be a natural map. An `O`-linear homomorphism `χ : A ⟶ B` induces
`ψ : A' ⟶ B'` such that (a) read through `pointEquiv`, the `T`-point `u ≫ ψ` is `F`, then `u`,
then `χ`; (b) `ψ` is additive and `O`-linear; (c) `ψ` sends the pull-back of a section `z` to the
pull-back of `z ≫ χ`. 


## Kernels of finite homomorphisms

`New.AddObj B` makes `B` a commutative group object with zero section `ζ[B]`, and `New.specOver R S`
is `Spec S` as a scheme over `Spec R`.


### `locallyOfFinitePresentation_left`

 If `A` is locally of finite presentation over `Spec R` and `B` is locally of finite type over
`Spec R`, then every morphism `f : A ⟶ B` over `Spec R` is locally of finite presentation. 

### `exists_isPullback_SpecMap`

 The pull-back of an affine morphism `f` along a point `Spec C ⟶ Y` is `Spec` of a ring map
`C ⟶ P`. 

### `eq_zero_iff_factors_zero_section`

 A morphism `f : A ⟶ B` over `Spec R` is zero exactly when, as a morphism of schemes, it factors
through the zero section `ζ[B]` of `B`. 

### `IsFiniteKernelRing`

 `ι : Spec S ⟶ A` is the kernel of `f : A ⟶ B` over `Spec R`, and `S` is finite over `R`: `ι` is
a closed immersion killed by `f`, through which every point of `A` killed by `f` factors; `S` is
flat over `R` if `f` is flat. 

### `IsFiniteKernelRing.finite`

 `S` is a finite `R`-module. 

### `IsFiniteKernelRing.flat`

 `S` is flat over `R` if `f` is flat. 

### `IsFiniteKernelRing.isClosedImmersion`

 `ι` is a closed immersion. 

### `IsFiniteKernelRing.comp_eq_zero`

 `ι` is killed by `f`. 

### `IsFiniteKernelRing.exists_comp_eq`

 Every point of `A` killed by `f` factors through `ι`. 

### `instance : IsClosedImmersion ζ[B].left`

 The zero section of a separated commutative group scheme is a closed immersion. 

### `exists_finite_kernel_ring`

 Let `B` be a separated commutative group scheme over `R` and `f : A ⟶ B` a finite morphism over
`R`. The fibre of `f` over the zero section is affine: it is `Spec S` for a finite `R`-algebra `S`,
flat over `R` if `f` is flat (`New.Variety.IsFiniteKernelRing`). 


## Global functions on a base change of an abelian variety

`New.HasConstFunctions s` says that global sections of `X`, viewed as functions on ring-valued
points (`New.PointFn.ofSection`), are constant on the fibres of `s`.


### `New.HasConstFunctions`

 For s : X → S, every function regular on all of X takes equal values at two ring-valued
points of X with the same image under s. 

### `New.Variety.hasConstFunctions_of_isPullback`

 Let A be an integral abelian scheme over a field k and X = A ×_k Spec C. A function regular on
all of X takes equal values at any two ring-valued points with the same image in Spec C. 
