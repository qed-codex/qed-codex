---
{
  "module": "EndStatement.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/EndStatement.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/EndStatement.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 Claims of the paper «Truly Subquadratic 3SUM and Truly Subcubic APSP via Triangles in Sparse Lopsided Graphs» (Josh
Alman, Virginia Vassilevska Williams), about programs of a word RAM defined here. Imports nothing, proves nothing. 

### `Instr`

 `i j k` name cells, `l` a position in the program, `[i]` is the word in cell `i`. The only constant is 1. 

### `exec`

 The verdict and the final memory, if `P`, run from position `pc` on memory `m`, halts within `t` steps, the halting
step counted; past its end `P` rejects. Addresses are read signed; `bltz` jumps on a negative word; `write` runs on. 

### `loadWords`

 The memory at the start: `ws` in cells 0, 1, 2, …, and 0 in every other cell. 

### `BigO`

 `T(n) = O(n^r)`, both sides raised to the power `r.den`: core Lean has no fractional powers. For `r = 1.9992 =
2499/1250` it says `T(n)^1250 ≤ K n^2499`. 

### `Problem`

 `yes`: when to accept (always, if not given). `output`: a condition on the cells after the input, read as signed. 

### `Problem.SolvedBy`

 One run: with `n` in cell 0 and the input after it, `P` halts within `t` steps with the right verdict and output. 

### `Problem.SolvedInTime`

 Theorem 2: «a word RAM with O(log n)-bit words», «all numbers in the input are integers of absolute value
n^O(1)»: for every `κ`, one `P`, `b`, `T` for all instances, correct at every `W ≥ b(⌊log₂ n⌋ + 1)`. 

### `ExactTriangle`

 Section 3.2: «S(a, b, c) := w(a, b) + w(b, c) + w(a, c). A zero triangle is a triangle … with S(a, b, c) = 0». 

### `ε_T`

 Theorem 19: «ε_T := 0.0017». 

### `Theorem_19`

 Theorem 19: «Exact Triangle … can be solved by a deterministic algorithm in … O(n^(3−ε_T)) time». 

### `ThreeSum`

 Section 1: «Given n numbers, decide whether three of them sum to 0». Three different positions. 

### `Theorem_22_3SUM`

 Theorem 22: «solve 3SUM on n integers of absolute value at most n^ν», in time «O(n^1.9992)». 

### `MinPlusProduct`

 Output, row by row: entry `(i, j)` is the least of the sums `A i k + B k j`. 

### `Theorem_22_MinPlus`

 Theorem 22: «the (min, +)-product of two n × n integer matrices», in time «O(n^2.99942)». 

### `Path`

 A path and its total weight; it may repeat vertices. 

### `APSP`

 Input: the 0/1 matrix of the edges, then the weights, with 0 for no edge. Output, two cells for each `(i, j)`: 1 if
there is a path, else 0; then the distance. 

### `Theorem_22_APSP`

 Theorem 22: «APSP on directed n-vertex graphs … and no negative cycles», in time «O(n^2.99942)». 

### `ZeroWeightKClique`

 `w i j u v`: weight between `u` in part `i` and `v` in part `j`. All `k²` blocks are input; only `i < j` counts. 

### `Corollary_39_ZeroWeight`

 Corollary 39: «decide in O(n^(k−ε_T⌊k/3⌋)) time whether some k-clique … has total edge weight zero». 
