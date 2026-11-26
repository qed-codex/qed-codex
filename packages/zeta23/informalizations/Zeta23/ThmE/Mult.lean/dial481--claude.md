---
{
  "module": "Zeta23/ThmE/Mult.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/ThmE/Mult.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/ThmE/Mult.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/

/-
Zeta23/ThmE/Mult.lean — the multiplicity-aware Theorem E ([thm:E] with the paper's stated constants):
for every primitive Dirichlet character χ mod q > 1 and Mathlib's 'DirichletCharacter.LFunction χ',
NO hypotheses: at least (2/3 − ε)·N_χ(T,2T) of the zeros are SIMPLE AND on the critical line and at
least (5/6 − ε)·N_χ(T,2T) are DISTINCT (the Cauchy–Schwarz forms in Zeta23/ThmE/Final.lean give 1/2
and 3/4); fixed-λ forms with H(λ), G(λ).  This is Zeta23/FinalMult.lean's moments/certificate
argument with the χ-scalars (ℓ_{1,χ}, λ_{1,χ}, ν_{X,χ}) of Zeta23/ThmE/AssemblyQ.lean.  The
multiplicity-aware zero side, seams and certificates are ZeroSide/Mult.lean, Assembly/SeamMult.lean
and Assembly/Certificate*.lean.
-/
```

### `moments_of_traces_chi`

 [thm:traces] + H-RvM ⟹ the two moment hypotheses of the certificate with κ = κ(λ):
tr Ĝ ≥ (1 − δ)N and ‖Ĝ‖_F² ≤ (κ(λ) + δ)N eventually, for every δ > 0. 

### `thmBmult_chi_abstract`

 **multiplicity-aware Theorem B at fixed λ ∈ (0,1)**: N₀ˢ(T,2T) ≥ (H(λ) − ε)·N(T,2T). 

### `thmCmult_chi_abstract`

 **multiplicity-aware Theorem C at fixed λ ∈ (0,1)**: N_d(T,2T) ≥ (G(λ) − ε)·N(T,2T),
G(λ) = 3/2 − κ(λ)/2. 

 ## L(s,χ): fixed λ, then λ → 1⁻ — NO hypotheses 

### `thmE_B_mult_lam`

 multiplicity-aware Theorem E/B at fixed λ ∈ (0,1): (H(λ) − ε)·N_χ ≤ N^s_{0,χ}, UNCONDITIONAL. 

### `thmE_C_mult_lam`

 multiplicity-aware Theorem E/C at fixed λ ∈ (0,1): (G(λ) − ε)·N_χ ≤ N_{d,χ}, UNCONDITIONAL. 

### `thmE_B₀_mult`

 **At least 2/3 of the zeros of L(s,χ) are SIMPLE AND ON THE CRITICAL LINE, UNCONDITIONAL**
(every primitive χ mod q > 1; as stated in [thm:E]). 

### `thmE_C₀_mult`

 **At least 5/6 of the zeros of L(s,χ) are DISTINCT, UNCONDITIONAL** (every primitive χ mod
q > 1; as stated in [thm:E]). 
