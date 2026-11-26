---
{
  "module": "OAI/Algorithms/SubexponentialSAT/BlockPacking.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/BlockPacking.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/BlockPacking.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Packing complete type blocks

The squared-deviation bound and the threshold from Section 5.4 imply a lower
bound for every type count. Enumerating the finite fibers then constructs
pairwise disjoint complete blocks. The construction from supplied enumerations
is explicit; no running-time theorem is asserted here.


### `three_quarters_of_square_bound`

 Scalar form of the imbalance estimate, with denominators cleared in the conclusion. 

### `count_lower_of_deviation_bound`

 The manuscript's threshold bounds every count, for any finite type space. 

### `count_fraction_lower_of_deviation_bound`

 The same lower bound in the fractional form used in Section 5.4. 

### `CompleteBlocks`

 A collection of complete blocks is an injective placement of block/type pairs,
preserving the assigned type. This also allows factors to cross block boundaries. 

### `count`

 The actual number of coordinates of a given type. 

### `count_eq_filter_card`

 Compatibility with type counts expressed by filtering the coordinates. 

### `ofEnumerations`

 Use the first `b` entries of each fiber enumeration. 

### `ofCountLE`

 Finite fiber equivalences supply the enumerations for abstract finite types. 

### `blockEmbedding`

 Embedding of the type universe into an individual complete block. 

### `block`

 The coordinates of one block, as a finite set. 

### `covered`

 All packed coordinates; coordinates outside this set are the leftovers. 

### `disjoint_blocks`

 Distinct blocks have no coordinate in common. 

### `unique_type_in_block`

 Every type occurs exactly once in every block. 

### `leftovers`

 Coordinates not assigned to any complete block. 

### `leftovers_le_quarter`

 The uncovered coordinates occupy at most one quarter of the input. 

### `exists_completeBlocks_of_count_lower`

 Pack as many blocks as the least populated fiber permits. The integer
minimum is used directly, so the coverage estimate loses no extra block. 

### `exists_completeBlocks_of_deviation_bound`

 Section 5.4: squared deviations and `D >= 16 N^3 a` yield complete blocks
covering at least three quarters of the coordinate set. 

### `exists_completeBlocks_of_nat_threshold`

 Natural-number threshold specialization. Take `a = 1 + Delta * k` to
recover exactly the threshold `D*` in equation (5.9). 
