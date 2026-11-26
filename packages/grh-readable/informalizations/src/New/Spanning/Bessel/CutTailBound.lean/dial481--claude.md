---
{
  "module": "src/New/Spanning/Bessel/CutTailBound.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Bessel/CutTailBound.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Bessel/CutTailBound.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The Bessel function at a real place: decay and cut

The file concerns Bessel functions (`New.IsBesselFunction`) on the real unitary group
G₁ = `New.Shape.G₁`: bounded functions to ℂ^I that transform on the left by a character of the
unipotent group 𝖴 = `New.Shape.Form.besselU` and by `rep` under H = U(κ). Throughout, p is a unitary
frame that diagonalises the form, c_λ = `New.HCParam.dsCoeffInFrame` is the discrete series
coefficient of a parameter l = 2λ with large gap (`New.HCParam.HasLargeGap`), v is a unit vector of
ℂ^I, and e = deg·c_λ with deg = `New.HCParam.formalDegree`. F is reproduced by e if F * e = F for
the convolution `New.convolve`: (F * e)(y) = ∫ e(a⁻¹) F(ya) da. The measure of 𝖴∖G₁ is
`New.besselQuotMeasure`. G₁ consists of r × r matrices with r = `𝔰.r`, ‖g‖ is the operator norm, and
n = `𝔰.n` = ϱ + 1 with ϱ the number of hyperbolic planes of the form.
* `New.exists_isDecayMajorant_besselAverage`: the normalised average of c_λ over the Bessel subgroup
  decays in the length, below a bounded integrable weight (`New.IsDecayMajorant`).
* `New.besselCut`: the cut of a function at length b^(6n+2); it is close to the function in L²
  (`New.IsDecayMajorant.lintegral_sq_besselCut_sub_le`).
* `New.exists_isCutPair_besselAverage`: a multiple of the average is reproduced by e and forms a cut
  pair (`New.IsCutPair`) with its cut.

Notions from other files:
* `New.besselLength`: for y in G₁, the infimum of ‖sy‖ + 1 over s in the Bessel subgroup S = 𝖴H
  (`New.Shape.Form.besselS`).
* `New.Shape.besselGraph`: the group 𝖴H as a graph, the pairs (g, k) in G₁ × U(κ) with k⁻¹g in 𝖴.
* `New.DiscreteSeries.besselAverage`: the function y ↦ ∫_S c_λ(x⁻¹ s y) π(s)⁻¹ v ds, where π is the
  character on 𝖴 and `rep` on H.
* `New.scaledBesselLength`: the larger of 1 and the length divided by b^(6n).

## Relation to the literature

A Bessel function at a real place, an average of a discrete series coefficient with a large period
integral, inherits the coefficient's decay. Normalised and multiplied by a scalar cut-off, it gives
a continuous approximant, close in L² and compactly supported modulo the unipotent group, with an
explicit tail bound. Related work: Muić, Fourier coefficients of automorphic forms and integrable
discrete series, 2015; Miličić, Asymptotic behavior of matrix coefficients of the discrete series,
1977; Wallach, Real Reductive Groups II, 1992.

See `New.Spanning.Bessel.FillingData` for related work.


### `norm_frameEquiv`

 The frame is unitary, so passing to it by `frameEquiv` (g ↦ p⁻¹ g p) keeps the operator
norm. 

### `lintegral_formalDegree_mul_decay_le`

 Let `G₁` be the unitary group of `r × r` matrices of the shape `𝔰`, and `l` a discrete series
parameter of gap `500 r ^ 3 + A`, with entries bounded by `L` and formal degree `deg`. For a natural
number `M > 8 r ^ 2`, `b ≥ 2000` and `r + L + 1 ≤ b ^ 4`, the integral of `deg * (2 / ‖g‖) ^ M`
(operator norm) over `g` in `G₁` is at most `b ^ (50 r ^ 2 + 1) * 2 ^ M`. 

### `formalDegree_mul_lintegral_decay_le`

 Let `G₁` be the unitary group of `r × r` matrices of the shape `𝔰`, and `l` a discrete series
parameter of gap `500 r ^ 3 + A`, with entries bounded by `L` and formal degree `deg`. For
`M = 9 r ^ 2`, `b ≥ 2000` and `r + L + 1 ≤ b ^ 4`, the product of `deg`, the integral of
`(2 / ‖g‖) ^ M` (operator norm) over `g` in `G₁`, and `16 ^ M` is at most `b ^ (99 r ^ 2)`. 

### `formalDegree_mul_volume_ball_le`

 Let `G₁` be the unitary group of `r × r` matrices of the shape `𝔰`, and `l` a discrete series
parameter of gap `500 r ^ 3 + A`, with entries bounded by `L` and formal degree `deg`. If
`b ≥ 2000`, `r + L + 1 ≤ b ^ 4` and `T ≥ 1`, the set of `g` in `G₁` of operator norm at most `T` has
volume at most `T ^ (9 r ^ 2) * b ^ (99 r ^ 2) / deg`. 

### `besselLength_div_le_half_norm`

 Let `s` be in the Bessel subgroup 𝖴H of `G₁` (the first component of a pair in `besselGraph`).
If `b ≥ 2` and the length `besselLength x` is at most `b ^ (5 n)`, with `n = ϱ + 1`, then the length
of `y` divided by `b ^ (6 n)` is at most `‖x⁻¹ s y‖ / 2`. 

### `scaledBesselLength_pow_mul_enorm_besselAverage_le`

 Decay of `W = besselAverage l rep x v`, the average `W y = ∫ c_λ(x⁻¹ s y) π(s)⁻¹ v ds` of the
discrete series coefficient of `l = 2λ` over the Bessel subgroup 𝖴H of `G₁`, where π is a character
on 𝖴 and `rep` on H = U(κ). The integrals run over `besselGraph`, the pairs `(s, k)` of an element
`s` of 𝖴H and its component `k` in H. Let `r` be the size of the matrices of `G₁` and `n = ϱ + 1`.
Suppose `l` has gap `500 r ^ 3 + A`, `v` is a unit vector, `b ≥ 2`, `besselLength x ≤ b ^ (5 n)` and
`i ≤ A`. Then `‖W y‖` times the `i`-th power of `max 1 (besselLength y / b ^ (6 n))` (this is
`scaledBesselLength y b`) is at most `∫ (2 / ‖x⁻¹ s y‖) ^ (9 r ^ 2) ds`. 

### `IsBesselFunction.smul_of_invariant`

 A Bessel function `Y` for `rep` is a bounded measurable function with `Y (n y) = ψ(n) Y y` for
`n` in `besselU` and `Y (h y) = rep h (Y y)` for `h` in `U(κ)`. If such `Y` is continuous, and `a`
is a continuous real function with `|a y| ≤ K` that is left invariant under the Bessel subgroup
`besselS`, then `a • Y` is a Bessel function for `rep`. 

### `exists_enorm_sq_mul_eq`

 A finite nonzero `q` can be scaled to any natural number by the square of a real number. 

### `besselCutoff`

 The cutoff of radius `R > 0`: it is `1` up to `R / 2`, `0` from `R` on, and linear in
between. 

### `besselCut`

 The cut `F♭` of `F`: the product of `F y` with the cutoff of radius `b ^ (6 n + 2)` evaluated at
the length `besselLength y`, where `n = ϱ + 1`. 

### `enorm_besselCut_le`

 `besselCut b F y` is `F y` multiplied by a number in `[0, 1]`, so its norm is at most
`‖F y‖`. 

### `enorm_besselCut_sub_le`

 `besselCut b F y` is `F y` multiplied by a number in `[0, 1]` (a cutoff evaluated at
`besselLength y`), so it differs from `F y` by at most `‖F y‖`. 

### `inCut_of_besselCut_ne_zero`

 Where the cut of `F` is nonzero, the length is at most `b ^ (6 n + 2)` (`InCut`). 

### `lt_besselLength_of_besselCut_ne`

 Where the cut of `F` differs from `F`, the length exceeds `b ^ (6 n + 2) / 2`. 

### `IsBesselFunction.besselCut`

 The cut of a continuous Bessel function is a Bessel function, as the length is left invariant
under `besselS`. 

### `IsDecayMajorant.lintegral_sq_besselCut_sub_le`

 Let `F♭ = besselCut b F` be the product of `F : G₁ → ℂ^I` with a cutoff of the length
`besselLength` that is `1` up to `b ^ (6 n + 2) / 2`, where `n = ϱ + 1`, and let `r` be the size of
the matrices of `G₁`. Let `w ≤ a` be a decay majorant (`IsDecayMajorant`) of the pair `F`, `F♭`
(formed by `FullOrCut.select`): `‖F y‖` and `‖F♭ y‖`, each multiplied by
`max 1 (besselLength y / b ^ (6 n)) ^ (3 r ^ 3 f)`, are at most `w y`, and `a ∫ w` is at most
`b ^ (400 r ^ 2) * card I`. If `b ≥ 2`, `r ≥ 100` and `f ≠ 0`, then `‖F♭ - F‖₂ ^ 2` is at most
`b ^ (-2 r ^ 3 f) * card I`. The integrals are over 𝖴∖G₁. 

### `lintegral_besselGraph_mul_eq`

 For `t` in the Bessel subgroup `besselS`, the integral of `φ (x⁻¹ s y)` over `s` in that
subgroup does not change when `y` is replaced by `t y`, as the measure on `besselGraph` is right
invariant. 

### `exists_isDecayMajorant_besselAverage`

 Let `r` be the size of the matrices of `G₁`, `n = ϱ + 1`, and `l = 2λ` a discrete series
parameter of gap `500 r ^ 3 + A`, with entries bounded by `L` and formal degree `deg`. Let
`W = besselAverage l rep x v` be the average of its coefficient `c_λ` over the Bessel subgroup 𝖴H at
a unit vector `v` and a point `x` with `besselLength x ≤ b ^ (5 n)`. Suppose that
`b ^ m * deg * ‖W‖₂ ^ 2` is at least `besselBallVolume x` (the volume of the `s` in 𝖴H with
`‖x⁻¹ s x - 1‖ ≤ 1`), that `F = c W` has `‖F‖₂ ^ 2 = card I`, and that `b ≥ 2000`,
`r + L + 1 ≤ b ^ 4`, `m ≤ 301 r ^ 2` and `3 r ^ 3 f ≤ A`. Then `F` and its cut `F♭ = besselCut b F`
have a decay majorant (`IsDecayMajorant`): a left 𝖴H-invariant function `w ≤ a < ∞` such that
`‖F y‖` and `‖F♭ y‖`, each multiplied by `max 1 (besselLength y / b ^ (6 n)) ^ (3 r ^ 3 f)`, are at
most `w y`, and `a ∫ w ≤ b ^ (400 r ^ 2) * card I`. 

### `exists_isCutPair_besselAverage`

 The Bessel function and its cut. Fix a unitary matrix that takes the form of G₁ to the diagonal
form with signs `ε` (the instance `UnitarySignFrame 𝔰 ε`). Let `l = 2λ` be a parameter for `ε` of
gap `500 r ^ 3 + A` with entries bounded by `L`. Let `c_λ = l.dsCoeffInFrame` be its discrete series
coefficient in this frame, and `deg = l.formalDegree`. Let `rep` be a continuous unitary
representation of U(κ) on ℂ^I, where κ indexes the summand X₀. Let `W = besselAverage l rep x v` be
the average of `c_λ` over the Bessel subgroup at a unit vector `v` and a point `x` with
`besselLength x ≤ b ^ (5 n)`. Assume `deg ‖W‖₂ ^ 2` is at least `b ^ (-m)` times
`besselBallVolume x`. Suppose `b ≥ 2000`, `r + L + 1 ≤ b ^ 4`, `r ≥ 100`, `f ≠ 0`, `m ≤ 301 r ^ 2`
and `3 r ^ 3 f ≤ A`. Then a real multiple `F` of `W` is fixed by convolution with `deg * c_λ`. It
also forms a cut pair with its cut `besselCut b F`. Here `IsCutPair` means Bessel functions, the
first normalised, close in L², with a decay majorant. Here `r` is the size of the matrices of G₁,
`n = ϱ + 1` with ϱ the number of hyperbolic planes, and `‖·‖₂` is the norm of L²(𝖴∖G₁), 𝖴 the Bessel
unipotent group. 
