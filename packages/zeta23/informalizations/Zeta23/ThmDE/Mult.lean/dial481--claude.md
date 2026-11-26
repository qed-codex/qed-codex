---
{
  "module": "Zeta23/ThmDE/Mult.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/ThmDE/Mult.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/ThmDE/Mult.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/

/-
Zeta23/ThmDE/Mult.lean — the multiplicity-aware Theorem D for Dirichlet L-functions ([thm:E]'s last
clause, "Theorem D holds likewise", with the paper's stated constants): for every primitive χ mod
q > 1 and Mathlib's
DirichletCharacter.LFunction χ, NO hypotheses,
  thmE_D₀_simple_mult : (HD 1 − ε)·N_χ(T,2T) ≤ N^s_{0,χ}(T,2T)   [HD 1 = 0.6725…, simple ∧ on-line]
  thmE_D₀_dist_mult   : (GD 1 − ε)·N_χ(T,2T) ≤ N_{d,χ}(T,2T)     [GD 1 = 0.83625…, distinct].
Pattern: Zeta23/ThmD/Mult.lean (ζ) — the ThmDE Endgame (thmDChi_abstract) with seamA ↦ seamA_mult2 /
seamA_mult3 (+ Nd_lower_c3), then the ThmDE/Final wiring and eps_form_HD / the GD = (HD+1)/2 trick.
Credits: the multiplicity-aware zero side / seams are Assembly/SeamMult.lean and ZeroSide/Mult.lean;
the ζ template is ThmD/Mult.lean.
-/
```

### `thmDChi_mult2_abstract`

 **multiplicity-aware Theorem D for L(s,χ), c = 2 (simple ∧ on-line), abstract.** 

### `thmDChi_mult3_abstract`

 **multiplicity-aware Theorem D for L(s,χ), c = 3 (distinct), abstract.** 

### `thmDChi_mult_lam_abstract`

 both mult lines at fixed λ ∈ (0,1), abstract zero configuration with the χ-inputs. 

 ## L(s,χ): fixed λ, then λ → 1⁻ — NO hypotheses 

### `thmE_D_simple_mult_lam`

 fixed λ: (HD(λ) − ε)·N_χ ≤ N^s_{0,χ}, UNCONDITIONAL. 

### `thmE_D_dist_mult_lam`

 fixed λ: (GD(λ) − ε)·N_χ ≤ N_{d,χ}, UNCONDITIONAL. 

### `thmE_D₀_simple_mult`

 **0.6725… of the zeros of L(s,χ) are SIMPLE AND ON THE CRITICAL LINE, UNCONDITIONAL** (every
primitive χ mod q > 1; multiplicity-aware Theorem D: HD 1 = 2 − 1/c₁* = 3/2 − cot(1/√2)/√2). 

### `thmE_D₀_dist_mult`

 **(3 − 1/c₁*)/2 = 0.83625… of the zeros of L(s,χ) are DISTINCT, UNCONDITIONAL.** 
