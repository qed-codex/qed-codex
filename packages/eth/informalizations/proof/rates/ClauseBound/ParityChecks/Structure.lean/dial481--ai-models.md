---
{
  "module": "proof/rates/ClauseBound/ParityChecks/Structure.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/ClauseBound/ParityChecks/Structure.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/ClauseBound/ParityChecks/Structure.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # What a potential below 1 gives

The potential is a sum of four nonnegative terms, so each of them is below 1 if the potential is.
`structure_` reads off the three bounds on the checks chosen so far: on the number of
pairs (check, clause in it), on the size of every check and on the number of checks that contain a
given clause; the last two in the form 2^(number) < …, before logarithms are taken.
`final` says that in the final state the first term is a nonnegative integer, hence 0, and that this
makes the checks good. That the four terms are nonnegative is a hypothesis of
both theorems. 

### `pr_pos`

 p = 1/nb is positive. 

### `lt_of_sum_lt`

 From (1/c)·S < 1, for a sum S of nonnegative terms a_i/b_i with 0 < b_i ≤ B: every a_i is below
c·B. 

### `structure_`

 What Υ < 1 gives in any state: fewer than 8pmr pairs, 2^|Λ_j'| < 8r(1 + p)^m for every check,
and 2^load(e) < 8m(1 + p)^r for every clause e, where load(e) is the number of checks j' < r that
contain e. 

### `half_eq`

 ½(1 + (−1)^q) = [q even]. 

### `Upar_final`

 In the final state the first term of the potential is the integer Σ_ξ ω(ξ)·∏_{j' < r} [|V_j'(ξ)|
even]. 

### `final`

 In the final state Υ < 1 makes the checks good. 
