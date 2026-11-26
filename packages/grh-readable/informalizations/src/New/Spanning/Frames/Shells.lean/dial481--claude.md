---
{
  "module": "src/New/Spanning/Frames/Shells.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Frames/Shells.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Frames/Shells.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The sum over the shells

The positions are cut into shells by their height. On one shell the bound for one frame loses a
power of the height. Below a threshold this loss is affordable. Above it every position has a deep
vector, whose gain pays for the loss. The argument is the same at a real place and at the finite
places; the shells that are summed have the powers of 2 as heights.

Notions from other files:
* A `PlaceData` `F` at the place is its data: a unit `F.levelUnit`, the positions, a compact box and
  measures.
* A gauge `Γ` is a notion of size at the place, with a scale `Γ.loss ≥ 2` that bounds volumes.
* `F.formMajorant` is the integral of the moduli of the two correlations of `W` at a position, and
  `Γ.weightedSquareProduct` is the product of their second moments, with a constant.
* `F.FloorMassLe j V 1` says that the mass of floor `j` near the next floor is at most `V`.

Contents of this file:
* `New.Floors.Gauge.IsShell`: a set of positions with a finite height at least 1. It is covered by
  few position balls (`New.Floors.Gauge.positionsOfSize`, each for its own gauge).
* `New.Floors.Gauge.IsShell.setLIntegral_le`: one shell.
* `New.Floors.Gauge.IsShell.setLIntegral_formMajorant_le`: the gain on a remote shell.
* `New.Floors.Gauge.IsShell.setLIntegral_le_inv_height`: a few factors of the gain pay for the
  growth in the height.
* `New.Floors.Gauge.lintegral_le_of_shells`: the sum over the shells. The integral over a shell is
  at most a common bound times the inverse of the height, and `∑ 2⁻¹ ^ i = 2`.


### `PlaceData.shellNormalization`

 The unit in which integrals over positions are measured: the product of the moduli
`F.floorModulus l` of the level `F.levelUnit` on the Heisenberg groups (at finite places the volume
of the congruence subgroup of the unipotent group), times a power of the constant `P.kernelBound` of
Plancherel's formula, times the squared `L²` norm `F.pairingNormSq W` of the correlation of `W`. 

### `Gauge.IsShell`

 For a gauge `Γ`, heads `p`, `q` of length `j` and the function `W`, a set `S` is a shell of the
given finite height at least 1 if it is covered by few position balls, and if a large height forces
a deep vector at each of its points. 

### `Gauge.IsShell.one_le_height`

 The height is at least 1. 

### `Gauge.IsShell.height_ne_top`

 The height is finite. 

### `Gauge.IsShell.exists_cover`

 `S` is covered by few position balls: for `x` in `S` the matrix `(x - 1) / F.levelUnit` has
  size 1 in the sense of one of at most `2 height ^ (9 n)` gauges `Γ'`, that is, `x` is in
  `Γ'.positionsOfSize`, and the scales `Γ'.loss` are at most `Γ.loss height²`. 

### `Gauge.IsShell.hasDeepVector`

 Far means deep: if `σ < 1` and `Γ.loss ^ (1200 n²) ≤ σ^(400 n²) height`, every active point
  has a vector of depth at least `σ⁻²` after the head. 

### `Gauge.IsShell.subset_positions`

 A shell lies in the set `F.positions` of positions of the level. 

### `Gauge.IsShell.inv_height_mul_height`

 The height of a shell is finite and not zero, so it cancels against its inverse. 

### `Gauge.IsShell.setLIntegral_le`

 Let `S ⊆ T.G` be a shell of height `height` for the gauge `Γ` and the sequences of units `p`,
`q`. Let `j ≤ 𝔰.ϱ`, and let `W` be a cut Bessel function (`F.IsCut W`). Only `q` is assumed to be a
head of length `j` for `Γ`. Suppose `f` has the gain `e` at each `x ∈ S`, that is, `f x ^ 2 ≤ e ^
2 * Γ.weightedSquareProduct j p q W x`. Then `F.headDensity j p q` times the integral of `f` over
`S` is at most `e * Γ.loss ^ (2 * 10 ^ 6 * 𝔰.n ^ 3) * height ^ (10 ^ 5 * 𝔰.n ^ 2) *
F.shellNormalization W`. 

### `Gauge.IsShell.setLIntegral_formMajorant_le`

 Let `S` be a shell of height `height` for the gauge `Γ` and `p`, `q`. Let `j ≤ 𝔰.ϱ`, and let
`p`, `q` be heads of length `j` (`Γ.IsHead`). Let `W` be a cut Bessel function (`F.IsCut W`), and
let `V ≥ 1` with `F.FloorMassLe j V 1`. Let `height > Γ.loss ^ (2400 * 𝔰.n ^ 2)`, and let
`τ ^ (800 * 𝔰.n ^ 2) = height⁻¹`. Then `F.headDensity j p q` times the integral of
`F.formMajorant j p q W` over `S` is at most `V * τ ^ F.volumeExponent * Γ.loss ^ (2 * 10 ^ 6 * 𝔰.n
^ 3) * height ^ (10 ^ 5 * 𝔰.n ^ 2) * F.shellNormalization W`. 

### `Gauge.IsShell.setLIntegral_le_inv_height`

 Let `S` be a shell of height `height` for `Γ` and `p`, `q`. Let `j ≤ 𝔰.ϱ`, and let `p`, `q` be
heads of length `j` (`Γ.IsHead`). Let `W` be a cut Bessel function (`F.IsCut W`), and let `V ≥ 1`
with `F.FloorMassLe j V 1`. Suppose `f x ≤ F.formMajorant j p q W x` for all `x`, and `f x ^
2 ≤ (V * e ^ F.volumeExponent) ^ 2 * Γ.weightedSquareProduct j p q W x` on `S`. Suppose also `e ≤ 1`
and `9 * 10 ^ 7 * 𝔰.n ^ 4 + r ≤ F.volumeExponent`. Then `F.headDensity j p q` times the integral of
`f` over `S` is at most `height⁻¹ * (V * e ^ r * Γ.loss ^ (3 * 10 ^ 8 * 𝔰.n ^ 4) *
F.shellNormalization W)`. 

### `Gauge.lintegral_le_of_shells`

 **The sum over the shells.** Let each `S i` be a shell of height `2 ^ i` for the gauge `Γ` and
`p`, `q`. Let the `S i` cover the support of `f`. Let `j ≤ 𝔰.ϱ`, and let `p`, `q` be heads of length
`j` (`Γ.IsHead`). Let `W` be a cut Bessel function (`F.IsCut W`), and let `V ≥ 1` with
`F.FloorMassLe j V 1`. Suppose `f x ≤ F.formMajorant j p q W x` for all `x`. Suppose also that if
`e < 1`, then `f x ^ 2 ≤ (V * e ^ F.volumeExponent) ^ 2 * Γ.weightedSquareProduct j p q W x` for
`x ∈ F.positions`. Let `9 * 10 ^ 7 * 𝔰.n ^ 4 + r ≤ F.volumeExponent`. Then `F.headDensity j p q`
times the integral of `f` over `T.G` is at most `V * min 1 e ^ r * Γ.loss ^ (4 * 10 ^ 8 * 𝔰.n ^ 4) *
F.shellNormalization W`. 
