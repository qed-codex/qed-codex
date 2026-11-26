---
{
  "module": "ThreeSumApsp/TimeClaims/Sec3/Arithmetic.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/TimeClaims/Sec3/Arithmetic.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/TimeClaims/Sec3/Arithmetic.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# The arithmetic behind the running-time claims of Section 3

Elementary inequalities that the deductions between running-time claims use silently.

* `⌈n^{1/3}⌉ ≥ 1` and `(log s + 1)^e ≥ 1`.
* Thin instances, `n ≥ D^18` (Theorem 5, Corollaries 15, 16 and 26): the overheads `n D`, `n² / √D`
  and `1` are at most `n² / D^a`, and so at most the bounds `n² log² D / D^{1/18}` and
  `n² / D^{0.063}`.
* The pieces into which Corollary 15 splits `W` have at most `n² / √D` query pairs (`splitCap_le`).


 ## Two quantities that are at least 1 

### `one_le_cbrtCeil`

 `⌈n^{1/3}⌉ ≥ 1` for `n ≥ 1`. 

### `one_le_log_add_one_pow`

 `(log s + 1)^e ≥ 1`. 

 ## Thin instances: `n ≥ D^18` 

### `mul_rpow_le_of_pow_le`

 `D^{1+a} ≤ n` for `a ≤ 17`. 

### `mul_le_sq_div_rpow`

 Writing the matrices: `n D ≤ n² / D^a`. 

### `one_le_sq_div_rpow`

 `1 ≤ n² / D^a`. 

### `sq_div_sqrt_le_sq_div_rpow`

 `n² / √D ≤ n² / D^a` for `a ≤ 1/2`. 

### `one_le_sq_div_sqrt`

 `1 ≤ n² / √D`. 

### `sq_div_rpow_le_sq_mul_log_sq_div`

 The factor `log² D` of Theorem 5 is at least 1: `n² / D^a ≤ n² log² D / D^a` for `D ≥ 3`. 

### `mul_le_thinBound`

 Writing the matrices costs at most the bound of Theorem 5: `n D ≤ n² log² D / D^{1/18}`. 

### `one_le_thinBound`

 `1 ≤ n² log² D / D^{1/18}`. 

### `sq_div_sqrt_le_thinBound`

 Reading `n² / √D` answers costs at most the bound of Theorem 5:
`n² / √D ≤ n² log² D / D^{1/18}`. 

 ## The pieces of Corollary 15 

### `splitCap_le`

 A piece has at most `n² / √D` query pairs. 

### `rpow_le_sqrt_mul_log_sq`

 `D^{1/18} ≤ √D log² D` for `D ≥ 3`. 

### `add_one_le_splitBound`

 The overhead `w + 1` is at most the bound of the general case of Corollary 15:
`w + 1 ≤ (n² + w √D) log² D / D^{1/18}`. 

### `sq_div_rpow_le_wantedBound`

 The second term of the bound of Corollaries 16 and 26 is at most the bound. 

### `one_le_wantedBound`

 `1 ≤ w D^{0.437} + n² / D^{0.063}`. 
