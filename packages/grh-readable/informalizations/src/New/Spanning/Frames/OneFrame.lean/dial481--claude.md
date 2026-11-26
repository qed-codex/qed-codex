---
{
  "module": "src/New/Spanning/Frames/OneFrame.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Frames/OneFrame.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Frames/OneFrame.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# One frame

After Cauchy–Schwarz each frame is paired with itself. The square of a partial correlation is
integrated over the position ball along the Heisenberg groups of the frame: a step below the pivot
uses up a weight, a step above it adds a vector by Parseval's formula. The letters G^(l), R^(l),
U_(<l), Y^(l) are those of the head of `New.Spanning.Frames.Lengths`, and K, M those of
`New.Spanning.Frames.Levels`.

## Main definitions and results

* `New.Floors.PlaceData.IsPairingKernel.pivotL1Norm_sq_le`: Cauchy–Schwarz for a pivot whose range
  has small mass.
* `New.Floors.Gauge.lintegral_cutSquare_le`: one step above the pivot.
* `New.Floors.Gauge.lintegral_weightedSquare_le`,
  `New.Floors.Gauge.lintegral_weightedSquareIntegral_le`: the bound for one frame.
* `New.Floors.Gauge.headDensity_mul_lintegral_le_mul_pairingNormSq`: a gain on the position ball
  survives the integration.

Notions from other files:
* `F.floorMeasure l`, written θ_l: the measure of floor l, carried by G^(l) = `floorGroup l`;
  `descConv F.floorMeasure l i` is the convolution θ_{l+i−1} ∗ ⋯ ∗ θ_l.
* `F.IsPairingKernel j k d`: the rules of a correlation k(g, y) = ⟪W g, W (d y)⟫ of a Bessel
  function W, where d commutes with G^(j); `F.partialCorrelation l k`, written k_l, is the average
  of k over the floors from l on.
* `F.depthWeight l g x`, written ℘_l(g, gx): the product of negative powers of the depths of the
  first l frame vectors; `F.weightedSquare l k x g` is ℘_l(g, gx)·|k_{l+1}(g, gx)|².
* `F.weightedSquareSum k x l`, written 𝖻_l: the sum of the integrated weighted squares over the
  floors from l on; `F.weightedSquareIntegral l k x` is its integral over the floors below l.
* `F.IsNear l g`: the coset R^(l) g meets `F.boxSet`, where R^(l) = `partialUnitriangularGroup l`.


 ### Estimates for pairing kernels 

### `exists_ne_zero_of_pivotL1Norm_ne_zero`

 If `F.pivotL1Norm l k g y`, the θ_l-integral of |k_{l+1}(σg, σy)|, is not zero, then
k(xg, xy) ≠ 0 for some x in G^(l) = `floorGroup l`. 

### `lintegral_partialCorrelation_sq_le`

 For `l ≤ 𝔰.ϱ`, the integral over σ against θ_l = `F.floorMeasure l` of the squared modulus of
the correlation `F.partialCorrelation (l + 1) k` from floor l + 1 on, taken at (σ g, σ (g x)), is at
most `F.weightedSquareSum k x l g` divided by `F.depthWeight l g x`. 

 ### Weighted squares and their sums over the floors 

### `measurable_weightedSquareSum`

 For a pairing kernel `k` at any floor `j`, the sum `F.weightedSquareSum k x l g` of the weighted
squares over the floors from `l` on is jointly measurable in the points `x` and `g` of the group. 

### `fixesLeft_weightedSquare_and_eq_zero`

 Let `k` be a pairing kernel at floor `j`: it obeys the rules of a correlation ⟪W g, W (d y)⟫,
with `d` commuting with `floorGroup j`. Consider the weighted square `F.weightedSquare j k x`. It is
left invariant under R^(j+1) = `partialUnitriangularGroup (j + 1)`. It vanishes at the points g that
are not near at `j + 1`. 

### `fixesLeft_weightedSquareSum_and_eq_zero`

 Let `k` be a pairing kernel at floor `j`: it obeys the rules of a correlation ⟪W g, W (d y)⟫,
`d` commuting with `floorGroup j`. The sum 𝖻_j = `F.weightedSquareSum k x j` of the integrated
weighted squares of `k` over the floors from `j` on is left invariant under
R^(j) = `partialUnitriangularGroup j` and vanishes at the points g that are not near at `j`. 

### `pivotL1Norm_sq_le`

 Cauchy–Schwarz on floor `l` for a pairing kernel `k`. Suppose that for every point z the
θ_l-integral of u(σz) over the σ with σz near at `l + 1` is at most `K`, and that ‖k_{l+1}(σg,
σy)‖² ≤ u(σg)·v(σ) for σ in `floorGroup l`, with `u` and `v` measurable. Then the square of
`F.pivotL1Norm l k g y`, the θ_l-integral of ‖k_{l+1}(σg, σy)‖, is at most `K` times the
θ_l-integral of `v`. 

### `pivotL1Norm_sq_le_of_floorMassLe_one`

 Cauchy–Schwarz on floor `l` for a pairing kernel `k`, without a weight: if for every `g` the σ
with σ g near at `l + 1` have θ_l-mass at most `K` (`F.FloorMassLe l K 1`), where
θ_l = `F.floorMeasure l`, then the square of `F.pivotL1Norm l k g y` is at most `K` times the
θ_l-integral of ‖`F.partialCorrelation (l + 1) k (σ * g) (σ * y)`‖². 

### `weightedSquareIntegral_eq_add_succ`

 Let `k` be a pairing kernel at any floor `j`, and let `l ≤ 𝔰.ϱ`. Then
`F.weightedSquareIntegral l k x`, the integral of `F.weightedSquareSum k x l` against θ_{l−1} ∗ ⋯ ∗
θ₀, is the integral of the weighted square `F.weightedSquare l k x` against θ_l ∗ ⋯ ∗ θ₀ plus
`F.weightedSquareIntegral (l + 1) k x`. 

### `weightedSquareIntegral_le_weightedSquareIntegral_zero`

 For a pairing kernel `k` and `l ≤ 𝔰.n`, `F.weightedSquareIntegral l k x`, the integrated sum of
the weighted squared correlations from floor `l` on, is at most `F.weightedSquareIntegral 0 k x`,
the same quantity taken over all floors. 

 ### Integrals of inverse depth weights and weighted squares over several floors 

### `Gauge.lintegral_invDepthWeight_floorMeasure_le`

 Deep vectors are rare, one floor. Let `Γ` be a gauge for the data `F` of a place, with constant
Λ = `Γ.loss`, let n = `𝔰.n` = ϱ + 1 be the number of floors, each with its measure
`F.floorMeasure a`, and let `x` lie in `F.positions`. The inverse depth weight
`F.invDepthWeight (a + 1) x` at `σ g` has integral over the `σ` of floor `a` at most Λ^(10⁴ n) times
the inverse depth weight of length `a` at `g`. 

### `Gauge.lintegral_invDepthWeight_descConv_le`

 Deep vectors are rare, several floors. Let `Γ` be a gauge for the place datum `F`, with constant
Λ = `Γ.loss`, let n = `𝔰.n` and `l + i ≤ ϱ`, and let `x` lie in `F.positions`. The inverse depth
weight of length `l + i` at `σ g` has integral over the `σ` in the `i` floors from `l` on at most
Λ^(10⁴ n i) times the inverse depth weight of length `l` at `g`. 

### `PlaceData.IsPairingKernel.lintegral_weightedSquare_le_weightedSquareSum`

 Let `k` be a pairing kernel at any floor `j`, `x` any point of the group and `l + i ≤ ϱ`. The
weighted square of floor `l + i`, taken at the pair `σ g`, `σ g x`, has integral over `σ` against
the convolution of the measures of the floors from `l` to `l + i` at most
`F.weightedSquareSum k x l g`, of which it is one term once the recursion is unfolded. 

### `lintegral_weightedSquareIntegral_le_of_lintegral_le`

 Let μ be a measure on the group, in the variable x, let j ≤ ϱ and let k be a pairing kernel at
floor j. If for every floor l with `j ≤ l ≤ 𝔰.ϱ` the integral of the weighted square of floor l,
over g against the convolution θ_l ∗ ⋯ ∗ θ₀ of the floor measures and over x against μ, is at most
`c`, then the weighted square integral `F.weightedSquareIntegral j k x` has μ-integral at most
`𝔰.n * c`. 

 ### The bound for one frame 

### `PlaceData.IsPairingKernel.enorm_partialCorrelation_mul_of_mem_unipotentBelow`

 For a pairing kernel `k`, the modulus of the correlation `F.partialCorrelation (l + 1) k` above
floor `l` does not change when its second point is multiplied on the left by an element `n` of
`unipotentBelow l`, the unipotent group of the first `l` floors. 

### `Gauge.closeMass`

 The measure of the `ν` in the unipotent group of the first `l` floors for which `g⁻¹ ν y` lies
in the position ball. 

### `Gauge.cutSquare`

 The squared modulus of the correlation above floor `l`, cut to the pairs `(g, y)` for which the
positions `g⁻¹ ν y` in the position ball have positive measure: `∞ * m` is `0` for `m = 0` and `∞`
otherwise, so the minimum is `0` or the square. Such a `y` lies in `Γ.closeBelow l g`; the cut takes
the place of the indicator of that set because it is measurable in the pair. 

### `Gauge.climbConst`

 The cost of one step up from floor `l`: `Γ.floorConst l` below the top floor, and `1` on the top
floor, where only the group H is left, of mass at most `1` on near points. 

### `Gauge.closeMass_mul_mul`

 If translating the Haar measure of the unipotent group of the first `l` floors by `σ` on the
left is the same as translating it by `t` on the right, then moving `g`, `y` to `σ g`, `t y` does
not change the mass of the position ball. 

### `Gauge.measurable_cutSquare`

 For a pairing kernel `k`, the cut square of floor `l` is jointly measurable in its two
points. 

### `Gauge.exists_centre_of_isNear`

 Let `g` be near at `a + 1`. Let `n₀` lie in the Heisenberg group `floorUnipotent a` and `ν₀` in
`unipotentBelow a`, and let `g⁻¹ ν₀ n₀ y` lie in the position ball `Γ.positionsOfSize`. Then there
are `t` in `partialUnitriangularGroup (a + 1) ⊓ floorGroup a` and `ν` in `unipotentBelow (a + 1)`
with two properties. First, the matrix `t ν g` has size 1 for the gauge `Γ`. Second, for each `n` in
the Heisenberg group with `n y` in `Γ.closeBelow a g`, some vector `v` differs from (t n₀ (t n)⁻¹ -
1) e*_a by a combination of the e_b, b < a (`CongrBelow`), and has size 17 after division by the
level unit `F.levelUnit`. 

### `Gauge.lintegral_cutSquare_le`

 One floor up. Let `Γ` be a gauge (size bounds for the place data `F`), `k` a pairing kernel for
`F` whose twist `d` commutes with G^(j) = `floorGroup j`, and `j ≤ l ≤ ϱ`. The cut square
`Γ.cutSquare k l g y` is the squared modulus of the correlation `k` above floor `l`. It is set to
zero where the positions of `(g, y)` in the position ball have measure zero. Its integral over `n`
against `heisenbergMeasure l`, taken at `(g, n * y)`, is at most the step cost `Γ.climbConst l`
times the integral of `Γ.cutSquare k (l + 1)` at `(σ * g, σ * y)` against `F.floorMeasure (l + 1)`.
Below the top floor this is Parseval's formula; on the top floor it is Cauchy–Schwarz on
H = `T.besselH`. 

### `Gauge.exists_factor_cutSquare_le`

 All floors above `l`. Let `k` be a pairing kernel at floor `j` and `j ≤ l ≤ ϱ + 1`. The Haar
measure `F.groupMeasure` factors as the convolution of `ascConv heisenbergMeasure l`, the measure of
the unipotent group of the first `l` floors, with an s-finite measure `ρ`; and the integral of the
cut square against `ρ` and the floors up to `l`, times the costs of the floors below `l`, is at most
the product of all costs times the squared L² norm of the kernel.

The factorization is a form of Weil's quotient integral formula for the unipotent group of the
first `l` floors, with an s-finite measure `ρ` on the group in place of the invariant measure on
cosets. 

### `Gauge.lintegral_weightedSquare_le`

 One frame, one pivot. Let `k` be a pairing kernel at floor `j` and `j ≤ l ≤ ϱ`. Over the
position ball `Γ.positionsOfSize`, the squared modulus of the correlation above floor `l`, weighted
by `F.depthWeight l`, has integral at most the product of the costs `Γ.floorConst` of the floors
times the squared L² norm of the kernel. 

### `Gauge.lintegral_weightedSquareIntegral_le`

 **One frame.** Let `k` be a pairing kernel at floor `j ≤ ϱ`. Over the position ball
`Γ.positionsOfSize`, the integral of `F.weightedSquareIntegral j k` for `F.groupMeasure` is at most
`𝔰.n` = ϱ + 1 times the product of the costs `Γ.floorConst l`, l < ϱ, times the squared L² norm of
`k` for `F.quotientMeasureFrom 0` in each variable. 

### `PlaceData.headDensity_sq_mul_eq_modulus`

 Let `p`, `q` be sequences of units of the ring `A` of the place `P`, with modulus |·|, let
`j ≤ ϱ` and r_a = `𝔰.k + 1 + 2 * (𝔰.ϱ - (a + 1))`. In the product over a < j of |p_a q_a|^(r_a) (the
squared `F.headDensity`), |p_a|^(-(2 r_a + 1)) (the squared `F.floorModulus`) and
|p_a / q_a|^(r_a + 1), the powers of |p_a| cancel and |q_0 ⋯ q_(j-1)|⁻¹ is left. 

### `Gauge.headDensity_mul_lintegral_le_mul_pairingNormSq`

 Let `W` be a cut Bessel function, j ≤ ϱ, 𝖬 = `F.groupMeasure` a Haar measure, `p` any sequence
of units, `q` a head of length `j` for the gauge `Γ`, and `S` a subset of the position ball of the
gauge `Γ'`. Let `f` have the gain `e` on `S`: f(x)² is at most e² times
`Γ.weightedSquareProduct j p q W x`, the product of the two second moments at x with its constants.
Then `F.headDensity j p q` times ∫_S f d𝖬 is at most e times the squared norm `F.pairingNormSq W` of
the correlation, times the product over l < ϱ of the `F.floorModulus l`,
`P.kernelBound ^ (card F.FreeIndex * 𝔰.ϱ)`, Λ^(1500000 n³ + 1) and Λ'^(25000 n²), where
Λ = `Γ.loss`, Λ' = `Γ'.loss` and n = ϱ + 1. 
