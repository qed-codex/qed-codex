---
{
  "module": "Zeta23/ThmD/Mult.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/ThmD/Mult.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/ThmD/Mult.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/

/-
Zeta23/ThmD/Mult.lean — the multiplicity-aware Theorem D, i.e. the second and third constants of the
paper's [thm:D]: with the Montgomery–Taylor window, at least 2 − 1/c₁* = 0.67250… of the zeros are
SIMPLE AND on the critical line, and at least (3 − 1/c₁*)/2 = 0.83625… are DISTINCT (the
Cauchy–Schwarz forms in Zeta23/ThmD/Final.lean give 2c₁* − 1 = 0.50659… and c₁* = 0.75329…) — by
running the c = 2 / c = 3 rank–trace inequalities (Assembly/SeamMult.lean; the zero side uses only
the Poisson identity, so the window-realizing family P.atD plugs in) through the Theorem-D endgame.
For Mathlib's riemannZeta, NO hypotheses.  The multiplicity-aware zero side and seams are
ZeroSide/Mult.lean and Assembly/SeamMult.lean; the underlying bookkeeping is Σ_ρ (c·m_ρ − m_ρ²).
-/
```

### `Nd_lower_c3`

 the c = 3 fixed-T algebra with an abstract second-moment constant:
from 6trĜ − ‖Ĝ‖² − 3N − 5NII − B(6+2√‖Ĝ‖²+B) ≤ 2N_d, |trĜ − N| ≤ R₁, ‖Ĝ‖² ≤ cinv·N + R₂:
(3 − cinv)N − [6R₁ + R₂ + 5NII + B(6 + 2√(cinv N + R₂) + B)] ≤ 2N_d. 

### `thmD_mult2_abstract`

 **multiplicity-aware Theorem D, c = 2 (simple ∧ on-line), abstract**: the thmD_abstract
statement with conclusion N₀ˢ. 

### `thmD_mult3_abstract`

 **multiplicity-aware Theorem D, c = 3 (distinct), abstract**: (3/2 − 1/(2c) − ε)N ≤ N_d. 

 ## fixed λ, abstract Z with the paper's inputs; then ζ; then λ → 1⁻ 

### `GD`

 GD(λ) := 3/2 − 1/(2c*(λ)) = (HD(λ) + 1)/2;  GD(1) = 0.83625… 

### `thmD_mult_lam_abstract`

 both lines at fixed λ ∈ (0,1), abstract zero configuration. 

### `thmD_simple_mult_lam`

 ζ at fixed λ ∈ (0,1): (HD(λ) − ε)N ≤ N₀ˢ, UNCONDITIONAL. 

### `thmD_dist_mult_lam`

 ζ at fixed λ ∈ (0,1): (GD(λ) − ε)N ≤ N_d, UNCONDITIONAL. 

### `thmD₀_simple_mult`

 **0.6725… of the zeros of ζ are SIMPLE AND ON THE CRITICAL LINE, UNCONDITIONAL**
([thm:D]'s second constant: 2 − 1/c₁* = 3/2 − cot(1/√2)/√2, the same as for N₀*, now for the
simple-and-on-line count; the Cauchy–Schwarz form in Zeta23/ThmD/Final.lean has 2c₁* − 1 = 0.50659…). 

### `thmD₀_simple_mult'`

 the same with the constant written out. 

### `thmD₀_dist_mult`

 **(3 − 1/c₁*)/2 = 0.83625… of the zeros of ζ are DISTINCT, UNCONDITIONAL** ([thm:D]'s third
constant; the Cauchy–Schwarz form in Zeta23/ThmD/Final.lean has c₁* = 0.75329…). 

### `thmD₀_simple_mult_cumulative`

 cumulative: liminf N₀ˢ(T)/N(T) ≥ 0.6725… 

### `thmD₀_dist_mult_cumulative`

 cumulative: liminf N_d(T)/N(T) ≥ 0.83625… 
