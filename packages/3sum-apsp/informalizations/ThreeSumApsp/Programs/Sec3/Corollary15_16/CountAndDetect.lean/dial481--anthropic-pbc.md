---
{
  "module": "ThreeSumApsp/Programs/Sec3/Corollary15_16/CountAndDetect.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec3/Corollary15_16/CountAndDetect.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec3/Corollary15_16/CountAndDetect.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# Corollary 15: counting triangles with the thin matrix product, and detecting with counting

Two steps of the proof of Corollary 15, with "the problem is solved in time T" read as
`ThinSolvedIn` and `LopSolvedIn`.

* `Claim.LopCountFromThinProduct`: "Apply Theorem 5 with N = n to the two biadjacency matrices".  An
  instance of #Lop-AE-SparseTri is given by its two biadjacency matrices, so a solver of the thin
  matrix product is a solver of #Lop-AE-SparseTri as it stands, called with U = 1, where U, the
  fourth argument and parameter, is the bound on the entries of the matrices
  (`solvesN_count_of_thin`, `claim_lopCountFromThinProduct`).
* `Claim.LopDetectFromCount`: the counts "are nonzero exactly for the query pairs that lie in a
  triangle".  One more procedure calls the counting solver and replaces every nonzero count by 1
  (`detect_spec`, `claim_lopDetectFromCount`).


 ## Bounds 

### `polyBound_snoc_one`

 One more parameter with the value 1 costs a factor `2^e`. 

### `polyBound_le_succ`

 Twice the bound leaves room for one more. 

 ## Counting with the thin matrix product 

### `solvesN_count_of_thin`

 A solver of the thin matrix product solves #Lop-AE-SparseTri. 

### `polyNeedN_snoc_one`

 A polynomially bounded need stays so when a parameter is fixed to 1. 

### `claim_lopCountFromThinProduct`

 **Counting common neighbours is a thin matrix product** (Section 3.1). 

 ## Detecting with counting 

### `N`

 The local variables that hold the arguments of a solver of the thin matrix product or of a
lopsided triangle problem: N, D, w, U, x, y, wi, wj, out, fr. 

### `lopDetectBody`

 detect(N, D, w, U, x, y, wi, wj, out, fr): calls the counting solver on the same arguments, then
replaces every nonzero answer by 1.  Local 10 takes the result of the call and is then the
counter. 

### `lopDetectTime`

 The number of steps of detect, if the counting solver takes Tn; the third parameter is w. 

### `lopDetectNeed`

 What detect needs: one more level of calls. 

### `length_thinOut`

 There is one answer for each wanted position. 

### `detect_spec`

 **detect** solves Lop-AE-SparseTri. 

### `polyNeedN_detect`

 The need of detect is polynomially bounded if that of the counting solver is. 

### `claim_lopDetectFromCount`

 **Detection from counting** (proof of Corollary 15). 
