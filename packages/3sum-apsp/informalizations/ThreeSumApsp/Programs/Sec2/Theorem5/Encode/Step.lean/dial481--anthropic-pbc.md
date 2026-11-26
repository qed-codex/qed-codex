---
{
  "module": "ThreeSumApsp/Programs/Sec2/Theorem5/Encode/Step.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec2/Theorem5/Encode/Step.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec2/Theorem5/Encode/Step.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# One encoding step (step (2) of Full, Section 2.3.1)

"For each term λ of Schönhage's identity, form A_λ := ∑_s φ_λ(s) a_s and B_λ := ∑_t ψ_λ(t) b_t."
The array a is in 7 n consecutive cells at src, slice after slice; the coefficients of all the forms
are in a table at tab, seven for each term; the array A_λ is written to n cells at dst.  B_λ is
formed by the same procedure, from the array b and the table of the coefficients of the ψ_λ.

`encStepVal` is the sum that belongs in a cell, summand by summand.  Its partial sums are small
(`EncStepPre.val_bounds`), and it does not change while the cells of `dst` are written
(`EncStepPre.val_congr`).  `encStepSum_spec` forms one sum, and `encStep_meets` runs through the
cells.


### `Src`

 The local variables of encStep: the arguments src, dst, n, lam, tab; the cell j of dst; the sum;
the number s of the summand. 

### `encStepAdd`

 One summand: Acc := Acc + tab[7 lam + s] · src[s n + j]. 

### `encStepSum`

 The sum over s < 7 of tab[7 lam + s] · src[s n + j]. 

### `encStepCell`

 One cell of dst. 

### `encStepBody`

 encStep(src, dst, n, lam, tab): for j < n, dst[j] := ∑_{s < 7} tab[7 lam + s] · src[s n + j]. 

 ## The sums 

### `encStepVal`

 The first s summands of what encStep writes at dst + j. 

### `encStepOut`

 What encStep writes at dst + c. 

### `encStepVal_succ`

 One more summand. 

### `EncStepPre`

 The hypotheses of `encStep`: the seven coefficients and the array at `src` lie below the `n`
cells at `dst`, which lie in the memory; the coefficients are -1, 0 or 1, the numbers are at most
`V` in absolute value, and `7 V` fits in a word. 

### `enc_coef_mul_bound`

 The product of a coefficient in {-1, 0, 1} and a number of absolute value at most `V`. 

### `enc_sum_bound`

 A sum of `s` numbers of absolute value at most `V` is at most `s V` in absolute value. 

### `summand_bounds`

 One summand is at most `V` in absolute value. 

### `val_bounds`

 The sum of `s` summands is at most `s V` in absolute value. 

### `keep`

 The hypotheses still hold when cells of `dst` have been written. 

### `val_congr`

 The sums do not change when cells of `dst` are written. 

 ## The program 

### `encStepSum_spec`

 **One sum**: the loop over the seven summands leaves the sum for cell j in the local Acc. 

### `tEncStep`

 A bound on the number of steps of `encStep` on `n` cells. 

### `encStep_meets`

 **encStep** writes `∑_{s < 7} tab[7 lam + s] · src[s n + j]` to `dst[j]` for all `j < n` and
changes nothing else. 
