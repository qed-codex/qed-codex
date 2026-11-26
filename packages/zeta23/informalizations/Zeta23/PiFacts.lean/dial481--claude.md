---
{
  "module": "Zeta23/PiFacts.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/PiFacts.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/PiFacts.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/

/-
Zeta23/PiFacts.lean — [eq:PiPfacts], first clause: the pointwise bound for the
pole density Π_X of [eq:Pidef],

    "|Π_X(τ)| ≤ 3√X/(1+|τ|)"        (the paper, [eq:PiPfacts])

proved here for all X ≥ 1 (the paper applies it with X = e^L → ∞, so any
threshold suffices; no threshold is needed), together with continuity of
Π_X(·) (consumed for integrability).  Consumer: Zeta23/PrimeSideA.lean
(LocalHyps.PiX_bound).

Key inequalities: (1+|τ|)² ≤ 5(1/4+τ²) (so 1/|s| ≤ √5/(1+|τ|) for s = ½+iτ),
|X^s − 1| ≤ √X + 1 ≤ 2√X, and 5/(2π) + 2√5/π < 3.
-/
```

### `PiX_bound`

 The paper's [eq:PiPfacts] Π_X-bound in the ∃X₀ packaging used by the
prime side (X₀ = 1 works). 

### `PiX_continuous`

 Continuity of τ ↦ Π_X(τ) for X > 0 (integrability input). 

 ### [eq:Bdef]: the pointwise bound |ν_X(τ)| ≤ B + log⁺(|τ|/4T), B = l + 4√X

Paper (after [eq:deltan]): "We shall use the following pointwise bound for ν_X.
By (eq:mufacts), (eq:PiPfacts) and (eq:cheb1), for T ≥ T₀,
  |ν_X(τ)| ≤ B + log⁺(|τ|/4T)  (τ ∈ ℝ),  |ν_X(τ)| ≤ B  (|τ| ≤ 4T),
  B := l + 4√X,  B² ≪ l² + X."                                        [eq:Bdef]

The μ-part consumes the H-Γ fields, so these lemmas take
hΓ : GammaFacts as a hypothesis — conditional on H-Γ exactly as the paper's §5.
The P_X-part uses the Chebyshev bound Zeta23.Cheb.chebyshevMertens.cheb1b
(paper's literal Σ_{n≤X} Λ(n)/√n ≤ 3√X for X ≥ x₀, absorbed into T₀), so no
Chebyshev hypothesis is needed. 

### `PX_abs_le`

 Triangle inequality for [eq:Pdef]: |P_X(τ)| ≤ (1/π)·Σ_{n≤X} Λ(n)/√n. 

### `B_sq_le`

 [eq:Bdef], last clause "B² ≪ l² + X" in explicit form (unconditional). 

### `B_nonneg`

 0 ≤ B for T ≥ 2π. 

### `nuX_abs_le`

 **[eq:Bdef]**: ∃T₀ ∀ T ≥ T₀ ∀ τ, |ν_X(τ)| ≤ B + log⁺(|τ|/(4T)), with
B := l + 4√X, X := e^{λl}.  Conditional on H-Γ (hΓ); the Chebyshev input is the
proved Zeta23.Cheb.chebyshevMertens. 

### `nuX_abs_le_window`

 [eq:Bdef], window form: |ν_X(τ)| ≤ B for |τ| ≤ 4T. 
