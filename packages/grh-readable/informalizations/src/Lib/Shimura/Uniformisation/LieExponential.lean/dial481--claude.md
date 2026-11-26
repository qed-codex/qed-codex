---
{
  "module": "src/Lib/Shimura/Uniformisation/LieExponential.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Shimura/Uniformisation/LieExponential.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Shimura/Uniformisation/LieExponential.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Exponential of compact commutative Lie groups and uniformisation of abelian varieties

The complex points `New.ComplexPoint A` of a scheme `A` over ℂ carry the classical topology. Here
`A` is an object of `Over (Spec ℂ)`, and a point is a morphism from `Spec ℂ` over it. A smooth
scheme has holomorphic charts, and a projective variety has compact complex points. For an abelian
variety A with a projective embedding (`New.LineBundle.IsProjEmbedding`), the group A(ℂ) is
therefore compact and commutative with a holomorphic chart at 0. An exponential map exists for any
such group, and it gives a uniformisation of A by ℂᵈ, where d is the dimension of A.

## Main definitions and results

* `New.exists_lie_exponential` constructs the exponential map of a compact commutative group with a
  chart at `0` in which addition is complex analytic. The value at `v` is a limit of `n • ψ (v / n)`
  along an ultrafilter on `ℕ`, which exists by compactness; no differential equation is solved.
* `New.exists_holomorphic_chart`: a smooth scheme has a holomorphic chart at every complex point.
* `New.LineBundle.IsProjEmbedding.compactSpace_complexPoint`: the complex points of a projective
  variety are compact.
* `New.LineBundle.IsProjEmbedding.nonempty_uniformisation`: an abelian variety of dimension d is
  uniformised by ℂᵈ.

Notions from other files:
* `New.IsFullRankLattice L`: the `ℤ`-submodule `L` of `V` is discrete and spans `V` over `ℝ`. Here
  `V` is a `FinComplexSpace`, that is, a finite-dimensional complex normed space.
* `New.IsAbelianScheme`: a commutative group scheme A over S is abelian if it is smooth and proper
  over S and multiplication by every m ≠ 0 is surjective.
* `New.Uniformisation`: a surjective homomorphism from a complex vector space V to the complex
  points of A, with kernel a lattice, holomorphic and immersive, through which homomorphisms
  holomorphic at 0 factor ℂ-linearly.
* `New.LineBundle.IsProjEmbedding`: The linear system N embeds the proper scheme X in projective
  space: points in one chart with the same affine coordinates and the same base point are equal.
* `New.HasGermAt`: For each open U of X containing φ(w₀) and each f regular on U: φ(w) lies in U for
  w near w₀, and the function f∘φ satisfies Q. `New.HolomorphicAt` is the case where Q is
  analyticity at w₀.

## Relation to the literature

Known; see `Lib.Shimura.Uniformisation.AppellHumbert` for sources.


 ## The exponential map of a compact commutative complex Lie group 

### `New.hasStrictFDerivAt_chart_add`

 Let `φ : G → V` be a chart at `0` of a commutative group `G` with inverse `ψ`: `ψ 0 = 0` and
`φ ∘ ψ = id` near `0`. If addition read in the chart, `(v, w) ↦ φ (ψ v + ψ w)`, is analytic at `0`,
then its strict derivative at `0` is `(v, w) ↦ v + w`: on each axis the map is `φ ∘ ψ`. 

### `New.exists_chart_nsmul_approx`

 Multiples in a chart: as long as `n • b` is small, `n • ψ b` stays in the set `C` on which `ψ`
inverts `φ`, and its coordinate is `n • b` up to a relative error `ε`. Here `φ 0 = 0`, `ψ 0 = 0`,
addition read in the chart stays in `C` near `0`, and its strict derivative at `0` is addition. 

### `New.isFullRankLattice_ker_of_isolated`

 Let `e : V →+ G` be a homomorphism from a finite-dimensional complex space to a compact group
that maps neighbourhoods of `0` onto neighbourhoods of `0` and has `0` as an isolated zero. Then its
kernel is a full-rank lattice in `V`. 

### `New.IsExpLimit`

 For a map `ψ : V → G`, `x` is an exponential limit of `v` when some sequence `b` has
`n • b n → v` and `n • ψ (b n) → x`, both along the hyperfilter of `ℕ`. 

### `New.isExpLimit_add`

 Exponential limits add. Let `ψ` invert `φ` on `C`, with `φ 0 = 0`, `ψ 0 = 0`, addition read in
the chart staying in `C` near `0` and having strict derivative `(v, w) ↦ v + w` at `0`. If `x` is an
exponential limit of `v` and `y` one of `w`, then `x + y` is one of `v + w`. 

### `New.eventually_norm_sub_le_of_isExpLimit`

 The main estimate. Let `C` be a closed set containing `0` on which `ψ` inverts `φ` and `φ` is
continuous, with `φ 0 = 0`, `ψ 0 = 0`, addition read in the chart staying in `C` near `0` and having
strict derivative `(v, w) ↦ v + w` at `0`. If `x` is an exponential limit of a small `v`, then `x`
lies in the chart and `φ x = v` up to a relative error `ε`. 

### `New.analyticAt_chart_comp_of_hasFDerivAt`

 A homomorphism `e : V →+ G` read in the chart is analytic at `0`. Here addition read in the
chart is analytic at `0`, `φ 0 = 0`, `e` stays in the chart near `0` (`ψ (φ (e v)) = e v`), and
`φ ∘ e` has derivative the identity at `0`. 

### `New.isExpLimit_fderiv_apply`

 The universal property of exponential limits. Let `ψ` invert `φ` near `0`, with `φ 0 = 0`. For a
homomorphism `γ : P →+ G`, continuous at `0` and with `φ ∘ γ` differentiable at `0`, `γ z` is an
exponential limit of `F z`, where `F` is the derivative of `φ ∘ γ` at `0`. 

### `New.exists_lie_exponential`

 The exponential map. Let `G` be a compact commutative topological group and `φ : G → V` a chart
at `0`: `φ 0 = 0`, and `φ`, `ψ` are inverse to each other near `0`, with `φ` continuous near `0` and
`ψ` at `0`. Let addition be analytic in the chart. Then some homomorphism `e : V → G` has (a) a
lattice as kernel; (b) `ψ ∘ φ ∘ e = e` near `0`, and `φ ∘ e` analytic at `0` with derivative the
identity; (c) image of finite index; (d) every homomorphism `γ` from a finite-dimensional complex
normed space, continuous at `0` and differentiable at `0` in the chart, is `e ∘ F` for a continuous
linear `F`. 

 ## Classical topology, charts, compactness and uniformisation 

### `instance : TopologicalSpace (ComplexPoint A)`

 The classical topology on the complex points of `A`. It is generated by the sets of points that
lie in an open `U` (`LandsIn x.1 U`) and at which a function `f : PointFn` regular on `U`
(`IsRegularOn f U`), evaluated at `ℂ` and the point, takes a value in a given open set `O`. 

### `continuousAt_complexPoint_iff`

 A family `γ` of complex points is continuous at `t₀` for the classical topology iff, for
every open `U` containing `γ t₀` and every function `f` regular on `U`, the point `γ t` lies
in `U` for `t` near `t₀` and `t ↦ f (γ t)` is continuous at `t₀`. 

### `exists_zero_set_chart`

 The zeros of an analytic map `F : ℂ^ι → ℂ^σ` near a zero `p₀` with onto derivative have an
analytic chart `c` to `ℂᵈ`, `d = #ι - #σ`, with analytic local inverse `g`. 

### `ofSection_aeval_eq_eval`

 Let `P` present `Γ(A, U)` over `Γ(Spec ℂ, V)`, the algebra map being `A.hom.appLE V U e`. At
a complex point `y` of `U`, a polynomial `q` in the generators takes the value of the polynomial
function of `q` (constants evaluated at the base point) at the coordinates of `y`. 

### `surjective_fderiv_relations`

 Let `P` be a submersive presentation of `Γ(A, U)` over `Γ(Spec ℂ, V)` and `x` a complex point of
`U` at which each `aeval P.val q` takes the value of the polynomial function of `q` at the
coordinates of `x`. Read the relations of `P` as polynomial functions on `ℂ^ι`; their derivative at
the coordinates of `x` is onto, because the Jacobian minor of `P` is a unit. 

### `exists_point_of_relations_eq_zero`

 Let `P` present `Γ(A, U)` over `Γ(Spec ℂ, V)`, the algebra map being `A.hom.appLE V U e`, for
affine opens `U` and `V`. Every zero `p` of the relations of `P`, read as polynomial functions on
`ℂ^ι`, is the vector of coordinates of a complex point of `U`. 

### `exists_holomorphic_chart`

 A scheme smooth of relative dimension `d` over ℂ has a holomorphic chart at every complex point
`x`: maps `φ` to ℂᵈ and `ψ` back with `φ x = 0`, such that `ψ` inverts `φ` near `x` and near `0`,
`φ` is continuous near `x`, `ψ` is a holomorphic family at `0`, and along every holomorphic family
`γ` through `x` the map `φ ∘ γ` is analytic, with derivative zero in each direction in which `γ`
is constant to first order. 

### `LineBundle.IsProjEmbedding.compactSpace_complexPoint`

 The complex points of a projective variety `A`, embedded by the linear system
`N : LineBundle A.left ι` with `ι` finite, are compact in the classical topology: they are a
continuous image of a closed subset of the unit sphere. 

### `isTopologicalAddGroup_complexPoint`

 On the complex points of an abelian variety with a projective embedding, addition and negation
are continuous: they are morphisms of schemes. 

### `holomorphicAt_of_analyticAt_chart_comp`

 Let `φ`, `ψ` be a chart at `0` of the complex points of `A`, with `φ 0 = 0` and `ψ` holomorphic
at `0`, and let `e` be a homomorphism from `ℂᵈ` with `φ ∘ e` analytic at `0` and `ψ ∘ φ ∘ e = e`
near `0`. Then `e` is a holomorphic family of points at `0`. 

### `LineBundle.IsProjEmbedding.nonempty_uniformisation`

 Uniformisation: an abelian variety A over ℂ, smooth of relative dimension d and embedded in
projective space by a linear system N, admits a uniformisation ℂ^d/L ≅ A(ℂ), with L a lattice in
ℂ^d. 
