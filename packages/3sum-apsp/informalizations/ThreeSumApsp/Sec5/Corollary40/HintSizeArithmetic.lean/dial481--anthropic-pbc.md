---
{
  "module": "ThreeSumApsp/Sec5/Corollary40/HintSizeArithmetic.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Sec5/Corollary40/HintSizeArithmetic.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Sec5/Corollary40/HintSizeArithmetic.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# The arithmetic of t = ⌊n^τ⌋

The hinted problems of Section 5.4 have matrices with t = ⌊n^τ⌋ rows or columns (hintSize τ n).  The
running times of the programs are expressions in n and t; the statements want powers of n.  This
file has the inequalities between the two, as inequalities between real numbers with explicit
constants.  No programs here.


 ## The number t 

### `one_le_hintSize`

 1 ≤ t. 

### `hintSize_le_rpow`

 t ≤ n^τ. 

### `rpow_le_two_mul_hintSize`

 n^τ ≤ 2 t: rounding down loses at most a factor 2. 

### `natCast_rpow_le_rpow`

 A power of n with a smaller exponent is smaller. 

### `hintSize_le`

 t ≤ n for τ ≤ 1. 

### `hintSize_pow_le_hintSize`

 t^k ≤ ⌊n^σ⌋ if kτ ≤ σ. 

### `hintSize_pow_eighteen_le`

 t^18 ≤ n for τ ≤ 1/18: the condition N ≥ D^18 of Corollary 26. 

### `hintSize_pow_eighteen_le_hintSize`

 t₁^18 ≤ t₂ for τ₁ ≤ τ₂/18. 

 ## Powers of t 

### `hintSize_rpow_le`

 t^q ≤ n^{qτ}. 

### `rpow_le_two_rpow_mul`

 n^{γτ} ≤ 2^γ t^γ. 

### `div_hintSize_rpow_le`

 1/t^γ ≤ 2^γ/n^{γτ}, in the form A/t^γ ≤ 2^γ A n^{-γτ}. 

### `two_rpow_le_two`

 2^γ ≤ 2 for γ ≤ 1. 

### `rpow_div_hintSize_rpow_le`

 n^a / t^γ ≤ 2^γ n^{a - γτ}. 

### `rpow_mul_hintSize_rpow_le`

 n^a t^q ≤ n^{a + qτ}. 

### `rpow_mul_hintSize_le`

 n^a t ≤ n^{a + τ}. 

 ## Corollary 40 with the data structure of Corollary 26: the exponents 0.063 and 0.437 

### `sq_div_hintSize_le`

 The preprocessing: n²/t^{0.063} ≤ 2 n^{2 - 0.063τ}. 

### `mul_hintSize_rpow_le`

 n queries: n t^{0.437} ≤ n^{1 + 0.437τ}. 

### `mul_hintSize_le`

 Reading or writing an n × t matrix: n t ≤ n^{2 - 0.063τ} for τ ≤ 1/18. 

 ## The number of blocks 

### `blocks_mul_le`

 A number c of blocks of b rows with c b < a + b, as ⌈a/b⌉ has, is at most 2a/b if b ≤ a. 

### `blocks_mul_sq_le`

 c ≤ ⌈n/t₂⌉ blocks of t₂ rows and t₂ columns have c t₂² ≤ 2 n t₂ ≤ 2 n^{1 + τ₂} entries. 

 ## The uMv problem with the data structure of Corollary 26 

### `blocks_sq_div_le`

 The preprocessing of c ≤ ⌈n/t₂⌉ blocks: c t₂²/t₁^{0.063} ≤ 4 n^{1 + τ₂ - 0.063τ₁}. 

### `hintSize_mul_hintSize_le`

 t₁ t₂ ≤ n^{τ₁ + τ₂}. 

### `hintSize_mul_hintSize_rpow_le`

 t₂ queries: t₂ t₁^{0.437} ≤ n^{τ₂ + 0.437τ₁}. 

 ## The general form, with logarithmic factors 

### `rpow_mul_log_sq_div_le`

 For 0 ≤ γ < γ': n^a (log t + 1)²/t^{γ'} = O(n^{a - γτ}), with one constant for all n, τ, a. 

### `rpow_mul_rpow_mul_log_le`

 For 0 ≤ q < r: n^a t^q (log t + 1) = O(n^{a + rτ}), with one constant for all n, τ, a. 

 ## The four general bounds of Corollary 40 

### `general_pre_le`

 The preprocessing, general form: n² (log t + 1)²/t^{γ'} ≤ C n^{2 - γτ}. 

### `general_query_le`

 n queries, general form: n t^q (log t + 1) ≤ C n^{1 + τ/2} for q < 1/2. 

### `general_umv_pre_le`

 The preprocessing of the blocks of the uMv problem, general form: c t₂² (log t₁ + 1)²/t₁^{γ'} ≤
C n^{1 + τ₂ - γτ₁}. 

### `general_umv_query_le`

 t₂ queries of the uMv problem, general form: t₂ t₁^q (log t₁ + 1) ≤ C n^{τ₂ + τ₁/2} for q < 1/2.

