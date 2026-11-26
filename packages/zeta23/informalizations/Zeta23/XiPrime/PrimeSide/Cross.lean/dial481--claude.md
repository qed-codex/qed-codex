---
{
  "module": "Zeta23/XiPrime/PrimeSide/Cross.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/XiPrime/PrimeSide/Cross.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/XiPrime/PrimeSide/Cross.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/

/-
Part of the Zeta23 formalization.

Zeta23/XiPrime/PrimeSide/Cross.lean — generalised-coefficient prime side:
[prop:cross](i) for the density P_c with ARBITRARY complex coefficients:
    |𝓜[μ, P_c]| ≤ C · l · L · S₁(c),      S₁(c) = Σ_{N≤X} ‖c_N‖/√N,
for T ≥ T₀ (C, T₀ depend on H-Γ only), provided c 1 = 0.

Route = Zeta23/ThmE/CrossMuPChi.lean (double IBP, oscillatory bounds abs_Mform_cos_le /
abs_Mform_cos_phase_le of CrossMuPCore) with Λ(n)·χ(n) ↦ c_N/√N and the per-N saving 1/log N
replaced by 1/log 2 (N ≥ 2; the N = 1 term is killed by c 1 = 0).  The ζ/χ proofs use the finer
Σ Λ(n)/(√n log n) ≪ √X/log X to get l√X; here the coefficient side only has the crude
S₁ ≪ √X·l, and l·L·S₁ ≪ L·l²·√X is still o(T·L·l²) — [XF′] Remark 7.2.
-/
```

### `Mform_u_Pc_eq`

 `𝓜[u, P_c]` as the finite cos/sin-split sum (mirror of ThmE.Mform_mu_PXc_eq). 

### `cross_muPc`

 **[prop:cross](i) for P_c** with arbitrary complex coefficients (`c 1 = 0`):
`|𝓜[μ, P_c]| ≤ C · l · L · S₁(c; X)` for `T ≥ T₀`, constants depending on H-Γ only. 
