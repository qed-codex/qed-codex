---
{
  "module": "src/Lib/General/Groups/IndexOfProduct.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/General/Groups/IndexOfProduct.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/General/Groups/IndexOfProduct.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The index of a product of subgroups is the product of the indices

One lemma of group theory, `New.Seesaw.index_pi_univ`: in a finite product of groups, the index of a
product of subgroups is the product of their indices (an infinite index is read as `0`).

## Relation to the literature

Known result: the index of a product of subgroups in a finite product of groups is the product of
the indices. Mathlib's `Subgroup.index_pi` is the case where all the factors are the same group.


### `New.Seesaw.index_pi_univ`

 In a finite product of groups `G i`, the index of the product `∏ i, H i` of subgroups
`H i ≤ G i` is the product of the indices of the `H i`. An infinite index is read as `0`. 
