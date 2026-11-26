---
{
  "module": "ThreeSumApsp/RunningTimes/Sec3/Theorem22.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/RunningTimes/Sec3/Theorem22.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/RunningTimes/Sec3/Theorem22.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# Theorem 22 on the word RAM

"Plug Theorem 19 into Theorem 21."  Each bound has three ingredients.

1. The paper's deduction between running times, proved for every reading `M` of the sentence "is
   solved by a deterministic algorithm in time T" (lemmas such as `threeSum_of_uniform_theorem_21a`;
   nothing is assumed about `M`).
2. The reading `lightModel`, in which the sentence means that a program of the light language solves
   the task within T steps.  For this reading the reductions that Theorem 21 cites are theorems,
   because they are written as programs that call an arbitrary solver (`Sec3.claim_…`); so
   Theorem 21 holds for it: `claim_theorem_21a` for 3SUM, `claim_theorem_21b_minPlus` and
   `claim_theorem_21b_apsp` for the (min,+)-product and APSP.
3. The way to the machine: a solver of a task, with one more procedure for the input layout,
   compiled, is a program of the word RAM that takes a constant times as many steps
   (`Sec3.realized_threeSum`, `realized_minPlusProduct`, `realized_apsp`).

From a bound `O(s^{3−δ} (log s)^e)` for Exact Triangle this gives

* 3SUM in `O(n^a)` time for every `a > 2 − δ/2` (`threeSum_of_uniform`);
* the (min,+)-product and APSP in `O(n^{3−δ/3} (log n)^{O(1)})` time (`minPlus_polylog_of_uniform`,
  `apsp_polylog_of_uniform`), and so in `O(n^a)` time for every `a > 3 − δ/3`
  (`SolvedInPolylogTime.solvedInTime`).

The theorem is the case `δ = 1/648` (using Theorem 5) and the case `δ = ε' = 0.00175` (using
Corollary 26).  For 3SUM the programs lose polylogarithmic factors only
(`Theorem22.threeSum_polylog`); the printed form with `n^{o(1)}` follows
(`SolvedInPolylogTime.solvedInLittleOTime`).


 ## Theorem 21 for programs of the light language 

### `claim_theorem_21a`

 Theorem 21(a): 3SUM from Exact Triangle, through Convolution-3SUM. 

### `claim_theorem_21b_minPlus`

 Theorem 21(b): the (min,+)-product from Exact Triangle, through Negative Triangle. 

### `claim_theorem_21b_apsp`

 Theorem 21(b): APSP from Exact Triangle, through the (min,+)-product. 

 ## A bound for Exact Triangle, plugged into Theorem 21 

### `threeSum_of_uniform`

 3SUM in `O(n^a)` time for every `a > 2 − δ/2`. 

### `minPlus_polylog_of_uniform`

 The (min,+)-product in `O(n^{3−δ/3} (log n)^{O(1)})` time. 

### `apsp_polylog_of_uniform`

 APSP in `O(n^{3−δ/3} (log n)^{O(1)})` time. 

### `wordRam_theorem_22_first`

 **Theorem 22**, on the word RAM: the bounds using Theorem 5. 

### `wordRam_theorem_22_second`

 **Theorem 22**, on the word RAM: the bounds using Corollary 26. 

### `WordRam.Items.Theorem_22_second.threeSum`

 The bound for 3SUM using Corollary 26. 

### `WordRam.Items.Theorem_22_second.minPlus`

 The bound for the (min,+)-product using Corollary 26. 

### `WordRam.Items.Theorem_22_second.apsp`

 The bound for APSP using Corollary 26. 

### `Theorem22.threeSum_polylog`

 Theorem 22, on the word RAM, with `(log n)^{O(1)}` in place of `n^{o(1)}`: 3SUM in
`O(n^{2−1/1296} (log n)^{O(1)})` and in `O(n^{2−ε'/2} (log n)^{O(1)})` time.

NOTE.  Theorem 22 has `n^{o(1)}` here.  The programs give `(log n)^{O(1)}`, and the printed form
follows (`wordRam_theorem_22_threeSum`). 

### `wordRam_theorem_22_threeSum`

 **Theorem 22**, on the word RAM: 3SUM in `n^{2−1/1296+o(1)}` and in `n^{2−ε'/2+o(1)}`
time. 
