---
{
  "module": "ThreeSumApsp/Sec3/Theorem21a/Convolution.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Sec3/Theorem21a/Convolution.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Sec3/Theorem21a/Convolution.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# Theorem 21(a): Convolution-3SUM reduces to Exact Triangle

[VW13, Theorem 4.3] in the form needed for Theorem 21(a): Convolution-3SUM on `N < t²`
numbers becomes `2t` instances of Exact Triangle on `t` vertices per part.  In instance `s` the
triangle `(a, b, c)` stands for the pair `i = at + b`, `j = ct + s - b` (`convTemplate`).  Every
solution is such a triangle (`exists_hasZeroTriangle`), and a zero triangle is a solution, because
an index out of range gives a weight so large that the sum is positive
(`convolution3SUM_of_isZeroTriangle`).  Together: `convolution3SUM_iff`, and with `t = ⌊√N⌋ + 1`,
`theorem_21a_convolution_to_exact`.


### `convTemplate`

 Instance `s` of the reduction from Convolution-3SUM.  The triangle `(a, b, c)` stands for the
pair `i = a t + b`, `j = c t + s - b`, for which `i + j = (a + c) t + s`: the edge `(a, b)` carries
`x_i`, the edge `(b, c)` carries `x_j`, and the edge `(a, c)` carries `-x_{i+j}`.  An edge whose
index is out of range gets the filler weight. 

### `convTemplate_AB`

 The weight of the edge `(a, b)`. 

### `convTemplate_BC`

 The weight of the edge `(b, c)`. 

### `convTemplate_AC`

 The weight of the edge `(a, c)`. 

### `exists_hasZeroTriangle`

 A solution `(i, j)` is the triangle `(⌊i/t⌋, i mod t, ⌊j/t⌋)` of the instance
`s = (j mod t) + (i mod t)`. 

### `neg_le_templateWeight`

 With the filler `2U + 1`, every weight is at least `-U`. 

### `convolution3SUM_of_isZeroTriangle`

 A zero triangle of an instance with the filler `2U + 1` is a solution. 

### `convolution3SUM_iff`

 The reduction of [VW13, Theorem 4.3], for `N < t²` numbers of absolute value at most `U`: there
are `i`, `j` with `x_i + x_j = x_{i+j}` if and only if one of the instances `s < 2t`, with the
filler `2U + 1`, has a zero triangle. 

### `theorem_21a_convolution_to_exact`

 The combinatorial content of [VW13, Theorem 4.3] in the form needed for **Theorem 21(a)**:
whether an array of `N` integers is a yes-instance of Convolution-3SUM is decided by asking `O(√N)`
times whether there is a zero triangle, each time in an instance with `O(√N)` vertices in each part
whose weights are entries of the array, up to sign, or a filler.  There are at most `2t` instances,
each with `t ≤ √N + 1` vertices in every part.  Each of their weights is a copy of some `±x_i`, at a
position `i` that does not depend on the numbers, or the filler `2U + 1`, where `U` bounds the
`|x_i|`. 
