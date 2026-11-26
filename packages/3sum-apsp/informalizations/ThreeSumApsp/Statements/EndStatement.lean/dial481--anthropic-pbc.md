---
{
  "module": "ThreeSumApsp/Statements/EndStatement.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Statements/EndStatement.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Statements/EndStatement.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# The five claims of the end statement

The item statements for Theorems 19 and 22 and Corollary 39 speak of the problems of the end
statement and contain the five bounds, with real exponents.  `SolvedInTime.endStatement` turns such
a bound into the form of the end statement, with the same program: a step bound with natural values,
and a rational exponent.

Which bound each claim takes, and on which of the paper's two routes it rests:

* Theorem 19: the third bound of `Items.Theorem_19`.  It follows from the second bound, so it rests
  on Theorem 17 with Corollary 16, that is, on Corollary 26 (Section 4), and not on the time bound
  of Theorem 5.
* 3SUM, the (min,+)-product and APSP: the first and the last two bounds of
  `Items.Theorem_22_second`, "using Corollary 26".
* Zero-Weight k-Clique: `Items.Corollary_39_zero`, from Theorem 19 using Corollary 26.


### `endStatement_theorem_19`

 Theorem 19: Exact Triangle on three `n × n` matrices of integers of absolute value at
most `n^κ` is solved in time `O(n^(3 - 0.0017))`. 

### `endStatement_theorem_22_3SUM`

 Theorem 22: 3SUM (do three of the numbers, at three different positions, sum to 0?) on
`n` integers of absolute value at most `n^κ` is solved in time `O(n^1.9992)`. 

### `endStatement_theorem_22_MinPlus`

 Theorem 22: the (min,+)-product of two `n × n` matrices of integers of absolute value
at most `n^κ` is computed in time `O(n^2.99942)`. 

### `endStatement_theorem_22_APSP`

 Theorem 22: APSP on directed graphs with `n` vertices, integer weights of absolute
value at most `n^κ` and no negative cycle is solved in time `O(n^2.99942)`. 

### `endStatement_corollary_39_zeroWeight`

 Corollary 39: for every `k ≥ 3`, Zero-Weight `k`-Clique on `k` parts of `n` vertices,
with integer weights of absolute value at most `n^κ`, is decided in time `O(n^(k - 0.0017 ⌊k/3⌋))`.

