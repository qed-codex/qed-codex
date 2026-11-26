---
{
  "module": "src/Lib/Cohomology/PointClass/ProjectiveNonvanishing.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Cohomology/PointClass/ProjectiveNonvanishing.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Cohomology/PointClass/ProjectiveNonvanishing.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The Hodge–Tate map does not kill point classes of the projective line and space

Let `k` be a field with an embedding in `ℚ̄_p`, and let `λ_h = New.Variety.hodgeTateMap h` be the
Hodge–Tate map of weight `h`, from Hodge cohomology to `p`-adic cohomology. We compute `λ₁` of the
symbol `[dT / T]` of the pair `(𝔸¹, 𝔸¹ ∖ 0)` through the extension `0 → T → Bˣ → Tˣ → 0`.

## Main definitions and results

* `New.Variety.thickeningOver.oneSubMu`, `New.Variety.thickeningOver.shortExact_oneSubMu`: the short
  exact sequence `0 → T → Bˣ → Tˣ → 0` whose first map is `t ↦ 1 - μ t`.
* `New.Variety.hodgeTateMap_symbolClass`: the image of `[dT / T]` comes from the product of the
  boundary class of the pair with the class of this extension.
* `New.Variety.projSpace.exists_hodgeTateMap_pointClass_line`: `λ₁` of the class of `[1 : 0]` in
  `ℙ¹` comes from a degree-two class `η` on `p`-adic tests such that `x ↦ x × η` is injective on
  functors with flat values.
* `New.Variety.projSpace.hodgeTateMap_pointClass_ne_zero`: the class of a point of `ℙ^d` has a
  nonzero image under the Hodge–Tate map of weight `d`.

Notions from other files:
* `New.Variety.PadicTest`: a `p`-adic test, a non-empty family of cells (`New.Variety.IsCell`) with
  a ring map from `O_C` to their product; `R` denotes its ring.
* `New.Variety.thickeningOver`: the functor sending a `p`-adic test with ring `R` to the `k`-algebra
  `B = W(R♭)[1/p] / (ker θ)²`. `New.Variety.genericOver` sends it to `T = R[1/p]`, and
  `New.Variety.thickeningOver.proj : B → T` is the projection; its kernel is `μ T`, `μ = [ε] - 1`.
* `New.Variety.hodgeTateMap`: `λ_h` sends a Hodge class to a class on Hodge–Tate pairs (a `p`-adic
  test with a finite free module `M` over `T`). It restricts along `B ×_T (T ⊕ M) → T ⊕ M`, applies
  the `h`-th power of the contraction class, and projects `⋀M` to degree zero.
  `New.Variety.restrictToPairs` maps cohomology on `p`-adic tests to the same target.
* `New.Variety.symbolClass`: the class `[dT / T]` in the Hodge cohomology of the pair
  `(𝔸^d, 𝔸^d ∖ 0)`.
* `New.Variety.pointClass`: the class of a `k`-point `z` in Hodge cohomology of degree `d`, the
  image of a chosen class with support `z` and multiplicity `1` at `z`. Projective space
  `New.Variety.projSpace k d` sends `A` to the unimodular vectors in `A ^ (d + 1)` modulo units.

## Relation to the literature

Known; see `Lib.Cohomology.PointClass.LinearIndependence` for sources.



## The Hodge–Tate map of the symbol [dT/T]

For a `p`-adic test with ring `R`, `T = R[1/p]` is `New.Variety.genericOver`, with additive group
`New.Variety.genericCoeff`.


### `isUnit_of_unimodular_one`

 A unimodular vector `v` of length one over a `k`-algebra `A` (an `A`-point of `𝔸¹ ∖ 0`) has a
unit as its only coordinate `v 0`. 

### `Gm.ofCoord`

 The coordinate of `𝔸¹ ∖ 0` as a map to the multiplicative group: the morphism from `ℤ[𝔸¹ ∖ 0]`,
the free abelian group on the unimodular vectors of length one, to `A ↦ Aˣ` (written additively)
on `k`-algebras. It sends a generator `[v]` to the coordinate `v 0`, a unit by
`New.Variety.isUnit_of_unimodular_one`. 

### `thickeningOver.oneSubMu`

 On `p`-adic tests with ring `R`, the morphism `t ↦ 1 - μ t` from the additive group of
`T = R[1/p]` (`New.Variety.genericCoeff`) to the units of `B = W(R♭)[1/p] / (ker θ)²`. Here `μ t` is
`New.Variety.thickeningOver.mulMu`, the product with `μ = [ε] - 1`. As `(μ s) * (μ t) = 0`, the
map sends sums to products, so its values are units. 

### `thickeningOver.shortExact_oneSubMu`

 On `p`-adic tests the sequence `0 → T → Bˣ → Tˣ → 0` is short exact: its first map is
`t ↦ 1 - μ t` (`New.Variety.thickeningOver.oneSubMu`), its second is induced on units by the
projection `New.Variety.thickeningOver.proj : B → T`, and `w` says that their composite is zero. 

### `pull_mk₀_comp_contractionPow_one_eq_pull_extClass_oneSubMu`

 Let `ω` be a form on `𝔸¹ ∖ 0` over Hodge tests that sends a point `a + m` to a one-form `w`
with `a • w = m`, so that `ω = dT / T` (such an `ω` is given by `New.Variety.symbolClass_one`). On
Hodge–Tate pairs, the pull-back of `ω` followed by one contraction
(`New.Variety.HodgeTatePair.contractionPow 1`) is the pull-back of the class of the extension
`0 → T → Bˣ → Tˣ → 0` (`New.Variety.thickeningOver.shortExact_oneSubMu`) along the coordinate
`New.Variety.Gm.ofCoord`. 

### `hodgeTateMap_symbolClass`

 The Hodge–Tate map on `[dT / T]` in dimension one: `λ₁ [dT / T]` is the image under
`New.Variety.restrictToPairs` of a degree-two class on `p`-adic tests. This class is the Yoneda
product of the boundary class of the pair `(𝔸¹, 𝔸¹ ∖ 0)` (the extension class of
`0 → ℤ[𝔸¹ ∖ 0] → ℤ[𝔸¹] → ℤ[𝔸¹] / ℤ[𝔸¹ ∖ 0] → 0`, restricted to tests) with the class of the
extension `0 → T → Bˣ → Tˣ → 0` of `New.Variety.thickeningOver.shortExact_oneSubMu`, pulled back
along the coordinate `New.Variety.Gm.ofCoord`. 


## The point class of the projective line

`New.Variety.hodgeTateMap h` is the Hodge–Tate map `λ_h` on Hodge cohomology.
`New.Variety.pointClass d z` is the class of a `k`-point `z`, and `New.Variety.cup` is the external
product of classes.


### `thickeningOver.teichmullerLift_epsTilt`

 For a `p`-adic test `c` with ring `R`, in `B = W(R♭)[1/p] / (ker θ)²` the Teichmüller lift of
`ε` (`Period.epsTilt`, mapped to the tilt `R♭`) is `1 + μ`, where `μ = mulMu c 1` is the image of
`[ε] - 1`. 

### `pairRestrictBijective_relFreeAb_of_isOpenSubfunctor`

 Let `V` be covered by charts of dimension one (`New.Variety.IsChartCovered 1 V`) and `U` an
open subfunctor of `V`. Then restriction from `p`-adic tests to Hodge–Tate pairs is bijective
(`New.Variety.PairRestrictBijective`) on the cohomology of `relFreeAb U = ℤ[V] / ℤ[U]`. 

### `projSpace.cutsOutLocus_stdChart_zero_X`

 On the chart `0` of the projective line (the points `[1 : x]`), the coordinate `X` cuts out the
point `affinePoint 0 0 = [1 : 0]`: a map `α` from the chart's ring to a `k`-algebra `C` kills `X`
exactly when it sends the chart's point to `[1 : 0]` (`New.Variety.CutsOutLocus`). 

### `projSpace.relFreeAb_mk_stdChart_one_eq_zero`

 The points of the chart `1` of the projective line (the points `[x : 1]`) avoid
`affinePoint 0 0 = [1 : 0]`: for every map `ψ` from the chart's ring to `A`, the image of the
chart's point is zero in `ℤ[ℙ¹] / ℤ[ℙ¹ ∖ [1 : 0]]` (`New.Variety.relFreeAb` of
`New.Variety.offPoints`). 

