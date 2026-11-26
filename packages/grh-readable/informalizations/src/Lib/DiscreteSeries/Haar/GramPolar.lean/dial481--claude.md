---
{
  "module": "src/Lib/DiscreteSeries/Haar/GramPolar.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/DiscreteSeries/Haar/GramPolar.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/DiscreteSeries/Haar/GramPolar.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The polar formula for the Gram map on bases

Let `J` be a hermitian involution of size `r` and `G = U(J)`, with the compact dual Haar measure
`dγ` (`New.haarU`). A basis `Y` whose Gram matrix `T = Yᴴ J Y` is near `J` is `γ σ(T)`, with `γ` in
`G` and `σ` a local section of the Gram map (`New.exists_isGramSection`).

* `New.IsGramSection.lintegral_eq`: the polar formula `dY = (vol U(r) / 2 ^ r) dγ dT`, where
  `vol U(r)` is `New.volU r`. The Jacobian is computed on tangent vectors: `Yᴴ J dY` has hermitian
  part `dT / 2`, and for fixed `T` it is `σᴴ (J γ⁻¹ dγ) σ`, which is skew-hermitian. The constant
  does not depend on the signature of `J`.

Notions from other files:
* `IsHermitianInvolution J`: the complex matrix `J` is hermitian and `J * J = 1`;
* `U J`: the group of `g` with `gᴴ * J * g = J`, where `volume` is the Haar measure `New.haarU J`,
  normalized so that it has mass `1` for `J = 1`;
* `gramCoords J Y`: the real coordinates of the hermitian matrix `Yᴴ * J * Y`;
* `cayleyChart J`: the Cayley parametrization of almost all of `U J` by real matrices `y` with
  `(cayleyDenom J y).det ≠ 0`; the density of the Haar measure there is `cayleyDensity J y` divided
  by `volU r`;
* `logDerivU (cayleyChart J) y`: the linear map `v ↦ γᴴ J dγ(v)`, with `γ = cayleyChart J y`;
* `skewAddHerm`: the linear equivalence from pairs of real matrices to complex matrices; its inverse
  sends `X` to the coordinates of the hermitian matrix `X + Xᴴ` and of the skew-hermitian matrix
  `(X - Xᴴ) / 2`.

## Relation to the literature

Known result: the invariant measure `dY / dT` on tuples of vectors with a given Gram matrix. Source:
C. L. Siegel, Über die analytische Theorie der quadratischen Formen, Ann. of Math. 36 (1935).


### `instance : (volume (α`

 The Haar measure of `U J` is invariant under right translations. 

### `measurePreserving_U_mul`

 Left multiplication by an element of the unitary group `U J` preserves Lebesgue measure on
tuples of vectors. 

### `ae_isUnit_add_one`

 Almost every element `g` of `U(J)`, for its Haar measure, has no eigenvalue `-1`. 

### `IsGramSection`

 The map `σ` is a differentiable section of the Gram map over the open set `V` of real
coordinates `t` of hermitian matrices, and its values there are bases. 

### `IsGramSection.isOpen`

 The set `V` is open. 

### `IsGramSection.measurable`

 The map `σ` is measurable on the whole space. 

### `IsGramSection.differentiableAt`

 The map `σ` is differentiable on `V`. 

### `IsGramSection.gramCoords_eq`

 For `t` in `V` the Gram matrix of `σ t` has the coordinates `t`. 

### `IsGramSection.isUnit`

 For `t` in `V` the matrix `σ t` is invertible. 

### `exists_isGramSection`

 There are an open set `V` of coordinates of Gram matrices, containing those of `1ᴴ * J * 1 = J`,
and a differentiable section of the Gram map over `V` through the standard basis `1`. 

### `skewCoords_fderiv_gram`

 The identity `gramCoords J (σ t) = t` of a section, differentiated at `t ∈ V` in the
direction `v`. 

### `mono`

 A section of the Gram map over `V` restricts to a section over each open subset of `V`. 

### `abs_det_skewAddHerm_mulLeft_comp`

 Multiplying the values of a linear map `D` on the left by `P` multiplies its Jacobian, read in
the coordinates `skewAddHerm.symm`, by `‖det P‖ ^ (2 r)`, where `r` is the size of the matrices. 

### `abs_det_skewAddHerm_symm_comp`

 Let `σ` be a differentiable section of the Gram map over the open set `V` (`IsGramSection`), and
let `γ = cayleyChart J`, with `cayleyDenom J y` invertible. At `t ∈ V`, let
`T(t', s) = σᴴ (γᴴ J dγ_y s) σ + σᴴ J dσ_t t'`. In coordinates via `skewAddHerm.symm`
(`Z ↦ (Z + Zᴴ, (Z - Zᴴ)/2)`), `|det T| = ‖det σ t‖ ^ (2 card ι) · cayleyDensity J y`. 

### `exists_hasFDerivAt_cayleyChart_mul`

 Let `J` be a hermitian involution, `σ` a section of the Gram map over `V`, `t ∈ V`, and `y` real
with `det (cayleyDenom J y) ≠ 0`. Then the map `(t, y) ↦ γ(y) σ(t)`, with `γ = cayleyChart J` the
Cayley chart, is differentiable at `(t, y)`. The absolute value of its Jacobian is the density
`New.cayleyDensity J y`, which is the absolute Jacobian of `J γ⁻¹ dγ`. The Jacobian is read in the
real coordinates `skewAddHerm.symm`, which send a complex matrix `Z` to the coordinates of the
hermitian matrix `Z + Zᴴ` and of the skew-hermitian matrix `(Z - Zᴴ) / 2`. 

### `exists_mul_eq`

 Let `J` be a hermitian involution, and let `σ` be a differentiable section over the open set `V`
of the Gram map `gramCoords J` (the real coordinates of `Yᴴ J Y`), whose values `σ t` are
invertible. Then every complex matrix `Y` with `t = gramCoords J Y` in `V` is `γ σ(t)` for some `γ`
in `U(J)`. 

### `ae_isUnit_add`

 Let `J` be a hermitian involution (`Jᴴ = J`, `J² = 1`). Let `σ` be a section of the Gram map
`gramCoords J` over the open set `V`: a differentiable map with invertible values, where
`gramCoords J Y` is the real coordinates, in the sense of `hermOfReal`, of `Yᴴ J Y`. For
Lebesgue-almost every complex matrix `Y` with `t = gramCoords J Y` in `V`, written `Y = γ σ(t)` with
`γ` in `U(J)`, the matrix `Y + σ(t) = (γ + 1) σ(t)` is invertible; that is, `γ` has no eigenvalue
`-1`. 

### `injOn_cayleyChart_mul`

 On `V` times the domain of the Cayley chart the map `(t, y) ↦ γ(y) σ(t)`, with `γ` the Cayley
chart, is injective. 

### `preimage_gramCoords_ae_eq_image`

 Up to a null set, the matrices `Y` with `gramCoords J Y` in `V` are the products `γ(y) σ(t)`
with `t` in `V` and `y` in the domain of the Cayley chart `γ`. 

### `lintegral_eq_cayleyChart_mul`

 The polar formula in the Cayley chart. Let `J` be a hermitian involution, `gramCoords J Y` the
real coordinates of the Gram matrix `Yᴴ J Y`, and `σ` a section of the Gram map over `V`. For
measurable `K ≥ 0`, the integral of `K` over all of `gramCoords J ⁻¹' V` equals `2 ^ (-r)`, with
`r = card ι`, times the integral of `cayleyDensity J y * K (cayleyChart J y * σ t)` over `t ∈ V` and
`y` with `det (cayleyDenom J y) ≠ 0`. Here `cayleyDensity J y` is the Jacobian of the Cayley chart
`γ = cayleyChart J`. 

### `lintegral_eq`

 The polar formula. Let `J` be a hermitian involution, let `σ` be a differentiable section with
invertible values over the open set `V` of the Gram map `gramCoords J` (the real coordinates, in the
sense of `hermOfReal`, of `Yᴴ J Y`), and let `K ≥ 0` be measurable. On the matrices `Y = γ σ(t)`
with `γ` in `U(J)` and `t = gramCoords J Y` in `V`, Lebesgue measure is
`dY = (vol U(r) / 2 ^ r) dγ dt`, where `r` is the size of the matrices, `vol U(r) = New.volU r` and
`dγ` is the compact dual Haar measure `New.haarU J`, the `volume` of `U J`; that is,
`∫ Y in gramCoords J ⁻¹' V, K Y` equals that constant times `∫ t in V, ∫ γ, K (γ σ(t))`. 
