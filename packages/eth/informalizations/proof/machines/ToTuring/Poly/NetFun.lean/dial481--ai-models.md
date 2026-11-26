---
{
  "module": "proof/machines/ToTuring/Poly/NetFun.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/machines/ToTuring/Poly/NetFun.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/machines/ToTuring/Poly/NetFun.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 Certificates that functions of the program that merges the nodes of a network on [g] into K
groups (the grouping of Lemma 1) are polynomial-time (`PolyT`). `Unary f` says
that f is polynomial-time even with its value written in unary. Certificates of helper functions are
stated for arbitrary
polynomial-time arguments, so that the tactic `fun_prop` can use them; those that need the
hypothesis `Np.Keeps` are found by
`fun_prop (disch := assumption)`. 

 ### General list and number functions 

### `foldr_max_polyT`

 The largest number of a list. 

### `unary_sum_map`

 A sum of unary numbers over a polynomial-time list is unary. 

 ### The functions of the program 

### `n_polyT`

 The lengths of the states, in binary. 

### `cap_polyT`

 The lengths of the labels, in binary. 

### `capWord`

 The label with number u.2 of the pair with number u.1.2. 
