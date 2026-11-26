---
{
  "module": "src/New/Spanning/RemainingTerms/OrbitSize.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/RemainingTerms/OrbitSize.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/RemainingTerms/OrbitSize.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Near terms in the filling theorem: the bound for an orbit, the tail and the open-cell term

This file defines the size allotted to a near orbit of terms `γ` and bounds the tail and the
open-cell term by it. The data are `S : New.Filling E 𝔰` for a shape `𝔰`, with the size hypotheses
`New.Filling.IsAdmissible`, which compare all constants with powers of the large parameter `b`.
For admissible data, if `S.termDiscNorm γ` is at least 1, then the orbit bound at the top cell
rank, with that norm as gauge, bounds the open-cell term of `γ` and, if `γ` is near, also the tail.
Here `k = |κ|`, `f` is the number of infinite places and `τ = b^(kf/4)`.

## Main definitions and results

* `New.Filling.cellRankSecondMoment`: the second moment D_j against which the size of a term of cell
  rank j is measured. It is the main second moment at the top cell rank and τ^(−16) = b^(−4kf) times
  the identity second moment below it.
* `New.Filling.orbitBound`: the bound allotted to a near orbit, as a function of its cell rank j and
  of its gauge x. It is τ² (D_j / (n_p (M^(2j'f) x)^k))^(1/2) with j' = min ϱ j, in units of the
  covolume ν.
* `New.Filling.IsNear.inv_pow_le_orbitBound`, `New.Filling.prod_pairingBoundSq_le`: the two bounds
  by the orbit bound at the top cell rank, for the tail and for the open-cell term.

Notions from other files:
* `New.Filling.termDisc`: 𝗀(γ) = |D_{ϱ+1}|² − N²|D_ϱ|², with D_l the leading minors of
  `New.Filling.frameProducts γ`.
* `New.Filling.mainSecondMoment`, `New.Filling.identitySecondMoment`: the numbers
  sourceDim² / (besselDegree · mass), with the mass of the genus of the standard lattice, and
  sourceDim times the order of the reduced image of the Bessel subgroup `besselS`.
* `New.Filling.unipotentCovolume`: the number ν that serves as covolume of the unipotent group.
* `New.Filling.IsNear` (from `New.Spanning.Unfolding.Terms`): `γ` joins two boxed archimedean
  points.
* `New.Filling.termDiscNorm`, `New.Filling.pairCountScale` (from `New.Spanning.Unfolding.Terms`):
  the product over the infinite places of |𝗀(γ)|_v, and the number n_p = #R̄₀ n_X N^(−kf).


### `cellRankSecondMoment`

 The second moment `D_j` against which the size of a term of cell rank `j` is measured:
`mainSecondMoment` at the top cell rank `ϱ + 1`, and `τ ^ (-16)` times `identitySecondMoment` below
it, where `τ` is `tailScale`. 

### `orbitBound`

 The bound `τ² (D_j / (n_p (M ^ (2 j' f) x) ^ k)) ^ (1 / 2)`, `j' = min ϱ j`, for one near orbit
of terms under left and right multiplication by the groups `classUnipotent₀`, of cell rank `j` and
gauge `x`, in units of the covolume `unipotentCovolume`. Here `τ` is `tailScale`, `D_j` is
`cellRankSecondMoment j`, `n_p` is `pairCountScale`, `M` is the level `S.M`, `k` is the rank of `X₀`
and `f` is the number of infinite places. 

### `norm_map_termDisc_le`

 At every infinite place the absolute value of `S.termDisc γ = |D_n|² - N² |D_{n-1}|²` is at most
`|D_n|²`, where `D_l` is the leading minor of order `l` of the matrix `S.frameProducts γ` of
products of the frame with its image under `γ`, and `n = ϱ + 1`. 

### `IsNear.termDiscNorm_le`

 For admissible data with size parameter `b = S.b` and a near term `γ` (see `IsNear`), the
product of the absolute values of `S.termDisc γ` over the `f` infinite places is at most
`b ^ (270 n² f)`, `n = ϱ + 1`. 

### `cellRankSecondMoment_nonneg`

 The second moment `D_j` against which the size of a term of cell rank `j` is measured is
nonnegative. 

### `orbitBound_top`

 At the top cell rank the orbit bound at `x` is
`τ² (mainSecondMoment / (pairCountScale M ^ (2 ϱ f k) x ^ k)) ^ (1 / 2)`, where `τ` is `tailScale`,
`M` is the level and `f` is the number of infinite places. 

### `pairCountScale_le_mainSecondMoment`

 For admissible data, `pairCountScale` is at most the main second moment. 

### `IsNear.inv_pow_le_orbitBound`

 Let the data be admissible, with size parameter `b = S.b`. Let `γ` be near, that is, some
archimedean point `y` has both `y` and `γ⁻¹ y` in `boxedPoints`, and let `x = termDiscNorm γ` be the
product of the absolute values of `termDisc γ` over the infinite places. If `1 ≤ x`, then the bound
`orbitBound ⊤ x` allotted to an orbit of the top cell rank `ϱ + 1` is at least `b ^ (-k³ f)`. 

### `pairingBoundConst`

 The factor of the product over the infinite places of the open-cell bounds `pairingBoundSq` at
`S.ratToInf γ v` that does not depend on `γ`: the product with the absolute values of
`S.termDisc γ` replaced by `1` (see `prod_pairingBoundSq_eq`). 

### `prod_pairingBoundSq_eq`

 For every rational `γ`, the product over the infinite places `v` of the open-cell bounds
`pairingBoundSq` is `pairingBoundConst / x ^ (10 ^ 5 n ^ 4 + (k - 1))`, where `x = termDiscNorm γ`,
`n = ϱ + 1` and `k` is the rank of `X₀`. 

### `prod_frameScaleSq_bounds`

 Let the data be admissible, with size parameter `b = S.b`, let `n = ϱ + 1` be the number of
frame vectors and `k` the rank of `X₀`. At an infinite place `v` let
`s_a = S.frameScaleSq v a = (S.realM v) ^ (2 (ϱ - a)) / N` be the squared scale of the frame vector
of index `a`. The product `s` of the `s_a` lies between `b ^ (-60 n²)` and `b ^ (46 n²)`, and
`∏ s_a ^ (k + 2 (ϱ - a))`, the factor of `frameScaleProd` at `v`, is at most `s ^ k b ^ (92 n³)`. 

### `pairingBoundConst_le_mul`

 For admissible data, `pairingBoundConst ≤ 2 ^ (k f) τ d² / (deg c_G ^ f Λ²)`. The left side is
the factor of the product over the infinite places of the open-cell bounds `pairingBoundSq` that
does not depend on the rational element at which they are taken. The numbers `d = card BesselCoord`
and `deg = besselDegree` are the products of the dimensions and of the degrees of the Bessel systems
at these places, `c_G = openCellConst` is a quotient of volumes of unitary groups, and
`Λ = frameScaleProd` is the product over all infinite `v` and all `a ≤ ϱ` of `s ^ (k + 2 (ϱ - a))`,
with `s = (S.realM v) ^ (2 (ϱ - a)) / N` the squared scale of the frame vector of index `a` at
`v`. 

### `two_pow_mul_pairCountScale_mul_le`

 For admissible data (`S.IsAdmissible`), `2 ^ (k f) n_p M ^ (2 ϱ f k) ≤ τ a_* vol(Ô) ^ n`, where
`n = 𝔰.n = ϱ + 1`. Here `k` is the rank of `X₀`, `f` is the number of infinite places,
`τ = tailScale = b ^ (k f / 4)` for the size parameter `b`, `M = p₀ p₁` is the level and
`vol(Ô) = volÔ E = 2 ^ f / √|disc E|`. With `R̄₀` the reduced image of the Bessel subgroup, `n_X`
the number of classes and `N = -h(z, z)` the prime `S.N`, `n_p = pairCountScale` is
`#R̄₀ n_X N ^ (-k f)`, and `a_* = scaledSiegelConst` is `#R̄₀ n_X` times
`unipotentOrder = M ^ (f ϱ (2 k + 2 ϱ + 1))` times `siegelConst = (π ^ k / ((k - 1)! N ^ k)) ^ f
|disc E| ^ (1 / 4) vol(Ô) ^ k`. 

### `pairingBoundConst_le`

 For admissible data, `pairingBoundConst` is at most `(ν τ² / 2)²
mainSecondMoment / (pairCountScale M ^ (2 ϱ f k))`. Here `ν` is `unipotentCovolume`, `τ` is
`tailScale`, `M` is the level, `ϱ` is the number of hyperbolic planes, `k` is the rank of `X₀` and
`f` is the number of infinite places. 

### `prod_pairingBoundSq_le`

 Let the data be admissible (`S.IsAdmissible`), let `γ` be rational, and let `x = termDiscNorm γ`
be the product of the absolute values of `termDisc γ` over the infinite places. If `1 ≤ x`, then the
product over the infinite places `v` of the open-cell bounds `pairingBoundSq` at `S.ratToInf γ v` is
at most `(ν σ / 2)²`. Here `ν` is `unipotentCovolume`, and `σ = orbitBound ⊤ x` is the value at `x`
of the bound `orbitBound` for an orbit of the top cell rank `⊤ = ϱ + 1`. 
