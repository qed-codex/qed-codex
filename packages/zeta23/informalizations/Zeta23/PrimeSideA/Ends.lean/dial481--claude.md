---
{
  "module": "Zeta23/PrimeSideA/Ends.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/PrimeSideA/Ends.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/PrimeSideA/Ends.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/

/-
Zeta23 — prime side, [lem:ends] "End effects" (the paper, §5, §5.3), with [eq:Kdef],
[eq:trG2int], [eq:Kbounds].

MAIN RESULT (consumed by thm:traces):
  theorem lem_ends (hΓ : GammaFacts) (hcheb : ChebyshevMertens) (hlam : 0 < lam ∧ lam ≤ 1) :
    ∃ C : ℝ, EventuallyAtCore cϱ lam (fun p F =>
      |trGt2A p F - MtotalA p F| ≤ C * (p.L * p.l * Real.log p.l * (p.l ^ 2 + p.X)))

PAPER (§5.3, verbatim): "For T ≥ T₀,  tr G̃² = 𝓜 + O(L l log l (l² + X)),
  𝓜 := ∬_{I×I} Φ(τ−τ')² ν_X(τ) ν_X(τ') dτ dτ'."

ROUTE (paper's, §5.3, with two simplifications that only change absolute constants):
* [eq:trG2int]  L² tr G̃² = Σ_{k,l<d} G_{kl}² = ∬_{ℝ²} K(τ,τ')² ν(τ)ν(τ') dτdτ',
  K(τ,τ') := Σ_{0≤k<d} φ̂(τ−τ_k)φ̂(τ'−τ_k) [eq:Kdef]  — here a product of two integrals and a
  FINITE sum, so no Fubini beyond ∫(f)·∫(g) = ∬ f⊗g.
* K_∞ := Σ_{k∈ℤ} φ̂(τ−τ_k)φ̂(τ'−τ_k) = L Φ(τ−τ') by [lem:poisson] (LocalHyps.poisson), so
  ∬_{I×I} K_∞² νν' = L² 𝓜, and  L²(tr G̃² − 𝓜)·L² … precisely:
  Σ G² − L²𝓜·… = 𝓔₁ + 𝓔₂,  𝓔₁ := ∬_{I×I}(K² − K_∞²)νν',  𝓔₂ := ∬_{ℝ²∖I×I} K²νν'.
* [eq:Kbounds]  |K|, |K_∞| ≤ L² (paper: aL²; a ≤ 1);  |K_out| = |K_∞ − K| handled by the
  weighted AM–GM  |Σ_{k∉[0,d)} a_k b_k| ≤ ½(s ρ(τ) + ρ(τ')/s), ρ(τ) := Σ_{k∉[0,d)} φ̂(τ−τ_k)²
  = aL² − Σ_{k<d} φ̂(τ−τ_k)² (Poisson diagonal — a FINITE expression), with s := g(τ')/g(τ),
  g := (1 + dist(·,∂I))⁻².  This replaces the paper's (∫_I ψ_k)²-sum (§5.3) and gives
  |𝓔₁| ≤ 2L²B²(∫_I ρ/g)(∫_I g) ≪ L²B²·L·l ≤ L³B² l log l  — within the lemma's error (the paper
  gets L³B² log L here; the slack l is free since 𝓔₂ is the dominant term anyway).
* 𝓔₂ exactly as the paper (§5.3): |𝓔₂| ≤ 2L² Σ_{k<d}(∫_{I^c}ψ_k|ν|)(∫_ℝ ψ_k|ν|),
  second factor ≤ 3Ψ₀B, Σ_k first factor = ∫_{I^c}|ν|σ ≪ BLl via the grid bound
  σ(τ) ≤ ψ(Δ) + h⁻¹∫_Δ^∞ψ, σ ≤ d ψ(Δ); for the far range we use log⁺x ≤ 2√x instead of
  integrating logarithms (constants only).
* [eq:Bdef] |ν_X(τ)| ≤ B + log⁺(|τ|/4T), B = l + 4√X (Zeta23/PiFacts.lean,
  from H-Γ + H-cheb); B² ≤ 2l² + 32X.
All constants C may depend on c_ϱ and λ (PrimeSideA convention); T₀ likewise.

The proof is assembled from the 𝓔₁ and 𝓔₂ bounds (Zeta23.PrimeSideA.EndsE1/EndsE2) in the
theorems below.
-/
```

### `Bconst_sq_le`

 `B² ≪ l² + X` [eq:Bdef]: `(l + 4√X)² ≤ 32 (l² + X)` (for `l ≥ 0`, `X ≥ 0`). 

### `lem_ends_nu_W`

 **[lem:ends], ν-generic, window-generic core**: LocalHypsCoreW + the cap L ≤ 2l (used downstream with λ ∈ (1,2]). 

### `lem_ends_nu`

 **[lem:ends], ν-GENERIC FORM** under the paper's window hypotheses (LocalHypsCore, λ ≤ 1):
`|L⁻² Σ_{k,l<d} G_{kl}(ν)² − 𝓜(ν)| ≤ C · L · l · log l · B²` for `T ≥ T₀` (C, T₀ depend on c_ϱ only),
for any continuous density with `|ν(τ)| ≤ B + log⁺(|τ|/4T)`, `l ≤ B`. 

### `nuBound_eventually`

 [eq:Bdef] in the present packaging: `Zeta23.nuX_abs_le` gives
`NuBound p (Bconst p) (Zeta23.nuX p.X)` for `T ≥ T₀(λ)`. 

### `lem_ends`

 **[lem:ends] (End effects)** (§5.3, verbatim): for `T ≥ T₀`,
`tr G̃² = 𝓜 + O(L · l · log l · (l² + X))`,  `𝓜 := ∬_{I×I} Φ(τ−τ')² ν_X(τ)ν_X(τ') dτdτ'`.
ζ-instantiation of `lem_ends_nu` with
`ν := ν_X`, `B := l + 4√X` ([eq:Bdef] via `Zeta23.nuX_abs_le`, continuity of μ from H-Γ);
`hcheb` is carried for interface uniformity. 
