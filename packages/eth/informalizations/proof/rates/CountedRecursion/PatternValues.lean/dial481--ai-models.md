---
{
  "module": "proof/rates/CountedRecursion/PatternValues.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/CountedRecursion/PatternValues.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/CountedRecursion/PatternValues.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # W_a and f_{a,a'} as the procedures compute them

For the network `patternNet D c g tr λ y W` (proof of Proposition 3, «Two networks for each ι», with
the pieces of Definition 7):
* `weight_eq`: «W_a is the product of the g table entries of row a and of the factors of the
  straight edges inside row a», in the form of `rowWeight`: the check `chkG`, then the product of
  the entries at the queries `pointQuery`;
* `factor_eq`: f_{a,a'}(z, θ) is `ClauseBound.Alg.gridFf` for the pieces, the form that `rowFactor`
  follows;
* `pair_eq`: Ψ_{a,a'} for a ≠ a', in either order, in the form of `rowPair` (from the statement
  `PairIsProduct`, a hypothesis here);
* the lengths of the strings that are cut out of a setting. From
  `ClauseBound.Alg.GridPresents.gridN_W`, `gridN_f`. 

### `gridOf`

 The network `gridN` of which `patternNet` is made. 

### `mem_S_iff`

 The settings of a row are the strings of g·g²·λ bits. 

### `pointQuery_ok`

 The query to the tables at the grid point number i of the row a is a legitimate one. 

### `weight_eq`

 **W_a**, as `rowWeight` computes it. 

### `c_eq`

 c_{a,a'} is the number `capG` computed from the pieces, the grid and the index y. 

### `factor_eq`

 **f_{a,a'}(z, θ)** is the function `ClauseBound.Alg.gridFf` for the pieces. 

### `pair_eq`

 **Ψ_{a,a'}(z, z')** for a ≠ a', as `rowPair` computes it: the query is put in order, then the
check and the product. 
