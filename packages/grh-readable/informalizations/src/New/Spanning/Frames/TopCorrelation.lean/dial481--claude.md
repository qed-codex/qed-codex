---
{
  "module": "src/New/Spanning/Frames/TopCorrelation.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Frames/TopCorrelation.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Frames/TopCorrelation.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Scaled orbital integrals of the finite Bessel vector on the floor group

A finite set of finite places is read as one ring (`IntegralPlace`); the docstrings call it a finite
place. This file defines the scaled orbital integrals `PlaceData.scaledOrbitalIntegral`. These are
normalized orbital integrals of the finite Bessel vector at the elements `w_p l⁻¹` with head `p` and
link `l⁻¹`. It also defines the integrand `PlaceData.unfoldedPairing` of their pairing. At a large
lattice datum it shows three things. The scaled orbital integrals are locally constant in the head
and on the floor group G^(ϱ). They vanish off a compact set. Their pairings are integrable over
`besselH`. It also writes the form `F.floorForm 𝔰.ϱ`, with a weight on the last diagonal entry of
`T.frameGram`, as an integral of these pairings. General lemmas give compactly supported step
extensions of locally constant functions and the nonnegativity of sums of integrals against a
matrix.

## Main definitions and results

* `New.Floors.IntegralPlace.IsLargeLatticeData.exists_isCompact_scaledOrbitalIntegral_support`: Let
  `F` be a large lattice datum. The scaled orbital integral `scaledOrbitalIntegral Z p l`, a density
  times `∫ W y ⊗ (W (l w_p⁻¹ y))^*` over the unitary group, with `W` the finite Bessel vector of `Z`
  and `w_p` the Weyl element of the head `p`, vanishes for the `l` in the floor group G^(ϱ) outside
  some compact set.
* `New.Floors.IntegralPlace.IsLargeLatticeData.inner_scaledOrbitalIntegral`: At a large lattice
  datum `F` and for `l` in the floor group G^(ϱ), the pairing of the scaled orbital integrals with
  heads `p`, `q` at `l` is the density `F.headDensity 𝔰.ϱ p q` of the two heads times the integral
  of the integrand `unfoldedPairing Z p q l` over two copies of the group.

Notions from other files:
* `T.floorGroup l`, written G^(l), fixes the basis vectors of the floors below `l` in the unitary
  group `T.G`; `besselH` is `T.floorGroup 𝔰.n` with `𝔰.n = 𝔰.ϱ + 1`, which also fixes the last frame
  vector `z`, in position `𝔰.top`; `orbitPoint 𝔰.top l` is `l⁻¹ z`.
* Place data `F` gives measures on these groups (`F.measureH` on `besselH`) and a congruence
  subgroup `F.congruenceSubgroup`; `P.IsLargeLatticeData F` says that it is large lattice data at a
  finite place `P`.
* `Z` is a group between `F.congruenceSubgroup` and the integral unitary group, and `Z.besselVector`
  is the vector of the finite Bessel functions of the cosets of `F.congruenceSubgroup` in `Z`.
* `weylElem 𝔰.ϱ p` is the Weyl element of a sequence `p` of units. An element `w_p l⁻¹` with `l` in
  the floor group has head `p` and link `l⁻¹`. The sequence is a head for a gauge `Γ` (a family of
  compact bounds on entries) if its inverse partial products are bounded by the gauge.


### `sum_sum_mul_integral_nonneg`

 Let `R` be a complex matrix and `f a b` integrable functions. If `∑ a b, R a b * f a b x` is a
nonnegative real for every `x`, then `∑ a b, R a b * ∫ f a b` is a nonnegative real. 

### `lintegral_ofReal_re_sum_sum_mul`

 Let `R` be a complex matrix and `f a b` integrable functions. If `∑ a b, R a b * f a b x` is a
nonnegative real for every `x`, then the lower Lebesgue integral of these values is the real part
of `∑ a b, R a b * ∫ f a b`. 

### `eventually_forall_apply_add_smul_eq`

 Let `C` and `L` be compact sets of vectors over `A`, and let `φ` be locally constant along `Q`
at the points of `C`. Then for all scalars `b` near `0` one has `φ (x + b • v) = φ x` whenever
`x ∈ C`, `v ∈ L`, and both `x` and `x + b • v` lie in `Q`. 

### `exists_unit_forall_apply_eq_of_inv_smul_sub_mem`

 Let `C` and `L` be compact sets of vectors over a finite place `A`, and let `φ` be locally
constant along `Q` at the points of `C`. Then for some unit `u` one has `φ x = φ y` whenever
`x ∈ Q`, `y ∈ C ∩ Q` and `x - y` lies in `u • L`. 

### `exists_step_function_extension`

 Let `φ` be a function on vectors over a finite place `A`, supported in `C ∩ Q` with `C` compact,
locally constant along `Q` at the points of `C`, and invariant on its support under a group `H` of
matrices in `GL n R`, where `R = P.integers` is the ring of integers. Then `φ` agrees on `Q` with a
compactly supported function `Φ` that is invariant under small translations and under `H`. 

### `besselOrbitalIntegral_apply`

 The coordinate `(i, j)` of the orbital integral tensor `∫ W y ⊗ (W (γ⁻¹ * y))^* ∂μ`. 

### `besselOrbitalIntegral_congr`

 The orbital integral tensor `∫ W y ⊗ (W (γ⁻¹ * y))^* ∂μ` depends only on the values
`W (γ⁻¹ * y)` at the points `y` with `W y ≠ 0`. 

### `exists_ne_zero_of_besselOrbitalIntegral_ne_zero`

 If the orbital integral tensor `∫ W y ⊗ (W (γ⁻¹ * y))^* ∂μ` is not zero, then `W y` and
`W (γ⁻¹ * y)` are both nonzero for some `y`. 

### `IntegralPlace.modulus_eq_of_inv_mul_mem_units`

 Two units of a finite place whose quotient is a unit of the ring of integers `O` (also written
`P.integers`) have the same modulus. 

### `PlaceData.scaledOrbitalIntegral`

 The normalized orbital integral at the element `w_p l⁻¹` with head `p` and link `l⁻¹`, where
`w_p` is the Weyl element `weylElem 𝔰.ϱ p`: the density `F.headDensity 𝔰.ϱ p 1` times the
correlations of the finite Bessel vector of `Z` with its translate by `w_p l⁻¹`, indexed by pairs of
cosets. Functions of the link are written below as functions of its inverse `l`. 

### `PlaceData.besselVector_apply`

 The coordinate of the finite Bessel vector of `Z` at a coset `c` of `F.congruenceSubgroup` in
`Z`, in terms of the chosen representative `c.out`. 

### `PlaceData.besselVector_mul_left`

 Let `F` be a place datum of the form `T`, whose Gram matrix `T.splitGram` is hermitian and
invertible, and let `Z` be a group between `F.congruenceSubgroup` and the integral unitary group.
The finite Bessel vector of `Z`, whose coordinates are right translates of the Bessel function
`P.extendedBesselChar F.levelUnit`, is left invariant under the elements of `F.congruenceSubgroup`
in `besselH`, the fixer of the hyperbolic pairs and the last frame vector. 

### `PlaceData.besselVector_mul_right`

 The finite Bessel vector of `Z`, whose coordinates are translates of the Bessel function
`P.extendedBesselChar F.levelUnit`, is right invariant under the congruence group
`F.congruenceSubgroup`, which `Z` normalises. 

### `PlaceData.continuous_besselVector`

 The finite Bessel vector of `Z` is a continuous function on the unitary group `T.G`. 

### `PlaceData.unfoldedPairing`

 The integrand of the pairing of the scaled orbital integrals with heads `p`, `q` at the inverse
link `l`, on two copies of the group: with `W` the finite Bessel vector of `Z`, its value at
`(y₁, y₂)` is `⟪W y₁, W y₂⟫ * ⟪W ((w_q l⁻¹)⁻¹ y₂), W ((w_p l⁻¹)⁻¹ y₁)⟫`. 

### `PlaceData.continuous_unfoldedPairing`

 The integrand `unfoldedPairing Z p q l y` is continuous in the inverse link `l` and the pair
`y` of group variables together. 

### `frameGram_top_eq_of_mem_besselH`

 Factors in `besselH`, the fixer of the hyperbolic pairs and the last frame vector, do not change
the last diagonal entry of `T.frameGram x`, the matrix of products of the frame with its image under
`x`: for `g`, `k` in `besselH` the entries at `g x k` and at `x` agree. 

### `inv_weylElem_mul_inv_mul`

 For `s` in the floor group `T.floorGroup 𝔰.ϱ`, which commutes with the Weyl element
`weylElem 𝔰.ϱ r` (written `w_r`), one has `(w_r * (a * s⁻¹)⁻¹)⁻¹ * (s * x) = a * w_r⁻¹ * x` for all
`a`, `x`. 

### `exists_gauge_isHead`

 At a large lattice datum `F`, some `Γ : Gauge F` (a scale: a notion of size with a loss
Λ = `Γ.loss`) makes every sequence of units `r` near `p`, and every one near `q`, a head of length
`𝔰.ϱ` (`Γ.IsHead 𝔰.ϱ r`). This means that the inverses of the products `r 0 * ⋯ * r (l-1)`,
`l ≤ 𝔰.ϱ`, have size 1. 

### `eventually_scaledOrbitalIntegral_mul_eq_self`

 Let `F` be a large lattice datum. The scaled orbital integral `scaledOrbitalIntegral Z p l` is a
density depending on `p` times `∫ W y ⊗ (W (l w_p⁻¹ y))^*` over the unitary group, with `W` the
finite Bessel vector of `Z` and `w_p` the Weyl element of the head `p`. For `z = (r, s)` near
`(p, 1)` with `s` in the floor group G^(ϱ), it does not change when `p` is replaced by `r` and `l`
by `l * s`, for all `l` in G^(ϱ) at once. 

### `exists_isCompact_scaledOrbitalIntegral_support`

 Let `F` be a large lattice datum. The scaled orbital integral `scaledOrbitalIntegral Z p l`
vanishes for `l` in the floor group `T.floorGroup 𝔰.ϱ` outside some compact set. 

### `inner_scaledOrbitalIntegral`

 At a large lattice datum `F` and for `l` in the floor group G^(ϱ), the pairing of the scaled
orbital integrals with heads `p`, `q` at `l` is the density `F.headDensity 𝔰.ϱ p q` of the two heads
times the integral of the integrand `unfoldedPairing Z p q l` over two copies of the group. 

### `hasMatrixSize_of_unfoldedPairing_ne_zero`

 Let `p` and `q` be heads for a gauge `Γ` of a large lattice datum, and let `l` lie in the floor
group G^(ϱ). If the integrand `unfoldedPairing Z p q l` of the pairing of the scaled orbital
integrals is nonzero at `(y₁, y₂)`, then the entries of `y₁` and `y₂` have size `60 * 𝔰.n ^ 2` for
`Γ`. 

### `exists_lintegral_enorm_unfoldedPairing_le`

 At a large lattice datum `F` there is a finite constant `C` such that the integral over `k` of
the norm of the integrand `unfoldedPairing Z p q (k * l) (y₁, y₂)` is at most `C` times the norm of
`⟪W y₁, W y₂⟫`, with `W` the finite Bessel vector of `Z`. Here `k` is integrated against
`F.quotientMeasureFrom i`, the convolution of the measures of the floors from `i` on. 

### `integrable_unfoldedPairing`

 Let `F` be a large lattice datum, `i ≥ 𝔰.ϱ`, and `l` in the floor group `T.floorGroup 𝔰.ϱ`. The
integrand `unfoldedPairing Z p q (k * l) (y₁, y₂)` of the pairing of the scaled orbital integrals at
`k * l` is integrable in `(k, y₁, y₂)`. Here `k` is integrated against `F.quotientMeasureFrom i`,
the convolution of the measures of the floors from `i` on. 

### `integrable_inner_scaledOrbitalIntegral`

 If `F` is a large lattice datum and `l` lies in `T.floorGroup 𝔰.ϱ`, the group fixing every basis
vector of floor below `𝔰.ϱ`, then the inner product of `scaledOrbitalIntegral Z p (k * l)` and
`scaledOrbitalIntegral Z q (k * l)` is integrable in `k` for `F.measureH`. 

### `_root_.New.Floors.PlaceData.unfoldedPairing_mul_inv`

 For `a` and `s` in the floor group `T.floorGroup 𝔰.ϱ`, the integrand `unfoldedPairing Z p q` at
the inverse link `a * s⁻¹` and the pair `(s * y, s * y * x)` is ⟪W (s y), W (s y x)⟫ times ⟪W (r (a
w_p⁻¹ y) x), W (a w_p⁻¹ y)⟫. Here `W = Z.besselVector`, `w_p = weylElem 𝔰.ϱ p` and
`r = weylRatio 𝔰.ϱ p q = w_q⁻¹ w_p`. 

### `identDistrib_unfoldedPairing`

 Let `F` be a large lattice datum and `φ` a measurable weight on the group, left and right
invariant under `besselH`, the fixer of the hyperbolic pairs and the last frame vector. Then `Φ`,
the integrand `unfoldedPairing Z p q` at `(l, y₁, y₂)` weighted by `φ l⁻¹`, and `Ψ`, the integrand
of the form `F.floorForm 𝔰.ϱ` with all its integrals written out, have the same law under the
product measures shown. 

### `_root_.New.Floors.integral_prod_prod_prod_prod_symm`

 Fubini's theorem for the first four variables of an integrable function on a product of five
spaces with s-finite measures. 

### `floorForm_top_eq_integral`

 Let `F` be a large lattice datum, and let the weight `φ x` be `P.ψ (ξ * θ)`, with `P.ψ` the
additive character of the place and `θ = ⟨z, x z⟩` the last diagonal entry of `T.frameGram x`, `z`
being the last frame vector. Let `f l` be `φ l⁻¹` times the pairing of the scaled orbital integrals
with heads `p`, `q` at the inverse link `l`. Then `f` is integrable for the measure
`F.partialGroupMeasure 𝔰.ϱ 2` of the top floors, and its integral is the form `F.floorForm 𝔰.ϱ`: the
density of the heads times an integral, weighted by `φ`, of a product of two correlations of the
finite Bessel vector of `Z`. 