### `projSpace.exists_relative_point_class`

 There is a degree-two class `ξT` in the cohomology on `p`-adic tests with coefficients
`genericCoeff` (a test with ring R ↦ R[1/p]) of ℤ[ℙ¹]/ℤ[`offPoints {affinePoint 0 0}`] composed with
`genericOver`. It satisfies two conditions. First, `hodgeTateMap 1` of the class of the point
`affinePoint 0 0 = [1 : 0]` of `ℙ¹` is `restrictToPairs` of the image of `ξT` in the cohomology of
ℤ[ℙ¹]. Second, the pull-back of `ξT` to the chart `stdChart k 1 0` equals the pull-back, along the
identification of that chart with the pair `(𝔸¹, 𝔸¹ ∖ 0)`, of the product of the boundary class of
`0 → ℤ[𝔸¹ ∖ 0] → ℤ[𝔸¹] → ℤ[𝔸¹]/ℤ[𝔸¹ ∖ 0] → 0` with the pull-back along `Gm.ofCoord` of the
degree-one class of the extension of units `thickeningOver.shortExact_oneSubMu`. 

### `thickeningOver.teichmullerLift_map`

 The Teichmüller lift is natural in the test: for a map `f : c ⟶ d` of `p`-adic tests,
`thickeningOver.map f` sends `[x]` to `[tilt.map f x]`. 

