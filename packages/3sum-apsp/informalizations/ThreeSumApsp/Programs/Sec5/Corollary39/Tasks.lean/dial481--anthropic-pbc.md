---
{
  "module": "ThreeSumApsp/Programs/Sec5/Corollary39/Tasks.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec5/Corollary39/Tasks.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec5/Corollary39/Tasks.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# Corollary 39: the tasks

The problems of Corollary 39, with the calling convention of all tasks: deciding whether some
k-clique has total weight zero (`kcTask`), finding a triangle of maximum (minimum) weight, and
finding a k-clique of maximum (minimum) total weight.  The instances of the triangle problems are
those of finding a negative triangle; those of the last two problems are those of Zero-Weight
k-Clique with a place for the k vertices of the answer.

With these tasks the sentence "is solved in time T" can be read, for all problems of Corollary 39,
as a statement about programs of the light language (`lightModel5`).


 ## Weight zero 

### `KcInst`

 A complete k-partite graph in the memory. 

### `KcInst.Pre`

 The weights stand below the free pointer, in the blocks (p, q) with p < q of an array of k²
blocks, and are bounded by U. 

### `kcTask`

 **Zero-Weight k-Clique**: kc(n, U, g, fr) returns 1 if some k-clique has total weight zero, and
0 if not. 

 ## Minimum and maximum weight 

### `maxTriTask`

 **Max-Weight Triangle**: maxTri(n, U, ab, bc, ac, res, fr) writes the vertices a, b, c of a
triangle of maximum weight to the cells res, res + 1, res + 2. 

### `minTriTask`

 **Min-Weight Triangle**: minTri(n, U, ab, bc, ac, res, fr) writes the vertices a, b, c of a
triangle of minimum weight to the cells res, res + 1, res + 2. 

### `KcFindInst`

 A complete k-partite graph in the memory, and the place for the k vertices of a clique. 

### `KcFindInst.Pre`

 The place for the answer lies below the free pointer and does not meet the weights. 

### `maxKcTask`

 **Max-Weight k-Clique**: maxKc(n, U, g, res, fr) writes the vertices of a k-clique of maximum
total weight, the vertex in part p to the cell res + p. 

### `minKcTask`

 **Min-Weight k-Clique**: minKc(n, U, g, res, fr) writes the vertices of a k-clique of minimum
total weight, the vertex in part p to the cell res + p. 

 ## Minimum and maximum at once

The host for k-Clique is one program with a flag mx, true for the maximum and false for the minimum.


### `better`

 The weight x is at least as good as the weight y. 

### `optTriTask`

 Max-Weight Triangle (mx = true) or Min-Weight Triangle (mx = false). 

### `optKcTask`

 Max-Weight k-Clique (mx = true) or Min-Weight k-Clique (mx = false). 

### `optTriTask_true`

 With the flag true, `optTriTask` is Max-Weight Triangle. 

### `optTriTask_false`

 With the flag false, `optTriTask` is Min-Weight Triangle. 

### `optKcTask_true`

 With the flag true, `optKcTask` is Max-Weight k-Clique. 

### `optKcTask_false`

 With the flag false, `optKcTask` is Min-Weight k-Clique. 

 ## The time model 

### `lightModel5`

 The reading of "is solved in time T" by programs of the light language, extended by the problems
of Corollary 39. 
