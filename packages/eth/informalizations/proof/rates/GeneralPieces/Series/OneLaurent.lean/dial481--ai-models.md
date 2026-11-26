---
{
  "module": "proof/rates/GeneralPieces/Series/OneLaurent.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/GeneralPieces/Series/OneLaurent.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/GeneralPieces/Series/OneLaurent.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # A step in the proof of Lemma 9 (Appendix B), paragraph "One Laurent polynomial"

From an expansion f± = Σ_c Γ_c·ε±^{N_c}·n_c alone: (ω₁ − ω₂)^H·f₊ and (ω₁ − ω₂)^H·f₋ are the same
element F = Σ_c Γ_c·(ω₁ − ω₂)^{H − N_c}·n_c of 𝓛 (`dW_pow_mul_fP`, `dW_pow_mul_fM`), and
F(1,1) = G·[π = σ] (`ev_F`), where G is the sum of the Γ_c with N_c = H. Only (ω₁ − ω₂)·ε± = 1 is
used. 

### `Expansion.F`

 F = Σ_c Γ_c·(ω₁ − ω₂)^{H − N_c}·n_c, an element of 𝓛. 

### `pow_mul_term`

 One term: if d·e = 1 and N ≤ H then d^H·(Γ·(e^N·n)) = Γ·(d^{H−N}·n). 

### `pow_mul_terms`

 The same for a sum of terms and a homomorphism φ from 𝓛. 

### `Expansion.dW_pow_mul_fP`

 (ω₁ − ω₂)^H·f₊ = F in 𝓛₊. 

### `Expansion.dW_pow_mul_fM`

 (ω₁ − ω₂)^H·f₋ = F in 𝓛₋. 

### `ev`

 F ↦ F(1,1): the homomorphism 𝓛 → ℚ that maps ω₁ and ω₂ to 1. 

### `ev_terms`

 At ω₁ = ω₂ = 1 only the terms with N_c = H remain. 

### `Expansion.ev_F`

 F(1,1) = G·[π = σ]. 
