---
{
  "module": "src/New/Spanning/Bessel/SchurBound.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Bessel/SchurBound.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Bessel/SchurBound.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Schur's bound for a Bessel function and its derivatives

Let `l = 2λ` be a doubled Harish-Chandra parameter of large gap and `c_λ` the coefficient `dsCoeff`
on `U(diag ε)` of its discrete series; the same letter stands for its pullback
`New.HCParam.dsCoeffInFrame` to `G₁` by the frame. Let `deg` be the formal degree
`New.HCParam.formalDegree`. Write `(F * k) y = ∫ k a⁻¹ • F (y a)` and `e = deg · c_λ`; as
`e a⁻¹ = deg · conj (c_λ a)`, the condition `F * e = F` says that `F` is fixed by the idempotent of
the discrete series. Such a bounded function has right derivatives of all orders, and they are
convolutions with kernels of controlled norm. Schur's bound in `L²(𝖴 ∖ G₁)` follows, `𝖴` being the
unipotent group `besselU`.

Notions from other files:
* `l : New.HCParam ε` is twice a Harish-Chandra parameter; `HasLargeGap A` bounds its gaps below.
* `p : UnitarySignFrame 𝔰 ε` is a unitary frame in which the form of `G₁` is `diag ε`.
* `frameEquiv : G₁ ≃ₜ* U(diag ε)` is conjugation by the frame.
* `Bumps ε` are the smooth compactly supported functions on `U(diag ε)`; `smear f` sends a bump `β`
  to the convolution of the continuous function `f` with `β`.
* `bumpDeriv` is the action of matrices on bumps by differentiation, `adTwist g` precomposes it with
  conjugation by `g`, and `word w` applies the action of the matrix units of the word `w`.
* `New.IsBesselFunction rep F`: `F` is bounded, measurable and transforms by a character under
  `besselU` and by `rep` under `U(κ)`.
* `𝔰.r` is the number of indices `BesselIndex` of `G₁`, and `𝔰.n` is one more than the number of
  hyperbolic planes of the shape `𝔰`.
* `RealPlace.HasSchurBound F rep B C`: `F` has right derivatives of all orders that are again Bessel
  functions, those of order `s ≤ 2 n ^ 2` satisfying Schur's `L²` bound with `B ^ (2 s) C`.
* `besselQuotMeasure` is the measure on `G₁` that represents integration over `besselU ∖ G₁`.

## Relation to the literature

Known result: Smoothness and Schur's orthogonality relations for vectors of a discrete series
representation (Harish-Chandra).


### `isBoundedMeasurable_formalDegree_mul_dsCoeffInFrame`

 Let `l = 2λ` be a doubled Harish-Chandra parameter of large gap, `c_λ = l.dsCoeffInFrame` the
coefficient on `G₁` of its discrete series and `deg = l.formalDegree` the formal degree. Then
`deg · c_λ` is bounded and measurable. 

### `norm_frame_conj_single`

 For the unitary frame `p`, each matrix unit `Matrix.single i j 1` conjugated by it,
`p.matrix⁻¹ * Matrix.single i j 1 * p.matrix`, has norm one. 

### `exists_mem_filtration_smear_word`

 Let `l = 2λ` be a doubled Harish-Chandra parameter with `l.HasLargeGap A` (gap `500 r³ + A`) and
entries bounded by `L`. Let `β` be a bump function whose convolution (`smear`) with `c_λ` is `c_λ`,
the generator of `U(𝔤) c_λ = l.DsModule`. Let `w` be a word of length `s` in the matrix units,
acting through `adTwist p.matrix⁻¹`. The convolution of `c_λ` with the derivative of `β` along `w`
is a vector `x` of step `s` of the filtration of `U(𝔤) c_λ`, with
`‖x‖ ≤ ((r + 1) ^ 4 (L + r + 1 + s)) ^ s`. Here `r = 𝔰.r` is the size of the matrices, and `‖x‖` is
the `L²` norm of `x` times the square root of the formal degree. 

### `convolve_formalDegree_mul_dsCoeffInFrame_self`

 Let `l = 2λ` be a doubled Harish-Chandra parameter of large gap, `c_λ = l.dsCoeffInFrame` the
coefficient on `G₁` of its discrete series and `deg = l.formalDegree` the formal degree. Then
`deg · c_λ` is idempotent under convolution on `G₁`. 

### `convolve_formalDegree_mul_dsCoeffInFrame_comp_frameEquiv`

 Let `l = 2λ` be a doubled Harish-Chandra parameter, `c_λ = l.dsCoeff` its coefficient on
`U(diag ε)`, `deg = l.formalDegree` the inverse of `∫ |c_λ| ^ 2`, and `β` a bump function on
`U(diag ε)`. The convolution on `G₁` of the pullbacks of `deg · c_λ` and `β` by the frame is the
pullback of `deg` times the convolution (`smear`) of `c_λ` with `β` on `U(diag ε)`. 

### `HCParam.HasLargeGap.norm_sq_eq_formalDegree_mul_integral`

 Let `l = 2λ` be a doubled Harish-Chandra parameter of large gap, `c_λ` the coefficient on
`U(diag ε)` of its discrete series and `deg = l.formalDegree` the formal degree. The squared norm
of a vector `x` of `U(𝔤) c_λ = l.DsModule`, a space of smooth functions on `U(diag ε)`, is `deg`
times the integral of `|x| ^ 2`. 

### `exists_derivative_kernels`

 Let `l = 2λ` be a doubled Harish-Chandra parameter of large gap with entries bounded by `L`,
`c_λ = l.dsCoeffInFrame` the coefficient on `G₁` of its discrete series, `deg = l.formalDegree` the
formal degree, and `r = 𝔰.r` the size of the matrices of `G₁`. To each word `w` in the matrix units
belongs an integrable kernel `X w`, with `X [] = deg · c_λ` and `X [] * X w = X w`. For a word of
length `s` the number `‖X w‖₂ ^ 2 / deg` is at most `((r + 1) ^ 4 (L + r + 1 + s)) ^ (2 s)`. For
every bounded measurable `F` with `F * X [] = F` the functions `F * X w` are the right derivatives
of `F`: along a curve `γ` with `γ' t = γ t · Z`, the derivative of `F * X w` at `t` is
`∑ Z a b • (F * X ((a, b) :: w)) (γ t)`. 

### `IsBesselFunction.lintegral_enorm_sq_integral_inner_translate`

 Let `l = 2λ` satisfy `l.HasLargeGap A` (gap `500 r³ + A`), with coefficient `c_λ` on `G₁` and
formal degree `deg`. Let `rep` be a unitary representation of `U(κ)` on `ℂ^I`. Let `F` be a Bessel
function for `rep`, integrable over `𝖴 ∖ G₁` (`besselQuotMeasure`) and fixed by convolution with
`deg · c_λ`. The squared norm in `L²(G₁)` of the matrix coefficient `g ↦ ∫ ⟪F y, F (y g)⟫` is
`‖F‖₂ ^ 4 / deg`, as this coefficient is `c_λ` times `‖F‖₂ ^ 2`. The integral in `y` and the norm
`‖F‖₂` are taken over `𝖴 ∖ G₁`. 

### `IsBesselFunction.convolve_of_integrable`

 Let `F` be a Bessel function on `G₁` for the unitary representation `rep` of `U(κ)`: bounded,
measurable, and transforming on the left by a character under `besselU` and by `rep` under `U(κ)`.
Its convolution with an integrable kernel `k` on `G₁` is again a Bessel function for `rep`. 

### `IsBesselFunction.hasSchurBound_of_convolve_eq`

 **Schur's bound for a Bessel function.** Let `l = 2λ` be a doubled Harish-Chandra parameter with
gap `500 r ^ 3 + A` (`l.HasLargeGap A`) and entries bounded by `L`. Its coefficient is
`c_λ = l.dsCoeffInFrame` on `G₁`, and its formal degree is `deg = l.formalDegree`. Let `rep` be a
unitary representation on `ℂ^I` of `U(κ)`, the unitary group of the positive definite middle part.
Let `F` be a Bessel function for `rep`, integrable over `𝖴 ∖ G₁` and fixed by convolution with
`deg · c_λ`. Let `B ≥ (r + 1) ^ 4 (L + r + 1 + 2 n ^ 2)`. Then `F` has right derivatives `V w` along
the words `w` in the matrix units, which are again Bessel functions for `rep`. Take
`s = |w| ≤ 2 n ^ 2` and `φ` integrable on `G₁`. Then the function `g ↦ ∫ φ y • V w (g y)` has
squared norm at most `B ^ (2 s) ‖F‖₂ ^ 2 ‖φ‖₂ ^ 2 / deg` in `L²(𝖴 ∖ G₁)`, with `‖F‖₂` taken over
`𝖴 ∖ G₁`. 
