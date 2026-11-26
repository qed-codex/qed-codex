---
{
  "module": "proof/rates/ClauseBound/ParityChecks/RunF.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/ClauseBound/ParityChecks/RunF.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/ClauseBound/ParityChecks/RunF.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The choice of the checks in the program is the run

In the program every growing list is cut off by the pad. This file shows that no cut-off is active
when the pad is long enough: the program's `runF` is the function `run`
of proof/rates/ClauseBound/ParityChecks/RunDefs.lean. The proof uses nothing about the two functions
`oA` and `oB` that the run queries: a check is a list of different clauses below m, because each
decision appends the clause that is being
decided or nothing; so its word is short, and there are at most r checks. 

### `runToC`

 The first e decisions for one check, with the list cut off by the pad after each. 

### `runC`

 All checks, with the list cut off by the pad after each. 

### `lenChk`

 A bound for the length of the word of a check. 

### `runTo_shape`

 After e decisions the check is a list of at most e clauses, all below e. 

### `len_runTo_le`

 The word of a check is short. 

### `runToC_eq`

 No cut-off is active in the decisions for one check. 

### `runChecks_shape`

 The first j checks are j lists with short words. 

### `len_runChecks_le`

 The word of the list of the first j ≤ r checks is short. 

### `runC_eq`

 No cut-off is active in the whole choice. 

### `lenChk_add_two_le`

 The bound for one check, in terms of bounds for m. 

### `big_eq`

 The length that the program asks of the pad, written as a product. 

### `lenChk_le_big`

 The word of a check is shorter than the length that the program asks of the pad. 

### `all_le_big`

 So is the word of the list of all checks. 

### `runF_eq`

 The choice of the checks in the program is the run. 
