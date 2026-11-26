---
{
  "module": "Ov/Core/Unit.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/Ov/Core/Unit.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/Ov/Core/Unit.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# Unit tensors and wires

Relations between unit tensors, whose legs may be at any parties, also several at one party, and between wires. They are
what the proof of Lemma lem:exponents (`Paper/Tensors.lean`) uses.


### `eq_rpow_of_mul_mono`

 A function f ≥ 1 on the positive integers that is multiplicative and monotone is a power function:
f(n) = n^e with e = log₂ f(2). 

 ### Unit tensors 

### `unit_val_of`

 The entry of a unit tensor at equal indices is 1. 

### `unit_val_not`

 The other entries of a unit tensor are 0. 

### `Restr.unit_mono`

 A smaller unit tensor is a restriction of a larger one. 

### `Equi.unit_mul`

 The product of the unit tensors of sizes m and n is the one of size m·n. 

### `Equi.unit_one`

 The unit tensor of size 1 is 1. 

### `Equi.push_unit`

 Several legs of a unit tensor at one party are as good as one leg. 

### `Equi.push_unit_congr`

 A pushed unit tensor depends only on the set of parties that hold a leg. 

### `Restr.push_const`

 A tensor with all its legs at one party is a restriction of 1. 

 ### Wires 

### `Equi.wire_comm`

 A wire may be read in both directions. 

### `Restr.wire_self`

 A wire with both ends at one party is a restriction of 1. 

### `Equi.wire_mul`

 Two parallel wires are one wire, whose dimension is the product. 

### `Equi.wire_one`

 A wire of dimension 1 is 1. 

### `Restr.wire_trans`

 The wire from p to q is a restriction of the product of the wires from p to r and from r to q. 

### `Restr.move`

 Moving legs: the leg j can be moved from π' j to π j through a wire of its dimension. 

### `one_le_unit`

 F of a pushed unit tensor of size at least 1 is at least 1. 

### `unit_le`

 F of a unit tensor that has a leg is at most its size. 
