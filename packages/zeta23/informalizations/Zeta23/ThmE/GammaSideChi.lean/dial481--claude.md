---
{
  "module": "Zeta23/ThmE/GammaSideChi.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/ThmE/GammaSideChi.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/ThmE/GammaSideChi.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/

/-
Zeta23/ThmE/GammaSideChi.lean — the Γ/conductor side of the folded contour
for L(s,χ) is EXACTLY ∫ μ_χ:
  (1/π)·Im ∫_L logDeriv(arch) = ∫_{T₁}^{T₂} μ_χ(t) dt,   arch(s) := q^{s/2} · Γℝ(s + κ),
where κ ∈ {0,1} is the parity (gammaFactor χ s = Γℝ(s + κ) by Even/Odd.gammaFactor_def), because
logDeriv arch = (log q)/2 + logDeriv Γℝ(·+κ) is holomorphic on Re s > 0 and on the critical line
  Re[(log q)/2 − (log π)/2 + ψ(¼ + κ/2 + it/2)/2] = π·μ_χ(t)   (μ_χ = Zeta23.ThmE.muq κ q).
This is the analogue of Zeta23/RvM/GammaSide.lean for L(s,χ).
-/
```

### `archChi`

 the archimedean factor carrying the conductor: arch(s) := q^{s/2}·Γℝ(s+κ). 

### `logDeriv_archChi`

 logDeriv arch(s) = (log q)/2 + (−(log π)/2 + ψ((s+κ)/2)/2) on Re s > 0. 

### `re_logDeriv_archChi_half`

 Re logDeriv arch(½+it) = π·μ_χ(t). 

### `gammaSideChi`

 the Γ/conductor-side contour identity: for 0 < T₁, T₂,
(1/π)·Im(halfContour (logDeriv arch) T₁ T₂) = ∫_{T₁}^{T₂} μ_χ. 
