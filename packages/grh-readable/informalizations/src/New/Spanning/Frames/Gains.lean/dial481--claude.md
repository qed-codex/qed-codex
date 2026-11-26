---
{
  "module": "src/New/Spanning/Frames/Gains.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Frames/Gains.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Frames/Gains.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Two frames: separation and the gains at one position

A weight made of depths separates the two frames. At a fixed position the form then gains from a
frequency, from two different heads, or from a deep vector. Throughout, θ_l is `F.floorMeasure l`,
and w_p is the Weyl element `weylElem j p` of a head `p` of length `j`.

Notions from other files:
* `PlaceData.IsNear`: `g` is near at `j` if `partialUnitriangularGroup j` moves it into the box
  `F.boxSet`.
* `PlaceData.partialCorrelation`, `PlaceData.pivotL1Norm`: the correlation of a kernel from floor
  `j` on, and the integral over floor `j` (the pivot) of the modulus of the correlation from floor
  `j + 1` on.
* `PlaceData.depthWeight`, `PlaceData.weightedSquareSum`: the product of the powers depth^(-s) over
  the first `j` vectors, and the sum over the floors from `j` on of the weighted squared
  correlations.
* `Gauge.weightedSquareProduct`: the product of the second moments `F.weightedSquareIntegral` of the
  two correlations, times a constant that depends on the gauge and on the head `p`.

## Main definitions and results

* `New.Floors.Gauge.sq_lintegral_le_mul_lintegral`,
  `New.Floors.Gauge.sq_lintegral_mul_comp_weylElem_inv_le_of_section`: separating the frames, also
  with a pivot on a section.
* `New.Floors.Gauge.formIntegrandL1Norm_sq_le_of_char`: the gain from a frequency.
* `New.Floors.Gauge.partialCorrelation_mul_eq_integral_sectionPoint`,
  `New.Floors.Gauge.formIntegrandL1Norm_sq_le_of_heads`: the phase of the lifts and the gain from
  two heads.
* `New.Floors.PlaceData.IsPairingKernel.pivotL1Norm_le_sum_deepModulus`: the cut at the first deep
  vector.
* `New.Floors.Gauge.pivotL1Norm_sq_le_of_deep`,
  `New.Floors.Gauge.formMajorant_sq_le_of_hasDeepVector`,
  `New.Floors.Gauge.formMajorant_zero_sq_le_of_hasDeepVector`: the gains from a deep vector.

## Relation to the literature

See `New.Spanning.MainTerm.EnergyEstimate` for related work.


### `Gauge.sq_lintegral_le_mul_lintegral`

 **Separating the frames.** Let `p` be a head of length j ≤ ϱ with Weyl element
w_p = `weylElem j p`, let `x` be a position and `F.groupMeasure` a Haar measure. Let `B`, `B'` be
measurable, left invariant under `partialUnitriangularGroup j` and zero off the points near at `j`.
Suppose `f(g)² ≤ K · B(g) / wgt(g) · B'(w_p⁻¹ g) / wgt(w_p⁻¹ g)` where `f(g) ≠ 0`, for the weight
`wgt = F.depthWeight j · x`. Then the square of the integral of `f` against
`F.partialGroupMeasure 0 j` is at most `K · D² · ∫ B · ∫ B'`, with `B`, `B'` integrated against the
convolution of the measures of the floors below `j`. Here `D` is the product of the
`F.floorModulus a (p a)⁻¹` over a < j, times `Γ.floorsConst`. 

### `Gauge.sq_lintegral_le_weightedSquareProduct`

 The separation of the frames for the weighted squares of the two correlations ⟨W g, W y⟩ and ⟨W
g, W (w_q⁻¹ w_p y)⟩. Let `W` be a cut Bessel function, `p` a head of length j ≤ ϱ, `x` a position
and `F.groupMeasure` a Haar measure. Suppose that, where `f(g) ≠ 0`, the square f(g)² is at most
`K * Γ.floorsConst` times the two sums of weighted squares, at g and at w_p⁻¹ g, each divided by its
weight. Then the square of the integral of `f` against `F.partialGroupMeasure 0 j` is at most `K`
times `Γ.weightedSquareProduct j p q W x`, the product of the second moments
`F.weightedSquareIntegral` of the two correlations and of a constant that depends on `Γ` and `p`. 

### `PlaceData.deepModulus`

 The modulus of the correlation of the kernel `k` above floor `a` at the points `y`, `y x`, cut
to the `y` at which the vector of floor `a` has depth at least `D`. 

### `PlaceData.IsPairingKernel.measurable_deepModulus`

 For a pairing kernel `k`, the cut modulus `F.deepModulus x D k a` is measurable. 

### `PlaceData.IsPairingKernel.pivotL1Norm_le_sum_deepModulus`

 **The cut at the first deep vector.** Let `k` be a pairing kernel (`F.IsPairingKernel`), and
suppose that for each `σ` in `floorGroup l` with k(σ g, σ g x) ≠ 0 some vector from floor `l` on has
depth at least `D` at `σ g`. Then `F.pivotL1Norm l k g (g * x)`, the integral over floor `l` of the
modulus of the correlation from floor `l + 1` on, is at most a sum of pieces, one for each floor `a`
with `l ≤ a < ϱ`: the integral of `F.deepModulus x D k a` over the floors from `l` to `a`. 

### `Gauge.lintegral_deepModulus_sq_le`

 One piece of the cut. Let `Γ` be a gauge with constant Λ = `Γ.loss`, `k` a pairing kernel for
`j` and `d`, `x` a position, `l ≤ a` and `g` a point. The piece is the integral of
`F.deepModulus x ε⁻¹ k a (σ g)` in σ over the floors from `l` to `a`. Its square is at most ε^s
Λ^(10⁴ n ϱ) times the sum `F.weightedSquareSum k x l g` of the weighted squares from floor `l` on,
divided by the weight of length `l` at `g`. Here n = `𝔰.n`, and s = `F.volumeExponent` is the power
of the inverse depths in the weight `F.depthWeight`. 

### `Gauge.pivotL1Norm_sq_le_of_deep`

 **Gain from a deep vector.** Let `x` be a position and `k` a pairing kernel
(`F.IsPairingKernel`), and suppose that for each `σ` in `floorGroup l` with k(σ g, σ g x) ≠ 0 some
vector from floor `l` on has depth at least `ε⁻¹` at `σ g`. Then the square of `F.pivotL1Norm`, the
integral over floor `l` of the modulus of the correlation from floor `l + 1` on, is at most
`ε ^ F.volumeExponent` times `Γ.floorsConst` times the sum of the weighted squared correlations from
floor `l` on, divided by the weight `F.depthWeight` of length `l`. 

### `Gauge.formMajorant_sq_le_of_floorMassLe`

 One position, no gain. Let `W` be a cut Bessel function, `p` a head of length j ≤ ϱ, `q` any
sequence of units, `x` a position and `F.groupMeasure` a Haar measure. Let `V` bound the mass of
floor `j`: for every g, the τ with τ g near at j + 1 have `F.floorMeasure j`-measure at most `V`.
Then Cauchy–Schwarz on floor `j` for each of the two factors `F.pivotL1Norm` gives `F.formMajorant
j p q W x ^ 2 ≤ V ^ 2 * Γ.weightedSquareProduct j p q W x`. 

### `Gauge.formMajorant_sq_le_of_hasDeepVector`

 Let `W` be a cut Bessel function, `p` a head of length j ≤ ϱ, `q` a second sequence of units,
`x` a position and `F.groupMeasure` a Haar measure. Let `V ≥ 1` bound the mass of floor `j`: for
every g, the τ with τ g near at j + 1 have `F.floorMeasure j`-measure at most `V`. Suppose that
every active point g has a floor a ≥ j with `σ⁻¹ ≤ F.depth a g x`. Then the square of the majorant
`F.formMajorant j p q W x` of the form at `x` is at most `σ ^ F.volumeExponent * V ^ 2` times
`Γ.weightedSquareProduct`, the product of the second moments of the two correlations with its
constants. 

### `Gauge.formMajorant_sq_le`

 Let `W` be a cut Bessel function, `p` a head of length j ≤ ϱ, `x` a position, `F.groupMeasure` a
Haar measure and `V ≥ 1` a bound for the mass of floor `j`. Write w_p = `weylElem j p` and
w_q = `weylElem j q`. Suppose that, if `σ < 1`, every active point g has a floor a ≥ j with
`σ⁻¹ ≤ F.depth a g x`; g is active when ⟨W g, W (g x)⟩ ≠ 0 and w_p⁻¹ g, w_q⁻¹ g x are near at j.
Then the square of the majorant of the form at `x` is at most `σ ^ F.volumeExponent * V ^ 2` times
`Γ.weightedSquareProduct`, the product of the second moments of the two correlations with its
constants. 

### `PlaceData.formMajorant_zero_eq`

 With no head, both pivots give the same integral: the majorant of floor `0` for the heads `1`,
`1` is the square of the integral `F.pivotL1Norm` over the pivot of the kernel ⟨W y, W y'⟩ at
the points `1`, `x`. 

### `Gauge.formMajorant_zero_sq_le_of_hasDeepVector`

 One position, no head. Let `W` be a cut Bessel function and `x` a position, and take both
sequences p, q equal to the constant `1`. Suppose every active point g has a floor a with
`σ⁻¹ ≤ F.depth a g x`; at floor `0`, g is active when ⟨W g, W (g x)⟩ ≠ 0. Then
`F.formMajorant 0 1 1 W x ^ 2` is at most `(σ ^ F.volumeExponent) ^ 2` times
`Γ.weightedSquareProduct 0 1 1 W x`, the product of the second moments with its constants. 

### `Gauge.formIntegrandL1Norm_sq_le_of_char`

 Let `W` be a cut Bessel function, `p` a head of length j ≤ ϱ, `q` a second sequence of units,
`x` a position and `F.groupMeasure` a Haar measure. Let ψ be the additive character of the place,
and let ψ(ηz) = ψ(ξz) for the unit ξ and all numbers z of size 200 n² (n = `𝔰.n`) in the gauge
(`Γ.ofSize`). Weight the form by ψ(η Z_jj), where Z_jj is the diagonal entry j of the frame Gram
matrix `T.frameGram`. Then the square of its modulus `F.formIntegrandL1Norm j p q W x` is at most
`(P.kernelBound / P.modulus ξ) ^ card F.FreeIndex` times `Γ.weightedSquareProduct`, the product of
the second moments of the two correlations with its constants. 

### `Gauge.sub_one_mulVec_eStar_mem_vecsOfSize`

 Let `t₀`, `t` lie in `floorGroup (a + 1)`, and let the matrices `t₀ n₀ g` and `t n g` have size
`s` in the gauge (all their entries lie in `Γ.ofSize s`). Then the column of `t₀ n₀ (t₀ n)⁻¹ - 1` at
the basis vector `eStar a` has size `2 s + 6`. 

### `Gauge.lintegral_heisenbergMeasure_le_of_heads`

 Parseval's inequality along the last vector of two heads. Let `W` be a cut Bessel function, `p`
a head of length i + 1 ≤ ϱ, `q` a second sequence of units, and
`ξ = (1 / p_i - 1 / q_i) / F.levelUnit` a unit. On the Heisenberg group of floor `i` the characters
of the two points differ by the frequency `-ξ p_i`. Write the correlation for
`frameCorrelation W (weylRatio (i + 1) p q)`. For `n` in this group let `Φ n` vanish unless
`w_p n g` is near at `i + 1`, and be at most `C` times the squared correlation from floor `i + 1` on
at `(n g, n y)`. Then the integral of `Φ` is at most `C` times
`(P.kernelBound / P.modulus ξ) ^ card F.FreeIndex`, `F.floorModulus i (p i)⁻¹`, `Γ.floorsConst` and
the squared L² norm of the correlation on the next floor. 

### `PlaceData.invDepthWeight_weylElem_of_isNear_succ`

 At a point `g` near at `i + 1`, `F.invDepthWeight i x (weylElem i p * ((weylElem (i + 1) p)⁻¹ *
g))` equals `(F.depthWeight i g x)⁻¹`: the inverse weight of length `i` does not see the last factor
of the Weyl element of length `i + 1`. 

### `Gauge.lintegral_indicator_le_of_section`

 Let `p` be a head of length i + 1 ≤ ϱ with Weyl element w_p = `weylElem (i + 1) p`, let `x` be a
position, `F.groupMeasure` a Haar measure and `wgt_l = F.depthWeight l · x`. Let `φ` be left
invariant under `floorGroup (i + 1)`, and let `B` be left invariant under
`partialUnitriangularGroup (i + 1)` and zero off the points near at `i + 1`. Suppose that the
integral of `φ (n g)²` over the `n` in the Heisenberg group of floor `i` with `w_p n g` near at
`i + 1` is at most `C · B(g) / wgt_(i+1)(g)`. Let `u(g)` be `wgt_(i+1)(g) φ(g)²` times the inverse
depth weight of length `i` at `weylElem i p * g`, cut to the `g` with `w_p g` near. Then the
integral of `u(w_p⁻¹ g)` against `F.partialGroupMeasure 0 (i + 1)` is at most `C · ∫ B` times
`Γ.floorsConst` and the product of the `F.floorModulus a (p a)⁻¹` over a < i, with `B` integrated
against the convolution of the measures of the floors up to `i`. 

### `Gauge.sq_lintegral_mul_comp_weylElem_inv_le_of_section`

 **Separating the frames when one pivot runs over a section.** Let `p` be a head of length
i + 1 ≤ ϱ with Weyl element w_p = `weylElem (i + 1) p`, let `x` be a position and `F.groupMeasure`
a Haar measure. Let `wgt_i φ₁²` and `B` be left invariant under `partialUnitriangularGroup (i + 1)`
and `φ₂` under `floorGroup (i + 1)`, and let all three vanish off the points near at `i + 1`; here
`wgt_l = F.depthWeight l · x`. Suppose that the integral of `φ₂ (n g)²` over the `n` in the
Heisenberg group of floor `i` with `w_p n g` near at `i + 1` is at most `K` times
`F.floorModulus i (p i)⁻¹ * Γ.floorsConst` times `B(g) / wgt_(i+1)(g)`. Then the square of the
integral of `φ₁(g) φ₂(w_p⁻¹ g)` against `F.partialGroupMeasure 0 (i + 1)` is at most
`K · ∫ wgt_i φ₁² · ∫ B` times `Γ.floorsConst ^ 3` and the square of the product of the
`F.floorModulus a (p a)⁻¹` over a ≤ i. The last two integrals are against the convolution of the
measures of the floors up to `i`. 

### `Gauge.partialCorrelation_mul_eq_integral_sectionPoint`

 The phase of the lifts. Let the place datum `F` have a gauge, let `W` be a cut Bessel function,
`ξ = (1 / p_i - 1 / q_i) / F.levelUnit`, and let `n` lie in the Heisenberg group of floor `i`. Let
`y'` be the point over `n` of the section `⟨e_i, y'⟩ = star p_i`. The correlation from floor `i + 1`
on at `(n g, n g')` is the integral, over the next vector `y = σ⁻¹ e_(i+1)`, of `ψ(-ξ ⟨y', y⟩)`
times the correlation from floor `i + 2` on at `(σ g, σ g')`, which does not depend on `y'`. 

### `Gauge.lintegral_section_le`

 Plancherel's bound for a pivot on a section. Let `W` be a cut Bessel function, `p` a head of
length `i + 1` and `ξ = (1 / p_i - 1 / q_i) / F.levelUnit`. Let `φ(σ)` be the correlation from floor
`i + 2` on at `(σ g, σ g')`, let `y = orbitPoint i.succ σ`, and let `y'` be the point over `n` of
the section `⟨e_i, y'⟩ = star p_i`. Over the `n` with `w_p n g` near at `i + 1`, the squared L² norm
of `n ↦ ∫ ψ(-ξ ⟨y', y⟩) φ(σ) dθ_(i+1)(σ)` is at most
`(P.kernelBound / P.modulus ξ) ^ card F.FreeIndex` times `F.floorModulus i (p i)⁻¹ * Γ.floorsConst`
times that of `φ`. 

### `Gauge.formIntegrandL1Norm_sq_le_of_heads`

 Let `W` be a cut Bessel function, `p` a head of length j = i + 1 ≤ ϱ, `q` a second sequence of
units, `x` a position and `F.groupMeasure` a Haar measure, and let
`ξ = (1 / p_i - 1 / q_i) / F.levelUnit` be a unit. Then the square of the L¹ norm
`F.formIntegrandL1Norm j p q W x 1` of the form integrand with weight `1` at `x` is at most
`(P.kernelBound / P.modulus ξ) ^ card F.FreeIndex` times `Γ.weightedSquareProduct j p q W x`, the
product of the second moments of the two correlations with `Γ.floorsConst ^ 3` and the squares of
the `F.floorModulus a (p a)⁻¹` over a < j. 
