---
{
  "module": "Zeta23/ExplicitFormula/Bridge.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/ExplicitFormula/Bridge.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/ExplicitFormula/Bridge.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/

/-
Zeta23/ExplicitFormula/Bridge.lean

The two "all integrals absolutely convergent" side-facts of App. A [app:EF]:
  * `integrable_fourier_of_contDiff_two` : k ∈ C_c²(ℝ) ⇒ 𝓕 k ∈ L¹(ℝ)   (from [eq:hfbound], Zeta23/Poisson/PaperFT.lean);
  * `integrable_paperFT_mul_mu`          : k ∈ C_c²(ℝ) ⇒ h_k · μ ∈ L¹(ℝ)  (from [eq:hfbound] + H-Γ [eq:mufacts]);
and the clean bridge
  * `explicitFormulaPaper_of_lit` : EF_lit Z → GammaFacts → ExplicitFormulaPaper Z,
i.e. the literature-form explicit formula [eq:EFstd] (plus the Stirling facts for μ that PaperInputs already
carries) implies the paper's [prop:EF]/[eq:EF] exactly as Hypotheses.lean states it.
-/
```

### `exists_abs_le_of_hasCompactSupport`

 A compactly supported function on ℝ is supported in some `[−Λ, Λ]`. 

### `norm_fourier_mul_one_add_sq_le`

 [eq:hfbound] on the real line, both orders, in terms of Mathlib's `𝓕`:
`‖𝓕 k w‖ (1 + w²) ≤ ‖k‖₁ + ‖k''‖₁/(4π²)`. 

### `integrable_fourier_of_contDiff_two`

 `k ∈ C_c²(ℝ)` ⇒ `𝓕 k` integrable (App. A: "h(r) ≪_k (1+|r|)^{-2}"). 

### `norm_paperFT_mul_one_add_sq_le`

 [eq:hfbound] on the real line for the paper transform: `‖h_k(τ)‖(1+τ²) ≤ ‖k‖₁ + ‖k''‖₁`. 

### `abs_mu_le_of_gammaFacts`

 From H-Γ: `|μ(τ)| ≤ K₂ (1+|τ|)^{1/2}` for all τ (continuity on [−1,1]; Stirling [eq:mufacts]
`μ(τ) = (1/2π)log(|τ|/2π) + O(τ^{-2})` and `log x ≤ 2x^{1/2}` for |τ| ≥ 1). 

### `integrable_paperFT_mul_mu`

 `k ∈ C_c²(ℝ)` and H-Γ ⇒ `h_k · μ` integrable on ℝ (dominated by `K (1+|τ|)^{−3/2}`). 

### `explicitFormulaPaper_of_lit`

 **The bridge.**  The literature-form explicit formula [eq:EFstd] (`EF_lit`) together with the
Stirling-type facts H-Γ for μ (already a field of `PaperInputs`) implies the paper's
[prop:EF]/[eq:EF] exactly as `Zeta23.ExplicitFormulaPaper` (Hypotheses.lean) states it (App. A). 
