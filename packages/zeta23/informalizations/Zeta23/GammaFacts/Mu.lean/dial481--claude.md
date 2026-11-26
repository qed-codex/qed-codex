---
{
  "module": "Zeta23/GammaFacts/Mu.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/GammaFacts/Mu.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/GammaFacts/Mu.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/

/-
Zeta23/GammaFacts/Mu.lean — the remaining H-Γ fields from the digamma series.  Canonical text: the paper [eq:mufacts]:
"μ is even, smooth, increasing in |τ|, μ ≥ μ(0) > −1, μ(τ) = (1/2π)log(|τ|/2π)
+ O(τ⁻²), μ′(τ) ≪ |τ|⁻¹ (|τ| ≥ 1)" plus the [eq:muints] integrals.
The ψ-toolkit is developed at a parametrized abscissa
a ∈ (0,1) (covers ζ's a = 1/4 and, composed with the recurrence, Theorem E's
a = 1/4 + κ/2).  Foundation: Zeta23.DigammaSeries.
-/
```

### `abscissa_mem`

 Points a + it with a ∈ (0,1) avoid the integers. 

### `re_term_eq`

 The real part of the n-th series term on the vertical line Re = a. 

### `re_inv_eq`

 Re(1/z) on the line. 

### `summable_re_terms`

 Summability of the real series. 

### `re_digamma_vertical`

 **The real digamma series on vertical lines** (the paper's display in [eq:mufacts]):
Re ψ(a+it) = −γ − a/(a²+t²) + Σₙ (1/(n+1) − (n+1+a)/((n+1+a)²+t²)). 

 ### Monotonicity on the vertical line, and the μ order facts 

### `re_digamma_mono`

 Re ψ(a + it) is monotone in t on t ≥ 0. 

### `mu_eq`

 Bridge to Zeta23.mu: μ(τ) in terms of the parametrized line at a = 1/4, t = τ/2. 

### `mu_monotoneOn`

 [eq:mufacts] "increasing in |τ|": μ is monotone on τ ≥ 0. 

### `mu_zero_le`

 [eq:mufacts] "μ ≥ μ(0)". 

### `neg_one_lt_mu_zero`

 [eq:mufacts] "μ(0) > −1". 

 ### The derivative bound μ′ ≪ 1/|τ|  (via the trigamma series) 

### `trigamma_tail_le`

 Trigamma tail bound on the quarter line: Σ'ₙ ((1/4+n)² + t²)⁻¹ ≤ 12/|t| for |t| ≥ 1/2. 

### `summable_quarter_line`

 Summability of the quarter-line trigamma comparison series. 

### `mu_deriv_bound`

 [eq:mufacts] "μ′(τ) ≪ |τ|⁻¹" (the GammaFacts.deriv_bound field shape). 
