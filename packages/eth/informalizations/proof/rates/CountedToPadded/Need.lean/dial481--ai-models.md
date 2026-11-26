---
{
  "module": "proof/rates/CountedToPadded/Need.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/CountedToPadded/Need.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/CountedToPadded/Need.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The number e′ and the exponent

Proofs of `CutNumberFacts`, `PrecisionCarriesOver`, `NeedSuffices` and `NeedIsSmall` (Defs.lean). 

### `length_unary`

 n in unary has n units. 

 ### The number e′ 

### `one_le_logK`

 log K_ℓ ≥ 1. 

### `e_pos`

 e_ℓ > 0. 

### `den_pos`

 The denominator is not 0. 

 ### Rounding up, and the number of bits 

### `le_ceilMul`

 ⌈min(a/b, 1)·n⌉ from below, for b > 0. 

### `ceilMul_le`

 ⌈min(a/b, 1)·n⌉ from above, for b > 0. 

### `size_le_log`

 A number m ≥ 1 has at most log m + 1 bits. 

 ### The exponent 

### `needOf_eq`

 The exponent at the index (ℓ, k), written out. 

### `cutNumberFacts`

 The number e′ lies in [e, 2e], is positive and at most 1, and is computed as the fraction
`cutFraction num`. 

### `precisionCarriesOver`

 A precision function for e is one for e′, with twice the constant. 

### `needSuffices`

 2^need is at least 4 times the printed bound for e′, C₀ and B + 1. 

### `needIsSmall`

 need ≤ e′K²λ + (2C₀ + 1)·K²·log(K(λ + B)). 
