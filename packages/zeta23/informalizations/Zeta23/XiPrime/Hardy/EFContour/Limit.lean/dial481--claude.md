---
{
  "module": "Zeta23/XiPrime/Hardy/EFContour/Limit.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/XiPrime/Hardy/EFContour/Limit.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/XiPrime/Hardy/EFContour/Limit.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/

/-
The R → ∞ passage of the explicit-formula contour argument,
generic in the integrand.

The integrand 'logDeriv f' of an entire f replaced by an arbitrary F : ℂ → ℂ and the rectangle values replaced by a
given convergent sequence E_j → L: fold of the two verticals by the odd symmetry F(1−s) = −F(s) on the
line, vanishing of the horizontals from ‖H‖ ≤ C_H/(1+R²) (WeilEF.norm_Hfn_le) and an O(log²) bound for
F at the heights R_j ∈ [j+j₀, j+j₀+1], truncated → full integral by dominated convergence, and
uniqueness of limits.  Nothing about zeros, poles or good heights lives here (they enter only through
hE / hlim / hhor).
-/
```

### `FlineF`

 the full-line integrand against an abstract F:  [H(c+it) + H(1−c−it)] · F(c+it). 

 ## Integrability of the full-line integrand 

### `integrable_FlineF_of`

 **Integrability** of FlineF from continuity + a log bound for F on Re s = c (−1 ≤ c ≤ 2). 

 ## The vertical sides 

### `verticals_eq_F`

 Folding the left vertical side onto the right one by  F(1−s) = −F(s) on the line:
V(c; −R, R) − V(1−c; −R, R) = I • ∫_{−R}^{R} FlineF. 

 ## The horizontal sides 

### `horizontal_vanish_F`

 **Horizontal sides vanish**: ‖H‖ ≤ C_H/(1+R_j²) on the segment and ‖F‖ ≤ K log²(j+j₀+3) there,
R_j ≥ j + j₀ ≥ 1, so  ‖HIntegral‖ ≤ (2c−1)·C_H·K·log²/(1+R_j²) → 0. 

 ## Assembly 

### `full_line_of_rectangles`

 **Generic passage to the full line.**  If the normalised rectangle integrals of H·F over
[1−c, c] × [−R_j, R_j] have known values E_j → L, F is continuous with log growth on Re s = c, odd under
s ↦ 1−s between the two vertical lines, and O(log²) on the horizontal segments at the heights R_j ∈ [j+j₀, j+j₀+1],
then the full-line integral exists and (1/2π)∫[H(c+it)+H(1−c−it)]F(c+it)dt = L. 
