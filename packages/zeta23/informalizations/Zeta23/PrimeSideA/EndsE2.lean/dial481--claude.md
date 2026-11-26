---
{
  "module": "Zeta23/PrimeSideA/EndsE2.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/PrimeSideA/EndsE2.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/PrimeSideA/EndsE2.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/

/-
Zeta23 — [lem:ends], bound for 𝓔₂ (§5.3).  Statement consumed by
Zeta23/PrimeSideA/Ends.lean.
Substrate: Zeta23/PrimeSideA/EndsWeighted.lean; 1-D estimates N1/N2 from
Zeta23/PrimeSideA/EndsNu.lean.
-/
```

### `abs_trG2integrand_le`

 Pointwise: |trG2integrand(τ,τ')| ≤ L² Σ_{k<d} ψ(τ−τ_k)ψ(τ'−τ_k) · |ν(τ)| |ν(τ')|
([eq:Kbounds]). 

### `majK2`

 the 𝓔₂ majorant kernel with its ν-weights: `L²·(Σ_{k<d} ψ(τ−τ_k)ψ(τ'−τ_k))·|ν(τ)||ν(τ')|`. 

### `majK2_integrable`

 the majorant kernel is integrable on ℝ² (finite sum of products of integrable 1-D weights). 

### `abs_calE2_le_maj`

 `|𝓔₂(ν)| ≤ ∬_{(I×I)ᶜ} majK2(ν)`. 

### `setIntegral_compl_sqI_majK2_le`

 **The Fubini core of the 𝓔₂ majorant bound** (§5.3), with the two 1-D estimates abstracted:
if  ∫ ψ(τ−a)|ν(τ)| dτ ≤ M₁  for every a ∈ [T,2T]  and  ∫_{Iᶜ} (Σ_k ψ(τ−τ_k))|ν(τ)| dτ ≤ M₂,  then
∬_{(I×I)ᶜ} majK2(ν) ≤ 2·L²·M₁·M₂  ((I×I)ᶜ ⊆ (Iᶜ×ℝ) ∪ (ℝ×Iᶜ) and two iterated integrals). 

### `calE2_maj_bound`

 **Majorant bound behind 𝓔₂** (§5.3): ∬_{(I×I)ᶜ} L²(Σ_k ψψ')·|ν||ν'| ≤ C·L³B²·l·log l
for T ≥ T₀ — the ν-dependence sits in a nonnegative bilinear kernel (Cauchy–Schwarz
in χ is pushed inside this). 

### `calE2_maj_bound_L`

 **Majorant bound behind 𝓔₂, L-intrinsic form** (no bandwidth cap; absorbing hypothesis
`L ≤ B`): ∬_{(I×I)ᶜ} majK2(ν) ≤ C·L³B²·(1 + log L)·(L + l) for T ≥ T₀. 

### `calE2_bound`

 **Bound for E2** (§5.3): |𝓔₂| ≤ C·L³B²·l·log l for T ≥ T₀ (corollary of the
majorant bound via |K²νν'| ≤ majK2). 
