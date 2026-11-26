---
{
  "module": "ThreeSumApsp/RunningTimes/FromClaims.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/RunningTimes/FromClaims.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/RunningTimes/FromClaims.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# From running-time claims to programs: Theorem 5, Corollaries 15 and 16, Theorem 19

Let `M` be a reading of "is solved by a deterministic algorithm in time T".  If the running times of
`M` for a problem are realized on the word RAM (`RealizedWithin`), a claim about `M` with the bound
of an item of the paper gives that item as a statement about programs.  Each theorem asks only for
the problems that its item mentions.  The work is done by `exists_solves`, `exists_solves_pair` and
`solvedAt_of_realized`; what is left here is that the paper's bound is at least 1 on its domain
(`one_le_thinBound`, `add_one_le_splitBound`, `one_le_wantedBound`).


### `Theorem5.of_claim`

 **Theorem 5**, about programs, from the claim about `M`. 

### `LopRealized`

 The running times of `M` for the two lopsided triangle problems are realized on the word RAM, on
the instances with entries 0 and 1 and `D ≥ 1`. 

### `LopRealized.count`

 #Lop-AE-SparseTri. 

### `LopRealized.detect`

 Lop-AE-SparseTri. 

### `exists_solves_lop`

 The two lopsided triangle problems at once.  The entries are 0 and 1, so the magnitude is
`U = 1 = n^0`.  If the running times `Tc` and `Td` are both at most `C X`, where `X ≥ 1`, on the
instances in `dom`, then two programs solve these instances in `O(X)` steps. 

### `Corollary15.of_claim`

 **Corollary 15**, about programs, from the claim about `M`. 

### `Corollary16.of_claim`

 **Corollary 16**, about programs, from the claim about `M`. 

### `Theorem19.of_claim`

 **Theorem 19**, about programs, from the two claims about `M`. 
