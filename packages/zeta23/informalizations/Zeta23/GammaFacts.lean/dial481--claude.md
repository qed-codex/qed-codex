---
{
  "module": "Zeta23/GammaFacts.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/GammaFacts.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/GammaFacts.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/

/-
Zeta23/GammaFacts.lean — the even and smooth clauses of H-Γ [eq:mufacts].

Paper [eq:mufacts] asserts: "μ is even, smooth, increasing in |τ|, μ ≥ μ(0) > −1,
μ(τ) = (1/2π)log(|τ|/2π) + O(τ⁻²), μ′(τ) ≪ |τ|⁻¹ (|τ| ≥ 1)" plus [eq:muints].

This file proves the EVEN and SMOOTH clauses against Mathlib's
Complex.digamma (= logDeriv Gamma):
  • digamma_conj : Γ'/Γ commutes with conjugation (from Complex.Gamma_conj +
    deriv_conj_conj);
  • mu_even : μ(−τ) = μ(τ);
  • mu_smooth : ContDiff ℝ ∞ μ (Γ is holomorphic hence analytic on Re > 0,
    so digamma is analytic there; compose with the affine line τ ↦ 1/4 + iτ/2).

The remaining clauses (monotonicity in |τ|, μ(0) > −1, the Stirling asymptotic
with O(τ⁻²), the derivative bound, and [eq:muints]) are the fields of
Zeta23.GammaFacts in Hypotheses.lean; they are proved in the files under
Zeta23/GammaFacts/ and assembled in Zeta23/GammaFacts/Complete.lean (`gammaFacts`).
The route: the digamma partial-fraction series
  digamma z = −γ_E + Σ_{n≥0} (1/(n+1) − 1/(n+z))  on ℂ ∖ (−ℕ)
(Zeta23/GammaFacts/Series.lean), from which monotonicity and μ ≥ μ(0) are termwise
monotonicity of (n+σ)/((n+σ)²+t²) in t², μ(0) > −1 is a finite partial-sum bound,
and the derivative bound is termwise differentiation; the Stirling clause uses a
vertical-line Stirling estimate (Zeta23/GammaFacts/StirlingVert.lean,
Zeta23/Analytic/Stirling.lean), and the integrals [eq:muints] follow by integrating
the asymptotic (Zeta23/GammaFacts/IntMu.lean).
-/
```

### `digamma_conj`

 Γ'/Γ commutes with complex conjugation (from Γ(z̄) = Γ(z)̄). 

### `mu_even`

 [eq:mufacts], "μ is even": μ(−τ) = μ(τ). 

### `gamma_ne_neg_nat`

 The open right half-plane where Γ is holomorphic and nonvanishing. 

### `mu_smooth`

 [eq:mufacts], "μ is smooth": μ ∈ C^∞(ℝ). 
