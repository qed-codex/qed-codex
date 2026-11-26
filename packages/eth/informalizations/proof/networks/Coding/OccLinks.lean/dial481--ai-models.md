---
{
  "module": "proof/networks/Coding/OccLinks.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/networks/Coding/OccLinks.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/networks/Coding/OccLinks.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The tests between two clusters and Lean's links

Section 6: «For a ≠ b, c_{a,b} is the number of tests with one occurrence in cluster a and the other
in cluster b. Choose an order of these tests, and let z_a|_b ∈ {0,1}^{c_{a,b}} list the bits of z_a
at their occurrences in cluster a».
`links_eq_tests`: for clusters a ≤ b the list `Coding.testsBetween g Φ a b`, with each occurrence
replaced by its place, is the list `Groundwork.Prog.Count.links g 3 Φ a b`, with each place of a
cluster replaced by its place in Φ. Both lists are increasing in the order of the dictionary, so it
is enough that they have the same members, and this is `mem_tests_iff` together with: the cluster of
an occurrence is the block of 3·m̄ places in which its place lies.
`import all StepMachines.Prog.CountNet` gives access to `locals_eq` and `mem_links`, which are not
public. 

### `mu_pos_of_occ`

 If Φ has an occurrence, then m̄ ≥ 1. 

### `clusterOf_eq_iff`

 The cluster of an occurrence is the block of 3·m̄ places in which its place lies. 

### `mem_occOf_iff`

 The occurrences in cluster a are the occurrences whose cluster is a. 

### `testsBetween_comm`

 The tests between the clusters a and b do not depend on the order in which the clusters are
named. 

### `mem_testsBetween`

 For a ≤ b the earlier occurrence of a test between the clusters a and b lies in cluster a. 

### `pairwise_tests`

 The tests, read as pairs of places, are listed in the order of the dictionary. 

### `links_eq_tests`

 The tests between two clusters are Lean's links, in the same order («Choose an order of these
tests», Section 6). 

### `map_links`

 Whatever is read off the links of Lean's network, place by place, is read off the tests. 

### `capF_eq`

 «c_{a,b} is the number of tests with one occurrence in cluster a and the other in cluster b»
(Section 6): Lean's number c_{a,b} is the number of tests between the clusters a and b. 
