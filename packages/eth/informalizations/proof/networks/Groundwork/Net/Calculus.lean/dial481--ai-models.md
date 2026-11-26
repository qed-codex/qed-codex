---
{
  "module": "proof/networks/Groundwork/Net/Calculus.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/networks/Groundwork/Net/Calculus.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/networks/Groundwork/Net/Calculus.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 The calculus of factorisations. An interaction between two nodes is «factorised» when it is
written as a sum over
labels θ of (a factor that reads one side and θ) times (a factor that reads the other side and θ);
the number of labels is
what the pair costs. Three rules: (a) a product of factorised functions is factorised over the
tuples of labels,
(b) labels may be renamed into a larger type, (c) every function factors through its second
    argument.
Also the number of pairs a < b, and the crossing X = [x=v][y=u] of Section 4 of the paper, a
function of the four
corners of a rectangle, for indices in any type α. 

 ### The calculus 

### `mem_tuples`

 Membership in the set of tuples. 

### `card_tuples`

 The number of tuples. 

### `sum_tuples_prod`

 Distributivity: a sum over tuples of a product is the product of the sums. 

### `prod_factorised`

 (a), for a family: a product of factorised functions is factorised over the tuples of labels, by
the products of the
factors. 

### `sum_renamed`

 (b): labels may be renamed into a larger type, both factors vanishing off the set D of names. 

### `sum_mul_eq`

 (c): every function factors through its second argument. 

 ### The number of pairs 

### `two_mul_card_pairs'`

 The ordered pairs are the pairs a < b, the pairs a > b and the diagonal. 

### `card_pairs`

 The number of pairs a < b. 

 ### The crossing 

### `X`

 X = [x=v][y=u]: opposite corners agree (the two diagonals of a rectangle with x, y on top and u,
v below). 
