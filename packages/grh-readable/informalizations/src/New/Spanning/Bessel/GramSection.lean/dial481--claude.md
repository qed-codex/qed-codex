---
{
  "module": "src/New/Spanning/Bessel/GramSection.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Bessel/GramSection.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Bessel/GramSection.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The Gram section γ_Z of the frame Gram matrix map on the unitary group G₁

For `γ` in the unitary group `New.Shape.G₁`, let `Z(γ) = New.realFrameGram γ = Fᴴ J₁ γ F` be the
matrix of products of the frame `F = (e₁, …, e_ϱ, z)` with its translate by `γ`. Let
`Ω = New.Shape.openCell` be the open set of invertible `Z` for which `ξ(Z) = invCorner Z`, the last
diagonal entry of `Z⁻¹`, has absolute value less than `1`. The file writes down an explicit matrix
`γ_Z` for `Z ∈ Ω` and proves that it is real differentiable with polynomial bounds.

## Main definitions and results

* `New.RealPlace.sectionMatrix`: a matrix in two variables `Z`, `W`, equal to `γ_Z` at `W = Zᴴ`.
* `New.RealPlace.differentiableAt_sectionMatrix`,
  `New.RealPlace.norm_sectionMatrix_le_and_norm_fderiv_le`: the matrix is real differentiable in
  `Z`, with polynomial bounds for it and its derivative.
  `New.RealPlace.IsBoundedInCell.norm_sectionMatrix_le` asks for bounds at the point `Z` only.
* `New.RealPlace.gramSection`: on `Ω` the matrix is an isometry of `J₁`
  (`New.RealPlace.sectionMatrix_isometry`), so it is the matrix of an
  element `γ_Z` of `G₁` (`New.RealPlace.coe_gramSection`).
* `New.RealPlace.measurable_gramSection`: the section is measurable.
* `New.RealPlace.realFrameGram_gramSection`: `Z(γ_Z) = Z` for `Z ∈ Ω`.
* `New.RealPlace.exists_eq_mul_gramSection_mul`: by Witt's theorem, `Z(γ) = Z ∈ Ω` determines `γ` up
  to factors `unipotentOf q * embedH k`, which fix the frame, on both sides.

Notions from other files:
* `New.Shape.BesselIndex`: the index set of the basis `e₁, …, e_ϱ`, `x_k` (`k ∈ κ`), `z`,
  `e*₁, …, e*_ϱ`; `k₀ = New.Shape.k₀` is a distinguished index in `κ`.
* `New.Shape.J₁`: the Gram matrix of the hermitian form defining `G₁`, with `ϱ` hyperbolic pairs
  `e_a, e*_a`, the identity on the span `X₀` of the `x_k` (`k ∈ κ`), and `h(z, z) = -1`.
* `New.Shape.frameCols`, `New.Shape.dualFrameCols`: the matrices `F` and `F'` whose columns are the
  basis vectors `(e₁, …, e_ϱ, z)` and `(e*₁, …, e*_ϱ, x_{k₀})`.
* `New.Shape.FrameMatrix`: the complex `(ϱ+1) × (ϱ+1)` matrices; `New.Shape.top` is the last index.



## The matrix γ_Z on Ω and bounds for it and its derivative

The matrices have a second argument `W`, and `γ_Z` is the value at `W = Zᴴ`. Norms of matrices are
`L²` operator norms.


### `invCorner`

 For a (ϱ+1)×(ϱ+1) complex matrix Z, the last diagonal entry ξ(Z) of its inverse. 

### `_root_.New.Shape.openCell`

 The set Ω of invertible (ϱ+1)×(ϱ+1) complex matrices whose inverse has last diagonal entry of
absolute value less than 1. 

### `oneSubNormSqInvCorner`

 For a (ϱ+1)×(ϱ+1) complex matrix Z, the real number ν(Z)² = 1 − |ξ|², ξ the last diagonal
entry of Z⁻¹. 

### `IsBoundedInCell`

 Z lies in Ω (`New.Shape.openCell`), and ‖Z⁻¹‖, ‖Z‖ (operator norms) and 1/ν(Z) are at most P,
where ν(Z)² = 1 − |ξ|², ξ the last diagonal entry of Z⁻¹. 

### `IsBoundedInCell.mem_openCell`

 The matrix lies in Ω. 

### `IsBoundedInCell.norm_inv_le`

 The inverse has operator norm at most P. 

### `IsBoundedInCell.norm_le`

 The matrix has operator norm at most P. 

### `IsBoundedInCell.inv_sqrt_oneSubNormSqInvCorner_le`

 The number 1/ν(Z) is at most P. 

### `diagLast`

 For a complex number x, the (ϱ+1)×(ϱ+1) diagonal matrix diag(1, …, 1, x). 

### `sectionCoeff`

 For matrices Z and W, the matrix Y(Z, W) with last row (0, …, 0, −1) and other entries
−(W⁻¹)_{a,last}(Z⁻¹)_{last,b}, halved unless b is last. For W = Zᴴ its columns are the coefficients
of the frame F = (e₁, …, e_ϱ, z) in a family F^∨(Z) that is dual to F and has the Gram matrix −ζᴴζ,
with ζ the last row of Z⁻¹. 

### `sectionFrame`

 The matrix (F·Y + F'·diag(1, …, 1, s))·Z, with F the frame, F' = (e*₁, …, e*_ϱ, x_{k₀}),
Y = `New.RealPlace.sectionCoeff Z W` and s = (1 − ξ(Z) ξ(W))^{1/2}, ξ = `invCorner`. For Z in Ω
and W = Zᴴ the first factor is the family F^∨(Z) dual to F, and the columns of F^∨(Z)·Z are the
images of the frame under γ_Z. The rows are indexed by the basis e_a, x_i (i in κ), z, e*_a
(`BesselIndex`), and k₀ = `𝔰.k₀` is the distinguished index in κ. 

### `sectionMatrix`

 The matrix 1 − FFᴴ − F'F'ᴴ + SFᴴ + (FW⁻¹ − S·Y(W, Z))·diag(1, …, 1, s⁻¹)·F'ᴴ, with F the
frame, F' = (e*₁, …, e*_ϱ, x_{k₀}), S = `New.RealPlace.sectionFrame Z W`,
Y = `New.RealPlace.sectionCoeff` and s = (1 − ξ(Z) ξ(W))^{1/2}, ξ = `invCorner`. For Z in Ω and
W = Zᴴ it is the matrix of γ_Z, and s = ν(Z). In that case it sends F to F^∨(Z)·Z and F^∨(Zᴴ) to
F·(Zᴴ)⁻¹, and it fixes the x_i with i ≠ k₀; here F^∨(Z) = F·Y(Z, Zᴴ) + F'·diag(1, …, 1, s) is dual
to the frame. Rows and columns are indexed by the basis e_a, x_i (i in κ), z, e*_a (`BesselIndex`),
and k₀ = `𝔰.k₀` is the distinguished index in κ. 

 ### The open set `Ω` 

### `gramDiscReal_eq_norm_det_sq_mul`

 For invertible `Z`, the number `𝗀(Z) = |det Z|² - |D_ϱ|²` (`gramDiscReal`, with `D_ϱ` the
leading minor of order `ϱ`) equals `|det Z|² ν(Z)²`. 

### `mem_openCell_iff`

 The set Ω (`openCell`: `Z` invertible and the last diagonal entry of `Z⁻¹` of absolute value
less than `1`) is the set where `𝗀(Z) = |det Z|² - |D_ϱ|²` (`gramDiscReal`) is positive, with `D_ϱ`
the leading minor of order `ϱ`. 

### `continuous_gramDiscReal`

 The number `𝗀(Z) = |det Z|² - |D_ϱ|²` (`gramDiscReal`, with `D_ϱ` the leading minor of order
`ϱ`) is a continuous function of `Z`. 

### `sqrt_eq_sqrt_oneSubNormSqInvCorner`

 For `Z` in Ω (`openCell`) the complex root `(1 - ξ(Z) ξ(Zᴴ)) ^ (1 / 2)` is the real square root
`ν(Z)` of `1 - |ξ(Z)|²`, where `ξ(Z) = invCorner Z` is the last diagonal entry of `Z⁻¹`. 

 ### Differentiability 

### `one_sub_invCorner_mul_mem_slitPlane`

 For `Z`, `W` in Ω the number `1 - ξ(Z) ξ(W)` lies in the slit plane. Here `ξ` is `invCorner`,
the last diagonal entry of the inverse. 

### `differentiableAt_sectionMatrix_uncurry`

 The matrix `sectionMatrix Z W` is holomorphic in `(Z, W)` on `Ω × Ω`, where `Ω` is
`𝔰.openCell`. 

### `differentiableAt_sectionMatrix`

 The matrix `sectionMatrix Y Yᴴ` of the section γ_Y (`gramSection`) is a real differentiable
function of `Y` at every point `Z` of Ω (`openCell`). 

 ### Bounds 

### `norm_sectionCoeff_le`

 If `‖Z⁻¹‖ ≤ P` and `‖W⁻¹‖ ≤ P` (operator norms), then `‖sectionCoeff Z W‖ ≤ 2 + 8 P²`. Here
`sectionCoeff Z W` is the matrix with last row `(0, …, 0, -1)` and other entries
`-(W⁻¹)_{a,last} (Z⁻¹)_{last,b}`, halved unless `b` is last. 

### `norm_sqrt_one_sub_invCorner_mul_le`

 For `Z`, `W` in Ω the root `s = (1 - ξ(Z) ξ(W)) ^ (1 / 2)` satisfies `|s| ≤ 2`.
Here `ξ` is `invCorner`, the last diagonal entry of the inverse. 

### `norm_inv_sqrt_one_sub_invCorner_mul_le`

 For `Z`, `W` in Ω, the root `s = (1 - ξ(Z) ξ(W)) ^ (1 / 2)` satisfies `|s⁻¹| ≤ 2 / ν(Z)`. 

### `norm_sectionMatrix_le_pow`

 Let `P ≥ 8`. Let Ω = `𝔰.openCell` be the matrices that are invertible and whose inverse has last
diagonal entry of absolute value below 1. Let `Z` lie in Ω with `‖Z⁻¹‖`, `‖Z‖` and `1 / ν(Z)` at
most `P` (`IsBoundedInCell`). Let `W` lie in Ω with `‖W⁻¹‖ ≤ P`. Then `sectionMatrix Z W` has
operator norm at most `P ^ 12`. 

### `IsBoundedInCell.norm_sectionMatrix_le_pow`

 Let `P ≥ 8` and let `Z` lie in Ω with `‖Z⁻¹‖`, `‖Z‖` and `1 / ν(Z)` at most `P`
(`IsBoundedInCell`). Then the matrix `sectionMatrix Z Zᴴ` of γ_Z has operator norm at most
`P ^ 12`. 

### `norm_fderiv_sectionMatrix_le`

 Let r > 0 and P ≥ 8, and let every y within r of Z lie in Ω with ‖y⁻¹‖, ‖y‖ and 1/ν(y) at most P
(`IsBoundedInCell`). Then the real derivative at Z of the matrix `sectionMatrix Y Yᴴ` of γ_Y has
norm at most 2P¹²/r. 

### `norm_sectionMatrix_le_and_norm_fderiv_le`

 Let `r > 0` and `P ≥ 8`. Suppose every `y` in `ball Z r` satisfies `IsBoundedInCell y P`: `y`
lies in Ω, meaning `y` is invertible and the last diagonal entry ξ(y) of y⁻¹ has modulus < 1, and
‖y⁻¹‖, ‖y‖ and 1/ν(y) are at most P. Then `sectionMatrix Z Zᴴ`, the matrix of the section γ_Z ∈ G₁,
has operator norm at most P¹². The real derivative of `Y ↦ sectionMatrix Y Yᴴ` at `Z` has norm at
most 2P¹²/r. 

### `IsBoundedInCell.isUnit_det_and_norm_inv_le`

 Let `T ≥ 4` and let `Z` lie in Ω with `‖Z⁻¹‖`, `‖Z‖` and `1 / ν(Z)` at most `T`
(`IsBoundedInCell`). Then a matrix `Y` within `T ^ (-6)` of `Z` is invertible, `‖Y⁻¹‖ ≤ 2 T`, and
`Y⁻¹` is within `2 T ^ (-4)` of `Z⁻¹`. 

### `IsBoundedInCell.inv_sq_le_oneSubNormSqInvCorner`

 If `T > 0` and `Z` lies in Ω with `‖Z⁻¹‖`, `‖Z‖` and `1 / ν(Z)` at most `T` (`IsBoundedInCell`),
then `ν(Z)² = oneSubNormSqInvCorner Z` is at least `T ^ (-2)`. 

### `IsBoundedInCell.mul_oneSubNormSqInvCorner_le`

 Write `ν(Z)² = 1 - |ξ(Z)|²` (`oneSubNormSqInvCorner`), with `ξ(Z)` the last diagonal entry of
`Z⁻¹`. Let `T ≥ 4` and let `Z` lie in Ω with `‖Z⁻¹‖`, `‖Z‖` and `1 / ν(Z)` at most `T`
(`IsBoundedInCell`). Then `(1 - 8 / T ^ 2) ν(Z)² ≤ ν(Y)²` for `Y` within `T ^ (-6)` of `Z`. 

### `IsBoundedInCell.of_mem_ball`

 Let `T ≥ 4` and let `Z` lie in Ω with `‖Z⁻¹‖`, `‖Z‖` and `1 / ν(Z)` at most `T`
(`IsBoundedInCell`). Then every `Y` within `T ^ (-6)` of `Z` lies in Ω and satisfies the same bounds
with `2 T` in place of `T`. 

### `IsBoundedInCell.gramDiscReal_div_two_le`

 Let `Z` lie in Ω with `‖Z⁻¹‖`, `‖Z‖` and `1 / ν(Z)` at most `T` (`IsBoundedInCell`), where
`ν(Z)² = 1 - |ξ(Z)|²` and `ξ(Z)` is the last diagonal entry of `Z⁻¹`. Let `T` be at least `8` and
at least the number `𝔰.n = ϱ + 1` of rows of `Z`. Then `𝗀(Z) / 2 ≤ 𝗀(Y)` for `Y` within `T ^ (-6)`
of `Z`, where `𝗀(Z) = |det Z|² - |D_ϱ|²` (`gramDiscReal`, with `D_ϱ` the leading minor of order `ϱ`)
equals `|det Z|² ν(Z)²` for invertible `Z`. 

### `IsBoundedInCell.norm_sectionMatrix_le`

 Let `T ≥ 4` and let `𝔰` be a shape (ϱ, κ, k₀). Let `Z` be a complex `(ϱ+1) × (ϱ+1)` matrix in Ω,
with `‖Z⁻¹‖`, `‖Z‖` and `1 / ν(Z)` at most `T` (`IsBoundedInCell`). Then `sectionMatrix Z Zᴴ` has
operator norm at most `T ^ 18`, and its real derivative in `Z` has norm at most `T ^ 25`. 

 ## The Gram section and double cosets over the open cell 

### `sectionMatrix_mul_frameCols`

 The matrix `sectionMatrix Z Zᴴ` sends the frame `F = (e₁, …, e_ϱ, z)` to the columns of
`sectionFrame Z Zᴴ = (F Y + F' diag(1, …, 1, s)) Z`. Here `F' = (e*₁, …, e*_ϱ, x_{k₀})`,
`Y = sectionCoeff Z Zᴴ` and `s = (1 - ξ(Z) ξ(Zᴴ)) ^ (1 / 2)` with `ξ = invCorner`. 

### `conjTranspose_inclMatrix_mul_mul_inclMatrix`

 For index maps `u`, `v`, multiplying `M` by the matrices of basis vectors `(inclMatrix ℂ u)ᴴ`
on the left and `inclMatrix ℂ v` on the right selects the rows `u` and the columns `v` of `M`. 

### `frameCols_gram_frameCols`

 The Gram matrix of the frame `F = (e₁, …, e_ϱ, z)` for the form `𝔰.J₁` is
`diagLast 0 - 1 = diag(0, …, 0, -1)`. 

### `frameCols_gram_dualFrameCols`

 The products for the form `𝔰.J₁` of the columns of `𝔰.frameCols` = (e₁, …, e_ϱ, z) with those of
`𝔰.dualFrameCols` = (e*₁, …, e*_ϱ, x_{k₀}) form the matrix `diagLast 0 = diag(1, …, 1, 0)`, that is,
`𝔰.frameColsᴴ * 𝔰.J₁ * 𝔰.dualFrameCols = diagLast 0`. 

### `frameCols_gram_sectionMatrix`

 Let `Z` be any complex `(ϱ+1) × (ϱ+1)` matrix, not necessarily in the set Ω, and let
`M = sectionMatrix Z Zᴴ`. Then `Fᴴ J₁ M F = Z`. 

### `conjTranspose_actOnCols_mul_mul`

 Let `C` be a matrix with orthonormal columns, its rows indexed by the basis `e_a`, `x_i`, `z`,
`e*_a` (`BesselIndex`). Then `actOnCols C A = 1 - C Cᴴ + C A Cᴴ`, which acts by `A` on the span of
the columns and fixes its orthogonal complement, is compatible with congruence:
`(actOnCols C A)ᴴ * actOnCols C J * actOnCols C A = actOnCols C (Aᴴ J A)`. 

### `sectionMatrix_isometry`

 For `Z ∈ 𝔰.openCell`, the matrix `sectionMatrix Z Zᴴ`, which is the matrix of γ_Z, preserves the
hermitian form with Gram matrix `𝔰.J₁`: `Mᴴ * 𝔰.J₁ * M = 𝔰.J₁`. 

### `gramSection`

 The section `γ_Z`. For `Z ∈ Ω` it is the element of `G₁` whose matrix is `sectionMatrix Z Zᴴ`
(see `New.RealPlace.coe_gramSection`). Off `Ω` it is the identity. 

### `measurable_gramSection`

 The section `Z ↦ γ_Z` (`gramSection`), from the complex `(ϱ+1) × (ϱ+1)` matrices to the unitary
group `G₁` of the form `𝔰.J₁`, is measurable. Here `γ_Z` has the matrix `sectionMatrix Z Zᴴ` for `Z`
in the open set Ω (`openCell`) and is the identity off Ω. 

### `coe_gramSection`

 For `Z` in the open cell Ω (`𝔰.openCell`), the matrix of the section γ_Z = `gramSection Z` ∈ G₁
is the explicit matrix `sectionMatrix Z Zᴴ`. 

### `gramSection_eventuallyEq`

 Near each `Z` in Ω, the matrix of `γ_Y` agrees with `New.RealPlace.sectionMatrix Y Yᴴ`. 

### `realFrameGram_eq_conjTranspose_mul`

 For `γ ∈ G₁`, the matrix `Z(γ) = realFrameGram γ` equals `Fᴴ J₁ γ F`, with `F = 𝔰.frameCols` the
frame (e₁, …, e_ϱ, z) and `J₁ = 𝔰.J₁`. 

### `realFrameGram_gramSection`

 On Ω the map `Z ↦ γ_Z` is a section of `γ ↦ Z(γ) = Fᴴ J₁ γ F` (`realFrameGram`, with `F` the
frame): `Z(γ_Z) = Z`. 

### `conjTranspose_framePair_mul_mul`

 For `γ ∈ G₁` the family `framePair γ = (F | γ F)` of the frame `F` and its image has, for the
form `𝔰.J₁`, the Gram matrix with diagonal blocks `diagLast 0 - 1 = diag(0, …, 0, -1)` and
off-diagonal blocks `Z(γ) = realFrameGram γ` and `Z(γ)ᴴ`. 

### `exists_eq_mul_gramSection_mul`

 Let `γ ∈ G₁` have frame Gram matrix `Z(γ) = Fᴴ J₁ γ F` (`realFrameGram`) equal to `Z ∈ Ω`. Then
`γ = u k γ_Z (u' l)⁻¹`, where `γ_Z = gramSection Z`, `u = unipotentOf q` and `u' = unipotentOf r`.
The elements `k`, `l` lie in the unitary group `U 1` of the identity matrix of size `κ`, which
`embedH` lets act on the span of the `x_i` (`i ∈ κ`). 
