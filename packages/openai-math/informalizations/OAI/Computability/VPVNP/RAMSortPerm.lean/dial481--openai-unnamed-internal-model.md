---
{
  "module": "OAI/Computability/VPVNP/RAMSortPerm.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMSortPerm.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMSortPerm.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Record multiplicities in the bitonic network

Each comparator outputs its two inputs in one of the two orders. Consequently the
list of records in a whole block is permuted by the network, including repeated records.


### `ofFn_join`

 In wire order, joining two contiguous blocks concatenates their record lists. 

### `compare_perm`

 A single parallel comparison layer preserves all input records. 

### `merge_perm`

 A merge phase preserves the multiset of records of the input block. 

### `sort_perm`

 The full network preserves every record and its multiplicity. 
