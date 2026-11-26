---
{
  "module": "src/New/Determinant/Exchange/RealVectors.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Determinant/Exchange/RealVectors.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Determinant/Exchange/RealVectors.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Smooth local Witt theorem and the exchange identity for `V' ⊕ W₁` and `V'`

Construction of the data at the real places for the identity `New.Exchange.RowColExchangeIdentity`
between the theta integrals of the pairs `(X, V' ⊕ W₁)` and `(X, V')`, where `X` splits over `W₁`.

* `New.Exchange.exists_isSchwartzVector_realSlice_eq`: a Schwartz Fock vector whose slices are a
  bump function times `realWeil 1 v`, scaled so that its slice at 0 for the opposite splitting is
  `v`.
* `New.Exchange.exists_contDiff_witt`: a local form of Witt's theorem for spans: frames near a
  nondegenerate frame `x` lie in the span of a unitary image of `x` that depends smoothly on them.
* `New.Exchange.exists_rowColExchangeIdentity_sum`: two vectors for which
  `New.Exchange.RowColExchangeIdentity` holds for these two pairs, one of them with a prescribed
  slice at 0.

Notions from other files:
* `New.Space.Splitting`: a decomposition V = (lE^p ⊕ kE^p) ⊥ iV₀ with dual isotropic frames l, k and
  an isometric embedding i of V₀; `New.Space.Splitting.symm` exchanges k and l. It is adapted
  (`New.Exchange.IsBaseAdapted`) if the frames are orthonormal at the infinite places and integral
  at the finite ones.
* `New.PairFock E s t`: the Fock space of matrices whose `(i, j)` coordinate has the sign
  `t i * s j`, repeated at every infinite place. These signs are `New.homSigns s t`, and repeating
  them at every place is `New.realSigns`.
* `New.realPairWeil γ γ'`: the Weil representation on this Fock space, restricted to a pair of
  unitary groups at the infinite places, twisted by the powers of the determinants with exponents
  `γ` on the second and `-γ'` on the first.
* `New.Exchange.IsSchwartzVector`: all moments of the Fock vector are finite.
* `New.Exchange.realSlice`: the slice of a vector in the mixed Schrödinger–Fock model of an adapted
  splitting.
* `New.Exchange.RowColExchangeIdentity`: two theta integrals are proportional on admissible data,
  with a formula for the absolute value of the factor.

## Relation to the literature

See `New.Determinant.Exchange.TheoremForPartners` for related work. See
`Lib.Adelic.Witt.IwasawaDecomposition` for sources.


### `exists_isSchwartzVector_realSlice_eq`

 Let `τ ≥ 0` be smooth, compactly supported and nonzero at some `y`, and let `v` be a Schwartz
vector for `(W₁, V')`. Then there are a complex number `κ` and a Schwartz vector `Λ` for `(X, V')`
whose slice at each `x` is `τ x • κ` times `realWeil 1 v`, and whose slice at `0` for `D.symm`, the
splitting with the two isotropic frames exchanged, is `v`. 

### `exists_isSchwartzVector_realSlice_zero_eq`

 Taking the slice at `0` is onto on Schwartz vectors. Every Schwartz vector `v` (all moments
finite) in the Fock space `PairFock E s t'` of `(W₁, V')` is the slice at `0` of a Schwartz vector
in the Fock space `PairFock E r t'` of `(X, V')`. 

### `exists_contDiff_witt`

 A smooth local form of Witt's theorem, for spans. Let `J` be Hermitian and `x` a frame
(a matrix of column vectors) with invertible Gram matrix `xᴴ * J * x`. There are elements `k y` of
the unitary group `U J`, indexed by all frames `y`, such that the matrix of `k y` is a smooth
function of `y` and, for `y` near `x`, the columns of `y` are linear combinations of those of
`k y * x`. 

### `isSchwartzVector_realBoxProd`

 The external product `realBoxProd he v w` of two Schwartz Fock vectors (all moments finite), for
a splitting `e` of the coordinates compatible with the signs, is a Schwartz vector. 

### `exists_contDiff_eventuallyEq_inv`

 Matrix inversion agrees, near a matrix `A₀` of nonzero determinant, with a function that is
smooth on all matrices. 

### `exists_mul_mul_eq_and_gram_eq`

 If `x * A` has an invertible Gram matrix for `J` and equals `g * x₀ * c` with `g` in the unitary
group `U J`, then `x` has the same form `g * x₀ * c'`, and `c'` carries the Gram matrix of `x₀` to
that of `x`. 

### `IsWittBump`

 Smooth data for Witt's theorem near a frame `x₀`, for a form `J`: a function `γ` on square
matrices, unitary elements `k y` indexed by frames `y`, and a bump function `σ` on families of
frames. For each member `y` of a family at which `σ` does not vanish, `γ` inverts the Gram matrix of
`y` and `y` lies in the span of `k y * x₀`. 

### `IsWittBump.contDiff_inv`

 `γ` is smooth. 

### `IsWittBump.inv_gram_base`

 `γ` inverts the Gram matrix of `x₀`. 

### `IsWittBump.contDiff_unitary`

 The matrix of `k y` is a smooth function of `y`. 

### `IsWittBump.contDiff_bump`

 `σ` is smooth. 

### `IsWittBump.hasCompactSupport_bump`

 `σ` has compact support. 

### `IsWittBump.bump_nonneg`

 `σ` is nonnegative. 

### `IsWittBump.bump_base`

 `σ` is `1` at the constant family `x₀`. 

### `IsWittBump.exists_mul_eq`

 Where `σ` does not vanish, each frame `y` lies in the span of `k y * x₀`. 

### `IsWittBump.inv_gram`

 Where `σ` does not vanish, `γ` inverts the Gram matrix of each frame. 

### `IsWittBump.det_gram_ne_zero`

 Where `σ` does not vanish, the Gram matrix of each frame is invertible. 

### `exists_contDiff_witt_and_bump`

 For `J` Hermitian and a frame `x₀` with invertible Gram matrix there are a smooth function `γ`,
elements `k y` of `U J` depending smoothly on the frame `y` and a bump function `σ`, equal to 1 at
the constant family `x₀`, such that for each member `y` of a family where `σ` is nonzero `γ` inverts
the invertible Gram matrix of `y` and `y` lies in the span of `k y * x₀` (`IsWittBump`). 

### `mul_gram_inv_mul_of_isUnit_det`

 The `J`-orthogonal projection `x * (xᴴ * J * x)⁻¹ * xᴴ * J * x₀` of `x₀` to the span of a frame
`x` does not change when `x` is multiplied on the right by an invertible matrix. 

### `exists_sum_one_eq_mul_mul_sum`

 Let `g`, `k` be unitary for the diagonal form with signs `t' ⊕ᵥ s` and `u` unitary for the form
with signs `t'`. If `k * x₀ * u = g⁻¹ * x₀`, where `x₀ = fromRows 1 0` is the frame of the first
summand, then `g * k * diag(u, 1)` fixes `x₀` and so is `diag(1, q)` with `q` unitary for `s`. 

### `placeMatrices`

 The coordinates at the infinite places of an `a × b` matrix, read as one complex matrix for each
place. 

### `realSlice_eq_slice_placeMatrices_symm`

 The real slice at an adelic matrix `x` is the slice at its coordinates at infinity. 

### `frameProjection`

 For a function `γ` that inverts Gram matrices, the projection of the frame `fromRows 1 0` of the
first summand to the span of the frame `x`, orthogonal for the form with signs `t' ⊕ᵥ s`. 

### `unitaryMovedFrame`

 The family `x` of frames moved by the inverses of the unitary elements `k (y v)`. 

### `exchangeSection`

 For families `y`, `x` of frames, one for each infinite place `w`, unitary elements `k y` indexed
by frames, a constant `κ` and vectors `v`, `v₁` in the Fock spaces `PairFock` of the signs `(s, t')`
and `(s, s)`, the vector `(σ y * σ x' * κ * ∏ w, conj (det (x' w)₁) ^ (2 * M w)) • ω (1, k ∘ y) (v ⊠
v₁)`, where `x' w = (k (y w))⁻¹ * x w` (`unitaryMovedFrame`), `(x' w)₁` is its upper square block,
`ω` is the real Weil representation `realPairWeil` twisted by `det ^ (j - M w)` on the unitary group
of `t' ⊕ᵥ s`, and `⊠` is the external product `realBoxProd`. In the applications `t'` and `s` are
the signs of spaces `V'` and `W₁`, `j` is half the rank of `W₁`, `M` is the weight of a character,
and this vector is a prescribed slice for the pair `(X, V' ⊕ W₁)`. 

### `exists_isSchwartzVector_realSlice_bump`

 Let `σ ≥ 0` be a smooth compactly supported function on families of frames in `V' ⊕ W₁`, equal
to 1 at the frame `(1, 0)` of `V'`, let `N` be a family of exponents and `v` a Schwartz vector (all
moments finite) in the Fock space `PairFock E s t'` of `(W₁, V')`. There are `κ` and a Schwartz
vector `Λ` for `(X, V')` whose slice at an adelic matrix with infinite components `x w`
(`atRealPlace`) is `σ (x, 0) * ‖∏ w, det (x w) ^ N w‖ ^ 2 * κ` times `v`, and whose slice at 0 for
`D.symm`, the splitting with the two isotropic frames exchanged, is `v`. 

### `exists_isSchwartzVector_exchangeSection`

 Let `σ` be smooth with compact support, `z` and `k` smooth maps on frames, and `v`, `v₁`
Schwartz vectors (all moments finite) in the Fock spaces `PairFock` of `(W₁, V')` and `(W₁, W₁)`.
Then some Schwartz vector `Φ` in the Fock space of `(X, V' ⊕ W₁)` has slice
`exchangeSection σ k j M κ v v₁ y x` at every adelic matrix with infinite components `x`, for
`y = z ∘ x`. 

### `exchangeSection_frameProjection_mul`

 For families `y`, `x` of frames, one for each infinite place `w`, and vectors `v₀`, `v₁` in the
Fock spaces `PairFock` of the signs `(s, t')` and `(s, s)`, the value `exchangeSection σ k j M κ v₀
v₁ y x` is `(σ y * σ x' * κ * ∏ w, conj (det (x' w)₁) ^ (2 * M w)) • ω (1, k ∘ y) (v₀ ⊠ v₁)`, where
`x' w = (k (y w))⁻¹ * x w` (`unitaryMovedFrame`), `(x' w)₁` is its upper square block, `ω` is the
real Weil representation `realPairWeil` twisted by `det ^ (j - M w)` on the unitary group of `t' ⊕ᵥ
s`, and `⊠` is the external product `realBoxProd`. Write `frameProjection γ x` for the projection of
the frame `(1, 0)` to the span of the frame `x`, with `γ` in the place of the inversion of the Gram
matrix. If `γ` inverts the Gram matrices of the frames on which `σ` is nonzero and of each `x w`,
then in the section with second argument `A w = x w * C w` (`C w` invertible) and first argument the
projections for `A`, these may be replaced by the projections for `x`. 

### `exists_unitary_pair_of_frame`

 If each frame `(h v)⁻¹ * fromRows 1 0` is `k v * fromRows 1 0 * c` with `c` carrying the form
with signs `t'` to its Gram matrix, then `c` is a unitary `u v`, and for some unitary `q v` one has
`diag(u v, (q v)⁻¹) * h v * k v = 1`. 

### `prod_conj_pow_eq_norm_div`

 Let `𝔠` be a tame character (`SplitTameChar`) of weight `μ ≥ 0` with automorphic character
`ν = 𝔠.character` of the norm-one ideles, so that `ν` has weight `μ w` at each infinite place `w`,
and let `z` be the idele with infinite part `ζ` and finite part 1. Then the product of the
`conj (ζ w) ^ (2 μ w)` is `‖∏ ζ w ^ (j + μ w)‖ ^ 2 / (ν(z / z̄) |z| ^ j)`. 

### `realPairWeil_exchangeSection`

 For families `y`, `x` of frames, one for each infinite place `w`, and vectors `v`, `v₁` in the
Fock spaces `PairFock` of the signs `(s, t')` and `(s, s)`, the value `exchangeSection σ k j M κ v
v₁ y x` is `(σ y * σ x' * κ * ∏ w, conj (det (x' w)₁) ^ (2 * M w)) • ω (1, k ∘ y) (v ⊠ v₁)`, where
`x' w = (k (y w))⁻¹ * x w` (`unitaryMovedFrame`), `(x' w)₁` is its upper square block, `ω` is the
real Weil representation `realPairWeil` twisted by `det ^ (j - M w)` on the unitary group of `t' ⊕ᵥ
s`, and `⊠` is the external product `realBoxProd` (its first argument is the proof that the signs
split accordingly). Suppose that `g * (k ∘ y) = 1` and `x' = (B, 0)` whenever `σ y ≠ 0`. Then `ω (1,
g)` carries this value to `σ y * σ (B, 0) * κ * ∏ w, conj (det (B w)) ^ (2 * M w)` times `v ⊠ v₁`.


### `atRealPlace_inv_sum_mul_fromRows`

 Let `h` be a point of `GInf E (t' ⊕ᵥ s)`, the unitary group for the signs `t' ⊕ᵥ s` at the
infinite places. Let `u`, `q` be points of `GInf E t'` and `GInf E s`. All three are completed by
`1` at the finite places to adelic points, and `G.sum` is the block sum of `u` and `q`. At each
infinite place `w`, the adelic matrix `(diag(u, q) * h)⁻¹ * fromRows B 0` has component
`h⁻¹ * fromRows 1 0 * u⁻¹ * B`. 

### `gram_signMatrix_fromRows_one_zero`

 The Gram matrix of the frame `fromRows 1 0` of the first summand, for the form with signs
`t' ⊕ᵥ s`, is the form with signs `t'`. 

### `IsWittBump.exists_mul_fromRows_mul_eq_of_ne_zero`

 Let `γ`, `k`, `σ` be smooth Witt data near `x₀ = fromRows 1 0` for the form with signs `t' ⊕ᵥ s`
(`IsWittBump`): for each member `z` of a family of frames where the bump function `σ` is nonzero,
`γ` inverts the Gram matrix of `z` and `z` lies in the span of `k z * x₀`, with `k z` unitary. Let
`y w = frameProjection γ (x w)` be the projection of `x₀` to the span of the frame `x w`, with `γ`
in the place of the inverse Gram matrix. If `σ y ≠ 0`, then `x w = k (y w) * x₀ * c` for a matrix
`c` that carries the form with signs `t'` to the Gram matrix of `x w`. 

### `IsWittBump.eventually_bump_frameProjection_ne_zero`

 Let `γ`, `k`, `σ` be smooth Witt data near `x₀ = fromRows 1 0` for the form with signs `t' ⊕ᵥ s`
(`IsWittBump`); in particular `γ` inverts the Gram matrix of `x₀` and the bump function `σ` is `1`
at the constant family `x₀`. For `h` near `1` in `GInf`, the product of the unitary groups of the
form over the infinite places, `σ` does not vanish at the family of projections `frameProjection γ`
of `x₀` to the spans of the frames `(h w)⁻¹ * x₀`, formed with `γ` in the place of the inverse Gram
matrix. 

### `IsWittBump.isPeriodIdentity`

 Let `γ`, `k`, `σ` be smooth Witt data near `x₀ = fromRows 1 0` (`IsWittBump`): for frames `y`
where the bump function `σ` is nonzero, `y` lies in the span of `k y * x₀` with `k y` unitary, and
`γ` inverts the Gram matrix of `y`; `frameProjection γ x` is the projection of `x₀` to the span of
`x`, formed with `γ`. Let `D` be an adapted Witt decomposition of the Hermitian space `X` as `W₁`
plus `card b` hyperbolic planes, let `W₁` have rank `2 j` and split off a hyperbolic plane by `D₁`,
let `V'` have rank `card b`, and let `𝔠` be a tame character of weight `μ`, with automorphic
character `ν = 𝔠.character`. Let `v₁` be a Schwartz vector (all moments finite). Suppose that the
slice of `Φ` at `x` is `exchangeSection` at `x` and `y = frameProjection γ ∘ x`, namely
`(σ y * σ x' * κ * ∏ w, conj (det (x' w)₁) ^ (2 * μ w)) • ω (1, k ∘ y) (v ⊠ v₁)`, where
`x' w = (k (y w))⁻¹ * x w` (`unitaryMovedFrame`), `(x' w)₁` is its upper square block, `ω` is the
real Weil representation `realPairWeil` twisted by `det ^ (j - μ w)` on the unitary group of
`t' ⊕ᵥ s`, and `⊠` is the external product `realBoxProd`, and that the slice of `Λ` at `x` is
`σ (x, 0) * ‖∏ w, det (x w) ^ (j + μ w)‖ ^ 2 * κ` times `v`. Then `IsPeriodIdentity` holds: for each
`h` at infinity there is `p` in `U V' × U W₁` such that for all invertible `B` the theta functional
of the slice of `Φ` at `(p h)⁻¹ (B, 0)`, moved by `p h` and integrated over the adelic quotient of
`U W₁`, is `ρ h * I₀ / (ν(z / z̄) |z| ^ j)` times the theta functional of the slice of `Λ` at `B`.
Here `z` is the idele with infinite part `det B` and finite part 1, `ρ h` is `σ` at the projections
of `x₀` to the spans of `(h w)⁻¹ * x₀`, and the period `I₀` is the value at `1` of the theta
integral `thetaLarge` over `U W₁` with real part `v₁` and, at the ramified places of `𝔠`, the
function `stdColDatum`. 

### `exists_rowColExchangeIdentity_sum`

 Let `D` be an adapted Witt decomposition of the Hermitian space `X` (signs `r`) as `W₁` (signs
`s`) plus `card b` hyperbolic planes, where `W₁` has even rank and an adapted splitting `D₁` along
an isotropic line, and let `V'` be a space with basis indexed by `b` and signs `t'`. Let `v` and
`v₁` be Schwartz vectors for `(W₁, V')` and `(W₁, W₁)`. Then there are vectors `Φ` for
`(X, V' ⊕ W₁)` and `Λ` for `(X, V')` with two properties. The slice `realSlice` of `Λ` at `0`, its
value at `0` in the mixed Schrödinger–Fock model of the splitting `D.symm` with the isotropic frames
exchanged, is `v`. And `RowColExchangeIdentity` holds: `Φ`, `Λ` are Schwartz and there is a real `C`
such that for each tame character `𝔠` of weight `μ` some `c : ℂ` has `C * ‖c‖ ^ 2 = lValueProdInt 𝔠
(rk (V' ⊕ W₁) - rk X / 2) * equalRankThetaRatio W₁ 𝔠 v₁`, and for all integral `z` the theta
integral of `Φ` and the row datum of `z` is `c` times that of `Λ` and the column datum of `z`. With
`χ` the character of `𝔠` at its ramified places, these data are `x ↦ χ⁻¹ (det)` of the matrix with
the rows of `z` and `x` ordered by `e`, and `x ↦ χ⁻¹ (det (z * x))`. 
