---
{
  "module": "src/New/Derivatives/Vacuum/TightFrames.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Derivatives/Vacuum/TightFrames.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Derivatives/Vacuum/TightFrames.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Scale of theta Taylor series, tight frames, jet series along lines

Let `P` be parameters, `d = P.d` and `K = ℚ(i√d)`. The file fixes the scale at which Taylor series
of theta functions are taken, and it builds theta functions from tight frames. For a space `V` with
all signs `1` and `f` in `New.Space.finitePart`, the function `New.Space.entireTheta f` is entire on
`ℂ^(places × n)`. A tight frame of length `M` is a finite family of vectors `y` of the lattice `𝔞₀`,
counted with multiplicities, such that `∑ y, (y† z) y = M z` for all `z` in `ℂ^places`, where `y`
stands for the vector of its images `τ y` under the CM type and `y† z = ∑ τ, conj (τ y) * z τ`.

## Main definitions and results

* `New.Parameters.areaScale` is `√(2π / √d)`, and `New.Parameters.periodFactor` is `vacuumRoot`
  divided by the unit of `New.CMLattice.chowla_selberg`.
* `New.Parameters.jetScale`: the scale `periodFactor * areaScale / cmPeriod`.
* `New.Parameters.isTightFrame_pow`: the powers of a primitive `q₁`-th root of unity are a tight
  frame of length `q₁`.
* `New.Space.taylor_line_eq_subst_jetSeries`: the Taylor series of `z ↦ entireTheta f (a • z)` on
  the line spanned by a vector `v` is the restriction of `jetSeries V a f`.
* `New.Parameters.IsResolutionProduct`: the theta functions of the rational translates of a vector
  are products of translated entire functions of linear forms; `IsResolutionProduct.theta_translate`
  and `IsResolutionProduct.jetSeries_translate` give their theta values and Taylor series.
* `New.Parameters.exists_isResolutionProduct_of_isTightFrame`: a product of monomial sections,
  pulled back along a tight frame, is the theta function of a vector with integral values.

Notions from other files:
* `New.Parameters`: a multiple `q₀` of `18480 = 16 · 3 · 5 · 7 · 11` and a prime `d` with
  `d ≡ q₀/2 - 1 mod q₀`. The CM field `E = P.E s` is generated over `K` by a primitive `q₁`-th root
  of unity `ζ`, `q₁ = P.q₁ s`, and `Φ τ : E →+* ℂ` is the embedding of its CM type at the infinite
  place `τ`.
* `New.finiteImage`: for a family `γ` in `E`, the finite adeles `α⁻¹ γ k`, with `α = P.α s` the
  idele of the fractional ideal `𝔞₀`; so `finiteImage id y ∈ Ô E` says that `y` lies in
  `𝔞₀ = E ∩ α Ô`.
* `New.PadicPlace`: a `p`-adic place of `ℂ`, that is, a ring homomorphism `ιₚ : ℂ →+* ℂ_[p]`.
* `New.Space.entireTheta`: for `f` in the space `𝒮 V` of a hermitian space `V`, the function
  `y ↦ θ(ϱ(y) f) exp(|y|²/2)` of a real vector `y` in Fock coordinates, with `θ` the theta
  functional `V.θ` and `ϱ` the Heisenberg representation `V.ϱ`.
* `finVec x`: the adelic vector with finite part `α x` and real part zero. So
  `V.ϱ (finVec (finiteImage γ)) f` is the translate of `f` by the finite image of `γ`.
* `New.CMLattice`: a lattice `C.Λ` in `ℂ`, stable under the integers of `K`, with a marked point of
  order two. Its hermitian form is `C.hermitianForm l z = (π / A) * conj l * z`, with `A = C.area`
  the area of a period parallelogram, and `C.twistedTranslate m l g` is the translate
  `z ↦ g (z + l)` times the Gaussian factor of the form `m • C.hermitianForm`. A section of degree
  `m` is multiplied by `C.multiplier l ^ m` under this translation for `l` in `C.Λ`, where
  `C.multiplier l` is a number of absolute value one.
* `pullForm φ B`: the pull-back `(u, v) ↦ B (φ u) (φ v)` of a form along a linear map `φ`.
* `New.Space.jetSeries`: the series whose coefficient of `z ^ k` is `a ^ |k| / k!` times the theta
  functional of `v ⊗ f`, where `v` is the Fock vector of the monomial `z ^ k`.

## Relation to the literature

A product of monomial sections of a CM curve, pulled back along a tight frame at scale `a / δ̄`, for
an integer `δ` of `K` and a point `a` of the lattice of the curve, is the theta function of a vector
of the finite part, by Fourier inversion. The theta value and the jet series of each rational
translate are the products of those of the translated sections. The values of the vector are
products of torsion values of monomials, so they are integral at every `p`-adic place. Eutactic
stars (sets of vectors that form a tight frame), the isogeny formula for theta functions and
integrality via torsion values are known from the literature. Related work: Conway–Sloane,
Low-dimensional lattices V, 1989; Finis, Divisibility of anticyclotomic L-functions and theta
functions with CM, 2006; Mumford, On the equations defining abelian varieties I, 1966.


 ## The CM curve and the constants fixing the scale 

### `cmCurve`

 The curve `𝓔 = ℂ / Ω₀ 𝓞_K`: a chosen CM lattice that is a complex multiple of `𝓞_K`.
See `latticeModule_cmCurve`. 

### `cmPeriod`

 The period of `K`: a nonzero complex number `Ω₀`, fixed once, such that the lattice of `cmCurve`
is `Ω₀ 𝓞_K`. See `latticeModule_cmCurve`. 

### `latticeModule_cmCurve`

 The lattice of the CM curve `cmCurve` is `Ω₀ 𝓞_K`, the multiple by `Ω₀` of the unit ideal of
`K = ℚ(i√d)`. 

### `chowlaSelbergUnit`

 The number `u` chosen in the Chowla–Selberg formula `CMLattice.chowla_selberg` for
`cmCurve`. See `norm_iota_chowlaSelbergUnit` and `area_mul_norm_chowlaSelbergUnit_sq`. 

### `area_mul_norm_chowlaSelbergUnit_sq`

 The Chowla–Selberg formula for the conjugates of `cmCurve`: for every automorphism `σ` of `ℂ`
over `K`, the area of the lattice conjugate by `σ`, times `‖σ u‖²` for `u = chowlaSelbergUnit`, is
`π exp(c) 2π / √d`, where `c = chowlaSelbergConst d = γ - Re L'/L(1, χ_K)`. 

### `areaScale`

 The number `√(2π / √d)`, as a unit of `ℂ`. 

### `periodFactor`

 The quotient of `vacuumRoot` by `chowlaSelbergUnit`. Here `vacuumRoot` is `(chiFin α)⁻¹ ^ (1/f)`
with the principal branch of the complex power, `f` is the number of infinite places of `E`, and
`chiFin` is the character `x ↦ υ(x) |x| ^ (-1/2)` of the finite ideles, `υ` the splitting character
of the Weil data. The denominator is a unit at every `p`-adic place of `ℂ`, so the two numbers have
the same absolute value there. 

### `jetScale`

 The number `periodFactor * √(2π / √d) / Ω₀`. Taylor series of theta functions are taken at
multiples of this scale. 


## The lattice `𝔞₀` and the powers of `ζ`

The ideal `𝔞₀ conj 𝔞₀` is the inverse different of `E / K`. In comments `α` is the idele of `𝔞₀`,
and `P'(ζ)` is `relDifferentGen`, the value at `ζ` of the derivative of the `q₁`-th cyclotomic
polynomial, which generates the different.


### `IsTightFrame.mul_left`

 Taking each vector of a tight frame `k` times as often multiplies its length by `k`. 

### `exists_norm_adeleExtension_alpha_mul_eq_one`

 Let `φ : E →+* ℂ_[p]` be an embedding of the CM field `E = P.E s`, and let `adeleExtension φ` be
its extension to the finite adeles. There is an element `y` of `𝔞₀⁻¹`, the inverse of the
fractional ideal `𝔞₀` of the idele `α = P.α s`, such that the integral adele `α y` is a unit at the
place of `φ`. 

### `coe_trace_eq_sum`

 The trace of `z` from `E` to `K`, as a complex number, is the sum of its images under the
embeddings of the CM type. 

### `finiteImage_id_eq_inv_alpha_mul`

 The finite image of `x` in `E` is the adele `α⁻¹ x`, with `α = P.α s` the idele of `𝔞₀`. 

### `exists_coe_eq_trace_of_isIntegral`

 If `z P'(ζ)` is integral, where `P'(ζ) = relDifferentGen` generates the different of `E / K`,
then the trace of `z` from `E` to `K` is an integer of `K`. 

### `sum_mul_conj_mem_quadInt`

 Let `x`, `y` in the CM field `E = P.E s` lie in `𝔞₀ = E ∩ α Ô`: the finite adeles
`finiteImage id x = α⁻¹ x` and `finiteImage id y = α⁻¹ y`, with `α = P.α s`, lie in the ring `Ô E`
of integral adeles. Then the hermitian product `∑ τ, Φ τ x * conj (Φ τ y)` lies in `quadInt d`, the
ring of integers of `K` inside `ℂ`. 

### `adeleExtension_alpha`

 The image of the idele `α` of `𝔞₀` under the extension of an embedding `φ : E →+* ℂ_[p]` to the
finite adeles: it is `φ(P'(ζ))⁻¹`, with `P'(ζ) = relDifferentGen`, if the prime of `E` induced by
`φ` divides `betaKInE = (1 + √-d) / 2`, and `1` otherwise. 

### `norm_iota_vacuumRoot`

 At a `p`-adic place `ιₚ` of `ℂ`, the absolute value of `vacuumRoot` is inverse to that of the
finite idele `α = P.α s` of the Weil data at the place of `weightEmbedding ιₚ τ : y ↦ ιₚ (τ ȳ)`, for
every `τ` in the CM type. For an embedding `φ : E →+* ℂ_[p]`, the map `adeleExtension φ` takes the
component of an adele at the prime of `E` induced by `φ` and applies the extension of `φ` to the
completion at that prime. 

### `span_vacuumRoot_eq`

 At a `p`-adic place `ιₚ` of `ℂ` with valuation ring `embValRing`, the number `vacuumRoot`
generates the module spanned by `τ(𝔞̄₀)⁻¹`, the set of the `τ ȳ` with `y` in `𝔞₀⁻¹`. 

### `norm_iota_periodFactor`

 At a `p`-adic place `ιₚ` of `ℂ`, the absolute value of `periodFactor` equals that of
`vacuumRoot`. It is the inverse of the absolute value of the idele `P.α s` of the Weil data at the
place of `weightEmbedding ιₚ τ : y ↦ ιₚ (τ ȳ)`. 

### `norm_periodFactor_mul_conj_le_one`

 For `y` in `𝔞₀` (that is, `α⁻¹ y` is an integral adele) the coefficients
`periodFactor * conj (τ y)` of the linear form `z ↦ periodFactor * y† z` are integral at the
`p`-adic place `ιₚ` of `ℂ`. 

### `norm_iota_periodFactor_eq_one`

 If the prime `p` does not divide `q₁ = P.q₁ s`, the order of the roots of unity that generate
`E = P.E s` over `K`, then `periodFactor` is a unit at the `p`-adic place `ιₚ` of `ℂ`. 

### `finiteImage_coe_mem`

 The integers of `P.E s` have integral finite image: for `a` in the ring of integers `𝓞 (P.E s)`,
the finite adele `α⁻¹ a` (`finiteImage id a`) lies in `Ô (P.E s)`. 

### `eq_of_phi_eq_of_isPrimitiveRoot`

 Two embeddings `Φ σ`, `Φ τ` of the CM type that agree on a primitive `q₁`-th root of unity
belong to the same infinite place. 

### `isTightFrame_pow`

 Orthogonality of characters: for parameters `P : Parameters`, `s : ℕ` and a primitive `q₁`-th
root of unity `z` of `E = P.E s`, with `q₁ = P.q₁ s`, the powers `z ^ i`, `0 ≤ i < q₁`, are a tight
frame of length `q₁` with all multiplicities `1`. 

### `isTightFrame_zeta_pow`

 The powers `ζ ^ i`, `0 ≤ i < q₁`, each taken `k` times, form a tight frame (`IsTightFrame`) with
frame bound `k * q₁`. 


## Jet series as Taylor series along lines

`New.taylorAtZero g` is the Taylor series at `0` of `g : ℂ → ℂ`, and `New.linearSeries μ` is the
linear form `∑ p, μ p * X p`. The space `V.finitePart` is spanned by the translates of the vacuum
under the finite Heisenberg operators.


### `iteratedDeriv_integral_exp_mul_realVac`

 Differentiation under the integral: for `f` in the Schwartz space `𝒮 V` of the hermitian space
`V : Space E n 1` over the CM field `E` and a continuous conjugate-linear form `L`, the `k`-th
derivative at `0` of `t ↦ ∫ exp (t * L w) * g w` is `∫ L w ^ k * g w`. Here `g w` is the Gaussian
`realVac w = exp (-|w|² / 2)` times the value of `f` at `realVec w`. The vector `realVec w` is the
adelic vector with finite part zero whose real part is `w` with its coordinates at `τ` multiplied by
`(2π Im τ(ȷ))^(-1/2)`, where `ȷ` is the element `j` of the Weil data. `normalizedVolume` is Lebesgue
measure divided by `π` to the number of coordinates. 

### `taylor_line_eq_subst_jetSeries`

 Let `V` be a hermitian space with all signs `1` and let `f` lie in `V.finitePart`, the span of
the translates of the vacuum under the finite Heisenberg operators. Then the Taylor series at `0` of
`t ↦ entireTheta f (a • t • v)` is obtained by substituting `v p * X` for the variable with index
`p` in `V.jetSeries a f`. Here `entireTheta f` is the function `y ↦ θ(ϱ(y) f) exp(|y|²/2)` of a real
vector `y`, where `ϱ(y) f` is the translate of `f` by `y` and `θ = V.θ` is the theta functional, a
linear form on `𝒮 V`. `V.jetSeries a f` is the series whose coefficient of `z ^ k` is `a ^ |k| / k!`
times the value of `θ` at `f` tensored at the real places with the polynomial `z ^ k`, seen as a
vector of the Fock model (the Fock vector of `z ^ k`). Here `|k| = ∑ p, k p` and
`k! = ∏ p, (k p)!`. 

### `eq_zero_of_jetSeries_eq_zero`

 For `V : Space E n 1` (all signs `1`), `f` in `V.finitePart` and `a ≠ 0`: if `V.jetSeries a f`,
the Taylor series at `0` of `z ↦ V.entireTheta f (a • z)`, vanishes, then `f = 0`. 

### `_root_.New.taylorAtZero_prod_comp_mul`

 The Taylor series at `0` of a finite product of entire functions `x ↦ G i (c i * x)` is the
product of the Taylor series of the `G i`, with `c i • X` substituted for the variable. 

### `_root_.New.mvPowerSeries_eq_of_forall_line`

 Two power series over `ℂ` in finitely many variables are equal if their restrictions
`rename (fun _ ↦ ()) (rescale v S)` to the line spanned by `v` agree for every vector `v`. 

### `theta_eq_prod_of_entireTheta_smul`

 If `entireTheta f (c • z) = ∏ i, G i (μ i ⬝ᵥ z)` for all `z`, then the theta functional of `f`
is `∏ i, G i 0`. 

### `jetSeries_eq_prod_of_entireTheta_smul`

 Let `V` have all signs `1`, so that `xᴴJx` is the identity at the infinite places. Let `f` lie
in `V.finitePart`, the span of the translates of the vacuum under the finite Heisenberg operators.
Suppose that `entireTheta f (c • z) = ∏ i, G i (μ i ⬝ᵥ z)` for all `z`, with every `G i` entire.
Then `V.jetSeries c f` is the product of the Taylor series of the `G i`, evaluated at the linear
forms `linearSeries (μ i) = ∑ p, μ i p * X p`. 

### `jetSeries_eq_prod`

 Let `V` have all signs `1`, let `f` lie in its finite part, and suppose that
`entireTheta f (c • z) = ∏ i, G i (μ c i ⬝ᵥ z)` for all `c` and `z`, with every `G i` entire. Then
the theta functional of `f` is `∏ i, G i 0`, and for every `c` the series `V.jetSeries c f` is the
product of the Taylor series of the `G i`, evaluated at the linear forms with coefficients
`μ c i`. 


## Vectors built from sections along a tight frame

Fourier inversion turns a product of monomial sections into the theta function of a vector.


### `cmPeriod_mem_cmCurve_lattice`

 The period `cmPeriod` lies in the lattice `cmPeriod 𝓞_K` of the curve `cmCurve`. 

### `norm_map_selfDualAddChar`

 The values of the character `selfDualAddChar` of the finite adeles have finite order, so their
images under a multiplicative map `ι` to a normed field have norm one. 

### `resolutionShift`

 The point `-b ⟨γ k, w j⟩` of `ℂ` for `i = (j, k)`, where
`⟨x, y⟩ = ∑ τ, Φ τ x * conj (Φ τ y)` is the sum over the CM type. 

### `resolutionFormCoeff`

 The coefficients of the linear form `z ↦ a * ∑ τ, conj (Φ τ (w j)) * z (τ, k)` for
`i = (j, k)`. 

### `resolutionLinearForm`

 The linear form `z ↦ a * ∑ τ, conj (Φ τ (w j)) * z (τ, k)` for `i = (j, k)`. 

### `resolutionLinearForm_realImage`

 For `i = (j, k)` the linear form `resolutionLinearForm a w i` is
`z ↦ a * ∑ τ, conj (Φ τ (w j)) * z (τ, k)`. The vector `realImage γ` is the image of `γ` at the
infinite places in Fock coordinates; its entry at `(τ, k)` is `P.areaScale * Φ τ (γ k)`, with
`P.areaScale = √(2π / √d)`. At this vector the form with `a = b / P.areaScale` takes the value
`b * ∑ τ, Φ τ (γ k) * conj (Φ τ (w j))`. 

### `mul_sum_mul_conj_mem_lattice`

 Let `x`, `y` in `P.E s` have integral finite images `α⁻¹ x`, `α⁻¹ y` (`finiteImage id`). Then
multiplying `a ∈ C.Λ` by `x† y = ∑ τ, Φ τ y * conj (Φ τ x)` gives an element of the CM lattice
`C.Λ`. 

### `IsResolutionProduct`

 `F` is the product of the functions `f i` along the vectors `w` at scale `b`: for a rational
vector `γ`, the theta function of `V.ϱ (finVec (finiteImage γ)) F`, the translate of `F` by the
finite image of `γ`, is the product of the twisted translates of the `f i`, each evaluated at a
linear form. The factor `i = (j, k)` is translated by `resolutionShift b w γ i` in degree `m j`:
`C.twistedTranslate m l g` is `z ↦ g (z + l)` times a Gaussian factor. 

### `IsResolutionProduct.mem_finitePart`

 `F` lies in the finite part of `V`. 

### `IsResolutionProduct.differentiable`

 The factors are entire. 

### `IsResolutionProduct.entireTheta_translate`

 The product formula; `P.areaScale = √(2π / √d)`. 

### `IsResolutionProduct.theta_translate`

 The theta value of the translate of a resolution product `F` by the finite image of a rational
vector `γ` is the product of the values at `0` of the translated factors. 

### `IsResolutionProduct.jetSeries_translate`

 Let `V` be a standard space, `C` a lattice in `ℂ` with complex multiplication by the integers of
`K`, and `F` the resolution product of the entire functions `f i`: for every rational vector `γ`,
the function `entireTheta F'` of the translate `F' = V.ϱ (finVec (finiteImage γ)) F` is the product
over `i = (j, k)` of the functions `C.twistedTranslate (m j) l (f i)`, with
`l = -b * ∑ τ, Φ τ (γ k) * conj (Φ τ (w j))`, each at the linear form `z ↦ b / P.areaScale * ∑ τ,
conj (Φ τ (w j)) * z (τ, k)`. Here `C.twistedTranslate n l g` is `z ↦ exp (-n * π * (z * conj
l + |l|² / 2) / C.area) * g (z + l)`. Then `V.jetSeries c F'`, the Taylor series at `0` of
`z ↦ entireTheta F' (c • z)`, is the product of the Taylor series of these translated functions,
each evaluated at the linear form `b / P.areaScale * c * ∑ τ, conj (Φ τ (w j)) * X (τ, k)`. 

### `IsResolutionProduct.norm_iota_apply_le_one`

 Let `δ δ̄ = N ≠ 0` for an integer `δ` of `K`, and let `b δ̄` lie in the lattice `C.Λ`. Let each
finite adele `finiteImage w j = α⁻¹ w j`, with `α = P.α s`, lie in the ring `Ô E` of integral adeles
of `E = P.E s`; that is, `w j` lies in `𝔞₀ = E ∩ α Ô`. Suppose that `F` is the resolution product of
the monomial sections `θ ^ r * (σ ^ 2) ^ t * G ^ u` of `C` with exponents `x i = (r, t, u)`, of
degree `r + 2 t + 3 u = m i.1`: the theta function of each rational translate of `F` is the product
of twisted translates of these sections, evaluated at linear forms. Here `θ` is the theta function
and `σ` the sigma function of `C`, and `G = translatedYThetaCube` is the entire function that equals
`C.translatedY * θ ^ 3` away from the poles of `C.translatedY`. Then the value of `F` at `finVec y`,
the adelic vector with finite part `α y` and real part zero, is integral at the `p`-adic place
`ιₚ : ℂ →+* ℂ_[p]`. 

### `sum_pullForm_resolutionLinearForm_apply`

 Let `w` be a tight frame of length `M` with multiplicities `m`: each `α⁻¹ * w j` is integral,
where `α = P.α s` is the finite idele of the Weil data, and `∑ j, m j * Φ σ (w j) * conj (Φ τ (w
j)) = M δ_{σ τ}`, where `Φ` is the CM type. Let the area `C.area` of a period parallelogram of `C`
be `|b|² M √d / 2`, with `d = P.d`. The forms `m j • C.hermitianForm`, where
`C.hermitianForm l z = (π / C.area) * conj l * z`, pulled back (`pullForm`) along the linear forms
of the frame at scale `b / P.areaScale`, sum to the standard hermitian form. 

### `normalizedShift_prod_comp_of_mem_lattice`

 Let each `f i` be a section of degree `m i.1` of `C`: twisted translation
`C.twistedTranslate (m i.1) l` by a period `l` multiplies it by `C.multiplier l ^ m i.1`. Suppose
that the linear forms `A i` take `u` to periods, and let `B` be the sum of the pull-backs
(`pullForm`) of the forms `m i.1 • C.hermitianForm` along the `A i`. Then the normalized translation
by `u` fixes the product of the `f i ∘ A i`. 

### `exists_isResolutionProduct_of_isTightFrame`

 Let `V` be a standard space (signs `1`, point the identity). Let `δ δ̄ = N ≠ 0` for an integer
`δ` of `K`, and let `w` be a tight frame of length `M` with multiplicities `m`. Let
`x i = (r, t, u)` be exponents of degree `r + 2 t + 3 u = m i.1` (`monomialDeg`). Let `C` be a CM
lattice of area `|a|² M √d / (2 N)` that contains `a`. The monomial section of `x i` is
`θ ^ r * (σ ^ 2) ^ t * G ^ u`, with `θ` the theta function and `σ` the sigma function of `C`. Here
`G = translatedYThetaCube` is the entire function equal to `C.translatedY * θ ^ 3` away from poles.

There is a vector `F` that is the resolution product of these sections along `w` at scale `a / δ̄`.
That is, for every rational vector `γ`, the theta function of the translate of `F` by the finite
image of `γ` is the product of twisted translates of the sections, evaluated at the linear forms of
the frame. The values of `F` at finite adelic vectors are integral at every `p`-adic place `ιₚ` of
`ℂ`. Let `entireTheta F` be the theta function of `F`, as an entire function on `ℂ^(Φ × n)`. It is a
theta function for the lattice `δ̄ 𝔞₀ⁿ`. That is, it is entire and fixed by the translations
`signedShift γ` (the translation by `γ` times its sign `± 1`) along the lattice. 
