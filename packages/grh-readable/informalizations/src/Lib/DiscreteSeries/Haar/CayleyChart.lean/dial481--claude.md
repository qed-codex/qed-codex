---
{
  "module": "src/Lib/DiscreteSeries/Haar/CayleyChart.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/DiscreteSeries/Haar/CayleyChart.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/DiscreteSeries/Haar/CayleyChart.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Cayley chart and an explicit Haar measure on the unitary group U(J)

For a hermitian involution J, this file builds an explicit Haar measure on the unitary group
`New.U J` through the Cayley chart and shows how it transforms. The Jacobians of the chart are
computed from the logarithmic derivative `Φᴴ J dΦ`, with real coordinates on skew-hermitian
matrices.

## Main definitions and results

* `New.logDerivU`: the form `Φᴴ J dΦ` of a map `Φ` to `New.U J`; it is skew-hermitian
  (`New.conjTranspose_logDerivU`).
* `New.HasGaussianIntegral.measurePreserving`,
  `New.HasGaussianIntegral.exists_measurePreserving_equiv`: a linear isomorphism that matches the
  forms of two volumes normalised by `New.HasGaussianIntegral` preserves measure.
* `New.cayleyChart`: the chart y ↦ 2 (1 - X)⁻¹ - 1, X = J⁻¹ (`New.skewOfReal` y) / 2, which is
  (1 + X)(1 - X)⁻¹ where 1 - X is invertible; its density is `New.cayleyDensity`.
* `New.haarU`, `New.lintegral_eq_cayleyChart`: the measure, and integrals against it in the chart.
* `New.cayleyChart_jacobian`: the Jacobian of q ↦ a · cayleyChart J (y q) · b.
* `New.measurePreserving_haarU`: maps g ↦ a g b of unitary groups, for suitable a and b, preserve
  `New.haarU`. It follows that `New.haarU` is a Haar measure.

Notions from other files:

* `New.skewOfReal`, `New.skewCoords`: real coordinates on skew-hermitian matrices: the imaginary
  parts of the diagonal entries, and orthonormal coordinates of one entry in each pair off it.
* `New.HasGaussianIntegral a q`: the volume gives `exp (-t * q)` the integral `(π / t) ^ a` for
  all `t > 0`.

## Relation to the literature

Part of a known result: the Haar measure of U(J) in Cayley coordinates.



## Skew coordinates, U(J) as a closed set, and determinants

* `New.isClosedEmbedding_U`, `New.continuous_U_iff_matrix`: U(J) has the topology of a closed set of
  matrices.


### `det_mulLeft_mulRight_real`

 For complex square matrices P of size m and Q of size n, the real-linear map X ↦ PXQ on
complex m×n matrices has determinant |det P|^(2n)·|det Q|^(2m). 

### `exists_U_coe_eq`

 Let J be a hermitian involution. Every matrix x with xᴴ J x = J is the matrix of an element
of U(J). 

### `isClosedEmbedding_U`

 For a hermitian involution J, sending an element of U(J) to its matrix is a closed embedding. 

### `continuous_U_iff_matrix`

 For a hermitian involution J, a map to U(J) is continuous if and only if it is continuous as a
map to matrices. 

### `skewCoords_skewOfReal`

 `skewCoords` reads the real coordinates y back from the skew-hermitian matrix `skewOfReal y`. 

### `conjTranspose_skewOfReal`

 The matrix `skewOfReal y` with real coordinates y is skew-hermitian. 

### `skewOfReal_skewCoords`

 A skew-hermitian matrix x is recovered by `skewOfReal` from its real coordinates
`skewCoords x`. 

 ## The logarithmic derivative, Jacobians of congruences, measure-preserving maps 

 ### The logarithmic derivative 

### `DifferentiableAtU`

 The condition that a map Φ from a real normed space to U(J), viewed as matrix-valued, is
real differentiable at the point p. 

### `logDerivU`

 For Φ : V → U(J), the real linear map v ↦ Φ(p)ᴴ J dΦ_p(v), that is the form Jg⁻¹dg pulled back
by Φ at p. 

### `conjTranspose_logDerivU`

 Let J be a hermitian involution and Φ : V → U(J) differentiable at p. Then the value
Φ(p)ᴴ J dΦ_p(v) of `logDerivU Φ p` is skew-hermitian. 

 ### Determinants 

### `abs_det_skew_congruence`

 Read real `n × n` matrices as skew-hermitian ones through `New.skewOfReal` and
`New.skewCoords`. Let `e` identify them with `V`, and let `L` be a linear map from `V` to them.
Following `L` by the congruence `S ↦ Cᴴ * S * C` multiplies `|det (e ∘ L)|` by `‖det C‖ ^ (2 n)`. 

### `Haar.det_eq_mul_of_fst_eq_of_snd_eq`

 The determinant of a block lower triangular map `T` of `V × W` is the product of the
determinants of its diagonal blocks: `A` gives the first component of `T (v, w)` from `v` alone,
and `B` gives the second component of `T (0, w)`. 

### `instance : (volume (α`

 If the volumes of two finite-dimensional real spaces are additive Haar measures, then so is
their product. 

### `instance {m : Type} [Fintype m] : HasGaussianIntegral (V`

 If the volume on V is Gaussian-normalised for q with exponent a, then the volume on m × n
matrices over V is so for the sum of q over the entries, with exponent a n m. 

 ### The scalar circle, and volumes normalised by a Gaussian 

### `circleScalar`

 For real t, the scalar matrix e^{it}·1 as an element of U(J). 

### `lintegral_gaussian_eq_one`

 If the volume on V is Gaussian-normalised for q (`HasGaussianIntegral a q`), then
exp(-π q) has lower integral 1. 

### `HasGaussianIntegral.measurePreserving`

 Suppose `∫ exp (-t q) = (π / t) ^ a` on `V` and `∫ exp (-t q') = (π / t) ^ b` on `W` for all
`t > 0` (`HasGaussianIntegral`). A linear isomorphism `e` with `q' ∘ e = q` preserves the volume. 

### `HasGaussianIntegral.exists_measurePreserving_equiv`

 Suppose `∫ exp (-t q) = (π / t) ^ a` on `V` for all `t > 0` (`HasGaussianIntegral a q`), and
`V` has the dimension of the real `n × n` matrices. A linear map `f` from these matrices to `V`
with `q (f y) = ∑ i, ∑ j, y i j ^ 2` is invertible, and its inverse preserves the volume. 


## The Cayley chart and the Haar measure on U(J)

* `New.Haar.lintegral_chart_rotate_le`: an injective parametrisation, rotated by a generic scalar,
  integrates to at most the full integral.

No chart is assumed to cover almost all of U(J). Instead, rotating by a generic scalar e^{it} moves
almost all points of any parametrisation into the Cayley chart.


### `cayleyDenom`

 The matrix 1 − ½J⁻¹Y, where Y is the skew-hermitian matrix `New.skewOfReal` y attached to the
real matrix y; the denominator in Cayley's chart. 

### `gram_two_smul_inv_cayleyDenom_sub_one`

 The matrix 2 D⁻¹ - 1, D = `New.cayleyDenom` J y, preserves the form of the hermitian
involution J, also where D is singular. 

### `cayleyChart`

 The Cayley chart. Put X = J⁻¹ (`New.skewOfReal` y) / 2, so that `New.cayleyDenom` J y = 1 - X.
This is the element of U(J) with matrix 2 (1 - X)⁻¹ - 1, which equals the Cayley transform
(1 + X)(1 - X)⁻¹ when 1 - X is invertible. For a hermitian involution J this matrix always lies in
U(J). Where 1 - X is singular, Mathlib's inverse is 0 and the value is -1. 

### `cayleyDensity`

 The real number (|det J| · |det(1 − ½J⁻¹S)|²)^(−N), where S = `New.skewOfReal` y is the
skew-hermitian matrix with coordinates y and N = card n. It is the Jacobian of the Cayley chart. 

### `sphereDensity`

 The number 2π^k r^{k−1}/(k−1)!; for k ≥ 1 the sphere of radius ρ in ℂ^k has area ρ times its
value at r = ρ². 

### `volU`

 The number ∏_{i<j} 2π^(i+1)/i!, a product of areas of unit spheres: the volume of the compact
unitary group U(j) for the metric in which the chart has density `New.cayleyDensity`. 

### `haarU`

 The measure on U(J) obtained from Lebesgue measure on the real matrices y with
det (`New.cayleyDenom` J y) ≠ 0, with density `New.cayleyDensity` J y divided by
`New.volU` (card n), by pushing forward along `New.cayleyChart` J. The set is taken as a subtype
because the chart is a measurable embedding there (`New.measurableEmbedding_cayleyChart`);
`New.lintegral_eq_cayleyChart` is the formula to use. For a hermitian involution J it is a Haar
measure. The constant `New.volU` (card n) is chosen so that the mass is 1 for J = 1
(`New.isProbabilityMeasure_haarU`). 

### `measureSpaceU`

 The measure space structure on U(J) whose `volume` is `New.haarU` J. 

### `det_cayleyDenom_one_ne_zero`

 For J = 1 the denominator 1 - (`New.skewOfReal` y) / 2 of the Cayley chart is invertible for
every y, because its hermitian part is the identity. 

### `measurableSet_det_cayleyDenom_ne_zero`

 The domain of the Cayley chart is measurable, being open. 

### `logDerivU_cayleyChart`

 Let J be a hermitian involution and S(y) = `New.skewOfReal` y the skew-hermitian matrix with
coordinates y, so that `New.cayleyDenom` J y = 1−½J⁻¹S(y). Where its determinant is not 0, the
Cayley chart g is differentiable and its form Jg⁻¹dg (`New.logDerivU`) takes the value XᴴS(v)X on a
direction v, where X = (1−½J⁻¹S(y))⁻¹. 

### `cayleyChartInv`

 The inverse of the Cayley chart: for g in U(J), the real n×n matrix of coordinates of the
complex matrix 2J(1−2(g+1)⁻¹). 

### `cayleyChart_injOn`

 The Cayley chart is injective on its domain, the real matrices y with
det (`New.cayleyDenom` J y) ≠ 0. 

### `cayleyChart_cayleyChartInv`

 If g ∈ U(J) and g + 1 is invertible, then `New.cayleyChartInv` g lies in the domain of the
Cayley chart and the chart sends it to g. 

### `measurableEmbedding_cayleyChart`

 The Cayley chart, restricted to its domain det (`New.cayleyDenom` J y) ≠ 0, is a measurable
embedding into U(J). 

### `lintegral_eq_cayleyChart`

 The integral of any f : U(J) → [0, ∞] (no measurability needed) for `volume` = `New.haarU` J,
written in the Cayley chart: it is the integral over the domain of the chart of f at the chart times
the density `New.cayleyDensity` J y / `New.volU` (card n). 

### `cayleyChart_jacobian`

 Let `J`, `J'` be hermitian involutions, `V` a finite-dimensional real normed space with
coordinates `e : V ≃ Matrix n n ℝ`, and `y : V → Matrix n n ℝ` with derivative `L` at `p`. Write `S`
for the skew-hermitian matrix with coordinates `y p` and `X = ½ J⁻¹ S`, and assume `det(1 − X) ≠ 0`.
Suppose `bᴴ (ε J) b = J'` for invertible `a`, `b` and a nonzero real `ε`, and that `Φ : V → U J'`
equals `a · (1 + X_q)(1 − X_q)⁻¹ · b` near `p` (the Cayley chart `cayleyChart J (y q)`). Then `Φ` is
differentiable at `p`, and the absolute determinant of `Φ(p)ᴴ J' dΦ_p` (`logDerivU Φ p`), read in
the coordinates `skewCoords` and `e`, equals `|det L|` times the Cayley density
`(|det J| · |det(1 − X)|²)^(−card n)`. 

### `abs_det_skewCoords_comp_logDerivU_cayleyChart`

 On the domain of the Cayley chart g, the Jacobian of the form Jg⁻¹dg (`New.logDerivU`) in the
coordinates `New.skewCoords` is the density `New.cayleyDensity`. 

### `abs_det_logDerivU_cayleyChart`

 Let S = `New.skewOfReal` y be the skew-hermitian matrix with coordinates y, put X = J⁻¹S/2, and
assume that `cayleyDenom J y` = 1 − X has nonzero determinant. Then the Cayley chart `cayleyChart J`
(the element 2(1 − X)⁻¹ − 1 of U(J)) is differentiable at y. Moreover, the linear map
v ↦ `skewCoords`(Φ(y)ᴴ J dΦ_y(v)), which is the form Jg⁻¹dg pulled back by Φ = `cayleyChart J` and
written in real coordinates, has absolute determinant `cayleyDensity J y` =
(|det J| · |det(1 − X)|²)^(−N), where N = card n. 

### `differentiableAt_cayleyChartInv_mul`

 If Φ from a real normed space V into U(J) is differentiable at p and c Φ(p) + 1 is invertible,
then q ↦ `New.cayleyChartInv` (c Φ(q)), the chart coordinates of c Φ, is differentiable at p. 

### `ae_isUnit_circleScalar_mul_add_one`

 For any complex matrix x, the matrix e^{it} x + 1 is invertible for almost every real t; here
the scalar e^{it} is taken as the element `New.circleScalar` t of U(J). 

### `Haar.lintegral_chart_rotate_le`

 Change of variables for a parametrisation of part of U(J), J a hermitian involution. Let e be a
measure preserving linear isomorphism from V to the real n×n matrices, A ⊆ V measurable and Φ :
V → U(J) injective on A and differentiable at each p ∈ A. Let w p be the Jacobian of Φ at p ∈ A: the
absolute determinant of its derivative Φᴴ J dΦ (`New.logDerivU`), read in the real coordinates
`New.skewCoords` of skew-hermitian matrices and moved to V by e⁻¹. Then for almost every real t and
every f : U(J) → [0, ∞], with N = card n, ∫_A (w p / `New.volU` N) f(e^{it} Φ p) dp ≤ ∫ f, the right
side for `volume` = `New.haarU` J; here `New.circleScalar` t is the scalar e^{it} and `New.volU` N
the normalising constant of the measure. 

 ### Invariance 

### `lintegral_comp_le_haarU`

 One half of `New.measurePreserving_haarU`. Let J, J' be hermitian involutions, a, b invertible
matrices and ε a nonzero real number with bᴴ (ε J) b = J', and φ : U(J) → U(J') a bijection of the
form g ↦ a g b. Then ∫ f ∘ φ over U(J) is at most ∫ f over U(J') for `volume` = `New.haarU`, for
every f : U(J') → [0, ∞]. 

### `measurePreserving_haarU`

 Let J, J' be hermitian involutions, a, b invertible matrices and ε a nonzero real number with
bᴴ (ε J) b = J'. A bijection φ : U(J) → U(J') given by g ↦ a g b carries `New.haarU` J to
`New.haarU` J'. The cases b = 1 and a = 1 with J' = J are left and right invariance; a = b⁻¹ with
ε = 1 is conjugation by an isometry; ε = -1 compares U(J) with U(-J). In all cases the form Jg⁻¹dg
changes by the congruence S ↦ ε bᴴ S b, whose Jacobian is 1. 

### `instance : (volume (α`

 The measure `New.haarU J` is a left Haar measure on U(J). 
