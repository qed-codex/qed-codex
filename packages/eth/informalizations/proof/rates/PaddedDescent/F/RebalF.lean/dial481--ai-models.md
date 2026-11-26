---
{
  "module": "proof/rates/PaddedDescent/F/RebalF.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/PaddedDescent/F/RebalF.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/PaddedDescent/F/RebalF.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The rebalancing on explicit data (mergedF = mergedVal, StR)

`mergedF` computes the same numbers as the value specification `NetE.mergedVal`, on well-formed
queries. The equality follows from uniqueness of results: the program `mergedM` over
the cost-free procedures `freeM` halts with the plain value on every input (by the run lemmas of the
combinators), `mergedM_runs` says
that it halts with `mergedVal` on well-formed queries, and results are unique. 

### `presents`

 How to show that a network of plain functions presents a network. 

 ### The programs over cost-free procedures halt with the plain value 

### `Halts`

 M halts on a with the result b. 

### `termP`

 `termF` without fuel. 

### `mergedP`

 `mergedF` without fuel. 

### `mergedP_eq`

 The plain value is the specification `mergedVal`, on well-formed queries. 

### `termF_eq`

 The fuelled `termF` equals the plain `termP`; the bound of the number of labels by the padding
length is needed only in the cases where the sum is evaluated. 

 ### `StR` 

### `betaC_le`

 The bound on the new label length, for any colouring. 

### `stR`

 `StR`: the rebalancing `rebalF` picks the first good grouping and returns a table whose value is
that of the merged network, with bounds on the new label length and on the entries. 
