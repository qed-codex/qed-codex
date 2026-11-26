---
{
  "module": "ThreeSumApsp/RunningTimes/Sec5/Corollary39/MinMaxWeight.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/RunningTimes/Sec5/Corollary39/MinMaxWeight.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/RunningTimes/Sec5/Corollary39/MinMaxWeight.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# Corollary 39, minimum and maximum weight, on the word RAM

Corollary 39 finds a k-clique of minimum, or of maximum, total weight.

* The host that builds the graph H for each choice of the fixed vertices and calls a solver that
  finds a best triangle takes at most n^t (T(N, ·) + C N²) steps (`exists_optTime_le`).  So it
  proves the two transfer claims of the proof (`claim_maxCliqueFromMaxTriangle`,
  `claim_minCliqueFromMinTriangle`).  The two other claims are [VW13, Theorem 3.3] for finding a
  maximum weight triangle, and the negation of the weights (`claim_VW13_Theorem_3_3_max`,
  `claim_minTriangleFromMax`).
* The input is that of Zero-Weight k-Clique.  The vertices of the clique go to the k cells behind
  it, and the free pointer is behind them (`optInst`, `pre_optClique`, `post_optClique`).  So a
  solver of either task gives a program for the layout of the end statement (`wrapMaxClique`,
  `wrapMinClique`).
* With the bound of Theorem 19 for Exact Triangle, the arithmetic of the running times, which holds
  for any reading of "is solved in time T" (`minMaxClique_of_theorem_19_VW13`), gives
  the bound of Corollary 39, and `Wrap.realized` and `FromClaims.solvedAt_of_realized` carry it to
  the word RAM (`corollary_39_min_max_of_theorem_19`).


 ## The two transfer claims 

### `exists_optTime_le`

 The time of the host: n^t calls of the solver, and a constant times N² steps for each of them
(proof of Corollary 39: t = numFixed k, N = n ^ width k). 

### `claim_maxCliqueFromMaxTriangle`

 The transfer claim for maximum weight. 

### `claim_minCliqueFromMinTriangle`

 The transfer claim for minimum weight. 

 ## The layout of the end statement 

### `wrapOptArgs`

 The arguments of the solver: n, U, the address 1 of the weights, the address 1 + k² n² of the
answer, and the free pointer 1 + k + k² n². 

### `wrapOpt_vals`

 The values of the arguments. 

### `wrapOpt_safe`

 The arguments stay within the limits. 

### `wrapOpt_fr_le`

 The free pointer is within what `Wrap` allows. 

### `optInst`

 The instance of either task: the weights stand from cell 1 on, and the answer goes behind
them. 

### `pre_optClique`

 The input meets the precondition of either task. 

### `post_optClique`

 The cells in which a solver of either task leaves the clique are the output cells. 

### `cliqueWeight_le_of_upperGraph`

 A comparison of two cliques in the graph that the solver is told is a comparison of the weights
that the end statement sums. 

### `wrapMaxClique`

 What connects Max-Weight k-Clique in the layout of the end statement with the task.  The program
always accepts: the answer is in the output cells. 

### `wrapMinClique`

 What connects Min-Weight k-Clique in the layout of the end statement with the task.  The program
always accepts: the answer is in the output cells. 

 ## Corollary 39, minimum and maximum weight 

### `corollary_39_min_max_of_theorem_19`

 **Corollary 39, minimum and maximum weight, on the word RAM**, from the bound of Theorem 19 for
Exact Triangle for programs of the light language. 
