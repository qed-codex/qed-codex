---
{
  "module": "proof/consequences/GraphProblems/SetTM.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/consequences/GraphProblems/SetTM.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/consequences/GraphProblems/SetTM.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Instances, codes and polynomial-time readers, used for Turing machines for problems on graphs

The type `Inst` of instances (a graph on n vertices and a number s ≤ n), the lengths of the codes
`codeWith G s` and `code G`, the word `nzW` of the bit «not zero», the fact that `nzW` and the
binary digits `Nat.bits` are computed in polynomial time, and the reader `readF`, which splits a
word by `read2` and applies a formula F, computed in polynomial time, to the length of the
first part and to the last part; `readF_polyT` says that `readF` is computed in polynomial time. 

### `Inst`

 The instances: a graph on n vertices and s ≤ n. 

### `length_codeWith`

 The length of the code. 

### `nzW`

 The bit «not zero», as a word. 

### `readF`

 The reader for a formula F. 
