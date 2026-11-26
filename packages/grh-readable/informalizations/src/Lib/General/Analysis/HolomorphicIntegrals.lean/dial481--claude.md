---
{
  "module": "src/Lib/General/Analysis/HolomorphicIntegrals.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/General/Analysis/HolomorphicIntegrals.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/General/Analysis/HolomorphicIntegrals.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Strong operator integrals, analyticity of parameter integrals, and Hua's integral bound

In the strong integral, operator-valued functions are integrated vector by vector, so no
measurability in the operator norm is needed. In the results on analytic families, E is a
finite-dimensional complex normed space, K a compact R₁ space and f : E → K → ℂ a family of
functions on K with parameter in E. The file also contains the Schwarz lemma in normed spaces,
holomorphy of dominated parameter integrals, a uniqueness result for analytic functions along
submersions, and Euler's beta integral together with Hua's bound for negative powers of
determinants.

## Main definitions and results

* `New.strongIntegral`: the operator `x ↦ ∫ y, F y x ∂μ`, when this map is a bounded operator.
* `New.DiscreteSeries.IsAnalyticFamily`: the map x ↦ f(x, ·) into the Banach space C(K, ℂ) is
  analytic at a point.
* `New.DiscreteSeries.IsAnalyticFamily.analyticAt_integral`: then x ↦ ∫ f(x, k) dμ(k) is analytic,
  for a finite Borel measure μ.
* `New.analyticAt_of_eventually_differentiableAt`: a map between finite-dimensional complex spaces
  that is differentiable near p is analytic at p.
* `New.eventually_differentiableAt_integral`: an integral of holomorphic functions of a parameter in
  a finite-dimensional space, dominated by an integrable function, is holomorphic.
* `New.hua_integral_le`: Hua's bound for the integral of a negative power of `|det (M + Yᴴ Y)|`,
  where `Y = X S + A`, over the rows of `X`, one row at a time;
  `New.lintegral_norm_det_add_inv_pow_le` is a cruder form for `Y = S X + c` and at least seven
  columns.

## Relation to the literature

Known result: an upper bound for Hua's determinant integral. The integral is bounded only from
above, with an affine change of the rows, instead of being computed exactly. Source: Hua, Harmonic
Analysis of Functions of Several Complex Variables in the Classical Domains, AMS 1963.


 ## The strong integral of a family of bounded operators 

### `New.strongIntegral`

 The strong integral of a family `F` of bounded operators. If some bounded operator agrees
with the map `x ↦ ∫ y, F y x ∂μ`, this is that operator (`New.strongIntegral_apply_of_exists`;
`invFun (⇑)` picks a preimage under the coercion from operators to functions); otherwise it is an
unspecified operator. The first case holds when every `y ↦ F y x` is integrable and the spaces are
complete (`New.exists_continuousLinearMap_apply_eq_integral`, `New.strongIntegral_apply`). 

### `HasDerivAt.map_clm`

 A complex-linear bounded operator `L` may be applied to the derivative of a curve
`f : ℝ → X`: if `f` has derivative `f'` at `t`, then `L ∘ f` has derivative `L f'` at `t`. 

### `New.strongIntegral_apply_of_exists`

 If some bounded operator agrees at every point with the map `x ↦ ∫ y, F y x ∂μ`, then so does
the strong integral of `F`. 

### `New.exists_continuousLinearMap_apply_eq_integral`

 For Banach spaces `X`, `Z` and a family `F` of bounded operators such that `y ↦ F y x` is
integrable for every `x`, the map `x ↦ ∫ y, F y x ∂μ` is a bounded operator. No bound on the
norms of the `F y` is assumed: the closed graph theorem gives the boundedness. 

### `New.strongIntegral_apply`

 For Banach spaces `X`, `Z` and a family `F` of bounded operators such that `y ↦ F y x` is
integrable for every `x`, the strong integral sends `x` to `∫ y, F y x ∂μ`. 


## Analytic maps into C(K, ℂ) and analyticity of differentiable maps

The idea is Cauchy's formula in one coordinate at a time, the circle being adjoined to K.
The strong integral `New.strongIntegral` serves here as the functional f ↦ ∫ f dμ on C(K, ℂ)
(`New.strongIntegral_eval`).


### `strongIntegral_eval`

 Let μ be a finite Borel measure on a compact R₁ space K. The strong integral of the evaluation
functionals `evalCLM ℂ k : g ↦ g k` (see `New.strongIntegral`) sends a continuous f : K → ℂ to
∫ f dμ. 

### `DiscreteSeries.IsAnalyticFamily`

 f : E → K → ℂ agrees near a with a map from E to the Banach space C(K, ℂ) that is analytic
at a. 

### `DiscreteSeries.IsAnalyticFamily.analyticAt_integral`

 Let E be a complex normed space, K a compact R₁ space and μ a finite Borel
measure on K. If x ↦ f(x, ·) is analytic at p ∈ E as a map to C(K, ℂ) (`IsAnalyticFamily f p`), then
its integral against μ is an analytic function of x at p. 

### `integral_cauchyKernel_circleMap`

 Cauchy's integral formula with the circle parametrised by the angle: for g differentiable on
the closed disc of radius r about c and |w - c| < r, the average over θ ∈ [0, 2π] of
(ζ - w)⁻¹ (ζ - c) g(ζ), where ζ = c + r exp(iθ), is g(w). 

### `ringInverse_apply_of_isUnit`

 The inverse of a unit of the ring of continuous complex functions is its pointwise inverse. 

### `isAnalyticFamily_of_continuousAt_of_differentiableAt`

 Let E be a finite-dimensional complex normed space and K a compact R₁ space. If, for all x near
p ∈ E and all k ∈ K, f : E → K → ℂ is jointly continuous at (x, k) and f(·, k) is complex
differentiable at x, then x ↦ f(x, ·) is analytic at p as a map to the Banach space C(K, ℂ), that
is, `IsAnalyticFamily f p`. 

### `isAnalyticFamily_of_differentiable`

 Let E be a finite-dimensional complex normed space, K a compact R₁ space and f : E → K → ℂ. If,
for all x near p ∈ E and all k ∈ K, f is jointly continuous at (x, k) and f(·, k) is complex
differentiable at x, then x ↦ f(x, ·) is analytic at p as a map to C(K, ℂ). The two hypotheses of
`New.isAnalyticFamily_of_continuousAt_of_differentiableAt` are here joined in one. 

### `DiscreteSeries.IsAnalyticFamily.of_analyticAt`

 Let E be a finite-dimensional complex normed space and F a complex normed space. If ι : K → F is
continuous, K is compact and R₁, and Θ is analytic at (p, ι k) for every k, then x ↦ Θ(x, ι ·) is
analytic at p ∈ E as a map to C(K, ℂ), that is, an `IsAnalyticFamily` at p. 

### `analyticAt_of_eventually_differentiableAt`

 Let E and F be finite-dimensional complex normed spaces. A map f : E → F that is complex
differentiable at every point near p is analytic at p. 

### `hasFDerivAt_mvPolynomial_eval`

 A complex polynomial P in finitely many variables is differentiable at every x, with
derivative v ↦ ∑ᵢ (∂P/∂Xᵢ)(x)·vᵢ, given by the formal partial derivatives. 

 ## The Schwarz lemma, holomorphic parameter integrals, Mellin integrals 

### `New.eq_fderiv_of_double`

 A map P between complex normed spaces that is complex differentiable at 0 and satisfies
P(w + w) = P(w) + P(w) for all w equals its derivative at 0, so is ℂ-linear. 

### `New.norm_sub_le_of_holomorphic_bdd`

 Schwarz lemma, at the centre of a ball: if a map f between complex normed spaces is complex
differentiable and of norm at most B on the open ball of radius r about c, then
‖f(z) − f(c)‖ ≤ (2B/r)·‖z − c‖ for z in that ball. 

### `New.aestronglyMeasurable_clm_of_apply`

 A family `A` of bounded operators on a finite-dimensional space `E` is a.e. strongly measurable
if `x ↦ A x y` is so for every vector `y`. 

### `New.eventually_differentiableAt_integral`

 Holomorphy of a parameter integral, the parameter `w` lying in a finite-dimensional space `E`.
Let each `f w : X → F` be a.e. strongly measurable for the measure `μ`, and for all `w` near `z`
and all `x` let `f · x` be complex differentiable at `w` with `‖f w x‖ ≤ g x`, `g` integrable.
Then `w ↦ ∫ f w x dμ` is differentiable at all `w` near `z`. 

### `New.analyticOnNhd_integral_mul_rpow`

 A Mellin integral that converges at two points converges between them. Let N > 0 be a
measurable function on X and T a complex-valued function on X. If the norm of T·N^s has finite
integral and T·N^t is integrable for μ, then T·N^z is integrable for real z in [s, t], and
z ↦ ∫ T·N^z dμ is continuous on [s, t] and real-analytic on (s, t). 


## Submodules as complex normed spaces

A submodule of a complex normed space is a normed space over ℂ, for the seminormed group structure
that comes from its normed group structure.


 ## Analytic functions vanishing on the image of a submersion 

### `New.eq_zero_of_submersion`

 Let E, F be complex Banach spaces, G entire on F, and f : E → F strictly differentiable at a
with surjective derivative. If G ∘ f vanishes near a, then G = 0. 


## Euler's beta integral and Hua's integral bound

The integrals are lower Lebesgue integrals with values in `[0, ∞]`.


### `New.lintegral_norm_add_rpow`

 Euler's beta integral: for Im z > 0 and s > 1/2, the integral over real t of |z + t|^{−2s}
equals √π Γ(s − 1/2)/Γ(s) · (Im z)^{−(2s−1)}. 

### `New.norm_det_star_mul_self_add_vecMulVec`

 For a square matrix C over ℂ and a row vector y, |det (C⋆C + (yC)⋆(yC))| = |det C|² (1 + |y|²),
where ⋆ is the conjugate transpose. The hypothesis det C ≠ 0 is not used. 

### `New.lintegral_one_add_sum_norm_sq_inv_pow`

 The integral of (1 + |y|²)^{−(k+1)} over y ∈ ℂ^κ, k the number of elements of κ, is π^k/k!. 

### `New.lintegral_norm_det_add_vecMulVec_inv_pow_le`

 One row of Hua's bound. Let `M` be positive definite and `S` invertible, both of size `k ≤ r`,
and put `w = v S + a` for a row vector `v` in `ℂ ^ k`. The integral of
`|det (M + wᴴ w)| ^ (-(r + 1))` over `v` is at most `π ^ k / (k! |det S|²) |det M| ^ (-r)`. 

### `New.hua_integral_le`

 Hua's integral bound. Let `M` be positive definite and `S` invertible, both of size `k`, let
`c ≥ 0`, `r ≥ k`, and put `w i = y i S + a i` for row vectors `y i` in `ℂ ^ k`. The integral of
`c |det (M + ∑_{i ∈ s} (w i)ᴴ (w i))| ^ (-(|s| + r))` over the rows `y i`, `i ∈ s`, is at most
`c (π ^ k / (k! |det S|²)) ^ |s| |det M| ^ (-r)`. The argument `x` of the iterated integral
`∫⋯∫⁻_s` (`MeasureTheory.lmarginal`) fixes the rows outside `s`, which do not occur in the
integrand. 

### `New.pi_pow_div_factorial_le_one`

 The volume `π ^ k / k!` of the unit ball of `ℂ ^ k` is at most `1` for `k ≥ 7`. 

### `New.lintegral_comp_mul_add`

 For an invertible matrix `S` and a measurable `g`, the substitution `A ↦ S A + c` on matrices
with rows in `ℂ ^ κ` multiplies `∫⁻ g` by `|det S| ^ (-2 #κ)`. 

### `New.measurable_det_add_conjTranspose_mul`

 For fixed matrices `S`, `c`, `G` the map `A ↦ det (G + (S A + c)ᴴ (S A + c))` is measurable. 

### `New.lintegral_norm_det_add_inv_pow_le`

 Hua's bound over matrices. Let `v = S A + c` with `S` invertible, where the rows of `A`
run through `ℂ ^ κ` and `#κ ≥ 7`, and let `G` be positive definite. The integral of
`C |det (G + vᴴ v)| ^ (-(#κ + #ι))` is at most `C |det S| ^ (-2 #κ) |det G| ^ (-#κ)`. 
