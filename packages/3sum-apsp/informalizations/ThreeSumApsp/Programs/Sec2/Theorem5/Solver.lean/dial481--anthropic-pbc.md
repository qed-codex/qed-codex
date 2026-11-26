---
{
  "module": "ThreeSumApsp/Programs/Sec2/Theorem5/Solver.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec2/Theorem5/Solver.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec2/Theorem5/Solver.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# Theorem 5: the solver

thm5(N, D, w, U, x, y, wi, wj, out, fr) is the algorithm of Section 2.4.4: find m with D = 4^m; the
shared stage (tables, encodings of all row bands and column bands); the tile, the output string and
its digits for every wanted position; the sort by tile and string; the strings in sorted order; the
pruned recursion on every tile that has a wanted position; the report.  The work area begins at the
free pointer fr.

The result is thm5_spec: on an instance of the thin matrix product in the regime of Theorem 5, the
wanted entries of XY end up in the cells from out on, nothing else below fr changes, and the run
takes at most 2 c + 100 times thm5Shape steps, where c is the constant with which the called
procedures meet their entries.  findM_spec treats the search for m; everything after it is
fromShared_ends, which is stated for arbitrary parameters.  tilesShape_le gives the shape of the
time of the pruned recursions, whatever the sorting permutation, and thm5_time compares the sum of
the times with the shape.


### `findM`

 The search for m with D = 4^m. 

### `thm5Body`

 thm5(N, D, w, U, x, y, wi, wj, out, fr): the search for m, then the six stages.  Locals 0 to 9
are the arguments.  Everything that is not in a local is read from the directory, which the shared
stage leaves in the 32 cells from fr on. 

### `SolverLimits`

 What the solver asks of the limits, when it is called at depth d with the free pointer fr: what
the stages ask, for the parameters and the matrices of the instance, and room for 7^{L+1} U. A
bounds the encoded numbers. 

### `thinWork`

 The work of the pruned recursions on all the tiles, for the wanted positions of an instance. 

### `searchLocals`

 The local variables after i rounds of the search for m. 

### `findM_spec`

 **The search for m**: after i rounds local 10 holds i and local 11 holds 4^i. 

### `thm5_time`

 The sum of the times of the statements is within the bound. 

### `tilesShape_le`

 The shape of the time of the pruned recursions is nB² + nB + 1 plus thinWork, whatever the
sorting permutation. 

### `SolverLimits.sharedPre`

 What the shared stage assumes holds for an instance in the regime of Theorem 5. 

### `Solver5`

 What the solver of Theorem 5 does in the program P: in the regime of the theorem it leaves the
wanted entries of the product in the cells from out on, changes nothing else below the free pointer,
and takes at most K · thm5Shape steps.  It does not read its fourth argument u (the bound on the
entries). 

### `thm5_spec`

 **Theorem 5, the solver**, with the constant 2 c + 100, where c is the constant with which the
called procedures meet their entries. 
