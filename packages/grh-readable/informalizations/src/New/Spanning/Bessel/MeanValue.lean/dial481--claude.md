---
{
  "module": "src/New/Spanning/Bessel/MeanValue.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Bessel/MeanValue.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Bessel/MeanValue.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The mean value inequality over the Gram matrix of two frames

Let `G₁` be the real unitary group `New.Shape.G₁`, `e = (e₁, …, e_ϱ, z)` its frame, `R°` the fixer
of the frame, the product of the unipotent group `𝖴⁰ = New.Shape.Form.besselU0` and the compact
group `H = U(κ)`, and `γ_Z = New.RealPlace.gramSection Z` the section of the map that sends `γ` to
the matrix `Z` of the products of `e` with `γ e`, over the open set `Ω = New.Shape.openCell` of the
invertible `Z` whose inverse has last diagonal entry of absolute value less than `1`.

On the frames `y = γ e` the fibre measure of the Gram map is compared with Haar measure in
`New.LeGramFibre.mconv_fixerHaar_le`. This file bounds the same fibre measure from below, by `dZ`
times a measure on the frames whose products with `e` form the matrix `Z`. Such a frame is `y' Z`
with `y'` dual to `e`. The first `ϱ` vectors of `y'` are moved by `𝖴⁰`, and the part of the last one
in `X₀ = ℂ ^ κ` runs over a sphere.

One can find the measure on the frames over `Z` by letting both frames vary and dividing two
equalities of fibre measures, the one on pairs of frames, which are tuples of `2 (ϱ + 1)` vectors
with an invertible Gram matrix, by the one on frames. Here a fibre measure enters only through the
relation of being at most it (`New.LeFibreMeasure`); the measure over `Z` is computed directly in
coordinates as a lower bound, and the fibre measure on frames is used as an upper bound.

* `New.RealPlace.lintegral_eq_lintegral_sphereMass_mul_dualFrameOfGram`: Lebesgue measure on the
  tuples dual to the frame, in terms of their Gram matrix and of `R°`.
* `New.RealPlace.leGramFibre_gramSectionMeasure`: the law of `s γ_Z e`, with a density proportional
  to `New.RealPlace.gramDiscReal Z ^ (|κ| - 1)`, is at most the fibre measure.
* `New.RealPlace.lintegral_gramSection_le`: the mean value inequality for the integral of
  `f (s' γ_Z s)` over `s, s'` in `R°` and `Z` in `Ω`.

Notions from other files:
* `fixerHaar 𝔰`: the measure `du dh` on `R°`, with `u = unipotentOf q` for Lebesgue measure `dq` and
  `embedH h` for the Haar probability measure `dh` on `U(κ)`.
* `frameCols`, `dualCols`, `isotropicCols`, `definiteCols`, `freeCols`: the matrices with the
  columns `(e₁, …, e_ϱ, z)`, `e*_b`, `e_b`, `x_i`, and `(e_b, x_i)` respectively.
* `J₁`: the hermitian form on the space with the basis `e_b, x_i, z, e*_b`, which pairs `e_b` with
  `e*_b`, is the identity on `X₀` and is `-1` at `z`.
* `top`, `k`, `k₀`: the last index of the frame, the number `|κ|` and a chosen element of `κ`.
* `embedH h`: the element of `G₁` that acts by `h` on `X₀` and fixes the other basis vectors.
* `hermOfReal t`: the hermitian matrix with the real coordinates `t`.

## Relation to the literature

Part of the bound on the open cell for the Bessel integrals at a real place; see
`New.Spanning.Bessel.FillingData`. For fibre measures of the Gram map compare Siegel, Über die
analytische Theorie der quadratischen Formen, Ann. of Math. 36 (1935).


 ### The measure on the fixer of the frame 

### `lintegral_fixerHaar`

 The integral for `fixerHaar 𝔰`, the measure on the fixer of the frame, is the iterated integral
of the value at `u h`. Here `h` runs over `U(κ)` with Haar probability measure, and `u` runs over
the unipotent group `𝖴⁰` with `besselHaar₀`, the image of Lebesgue measure under `unipotentOf`. 

### `lintegral_fixerHaar_eq_unipotentOf`

 The integral for `fixerHaar 𝔰`, the measure on the fixer of the frame, in coordinates: the
iterated integral of the value at `unipotentOf q * embedH h`, for Lebesgue measure in the parameter
`q` of the unipotent group and Haar measure in `h` on `U(κ)`. 

### `lintegral_fixerHaar_eq_inv`

 The measure `fixerHaar 𝔰`, that is `du dh` on the fixer `R° = 𝖴⁰ H` of the frame, is invariant
under inversion: the integral of `φ` is the iterated integral of `φ ((u h)⁻¹)`. 

 ### Tuples dual to the frame 

### `submatrix_hermOfReal`

 Taking a principal submatrix along an injective map commutes with `hermOfReal`. 

### `splitLast`

 The equivalence of `Fin j ⊕ Unit` with `Fin (j + 1)` that sends `inl b` to `b.castSucc` and the
point of `Unit` to `Fin.last j`. 

### `joinCol_castSucc`

 The matrix `joinCol (splitLast j) p`, made of the `j` columns of `p.1` followed by the vector
`p.2`, agrees with `p.1` in each column before the last. 

### `joinCol_last`

 The matrix `joinCol (splitLast j) p`, made of the `j` columns of `p.1` followed by the vector
`p.2`, has the last column `p.2`. 

### `dualFrameOfGram`

 For a hermitian matrix `T` of size `ϱ + 1` (a `FrameMatrix`), the tuple of the vectors
`e*_b + ½ ∑_a T_{ab} e_a`, `b < ϱ`, and `-z + ∑_a T_{a,last} e_a + √(1 + T_{last,last}) x_{k₀}`,
as the columns of a matrix whose rows are indexed by the basis `e_a, x_i, z, e*_a` (`BesselIndex`).
Here `x_{k₀}` is the chosen basis vector of `X₀`. The tuple is dual to the frame `(e₁, …, e_ϱ, z)`,
and it has the Gram matrix `T` if the number under the root is not negative
(`New.RealPlace.gram_dualFrameOfGram`). 

### `dualFrameOfGram_apply_inl`

 The coefficient of `e_a`, the basis vector with the index `.inl a`, in column `b` of
`dualFrameOfGram T` is the entry `T a.castSucc b` in row `a` of `T`, halved when `b ≠ top`, i.e. in
the first `ϱ` columns. 

### `dualFrameOfGram_apply_eStar`

 The coefficient of `e*_a`, the basis vector with the index `eStar a`, in column `b` of
`dualFrameOfGram T` is `1` if `b = a` and `0` otherwise. 

### `dualFrameOfGram_apply_z`

 The coefficient of `z` in `dualFrameOfGram T` is `-1` in the last column and `0` in the
others. 

### `dualFrameOfGram_apply_indexX₀`

 The part in `X₀` of `dualFrameOfGram T` is `√(1 + T_{last,last}) x_{k₀}` in the last column and
zero in the others. Here `indexX₀ i` is the index of the basis vector `x_i` of `X₀`. 

### `gram_dualFrameOfGram`

 Let `T` be a hermitian `(ϱ + 1)×(ϱ + 1)` matrix (`𝔰.FrameMatrix`) with `1 + Re T_{top,top} ≥ 0`.
Then the tuple `dualFrameOfGram T` has the Gram matrix `T` for `𝔰.J₁`. 

### `sphereMass`

 The mass `π ^ k r ^ (k - 1) / (k - 1)!` of the sphere `⟨x, x⟩ = r` in `ℂ ^ k` for the fibre
measure `dx / d⟨x, x⟩` if `r > 0`, and `0` if `r ≤ 0`. The mass is written as half of
`sphereDensity k r = 2 π ^ k r ^ (k - 1) / (k - 1)!`. 

### `sphereMass_of_pos`

 For `r > 0` the mass of the sphere `⟨x, x⟩ = r` in `ℂ ^ k` is half of
`sphereDensity k r = 2 π ^ k r ^ (k - 1) / (k - 1)!`. 

### `lintegral_neg_single_add_freeCols_mulVec_eq`

 Coordinates for the last vector `-z + ∑ a_b e_b + x` of a tuple dual to the frame
`(e₁, …, e_ϱ, z)`, where `v = (a, x)` and `x` lies in `X₀ = ℂ ^ κ`, of dimension `k = |κ|` and with
the basis `x_i`. Fix `u = unipotentOf q`, an element of the unipotent group `𝖴⁰` fixing the frame.
Write the vector as `u · embedH h` applied to `-z + ∑ c_b e_b + √(1 + r) x_{k₀}`, where `p = (c, r)`
and `r` is the product of the vector with itself. Here `k₀` is the chosen element of `κ`, `h` lies
in `U(κ)`, and `embedH h` acts as `h` on `X₀` and as the identity elsewhere. Then Lebesgue measure
`dv` is `sphereMass k (1 + r) dc dr dh`, with `dh` the Haar probability measure. 

### `lintegral_eq_lintegral_sphereMass_mul_dualFrameOfGram`

 Coordinates on the tuples dual to the frame `e = (e₁, …, e_ϱ, z)`, which are the `J₁ e + R p`:
here `e` is `frameCols`, and `R` is `freeCols`, whose columns are the `e_b` and the basis vectors
`x_i` of `X₀ = ℂ ^ κ`. Write such a tuple as `s y(T)`, where `T = hermOfReal t` is its Gram matrix,
with real coordinates `t`, `y(T) = dualFrameOfGram T` is the standard dual tuple with the Gram
matrix `T`, and `s` lies in the fixer `R°` of the frame, with its measure `ds = fixerHaar 𝔰`. Then
Lebesgue measure `dp` is `2 ^ (-ϱ) sphereMass k r dt ds`, where `k = |κ|` and
`r = 1 + T_{last,last}`. 

 ### The fibre measure on frames, over the matrix of products with the standard frame 

### `lintegral_eq_dualFrameOfGram_mul`

 Coordinates on the tuples `y = J₁ e Z + R p` whose products with the frame
`e = (e₁, …, e_ϱ, z) = 𝔰.frameCols` form the invertible matrix `Z`, where `R = 𝔰.freeCols` has the
columns `e_b` and `x_i`. Write `y = y' Z`, so that `y'` is dual to the frame and has the Gram matrix
`T' = Z⁻¹ᴴ T Z⁻¹` if `y` has the Gram matrix `T = hermOfReal t`. Then `y' = s · dualFrameOfGram T'`
is the standard dual tuple with the Gram matrix `T'`, moved by an element `s` of the fixer `𝖴⁰ U(κ)`
of the frame, and Lebesgue measure `dp` is `|det Z| ^ (2 (k - 1)) 2 ^ (-ϱ) sphereMass k r dt ds`,
where `k = |κ|` and `r = 1 + T'_{last,last}`. Here `sphereMass k r` is the mass
`π ^ k r ^ (k - 1) / (k - 1)!` of the sphere `⟨x, x⟩ = r` in `ℂ ^ k` if `r > 0`, and `0` otherwise;
`ds = fixerHaar 𝔰` is Lebesgue measure in the parameter of `unipotentOf` on `𝖴⁰` times the Haar
probability measure on `U(κ)`; and `s.val.val` is the matrix of `s`. 

### `inv_frameGram_inv_apply`

 The Gram matrix of the frame is `diag(0, …, 0, -1)`; so its congruence by `Z⁻¹` is `-ζᴴ ζ` for
the last row `ζ` of `Z⁻¹`. 

### `one_add_inv_frameGram_inv_top`

 For the congruence `T` by `Z⁻¹` of the Gram matrix of the frame, `1 + T_{last,last}` is
`oneSubNormSqInvCorner Z = 1 - |ξ|²`, with `ξ` the last diagonal entry of `Z⁻¹`. 

### `sectionCoeff_conjTranspose_castSucc_apply`

 Let `ζ` be the last row of `Z⁻¹`. Row `a < ϱ` of `sectionCoeff Z Zᴴ` is row `a` of `-ζᴴ ζ`,
halved in the first `ϱ` columns. The matrix `sectionCoeff Z W` is built from the last row of `Z⁻¹`
and the last column of `W⁻¹`. 

### `sectionCoeff_conjTranspose_top_apply`

 The last row of `sectionCoeff Z Zᴴ` is `(0, …, 0, -1)`. For `Z` in the open cell, the columns of
`sectionCoeff Z W` at `W = Zᴴ` are the coefficients of `e₁, …, e_ϱ, z` in the tuple `y'` that is
dual to the frame `e` and has `γ_Z e = y' Z`. 

### `dualFrameOfGram_mul_eq_gramSection_mul`

 For `Z` in the open cell and `γ_Z = gramSection Z`, the chosen element of `G₁` for which the
products of `e` with `γ_Z e` form `Z`, the image `γ_Z e` of the frame `e = 𝔰.frameCols` is `y' Z`,
where `y'` is the tuple dual to `e` that `New.RealPlace.dualFrameOfGram` attaches to the congruence
by `Z⁻¹` of the Gram matrix of `e`. 

### `gramSectionMeasure`

 The measure on `G₁` that is the law of `s γ_Z`, for `Z` in the open cell and `s` in the fixer
`R°` of the frame, under `dZ ds` with the density `2 ^ (-ϱ) π ^ k 𝗀(Z) ^ (k - 1) / (k - 1)!`. Here
`γ_Z = New.RealPlace.gramSection Z` and `𝗀 = New.RealPlace.gramDiscReal`. 

### `gramCoords_dualFrameOfGram_mul`

 Let `T = hermOfReal t`, let `Z` be invertible and put `T' = Z⁻¹ᴴ T Z⁻¹`. If
`1 + T'_{last,last} ≥ 0`, then for all `s` in `G₁` the tuple `s (dualFrameOfGram T') Z` has the
Gram matrix `T`, that is, its Gram coordinates `gramCoords` are `t`. 

### `det_ne_zero_of_mem_openCell`

 A matrix in the open cell, the set of invertible `Z` whose inverse has last diagonal entry of
absolute value less than `1`, has nonzero determinant. 

### `enorm_det_pow_mul_sphereMass`

 Let `𝔰` be a shape with `ϱ` hyperbolic pairs and index set `κ`, and let `k = |κ|`. Let `Z` lie
in the open cell `𝔰.openCell`: `Z` is invertible and the last diagonal entry of `Z⁻¹` has absolute
value less than 1. Let `𝗀(Z) = gramDiscReal Z` be `|det Z|²` minus the squared absolute value of the
leading minor of order `ϱ` of `Z`. Take the mass `sphereMass` of the sphere in `ℂ ^ k` of squared
radius `oneSubNormSqInvCorner Z = 𝗀(Z) / |det Z|²`, and multiply it by
`|det Z| ^ (2 (k - 1)) 2 ^ (-ϱ)`. The result is the density
`2 ^ (-(ϱ + 1)) sphereDensity k 1 · 𝗀(Z) ^ (k - 1)` of `New.RealPlace.gramSectionMeasure`. 

### `setLIntegral_openCell_frame_coords_le`

 The integral of `K ≥ 0` over the tuples `J₁ e Z + R p` with `Z` in the open cell, where `e` is
the frame and `R = 𝔰.freeCols`, is at most its integral over all tuples. 

### `leGramFibre_gramSectionMeasure`

 Let `e = 𝔰.frameCols` be the matrix with the columns `e₁, …, e_ϱ, z` of the frame and `𝔰.J₁` the
matrix of the hermitian form that defines `G₁`. The measure `gramSectionMeasure 𝔰` is the law of
`s γ_Z` under `2 ^ (-ϱ) π ^ k / (k - 1)! · 𝗀(Z) ^ (k - 1) dZ ds`, where `Z` runs over the open cell,
`s` over the fixer of `e` with `ds = fixerHaar 𝔰`, `γ_Z = gramSection Z`, `k = |κ|`, and
`𝗀(Z) = gramDiscReal Z` is `|det Z|²` less the squared absolute value of the leading minor of order
`ϱ`. The image `l` of this measure under `g ↦ g e` is at most the fibre measure `dY / dT` of the
Gram map `Y ↦ T = Yᴴ J₁ Y` over the Gram matrix `T₀` of `e`. Here `dY` is Lebesgue measure on the
matrices `Y` of the size of `e`, and `dT` is Lebesgue measure in the real coordinates of `T`
(`hermOfReal`). By the definition of `LeGramFibre` this means: if `K ≥ 0` is lower semicontinuous
and `∫_{T(Y) ∈ S} K dY ≤ C vol(S)` for all open `S` inside some neighbourhood of `T₀`, then
`∫ K dl ≤ C`. 

### `lintegral_gramSection_le`

 The mean value inequality. For measurable `f ≥ 0` on `G₁`, the integral of `f (s' γ_Z s)` over
`s, s'` in the fixer `R°` of the frame and `Z` in the open cell, with density `c 𝗀(Z) ^ (k - 1)`, is
at most the integral of `f` over `G₁` for Haar measure. Here `γ_Z = New.RealPlace.gramSection Z` is
the element with the matrix `Z` of products of the frame `e` with `γ_Z e`, `k = |κ|`,
`r = k + 2 ϱ + 1`, `c = New.Shape.openCellConst` is `vol U(k) / vol U(r)` times the area of the unit
sphere in `ℂ ^ k`, and `𝗀 = New.RealPlace.gramDiscReal` is `|det Z|²` less the squared absolute
value of the leading minor of order `ϱ`. 
