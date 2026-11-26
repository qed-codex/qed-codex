---
{
  "module": "Zeta23/ThmD/PP.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/ThmD/PP.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/ThmD/PP.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/

/-
Zeta23/ThmD/PP.lean
The single changed proof step of §7.1 (the paper, text preceding [eq:ratio-general]):
  "the last step of Proposition [prop:PP] is replaced by partial summation from [eq:cheb2]:
   since |g'| ≤ ‖(φ²)'‖₁ ≤ 2,
   Σ_{n≤X} a_n² g(y_n) = ∫_0^L g(y)·y dy + O(L²) = (L³/2)·J + O(L²)."
Generic in g.  Hypothesis on g:
g is taken C¹ with |g'| ≤ 2 (exactly the paper's "since |g'| ≤ 2") rather than Lipschitz-2 —
this matches Mathlib's Abel summation formula (sum_mul_eq_sub_integral_mul₀) directly, and the
concrete g_D = φ_D² ⋆ φ_D² is C¹ with |g_D'| ≤ ‖(φ_D²)'‖₁ ≤ 2 (Window.lean).
Consumed by the FactsD instance for the Montgomery–Taylor window (sumJ field).
-/
```

### `abel_sum_close`

 **The partial-summation step, abstract in the weights** (Abel summation): for any weight
sequence 'c' with c 0 = c 1 = 0 whose partial sums satisfy the [eq:cheb2a]-shape
|Σ_{k≤t} c k − (log t)²/2| ≤ C₀ log t (t ≥ 2), and any C¹ g with |g'| ≤ 2, g ≡ 0 on [L,∞):
  Σ_{n≤X} c n · g(log n) = ∫_0^L g(y)·y dy + O(L²),   X = e^L.
(Instances: c n = Λ(n)²/n — 'sumA2g_close' below, ζ; and c n = Λ(n)²/n·1_{(n,q)=1} — the
Dirichlet-character version in Zeta23/ThmDE/, from [eq:cheb2a] for n coprime to q.) 

### `sumA2g_close`

 **[thm:D proof], the partial-summation step** (replaces [eq:gbounds]+sandwich):
for any C¹ weight g with |g'| ≤ 2 and g ≡ 0 on [L, ∞),
  Σ_{n≤X} Λ(n)²/n · g(log n) = ∫_0^L g(y)·y dy + O(L²),   X = e^L
(from [eq:cheb2] by Abel summation). 
