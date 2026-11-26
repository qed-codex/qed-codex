---
{
  "module": "proof/consequences/GraphProblems/Read.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/consequences/GraphProblems/Read.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/consequences/GraphProblems/Read.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Corollary 7: reading the input word

The word of a graph is n in unary, possibly s in unary, and the n² entries of the adjacency matrix
row by row. This file shows that `read1` and `read2` recover n, s and the matrix from the word, that
the
matrix has n² entries, and that the entry u·n + v of the matrix says whether u and v are adjacent. 

### `ones_unary_append`

 The number of ones at the start of 1ᵐ0x is m. 

### `rest_unary_append`

 What follows the first ones and the zero that ends them in 1ᵐ0x is x. 

### `getD_flatMap`

 In a list of rows of length n written one after the other, the entry i·n + j is the entry j of
row i. 

### `stRead1`

 `read1` recovers n and the matrix from the word of a graph. 

### `stRead2`

 `read2` recovers n, s and the matrix from the word of a graph and a number. 

### `stAdj`

 The entry u·n + v of the matrix is 1 if and only if u and v are adjacent. 

### `stMatrixLength`

 The matrix has n² entries. 
