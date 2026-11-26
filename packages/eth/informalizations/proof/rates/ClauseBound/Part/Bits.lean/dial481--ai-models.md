---
{
  "module": "proof/rates/ClauseBound/Part/Bits.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/ClauseBound/Part/Bits.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/ClauseBound/Part/Bits.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The least h with p(h) ≥ 2^λ, and the label counts of the pieces made from partitions

For a length λ let h be the least integer ≥ 2 with p(h) ≥ 2^λ, where p counts partitions. In the
proof of Theorem B (Appendix B) the piece number s, |s| ≤ 2h, factors row-wise through R^row_s =
Σ_{i ≤ 2h} p(s + i) labels and
column-wise through R^col_s = Σ_{i ≤ 2h} p(2h − s − i) labels. The file defines h, R^row_s and
R^col_s and proves elementary facts about them and about partition numbers and logarithms:
p(E) ≥ (E + 1)/2, p(1) = 1, h ≥ 2, p(h) ≥ 2^λ, p(h − 1) < 2^λ, R^row_s ≥ 1 and R^col_s ≥ 1 for |s| ≤
2h, κ > 0, and bounds on log₂ and ⌈log₂⌉. 

### `gauss`

 E(E + 1) ≤ 2·(1 + 2 + … + E). 

### `succ_le_two_mul_p`

 p(E) ≥ (E + 1)/2, from the terms k = 1 of the recurrence. 

### `p_one`

 p(1) = 1. 

### `pz`

 p(E) for an integer E; 0 for E < 0. 

### `exists_h`

 Some h ≥ 2 has p(h) ≥ 2^λ. 

### `hOf`

 The least h ≥ 2 with p(h) ≥ 2^λ. 

### `Rrow`

 Σ_{i=0}^{2h} p(s + i). 

### `Rcol`

 Σ_{i=0}^{2h} p(2h − s − i). 

### `two_le_hOf`

 h ≥ 2. 

### `two_pow_le_p_hOf`

 p(h) ≥ 2^λ. 

### `one_le_Rrow`

 R^row_s ≥ 1 for |s| ≤ 2h. 

### `one_le_Rcol`

 R^col_s ≥ 1 for |s| ≤ 2h. 

### `kappa_pos`

 κ > 0. 

### `p_pred_lt`

 p(h − 1) < 2^λ, because h is the least. 

### `logb_le_sqrt_sqrt`

 log₂ E ≤ 4·E^(1/4)/ln 2. 

### `le_two_pow_of_logb_le`

 If log₂ r ≤ y ≤ c then r ≤ 2^c. 

### `clog_le`

 If log₂ r ≤ y then ⌈log₂ r⌉ ≤ y + 1. 

### `logb_succ_le`

 log₂(k·h + 1) ≤ 3 + log₂ h for k ≤ 4 and h ≥ 1. 
