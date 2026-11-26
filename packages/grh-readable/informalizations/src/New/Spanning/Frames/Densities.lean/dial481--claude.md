---
{
  "module": "src/New/Spanning/Frames/Densities.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Frames/Densities.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Frames/Densities.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The densities as integrals over pairs of frames

For a cut Bessel function `W` and two heads (sequences of units `p`, `q`), the form of floor `j` is
a density times an integral, over a position `x` and two frames, of a weighted product of two
correlations. The file defines these forms and their majorants, and proves the descent from one
floor to the next.

Notions from other files:
* `F : PlaceData ι T m` is the data of a place: the measures of the floors, the level `F.levelUnit`
  and the compact set `F.boxSet` (the box) of the unitary group `T.G`; a `Gauge F` is a notion of
  size with a number Λ = `Γ.loss` whose powers bound moduli and volumes.
* G^(l) = `floorGroup l` and R^(l) = `partialUnitriangularGroup l` are the subgroups described in
  `New.Spanning.Frames.Lengths`, and 𝖴 = `T.besselU` is the Bessel unipotent group. A point `g` is
  near at `j` (`F.IsNear j g`) if R^(j) g meets the box.
* θ_j = `F.floorMeasure j` is the measure of floor `j`, 𝗆_j = `F.partialGroupMeasure 0 j` the
  convolution of the Heisenberg and floor measures of the floors below `j`, and 𝖬 = `F.groupMeasure`
  that of all floors.
* `F.partialCorrelation j k g y` is the correlation from floor `j` on, the integral of
  `k (σ g) (σ y)` against `F.quotientMeasureFrom j`, the convolution of the θ_l with l ≥ j.
* w_p = `weylElem j p` is the Weyl element of the first `j` hyperbolic pairs with the entries `p a`,
  and `weylRatio j p q` is the diagonal element w_q⁻¹ w_p.

## Main definitions and results

* `New.Floors.PlaceData.IsCut`, `New.Floors.PlaceData.floorForm`,
  `New.Floors.PlaceData.formIntegrandL1Norm`, `New.Floors.PlaceData.formMajorant`: the forms and
  their majorants.
* `New.Floors.Gauge.inner_besselOrbitalIntegral`: the product of two orbital integrals as a double
  integral.
* `New.Floors.Gauge.isPairingKernel_frameCorrelation`: the rules for correlations.
* `New.Floors.PlaceData.floorForm_zero_eq_integral`: the mass: the form of floor 0 is the integral
  of a square.
* `New.Floors.Gauge.integral_weight_mul_floorForm_succ`,
  `New.Floors.Gauge.integral_psi_mul_floorForm_succ`: descent from one floor to the next.

## Relation to the literature

See `New.Spanning.MainTerm.EnergyEstimate` for related work.


### `PlaceData.headDensity`

 The density κ_j of two sequences of units `p`, `q`: the product over `a < j` of
`modulus (p a * q a) ^ (d a / 2)` with `d a = 𝔰.k + 1 + 2 * (𝔰.ϱ - (a + 1))`. The power `d a / 2` is
written as the `d a`-th power of a square root. 

### `frameCorrelation`

 The correlation `⟨W x, W (d y)⟩` of two points, the second translated by `d`. 

### `Place.IsBessel`

 W is a Bessel function of frequency η: bounded, measurable, with W(ux) = ψ(η σ(u))W(x) for u in
𝖴 = `T.besselU`, where σ(u) = `simpleRootSum u` is the superdiagonal sum of the frame block. 

### `Place.IsBessel.map_unipotent_mul`

 Left translation by u in the Bessel unipotent group multiplies W by
  ψ(η · `simpleRootSum u`). 

### `PlaceData.IsCut`

 W is a cut Bessel function for the place datum: Bessel of frequency `F.levelUnit⁻¹`, and zero at
x unless ux lies in the box `F.boxSet` for some u in 𝖴 = `T.besselU`. 

### `PlaceData.IsCut.exists_mul_mem_box`

 W vanishes off the translates of the box `F.boxSet` by the Bessel unipotent group. 

### `PlaceData.pairingNormSq`

 The squared L² norm of the correlation ⟪W x, W y⟫ for the measure `F.quotientMeasureFrom 0` in
both variables, which stands for integration over 𝖴∖G. 

### `PlaceData.partialCorrelationProduct`

 At the position `x`: the correlation from floor `j` on (`F.partialCorrelation j`) of the kernel
⟨W y, W y'⟩ at the points `g`, `g x`, times the conjugate of that of the kernel ⟨W y, W (d y')⟩ at
`w⁻¹ g`, `w⁻¹ g x`. 

