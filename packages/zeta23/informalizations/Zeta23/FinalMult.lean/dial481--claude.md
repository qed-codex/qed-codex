---
{
  "module": "Zeta23/FinalMult.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/FinalMult.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/FinalMult.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/

/-
Zeta23/FinalMult.lean — Theorems B and C of the paper with their stated constants 2/3 and 5/6
(the multiplicity-aware forms): running the §6 certificate on the multiplicity-aware rank–trace
inequalities of Assembly/SeamMult.lean (parameter c = 2 ⇒ N₀ˢ, c = 3 ⇒ N_d) with the SAME second
moment κ(λ) = 1/λ + λ/3 as Theorem A gives, for Mathlib's riemannZeta with NO hypotheses,

  thmB₀_mult : ∀ ε > 0, ∃ T₀, ∀ T ≥ T₀, (2/3 − ε)·N(T,2T) ≤ N₀ˢ(T,2T)   (simple AND on the line),
  thmC₀_mult : ∀ ε > 0, ∃ T₀, ∀ T ≥ T₀, (5/6 − ε)·N(T,2T) ≤ N_d(T,2T)    (distinct),

(Zeta23/Final.lean has the Cauchy–Schwarz forms of the same statements, with 1/2 and 3/4)
plus the fixed-λ forms (constants H(λ) = 2 − κ(λ) and G(λ) := 3/2 − κ(λ)/2) and cumulative forms.
-/
```

### `kfun`

 κ(λ) := 1/λ + λ/3, the second-moment constant of [eq:tr2]/[eq:ratio] (so H(λ) = 2 − κ(λ)). 

### `Gfun`

 G(λ) := 3/2 − κ(λ)/2 — the c = 3 certificate constant; G(1) = 5/6. 

### `Gfun_ge_near_one`

 near λ = 1: G(λ) ≥ 5/6 − (1 − λ) for 1/2 ≤ λ ≤ 1. 

### `eps_form_fiveSixths`

 ε-form sup for G: constant 5/6 = sup_{λ<1} G(λ). 

 ## The moment hypotheses from [thm:traces] (abstract zero configuration) 

### `moments_of_traces`

 [thm:traces] + H-RvM ⟹ the two moment hypotheses of the certificate with κ = κ(λ):
tr Ĝ ≥ (1 − δ)N and ‖Ĝ‖_F² ≤ (κ(λ) + δ)N eventually, for every δ > 0. 

 ## The multiplicity-aware theorems at fixed λ < 1, abstract zero configuration 

### `thmBmult_abstract`

 **multiplicity-aware Theorem B at fixed λ ∈ (0,1)**: N₀ˢ(T,2T) ≥ (H(λ) − ε)·N(T,2T). 

### `thmCmult_abstract`

 **multiplicity-aware Theorem C at fixed λ ∈ (0,1)**: N_d(T,2T) ≥ (G(λ) − ε)·N(T,2T),
G(λ) = 3/2 − κ(λ)/2. 

 ## ζ: fixed λ, then λ → 1⁻, then cumulative — NO hypotheses 

### `thmB_mult_lam`

 **multiplicity-aware Theorem B for ζ at fixed λ ∈ (0,1), UNCONDITIONAL**:
(H(λ) − ε)·N(T,2T) ≤ N₀ˢ(T,2T). 

### `thmC_mult_lam`

 **multiplicity-aware Theorem C for ζ at fixed λ ∈ (0,1), UNCONDITIONAL**:
(G(λ) − ε)·N(T,2T) ≤ N_d(T,2T), G(λ) = 3/2 − 1/(2λ) − λ/6. 

### `thmB₀_mult`

 **At least 2/3 of the zeros of ζ are SIMPLE AND ON THE CRITICAL LINE, UNCONDITIONAL**
(this is the paper's [thm:B]; Zeta23/Final.lean has the Cauchy–Schwarz form with 1/2): for every ε > 0 and all large T,
(2/3 − ε)·N(T,2T) ≤ N₀ˢ(T,2T), for Mathlib's riemannZeta. 

### `thmC₀_mult`

 **At least 5/6 of the zeros of ζ are DISTINCT, UNCONDITIONAL** (the paper's [thm:C];
Zeta23/Final.lean has the Cauchy–Schwarz form with 3/4): (5/6 − ε)·N(T,2T) ≤ N_d(T,2T). 

### `thmB₀_mult_cumulative`

 cumulative form: liminf N₀ˢ(T)/N(T) ≥ 2/3. 

### `thmC₀_mult_cumulative`

 cumulative form: liminf N_d(T)/N(T) ≥ 5/6. 
