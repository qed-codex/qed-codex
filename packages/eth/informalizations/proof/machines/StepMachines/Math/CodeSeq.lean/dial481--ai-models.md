---
{
  "module": "proof/machines/StepMachines/Math/CodeSeq.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/machines/StepMachines/Math/CodeSeq.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/machines/StepMachines/Math/CodeSeq.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 Tuples coded by words cut into chunks of various lengths: the entry at i is decoded from chunk
number pos i, and chunk
number κ has length n κ and starts at the offset Σ_{κ' < κ} n κ'. 

### `chunkAt`

 The chunk number κ of a word cut into chunks of lengths n 0, n 1, … 

### `chunk_ext`

 A word of the full length is known by its chunks. 

### `exists_chunks`

 Every list of chunks of the right lengths comes from a word. 

### `seq`

 The code of the tuples that have an entry of T i at every i with P i and d elsewhere, where pos
numbers the i with P i
by 0, …, r - 1: a word of Σ_{κ < r} n κ bits whose chunk number pos i is a code word in Dk i,
decoded by deck i. 

### `length_chunkAt`

 The length of a chunk of a word of the full length. 
