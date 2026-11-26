---
{
  "module": "proof/rates/ClauseBound/Group/Grouping.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/ClauseBound/Group/Grouping.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/ClauseBound/Group/Grouping.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Groupings as permutations of one fixed grouping: lemmas for case (ii) of Lemma 8

Lemmas for a proof of case (ii) of Lemma 8 by counting instead of probability. The paper takes a
uniformly random grouping with groups of g/K nodes, n nodes here. Here the groupings are χ₀∘e, where
χ₀ is one fixed grouping with
groups of n nodes and e runs over all permutations of the nodes; every such grouping arises from the
same number of permutations, but this is not needed. What is needed: the group number γ of
χ₀∘e is each set of n nodes for the same number of e (`fiber_le`), and among the e for which it is a
given set A, the group number γ' is each set of n nodes outside A for the same number of
e. Both follow from the fact that a permutation of the nodes carries one such configuration to the
other (`exists_perm_sets`). So the fraction of the e with a property of the group is the
fraction of the sets of n nodes with that property (`card_filter_le_of_fibers`), which Hoeffding's
inequality for sampling without replacement bounds. 

 ### Permutations that carry one configuration of sets to another 

### `exists_perm_of_fiber`

 Two colourings with classes of the same sizes differ by a permutation. 

### `card_colour`

 The sizes of the four classes of the colouring by membership in two disjoint sets. 

### `exists_perm_sets`

 A permutation that keeps the set A and carries A'' to A', two sets of the same size that are
disjoint from A. 

 ### Counting through a map with fibres of one size 

### `card_filter_le_of_fibers`

 If all fibres of F over Xs have the same size, the fraction of Ω' on which F has a property is
the fraction of Xs with that property. 

 ### The groupings 

### `chi0`

 One grouping with groups of n nodes. 

### `cls`

 The group number γ of the grouping χ₀∘e. 

### `card_cls`

 Every group has n nodes. 

### `disjoint_cls`

 Different groups are disjoint. 

### `mem_cls_mul`

 The groups of χ₀∘e∘p are the preimages under p of the groups of χ₀∘e. 

### `fiber_le`

 If p carries A'' to A' and multiplication by p keeps Ω', then the group number γ' is A'' at
least as often on Ω' as it is A'. 
