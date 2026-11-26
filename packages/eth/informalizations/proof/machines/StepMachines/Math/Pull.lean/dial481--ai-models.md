---
{
  "module": "proof/machines/StepMachines/Math/Pull.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/machines/StepMachines/Math/Pull.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/machines/StepMachines/Math/Pull.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 `Network.pull`: a network carried to words of bits along codes (`Code`) of its states and
labels.
A network has nodes with finite sets of states and integer weights W, and for every
pair of nodes an interaction Ψ that is a sum over labels.
Pulling keeps the capacities, hence U; it keeps the value if every word names a state, and the
bounds `Sized P B` if the names
of the states have at most P bits. 

### `pull`

 The network on words: states of a are the words of length n a, labels of {a,b} the words of
length c a b;
the factors vanish at the words that name no label. cl a b is read at a ≤ b only. 

### `sum_pi_dec`

 A sum over tuples of elements is the sum over the tuples of their names. 

### `value_pull`

 If every word of length n a names a state of a (the codes cs are full), the pulled network has
the value of N. 

### `sized_pull_of_le`

 The pulled network has the size of N as soon as the names of the states have at most P bits. 
