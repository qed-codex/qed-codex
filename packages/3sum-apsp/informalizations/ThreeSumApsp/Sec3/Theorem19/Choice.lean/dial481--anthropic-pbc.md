---
{
  "module": "ThreeSumApsp/Sec3/Theorem19/Choice.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Sec3/Theorem19/Choice.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Sec3/Theorem19/Choice.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# The cost analysis of Theorem 19 for a general choice of the parameters

The two halves of the proof of Theorem 19 are the same computation with different numbers.  Both
apply Theorem 17 with a number `D ≥ 16` between `n^{1/18}/c` and `n^{1/18}` and with `g = ⌈D^η⌉`,
and solve each of the at most `4ng` instances with a saving `D^{2η}`.  Such a pair `D`, `η` is a
`Choice`, and the computation is carried out here for every choice.

1. A choice satisfies the hypotheses `16 ≤ D ≤ n` and `1 ≤ g ≤ √D` of Theorem 17 and the hypothesis
   `D^18 ≤ n` of Corollaries 15 and 16 (`Choice.sixteen_le`, `Choice.le_n`, `Choice.one_le_ceil`,
   `Choice.ceil_le_sqrt`, `Choice.pow_eighteen_le`).
2. The lower bound on `D` gives `D^{-η} ≤ c^η n^{-η/18}` (`Choice.saving`), and the upper bound
   gives `D^a ≤ n^{a/18}` (`Choice.rpow_le_rpow_div`).
3. Each of the four terms of the running time is `O(n^{3-η/18})` up to logarithms: the instances
   (`Choice.instances_le`) and the scans (`Choice.scans_le`) by the first bound, the choice of `p`
   (`Choice.strassen_le`) and building the instances (`Choice.build_le`) by the second.
4. So is their sum (`exists_total_le`).


### `Choice`

 A choice of the parameters of Theorem 17 as in both halves of the proof of Theorem 19: `D ≥ 16`
lies between `n^{1/18}/c` and `n^{1/18}`, and `g = ⌈D^η⌉` with `0 ≤ η ≤ 1/4`. 

### `Choice.sixteen_le`

 `D ≥ 16`, as Theorem 17 asks. 

### `Choice.le_root`

 `D ≤ n^{1/18}`. 

### `Choice.root_div_le`

 `D ≥ n^{1/18}/c`. 

### `Choice.c_pos`

 The constant `c` is positive. 

### `Choice.η_nonneg`

 `η ≥ 0`. 

### `Choice.η_le`

 `η ≤ 1/4`, so that `g ≤ √D`. 

### `le_root_iff`

 `x ≤ n^{1/18}` says that `x^18 ≤ n`. 

### `sixteen_le_root`

 `n^{1/18} ≥ 16` for `n ≥ 16^18`. 

 ### The hypotheses of Theorem 17 and of Corollaries 15 and 16 

### `pow_eighteen_le`

 "Corollary 15 [...] applies because D^{18} ≤ n", and likewise Corollary 16. 

### `le_n`

 `D ≤ n`, as Theorem 17 asks. 

### `one_le_ceil`

 `g ≥ 1`, as Theorem 17 asks. 

### `ceil_le`

 `g ≤ 2 D^η`: rounding up a number that is at least 1 at most doubles it. 

### `ceil_le_sqrt`

 `g ≤ √D`, as Theorem 17 asks: with `r = D^{1/4} ≥ 2` we have `g ≤ 2 D^η ≤ 2r ≤ r² = √D`. 

 ### Logarithms 

### `one_le_log`

 `log n ≥ 1`, because `n ≥ D ≥ 16`. 

### `log_le_log`

 `log D ≤ log n`. 

 ### Powers of `D` in terms of `n` 

### `saving`

 "Finally D^{−1/36} ≤ 4^{1/36} n^{−1/648}", and "D ≥ n^{1/18}/2 gives D^{−0.0315} ≤ 2
n^{−0.0315/18}".  In general, `D ≥ n^{1/18}/c` gives `D^{-η} ≤ c^η n^{-η/18}`. 

### `cube_mul_saving_le`

 `n³ D^{-η} ≤ c^η n^{3-η/18}`. 

### `rpow_le_rpow_div`

 `D^a ≤ n^{a/18}` for `a ≥ 0`. 

### `rpow_le_of_le`

 A power `n^b` with `b ≤ 2.9` is at most `n^{3-η/18} Λ`, for every factor `Λ ≥ 1`. 

 ### The four terms of the running time

`Λ` is the logarithmic factor of the result, `log² n` or `log n`. 

### `instances_le`

 "The O(nD^{1/36}) instances cost O(n² log² D/D^{1/18}) each, so O(n³ D^{−1/36} log² n) in all",
and "The instances cost O(nD^{0.0315}) · O(n²/D^{0.063}) = O(n³ D^{−0.0315})".  `X` is the
logarithmic factor in the cost of one instance, `log² D` or 1. 

### `scans_le`

 "the scans cost O(n³ D^{−1/36} log n)", and "the scans O(n³ D^{−0.0315} log n)", from the term
`κ n³ log n/g` of Theorem 17. 

### `strassen_le`

 "the choice of p costs O(n^{log₂ 7} D^{3/2}) = O(n^{2.9}) with Strassen's algorithm" (both
cases): `log₂ 7 + (3/2)/18 < 2.81 + 0.09`.  Strassen's exponent stands for the `ω + o(1)` of
Theorem 17. 

### `build_le`

 "building the instances costs O(n² D^{1.03})", respectively "O(n² D^{1.04})", from the term
`n² D g` of Theorem 17: it is at most `2 n² D^{1+η} ≤ 2 n^{2+(1+η)/18}`. 

### `exists_total_le`

 **The cost analysis of Theorem 19**, for every choice of the parameters: the time is `O(κ
n^{3-η/18} Λ)`.  The left side is the bound of Theorem 17: the number `4ng` of instances times the
cost `a n² X/D^{2η}` of one instance, plus `b` times the three terms of the additional time (with
Strassen's exponent).  `a` and `b` stand for the constants hidden in the two `O(·)`, `X` is the
logarithmic factor in the cost of one instance, and `Λ` the one in the result.  `κ` is the exponent
in the bound on the weights, the paper's ν; the paper hides it in the `O(·)`.  The constant `C`
depends only on `c` and `η` and is chosen before `n` and `D`, which is why `c ≥ 0` is asked for
separately. 
