---
{
  "module": "src/Lib/Shimura/ThetaGroup.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Shimura/ThetaGroup.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Shimura/ThetaGroup.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Lifts of morphisms to sections of line bundles, and theta structures on abelian schemes

A morphism `f : X' → X` and an isomorphism `f^* L ≅ L'` induce a map on global sections
`Φ : H⁰(L) → H⁰(L')`. Over a local ring `R`, these maps let translations of an abelian scheme act on
sections of a line bundle. For a theta structure on `N` indexed by a group `H`, it also gives a
bound on the exponent of `K([N])`, under further hypotheses.

## Main definitions and results

* `New.Variety.IsSectionLift`: `Φ` comes from some isomorphism `f^* L ≅ L'`;
  `New.Variety.IsTranslationLift` is the case of a translation; `New.Variety.coordSection` is the
  `j`-th coordinate section of a linear system.
* `New.Variety.exists_isSectionLift`, `New.Variety.IsSectionLift.picClass_eq`: a lift exists when
  `[L'] = f^* [L]`, and only then.
* `New.Variety.IsTranslationLift.mul`, `New.Variety.IsTranslationLift.pow`,
  `New.Variety.exists_isTranslationLift_iff`: lifts of translations multiply, and the translation by
  `z` lifts to `L`, over a local ring `R`, exactly when the pairing `New.Pic.pairing` of `[L]`
  vanishes on `z` and the identity, that is, when `z` lies in the kernel `K([L])`.
* `New.Variety.IsThetaStructure`: a linear system with coordinates indexed by a group `H`, permuted
  up to a cocycle by lifts of the maps `y ↦ ± y + η s`.
* `New.Variety.IsThetaStructure.pull_eq_of_picClass_eq`: rigidity of theta structures along a
  homomorphism.
* `New.Variety.IsThetaStructure.card_nsmul_eq_zero_of_isTranslationLift`: the order of `H` kills
  every section whose translation lifts to `N`, when `N` is a projective embedding; over a local
  ring these are the sections in `K([N])`.

Notions from other files:
* `New.LineBundle.pull`: the pull-back of the line bundle (U_i, g_ij) along p: Y → X, with cover
  p⁻¹U_i and transition functions p*g_ij.
* `New.LineBundle.IsLinearSystem`: L is a linear system, the model being g_ij = s_j / s_i on
  U_i = {s_i ≠ 0} for sections s_i without common zero.
* `New.HasConstFunctions`: for s : X → S, a function regular on all of X takes equal values at two
  ring-valued points with the same image under s.

## Relation to the literature

Known; see `Lib.Shimura.IntegralModel.UniversalFamily` for sources.



## Lifts of a morphism to global sections

A line bundle `New.LineBundle` is a cover `U i` with a cocycle `g i j` of functions on ring-valued
points (`New.PointFn`); a section `s` (`IsSection`) has each `s i` regular on `U i` (`IsRegularOn`),
with `s i = g i j * s j` on `U i ∩ U j`; it lies in `H0` if also `s i = 0` off `U i`; an isomorphism
`M ≅ L` is a frame (`New.LineBundle.IsFrame`) of `L.mul M.inv`.


### `IsPullbackVia`

 The map `Φ` on global sections is pull-back along `f` followed by `u`. Here `u` is a frame of
`L' ⊗ (f^* L)⁻¹`, that is, an isomorphism `f^* L ≅ L'`. At every point that lands in the chart `i`
of `L'` and whose image lands in the chart `a` of `L`, one has `(Φ s)_i = u_(i,a) · f^* s_a`. 

### `IsSectionLift`

 The condition that the map Φ : H⁰(L) → H⁰(L') is pull-back along f : X' → X followed by some
isomorphism f^*L ≅ L'. 

### `IsTranslationLift`

 The R-linear endomorphism Φ of H⁰(L) is pull-back along the translation t_z by the section z
followed by some isomorphism t_z^*L ≅ L. 

### `coordSection`

 For a linear system L on an R-scheme and an index j, the j-th coordinate as an element of
the R-module H⁰(L) of global sections. 

### `H0_ext`

 Two sections of `L` are equal if they agree on each chart `L.opens i`. Only charts on which both
`i`-th components are regular need to be checked, and there they must agree at all points that land
in the chart. 

### `IsSectionLift.picClass_eq`

 A lift `Φ` along `f` from sections of `L` to sections of `L'` exists only if `[L'] = f^* [L]` in
the Picard group. 

 ### Construction of lifts 

### `pullSections`

 For f : X' → X lying over the ring map φ : R → R' and M = f^*L, the φ-semilinear pull-back
of global sections H⁰(L) → H⁰(M). 

### `exists_isPullbackVia`

 A frame `u` of `N ⊗ (F^* L)⁻¹` gives the `R`-linear map `s ↦ u * F^* s` on sections, which is
pull-back along `F` followed by `u`. 

### `exists_isSectionLift`

 If `[N] = F^* [L]` in the Picard group, there is an `R`-linear lift `Φ` of `F` from sections
of `L` to sections of `N`. 

### `IsSectionLift.pull_eq_of_coordSection`

 If a lift `Φ` along `f` sends each coordinate of `L` to `a` times the corresponding coordinate
of `L'`, then `f^* L = L'` as linear systems. 

### `exists_isSectionLift_coordSection`

 Let `L` be a linear system on `X`, `F : Y ⟶ X`, and `s j` sections of `N` indexed like the
coordinates of `L`. Suppose that at each point in `N.opens i` whose image lies in `L.opens a`, (a)
some `s j` is a unit and (b) `s j = s a * F^* (L.transition a j)`. Then there is an `R`-linear lift
`Φ` of `F` that sends the `j`-th coordinate of `L` to `s j`. 

### `isSectionLift_pullSections`

 The pull-back of sections `pullSections φ hf e` along `f` is a lift of `f` from sections of `L`
to sections of `M = f^* L`. 

 ### Composition, uniqueness and injectivity 

### `pullSections_coordSection`

 The pull-back of the `i`-th coordinate section of `L` is the `i`-th coordinate section of the
pulled-back linear system `M`, where `e : M = L.pull f`. 

### `IsSectionLift.comp`

 Here `IsSectionLift L' L f Φ` means that `Φ : H⁰(L) → H⁰(L')` is pull-back of sections along
`f : X' ⟶ X` followed by some isomorphism `f^*L ≅ L'`. If `Θ` lifts `g : X'' ⟶ X'` from sections of
`L'` to sections of `L''` (over `R''`), and `Φ` lifts `f : X' ⟶ X` from sections of `L` to sections
of `L'`, then `Θ ∘ Φ` lifts the composite `g ≫ f` from sections of `L` to sections of `L''`. 

### `IsSectionLift.exists_eq_smul`

 If X' is a commutative group scheme over R' whose global functions are constant, two maps
Φ, Ψ: H⁰(L) → H⁰(L'), each pull-back along f followed by some isomorphism f^*L ≅ L', are
proportional: Φ(s) = cΨ(s) for all s, for some c in R'. 

### `IsSectionLift.injective`

 A lift along a quasi-compact, scheme-theoretically dominant morphism `f` is injective: a section
is determined by its pull-back along `f`. 


## Lifts of translations and theta structures

Rigidity and the bound on `K([N])` reduce to `New.Variety.IsThetaStructure.pull_eq_of_intertwines`.


### `IsTranslationLift.mul`

 Lifts `Φ` and `Ψ` of the translations by `z` and by `w` compose to the lift `Φ * Ψ` of the
translation by `z + w`. 

### `exists_isTranslationLift_iff`

 The translation by `z` lifts to `L` if and only if `z ∈ K([L])`, that is, the class
`⟨z, 𝟙 A⟩ = t_z^*[L] - [L]` vanishes in `Pic A`; the terms pulled back from the base are trivial
over the local ring `R`. 

 ### Theta structures 

### `IsThetaStructure`

 A theta structure on a linear system `N` on `A` whose coordinates `X t = coordSection hN t` are
indexed by an abelian group `H` of order invertible in `R`. Each map `y ↦ ± y + η s` has a lift
to `N` that sends `X t` to `c s t • X (±(s + t))`, where `c s` is a character of `H` and
`c s (-t) = c t s`. For the subgroup `Lg`: `X s = X 0` for `s ∈ Lg`, and the sum of `c s l ^ 2`
over `l ∈ Lg` vanishes for `s ∉ Lg`. 

### `IsThetaStructure.neg_eq_swap`

 The symmetry `c s (-t) = c t s` of the cocycle `c`. 

### `IsThetaStructure.theta_law`

 The theta law: the map `y ↦ ± y + η s` has a lift to `N` that sends the coordinate `X t` to
  `c s t • X (±(s + t))`. 

### `IsThetaStructure.coordSection_eq_of_mem`

 The coordinates indexed by `Lg` all equal `X 0`. 

### `IsThetaStructure.isUnit_card`

 The order of `H` is a unit of `R`. 

### `IsThetaStructure.sum_sq_eq_zero`

 For `s ∉ Lg` the sum of `c s l ^ 2` over `l ∈ Lg` vanishes. 

### `IsThetaStructure.pull_eq_of_intertwines`

 Write `X t` and `X' t` for the coordinates `coordSection hN t` and `coordSection hN' t` of the
theta structures `h` and `h'`. Assume that the coordinates of `N` span `H⁰(N)` (`h_span`). Let
`U s` send `X t` to `c s t • X (s + t)`, and let `T : H⁰(N') → H⁰(N)` be a lift of `f : A ⟶ A'` with
`T (X' s) = U s (T (X' 0))` for all `s`. Then `f^* N' = N` as linear systems. 

### `IsThetaStructure.pull_eq_of_picClass_eq`

 Rigidity. Let `N` on `A` and `N'` on `A'` be theta structures over the ring `R` for the same
finite group `H` of odd order and the same subgroup `Lg`. Assume that global functions on `A` are
constant on the fibres over `R` (`h_const`) and that the coordinates of `N` span `H⁰(N)` (`h_span`).
If a homomorphism `f: A ⟶ A'` carries `η` to `η'` and `[N] = f^* [N']` in the Picard group, then
`f^* N' = N` as linear systems: `f` matches the coordinates. 

### `IsThetaStructure.card_nsmul_eq_zero_of_isTranslationLift`

 Let `N` be a theta structure on `A` over the ring `R`, indexed by the finite group `H`, which is
a projective embedding. Assume that global functions on `A` are constant on the fibres over `R`
(`h_const`), and that the coordinates of `N` span `H⁰(N)` (`h_span`). If the translation by a
section `y` lifts to `N` (when `R` is local, this means `y ∈ K([N])`), then `y` is killed by the
order of `H`. 
