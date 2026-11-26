---
{
  "module": "proof/machines/ToTuring/Poly/Count.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/machines/ToTuring/Poly/Count.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/machines/ToTuring/Poly/Count.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 The network of a k-CNF of Section 6 and of the proof of Theorem A (c) (clauses cut into g
groups, one bit for each literal slot, one-bit equality
wires), defined in StepMachines/Prog/CountNet.lean (functions) and Prog/Count.lean (`satP`). The
plain functions that define it are
polynomial-time (`PolyT`). Its two
lengths, the state bits of a node (`n_unary`) and the label bits of a pair of nodes (`capF_unary`),
are `Unary`. 

### `wF_polyT`

 The weight of a group of clauses at a state word is polynomial-time. 

### `fF_polyT`

 The factor of two groups of clauses at a state word and a label word is polynomial-time. 

### `capF_unary`

 The number of label bits of two groups is given in unary: it is the length of the list of their
links. 

### `mu_le_length`

 A group has at most as many clauses as the formula, for every g (`mu_le` of
StepMachines/Prog/CountNet.lean needs 0 < g). 

### `n_unary`

 The number of state bits of a group is given in unary. 

### `satP_keeps`

 The network `satP g k` of a k-CNF cut into g groups (Section 6, proof of Theorem A (c))
satisfies `Keeps`: its weights `W` and label
factors `f` are polynomial-time, and its lengths `n` and `cap` are unary. 
