---
{
  "module": "proof/networks/Value/Sums.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/networks/Value/Sums.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/networks/Value/Sums.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Sums inside the tables, products by groups, and the sum over θ_{a,b}

Proof of Lemma 1, end of the paragraph «The algorithm». This file proves two of the statements of
proof/networks/Value/Defs.lean:
* `stSumsInside`, «Together with the sums inside the tables»: a product over the groups of sums over
  the settings of the nodes of the group is one sum over the settings of all nodes;
* `stSumOut`, «Each θ_{a,b} occurs only in f_{a,b} and f_{b,a}, and Σ_{θ_{a,b}∈{0,1}^{c_{a,b}}}
  f_{a,b}(z_a, θ_{a,b}) f_{b,a}(z_b, θ_{a,b}) = Ψ_{a,b}(z_a, z_b)»;
and two facts on products, used for the joint sum: every pair of nodes inside a group lies in
exactly one group (`prod_inside`), and the ordered pairs (a, b) with a in the group γ and b outside
it, taken over all γ, are the unordered pairs of nodes in different groups, each in both orders
(`prod_across`). 

### `stSumsInside`

 «Together with the sums inside the tables»: every node lies in exactly one group, so a family
(z_γ)_γ of settings of the groups is one choice z of a setting for every node. 

### `prod_inside`

 The pairs {a, b} inside the group γ, over all γ, are the pairs of nodes in the same group. 

### `prod_across`

 The ordered pairs (a, b) with a in the group γ and b outside it, over all γ, are the pairs {a,
b} of nodes in different groups, each in both orders. 

### `stSumOut`

 «Each θ_{a,b} occurs only in f_{a,b} and f_{b,a}, and Σ_{θ_{a,b}∈{0,1}^{c_{a,b}}} f_{a,b}(z_a,
θ_{a,b}) f_{b,a}(z_b, θ_{a,b}) = Ψ_{a,b}(z_a, z_b)»: the sum over all θ of the product over the
pairs is the product over the pairs of the sums, each sum is Ψ_{a,b}(z_a, z_b), and the pairs in the
same group and the pairs in different groups are all pairs. 
