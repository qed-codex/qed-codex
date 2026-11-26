---
{
  "module": "src/Lib/DiscreteSeries/Bruhat/ComplexPlace.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/DiscreteSeries/Bruhat/ComplexPlace.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/DiscreteSeries/Bruhat/ComplexPlace.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The place ℂ: polar coordinates, Cartan decomposition and the measure of the hyperboloid

The archimedean instance of the local theory: the place `ℂ` and the top floor `ϱ` of the group
`New.Shape.G₁`, the unitary group of `ϱ` hyperbolic planes plus `V_ϱ = X₀ ⊕ ℂ z`, where `X₀ = ℂ^κ`
is standard and `h(z, z) = -1`. `New.RealPlace.embedH` embeds `U(X₀)` (written `U 1`) in it.
`floorGroup l` is the subgroup that fixes the basis vectors of the floors below `l`.

* `New.Floors.complexPlace`, `New.Floors.complexBasis`: `ℂ` is a place (`New.Floors.Place`); a
  hyperbolic basis of `V_ϱ`.
* `New.Floors.lintegral_eq_polar`: polar coordinates on `ℂ^κ` by the unitary group.
* `New.Floors.cellChart`, `New.Floors.cellDensity`, `New.Floors.cellLaw`: for each floor a chart
  `ℂ → G₁` (a boost at the top for `c ≠ 0`, a Weyl element otherwise), its density, and the law of
  its inverse.
* `New.Floors.cartan_decomposition`: the Cartan decomposition `U(X₀) · boost · U(X₀)` of an element
  of the top floor group whose corner entry `h(z, σ z)` has absolute value above 1.
* `New.Floors.map_orbitPoint_cellLaw_top`: polar coordinates for the measure of the hyperboloid
  `h(v, v) = -1`.

Notions from other files:
* `New.Shape.middleGram`: for a scalar N, the diagonal matrix on κ plus one point, with entries 1 on
  κ and −N at the extra point.
* `New.Floors.FloorGroups.orbitPoint`: for b ≤ ϱ and an isometry g, the vector g⁻¹f_b, where
  f = (e_0, …, e_{ϱ-1}, z) is the frame; `𝔰.top` is the position ϱ of z.
* `New.Floors.HyperbolicBasis.floorQuadricMeasure`: the measure on a quadric in V_b, a level set of
  v ↦ h(v, v) (by default h(f_b, f_b)): the image of `New.Floors.Place.quadricMeasure` under the
  basis `F.floorBasis b`.
* `New.realFrameGram`: for y in G₁, the (ϱ+1)×(ϱ+1) complex matrix Z(y) of products h(f_j, y f_l) of
  the frame with its translate.

## Relation to the literature

Known results: polar coordinates on ℂ^κ, the Cartan decomposition of a unitary group of rank one,
and the invariant measure of the hyperboloid h(v, v) = −1, here written in the coordinates of the
top floor. Source: Knapp, Lie Groups Beyond an Introduction; Helgason, Groups and Geometric
Analysis, Ch. I §5.


### `complexPlace`

 The place `ℂ`: `τ = 1/2`, `δ = i/2`, `ν` the image of Lebesgue measure under `r ↦ r i`,
modulus `‖x‖ ^ 2`, character `x ↦ exp (x - x̄)` and constant `c = π ^ 2`. 

### `complexBasis`

 For the fixed index k₀ of κ (`𝔰.k₀`), the basis of V_ϱ = X₀ ⊕ ℂz made of the hyperbolic pair
(1+i)/2·(x_{k₀} ± z) and the orthonormal vectors x_i, i ≠ k₀. 

### `lintegral_eq_polar`

 Polar coordinates on `ℂ^κ`, with `m = |κ|`: for an index `k` in `κ` and measurable
`g : ℂ^κ → [0, ∞]`, `∫ g(ω) dω = ∫₀^∞ π^m r^(m-1) / (m-1)! ∫_{U(m)} g(h (√r x)) dh dr`, where `x` is
the basis vector of index `k`, `r` is the squared norm and `dh` is the Haar probability measure. 

### `cellBoost`

 The boost in the plane of k₀ and z with parameter a, for 1 ≤ |a|. With s = √(|a|² - 1) it acts
on that plane by the matrix with rows (conj a, s) and (-s, -a), and it fixes the other basis
vectors. 

### `continuous_cellBoost`

 The boost depends continuously on its parameter. 

### `one_le_norm_div_min`

 For a ≠ 0 the point a / min(1, |a|) lies outside the open unit disc. 

### `cellChart`

 The chart of the big cell of floor l. On the top floor and for c ≠ 0 it is the boost at
c / min(1, |c|), which is c if 1 ≤ |c| and c / |c| otherwise. In all other cases it is
`floorWeyl l c`. 

### `cellDensity`

 The density of floor l at c: |c|^{2(k−1)+4(ϱ−l)} for l < ϱ; otherwise
2π^k((|c|²−1)⁺)^{k−1}/(k−1)!; k = |κ|. For l ≥ ϱ and |c| ≤ 1 this is 0 if and only if k > 1. 

### `cellLaw`

 The measure on G₁ that is the image of the density `New.Floors.cellDensity` of floor l times dc
on ℂ under c ↦ w_l(c)⁻¹ (`New.Floors.cellChart`). 

### `cellChart_top_of_one_le`

 On the top floor and for 1 ≤ |c|, the chart is the boost at c. 

### `cellBoost_mem_floorGroup`

 For 1 ≤ |c| the boost at c fixes the basis vectors of the floors below the top, that is, it
lies in `floorGroup ϱ`. 

### `cellChart_mem_floorGroup`

 The chart of floor l takes its values in the group of floor l, which fixes the basis vectors
of the floors below l. 

### `embedH_mem_floorGroup`

 The embedding of U(X₀) in G₁ takes its values in the group of the top floor, which fixes the
basis vectors of all floors below ϱ. 

### `measurable_cellChart`

 The chart of floor l is a measurable function of its parameter. 

### `measurable_cellDensity`

 The density of floor l is a measurable function on ℂ. 

### `realFrameGram_cellChart`

 For `1 < ‖c‖` the boost `w = cellChart 𝔰 ϱ c` has `h(z, w z) = c`: this is the entry at
(`top`, `top`) of the matrix `realFrameGram` of products of the frame with its translate by `w`,
`top` being the position of `z`. 

 ### The top floor: Cartan decomposition and the hyperboloid 

### `cartan_decomposition`

 Cartan decomposition of `U(V_ϱ)`, the isometry group of the form `middleGram 1` (diagonal: 1 on
X₀, indexed by κ, and −1 at z). Let `σ` fix the basis vectors of the floors below the top
(`σ ∈ floorGroup ϱ`) and let `c = h(z, σ z)`, the last diagonal entry of `realFrameGram σ`, have
`|c| > 1`. Then `σ = k w_ϱ(c) k'` for some `k`, `k'` in `U(X₀)`, embedded by `embedH` (identity off
X₀), where `w_ϱ(c)` is the boost `cellChart 𝔰 ϱ c`. 

### `hyperboloidPoint`

 The point √(Γ + |c|²) h x + c z of X₀ ⊕ ℂz, in the coordinates `BesselIndex` of the whole space
(`definiteCols` puts X₀ into them), for a real level Γ and a pair (c, h), x being the basis vector
at k₀. For Γ + |c|² ≥ 0 it lies on the hyperboloid h(v, v) = Γ. 

### `hyperboloidMeasure`

 The image of S((Γ + |c|²)⁺) dc dh under `hyperboloidPoint Γ`, where S is `sphereDensity k`,
S(r) = 2π^k r^(k−1)/(k−1)! with k = |κ|, and dh is the Haar probability measure of U(X₀). For k > 1
it is a measure on the hyperboloid h(v, v) = Γ of V_ϱ, written in polar coordinates. 

### `lintegral_hyperboloidMeasure`

 An integral against `hyperboloidMeasure Γ` is the iterated integral over c and h of the
integrand at `hyperboloidPoint Γ (c, h)`, with the density S((Γ + |c|²)⁺). 

### `star_dotProduct_hyperboloidPoint`

 For Γ + |c|² ≥ 0 the point `hyperboloidPoint Γ (c, u)` has h(v, v) = Γ. 

### `lintegral_slice_eq_hyperboloid`

 Polar coordinates on the slice of X₀ ⊕ ℂz with coordinate c at z, for |κ| > 1: with r the
squared norm of the part in X₀ and r = 2t + |c|², the integral over x ∈ X₀ of f(h(v, v), v) is,
where v is (x, c) in the indices `MiddleIndex` of X₀ ⊕ ℂz, put by `inclMatrix` into the coordinates
`BesselIndex` of the whole space, ∫ S((2t + |c|²)⁺) ∫ f(2t, `hyperboloidPoint (2t) (c, u)`) du dt, S
being `sphereDensity k`. 

### `isDisintegration_hyperboloidMeasure`

 For k = |κ| > 1, let h be standard on X₀ = ℂ^κ with h(z, z) = −1. The measures
`hyperboloidMeasure (2 Im β)` on the level sets h(v, v) = 2 Im β, β skew, disintegrate the volume of
V_ϱ = X₀ ⊕ ℂz along h(v, v). The volume is extended by zero to the whole space, and integrating
f(δ⁻¹β, v) against them and then over β = ri (Lebesgue in r) gives the integral of f(h(v, v), v);
here δ = i/2, so δ⁻¹β = 2 Im β. 

### `map_orbitPoint_cellLaw_top`

 Polar coordinates on the hyperboloid h(v, v) = −1 of V_ϱ = X₀ ⊕ ℂz, where X₀ has an orthonormal
basis indexed by κ and h(z, z) = −1, assuming `1 < 𝔰.k` (i.e. |κ| > 1). Let c have the law
`cellDensity`(c) dc, let w_ϱ(c) be the boost `cellChart 𝔰 ϱ c`, and let h ∈ U(X₀), embedded in G₁ by
`embedH`, have the Haar probability law. Then the map σ ↦ σ⁻¹z (`orbitPoint` at the top position)
carries the law of w_ϱ(c)⁻¹h to `floorQuadricMeasure`, the image of `quadricMeasure` of that
hyperboloid under the basis `complexBasis 𝔰`. 
