---
{
  "module": "proof/machines/StepMachines/Prog/CountNet.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/machines/StepMachines/Prog/CountNet.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/machines/StepMachines/Prog/CountNet.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 The network of a k-CNF, as in Section 6 (the network of Φ), on words. The clauses are cut into g
clusters of μ
clauses, a state of a cluster has one bit for each literal slot, and a link (an equality test of the
paper) joins consecutive
occurrences of a variable. The file has plain list functions for the weights, factors and
capacities, and their agreement
with the network `SatNet.net`. State word: bit c*k+j is the slot (c,j). Label word: one bit for each
link, in reading
order. 

### `Fml`

 A formula as data: a literal is (variable, the value that makes it true). 

 ### The plain functions 

### `mu`

 The number of clauses of a cluster. 

### `litAt`

 The literal at place i % k of clause i / k. 

### `varAt`

 The variable at slot i. 

### `slotsOf`

 The slots of the clauses of φ: 0, …, m*k - 1. 

### `linkB`

 Slot i' is the next occurrence of the variable at slot i. 

### `locals`

 The slots of a cluster: 0, …, μ*k - 1. 

### `rows`

 The clauses of a cluster: 0, …, μ - 1. 

### `links`

 The links from cluster a to cluster b, as pairs of slots of the clusters, in reading order. 

### `capF`

 The capacity of two clusters: the number of links between them, one label bit each. 

### `wF`

 The weight of cluster a at the state word z, for x = (φ, (a, z)): 1 if the slots without a
literal carry false,
every clause of the cluster has a true literal and the links inside the cluster join equal bits,
else 0. 

### `fF`

 The factor of clusters a, b on the side of a, at the state word z and the label word θ,
for x = (φ, ((a, b), (z, θ))): 1 if every link of the two clusters has, at its end in a, the bit
that θ gives it, else 0. 

### `wordNet`

 The cluster network on words. 

 ### Ranges 

 ### Slots as numbers 

### `loc`

 The place of a slot in its cluster. 

 ### States 

### `bits`

 The state that a word writes. 

 ### Links 

### `all_links_iff`

 A condition on all links of two clusters, read on slots. 

### `wF_eq`

 The plain weight is the weight of the network. 

 ### Labels 

### `sum_words_zip`

 One bit a link: the sum over the label words restores the equalities. 

### `wordNet_Ψ_lt`

 The interaction of clusters a < b on words. 

### `length_links`

 The number of links is the capacity of the network. 

 ### The value and the size 

### `value_congr`

 Two networks that agree along a bijection of their states have the same value. 

### `value_wordNet`

 The network on words has the value of `SatNet.net`, the network of a formula as in Section 6. 

### `U_wordNet`

 The network on words has the same U, the sum of the capacities over ordered pairs of clusters,
as `SatNet.net`. 

### `sized_wordNet`

 The network on words has size 2kμ: every node has at most 2^(2kμ) states and at most 2kμ label
bits.
Its weights, factors and interactions are 0 or 1, so the bound 2^B on their absolute values holds
for every B. 
