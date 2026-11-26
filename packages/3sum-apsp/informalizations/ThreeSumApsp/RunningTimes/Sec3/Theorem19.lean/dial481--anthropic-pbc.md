---
{
  "module": "ThreeSumApsp/RunningTimes/Sec3/Theorem19.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/RunningTimes/Sec3/Theorem19.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/RunningTimes/Sec3/Theorem19.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# Theorem 19 on the word RAM

The route, as in the paper.  Theorem 17 reduces Exact Triangle to instances of the lopsided triangle
problem.  With the parameters `D` and `g` of Section 3.3 and Corollary 15 for the instances the
total is `O(n^{3−1/648} log² n)` (`claim_theorem_19_usingTheorem5`); with Corollary 16 it is
`O(n^{3−ε'} log n)`, `ε' = 0.00175` (`claim_theorem_19_usingCorollary26`).  Both are claims about
programs of the light language that keep the dependence on `κ`.  The outermost procedure for the
input layout and the compiler (`Light.Sec3.realized_exactTriangle`) carry them to the word RAM.
The third bound of the theorem, `O(n^{3−ε_T})`, follows from the second, so it rests on Corollary 16
and not on Corollary 15.

Section 3.4 needs the two bounds for all numbers of vertices and all bounds on the weights:
`claim_exactTriangleUniform_usingTheorem5`, `claim_exactTriangleUniform_usingCorollary26`.  They
combine the program with brute force below a threshold, as in the proof ("smaller instances are
solved by brute force").


### `claim_theorem_19_usingTheorem5`

 Theorem 19, the bound using Theorem 5, for programs of the light language. 

### `claim_theorem_19_usingCorollary26`

 Theorem 19, the bound using Corollary 26, for programs of the light language. 

### `closure_monoExactTriangle`

 A program that solves Exact Triangle in time `T` solves it in every larger time. 

### `claim_exactTriangleUniform_usingTheorem5`

 The bound using Theorem 5, for all numbers of vertices and all bounds on the weights. 

### `claim_exactTriangleUniform_usingCorollary26`

 The bound using Corollary 26, for all numbers of vertices and all bounds on the weights. 

### `wordRam_theorem_19`

 **Theorem 19**, on the word RAM. 

### `WordRam.Items.Theorem_19.rounded`

 The third bound of the theorem, `O(n^{3−ε_T})`. 
