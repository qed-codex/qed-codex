---
{
  "module": "ThreeSumApsp/Programs/Sec4/ChoosingParameters/Statement.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec4/ChoosingParameters/Statement.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec4/ChoosingParameters/Statement.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# Section 4.4, the data structure as a light program

Section 4.4. The programs hold rational parameters c = a/b, θ = p/q and a threshold m₀. They are a
data structure for the entries of a thin matrix product (`programIsDataStructure_of_costsWithin`),
on every domain of inputs and for all bounds Tp (preprocessing time and space) and Tq (query time)
that dominate the two cost expressions (8) and L ∑ α_d of Theorem 30 at these parameters. The regime
and the bounds are parameters, so that the statements of Section 4 about data structures
(Corollaries 26 and 31, Theorem 24) are instances; the compiler takes the statement to the word RAM
in `isDataStructure_of_costsWithin`.


### `le_mul_of_le_mul_add`

 A quantity that is at most a t + 40 is at most A t, if a + 40 ≤ A and t ≥ 1. 

### `lim31_thinPair`

 **Word size**: with the free pointer behind the input, the limits are polynomial in N, and N and
all numbers of the input fit in a word. 

### `programIsDataStructure_of_costsWithin`

 **The programs with rational parameters are a data structure**, on every domain and for all
bounds that dominate the costs of Theorem 30. 
