---
{
  "module": "Zeta23/ThmDE/Final.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/ThmDE/Final.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/ThmDE/Final.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/

/-
Zeta23/ThmDE/Final.lean — **"Theorem D holds likewise" for Dirichlet L-functions** (the paper
[thm:E], last sentence).  For every primitive Dirichlet character χ mod q > 1
and the nontrivial zeros of Mathlib's 'DirichletCharacter.LFunction χ' (counts of
Zeta23/ThmE/Statement.lean), with NO hypotheses:

  thmE_D₀        : ∀ ε > 0, ∃ T₀, ∀ T ≥ T₀, (HD 1 − ε)·N_χ(T,2T) ≤ N*_{0,χ}(T,2T),
  thmE_D₀_simple : … (2c₁* − 1 − ε)·N_χ(T,2T) ≤ N^s_{0,χ}(T,2T),
  thmE_D₀_dist   : … (c₁* − ε)·N_χ(T,2T) ≤ N_{d,χ}(T,2T),

HD 1 = 2 − 1/c₁* = 3/2 − cot(1/√2)/√2, c₁* = Zeta23.ThmD.cStar 1 — the Montgomery–Taylor constants of
[thm:D]; and the fixed-λ forms at every λ ∈ (0,1).  Assembly = Zeta23/ThmD/Final.lean's with the
χ-pieces: Concrete (χ-D prime side), ZeroSide (P.atD tail/EF-bridge for χ), Limit (λ_{1,χ} → λ),
Endgame (§6 for χ with the window-general ratio constant), and ThmE/Final.lean's unconditional
input package paperInputsChi_L (EF(χ), RvM(χ), Γ(χ), cheb, cheb-coprime, MV — all theorems).
-/
```

### `thmDChi_lam_abstract`

 **Theorem D for L(s,χ) at fixed λ ∈ (0,1), abstract zero configuration with the χ-inputs** —
all three lines. 

 ## L(s,χ): fixed λ, then λ → 1⁻ — NO hypotheses 

### `thmE_D_lam`

 **Theorem D for L(s,χ) at fixed λ ∈ (0,1)**, Thm-A line, UNCONDITIONAL. 

### `thmE_D_simple_lam`

 fixed λ, Thm-B line for L(s,χ), UNCONDITIONAL. 

### `thmE_D_dist_lam`

 fixed λ, Thm-C line for L(s,χ), UNCONDITIONAL. 

### `thmE_D₀`

 **[thm:E] "Theorem D holds likewise", first constant, NO hypotheses**: for every primitive
Dirichlet character χ mod q > 1, for every ε > 0 and all large T, at least
(2 − 1/c₁* − ε)·N_χ(T,2T) of the zeros of Mathlib's 'DirichletCharacter.LFunction χ' with
ordinate in (T,2T], counted with multiplicity, are matched by DISTINCT critical-line zeros
(2 − 1/c₁* = HD 1 = 3/2 − cot(1/√2)/√2 = 0.6725…). 

### `thmE_D₀'`

 the same with the constant written out: (3/2 − cot(1/√2)/√2 − ε)·N_χ ≤ N*_{0,χ}. 

### `thmE_D₀_simple`

 **[thm:E] "Theorem D holds likewise", second constant, NO hypotheses**:
N^s_{0,χ}(T,2T) ≥ (2c₁* − 1 − ε)·N_χ(T,2T) — simple AND on the line (0.5065…). 

### `thmE_D₀_dist`

 **[thm:E] "Theorem D holds likewise", third constant, NO hypotheses**:
N_{d,χ}(T,2T) ≥ (c₁* − ε)·N_χ(T,2T) — distinct zeros (0.7532…). 
