---
{
  "module": "ThreeSumApsp/Programs/Sec4/Corollary26/Claim.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec4/Corollary26/Claim.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec4/Corollary26/Claim.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# Corollary 26, the offline form, for programs of the light language

Corollary 26: "Hence, for every set W of positions of an N × N matrix, the entries (XY)[I, J], (I,
J) ∈ W, can be computed deterministically in O(|W| D^{0.437} + N²/D^{0.063}) time". This is
`Claim.Corollary_26_wanted`, here with "is solved in time T" read as a statement about programs of
the light language (`claim_corollary_26_wanted`).

The program is `program26`: for m = ⌈log₄ D⌉ ≥ 60 it builds and asks the data structure of Theorem
30 with L = 21 m and t = ⌈m/9⌉, and for m < 60 it computes inner products. The procedure
allInstances26 of that program solves the task on all instances (`allInstances26_program26`), with a
polynomially bounded need (`allInstancesNeed26_poly`), and for N ≥ D^18 its time is within the bound
(`allInstancesTime26_le`).

This is the form of Corollary 26 on which Corollary 16, and through it the second bounds of Theorems
19 and 22, rest: a procedure that other procedures call. The statement about one program that reads
the input of the problem is `wordRam_corollary_26_wanted`.


### `allInstancesTime26_mono`

 The time of allInstances26 is monotone in the number of wanted positions and does not depend on
the bound on the entries. 

### `allInstances26_program26`

 **The procedure allInstances26 of `program26` solves the task on all instances**: the program
holds allInstances26, regimeTest26 and the brute force at their numbers. 

### `claim_corollary_26_wanted`

 **Corollary 26, last sentence, for programs of the light language.** 
