---
{
  "module": "proof/networks/Groundwork/Cross/Bit.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/networks/Groundwork/Cross/Bit.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/networks/Groundwork/Cross/Bit.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 Uncrossing for single bits: the one-bit identity X₁ = I₁ − s ⊗ s (theorem `uncross`), the
crossing of two λ-bit diagonals as the sum
of the λ+1 terms A_i, and the bound |A_i| ≤ 2^λ. The paper's Lemma 2 instead cuts the strings into
blocks of 3 bits and uses the eight-square identity. 

### `uncross`

 One bit of the crossing is I minus s ⊗ s. 

### `cross_eq_prod`

 A λ-bit crossing is the product of its bits. 

### `sum_A`

 Only λ+1 terms: the crossing is A_0 + … + A_λ. 

### `abs_prod_le_one`

 A product of integers of absolute value at most 1 has absolute value at most 1. 

### `abs_sum_powersetCard_le`

 A sum over the sets S of i positions of products of λ integers of absolute value at most 1 has
absolute value at most
C(λ,i) ≤ 2^λ. 

### `abs_A_le`

 At most C(λ,i) ≤ 2^λ terms, each 0 or ±1. 
