---
{
  "module": "Nc/Cross/Near.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/Nc/Cross/Near.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/Nc/Cross/Near.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# States, and the terms of the expansion of `det [[X, AΛB],[B'ΛA', Y]]`

The definitions for the step "The coefficients" of the proof of Proposition prop:identity; the step itself is in
Paper/Identity.lean (Paper.prop_identity_schur to Paper.prop_identity_near). In the paper's letters `X = M₁`, `Y = M₂`, `A = F`,
`A' = F′`, `B = G`, `B' = −G′` and `Λ = D`.


### `en`

 The energy `∑ (2i+1)` of a set. 

### `pairs`

 The states of energy at most `E`. 

### `topRows`

 The upper rows `(X, 0, A, 0)` and `(0, Y, 0, B')` of the big matrix. 

### `lowRows`

 The parts `(0, −B, 0, 0)` and `(−A', 0, 0, 0)` of the lower rows, without the factors from `Λ`. 

### `unitRows`

 The parts of the lower rows with the entry 1. 

### `termMat`

 The matrix of the term of `T`: in the lower rows in `T` the first part is taken, in the others the entry 1. 

### `cgrp`

 Columns of the first group. 

### `rgrp`

 Rows of the first group. 

### `termMat_eq_glue`

 The matrix of a term falls into two blocks: one made of `X, A, A'` and one made of `Y, B, B'`. 

### `enT`

 The paper's `E(T)`, for `T = (T₁, T₂)`. 

### `goodT`

 The `T` with `|T₁| = |T₂|` and `E(T) ≤ N`: the terms that contribute to the coefficient of `x^N`. 
