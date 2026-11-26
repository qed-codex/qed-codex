---
{
  "module": "proof/rates/ClauseBound/Boson/Text.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/ClauseBound/Boson/Text.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/ClauseBound/Boson/Text.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The matrices `op` and the operators a[r] of the paper

This file shows that the matrices `op`, defined by recursion, are those of the operators a[r] that
Appendix B of the paper defines on the polynomial ring: the entry `op a r π σ` is the coefficient of
t^π in a[r]·t^σ. 

 # The matrices are those of the operators of the paper

The ring is ℤ[t₀, t₁, …] (the paper: ℚ[t₁, t₂, …]; t₀ is not used, and all coefficients are
integers). ∇₋ₗ is the multiplication by t_l and ∇ₖ = k·∂/∂t_k. For a tuple of nonzero integers,
`nord` is the product of the ∇ with negative index times the product of the ∇ with positive index,
the latter applied first. The paper defines a[r], for a monomial a with the parts a₁, …, a_q, as the
sum over
all tuples (k₁, …, k_q) of nonzero integers with sum −r of ∏ C(−k_i − 1, a_i − 1) times this
product. For every M that is at least the weights of π and σ, the sum over the tuples with entries
between
−M and M, applied to t^σ, has as its coefficient of t^π the entry `op a r π σ` of the matrix that
was defined by recursion (`op_eq_sum`). 

### `Rg`

 The ring. 

### `mon`

 The monomial t^μ. 

### `coef`

 The coefficient of t^μ. 

### `nabPos`

 ∇ₖ = k·∂/∂t_k for k ≥ 1. 

### `nord`

 ∏_{k_i < 0} ∇_{k_i} · ∏_{k_i > 0} ∇_{k_i}, applied to f. 

### `wt`

 ∏_i C(−k_i − 1, a_i − 1). 

### `win`

 The nonzero integers between −M and M. 

### `tup`

 The tuples of q nonzero integers between −M and M. 

### `sum_win`

 A sum over the window. 

### `sum_tup_succ`

 A sum over the tuples of length q + 1. 

### `coef_X_mul`

 The coefficients of t_l·f. 

### `nabPos_mon`

 ∇ₖ on a monomial. 

### `nord_cons_neg`

 A negative index: one more multiplication, on the left. 

### `nord_cons_pos`

 A positive index: one more differentiation, applied first. 

### `op_eq_sum`

 The entry of the matrix defined by recursion is the coefficient of t^π in a[r]·t^σ, with a[r]
the sum over tuples of the paper. 
