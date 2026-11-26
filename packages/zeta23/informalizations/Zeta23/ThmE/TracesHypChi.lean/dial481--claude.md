---
{
  "module": "Zeta23/ThmE/TracesHypChi.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/ThmE/TracesHypChi.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/ThmE/TracesHypChi.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/

/-
Zeta23/ThmE/TracesHypChi.lean — the thm:traces package for Dirichlet L-functions.
Mirror of Zeta23/PrimeSideTemp.lean ([thm:traces] as an explicit hypothesis)
with ζ's density ν_X replaced by ν_{X,χ} and ℓ₁ by ℓ_{1,χ} ([thm:E] proof (i),(iii)).
The hypothesis is discharged by the §5-χ generalization elsewhere in the repository; it is an
explicit hypothesis of the Theorem E assembly, never a Lean axiom.
-/
```

### `lam1q`

 `λ_{1,χ} := L/ℓ_{1,χ}`  ([thm:E] proof (iii): "λ₁ = L/ℓ_{1,χ} → λ as q is fixed"). 

### `GentryChi`

 G_{kl} for L(s,χ) via the PRIME side: `∫ φ̂(τ−τ_k) φ̂(τ−τ_l) ν_{X,χ}(τ) dτ`
([eq:Gdef] second expression with ν_{X,χ}). 

### `trGtildeChi`

 tr G̃ for L(s,χ) (prime side). 

### `trGtildeSqChi`

 tr G̃² for L(s,χ) (prime side). 

### `mainTr2Chi`

 The main term of [eq:tr2] for L(s,χ): `(TL/2π)(ℓ_{1,χ}² + L²/3)`. 

### `TracesBoundsChi`

 **[thm:traces] for L(s,χ)** (the conclusions of the paper [thm:traces] with ℓ₁ → ℓ_{1,χ},
λ₁ → λ_{1,χ}, ν_X → ν_{X,χ}; [thm:E] proof (iii)).  Same EvBound shapes as `Zeta23.TracesBounds`;
all constants may additionally depend on q (q fixed in [thm:E]; recorded for the hybrid-range
question [rem:otherL](i)). 

### `ThmTracesHypChi`

 The Theorem E traces hypothesis at a zero configuration Z (the analogue of `Zeta23.ThmTracesHyp`). 
