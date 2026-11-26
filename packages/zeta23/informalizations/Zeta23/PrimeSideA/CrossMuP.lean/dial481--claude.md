---
{
  "module": "Zeta23/PrimeSideA/CrossMuP.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/PrimeSideA/CrossMuP.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/PrimeSideA/CrossMuP.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/

/-
Part of the Zeta23 formalization of
  "More than two thirds of the zeros of the Riemann zeta function lie on the critical line".
Imported by PrimeSideA.lean.
-/
```


# [prop:cross] (i):  `𝓜[μ, P_X] ≪ l √X`   (the paper §5.4)

Paper proof (§5.4): with `m(τ′) := ∫_I Φ(τ−τ′)² μ(τ) dτ`, "`m` is `C¹`, and differentiating
under the integral and integrating by parts in `τ`,
`m′(τ′) = μ(T)Φ(T−τ′)² − μ(2T)Φ(2T−τ′)² + ∫_I μ′(τ)Φ(τ−τ′)² dτ`, so that `∫_I|m′| ≪ lL`.
For `y ≥ log 2`, integrating by parts, `|∫_I m(τ′)cos(τ′y)dτ′| ≤ (2 sup|m| + ∫_I|m′|)/y ≪ lL/y`.
Therefore `|𝓜[μ,P_X]| = |π⁻¹ Σ_n a_n ∫_I m(τ′)cos(τ′y_n)dτ′| ≪ lL Σ_{n≤X} a_n/log n ≪ lL √X/L = l√X`
by (eq:cheb1)."

Formal route (same two integrations by parts, but ordered so that NO differentiation under the
integral sign is needed): Fubini with `τ` outer; IBP in `τ′` on `Φ(τ−τ′)²·cos(τ′y)` (the derivative
lands on `Φ²`, `Φ ∈ C¹`); Fubini swap; IBP in `τ` on `μ(τ)·(Φ²)′(τ−τ′)` (the derivative lands on
`μ`); then the sup bounds `|μ| ≤ l`, `|μ′| ≤ C/T` on `I` and `∫_S Φ(·−c)² ≤ ∫_ℝ Φ² = 2πbL` give
`|𝓜[μ, cos(·y)]| ≤ (4l + C)·2πbL/|y|`, and [eq:cheb1] (`cheb1c`: `Σ Λ(n)/(√n log n) ≪ √X/log X`, `log X = L`)
finishes.  Inputs: `LocalHyps` (Φ ∈ C¹, Φ even, ∫Φ² = 2πbL, b ≤ a ≤ 1, l ≥ 1), H-Γ (`smooth`,
`deriv_bound`, via `mu_abs_le_l`), H-cheb (`cheb1c`).


 ## [prop:cross] (i) 

### `Mform_mu_PX_eq`

 `𝓜[μ, P_X]` as the finite sum `−π⁻¹ Σ_n a_n 𝓜[μ, cos(· y_n)]` (§5.4, Fubini/linearity). 

### `prop_cross_muP`

 **[prop:cross] (i)** (§5.4): `𝓜[μ,P_X] ≪ l√X`, stated in the `∃ C, EventuallyAtCore cϱ lam …`
form used by the results of `PrimeSideA.lean` (which imports this file). 
