---
{
  "module": "proof/rates/CountedRecursion/RowWeightRun.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/CountedRecursion/RowWeightRun.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/CountedRecursion/RowWeightRun.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The procedure for W_a

`rowWeight_within`: on a setting z of the row a, the procedure `rowWeight` returns W_a(z) of the
network of the pattern within g·(tq + 1) operations, if a query to the tables of the clique costs
tq: «W_a is the product of the g table entries of row a and of the factors of the straight edges
inside row a» (proof of Proposition 3). The bound on the states is explicit.
Also here: what the procedures that compute the network of a pattern have in common (the oracle,
sizes of answers). 

### `upOracle`

 The oracle of the procedures: the tables of the clique on g² nodes, and the pieces. 

### `size_answer`

 An integer below 2^n in absolute value, as an answer, has size at most n + 2. 

### `size_lt_le`

 A counter below n has size at most the size of n. 

### `size_two_pow_pow`

 The size of (2^n)^k. 

### `answersOf_eq`

 A legitimate query to the tables is answered by the entry. 

### `dig_mem`

 ι(q) is in 𝓘. 

### `rowWeight_within`

 **The procedure for W_a.** 
