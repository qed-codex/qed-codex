---
{
  "module": "Zeta23/Main.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/Main.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/Main.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/

/-
Zeta23/Main.lean — ζ-level headline theorems: proofs.
Instantiates the abstract §6 assembly (Zeta23.Assembly, over an arbitrary ZeroConfig) at the
nontrivial zeros of Mathlib's riemannZeta (Zeta23.zetaZeros), and performs the λ → 1⁻ and
dyadic-summation wrappers. See Zeta23/Statement.lean for the definitions being talked about.
-/
```

### `tendsto_Ncount_zero_atTop`

 N(0,T) → ∞ for ζ's zeros, from H-RvM (via N(0,T) ≥ N(T/2,T)). 

### `cumulative_of_dyadic`

 Generic dyadic wrapper at the ζ level: a dyadic ε-form for an interval-additive count f
against N gives the cumulative ε-form. 

### `thmA_of_lam`

 λ → 1⁻ wrapper for Theorem A at the ζ level. 

### `thmB_of_lam`

 λ → 1⁻ wrapper for Theorem B at the ζ level. 

### `thmC_of_lam`

 λ → 1⁻ wrapper for Theorem C at the ζ level. 

### `thmA_cumulative_of_dyadic`

 dyadic wrapper, Theorem A. 

### `thmB_cumulative_of_dyadic`

 dyadic wrapper, Theorem B. 

### `thmC_cumulative_of_dyadic`

 dyadic wrapper, Theorem C. 

 ## Theorem A from PaperInputs + the thm:traces hypothesis

`thmA_of_traces` is a named declaration whose type shows exactly what is assumed: the
published inputs H : PaperInputs, a taper profile, and the thm:traces hypothesis
ThmTracesHyp (stated on the prime-side ν_X integrals). The zero-side block package and the
tail package are discharged from the sibling files. 

### `paramsOf`

 the §6 parameter choice: profile ϱ, exponent λ, ramp width w := 1. 

### `eventually_side_conditions`

 Discharge of the "small" eventually-hypotheses of Assembly.thmA_abstract from Taper.lean,
the H-EF bridge (GzGp.lean), Tail's boundary count and Assembly's ℰ_T → 0. 

### `eventually_blockInputs`

 prop:block + [eq:Ncount] eventually (ZeroSide.eventually_blockInputs_of), with its two
inputs discharged: a > 0 eventually ([eq:abdef] via Taper's half_le_a) and lem:poisson ★
(Params.hasSum_phiHatR_sq). 

### `thmA_lam_of_traces`

 **Theorem A at fixed λ ∈ (0,1), modulo the thm:traces hypothesis.** 

### `thmA_of_traces`

 **Theorem A (2/3, dyadic ε-form) modulo the thm:traces hypothesis.** 

### `thmA_cumulative_of_traces`

 and its cumulative form (liminf N₀*(T)/N(T) ≥ 2/3), same hypotheses. 

### `thmB_lam_of_traces`

 Theorem B at fixed λ, modulo the thm:traces hypothesis. 

### `thmC_lam_of_traces`

 Theorem C at fixed λ, modulo the thm:traces hypothesis. 

### `thmB_of_traces`

 Theorem B modulo thm:traces: (1/2 − ε), dyadic. 

### `thmB_cumulative_of_traces`

 Theorem B modulo thm:traces, cumulative. 

### `thmC_of_traces`

 Theorem C modulo thm:traces: (3/4 − ε), dyadic. 

### `thmC_cumulative_of_traces`

 Theorem C modulo thm:traces, cumulative. 

 ## Minimal trust base, displayed in the type

The literature-form explicit formula EF_lit ([eq:EFstd]) implies the paper form given
H-Γ (Zeta23.EF.explicitFormulaPaper_of_lit), and H-cheb is a theorem (Zeta23.Cheb.chebyshevMertens).
So the published inputs reduce to: EF_lit, Riemann–von Mangoldt (+ local count),
Montgomery–Vaughan, and the Γ-facts. 

### `PaperInputs.of_lit`

 PaperInputs from the minimal trust base. 

### `thmA_final_of_traces`

 **Theorem A, minimal-trust-base form, modulo the thm:traces hypothesis.** 

### `thmA_std_of_traces`

 **Theorem A, hypothesis-minimal form**: with the concrete profile
ϱ := Real.smoothTransition (Zeta23.stdProfile), so the type carries only the literature trust base
(hEF, hRvM, hMV, hΓ) and the thm:traces hypothesis hTr. 

### `thmB_std_of_traces`

 same, Theorem B. 

### `thmC_std_of_traces`

 same, Theorem C. 
