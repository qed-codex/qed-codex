---
{
  "module": "Nc/Flag/Transversal.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/Nc/Flag/Transversal.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/Nc/Flag/Transversal.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# Section "Flat or contracting": transversal matrices

"We call W₁, W₂, … transversal if both their column spaces and their row spaces are independent." The theorem
`transversal_iff` says that this holds if and only if, for some invertible p and q, W_k = p·dg(S_k)·q with disjoint sets S_k.


### `colSpace`

 The column space of a matrix. 

### `rowSpace`

 The row space of a matrix. 

### `Transversal`

 "We call W₁, W₂, … transversal if both their column spaces and their row spaces are independent." 

### `trU`

 The transpose of an invertible matrix. 

### `colSpace_X`

 The column space of p·dg(S)·q is spanned by the columns of p in S. 

### `exists_glm_col`

 Linearly independent vectors are columns, at given places, of an invertible matrix. 

### `exists_glm_row`

 Linearly independent vectors are rows, at given places, of an invertible matrix. 

### `transversal_iff`

 Matrices are transversal if and only if in some frame (p, q) they are diagonal, with entries 0 and 1 and with
disjoint supports. 
