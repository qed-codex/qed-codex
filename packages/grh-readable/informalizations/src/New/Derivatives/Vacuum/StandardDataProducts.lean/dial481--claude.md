---
{
  "module": "src/New/Derivatives/Vacuum/StandardDataProducts.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Derivatives/Vacuum/StandardDataProducts.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Derivatives/Vacuum/StandardDataProducts.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Standard data as products of theta functions of the curve

* `New.IsTightFrame.isResolution`: a tight frame of length `b²` gives a resolution of the identity
  on `Eⁿ`.
* `New.CMLattice.exists_prod_twistedTranslate_eq_thetaProd_mul`: a product of translates of `θ` by
  `δ`-division points, taken at `δ̄ z`, is a power of a product of copies of `θ` times an integral
  series.
* `New.Parameters.exists_isVacuumExpansion`: the integral vacuum is an integral combination of
  translates of a vector whose theta function is a product of copies of `θ` along a tight frame;
  `New.Parameters.IsVacuumExpansion` collects the properties of this expansion.
* `New.Parameters.exists_jetSeries_map_eq_thetaProd_pow_mul`: the theta function of standard data of
  level `δ ≠ 0`, taken at `δ̄ (√(2π / √d) / Ω₀) z` with `d` and `Ω₀` as below, is the power `δ δ̄`
  of the product of `θ` along a resolution of the identity times an integral series in the
  parameters of these copies.

Standard data are integral combinations of translates of the integral vacuum. The proof has three
steps. Fourier inversion writes the integral vacuum through the translates of one product of copies
of `θ`, with a denominator prime to `p`. A translate of this product is a product of translates.
Each translated factor falls under the integrality principle on one curve.

Notions from other files:
* `finiteImage x` is the finite adelic vector `α⁻¹ x` of a rational vector `x`, where `α` is the
  idele of the Weil data of `E`; its coordinates lie in `Ô E` exactly when those of `x` lie in the
  lattice `𝔞₀ = E ∩ α Ô`.
* `V.ϱ (finVec x)` is the Heisenberg translation of `𝒮 V` by the finite adelic vector `α x`, called
  the translation by `x` below, and `V.finHeisenbergOp x` is this translation times a root of unity.
* `intVacuum V`, the integral vacuum, is the vacuum `V.vacElem` (a Gaussian times the signed
  indicator of the standard lattice) times a fixed power of the vacuum scale of the parameters.
* `daggerForms u` are the linear forms `u_j† z` read in `ℂ_p`, and `C.thetaProd μ m` is the product
  `∏ θ(μ_j z) ^ m j` of copies of the theta function of the curve `C`.
* `V.jetSeries c f` is the Taylor series of the theta function of `f` in Fock's coordinates, taken
  at `c z`. Here `P.areaScale` is the number `√(2π / √d)`, where `K = ℚ(√-d)`, and `P.cmPeriod` is
  the fixed period `Ω₀` of `K`: the lattice of the curve `P.cmCurve` is `Ω₀ 𝓞_K`. The factor
  `P.areaScale / P.cmPeriod` passes from Fock's coordinates to those of the curve
  `ℂ / cmPeriod 𝓞_K`.
* `finiteImage id a ∈ Ô E` says that the element `a` of `E` lies in `𝔞₀`; `Φ τ` is the complex
  embedding of the infinite place `τ` in the CM type.
* `IsTightFrame w m M` says that the `w i` lie in `𝔞₀` and that the matrix
  `(∑ m i τ(w i) conj σ(w i))`, indexed by infinite places `τ` and `σ`, is `M` times the identity.
  The number `M` is called the length of the frame.
* `V : Space E n ε` is a hermitian space of rank `n` with signs `ε` at the infinite places, together
  with an adelic point, `𝒮 V` is its Weil model, `V.θ` the theta functional on it, and
  `V.finitePart` the span of the images of the vacuum under the operators `V.finHeisenbergOp x`.
* `taylorVia ιₚ f` is the Taylor series of `f` at `0` read in `ℂ_p`, and `linearSeries μ` the linear
  form `μ` as a power series. `C.twistedTranslate k a f` is the translate of `f`, of weight `k`, by
  `a` times the factor that keeps it a theta function.


### `resolutionVectors`

 The vectors `w i / ν`, placed in each copy of `E` in `Eⁿ`: the vector of index `(i, c)` has
`w i / ν` in the coordinate `c` and `0` elsewhere. 

### `dagger_resolutionVectors`

 The linear form `u† z` of the vector `u` of index `(i, c)` in `resolutionVectors w ν` involves
only the coordinate `c`, with coefficient `conj (τ (w i)) / ν` at the infinite place `τ`. 

### `IsTightFrame.isResolution`

 Let `w` be a tight frame with all multiplicities one and frame bound `b * b ≠ 0`: the matrix
`(∑ Φ τ (w i) * conj (Φ σ (w i)))`, indexed by infinite places `τ` and `σ`, is `b * b` times the
identity. For `k ≠ 0` this gives a resolution of the identity `z = ∑ k² (u† z) u` on `Eⁿ`. Here `u`
runs over the vectors `w i / (b k)` (`resolutionVectors w (b * k)`), placed in each copy of `E`. 

### `Parameters.isResolution_resolutionVectors_zeta_pow`

 In the field `E = P.E s` of level `s` of the parameters `P` let `ζ = P.ζ s`, a primitive root of
unity of order `q₁ = P.q₁ s`. The vectors `ζ ^ i / q₁` for `0 ≤ i < q₁`, each taken `q₁` times and
placed in each copy of `E`, are a resolution of the identity on `Eⁿ`. 

### `CMLattice.exists_prod_twistedTranslate_eq_thetaProd_mul`

 Let `d` be a prime congruent to `7` modulo `8`, `C` a lattice with complex multiplication by the
integers of `ℚ(√-d)`, and `δ ≠ 0` such an integer, of norm `N`. Write `T_y` for the twisted
translation `C.twistedTranslate 1 y`, whose degree `1` is that of the theta function `θ` of `C`. If
`δ y_i` is a period of `C` for every `i`, the product of the `(T_{y_i} θ)(δ̄ z_i)` along linear
forms `z_i = μ_i z` is `∏ θ(z_i) ^ N` times an integral series in the parameters at the `z_i`, an
element of `C.multiSeriesRing μ`. 

### `mem_integralAfter_of_nsmul_mem`

 Let `ν` be prime to `p` and `ν y` lie in the standard lattice `Ô E ^ n`, where `E = P.E s`. For
every integer `δ` of `K` the vector `y` lies in `integralAfter δ` of the places above `p`, that is,
the coordinates of `δ y` are integral at these places. 

### `finiteImage_resolutionVectors_mem`

 If the `w i` lie in the lattice `𝔞₀` (their finite images are integral) and `ν` is prime to
`p`, the finite images of the vectors `w i / ν` of `Eⁿ` are integral at all places above `p`. 

### `exists_coprime_mul_mem_of_mem_integralAfter`

 A finite adelic vector that is integral at the places above `p` becomes integral everywhere
when it is multiplied by a suitable number prime to `p`. 

### `exists_rho_finiteImage_eq_and_coprime_mul_mem`

 Let `V` be a standard space over `E = P.E s` (its signs `ε` are `+1` and its point is the
identity), and let `F` lie in the finite part of its Weil model `𝒮 V`, the span of the translates of
the vacuum by finite adelic vectors. Here `V.ϱ (finVec x)` is the Heisenberg translation by the
adelic vector with finite part `α x` and real part zero. If `δ x` is integral above `p`, it acts on
`F` as the translation by a rational vector `γ` with `δ γ` in `𝔞₀ⁿ ⊗ ℤ_(p)`: for a number `m` prime
to `p`, the vector `m δ γ` lies in the lattice `𝔞₀ⁿ` (its finite image is integral). 

### `exists_coprime_isTightFrame_sq`

 There is a tight frame in the CM field `P.E s`, with all multiplicities one, whose length is
the square of a number `b` prime to `p`. It repeats `b` times each vector of a tight frame of
length `b`: that of the powers of `ζ` if `p` does not divide `q₁`, and otherwise that of a length
prime to `q₁`. 

### `mul_neg_sum_mul_conj_mem_cmCurve_lattice`

 Let `w` and `m δ γ` have finite images in `Ô (P.E s)`, where `δ` is an integer of the imaginary
quadratic field `P.K`. If `m * b` divides `k`, then multiplying by `k δ` sends the point
`-(cmPeriod / b) ∑ Φ τ γ * conj (Φ τ w)`, summed over the infinite places `τ`, into the lattice
`P.cmCurve.Λ`, which is `cmPeriod 𝓞_K`. 

### `intVacuum_eq_sum_smul_vacElem`

 A vector of `𝒮 V` is evaluated as its theta function, here at `finVec (x i)`. If
`∑ c i * V.vacElem (finVec (x i)) = M ≠ 0`, then `intVacuum V` is the sum of the `(M⁻¹ * intVacuum V
(finVec (x i))) • c i • V.vacElem`. 

### `exists_finHeisenbergOp_rho_eq_smul`

 Let `V` be a hermitian space over `E = P.E s` with signs `ε`, and `F` a vector of its Weil model
`𝒮 V`. The operator `V.finHeisenbergOp x` takes the translate of `F` by `y` to a multiple of the
translate of `F` by `x + y`, and the scalar lies in the valuation ring `embValRing` of the embedding
`ιₚ` of `ℂ` in `ℂ_p`. 

### `IsVacuumExpansion`

 An expansion of the integral vacuum of a standard space `V` (of rank `n`, with signs `ε` at the
infinite places) along a tight frame in `E = P.E s`. The frame `w` has length `b²` with `b` prime
to `p`. The integral vacuum is a combination, with `ιₚ`-integral coefficients `a j`, of the
translates of a vector `F` of the Weil model `𝒮 V` by the points `y j`. The vector `F` lies in the
finite part `V.finitePart`, spanned by the images of the vacuum under finite Heisenberg operators,
and the theta functions of its rational translates are products of translates of `θ` along the
frame. 

### `IsVacuumExpansion.coprime`

 The number `b` is prime to `p`. 

### `IsVacuumExpansion.isTightFrame`

 The vectors `w i`, each taken once, are a tight frame of length `b²`. 

### `IsVacuumExpansion.mem_finitePart`

 The vector `F` lies in the finite part of `𝒮 V`. 

### `IsVacuumExpansion.nsmul_mem_stdLattice`

 The vectors `b y j` are integral. 

### `IsVacuumExpansion.intVacuum_eq_sum`

 The integral vacuum is the sum of the translates of `F` by `y j` with coefficients `a j`. 

### `IsVacuumExpansion.jetSeries_eq_prod`

 For rational `γ` and complex `c`, the Taylor series of the theta function of the translate of
  `F` by `γ`, taken at `c (areaScale / cmPeriod) z` with `areaScale = √(2π / √d)` and `cmPeriod`
  the period `Ω₀` of `K = ℚ(√-d)`, is a product of twisted translates of the function `θ` of the
  curve `ℂ / Ω₀ 𝓞_K` along the forms `c u† z`, over the vectors `u` of
  `resolutionVectors w b`. 

### `exists_intVacuum_eq_sum_of_isThetaFunction`

 Let `V` be a standard space, `b` a number prime to `p`, and `F` a vector of its Weil model on
which the theta functional `V.θ` takes the value `1`. Suppose that `entireTheta F`, the theta
function of `F` in Fock's coordinates divided by the Gaussian, is entire and fixed by the signed
translations by the lattice `b 𝔞₀ⁿ`. Then `intVacuum V` is `∑ a j • V.ϱ (finVec (y j)) F`, with
coefficients `a j` in `embValRing` (integral under `ιₚ`) and points `y j` with `b y j` in the
standard lattice `Ô E ^ n`. 

### `exists_isVacuumExpansion`

 The integral vacuum `intVacuum V` of a standard space `V` has an expansion along a tight frame,
`IsVacuumExpansion p V b w F y a`. There are vectors `w i` in `𝔞₀` whose matrix
`(∑ τ(w i) conj σ(w i))` is `b²` times the identity, with `b` prime to `p`. There is a vector `F` in
the finite part of `𝒮 V`, and there are points `y j` with `b y j` integral. The integral vacuum is a
combination, with coefficients `a j` in `embValRing`, of the translates of `F` by the `y j`. 

### `thetaMultiples`

 Let `V` be a space of rank `n` over `E = P.E s` with signs `ε`, and `μ` a family of linear
forms. These are the vectors `g` of its Weil model `𝒮 V` such that the Taylor series of the theta
function of `g` at `c z`, read in `ℂ_p`, is `Θ` times an integral series in the parameters of the
curve `P.cmCurve`, which is `ℂ / cmPeriod 𝓞_K`, at the forms `μ` (an element of
`multiSeriesRing μ`). 

### `map_linearSeries_smul_dagger_resolutionVectors`

 For `k ≠ 0` the form `c̄ (w i / b)† z`, read in `ℂ_p`, is `k c̄` times the form
`(w i / (b k))† z`. 

### `mem_thetaMultiples_of_jetSeries_eq_prod`

 Let `δ ≠ 0` have norm `N`. Suppose the theta function of `g` at `c z` is a product of the
translates `twistedTranslate 1 (t i)` of `θ` along the forms `δ̄ u† z`. Here `u` runs over the
vectors `resolutionVectors w b i`, which for `i = (i', c')` have `w i' / b` in coordinate `c'` and
`0` elsewhere. If `k ≠ 0` and `k δ` takes the `t i` to periods, then `g` lies in `thetaMultiples`:
this product, read in `ℂ_p`, is `θ_u ^ N` times an integral series. Here `θ_u` is the product of the
`θ(u† z) ^ k²` over `u` in `resolutionVectors w (b k)`. 

### `exists_jetSeries_map_eq_thetaProd_pow_mul`

 Let `f` be standard data of level `δ ≠ 0` on a standard space `V`, that is, an integral
combination of images of the integral vacuum under the finite Heisenberg operators of points that
`δ` makes integral above `p`, and let `N = δ δ̄`. There are vectors `u j` with multiplicities `m j`
forming a resolution of the identity (`IsResolution u m`), with each `finiteImage (u j)` integral at
the places above `p`. For these, the Taylor series of the theta function of `f` at
`δ̄ (areaScale / cmPeriod) z`, read in `ℂ_p` through `ιₚ`, is `(∏ θ(u_j† z) ^ m j) ^ N` times an
integral series in the parameters of the curve at the forms `u_j† z`. 
