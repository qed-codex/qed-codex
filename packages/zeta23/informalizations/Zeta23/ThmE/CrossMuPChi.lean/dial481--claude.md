---
{
  "module": "Zeta23/ThmE/CrossMuPChi.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/ThmE/CrossMuPChi.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/ThmE/CrossMuPChi.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/

/-
Zeta23/ThmE/CrossMuPChi.lean — [prop:cross] (i) for L(s,χ):  `𝓜[μ_χ, P_{X,χ}] ≪_q l√X`
(statement in Zeta23/ThmE/PrimeSideChi.lean, which re-exports this proof).

Route = the ζ-proof of Zeta23/PrimeSideA/CrossMuP.lean (double IBP, no differentiation under the
integral), with two changes: the density μ_χ's bounds come from the H-Γ(χ) package
(`GammaFactsChi`: stirling for |μ_χ| ≤ C_q·l on I, deriv_bound for |μ_χ′| ≤ C/T), and the prime
sum has complex unimodular-or-smaller coefficients: `Re(c_n·n^{−iτ}) = ‖c_n‖·cos(τ·log n − arg c_n)`,
handled by the PHASE-SHIFTED oscillatory bound `abs_Mform_cos_phase_le` (CrossMuPCore) — the bounds
enter only through `‖c_n‖ ≤ 1`, exactly per [thm:E] proof (iii).
-/
```

 ## The Mform finite-sum split and the oscillatory bound 

### `Mform_mu_PXc_eq`

 `𝓜[u, P_{X,c}]` as the finite phase-split sum (mirror of the ζ `Mform_mu_PX_eq`). 

 ## [prop:cross](i) for L(s,χ) — the proof 

### `prop_cross_muP_chi_proved`

 **[prop:cross](i) for L(s,χ)** (statement = `prop_cross_muP_chi` of PrimeSideChi.lean, plus
the mathematically-required `1 ≤ q`): `|𝓜[μ_χ, P_{X,χ}]| ≪_q l√X`.  Complex coefficients enter
only through `|re|, |im| ≤ ‖c n‖ ≤ 1` ([thm:E] (iii)); the sin-part uses the phase-shifted
oscillatory bound at `θ = −π/2`. 
