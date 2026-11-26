---
{
  "module": "Nc/Cross/Split.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/Nc/Cross/Split.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/Nc/Cross/Split.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# Determinants that factor, and the expansion of `det [[X, AΛB],[B'ΛA', Y]]`

Rows and columns fall into two groups. For every set `T` of inner indices the expansion has a term
`∏_T λ · α_T · β_T`, where `α_T` depends on `X, A, A'` and `β_T` on `Y, B, B'` only; it vanishes unless
`T` has as many elements on the left as on the right.


### `glueMat`

 The matrix with the entries of `N₁` in the rows and columns of the first group, those of `N₂` in the rows
and columns of the second, and zeros elsewhere. 

### `det_glue`

 A glued determinant is a product. 

### `det_expand`

 Expansion of a determinant in the rows `λ_r v_r + e_r`. 
