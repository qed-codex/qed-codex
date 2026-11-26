---
{
  "module": "proof/machines/StepMachines/Prog/NetVal.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/machines/StepMachines/Prog/NetVal.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/machines/StepMachines/Prog/NetVal.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 The rebalancing of a network into K classes: what the programs of StepMachines/Prog/NetProg.lean
compute. A network on g nodes is
merged along a colouring with K colours into an instance of the problem on K nodes. mergedVal is an
entry of a tensor of
that instance, the value of the instance is the value of the network, and some colouring passes the
test goodB. 

### `Network.ZW_toInst`

 The instance N.toInst D dec has the value of the network N. Its labels are words: x ∈ D a b ⊆
words ℓ stands for the
label dec a b x of N, and x ↦ dec a b x carries sums over D a b to sums over the labels of N. 

### `tuples_congr'`

 Tuples depend on the sets only where the predicate holds. 

### `cut_take`

 cut reads only the first Σ c i bits. 

### `prod_range_mul_self`

 A product over i < g*g as a product over pairs. 

### `chi`

 The colouring with the code x. 

### `membersF`

 The members of a class, as elements of Fin g. 

### `prsF`

 The pairs of members of two classes, as elements of Fin g × Fin g. 

### `zAt_eq_cut`

 The state of a member, by cut. 

### `lAt_eq_cut`

 The label of a pair, by cut. 

### `mD`

 The words of β bits that stand for a label of the classes G, G': a tuple of labels followed by
zeros. 

### `mdec`

 The label that such a word stands for. 

### `ZW_merged`

 The value of the instance of the merged network is the value of the network. 

### `termVal_pair`

 The factor number a*g + b. 

### `prod_termVal`

 The product of the factors, regrouped: weights, inner interactions, factors towards the other
classes. 

### `toInst_eq_mergedVal`

 mergedVal is the entry of the instance of the merged network. 

 ### Good colourings 

### `goodB_iff`

 What the test goodB of a colouring says: every class has fewer than 2g/K nodes, and two classes
share at most betaC
label bits. 

### `exists_goodB`

 For g ≥ 3K⁸ some colouring among the K^g passes the test. 
