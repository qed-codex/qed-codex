---
{
  "module": "Zeta23/ThmE/GzGpChi.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/ThmE/GzGpChi.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/ThmE/GzGpChi.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/

/-
Zeta23/ThmE/GzGpChi.lean — the H-EF(χ) bridge for L(s,χ).

[thm:E] proof (i): "Proposition [prop:EF] holds for W_χ(f,g) := Σ_ρ m_ρ h_f(γ_ρ) conj(h_g(conj γ_ρ))
(zeros of L(s,χ)) with ν_X replaced by ν_{X,χ} := μ_χ + P_{X,χ} … Since ν_{X,χ} is real, G is again
real symmetric."  Exactly as for ζ: instantiate the hypothesis ExplicitFormulaPaperChi κ q c Z at
(f_k, f_l); the zero side is Z.Gz verbatim (Zeta23.GzGp.Gz_eq_W, density-independent), the prime side is
GpChi (Zeta23/ThmE/AssemblyQ.lean) because φ̂ is real on ℝ (Zeta23.GzGp.phiHat_ofReal) and nuXc is
real-valued by construction.  Consumed by the thmE gates (hGzGp).
-/
```

### `EFrhs_eq_GpChi`

 Prime side: the [eq:EF]_χ right-hand side at (f_k, f_l) is literally (G^{prime}_χ)_{kl}. No hypotheses. 

### `ZeroConfig.Gz_eq_GpChi`

 **The H-EF(χ) bridge**: zero-side and prime-side matrices for L(s,χ) agree, given H-EF(χ), L > 0,
φ ∈ C² and supp φ ⊆ [−L/2, L/2]. 

### `ZeroConfig.summable_Gsummand_chi`

 Under H-EF(χ) the zero-side entries are absolutely summable (for the χ-tail file). 
