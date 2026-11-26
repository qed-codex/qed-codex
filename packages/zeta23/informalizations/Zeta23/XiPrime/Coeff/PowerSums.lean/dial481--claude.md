---
{
  "module": "Zeta23/XiPrime/Coeff/PowerSums.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/XiPrime/Coeff/PowerSums.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/XiPrime/Coeff/PowerSums.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/

/-
Zeta23/XiPrime/Coeff/PowerSums.lean — Σ_{N ≤ e^u} f(N)/N for Dirichlet powers f = Λ^{∗m}.

  Sdiv f u := Σ_{N ≤ e^u} f(N)/N.
  Recursion (from Coeff/Swap):      Sdiv (g ∗ f) u = Σ_{d ≤ e^u} g(d)/d · Sdiv f (u − log d).
  Chebyshev–Mertens upper bound:    Sdiv (Λ^{∗m}) u ≤ (u + m·K)^m / m!      (u ≥ 0; K = log 4 + 4),
by induction on m, each step being Coeff/Abel.mertens_step applied to the decreasing polynomial
v ↦ (u + mK − v)^m/m!  ([XF′ Remark 7.2]: "M_j(u) ≤ (u+2jC)^j/j! by induction from Mertens").
-/
```

### `Sdiv`

 Sdiv f u := Σ_{N ≤ e^u} f(N)/N. 

### `Sdiv_one`

 Sdiv δ u = 1 for u ≥ 0. 

### `Sdiv_mul`

 the recursion  Sdiv (g∗f) u = Σ_{d ≤ e^u} g(d)/d · Sdiv f (u − log d). 

### `integral_const_sub_pow`

 the polynomial-with-shift integral:  ∫₀ᵘ (c − v)^n dv = (c^{n+1} − (c−u)^{n+1})/(n+1). 

### `pow_add_mul_pow_le`

 binomial inequality  a^{m+1} + (m+1)·a^m·b ≤ (a+b)^{m+1}  for a, b ≥ 0. 

### `Sdiv_lamPow_le`

 **Chebyshev–Mertens bound for the Dirichlet powers:**  Σ_{N ≤ e^u} Λ^{∗m}(N)/N ≤ (u + mK)^m/m!. 

### `Sdiv_mono`

 monotonicity in u of Sdiv for f ≥ 0. 

### `Sdiv_lam_le`

 the Mertens bound itself in Sdiv form: Sdiv Λ u ≤ u + K. 
