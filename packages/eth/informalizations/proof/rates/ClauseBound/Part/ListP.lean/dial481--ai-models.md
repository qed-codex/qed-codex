---
{
  "module": "proof/rates/ClauseBound/Part/ListP.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/ClauseBound/Part/ListP.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/ClauseBound/Part/ListP.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Partitions as lists

`partsLe E k` is the list of the partitions of E into parts of size at most k, each written as a
nonincreasing list of positive integers: first those with all parts < k, then those that begin
with k. `partsOf E = partsLe E E` lists all partitions of E (`mem_partsOf`), each once
(`nodup_partsOf`), so it has p(E) members (`length_partsOf`); `partsLe E k` is the same list for
every k ≥ E
(`partsLe_of_le`). As multisets the members are the multisets of positive integers with sum E, each
once (`mem_map_coe_partsOf`, `nodup_map_coe_partsOf`). A by-product is p(E) ≤ 2^E
(`p_le_two_pow`). The definitions use recursion on natural numbers and lists only. 

### `partsLe`

 The nonincreasing lists of positive integers ≤ k with sum E: first those with all parts < k,
then those that begin with k. 

### `partsOf`

 The partitions of E, as nonincreasing lists of positive integers. 

### `partsLe_zero_right`

 With no part allowed, only the empty list, for E = 0. 

### `partsLe_succ`

 The step of the recursion. 

### `mem_partsLe`

 The members of `partsLe E k`. 

### `nodup_partsLe`

 No list occurs twice in `partsLe E k`. 

### `partsLe_of_le`

 Parts larger than E do not occur: the list is the same for all k ≥ E. 

### `length_partsLe_mono`

 The list grows with k. 

### `le_sum_of_mem`

 A member of a list of natural numbers is at most the sum. 

### `length_partsLe_aux`

 For E ≥ 1 there are at most 2^E − 2^(E−k) lists; for E = 0 there is one. 

### `mem_partsOf`

 The members of `partsOf E` are the nonincreasing lists of positive integers with sum E. 

### `nodup_partsOf`

 No list occurs twice in `partsOf E`. 

### `mem_map_coe_partsOf`

 As multisets, the members of `partsOf E` are the multisets of positive integers with sum E. 

### `nodup_map_coe_partsOf`

 As multisets, the members of `partsOf E` are different from each other. 

### `length_partsOf`

 There are p(E) of them. 

### `length_partsLe_le`

 `partsLe E k` has at most p(E) members. 

### `p_le_two_pow`

 p(E) ≤ 2^E. 
