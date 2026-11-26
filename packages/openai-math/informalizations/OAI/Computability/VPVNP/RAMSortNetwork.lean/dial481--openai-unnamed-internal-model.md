---
{
  "module": "OAI/Computability/VPVNP/RAMSortNetwork.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMSortNetwork.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMSortNetwork.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Batcher's bitonic sorting network

Lemma 10.1 of *VP and VNP differ over every field* sorts records by phases.
A phase on a block of size `2^(b+1)` compares its two halves at stride
`2^b`, then continues the merge in parallel in the two halves. The phase
begins with an ascending left half and a descending right half.


### `Wires`

 A contiguous block of records in the network. 

### `lo`

 Read the first half of a block. 

### `hi`

 Read the second half of a block. 

### `join`

 Write the two halves of a block. 

### `eq_of_halves`

 Equality of blocks can be checked separately on each half. 

### `lower`

 Value written at the smaller index of a comparator. 

### `upper`

 Value written at the larger index of a comparator. 

### `merge`

 One merge phase. The two recursive calls are parallel disjoint blocks. 

### `sort`

 Sort a block, with ascending order requested by `true`. 

### `merge_map`

 Thresholding commutes with every comparator, and hence with a full merge. 

### `sort_map`

 A monotone map can be pushed from the output to the input of the network. 
