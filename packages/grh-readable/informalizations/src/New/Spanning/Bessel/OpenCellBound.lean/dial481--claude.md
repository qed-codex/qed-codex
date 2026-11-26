---
{
  "module": "src/New/Spanning/Bessel/OpenCellBound.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Bessel/OpenCellBound.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Bessel/OpenCellBound.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Bounds near a point of Ω and the open cell bound for a Bessel system

Write Ω = `New.Shape.openCell`, 𝗀(Z) = |det Z|² − |D_ϱ|² and ν(Z)² = 1 − |ξ|², where ξ is the last
diagonal entry of Z⁻¹. At and near a point `Z` of Ω (so `0 < 𝗀(Z)`) the matrix, its inverse, 𝗀 and ν
obey explicit size bounds. Such bounds on a ball supply the hypothesis of
`New.RealPlace.lintegral_gramSection_integral_le`. For a Bessel system, a family of kernels is then
shown to be an `L²` contraction at each `γ` in `New.Shape.G₁` whose frame Gram matrix lies in Ω,
provided that some `y` and `γ⁻¹ y` both lie in a frame box of large enough size.

## Main definitions and results

* `New.RealPlace.isBoundedInCell_of_inv_le_gramDiscReal`: if `M⁻¹ ≤ 𝗀(Z)` and the entries of `Z` are
  at most `M ^ 2`, a power of `M` bounds the matrix, its inverse and `1 / ν`.
* `New.RealPlace.gramDiscReal_div_two_le_and_isBoundedInCell`: on a small ball about such a `Z` the
  matrix stays in Ω with these bounds, and 𝗀 drops by at most a factor two.
* `New.BesselSystem.exists_isOpenCellBound`: the family of shifted kernels is a contraction from
  `L²(ν)` to `L²(m)`, with `m` a probability measure and `ν` of total mass at most `pairingBoundSq`
  (`New.BesselSystem.IsOpenCellBound`).

Notions from other files:
* `New.RealPlace.gramDiscReal`: 𝗀(Z) = |det Z|² − |D_ϱ|² for a (ϱ+1)×(ϱ+1) complex matrix Z
  (`New.Shape.FrameMatrix`), where D_l (`New.leadingMinor`) is the leading principal minor of order
  l.
* `New.Shape.openCell`: The set of invertible (ϱ+1)×(ϱ+1) complex matrices whose inverse has last
  diagonal entry ξ of absolute value less than 1; `New.RealPlace.oneSubNormSqInvCorner` is
  ν² = 1 − |ξ|².
* `New.RealPlace.gramSection`: For Z in Ω, an element γ_Z of G₁ whose frame Gram matrix
  (`New.realFrameGram`) is Z.
* `New.frameBox`: The set of y in G₁ such that every vector y⁻¹f_a of the moved frame
  (`New.frameVector`) has Euclidean norm at most a given bound.
* `New.besselLength`: For y in G₁, the infimum of ‖sy‖ + 1 over s in the Bessel subgroup S
  (`New.Shape.Form.besselS`).
* `New.BesselSystem 𝔰 B f`: a Bessel function `besselFn .full` on G₁ with values in ℂ^I, its cut
  `besselFn .cut` and their bounds. The real `B ≥ 8 r` (r the rank of G₁) sets the scale of the
  bounds, the natural number `f` the rate of decay, and |I| / `deg` is the constant of Schur's
  bound.

## Relation to the literature

See `New.Spanning.Bessel.FillingData` for related work.



## Sizes at and near a point of Ω

Norms of matrices are `L²` operator norms.


### `l2_opNorm_le_pow_four`

 A complex matrix of size `l ≤ M` with entries of norm at most `M ^ 2` has operator norm at most
`M ^ 4`. 

### `isBoundedInCell_of_inv_le_gramDiscReal`

 Sizes at a point of Ω. Let `Z` be a complex matrix of size `n = ϱ + 1 ≤ M` with entries of norm
at most `M ^ 2` and with `M⁻¹ ≤ 𝗀(Z)`. Then `Z` lies in Ω, and every `T ≥ M ^ (8 n)` bounds `‖Z⁻¹‖`,
`‖Z‖` and `1 / ν(Z)` (`IsBoundedInCell`). 

### `gramDiscReal_div_two_le_and_isBoundedInCell`

 Sizes near a point of Ω. Let `Z` be a complex matrix of size `n = ϱ + 1` and `M ≥ 8 n`, with
`M⁻¹ ≤ 𝗀(Z)` and entries of `Z` of norm at most `M ^ 2`; let `P ≥ M ^ (9 n)`. Every `Z'` at operator
distance less than `(P ^ 6)⁻¹` from `Z` has `𝗀(Z) / 2 ≤ 𝗀(Z')` and satisfies `IsBoundedInCell Z' P`:
it lies in Ω, and `‖Z'⁻¹‖`, `‖Z'‖`, `1 / ν(Z')` are at most `P`. 


## The open cell bound for a Bessel system

Let `γ` in `New.Shape.G₁` have its frame Gram matrix in the open cell, and let `X` be a Bessel
system (`New.BesselSystem`). For shifts `t` in `besselFixer`, the products of the values of
`X.besselFn` at `γ t y` and at `t y` form a kernel, which is integrated against `φ y` over a compact
set. The mean of its squared norm over the shifts is at most `∫ ‖φ‖² dν` for a finite measure `ν` of
total mass at most `pairingBoundSq`. In this part the letter `Ω` in the code denotes a subset of
`besselU0`.


### `New.RealPlace.sectionCoeff_castSucc_castSucc`

 The matrix `sectionCoeff Zᴴ Z` is a coefficient matrix in the formula `sectionMatrix Z Zᴴ` for
the section `γ_Z`. Outside the last row and column its entry at `(i, a)` is
`-(Z⁻¹)_{i,last} (Zᴴ⁻¹)_{last,a} / 2`. 

### `New.RealPlace.sectionCoeff_last_castSucc`

 The last row of `sectionCoeff Zᴴ Z`, a coefficient matrix in the formula `sectionMatrix Z Zᴴ`
for the section `γ_Z`, vanishes outside the last column. 

### `New.inv_apply_eStar_eq_sum_frameVector`

 Let `Z` lie in the open cell `𝔰.openCell`: `Z` is invertible and the last diagonal entry of
`Z⁻¹` has absolute value less than 1. Let `γ_Z = gramSection Z`, an element of the unitary group
`G₁` of the hermitian form `h`, whose frame Gram matrix (the matrix of the products
`h(f_j, γ_Z f_l)`) is `Z`. Let `w` be in `besselU`, the group of block upper unitriangular elements
of `G₁`. Let `Z' = realFrameGram (w γ_Z)`, the matrix of the products `h(f_j, w γ_Z f_l)`. For `z`
in `G₁`, the column of `z⁻¹` at the basis vector `e*_a` (dual to `f_a = e_a`) is a combination of
the moved frames at `w γ_Z z` and at `z`, with coefficients built from the entries of `Z'ᴴ⁻¹`, `Z⁻¹`
and `Zᴴ⁻¹`. Here `BesselIndex` indexes the basis `e_a`, `x_j` (`j` in `κ`), `z₀`, `e*_a`, the frame
is `(f_i) = (e₁, …, e_ϱ, z₀)`, and `frameVector y i = y⁻¹ f_i`. 

### `New.norm_le_of_besselLength_gramSection_mul_le`

 A bound for `‖z‖` from the length of `γ_Z z`. Let `n = 𝔰.n = ϱ + 1`, `8 n ≤ M` and
`M ^ (9 n) ≤ R`. Let `M⁻¹ ≤ gramDiscReal Z`, the number |det Z|² − |D_ϱ|² with D_ϱ the leading
principal minor of order ϱ, so that `Z` lies in the open cell, and let `‖Z⁻¹‖ ≤ R`. Suppose that the
vectors `z⁻¹ f_a` of the moved frame have norm at most `M` (`frameBox`), where the frame
`(f_a) = (e₁, …, e_ϱ, z₀)` consists of ϱ + 1 fixed basis vectors of the space on which `G₁` acts,
and that `besselLength (γ_Z z)`, the infimum of `‖s γ_Z z‖ + 1` over `s` in the Bessel subgroup, is
at most `M`. Then the operator norm of `z` is at most `R ^ 5`. 

### `New.sum_enorm_sq_integral_mul_star`

 Let `W` be a Bessel function on the unitary group `G₁` with values in `ℂ^I`. It is bounded and
measurable. Under left translation it transforms in two ways: by the character
`n ↦ wave (simpleRootSum n)` of the block unitriangular subgroup `besselU`, where `simpleRootSum n`
is the sum of the entries of `n` just above the diagonal on the frame; and by the unitary
representation `rep` of the unitary group `U(κ)` of the positive definite middle part. Let `ψ` be
integrable and let `s, t` lie in the Bessel subgroup `besselS`, which these two groups generate. The
squared Hilbert–Schmidt norm of the integral of `ψ y * W (s * g * y) ⊗ conj (W (t * y))` does not
depend on `s` and `t`. It equals the sum of the squared norms of the columns at `s = t = 1`. 

### `New.gramDiscReal_le_pow`

 Let `0 < 𝗀(Z)`, where 𝗀(Z) = |det Z|² − |D_ϱ|² is `gramDiscReal`, D_ϱ the leading principal
minor of order ϱ. If the entries of `Z` have norm at most `ρ ^ 2` and `n ≤ ρ`, where `n = ϱ + 1` is
the size of `Z`, then `𝗀(Z) ≤ ρ ^ (8 n)`. 

### `New.inv_pow_div_gramDiscReal_le`

 If `0 < 𝗀(Z)` and `1 ≤ ρ`, then `(ρ ^ N / 𝗀(Z))⁻¹ ≤ 𝗀(Z)`; here 𝗀(Z) is `gramDiscReal Z`, the
number |det Z|² − |D_ϱ|² with D_ϱ the leading principal minor of order ϱ. 

### `New.le_pow_div_gramDiscReal`

 Let `0 < 𝗀(Z)`, where 𝗀(Z) = |det Z|² − |D_ϱ|² is `gramDiscReal`, D_ϱ the leading principal
minor of order ϱ. Let `n ≤ ρ` and `1 ≤ ρ` with `n = ϱ + 1`, and let the entries of `Z` have norm at
most `ρ ^ 2`. Then `ρ ≤ ρ ^ (9 n) / 𝗀(Z)`. 

### `New.BesselSystem.lintegral_indicator_mul_enorm_sq_le`

 Let `W = X.besselFn .full` be the Bessel function of a Bessel system `X` before its cut, with
values in `ℂ^I`, `I = X.Index`; the scale `B` and the rate of decay `f` of `X` do not enter the
bound. Let `A` be a measurable set of elements of operator norm at most `R`, `1 ≤ R`, in `G₁`, the
unitary group of the form with middle block `middleGram 1 = diag(1, …, 1, -1)`. Suppose that for
every `y` the set of `u` in the frame-fixing unipotent subgroup `besselU0` with `u y ∈ A` has Haar
measure (`besselHaar₀`) at most `K`. Then `∫_A ‖W‖ ^ 2 ≤ K (2 R²) ^ (2 n²) |I|`, where
`n = 𝔰.n = ϱ + 1`. 

### `New.isL2Contraction_of_columns`

 Let `W` be a continuous Bessel function on the unitary group `G₁`. Let `A` be compact, `g`
measurable, and `s` and all `t x` in the Bessel subgroup `besselS`. Suppose that
`∫_S ‖∫ β y • W (g x * y)‖² dμ(x) ≤ K ∫ ‖β‖²` for all measurable integrable weights `β` that vanish
off `A`. Then the kernel `W (s * g x * y) ⊗ conj (W (t x * y))`, integrated against volume on `A`,
has operator norm at most one (`IsL2Contraction`) from `L²` of `(μ S)⁻¹ K` times the measure of
density `‖W‖²` on `A` to `L²` of `μ` conditioned on `S`. 

### `New.Shape.FixerFactors`

 The pairs `(h, v)` with `h` in the unitary group `U(κ)` of the positive definite middle part and
`v` in the frame-fixing unipotent subgroup `besselU0` of `G₁`. 

### `New.BesselSystem.isL2Contraction_gramSection`

 Schur's bound at the section `γ_Z = gramSection Z`, in operator form, for the uncut function
`W = X.besselFn .full` of a Bessel system `X` with scale `B`. For `P ≥ B ^ 5` the field
`X.hasSchurBound` gives `HasSchurBound` with the two constants `P` and `D = |I| / X.deg`: `W` and
its right derivatives `V` of each order `l ≤ 2 n²` are Bessel functions, and `φ ↦ ∫ φ(y) V(g y) dy`
has squared norm at most `P ^ (2 l) D` as a map from `L²(G₁)` to functions of `g` in
`L²(besselU∖G₁)` (`SchurLe`). Here `n = ϱ + 1` and `I = X.Index`.

Let `8 r ≤ P` and `B ^ 5 ≤ P`, where `r` is the size of the matrices in `G₁`, and let `0 < c`. On
the ball of radius `(P ^ 6)⁻¹` about `Z`, let `c ≤ gramDiscReal Y` and `IsBoundedInCell Y P` hold.
Let `A` be a compact set of norm at most `P ^ 20` that contains a subset `Ω` of the frame-fixing
unipotent subgroup `besselU0`, and let `s` and all `t x` lie in the Bessel subgroup. Let `μ` be
`openCellConst · c ^ (|κ| - 1)` times Haar measure (`fixerMeasure`) on the pairs `x = (h, v)` in
`U(κ) × besselU0` (`FixerFactors`). Let `K = P ^ (2000 n²) D`.

For `x` drawn from `m`, which is `μ` conditioned on `v ∈ Ω`, put `k_(i,j)(x, y) = W_i (s γ_Z (v h)⁻¹
y) · conj (W_j (t x * y))`. Then `IsL2Contraction` says that, for bounded measurable `φ`, the mean
over `m` of `∑_(i,j) |∫_A φ(y) k_(i,j)(x, y) dy|²` is at most `∫ |φ|²` with respect to
`(μ (U(κ) × Ω))⁻¹ K` times the measure of density `‖W‖²` on `A`. 

### `New.scale_mul_le_pow`

 For `1 ≤ M`, `M₀ = M ^ (9 n)` and `P = (M₀ ^ 5) ^ n`, the product `P ^ (2000 n²) · M₀ ^
5 · (M · P ^ 20 · P ^ 20) ^ (2 n²)` equals `M ^ (93600 n⁴ + 2 n² + 45 n)`, hence is at most
`M ^ (10⁵ n⁴)`. 

### `New.toReal_inv_mul_mul_le`

 Let `a, b, p ≥ 0` and `c, δ > 0` be real, `d` natural. If `m ≤ a ω b d` in `ℝ≥0∞` with `ω`
finite and nonzero, then `ω` cancels: `(c ω)⁻¹ · (p d / δ) · m ≤ p a b d² / (δ c)` as reals. 

### `New.norm_inv_mul_le_of_besselLength_le`

 Let `8 n ≤ M` and `M ^ (9 n) ≤ R`, where `n = 𝔰.n = ϱ + 1`. Let `M⁻¹ ≤ gramDiscReal Z`, the
number |det Z|² − |D_ϱ|² with D_ϱ the leading principal minor of order ϱ, so that `Z` lies in the
open cell. Let `‖Z⁻¹‖ ≤ R`, and let `γ_Z = gramSection Z`, an element of the unitary group `G₁` with
frame Gram matrix `Z`. Let `s` lie in the Bessel subgroup `besselS`, `v` in the frame-fixing
unipotent group `besselU0` and `h` in `U(κ)`, embedded in `G₁` by `embedH`. Suppose that the moved
frame vectors `z⁻¹ f_a` have norm at most `M` (`frameBox`). If also
`besselLength (s γ_Z (v h)⁻¹ z) ≤ M`, then the operator norm of `v⁻¹ z` is at most `R ^ 5`. 

### `New.exists_mul_eq_mul_gramSection_mul`

 Let `realFrameGram γ`, the matrix of the products `h(f_j, γ f_l)` of the frame
`(f_i) = (e₁, …, e_ϱ, z)` with its translate by `γ`, lie in the open cell `𝔰.openCell`. This means
it is invertible and its inverse has last diagonal entry of absolute value less than 1. Let
`γ_Z = gramSection (realFrameGram γ)` be its section. Then there are `s` in the Bessel subgroup
`besselS` and a measurable map `t`. The map `t` goes from `FixerFactors` (pairs `(h, v)` in
`U(κ) × besselU0`) into the fixer `besselFixer`, the elements fixing each frame vector. They satisfy
`γ t(h, v) = s γ_Z (v h)⁻¹` for all `h` and `v`. 

### `New.BesselSystem.IsOpenCellBound`

 The conclusion of the open cell bound at `γ` in `G₁` and scale `ρ`, for the uncut function
`W = X.besselFn .full` of a Bessel system `X`. The shifts `t x`, with `x` drawn from `m`, fix the
frame, and the kernels `W (γ t z) ⊗ conj (W (t z))` on the set `A` are bounded on average by the
measure `ν`. Its mass is at most `pairingBoundSq`, the number
`(ρ ^ (9 n) / 𝗀) ^ (10⁵ n⁴) |I|² / (X.deg · openCellConst · (𝗀 / 2) ^ (k - 1))` with
`𝗀 = gramDiscReal (realFrameGram γ)`, `n = ϱ + 1`, `k = |κ|` and `I = X.Index`. 

### `New.BesselSystem.IsOpenCellBound.isCompact`

 The domain `A` is compact. 

### `New.BesselSystem.IsOpenCellBound.measurable`

 The shift is a measurable map. 

### `New.BesselSystem.IsOpenCellBound.mem_besselFixer`

 Every shift lies in the fixer of the frame. 

### `New.BesselSystem.IsOpenCellBound.isProbabilityMeasure`

 The shifts are averaged by a probability measure. 

### `New.BesselSystem.IsOpenCellBound.isL2Contraction`

 The mean over `m` of the squared Hilbert–Schmidt norm of
  `∫_A φ z • W (γ t z) ⊗ conj (W (t z))` is at most `∫ ‖φ‖ ^ 2 dν`, for bounded measurable `φ`. 

### `New.BesselSystem.IsOpenCellBound.isFiniteMeasure`

 The bounding measure is finite. 

### `New.BesselSystem.IsOpenCellBound.measureReal_univ_le`

 The total mass of the bounding measure is at most `pairingBoundSq`. 

### `New.BesselSystem.IsOpenCellBound.ae_mem_of_besselLength_le`

 For almost every shift, `A` contains every `z` in `frameBox ρ` such that `γ t z` has
  `besselLength` at most `ρ`. 

### `New.BesselSystem.IsKernelBound`

 A mean `L²` bound for the kernels `W (g x * z) ⊗ conj (W (t x * z))`, where
`W = X.besselFn .full` is the uncut function of a Bessel system `X`, `x` is drawn from `m` and `z`
ranges over `A`. The bounding measure `ν` has mass at most `C`, and `A` captures the points of
Bessel length at most `M`. 

### `New.BesselSystem.IsKernelBound.isCompact`

 The domain `A` is compact. 

### `New.BesselSystem.IsKernelBound.isL2Contraction`

 The mean over `m` of the squared Hilbert–Schmidt norm of
  `∫_A φ z • W (g x * z) ⊗ conj (W (t x * z))` is at most `∫ ‖φ‖ ^ 2 dν`, for bounded measurable
  `φ`. 

### `New.BesselSystem.IsKernelBound.isProbabilityMeasure`

 The parameters are averaged by a probability measure. 

### `New.BesselSystem.IsKernelBound.isFiniteMeasure`

 The bounding measure is finite. 

### `New.BesselSystem.IsKernelBound.measureReal_univ_le`

 The total mass of the bounding measure is at most `C`. 

### `New.BesselSystem.IsKernelBound.ae_mem_of_besselLength_le`

 For almost every `x`, `A` contains every `z` in `frameBox M` such that `g x * z` has
  `besselLength` at most `M`. 

### `New.BesselSystem.exists_isKernelBound_gramSection`

 The open cell bound at the section `γ_Z = gramSection Z`, for the uncut function
`W = X.besselFn .full` of a Bessel system `X` with scale `B`. Here `n = ϱ + 1` and `I = X.Index`.

Let `B ≤ M` and `M⁻¹ ≤ gramDiscReal Z = |det Z|² − |D_ϱ|²`, D_ϱ the leading principal minor of order
ϱ, let the entries of `Z` have norm at most `M ^ 2`, and let `s` and all `t x` lie in the Bessel
subgroup `besselS`. For `x = (h, v)` in `U(κ) × besselU0` (`FixerFactors`) put
`g x = s γ_Z (v h)⁻¹`. There are (`IsKernelBound`) a compact set `A`, a probability measure `m` and
a finite measure `ν` such that the kernel `W (g x * z) ⊗ conj (W (t x * z))`, integrated against
volume on `A`, has norm at most one from `L²(ν)` to `L²(m)` (`IsL2Contraction`). The mass of `ν` is
at most `M ^ (10⁵ n⁴) |I|² / (X.deg · openCellConst · (gramDiscReal Z / 2) ^ (k - 1))`, where
`k = |κ|` and `openCellConst` is vol U(k) · (2π^k/(k−1)!) / vol U(r), `r` the rank of `G₁`. Almost
surely `A` contains every `z` with all `‖z⁻¹ f_a‖ ≤ M` and `besselLength (g x * z) ≤ M`. 

### `New.BesselSystem.exists_isOpenCellBound`

 The open cell bound, for the uncut function `W = X.besselFn .full` of a Bessel system `X` of
scale `B`. Let `Z = realFrameGram γ`, the matrix of products of the frame `f_a` with its translate
by `γ`, have `0 < gramDiscReal Z`. Let `B ≤ ρ`, and let some `y` have all `‖y⁻¹ f_a‖` and
`‖y⁻¹ γ f_a‖` at most `ρ` (`frameBox ρ`). There are (`IsOpenCellBound`) a compact set `A`, a
probability measure `m` on the pairs `FixerFactors`, a measurable map `t` from them into the fixer
`besselFixer` of the frame, and a finite measure `ν` of mass at most `pairingBoundSq`, such that the
mean over `m` of the squared Hilbert–Schmidt norm of `∫_A φ z • W (γ t z) ⊗ conj (W (t z))` is at
most `∫ ‖φ‖ ^ 2 dν` for all bounded measurable `φ`. Almost surely `A` contains every
`z ∈ frameBox ρ` with `besselLength (γ t z) ≤ ρ`. With `𝗀 = gramDiscReal Z`, `n = ϱ + 1`, `k = |κ|`
and `I = X.Index`, the number `pairingBoundSq` is `(ρ ^ (9 n) / 𝗀) ^ (10⁵ n⁴)
|I|² / (X.deg · openCellConst · (𝗀 / 2) ^ (k - 1))`. 
