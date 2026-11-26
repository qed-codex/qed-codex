---
{
  "module": "ThreeSumApsp/Spec/Sec5/Corollary40/Outputs.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Spec/Sec5/Corollary40/Outputs.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Spec/Sec5/Corollary40/Outputs.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# The output of uMv-hinted uMv, in terms of integer matrix products

Proof of Corollary 40: "We compute over ℤ with 0/1 matrices; a Boolean entry is 1 exactly when the
corresponding integer entry is positive."  A data structure for thin matrix products returns entries
of integer products.  The output `(U N_{I,J} V)_{i,j}` of uMv-hinted uMv is true exactly if, for
some `ℓ` with `V[ℓ, j] = 1`, the entry `(i, ℓ)` of the integer product `U N_{I,J}` is not 0
(`uMvHintedOutput_eq`).

The paper cuts "the n rows of U into n/t₂ blocks of t₂ rows".  `rowsFrom X s t` is the block of the
`t` rows of `X` from the row `s` on; the entries of its product with `Y` are entries of `X Y`
(`rowsFrom_mul`).  The data structure asks for a bound on the entries of its inputs;
`Corollary40.abs_toInt_le` and `abs_rowsFrom_le` give it.


 ## 0/1 matrices 

### `boolMul_eq_true_iff_ne_zero`

 An entry of a Boolean product is true exactly if the entry of the integer product is not 0. 

 ## The output of uMv-hinted uMv 

### `uMvHintedOutput_eq`

 "In Phase 4, (U N_{I,J} V)_{i,j} = ∑_{ℓ=1}^{t₂} (U N_{I,J})_{i,ℓ} V_{ℓ,j} is a sum of at most t₂
entries of XY".  The output is true exactly if for some `ℓ` with `V[ℓ, j] = 1` the entry `(i, ℓ)` of
`U N_{I,J}` is not 0. 

 ## Blocks of rows 

### `rowsFrom`

 The `t` rows of a matrix from the row `s` on. 

### `rowsFrom_mul`

 An entry of the product of a block of rows with `Y` is an entry of `XY`. 

### `abs_rowsFrom_le`

 A bound on the entries of a matrix bounds the entries of a block of its rows. 
