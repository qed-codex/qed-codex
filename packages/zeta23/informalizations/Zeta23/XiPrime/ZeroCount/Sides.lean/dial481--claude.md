---
{
  "module": "Zeta23/XiPrime/ZeroCount/Sides.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/XiPrime/ZeroCount/Sides.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/XiPrime/ZeroCount/Sides.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/

/-
Zeta23/XiPrime/ZeroCount/Sides.lean — the Y′/Y pieces of the half-contour are O(log T).

  * horizontal_bound : at a good height T with |T| ≥ t₁,  |Im ∫_{1/2}^{2} Y′/Y(σ+iT) dσ| ≤ C log(|T|+3)
      — Landau's partial fraction (ZeroCount/Landau.lean) on the 3/2-ball about 2+iT covering the segment:
        each term m_ρ/(s−ρ) moves the argument by ≤ π (ArgBound (B)), Σ m_ρ ≪ log, remainder ≪ log.
  * vertical_bound   : for t₁ ≤ T₁ ≤ T₂,  |Im ∫_{T₁}^{T₂} Y′/Y(2+it)·i dt| ≤ 3π
      — on Re s = 2, Y = (s(s−1)/2)·ζ·(L + ζ′/ζ) (Seam.Yfn_eq_factor); each factor has positive real part
        (up to the sign of the first), so each log moves by ≤ π (ArgBound (A); RvM.vertical_two for ζ).
-/
```

 ### horizontal sides 

### `horizontal_bound`

 **Horizontal sides.** 

 ### the vertical side Re s = 2 

### `Pneg`

 the polynomial factor, with the sign making its real part positive on Re s = 2, |t| ≥ 2. 

### `Gfn`

 G := L + ζ′/ζ = ξ′/ξ (the logarithmic derivative of ξ). 

### `Lfn_analyticAt`

 L is analytic on Re s > 0 away from s = 1. 

### `logDeriv_zeta_analyticAt`

 ζ′/ζ is analytic where ζ ≠ 0 (s ≠ 1). 

### `logDeriv_Yfn_two`

 logDeriv Y = logDeriv Pneg + logDeriv ζ + logDeriv G on the line Re s = 2 (where G ≠ 0). 

### `vertical_bound`

 **Vertical side.** 
