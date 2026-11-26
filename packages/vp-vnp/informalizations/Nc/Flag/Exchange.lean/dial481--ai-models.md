---
{
  "module": "Nc/Flag/Exchange.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/Nc/Flag/Exchange.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/Nc/Flag/Exchange.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# Section "Flat or contracting", step "Rank one": vectors and matrices of rank one

Linear algebra over F₂ for the proof of Theorem thm:alt (Paper/Alternative.lean). The matrix u xᵀ is `vecMulVec u x`. For
nonzero u₁x₁ᵀ and u₂x₂ᵀ, the matrices W, u₁x₁ᵀ, u₂x₂ᵀ are transversal if and only if u₁, u₂ are independent modulo the column space of W, and x₁, x₂ modulo
its row space (`transversal_vec_iff`). The lemma `connect` joins any two vectors outside a subspace of codimension at least 2 by
steps x ↦ x + y with x, y independent modulo the subspace.


### `Indep2`

 The vectors u₁, u₂ are independent modulo the subspace A: none of u₁, u₂, u₁ + u₂ lies in A. In other words, u₁ is
outside A, and u₂ is outside the span of u₁ with A. 

### `exists_indep2`

 Outside a subspace of codimension at least 2, every vector has a second one that is independent of it. 

### `connect`

 "Such moves connect all vectors outside" a subspace R of codimension at least 2: a function that does not change when x
becomes x + y, for x, y independent modulo R, has one value outside R. 

 ### Matrices u xᵀ 

 ### Independent subspaces 

 ### Transversal matrices of rank one 

### `transversal_vec`

 W and u xᵀ ≠ 0 are transversal if and only if u is outside the column space and x outside the row space of W. 

### `transversal_vec_iff`

 W, u₁x₁ᵀ ≠ 0 and u₂x₂ᵀ ≠ 0 are transversal if and only if u₁, u₂ are independent modulo the column space of W and x₁, x₂
modulo its row space. 

### `transversal_zero`

 The zero matrix is transversal to every matrix. 

### `Transversal.tail`

 The last two of three transversal matrices are transversal. 

### `X_singleton`

 The matrix p·dg{i}·q is u xᵀ for the column u of p and the row x of q with the index i. 
