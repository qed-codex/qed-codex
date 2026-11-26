---
{
  "module": "src/New/Spanning/Frames/Depth.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Frames/Depth.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Frames/Depth.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Depth

For a fixed position few frame vectors are deep, and for a fixed frame vector few translates of the
position leave it shallow. Both are read on vectors that look the same from the two points. A
position far from 1 has a deep vector, and a head keeps the first vectors shallow. The letters
G^(l), R^(l), U_(<l), Y^(l) are those of the head of `New.Spanning.Frames.Lengths`, and K, M those
of `New.Spanning.Frames.Levels`.

## Main definitions and results

* `New.Floors.PlaceData.IsCommonBound.depth_le`, `New.Floors.Gauge.floorMassLe_depth_pow`,
  `New.Floors.Gauge.lintegral_depth_pow_section_le`: deep vectors are rare, also on a section.
* `New.Floors.Gauge.exists_lift_of_mem_closeBelow`,
  `New.Floors.Gauge.lintegral_heisenbergMeasure_inv_depth_le`: long coordinates force depth.
* `New.Floors.Gauge.lintegral_invDepthWeight_le`, `New.Floors.Gauge.lintegral_depthWeight_le`: the
  two halves of the weight over all floors of a head.
* `New.Floors.Gauge.hasMatrixSize_sub_one_of_stableProducts`,
  `New.Floors.Gauge.exists_unit_mem_stableProducts_of_isHead`: bounded depths bound the position;
  under a head, each 𝔡_a with a < j contains a unit with bounded inverse.

Notions from other files:
* `F.IsStable l g g' ω`: ω is orthogonal to the e_b, b < l, and (g⁻¹ ω, g'⁻¹ ω') lies in
  `F.closePairs` for some ω' congruent to ω modulo these e_b.
* `F.stableProducts a x y`: the set 𝔡_a of the products ⟨e_a, ω⟩ with the ω stable at x and x y.
* `F.depth a x y`: the inverse of the volume of 𝔡_a.
* `F.depthWeight j x y`: the product over a < j of the depth^(-s), s = `F.volumeExponent`.
* `F.IsNear j g`: ξ g lies in the box `F.boxSet` for some ξ in `partialUnitriangularGroup j`.

## Relation to the literature

See `New.Spanning.MainTerm.EnergyEstimate` for related work.


### `IsShortFrom.isStable`

 A vector ω orthogonal to the e_b, b < l, and short from the points g and g' (the pair
(g⁻¹ ω, g'⁻¹ ω) is close) is stable at g and g', with the same lift at both points. 

### `isOpen_setOf_mem_stableProducts`

 The sets 𝔡_a = `F.stableProducts a x y` form an open family in (x, y). 

### `stableProducts_mul_left`

 The set 𝔡_a = `F.stableProducts a x y` of the points x and x y does not change when both points
are moved by an element ξ of R^(a+1) = `partialUnitriangularGroup (a + 1)`. 

### `stableProducts_unipotentBelow_mul`

 The set 𝔡_a of the points x and y, which is `F.stableProducts a x (x⁻¹ * y)`, does not change
when y alone is moved by an element ν of U_(<a) = `unipotentBelow a`. 

### `volume_stableProducts_ne_zero_ne_top`

 For all x, y in the unitary group `T.G`, the subset 𝔡_a = `F.stableProducts a x y` of A has
nonzero finite volume. 

### `depth_ne_zero`

 The depth, the inverse of the volume of 𝔡_a, is nonzero. 

### `depth_ne_top`

 The depth, the inverse of the volume of 𝔡_a, is finite. 

### `depth_mul_left`

 The depth of e_a at the points x and x y does not change when both points are moved by an
element ξ of `partialUnitriangularGroup (a + 1)`. 

### `depth_unipotentBelow_mul`

 The depth of e_a at the points x and y does not change when y alone is moved by an element ν
of `unipotentBelow a`. 

### `measurable_depth`

 The depth of e_a is a measurable function of the pair (x, y). 

### `IsCommonBound.depth_le`

 Let X' be the span of the columns of `F.orthonormalPart`, and let W be the set of common vectors
for g, x and v: the w in X' killed by the rows of v and short from g and g x. Let φ(u) bound the
inverse volume of ⟨u, W⟩, and let σ move W to vectors orthogonal to the e_b, b < a. Then the depth
of e_a at σ g and σ g x, the inverse volume of `F.stableProducts a (σ * g) x`, is at most φ(y_X),
where y = σ⁻¹ e_a = `orbitPoint a.castSucc σ` and y_X is the vector of the products of the basis
vectors of X' with y. 

### `depthWeight_succ`

 The weight of length a + 1 is the weight of length a times depth^(-s) of e_a, where
s = `F.volumeExponent`. 

### `depthWeight_ne_zero_and_ne_top`

 The weight of length j, the product of the powers depth^(-s), is nonzero and finite. 

### `depthWeight_div_succ`

 The quotient of the weights of lengths a and a + 1 is the s-th power of the depth of e_a, where
s = `F.volumeExponent`. 

### `depthWeight_mul_left`

 The weight of length j at the points x and x y does not change when both points are moved by an
element ξ of `partialUnitriangularGroup j`. 

### `invDepthWeight_mul_left`

 The function `F.invDepthWeight j x`, the inverse of the weight of length j on the points near at
j and zero elsewhere, is left invariant under `partialUnitriangularGroup j`. 

### `measurable_depthWeight`

 The weight of length j is a measurable function of the pair (x, y). 

### `PlaceData.measurable_invDepthWeight`

 The function `F.invDepthWeight j x`, the inverse of the weight of length j on the points near at
j and zero elsewhere, is measurable. 

### `isOrthogonalBelow_orthonormalPart_mulVec`

 A combination of the orthonormal vectors, the columns of `F.orthonormalPart`, is orthogonal to
the frame vectors e_b with b < l and b < ϱ. 

### `floorMassLe_depth_pow`

 Deep vectors are rare. For x in the set `F.positions` and every g, take the s-th power of the
depth of e_a at σ g and σ g x. Integrate it for the measure `F.floorMeasure a` in σ, over the σ with
σ g near at a + 1. The integral is at most Λ^(10⁴ n) (`F.FloorMassLe`), where Λ = `Γ.loss` is the
constant of the gauge and n = `𝔰.n`. 

### `floorsConst`

 The bound Λ^(10⁶ n³) for all floors of a head together: at most n floors at Λ^(10⁶ n²) each,
with n = `𝔰.n` and Λ = `Γ.loss`, the constant of the gauge. 

### `mulVec_apply_inl_of_mem_floorGroup`

 An element g of `floorGroup l` does not change the coordinate of a vector at e_c for c < l. 

### `lintegral_depth_pow_section_le`

 Let the head p of length a + 1 be adapted (`Γ.IsHead`), x in `F.positions`, y in the box
`F.boxSet` and ν in `unipotentBelow a`, and write w_p for the Weyl element `weylElem (a + 1) p`. The
integral of the s-th power of the depth `F.depth a z x`, the inverse volume of
`F.stableProducts a z x`, at z = w_p n ν y, over the n in the Heisenberg group of floor a with z
near at a + 1, is at most |p_a|^(-r-1/2) Λ^(10⁶ n²). Here Λ = `Γ.loss`, the first factor is
`F.floorModulus a (p a)⁻¹`, and r = k + 1 + 2 (ϱ - a - 1). 

### `lintegral_invDepthWeight_succ_le`

 For z near at j, `F.invDepthWeight j x z` is the product over the floors l < j of the s-th
powers, s = `F.volumeExponent`, of the depths of e_l at z and z x. Let the head p of length a + 1 be
adapted (`Γ.IsHead`), x in `F.positions`, y in the box `F.boxSet` and ν in `unipotentBelow a`. The
integral over the n in the Heisenberg group of floor a of the inverse weight of length a + 1 at
`weylElem (a + 1) p` n ν y is at most the inverse weight of length a at `weylElem a p` ν y, times
`F.floorModulus a (p a)⁻¹` and the power 10⁶ `𝔰.n`² of the constant `Γ.loss` of the gauge. 

### `lintegral_invDepthWeight_le`

 The integral of the inverse weight. Let the head p of length j ≤ ϱ be adapted (`Γ.IsHead`), x a
position and g near at j (ξ g lies in the box for some ξ in `partialUnitriangularGroup j`). Let
w_p = `weylElem j p`. The integral of the inverse weight `F.invDepthWeight j x` at w_p ν g, for the
convolution of the Heisenberg measures of the floors below j in the variable ν, is at most
`Γ.floorsConst` = Λ^(10⁶ n³) times the product over a < j of the
|p_a|^(-r_a-1/2) = `F.floorModulus a (p a)⁻¹`. 

### `lintegral_mul_invDepthWeight_le`

 Let the head p of length j ≤ ϱ be adapted, x a position and j ≤ b. Let Φ be measurable, left
invariant under `partialUnitriangularGroup b` and zero off the points near at b. Integrate Φ(g)
times the inverse weight at `weylElem j p * g` against the convolution of the Heisenberg measures of
the floors below j with a measure ρ. The result is at most the product over a < j of the
`F.floorModulus a (p a)⁻¹`, times `Γ.floorsConst`, times the integral of Φ against ρ. 

### `floorConst`

 The cost of floor l on the position ball: |M|^(r_l+1/2) c^(rank X') Λ^(4900 n), where
|M|^(r_l+1/2) = `F.floorModulus l`, c = `P.kernelBound` and X' has the basis `F.FreeIndex`. 

### `form_sub_form_heisenbergElem_inv_mulVec`

 An identity for the Heisenberg group of floor a. Let ⟨·, ·⟩ be the form of `T.splitGram`. For
t = (ω, β) let n = `P.heisenbergElem a t`, with ω extended by zero. Let ζ, ζ' be congruent modulo
the e_b, b < a, and let o be orthogonal to the e_b, b ≤ a. Then ⟨ζ, o⟩ - ⟨n⁻¹ ζ', o⟩ is the
conjugate of ⟨e_a, ζ⟩ = `ζ (eStar a)` times ⟨ω, o⟩. 

### `closeBelow`

 The translates under U_(<l) of the points that are close to g: the z for which g⁻¹ ν z is a
close position for some ν in U_(<l). 

### `hasMatrixSize_mul_inv_sub_one`

 Two points of the position ball: if g lies in the box K = `F.boxSet` and x, y lie in the
position ball (`Γ.positionsOfSize`), then all entries of (g x (g y)⁻¹ - 1) / M have size 14, where
M = `F.levelUnit` is the level. 

### `exists_lift_of_mem_closeBelow`

 The range of the coordinates on a Heisenberg group. Let g lie in the box `F.boxSet` and let g⁻¹
y lie in the position ball (`Γ.positionsOfSize`). Let n lie in the Heisenberg group
`floorUnipotent a` of floor a, with g⁻¹ ν n y in the position ball for some ν in `unipotentBelow a`
(`Γ.closeBelow`). Then some vector v differs from (n⁻¹ - 1) e*_a by a combination of the e_b, b < a
(`CongrBelow`), and all entries of `F.levelUnit⁻¹ • v`, that is v divided by the level
`F.levelUnit`, have size 17 for the gauge Γ (`Γ.vecsOfSize 17`). 

### `form_inv_mulVec_inv_mulVec_cancel`

 Moving a point and a vector by unitary elements: ⟨(g g⁻¹ n y)⁻¹ ζ, (g g⁻¹ y)⁻¹ o⟩ = ⟨n⁻¹ ζ, o⟩
for the form ⟨·, ·⟩ of `T.splitGram`. 

### `star_smul_orthonormalPart_dotProduct`

 The product of c (ω / M)_X with a vector u of X' is c̄ ⟨ω, u⟩ / M, where M = `F.levelUnit` is
the level, u is read as the combination `F.orthonormalPart *ᵥ u` of the orthonormal vectors, and
y_X = `F.orthonormalPartᴴ *ᵥ T.splitGram *ᵥ y`. 

### `lintegral_heisenbergMeasure_inv_depth_le`

 Let g lie in the box `F.boxSet` and let g⁻¹ y lie in the position ball (`Γ.positionsOfSize`).
Consider the integral of depth^(-s) of e_a at the points g and n y, over the n in the Heisenberg
group of floor a (measure `heisenbergMeasure a`) with n y in `Γ.closeBelow a g`. It is at most
|M|^(r+1/2) Λ^(4600 n), where the first factor is `F.floorModulus a`, Λ = `Γ.loss`, and the n in the
exponent is `𝔰.n`. Here M = `F.levelUnit` is the level, s = `F.volumeExponent`, and r is the number
of coordinates of the vector part of that group. The inverse depth `(F.depth a z x)⁻¹` is the volume
of the products of e_a with the vectors that are stable at z and z x. 

### `lintegral_depthWeight_succ_le`

 One floor of the weight `F.depthWeight`. The weight of length j is the product over the first j
vectors e_l of depth^(-s), where s = `F.volumeExponent` and the depth `F.depth` is the inverse
volume of 𝔡_l. Let g lie in the box `F.boxSet`. Suppose that C ≠ ∞ bounds, for all y, the integral
of `Γ.positionsOfSize.indicator (F.depthWeight a g)` at g⁻¹ ν y over ν. The measure in ν is
`ascConv heisenbergMeasure a`, the convolution of the Heisenberg measures of the floors below a.
Then for all y the same integral of length a + 1 is at most C |M|^(r+1/2) Λ^(4600 n). Here
|M|^(r+1/2) = `F.floorModulus a`, M = `F.levelUnit` is the level, r is the rank of the vector part
of the Heisenberg group of floor a, Λ = `Γ.loss` and n = `𝔰.n`. 

### `lintegral_depthWeight_le`

 The integral of the weight over the position ball. Let j ≤ ϱ and let g be near at j (ξ g lies in
the box for some ξ in `partialUnitriangularGroup j`). The weight `F.depthWeight j` is the product of
the powers depth^(-s), s = `F.volumeExponent`, over the first j frame vectors. Integrate it at the
points g and ν y, over the ν for which g⁻¹ ν y lies in the position ball (`Γ.positionsOfSize`),
against the convolution of the Heisenberg measures of the floors below j. The result is at most the
product of the constants `Γ.floorConst l`, l < j. 

### `exists_hasMatrixSize_of_isNear`

 One translate bounds the sizes of g and w_p⁻¹ g. Let j ≤ ϱ, let the head p of length j be
adapted (`Γ.IsHead`), and let g and w_p⁻¹ g be near at j (`F.IsNear`: a translate by an element of
`partialUnitriangularGroup j` lies in the box), where w_p = `weylElem j p`. Then for some σ in
`floorGroup j` the entries of σ g have size 60 n² and those of σ w_p⁻¹ g have size 99 n²
(`Γ.HasMatrixSize`), where n = `𝔰.n`. 

### `hasShortDual_of_mem_stableProducts`

 Let the unit c lie in 𝔡_a = `F.stableProducts a x y`, the set of products ⟨e_a, ω⟩ with the
vectors ω that are stable at x and x y, and let c⁻¹ have size 1. Then e_a has a short dual of size 5
for the points x and x y modulo the level `F.levelUnit` (`Γ.HasShortDual`): divide a stable vector
by its product c with e_a. 

### `gaugesDifferLe_last_quotient_of_close`

 Let u x and v y lie in the box `F.boxSet`, with u, v in the Bessel unipotent group `T.besselU`,
and let (v y - u x) / `F.levelUnit` have size 2 for Γ (`Γ.HasMatrixSize`). Then the lengths read at
x and y differ by at most size 9 modulo the level `F.levelUnit` (`Γ.GaugesDifferLe`): if ω is
orthogonal to all e_b, b < ϱ, and x⁻¹ ω has size i, then (x⁻¹ ω - y⁻¹ ω') / `F.levelUnit` has size
i + 9 for some ω' congruent to ω modulo the e_b. 

### `hasMatrixSize_sub_one_of_forall_stableProducts`

 Bounded depths bound the position. Let u x and v x y lie in the box `F.boxSet` for some u, v in
the Bessel unipotent group `T.besselU`, with (v x y - u x) / `F.levelUnit` of size 2, where
`F.levelUnit` is the level. If each set 𝔡_a = `F.stableProducts a x y` contains a unit whose inverse
has size 1, then (y - 1) / `F.levelUnit` has size 99 n (`Γ.HasMatrixSize`), where n = `𝔰.n`. 

### `exists_unit_mem_stableProducts_of_isHead`

 Let j ≤ ϱ, let the heads p, q of length j be adapted (`Γ.IsHead`), and let the inverse of the
level `F.levelUnit` have size 1 (`Γ.ofSize 1`). Let x, x y, w_p⁻¹ x and w_q⁻¹ x y be near at j
(`F.IsNear`), where w_p = `weylElem j p` and w_q = `weylElem j q`. Then for a < j the set
𝔡_a = `F.stableProducts a x y` contains a unit c whose inverse has size 10 n, that is, lies in
`Γ.ofSize (10 * 𝔰.n)`. 

### `hasMatrixSize_sub_one_of_stableProducts`

 Let j ≤ `𝔰.ϱ` and let the heads p, q of length j be adapted to the gauge S. If j ≠ 0, let the
inverse of the level M = `F.levelUnit` have size 1 for S (`hM`), and let the numbers of size 10
`𝔰.n` for S have size 1 for Γ (`hS`). Let u x and v x y lie in the box `F.boxSet` for some u, v in
the Bessel unipotent group `T.besselU`, with (v x y - u x) / M of size 2. Let w_p⁻¹ x and w_q⁻¹ x y
be near at j (`F.IsNear`), where w_p = `weylElem j p` and w_q = `weylElem j q`. If each
𝔡_a = `F.stableProducts a x y` with a ≥ j contains a unit whose inverse has size 1, then (y - 1) / M
has size 99 `𝔰.n`. Sizes refer to Γ unless S is named. 
