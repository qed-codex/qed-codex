---
{
  "module": "Zeta23/XiPrime/ExplicitFormula/FullLine.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/XiPrime/ExplicitFormula/FullLine.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/XiPrime/ExplicitFormula/FullLine.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/

/-
Zeta23/XiPrime/ExplicitFormula/FullLine.lean — (EF1) the R → ∞ limit, GENERIC in the function f.

For an ENTIRE f with: logDeriv f (1−s) = −logDeriv f s; all zeros in 1−c < Re s < c; good heights
R_j ∈ [j+j₀, j+j₀+1] with f ≠ 0 and ‖f′/f‖ ≤ C log²(j+j₀+3) on Im s = ±R_j, 1−c ≤ Re ≤ c; and a line
bound ‖f′/f(c+it)‖ ≤ M log(2+|t|), the rectangle identity (Contour.lean) passes to the limit:
    (1/2π) ∫ [H(c+it) + H(1−c−it)] · f′/f(c+it) dt = Σ'_ρ ord_ρ(f) · H(ρ)      (H = WeilEF.Hfn k),
the horizontal sides vanishing (‖H‖ ≤ C_H/(1+R²) on −1 ≤ Re ≤ 2, WeilEF.norm_Hfn_le), the left vertical
folding onto the right one by the symmetry, and the finite zero sums exhausting the (assumed absolutely
convergent) tsum.  Pattern: Zeta23/WeilEF/{FullLine,Horizontal,ZeroSumLimit,FullLineAssembly}.lean.
Instances (§ Instances): f = s(s−1) → rational_line;  f = ξ′ → (EF1) full_line_identity.
-/
```

 ## Generic majorants 

### `Fline`

 the full-line integrand  F_f(t) := [H(c+it) + H(1−c−it)] · f′/f(c+it). 

### `continuous_weight`

 the two-sided weight t ↦ H(c+it) + H(1−c−it) is continuous. 

### `norm_weight_le`

 the two-sided weight decays like 1/(1+t²) when −1 ≤ 1−c and c ≤ 2. 

### `continuous_logDeriv_line`

 f′/f is continuous along a vertical line on which f (entire) does not vanish. 

### `integrable_decay_mul_log`

 generic: (continuous, ≤ C/(1+t²)) × (continuous, ≤ M log(2+|t|)) is integrable on ℝ. 

### `ne_zero_on_line`

 points of the line Re s = c are not zeros of f. 

### `integrable_Fline_of`

 **Integrability of the full-line integrand** from the line bound. 

### `tendsto_intervalIntegral_of_integrable`

 the truncated integrals of an integrable F converge to ∫ F along any R_j ≥ j. 

 ## The vertical sides 

### `verticals_eq_of`

 Folding the left vertical side onto the right one by  f′/f(1−s) = −f′/f(s):
V(c; −R, R) − V(1−c; −R, R) = I • ∫_{−R}^{R} F_f. 

 ## Good heights, re-indexed 

### `exists_heights_of`

 from "∀ j ≥ j₀ ∃ R ∈ [j, j+1] …" to a height SEQUENCE R_j ∈ [j+j₀, j+j₀+1], j₀ ≥ 1, with the
log²-bound written in terms of j. 

 ## The horizontal sides 

### `horizontal_vanish_of`

 **Horizontal sides vanish**: ‖H‖ ≤ C_H/(1+R_j²) on the segment and ‖f′/f‖ ≤ K log²(j+j₀+3) there,
R_j ≥ j + j₀ ≥ 1, so  ‖HIntegral‖ ≤ (2c−1)·C_H·K·log²/(1+R_j²) → 0. 

 ## The zero side 

### `zero_sum_limit_of`

 **Zero-sum limit**: finite sums over the windows {|Im ρ| < R_j} ∩ Zset (R increasing to ∞)
converge to the tsum of an absolutely convergent g over Zset. 

 ## Assembly 

### `full_line_identity_of`

 **Generic full-line identity.**  f entire, logDeriv f (1−s) = −logDeriv f s, all zeros of f
(the set Zset) in the open strip 1−c < Re < c (1/2 < c ≤ 2), good heights with a log² bound for f′/f on
the horizontal segments, a log bound for f′/f on Re s = c, and absolute convergence of the zero sum.
Then  (1/2π) ∫ [H(c+it) + H(1−c−it)]·f′/f(c+it) dt = Σ'_{ρ ∈ Zset} ord_ρ(f)·H(ρ). 

 ## Instances 

 ### f = s(s−1): the rational piece of (EF2)  (logDeriv = 1/s + 1/(s−1), zeros 0, 1, simple) 

### `mulSubOne`

 the polynomial s(s−1). 

### `norm_logDeriv_mulSubOne_le`

 ‖1/s + 1/(s−1)‖ ≤ 2/|Im s| off the real axis. 

### `mulSubOne_good_heights`

 good heights for s(s−1): R_j = j (j ≥ 2), ‖1/s + 1/(s−1)‖ ≤ 1 ≤ log²(j+3). 

### `logDeriv_mulSubOne_line`

 on Re s = c > 1:  logDeriv (s(s−1)) = 1/s + 1/(s−1), bounded by 1 + 1/(c−1). 

### `rational_line_inst`

 The rational-line identity (cf. `rational_line`), as the f = s(s−1)
instance of full_line_identity_of:  (1/2π)∫[H(c+it)+H(1−c−it)]·(1/(c+it) + 1/(c+it−1)) dt = H(0) + H(1). 

 ### f = ξ′: (EF1) [XF′ Prop. 4.1] 

### `full_line_identity_gen`

 **(EF1) on a general line Re s = c ∈ (1, 3/2]**, conditional on (F2), with the line bound
‖ξ″/ξ′(c+it)‖ ≤ M log(2+|t|) as an explicit hypothesis (in tree only for c = 5/4:
LineBound.norm_logDeriv_xiDeriv_line).  Good heights: ZeroCount.xiDeriv_good_heights;
absolute convergence: WeilEF.EF_zero_sum_summable_gen plus the local zero count. 

### `full_line_identity`

 **(EF1) The full-line identity for ξ″/ξ′** [XF′ Prop. 4.1] on the line Re s = 5/4,
conditional on (F2) only:  Σ'_{ξ′(ρ)=0} m_ρ H(ρ) converges absolutely and equals
(1/2π) ∫ [H(5/4+it) + H(−1/4−it)]·ξ″/ξ′(5/4+it) dt.  No pole terms: ξ′ is entire. 
