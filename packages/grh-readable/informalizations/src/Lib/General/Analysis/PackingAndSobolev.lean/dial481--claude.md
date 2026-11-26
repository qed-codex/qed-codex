---
{
  "module": "src/Lib/General/Analysis/PackingAndSobolev.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/General/Analysis/PackingAndSobolev.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/General/Analysis/PackingAndSobolev.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Packing bounds for separated points and Sobolev trace inequalities
The first results count and sum over points `f i` of a finite-dimensional real normed space `V` at
mutual distance at least `m > 0`. Here `d = finrank ℝ V`. The remaining results bound the value of a
function at a point by `L²` norms of the function and of its derivatives, first on an interval and
then at the corner of a cube.

## Main definitions and results

* `New.encard_le_of_separated`: at most `(1 + 2R/m)^d` such points lie in the ball `‖x‖ ≤ R`,
  where `R ≥ 0`, by comparing volumes.
* `New.tsum_le_of_separated`: if `u i ≥ 1`, `‖f i‖ ≤ R * u i`, `R ≥ 0`, `d < A` and
  `A ≤ c (A - d)`, then `∑ u i ^ (-A) ≤ (1 + 2R/m)^d * c`, by the layer bound
  `New.DiscreteSeries.integral_rpow_neg_le_of_measure_le`.
* `New.tsum_inv_pow_le_of_separated`: if the points satisfy `‖f i‖ ≥ m` and `n ≥ d + 2`, then
  `∑ ‖f i‖⁻¹ ^ n ≤ (5/m)^n`.
* `New.sobolev_trace`: if `‖g'‖ ≤ b` pointwise on `[0, ε]`, where `0 < ε ≤ 1`, then
  `‖g 0‖² ≤ ∫₀^ε (2/ε) (‖g‖² + b²)`.
* `New.sobolev_trace_cube`: its iteration over the coordinates of a cube `[0, ε] ^ D` and a
  parameter space, for functions `f i` indexed by the words `i` in a finite alphabet, where the
  norms of the partial derivatives of `f i` are bounded by `Λ ∑ l, ‖f (l :: i)‖`, the sum over the
  letters `l`.


 ## Packing bounds and sums over separated points 

### `encard_le_of_separated`

 Packing bound: in a finite-dimensional real normed space `V`, if the points `f i`, for `i` in
`S`, have pairwise distances at least `m > 0` and norms at most `R`, with `R ≥ 0`, then `S` has
at most `(1 + 2R/m) ^ finrank ℝ V` elements. 

### `tsum_le_of_separated`

 Let points `f i` of a real normed space of finite dimension `d` have mutual distances at least
`m > 0`, with `‖f i‖ ≤ R * u i`, `u i ≥ 1` and `R ≥ 0`. If `A > d` and `A ≤ c (A - d)`, then
`∑ u i ^ (-A)` converges and is at most `(1 + 2R/m) ^ d * c`. 

### `tsum_inv_pow_le_of_separated`

 Let points `f i` of a real normed space of finite dimension `d` have norms and mutual
distances at least `m > 0`. For a natural number `n ≥ d + 2`, `∑ ‖f i‖⁻¹ ^ n` converges and is
at most `(5/m) ^ n`. 

 ## Sobolev trace inequality on an interval and at the corner of a cube 

### `New.sobolev_trace`

 One-dimensional Sobolev trace inequality: let `g` take values in a real inner product space,
let `0 < ε ≤ 1`, and suppose that at every `t ∈ [0, ε]` it has a derivative of norm at most `b t`.
Then `‖g 0‖² ≤ ∫₀^ε (2/ε) (‖g t‖² + (b t)²) dt`. 

### `New.lintegral_sobolev_trace`

 The trace inequality integrated over a parameter `ω` with a measure `σ`: let `g t ω` and the
`h l t ω`, for `l` in a finite type `L`, take values in `ℂ ^ I` and be measurable in `(t, ω)`, let
`0 < ε ≤ 1`, and suppose that, for almost all `ω`, the function `t ↦ g t ω` has at every point `t`
of `[0, ε]` a derivative of norm at most `Λ ∑ l, ‖h l t ω‖`. Then
`∫ ‖g 0 ω‖² dω ≤ ∫₀^ε (2/ε) (∫ ‖g t ω‖² dω + |L| Λ² ∑ l, ∫ ‖h l t ω‖² dω) dt`. 

### `New.sobolev_trace_cube`

 Sobolev trace at the corner of a cube. Let `D` and `L` be finite types and, for every word
(list) `i` in the alphabet `L`, let `f i x ω` be measurable in `x ∈ ℝ ^ D` and a parameter `ω`.
Let `0 < ε ≤ 1`. Assume that for almost all `ω` every partial derivative of `f i` on the cube
`[0, ε] ^ D` exists and has norm at most `Λ ∑ l, ‖f (l :: i)‖` (here `update x d t` is the point
`x` with its coordinate `d` changed to `t`), and that the integral of `‖f i‖²` over the cube and
`ω` is at most `K` for all words `i` of length at most `|D|`. Then, for the empty word `[]`,
`∫ ‖f [] 0 ω‖² dω ≤ (2 (1 + (|L| Λ)²) / ε) ^ |D| * K`. 