### `teichmullerCoordinate`

 The Teichmüller coordinate. For a `p`-adic test with ring `R`, a point `t` of the perfect disc
over the tilt is an `O♭`-algebra map `O♭[ℚ≥0] → R♭` with coordinate `u = t (T ^ 1)`; it goes to the
Teichmüller lift `[u]`, a point of the affine line over `B = W(R♭)[1/p] / (ker θ)²`. 

### `teichmullerCoordinate_mul_inv`

 On a point of the torus `O♭[ℚ] → R♭`, the Teichmüller coordinates at `u` and at `u⁻¹` multiply
to `1`. 

### `teichmullerCoordinate_comp_proj_charTwist`

 Followed by the projection `B → T = R[1/p]`, the Teichmüller coordinate does not change when the
point is twisted by `charTwist`, which multiplies `u` by `ε` or by `ε⁻¹`. 

### `exists_teichmuller_coordinate`

 The Teichmüller coordinate `A = New.Variety.teichmullerCoordinate` with its three properties:
(a) its formula, (b) `[u] [u⁻¹] = 1` on the torus, (c) invariance under `charTwist` after the
projection to `R[1/p]`. 

### `pullbackAlong_tensorPoint_comp_eq_self`

 If `one` is a unit for `mult`, that is, `x ↦ x ⊗ one` followed by `mult` is the identity of `F`,
then pulling the class `x ⊗ F` followed by `mult` back along `S ↦ S ⊗ one` recovers `x`. 

### `unitsExtClass`

 The class on `p`-adic tests that `λ₁` gives on the symbol `[dT/T]`
(`New.Variety.hodgeTateMap_symbolClass`): the boundary class of the pair `(𝔸¹, 𝔸¹ ∖ 0)` times the
class of the extension `0 → T → Bˣ → Tˣ → 0` of `New.Variety.thickeningOver.shortExact_oneSubMu`,
pulled back along `New.Variety.Gm.ofCoord`. 

### `projSpace.map_unitsExtClass_eq_map_of_comp_eq`

 Let `s` be a section of the map of pairs induced by the coordinate of the chart `0` of `ℙ¹`
(`h_section`), and let `ξT` restrict on the chart `0` to the pull-back of
`New.Variety.unitsExtClass` along that coordinate (`h_compare`). If `j'` lifts `j` followed by `s`
and the inclusion of the chart (`hj'`), then the pull-back of `unitsExtClass` along `j` is the
pull-back along `j'` of the image of `ξT` in `ℤ[ℙ¹]`. 

### `projSpace.exists_map_eq_map_of_isTodaCancellation`

 The map `j` of a Toda cancellation lifts through the projective line. Let `A` be a natural map
