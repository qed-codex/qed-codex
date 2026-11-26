---
{
  "module": "src/Lib/General/Measure/QuadricDisintegration.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/General/Measure/QuadricDisintegration.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/General/Measure/QuadricDisintegration.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Measures on hermitian quadrics: existence and uniqueness of disintegrations

This file develops measure theory on hermitian quadrics over a "place" `A`. The result is a measure
that is written `Dirac(h(x, x) - Γ) dx` and is determined by the disintegration property. Quadrics
and disintegrations are indexed by skew elements `b`, with `Γ = δ⁻¹ * b` for a skew unit δ.

* `New.Floors.Place`: the data and properties of a place. Here `skewMeasure`, written ν, is a Haar
  measure on the skew elements, and `skewUnit`, written δ, is a skew unit. For hermitian Γ, the
  element δΓ is skew (`New.Floors.Place.skewUnitMul`).
* `New.Floors.Place.flatChart`, `New.Floors.Place.quadricMeasure`: for hermitian `T`, an explicit
  chart of `h(x, x) = δ⁻¹ * b`, and the image of the flat measure under it. Here `h` is a hyperbolic
  plane plus `T` (`New.Floors.planeSumGram`).
* `New.Floors.Place.IsDisintegration`: disintegrations along `h(x, x)`. For hermitian `T`, the chart
  measures form a disintegration of the volume (`New.Floors.Place.isDisintegration_quadricMeasure`).
  Disintegrations are unique at every skew `b` (`New.Floors.Place.IsDisintegration.unique`). They
  move along a matrix `M` with `Mᴴ * J * M = T` that has a left inverse
  (`New.Floors.Place.IsDisintegration.map`).

Notation: for a ring with involution, `skewAdjoint A` is the group of elements with `star x = -x`,
and `x⁻¹ʳ` is the ring inverse, which is zero at non-units. The vector `x ⊕ᵥ y` on a disjoint union
of index sets is `x` on the first part and `y` on the second. The group `U T` consists of the
invertible matrices g with `gᴴ * T * g = T`.


### `TraceOne`

 A choice of an element τ = `element` with τ + τ̄ = 1 in a commutative ring with involution. 

### `TraceOne.element`

 The chosen element τ. 

### `TraceOne.element_add_star`

 τ has trace one: τ + τ̄ = 1. 

### `Place`

 A place, such as ℂ or a finite product of completions: a locally compact star ring A with Haar
volume, an element τ = `element` of trace one, a skew unit δ, a Haar measure ν on the skew elements,
a modulus `modulus` that describes how matrices scale the volume, a unitary additive character ψ,
and a bound c = `kernelBound` in [0, ∞] such that some kernel has Fourier transform of L¹ norm at
most `c`. 

### `Place.skewUnit`

 A unit δ, skew by `star_skewUnit`. 

### `Place.skewMeasure`

 A measure ν on the skew elements, Haar by `haar`. 

### `Place.modulus`

 The modulus, a multiplicative map to [0, ∞]. 

### `Place.ψ`

 An additive character ψ. 

### `Place.kernelBound`

 A bound for the L¹ norm of the Fourier transform of the kernel in
  `exists_plancherel_kernel`. 

### `Place.haar`

 ν is an additive Haar measure. 

### `Place.continuous_psi`

 ψ is continuous. 

### `Place.measurable_modulus`

 The modulus is measurable. 

### `Place.star_skewUnit`

 δ is skew: δ̄ = −δ. 

### `Place.measurePreserving_split`

 The map (a, b) ↦ τδ⁻¹a + b on pairs of skew elements carries ν × ν to the volume of A. 

### `Place.modulus_star_and_neg`

 The modulus is invariant under conjugation and under negation. 

### `Place.map_mulVec_volume`

 An invertible matrix M maps the volume of Aⁿ to (`modulus` (det M))⁻¹ times itself. 

### `Place.ae_isUnit`

 Almost every element is a unit. 

### `Place.exists_locallyIntegrable_bound`

 On units, the power −1/2 of the modulus has a locally integrable majorant:
  (`modulus` u)⁻¹ ≤ |g(u)|² for some locally integrable g. 

### `Place.norm_psi`

 The values of ψ have absolute value one. 

### `Place.exists_plancherel_kernel`

 There is a continuous integrable G ≥ 0 with G(0) = 1 whose Fourier transform
  z ↦ ∫ G(v) ψ(v̄z) dv has L¹ norm at most c. 

 ### Skew elements 

### `skewPart`

 The skew element x − x̄ attached to x. 

### `hermitianMul`

 The product xβ of a hermitian element x and a skew element β, as a skew element. 

### `isClosed_skewAdjoint`

 The skew elements form a closed subset of `A`, so they inherit a Polish and a locally compact
topology. 

 ### Lemmas on measures, and the hyperbolic plane plus a form 

### `lintegral_eq_mul_lintegral_map`

 For a map f : Z → Z, a measure ζ on Z with ζ.map f = c⁻¹ • ζ, and c neither zero nor infinite,
the integral of g against ζ is c times the integral of g against the image ζ.map f. 

### `lintegral_congr_of_ae_imp`

 For a measure ζ on Z and f, g : Z → [0, ∞], if p holds ζ-almost everywhere and f = g where p
holds, then f and g have the same lower integral. 

### `lintegral_le_of_ae_imp`

 For a measure ζ on Z and f, g : Z → [0, ∞], if p holds ζ-almost everywhere and f ≤ g where p
holds, then the lower integral of f is at most that of g. 

### `lintegral_lt_top_of_hasCompactSupport`

 A continuous function f ≥ 0 of compact support has a finite integral against a measure ζ that
is finite on compact sets. 

### `continuous_lintegral_of_compact_support`

 Let F ≥ 0 be jointly continuous in x in X and y in Z, vanishing for y outside a compact set k,
and let ζ be finite on compact sets. Then x ↦ ∫ F(x, y) dζ(y) is continuous. 

### `continuous_lintegral_and_lt_top`

 Let F ≥ 0 be jointly continuous in a skew element x of A and y in Z, vanishing for y outside
a compact set k, and let ζ be finite on compact sets. Then x ↦ ∫ F(x, y) dζ(y) is continuous and
finite. 

### `measurePreserving_sumElim`

 For a place A and finite index sets ι, κ, joining two vectors is a volume-preserving map
from A^ι × A^κ to A^(ι ⊔ κ). 

### `measurePreserving_pair_sumElim`

 For a place A and a finite index set ι, the map (s, t, w) ↦ (s, t) ⊕ w from A × A × A^ι to
vectors indexed by the disjoint union of Fin 2 and ι preserves the volume. 

### `planeSumGram`

 The Gram matrix of a hyperbolic plane plus the form T: block diagonal with blocks (0 1; 1 0)
and T. 

### `instance : BorelSpace (U T)`

 The unitary group of the Gram matrix T is a Borel space. 

### `flatChart`

 The flat chart of the quadric h(v, v) = δ⁻¹b in a hyperbolic plane (e, e') plus T:
(t, w, a) ↦ (t̄⁻¹τ(δ⁻¹b − h(w, w)) + ta)e + te' + w, with a skew. Here t̄⁻¹ is the ring inverse,
which is zero when t̄ is not a unit; the image point lies on the quadric when T is hermitian and t
is a unit. 

### `quadricMeasure`

 The image of dt dw dν(a) under the flat chart `New.Floors.Place.flatChart`. For hermitian T it
is the fiber measure dv / dh(v, v) on the quadric h(v, v) = δ⁻¹b
(`isDisintegration_quadricMeasure`).

This makes Weil's fiber measures for a submersion explicit for the map v ↦ h(v, v), which is a
submersion at points whose coordinate t is a unit. 

 ### Disintegrations along the form, and scaling of the volume 

### `IsDisintegration`

 The family l_b, indexed by skew b, disintegrates μ along h(x, x) = x̄ᵀJx. For continuous
compactly supported f ≥ 0, the integrals ∫ f dl_b are finite and continuous in b. Moreover, for
measurable f, we have ∫ f(h(x, x), x) dμ = ∬ f(δ⁻¹b, x) dl_b dν(b). 

### `IsDisintegration.continuous_and_lt_top`

 For continuous f ≥ 0 of compact support, b ↦ ∫ f d`l b` is continuous on the skew elements and
  finite. 

### `IsDisintegration.lintegral_eq`

 For measurable f, the integral of f(x̄ᵀJx, x) against μ is the integral over skew b, against
  ν, of the integral of f(δ⁻¹b, x) against `l b`. 

### `measurePreserving_mulVec`

 A matrix T over a place A whose determinant d satisfies d̄d = 1 preserves the volume of A^ι. 

### `map_mul_volume`

 Multiplication by a unit u maps the volume of A to (`modulus` u)⁻¹ times itself. 

### `map_skewMeasure_hermitianMul`

 For a place `A` (a locally compact star ring carrying a Haar measure ν = `skewMeasure` on its
skew elements and a modulus `modulus` describing how matrices scale volume), multiplication β ↦ uβ
by a hermitian unit `u` maps ν to (`modulus` u)^(-1/2) times ν. 

### `map_skewMeasure_mul_unit`

 For a hermitian unit u, the map β ↦ skew part of τuβ (τ the trace-one element of the place, skew
part of x being x − x̄), which equals β ↦ uβ, maps the measure ν on the skew elements to (`modulus`
u)^(-1/2) times ν. 

 ### Properties of the chart and of disintegrations 

### `skewUnitMul`

 The skew element δΓ of a hermitian element Γ. The default proof of star Γ = Γ applies when Γ
is a diagonal entry of a matrix of class `IsHermitianUnit` (hermitian and invertible). 

### `form_flatChart`

 For a place `A` with skew unit δ (`skewUnit`) and trace-one element τ, let `T` be a hermitian
ι×ι matrix, `b` a skew-adjoint element, and h the hermitian form whose Gram matrix `planeSumGram T`
is a hyperbolic plane (e, e') plus `T`. For p = ((t, w), a) with t a unit, w : ι → A and a
skew-adjoint, the flat-chart point x = (t̄⁻¹τ(δ⁻¹b − h(w, w)) + ta)e + te' + w (`flatChart T b p`)
satisfies h(x, x) = star x ⬝ᵥ `planeSumGram T` *ᵥ x = δ⁻¹b, that is, x lies on the quadric of b. 

### `skewMeasure_le_of_sub_mem`

 Let ν be the Haar measure on the skew elements, δ the skew unit and τ the element of trace one.
Let S be a set of skew elements and u a unit. Suppose that for any two pairs p, q in S × S, with
(β, β') = p − q, the element u(τδ⁻¹β + β') lies in C. If vol(C) / `modulus` u ≤ x², then
ν(S) ≤ x. 

### `IsDisintegration.isFiniteMeasureOnCompacts`

 The measures of a disintegration along the form with matrix T are finite on compact sets. 

### `IsDisintegration.unique`

 Two disintegrations l, l' of the same measure μ along the form h(x, x) = x̄ᵀTx agree at every
skew element b. Here `IsDisintegration` requires two things: that ∫ f dl_b be finite and continuous
in b for continuous compactly supported f ≥ 0, and that ∫ f(h(x, x), x) dμ = ∬ f(δ⁻¹b, x) dl_b dν(b)
for measurable f. The continuity in b is why equality holds at every b rather than only almost
everywhere. 

### `IsDisintegration.map`

 Let l disintegrate μ along the form with matrix T: measurable f satisfy ∫ f(x̄ᵀTx, x) dμ = ∬
f(δ⁻¹b, x) dl_b dν(b), and ∫ f dl_b is finite and continuous in b for continuous compactly
supported f ≥ 0. If M has a left inverse L and pulls the form J back to T, then the images of l_b
under M disintegrate the image of μ along J. 

### `lintegral_iSup_fibre_lt_top`

 Let `T` be any square matrix over `A` (not assumed hermitian), ν the Haar measure `skewMeasure`
on the skew elements, and `K` a compact subset of `Fin 2 ⊕ ι → A`. Let h be the form with Gram
matrix `planeSumGram T` (a hyperbolic plane e, e' plus T), and consider the flat chart
`flatChart T b` ((t, w), a) ↦ (t̄⁻¹τ(δ⁻¹b − h(w, w)) + ta)e + te' + w, where t̄⁻¹ is zero if t̄ is
not a unit. Then the supremum over skew `b` of the ν-measure of the fibre {a | flatChart T b ((t,
w), a) ∈ K} has finite lower integral over (t, w) ∈ A × (ι → A). 

### `lintegral_form_eq_lintegral_flatChart`

 Let T be hermitian, t a unit, w a vector and h the form of `planeSumGram T`. The integral over
s of f(h(x, x), x) at x = (s, t, w) is the double integral over skew b, a of f(δ⁻¹b, x) at the
chart point x of ((t, w), a) on the quadric of b. 

### `continuous_lintegral_flatChart`

 For T hermitian, f ≥ 0 continuous of compact support and a base point p = (t, w) with t a
unit, the integral of f over the fibre of the flat chart at p is continuous in b. 

### `lintegral_flatChart_le`

 For f ≥ 0 continuous of compact support, the integral of f over the fibre of the flat chart at
p = (t, w) is at most sup f times the supremum over b of the ν-measures of the sets
{a | the chart point at (p, a) for b lies in the topological support of f}. 

### `isDisintegration_quadricMeasure`

 Let `T` be hermitian and let h be the form with Gram matrix `planeSumGram T` (a hyperbolic plane
plus T). The measures `quadricMeasure T b` are the images of dt dw dν(a) under the flat chart. They
disintegrate `volume` along h(v, v): they are the fibre measures on h(v, v) = δ⁻¹b for skew b, with
base measure ν. 