### `PlaceData.formIntegrand`

 At the position x and the point g, the double integral ∬ ω(στ⁻¹) k(σg, σgx)
conj(k'(τw_p⁻¹g, τw_p⁻¹gx)) dθ_j(τ) dθ_j(σ). Here θ_j = `F.floorMeasure j`, w_p = `weylElem j p`,
and k, k' are the correlations from floor j + 1 on of
`New.Floors.PlaceData.partialCorrelationProduct` for the twist `weylRatio j p q`. 

### `PlaceData.floorForm`

 The form 𝓘_j(p, q; ω): the density κ_j = `F.headDensity j p q` times the integral of the double
integral `New.Floors.PlaceData.formIntegrand` over the position against 𝖬 = `F.groupMeasure` and
over the point against 𝗆_j = `F.partialGroupMeasure 0 j`. 

### `PlaceData.formIntegrandL1Norm`

 The number 𝖥_j(x; ω): at the position x, the integral against 𝗆_j = `F.partialGroupMeasure 0 j`
of the modulus of the double integral `New.Floors.PlaceData.formIntegrand` that defines
`F.floorForm`. 

### `PlaceData.formMajorant`

 The majorant of the form at the position `x`: the integral against
𝗆_j = `F.partialGroupMeasure 0 j` of the product of two factors `F.pivotL1Norm j`, one for each
kernel, each the integral over floor j of the modulus of the partial correlation from floor j + 1
on. 

### `Gauge.weightedSquareProduct`

 The product of the second moments `F.weightedSquareIntegral` of the two correlations at `x`,
times the constant made of the squared product of `F.floorModulus a (p a)⁻¹` over a < j and of the
cube of `Γ.floorsConst`. A number has the gain `ς` at `x` if its square is at most `ς ^ 2` times
this product; the density `F.headDensity` is not included. 

### `PlaceData.IsActive`

 At the position `x`, the point `y` is active for the heads `p`, `q`: the correlation of `y` and
`y x` is not zero, and both points are near at `j` after the Weyl elements are undone. 

### `PlaceData.IsActive.inner_ne_zero`

 The correlation of the two points is not zero. 

### `PlaceData.IsActive.isNear_left`

 The point `w_p⁻¹ y` is near at `j`. 

### `PlaceData.IsActive.isNear_right`

 The point `w_q⁻¹ y x` is near at `j`. 

### `PlaceData.HasDeepVector`

 At the position `x`, every active point `y` has a frame vector e_a with `j ≤ a` whose depth
`F.depth a y x` is at least `D`. 

### `PlaceData.hasDeepVector_inv_iff`

 Every active point `y` at the position `x` has a frame vector e_a with `j ≤ a` of depth at least
`σ⁻¹` if and only if it has such a vector whose set of products `F.stableProducts a y x` has volume
at most `σ`. 

### `frameGram_diag_mul`

 For b ≤ ϱ, let x be in both R^(b+1) = `partialUnitriangularGroup (b + 1)` and G^(b) =
`floorGroup b`, so that x fixes the frame vector f_b. Then multiplying y by x on the left or on the
right leaves the diagonal entry h(f_b, y f_b) of Z(y) = `T.frameGram y` unchanged. 

### `PlaceData.enorm_floorForm_le`

 The form of floor `j` with the weight `ω` is bounded by its L¹-norm version:
|𝓘_j(p, q; ω)| ≤ κ_j ∫ 𝖥_j(x; ω) d𝖬(x), where 𝓘_j = `F.floorForm j`, κ_j = `F.headDensity j p q`,
𝖥_j = `F.formIntegrandL1Norm j` and 𝖬 = `F.groupMeasure`. 

### `PlaceData.partialGroupMeasure_top`

 The partial group measure of the last two floors, `ϱ` and `ϱ + 1`, is the convolution of the
Haar measure `F.measureH` of the group H = `besselH`, which is the measure of floor `ϱ + 1`, with
the measure of floor `ϱ`. 

### `Gauge.isCompact_hasMatrixSize`

 The elements of the unitary group whose matrix entries have size `j` for the gauge `Γ` form a
compact set. 

### `Place.IsBessel.besselOrbitalIntegral_besselU_mul`

 Let `W` be a Bessel function of frequency `η`, so that `W (u * y) = χ(u) • W y` for `u` in the
unipotent group 𝖴 = `T.besselU`, with `χ(u) = ψ (η * simpleRootSum u)`. For a left invariant measure
`μ`, the orbital integral J(γ) = ∫ W(y) ⊗ W(γ⁻¹y)^* dμ(y) (`besselOrbitalIntegral μ W γ`) satisfies
J(u⁻¹γu') = conj χ(u) · χ(u') · J(γ) for `u`, `u'` in 𝖴. 

### `PlaceData.IsCut.isNear_of_ne_zero`

 A cut Bessel function `W` vanishes off the points near at `j`, for every `j`: if `W x ≠ 0`, then
`u x` lies in the box `F.boxSet` for some `u` in `partialUnitriangularGroup j`. 

### `Gauge.leadingMinor_mem_ofSize_of_besselOrbitalIntegral_ne_zero`

 Let `W` be a cut Bessel function for the place datum `F`. If the orbital integral J(γ) = ∫
W(y) ⊗ W(γ⁻¹y)^* dμ(y) is not zero, then all leading minors of the matrix of the products h(f_a, γ
f_b) of the frame vectors (`T.frameGram γ`) have size `9 * 𝔰.n`, that is lie in the set
`Γ.ofSize (9 * 𝔰.n)`, in every gauge `Γ` for `F`. 

### `PlaceData.IsCut.formIntegrandL1Norm_le_formMajorant`

 Let W be a cut Bessel function and |ω| ≤ 1 everywhere. For every floor `j : ℕ`, all sequences of
units `p q : ℕ → Aˣ` and every point x of the group, the L¹ norm 𝖥_j(x; ω) of the form integrand at
x is at most the majorant `F.formMajorant j p q W x`. 

### `Gauge.hasMatrixSize_of_ne_zero`

 Compact support of the orbital integrals, with a bound. Let W be a cut Bessel function, p a head
of length ϱ for the gauge Γ, with Weyl element w_p = `weylElem 𝔰.ϱ p`, and x in
G^(ϱ) = `floorGroup 𝔰.ϱ`. If W(y) ≠ 0 and W((w_p x)⁻¹y) ≠ 0, then the entries of y have size 60 n²,
where n = `𝔰.n` = ϱ + 1: the unipotent factors that move the two points into the box are solved from
the minors of the head. 

### `Gauge.inner_besselOrbitalIntegral`

 The inner product of two orbital integrals as an integral over two copies of the group. Let Γ be
a gauge for the place datum F and μ a Haar measure. Let W be a continuous cut Bessel function, that
is a Bessel function that vanishes off the 𝖴-translates of the box of F. Let p and q be heads of
length ϱ for Γ, with Weyl elements w_p = `weylElem 𝔰.ϱ p` and w_q, and let x be in the subgroup
G^(ϱ) = `floorGroup 𝔰.ϱ`. Write J(γ) = ∫ W(y) ⊗ W(γ⁻¹y)^* dμ(y) for `besselOrbitalIntegral μ W γ`.
Then ⟨J(w_p x), J(w_q x)⟩ is the μ×μ-integral over (y, y') of ⟨Wy, Wy'⟩ times the conjugate of
⟨W((w_p x)⁻¹y), W((w_q x)⁻¹y')⟩. 

### `Gauge.isPairingKernel_frameCorrelation`

 Let `W` be a cut Bessel function for the place datum `F`, which has a gauge, and `p`, `q` two
sequences of units. The kernel `⟪W g, W (w y)⟫`, with `w` = `weylRatio j p q`, satisfies the rules
of `New.Floors.PlaceData.IsPairingKernel`: it is measurable, transforms by a character under the
unipotent groups, its `w` commutes with the group of floor `j`, it has bounded mass, and its partial
correlations vanish unless the first point is near. 

### `Gauge.isPairingKernel_frameCorrelation_one`

 For a place datum F with a gauge and a cut Bessel function W, the function (x, y) ↦ ⟨W(x), W(y)⟩
is a kernel in the sense of `New.Floors.PlaceData.IsPairingKernel` at floor j, with twisting element
1. 

### `PlaceData.partialCorrelationProduct_eq`

 Let the place datum `F` have a gauge and let `W` be a cut Bessel function. For every floor
`j : ℕ`, all sequences of units `p q : ℕ → Aˣ` and every position `x`, the double integral over
floor `j` with the weight `1`, `F.formIntegrand j p q W x 1`, is the product of two correlations
from floor `j` on, `F.partialCorrelationProduct j W x (weylRatio j p q) (weylElem j p)`. 

### `PlaceData.floorForm_zero_eq_integral`

 The mass. For a place datum `F` with a gauge and a cut Bessel function `W`, the form of floor
`0` for the weight `1` is the integral of `|k₀(1, z)|²` in `z` against `F.groupMeasure`. Here
`k₀ = F.partialCorrelation 0 k` is the correlation from floor `0` on, an integral over all floors,
of the kernel `k = frameCorrelation W 1`. 

### `PlaceData.integrable_and_integral_succ_eq_mul_floorForm`

 The form of floor `b` as an integral of products of correlations from floor `b + 1` on. Let the
place datum `F` have a gauge, let `W` be a cut Bessel function whose majorant
`F.formMajorant b p q W`, for sequences of units `p q : ℕ → Aˣ`, has a finite integral against
𝖬 = `F.groupMeasure`, and let φ be measurable with |φ| ≤ 1. Let `F.floorMeasure b` be the image
under `(c, n) ↦ (v c)⁻¹ * n` of the product of `volume.withDensity ρ` and `ζ`, where `v` and `ρ` are
measurable, `ρ` is a.e. finite and `ζ` is carried by
`partialUnitriangularGroup (b + 1) ⊓ floorGroup b`. Write Z(x) for the Gram entry
`T.frameGram x b b`. Let `Ψ c` be, for almost every `c`, the product of `t`, the density
`F.headDensity b p q`, `ρ c`, φ(Z(v c)) and the integral over positions and points of
`F.partialCorrelationProduct (b + 1)` for the twist `weylRatio b p q` and the element
`weylElem b p * v c`. Then `Ψ` is integrable, and its integral is `t` times the form
`F.floorForm b p q W (φ ∘ Z)`. 

### `Gauge.integral_weight_mul_floorForm_succ`

 Descent. Let the place datum F have a gauge, let W be a cut Bessel function, `p q : ℕ → Aˣ`
sequences of units and a < ϱ. Let the majorant `F.formMajorant a p q W` have a finite integral
against 𝖬 = `F.groupMeasure`, and let φ be a measurable function on A with |φ| ≤ 1. Then
c ↦ φ(c) · t · 𝓘_{a+1}((p, c), (q, c); 1) is integrable, with integral t · 𝓘_a(p, q; φ(Z_{a,a})).
Here 𝓘_j(p, q; ω) is `F.floorForm j p q W ω`, (p, c) is p with the entry a replaced by c, and
Z_{a,a}(x) = h(f_a, x f_a) is a diagonal entry of `T.frameGram x`. 

### `Gauge.integral_psi_mul_floorForm_succ`

 Descent for a character: the case φ(c) = ψ(ηc) of
`New.Floors.Gauge.integral_weight_mul_floorForm_succ`, for a cut Bessel function `W` whose majorant
on floor `a` has a finite integral against `F.groupMeasure`. As a function of the common entry `c`
of `p` and `q` at `a`, ψ(ηc) times `t` times the form of floor `a + 1` with weight `1` is
integrable, and its integral is `t` times the form of floor `a` with the weight ψ(η Z(x)), where
Z(x) is the Gram entry `T.frameGram x a a`. 
