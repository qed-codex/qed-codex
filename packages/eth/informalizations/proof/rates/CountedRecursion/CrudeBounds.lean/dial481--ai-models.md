---
{
  "module": "proof/rates/CountedRecursion/CrudeBounds.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/CountedRecursion/CrudeBounds.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/CountedRecursion/CrudeBounds.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The crude bounds

Proof of Theorem A (b), the step from ℓ to ℓ + 1: crude bounds give L ≤ N + 1, B' ≤ N + g²B₁, g(P +
B₁) ≤ Ξ^{c+4} and K(L + B') ≤ Ξ^{c+5}. Here N = g⁴λ, P = g³λ, B₁ = gB + g²(2λ)^c, B' = ⌈2gP/K⌉ +
g²B₁, Ξ = g²(λ + B).
* `crude_plain`: the last three, for all numbers 3 ≤ K ≤ g and every L ≤ N + 1. With s = λ + B: each
  of the three terms of g(P + B₁) is at most Ξ^c·g⁴s, and 3 ≤ g⁴s³; each of the five terms of g(2N +
  1 + g²B₁) is at most Ξ^c·g⁵s, and 5 ≤ g⁵s⁴.
* `crudeBounds : CrudeBounds`: at K = K_ℓ, g = g_ℓ. 

### `crude_first`

 B' ≤ N + g²B₁: ⌈2N/K⌉ ≤ N. 

### `crude_second`

 g(P + B₁) in plain variables: s is λ + B, T is (2λ)^c, E is Ξ^c. 

### `crude_third`

 g(2N + 1 + g²B₁) in plain variables. 

### `crude_plain`

 The crude bounds for all numbers 3 ≤ K ≤ g. 

### `crudeBounds`

 **Crude bounds give L ≤ N + 1, B' ≤ N + g²B₁, g(P + B₁) ≤ Ξ^{c+4} and K(L + B') ≤ Ξ^{c+5}**: the
last three, for every L ≤ N + 1. 
