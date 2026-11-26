---
{
  "module": "ThreeSumApsp/RunningTimes/Sec5/Corollary39/ZeroWeightLayout.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/RunningTimes/Sec5/Corollary39/ZeroWeightLayout.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/RunningTimes/Sec5/Corollary39/ZeroWeightLayout.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# Zero-Weight k-Clique: from a solver of the task to a program for the layout of the end statement

Zero-Weight k-Clique (Corollary 39).  `realized_zeroKClique`: if the task `kcTask k` is
solved in time T, then `EndStatement.ZeroWeightKClique k` is solved on the word RAM within a
constant times T.

The input is n in cell 0 and then, for each ordered pair of parts (p, q), an n × n block of numbers;
the weight between vertex u of part p and vertex v of part q stands in cell
1 + ((p k + q) n + u) n + v (`getD_kList`).  Only the blocks with p < q count.  The solver is told
the graph of these blocks (`upperGraph`), whose cliques have the weights that the end statement sums
(`cliqueWeight_upperGraph`, `hasZeroClique_upperGraph`), and it reads no other block
(`kcPre_input`).  The free pointer is 1 + k² n².


 ## The list of the weights 

### `kList`

 The weights, as the input has them. 

### `kList_eq`

 The list of the weights, block after block. 

### `length_kList`

 There are `k² n²` weights. 

### `kList_zero`

 At size 0 there are no weights. 

### `getD_kList`

 The entry at the place of a weight is the weight. 

### `mem_kList`

 Every weight is one of the numbers of the input. 

 ## The graph of the upper blocks 

### `upperGraph`

 The complete `k`-partite graph whose weights between the parts `p < q` are the block
`(p, q)`. 

### `cliqueWeight_upperGraph`

 A clique of the graph has the weight that the upper blocks give it. 

### `hasZeroClique_upperGraph`

 Some clique of the graph has weight 0 exactly if the question of the end statement has the
answer yes. 

### `kcPre_input`

 What a solver of a weighted `k`-Clique problem asks of the memory holds for the input, with the
weights from cell 1 on. 

 ## The connection 

### `cliqueArgs`

 The arguments of the solver: n, U, the address 1 of the weights, and the free pointer
1 + k² n². 

### `safe_cliqueArgs`

 The arguments stay within the limits. 

### `wrapClique`

 What connects Zero-Weight k-Clique in the layout of the end statement with the task. 

### `realized_zeroKClique`

 **Zero-Weight k-Clique**: if the task is solved in time T, then the problem is solved on the
word RAM within a constant times T. 
