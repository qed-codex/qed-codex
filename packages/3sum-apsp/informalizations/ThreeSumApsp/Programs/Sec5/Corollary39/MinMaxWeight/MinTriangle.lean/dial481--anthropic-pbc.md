---
{
  "module": "ThreeSumApsp/Programs/Sec5/Corollary39/MinMaxWeight/MinTriangle.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec5/Corollary39/MinMaxWeight/MinTriangle.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec5/Corollary39/MinMaxWeight/MinTriangle.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# Min-Weight Triangle from Max-Weight Triangle, as a host

Proof of Corollary 39: "a minimum weight triangle is a maximum weight triangle for the negated
weights". minTri(n, U, ab, bc, ac, res, fr) writes the three negated matrices to the free pointer
and calls a solver of Max-Weight Triangle (`minTri_spec`, `isHost_minTri`).  The quoted sentence is
`Corollary39.isMinWeightTriangle_iff_negate`; the three matrices that the program writes are the
instance with the negated weights (`triOf_affL_neg`).


### `Size`

 The locals of minTri(n, U, ab, bc, ac, res, fr).  The arguments; the first one also takes the
result, and the free pointer is the address of the first negated matrix.  Then n², the addresses of
the other two negated matrices, the free pointer for the solver, and a result that is not used. 

### `minTriBody`

 minTri(n, U, ab, bc, ac, res, fr). 

### `minTriTime`

 The time of minTri, if the solver of Max-Weight Triangle takes T n U steps. 

### `minTriNeed`

 The need of minTri, if the solver of Max-Weight Triangle needs r n U. 

### `triOf_affL_neg`

 The three negated matrices are the instance with the negated weights. 

### `minTri_spec`

 **minTri** finds a minimum weight triangle: it negates the three matrices and asks for a maximum
weight triangle. 

### `polyNeed_minTriNeed`

 The need of minTri is polynomially bounded if the need of the solver is. 

### `isHost_minTri`

 **Min-Weight Triangle from Max-Weight Triangle.** 
