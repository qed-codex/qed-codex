---
{
  "module": "Ov/Core/Wire.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/Ov/Core/Wire.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/Ov/Core/Wire.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# The values of a spectral point at wires

The parts of Lemma lem:exponents (`Paper/Tensors.lean`) in the form in which the development cites them, and what follows
at once for tensors whose legs are moved.


### `unit_eq`

 φ(⟨n⟩_P) = n^g with g = log₂ φ(⟨2⟩_P), wherever the legs are. 

### `wire_eq`

 φ(⟨n⟩_pq) = n^(d_φ(p,q)). 

### `wire_two`

 φ(⟨2⟩_pq) = 2^(d_φ(p,q)). 

### `wire_le`

 φ(⟨n⟩_pq) ≤ n^(d_φ(p,q)), also for n = 0. 

### `e_nonneg`

 Distances are not negative. 

### `e_le_one`

 Distances are at most 1. 

### `e_self`

 The distance from a party to itself is 0. 

### `e_comm`

 Distances are symmetric. 

### `push_const_le`

 A tensor with all its legs at one party costs at most 1. 

### `push_le_move`

 Moving legs: if the leg j moves from π' j to π j, the value grows at most by the values of wires
between π j and π' j that have the dimensions of the legs. 

### `pull_e`

 The distances of a pull-back. 
