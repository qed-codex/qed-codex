---
{
  "module": "src/New/Spanning/Bessel/LargeFunction.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Bessel/LargeFunction.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Bessel/LargeFunction.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Bessel systems of discrete series type and a Bessel function large at a point

Given a unitary frame that diagonalises the form `New.Shape.J₁`,
`New.Filling.IsDiscreteSeriesBessel` ties an abstract Bessel system `New.BesselSystem` to a discrete
series parameter `l` and a weight `kw` of the subgroup `H = U(X₀)`. Let `𝖴` be the unipotent group
`New.Shape.Form.besselU` and let `R = 𝖴 H` be the Bessel group, realised as the subgroup
`New.Shape.besselGraph` of `G₁ × H`. There is a point `x` of bounded size at which the period of a
discrete series coefficient over `R` is large. For a parameter of large gap, the average of the
coefficient over `R` converges absolutely (`integrable_besselIntegrand`). It is a Bessel function
(`isBesselFunction_besselAverage`) that the kernel of the discrete series reproduces
(`convolve_besselAverage`).

## Main definitions and results

* `New.DiscreteSeries.UnitarySignFrame`: a unitary frame taking `J₁` to the diagonal matrix of signs
  `ε`.
* `New.Filling.IsDiscreteSeriesBessel`: the Bessel system has type `(l, kw)`.
* `New.DiscreteSeries.IsSteep.exists_stationary_point`: a point `x` of bounded length at which the
  period over `R` is large. It carries the stationary position of `U(X₀)` to the standard frame.

Notions from other files:
* `New.Shape.G₁`: the unitary group of the complex hermitian form made of ϱ hyperbolic planes, the
  standard positive form on X₀ = ℂ^κ, and one vector z with h(z, z) = −1. Its Gram matrix is
  `splitGram ϱ (middleGram κ 1)`, indexed by `New.Shape.BesselIndex`. Here n = ϱ + 1, k = |κ| and
  r is the dimension of the whole space.
* `New.Shape.besselGraph`: the Bessel group `R = 𝖴 H`, stored as the pairs of an element of G₁ and
  its image in H, with the measure `du dh`.
* `New.simpleRootSum`: the sum of the entries just above the diagonal on the frame e₁, …, e_ϱ, z.
* `New.besselLength`: for y in G₁, the infimum of ‖s y‖ + 1 over s in R; it is the length of y.
* `New.HCParam.HasLargeGap l A`: for `l = 2λ` with N coordinates, the entries are distinct, of the
  parity of N − 1, and entries of `λ` at coordinates of opposite sign are 500 N³ + A apart or more.

## Relation to the literature

See `New.Appendix.DiscreteSeries.Periods` for related work. See
`Lib.DiscreteSeries.Bessel.UnipotentHaarMeasure` for sources.


### `New.DiscreteSeries.UnitarySignFrame`

 A fixed unitary matrix p with pᴴJ₁p the diagonal matrix of the signs ε, where
J₁ = `New.Shape.J₁`. 

### `New.DiscreteSeries.UnitarySignFrame.mem_unitary`

 The matrix `p` is unitary. 

### `New.Filling.IsDiscreteSeriesBessel`

 The Bessel system `B` has type `(l, kw)`: its full function is the Bessel function of the
discrete series of parameter `l`, with values in the representation of `H` of weight `kw`. 

### `New.Filling.IsDiscreteSeriesBessel.deg_eq`

 The degree is given by Weyl's dimension polynomial at `l`. 

### `New.Filling.IsDiscreteSeriesBessel.exists_conj_rep_eq_schur`

 After an invertible change of coordinates `A`, the representation on the values is given by
  the transposed Schur matrix of weight `kw` at `gᵀ`. Here `Unit` is a set of places with one
  point. 

### `New.Filling.IsDiscreteSeriesBessel.integral_dsKernel_mul`

 The full function is fixed by right convolution with the kernel `l.dsKernel`, carried over
  from `USign ε` by the fixed frame. 

### `New.Filling.IsDiscreteSeriesBessel.exists_eq_besselAverage`

 The full function is `c ∫_R c_l(x⁻¹ s y) π(s)⁻¹ v ds` for a constant `c`, a point `x` and a
  vector `v`, and the integral converges absolutely. Here `c_l` is the coefficient of `l` and `π`
  is the representation of `R` that is given by `B.rep` on `H` and a character on `𝖴`. 


## The stationary point

The point `x` carries the stationary position of `H` in `G₁` to the standard frame, by Witt's
theorem.


### `lintegral_unfold_besselGraphMeasure`

 The measure on `R` unfolds 𝖴∖G₁ to G₁: for measurable `f ≥ 0`, the integral of `f (x s y)` over
`s` in `R` and then over `y` in G₁ for `besselQuotMeasure`, which computes integrals over 𝖴∖G₁,
is the integral of `f` over G₁. 

### `exists_sub_one_mul_frameCols_eq`

 For `s` in `besselGraph` (the group `R`), its first component `s.val.fst` lowers the flag of the
frame `e₁, …, e_ϱ, z`: `(s.val.fst - 1) * frameCols = isotropicCols * N` for some strictly
triangular `N`. Here `frameCols` has columns `e₁, …, e_ϱ, z` and `isotropicCols` has columns
`e₁, …, e_ϱ`. The sum of the entries `N a a.succ` is `simpleRootSum s.val.fst`. 

### `exists_sub_one_mul_definiteCols_eq`

 An element `s` of `besselGraph` (the group `R`) acts on `X₀`, the span of the columns of
`definiteCols`, by its image `s.val.snd` in `H`, modulo the span of `e₁, …, e_ϱ` (the columns of
`isotropicCols`). 

### `exists_besselGraph_fst_eq`

 Let `g` in `G₁` lower the flag of the frame `e₁, …, e_ϱ, z`. That is, `g - 1` maps the frame
into the span of `e₁, …, e_ϱ` by a strictly triangular matrix `N`. Then `g` is the first component
`s.val.fst` of some `s` in `besselGraph` (the group `R`). 

### `besselPairHom`

 The map `s ↦ (x⁻¹ s x, h)`, where `h` is the image of `s` in `H` and `x⁻¹ s x` is written in the
frame of signs `ε`. 

### `isProperMap_besselPairHom_fst`

 The first component `s ↦ x⁻¹ s x` of `besselPairHom x` is proper: `R` is closed in `G₁ × H` and
`H` is compact. 

### `subOnePair_besselPairHom_fst`

 The first entry of `subOnePair (besselPairHom x) s`, the first component minus one, is the
conjugate of `s - 1` by `x p`, where `p` is the frame of signs `ε`. 

### `besselPairHom_snd_val`

 The second component of `besselPairHom x s` has the matrix of the image of `s` in `H`. 

### `subOnePair_besselPairHom_snd`

 The second entry of `subOnePair (besselPairHom x) s` is the image of `s` in `H`, minus one. 

### `norm_frame_mulVec_le`

 The unitary frame `p` takes a vector with entries of modulus at most `M` to one of length at
most `√r M`, where `r` is the dimension. 

### `IsPosition.exists_mul_eq_frameCols_and_besselLength_le`

 Take a position (`IsPosition`) of `H = U(X₀)` in `U(ε)`: independent vectors `v₁, …, v_n` (the
columns of `v`) whose products for the form `signMatrix ε` vanish except that of `v_n` with itself,
and an isometry `i₀` of `X₀` into their orthogonal complement. Let `v_n` have norm `-1`. Let
`w 0 = v₁, …, w (n - 1) = v_n` continue to a sequence such that `w 0, …, w (2 n - 2)` have entries
of modulus at most `M ≥ 1`, and the product of `w a` and `w b` is `0` for `a + b < 2 n - 2` and `-1`
for `a + b = 2 n - 2`. Then there is an `x` in `G₁` such that `x p`, where `p` is the frame of signs
`ε`, takes `i₀` to the inclusion of `X₀` and `v₁, …, v_n` to `e₁, …, e_ϱ, z`, and such that
`besselLength x`, the infimum of `‖s x‖ + 1` over `s` in the Bessel group, is at most `8 n √r M`. 

### `initCols_eq_of_frame`

 If `x p` takes the columns of `v` to the frame, then its first ϱ columns `initCols v` are the
images of `e₁, …, e_ϱ`, the columns of `isotropicCols`, under the inverse of `x p`. 

### `lowersFlag_besselPairHom`

 At a point `x` such that `x p` sends the columns `v₁, …, v_{ϱ+1}` of `v` to the frame
`frameCols`, `x⁻¹ s x - 1` lowers the flag of the `v_j` (`LowersFlag`: it maps the span of the first
`j` into that of the first `j - 1`). The sum of the coefficients of `v_j` in the image of `v_{j+1}`
is `simpleRootSum` of the `G₁` component of `s`. 

### `inducesOn_besselPairHom`

 Take a point `x` such that `x p` takes `i₀` to `definiteCols` and takes the columns of `v` to
`frameCols`. Then every `s` in `besselGraph` (the group `R`) satisfies `InducesOn` for the two
components of `subOnePair (besselPairHom x) s`. That is, `x⁻¹ s x` acts by the image of `s` in `H`
on the image of `i₀`, modulo the span of `v₁, …, v_ϱ`. 

### `exists_besselPairHom_fst_eq`

 Let `x` be in `G₁` and `p.matrix` the unitary matrix of `UnitarySignFrame`, with
`p.matrixᴴ J₁ p.matrix = diag(ε)`. Suppose `x * p.matrix` takes the columns of `v` to `frameCols`,
the frame `e₁, …, e_ϱ, z`. Let `g` be in `positionGroup ε v`: the `g` in `USign ε` such that `g - 1`
maps the span of the first `j` columns of `v` into the span of the first `j - 1`, for the `j` up to
a fixed bound. Then `g` is the first component `x⁻¹ s x` of `besselPairHom x s` for some `s` in
`besselGraph` (the group `R`). 

### `mul_sqrt_mul_pow_le_pow`

 The bound `8 n √r M` of `IsPosition.exists_mul_eq_frameCols_and_besselLength_le` at
`M = (3 B + a) ^ (2 n)` is at most `b ^ (5 n)` when `1 ≤ B`, `3 B + a ≤ b ^ 2` and `8 n r ≤ b`. 

### `IsSteep.exists_stationary_point`

 Split the coordinates of `G₁` into `X` and `2 n` more (by `e`), and those of `H` into `X` and
one more (by `τ`). Let the parameter `l` of `U(ε)` be steep with bound `B ≥ 1` (its lowest `K`-type
has weight `0` on `X` and decreasing weight in `[-3 B, -B]` on the others, where the signs
alternate), and let the lowest `K`-type of the parameter `u` of `H` have weight `a` at the last
coordinate and `0` on `X`. Let both parameters have entries of modulus at most `L` and large gap
(`HasLargeGap`: for `2λ` with `N` coordinates, entries of `λ` at coordinates of opposite sign differ
by at least `500 N³ + excess`), where `10 ^ 30 ((r + k)² log β)³ ≤ excess`. If `10 ^ 12 ≤ β`,
`r + k + L ≤ β`, `3 B + a ≤ b ^ 2` and `8 n r ≤ b`, there is a point `x` whose length
`besselLength x`, the infimum of `‖s x‖ + 1` over `s` in `R`, is at most `b ^ (5 n)`, and such that
the volume of `{‖x⁻¹ s x - 1‖ ≤ 1}` in `R` is at most `β ^ (20 (r + k)²)` times the modulus of the
period. The period is the integral over `s` in `R`, with image `t` in `H`, of `c_l(x⁻¹ s x)` times
the conjugate of `c_u(t)` times `exp (conj σ - σ)`. Here `c_l = l.dsCoeff` and `c_u = u.dsCoeff` are
the discrete series coefficients, and `σ = simpleRootSum s` is the sum of the entries of `s` just
above the diagonal on the frame `e₁, …, e_ϱ, z`. 

 ## The Bessel integral 

### `measurePreserving_unfold_besselGraphMeasure`

 The map `(y, s) ↦ s y` carries the measures of 𝖴∖G₁ and of the Bessel group `R = 𝖴 H` to the
Haar measure of G₁. 

### `besselBallVolume`

 The volume of the set of `s` in `R` with `‖x⁻¹ s x - 1‖ ≤ 1`, the matrix `x⁻¹ s x` being written
in the frame of signs `ε` (the first component of `besselPairHom x s`). 

### `besselBallVolume_ne_top`

 The ball whose volume is `besselBallVolume x` has finite measure, as the conjugation by `x` is
proper on `R`. 

### `besselBallVolume_ne_zero`

 The ball whose volume is `besselBallVolume x` has nonzero measure, as it is a neighbourhood of
`1` in `R`. 

### `lintegral_decay_le_besselBallVolume`

 The covering bound: let `N = 9 r ^ 2`. The integral of `(2 / ‖x⁻¹ s y‖) ^ N` over `s` in
`besselGraph` (the group `R`) is at most `16 ^ N` times `besselBallVolume x`, uniformly in `y`. The
norm is the operator norm in the frame of signs `ε` (via `frameEquiv`). 

### `norm_dsCoeffInFrame_le`

 If `l` has the gap `500 r ^ 3 + excess` (`HasLargeGap`), its coefficient `c_λ`, which is
`l.dsCoeffInFrame`, satisfies `|c_λ(g)| ≤ (2 / ‖g‖) ^ (j + 9 r ^ 2)` for `j ≤ excess`, the norm
being read in the frame of signs `ε`. 

### `continuous_besselIntegrand`

 For a continuous representation `rep`, the integrand `besselIntegrand l rep x v y s`, which is
`c_λ(x⁻¹ s y) π(s)⁻¹ v` with `c_λ = l.dsCoeffInFrame`, is jointly continuous in `y` and `s`. 

### `enorm_besselIntegrand`

 For a unit vector `v`, the norm of the integrand `c_λ(x⁻¹ s y) π(s)⁻¹ v` is `|c_λ(x⁻¹ s y)|`,
as `π` is unitary. 

### `lintegral_enorm_besselIntegrand_le`

 For a unit vector `v` and a parameter `l` of gap `500 r³ + excess`, the integral over `R` of the
norm of `besselIntegrand l rep x v y` is at most `16 ^ (9 r ^ 2)` times `besselBallVolume x`, the
volume of `{‖x⁻¹ s x - 1‖ ≤ 1}` in `R`. 

### `integrable_besselIntegrand`

 For a continuous representation `rep`, a unit vector `v` and a parameter `l` of gap
`500 r³ + excess`, the integral over `R` defining `besselAverage l rep x v y` converges
absolutely. 

### `besselAverage_mul`

 Let `rep` be a continuous unitary representation of `H` on `ℂ^I`, `v` a unit vector of `ℂ^I`,
`x` a point of `G₁`, and `l = 2λ` a parameter with coefficient `c_λ = l.dsCoeffInFrame` and large
gap. For `s = (g, h)` in `R` let `π(s)` be the scalar `wave (simpleRootSum g)` times the operator
`besselValueRep rep h` of `rep h`. Let `W = besselAverage l rep x v`, that is,
`W(y) = ∫_R c_λ(x⁻¹ t y) π(t)⁻¹ v dt` for the measure `du dh` on `R = 𝖴 H`. Then
`W(s y) = π(s) W(y)` for all `s` in `R` and `y` in `G₁`. 

### `isBesselFunction_besselAverage`

 Let `rep` be a continuous unitary representation of `H`, `v` a unit vector, and `l = 2λ` a
parameter with coefficient `c_λ = l.dsCoeffInFrame` and large gap. Let `π` be the representation of
`R = 𝖴 H` that is `rep` on `H` and the character `ψ(u) = exp (σ - conj σ)`, `σ = simpleRootSum u`,
on the unipotent group `𝖴`. Then `W = besselAverage l rep x v`, given by
`W(y) = ∫_R c_λ(x⁻¹ s y) π(s)⁻¹ v ds`, is a Bessel function: it is bounded and measurable, with
`W(u y) = ψ(u) W(y)` for `u` in `𝖴` and `W(h y) = rep h W(y)` for `h` in `H`. 

### `convolve_besselAverage`

 Let `rep` be a continuous unitary representation of `H` on `ℂ^I`, `v` a unit vector of `ℂ^I`,
`x` a point of `G₁`, and `l = 2λ` a parameter with coefficient `c_λ = l.dsCoeffInFrame`, formal
degree `deg` and large gap. Let `W = besselAverage l rep x v`. Then convolution with the idempotent
kernel `e_λ = deg c_λ` reproduces `W`: `∫ e_λ(a⁻¹) W(y a) da = W(y)` for all `y` in `G₁`. 

### `enorm_besselAverage_le`

 For a unit vector `v`, the norm of `besselAverage l rep x v y` is at most the integral of
`|c_λ(x⁻¹ s y)|` over `s` in `R`, where `c_λ = l.dsCoeffInFrame`. 

### `integrable_besselAverage`

 Let `rep` be a continuous unitary representation of `H`, `v` a unit vector, and `l = 2λ` a
parameter with coefficient `c_λ = l.dsCoeffInFrame` and large gap. Then
`W = besselAverage l rep x v`, given by `W(y) = ∫_R c_λ(x⁻¹ s y) π(s)⁻¹ v ds` with `π` the unitary
representation of `R = 𝖴 H` in `besselIntegrand`, is integrable for `besselQuotMeasure`, the measure
on G₁ that computes integrals over 𝖴∖G₁. 

### `formalDegree_mul_integral_norm_sq_besselAverage`

 The norm is a period. Let `rep` be a continuous unitary representation of `H`, `v` a unit
vector, and `l = 2λ` a parameter with coefficient `c_λ = l.dsCoeffInFrame`, formal degree `deg` and
large gap. Let `W = besselAverage l rep x v`. Then `deg ‖W‖₂ ^ 2 = ⟪v, W(x)⟫`, the norm being that
of L²(𝖴∖G₁), computed by `besselQuotMeasure`. 

### `besselBallVolume_le_of_period`

 Let `rep` be a continuous unitary representation of `H` on `ℂ^I`, `v` a vector of `ℂ^I` such
that `⟪v, rep k v⟫` is the coefficient of the parameter `u` at each `k` in `H`, and `l = 2λ` a
parameter with coefficient `c_λ = l.dsCoeffInFrame` and large gap. Let `π` be the representation of
`R = 𝖴 H` that is `rep` on `H` and the character `g ↦ exp (σ - conj σ)`, `σ = simpleRootSum g`, on
`𝖴`. Let `W = besselAverage l rep x v`. Suppose that `besselBallVolume x`, the volume of
`{‖x⁻¹ s x - 1‖ ≤ 1}` in `R`, is at most `P ≥ 0` times the modulus of the period
`∫_R c_λ(x⁻¹ s x) ⟪v, π(s)⁻¹ v⟫ ds`. Then it is at most `P` times the formal degree of `l` times
`‖W‖₂ ^ 2`, the norm being that of L²(𝖴∖G₁). 
