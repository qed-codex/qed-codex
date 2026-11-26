---
{
  "module": "proof/rates/CountedRecursion/PatternIs.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/CountedRecursion/PatternIs.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/CountedRecursion/PatternIs.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # «Definition 2 holds with B₁ = gB + g²(2λ)^c in the role of B»

Proof of Theorem A (b): in the display of c_{a,a'} we have c^row_{ι(q)} ≤ 2λ, so P = g³λ, gP = N,
and moreover c_{a,a'} ≤ g²λ = P/g; by Definition 7 (c), Definition 2 holds with B₁ = gB + g²(2λ)^c
in the role of B.
* `pattern_c_le`: c_{a,a'} ≤ g²λ;
* `abs_weight_lt`, `abs_factor_lt`, `abs_pair_lt`: all values are below 2^{B₁}, strictly: a weight
  is a product of g entries below 2^B; the other values do not depend on the tables, so the bound
  for tables that are 0 (`sized_zero`) applies to them; the bound then holds with room to spare,
  since gB ≥ 1;
* `pattern_is`: the network is a network with the parameters P = g³λ and B₁. 

### `pattern_c_le`

 «c_{a,a'} ≤ g²λ». 

### `sized_zero`

 The network for tables that are 0: its sizes, from `gridN_sized`. 

### `pow_lt_bitsOne`

 2^{g²(2λ)^c} is below 2^{B₁}. 

### `abs_factor_lt`

 |f_{a,a'}| < 2^{B₁}. 

### `pair_fact`

 Ψ is the sum over θ ∈ {0,1}^{c_{a,a'}} of the products of the two functions of the
factorization. 

### `abs_pair_lt`

 |Ψ_{a,a'}| < 2^{B₁}. 

### `abs_weight_lt`

 |W_a| < 2^{B₁}: a product of g entries below 2^B. 

### `pattern_is`

 **The network is a network with the parameters P = g³λ and B₁ = gB + g²(2λ)^c.** 
