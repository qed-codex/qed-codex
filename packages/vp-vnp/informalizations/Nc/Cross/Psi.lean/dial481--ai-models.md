---
{
  "module": "Nc/Cross/Psi.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/Nc/Cross/Psi.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/Nc/Cross/Psi.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# The determinant `Ψ`

Four sites `a, b, c, d`; a word at a site is a pair (rows, columns) of tuples of natural numbers. `Ψ` is the
determinant of a matrix over `ℤ[x]`, `y = x²`, with the blocks (rows `a, d | c, b`, columns `a, d | c, b`)
`ad: C`, `cb: -(y-1)C`, `ac: Λ`, `ab: (y-1)ΛB`, `dc: BᵀΛ`, `db: -Λ`, and minus the transposes.


### `Wd`

 Words: rows and columns at a site. 

### `blX`

 The block of rows and columns at `a, d`: the paper's `M₁`. 

### `blY`

 The block of rows and columns at `c, b`: the paper's `M₂`. 

### `blU`

 The block of rows at `a, d` and columns at `c, b`. 

### `matM`

 The paper's matrix **M**, with the rows and the columns in the order `a, d | c, b`. 

### `psi`

 The paper's `Ψ = det M`. 

### `facA`

 The paper's `F`: the rows `([r = i])_{r<K}` for `i ∈ I_a` and `(B(r,i))_{r<K}` for `i ∈ I_d`. 

### `facB`

 The paper's `G`: the columns `([r = j])_{r<K}` for `j ∈ J_c` and `((y−1)B(r,j))_{r<K}` for `j ∈ J_b`. 

### `dvd_det_sub`

 Congruent matrices have congruent determinants. 
