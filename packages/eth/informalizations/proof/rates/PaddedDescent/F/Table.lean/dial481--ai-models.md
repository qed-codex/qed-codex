---
{
  "module": "proof/rates/PaddedDescent/F/Table.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/PaddedDescent/F/Table.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/PaddedDescent/F/Table.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Explicit tables (StT1, StT2, StT3a, StT3b, StT3c)

Z reads an instance only at well-formed queries; a table made by `tabulate` answers every
well-formed query like the function it was made
from; it is well-formed (`WF`); the word of a well-formed instance is short; its entries are bounded
in the sense of `BoundedInst`. 

### `stT1`

 T1: Z reads an instance only at well-formed queries. 

### `block_flatten`

 The j-th block of a concatenation of words of length ℓ. 

### `skip`

 The numbers 0, 1, … without v. 

### `flatten_skip`

 An empty word may be left out of a concatenation. 

### `stT2`

 T2: a table made by `tabulate` answers every well-formed query like F. 

### `unflat_wf`

 `unflat` of a word of the right length is a well-formed query. 

### `stT3a`

 T3a: a tabulated instance is well-formed. 

### `stT3b`

 T3b: the word of a well-formed instance is short. 

### `stT3c`

 T3c: the entries of a well-formed instance are bounded, in the form that `sideN_sized` asks for. 
