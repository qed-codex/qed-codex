---
{
  "module": "Nc/Flag/Para.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/Nc/Flag/Para.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/Nc/Flag/Para.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# Section "Flat or contracting": quadrangles in a metric on the matrices over F₂

Definitions and lemmas for the proof of Theorem thm:alt (Paper/Alternative.lean). `nn w a W` is the paper's
n_a(W) = |a, a+W|², `BB w a W W'` is its B_a(W, W'), and `X p q S` is the matrix p·dg(S)·q: the matrices `X p q S` for
disjoint sets S, in one frame (p, q), are the transversal families (Nc/Flag/Transversal.lean).


### `Mt`

 Square matrices over F₂. 

### `defect`

 The squared sides minus the squared diagonals of the quadrangle a, a+M, a+M+N, a+N. 

### `nn`

 The squared distance n_a(M) from `a` to `a + M`. 

### `X`

 The matrix of a set of indices in a frame. 

### `exists_factor`

 Every matrix is diagonal with entries 0 and 1 in some frame. 

### `MD`

 The sum of |a, a + p·E·q|² over all a and all invertible p, q. 

### `sum_all_defect`

 The defects of the quadrangles with sides W = X p q S and W' = X p q T, added over all frames and all a. 

### `BB`

 The scalar product B_a(M, N) = ½(n_a(M+N) − n_a(M) − n_a(N)). 
