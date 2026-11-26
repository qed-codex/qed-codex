---
{
  "module": "proof/machines/Tower/Toy/Spec.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/machines/Tower/Toy/Spec.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/machines/Tower/Toy/Spec.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # A toy recursion: the sum

What the proofs of Toy/Meets.lean need about `sumF`: it is the sum over all bit strings of length ℓ,
it reads only the entries of these strings, it is at most 2^ℓ times the largest entry, and the value
of a callee is the sum over the strings that begin with its bit. 

### `sumF_eq`

 F(ℓ, f) is the sum of f over all bit strings of length ℓ. 

### `sumF_congr`

 F(ℓ, f) reads only the entries of the strings of length ℓ. 

### `sumF_le`

 F(ℓ, f) is at most 2^ℓ times a bound on the entries. 

### `val_child`

 The value of a callee is the sum over the strings that begin with its bit. 