from the perfect disc to the affine line over `B` whose values at `u` and `u⁻¹` multiply to `1` on
the torus (`hA_inv`), and let its image `a` in `R[1/p]` be invariant under the twists of the two
discs (`hA_twist`). Let `(j, y, ω)` cancel `New.Variety.unitsExtClass` in the sense of
`New.Variety.IsTodaCancellation`, for the gluing of the two discs and the map induced by `a`. Let
`ξT` be a class on tests relative to the complement of `[1 : 0]` whose restriction to the chart `0`
is the pull-back of `unitsExtClass` along the coordinate (`h_compare`). Then the pull-back of
`unitsExtClass` along `j` is the pull-back along some `j'` of the image of `ξT` in `ℤ[ℙ¹]`. 

### `eq_zero_of_cup_eq_zero_of_isTodaCancellation`

 Let `(j, y, ω)` cancel `New.Variety.unitsExtClass` in the sense of
`New.Variety.IsTodaCancellation`, for the gluing of the two perfect discs, where `ε` sends the point
to a unit for the multiplication of `R[1/p]` (`h_unit`). If the pull-back of `unitsExtClass` along
`j` is the pull-back of `η` along `j'` (`h_pull`), then for `N` with flat values and `x` in
`H^n(N, R[1/p])`, the product `x × η` vanishes only if `x = 0`. 

### `projSpace.exists_hodgeTateMap_pointClass_line`

 Let `k` be a field of characteristic `0` with an embedding in `ℚ̄_p`. There is a degree-two
cohomology class `η` of the functor `S ↦ ℤ[ℙ¹(S[1/p])]` on `p`-adic tests `S` (with ring `R`,
written `S[1/p] = R[1/p]`), with coefficients `S ↦ R[1/p]` (`genericCoeff`), such that the following
hold. (a) The Hodge–Tate map `hodgeTateMap 1` sends the class of the point `[1 : 0]` to
`restrictToPairs η`. (b) For every functor `N` from `p`-adic tests to abelian groups with flat
values and every `x` in the degree-`n` cohomology of `N` with coefficients `R[1/p]`, the cup product
of `x` and `η` (paired by multiplication in `R[1/p]`) vanishes only if `x = 0`. 

 ## Point classes of projective space 

### `New.Variety.projSpace.pointClass_eq_pointClass_affinePoint`

 All `k`-points of projective space have the same class: a global function takes the same value
at all of them. 

### `New.Variety.hodgeTateMap_pointClass_eq_zero_of_ne`

 Let `k` be a field of characteristic zero with an embedding in `ℚ̄_p`, and let `X` be a functor
on `k`-algebras with an atlas of dimension `d` (separated, with finitely many charts, each having
`d` étale coordinates, that together contain every field-valued point). For a `k`-point `z` of `X`,
the class `pointClass d z` of `z` in degree-`d` Hodge cohomology is killed by `hodgeTateMap l` for
every `l ≠ d`. 

### `New.Variety.projSpace.exists_map_pointClass_eq_nsmul_map_cup`

 In characteristic zero, let `z` be a `k`-point of `ℙ^d` and
`lineProductMap k d : ℙ^d × ℙ¹ → ℙ^(d+1)` the map sending `([v], [w 0 : w 1])` to the point with
coordinates `w 0 * ∑ i, v i` and `(w 1 - i * w 0) * v i`. Then the pull-back along this map of the
Hodge class of the point `affinePoint 0 0 = [1 : 0 : … : 0]` of `ℙ^(d+1)` is a positive multiple `n`
of the image in the Hodge cohomology of `ℤ[ℙ^d × ℙ¹]` of the cup product (exterior-algebra
multiplication) of the classes of `z` and of `[1 : 0]` in `ℙ¹`. 

### `New.Variety.projSpace.hodgeTateMap_pointClass_ne_zero`

 Let `k` be a field of characteristic zero with an embedding in `ℚ̄_p`, and let `z` be a
`k`-point of projective `d`-space. The Hodge–Tate map `hodgeTateMap d` does not kill the class
`pointClass d z` of `z` in the degree-`d` Hodge cohomology of projective `d`-space. 
