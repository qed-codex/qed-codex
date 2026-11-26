---
{
  "module": "OAI/Computability/VPVNP/RAMSortLayers.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMSortLayers.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMSortLayers.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Addressed layers of the bitonic sorting network

Lemma 10.1 uses one XOR mask at every site of a layer. The layer definitions
below act on records indexed by natural numbers. Their restrictions to aligned
finite blocks agree with the recursive bitonic network. In particular the
result at each index of a finite array is independent of all records outside it.


### `block`

 Read an aligned block of `2^k` records from the global array. 

### `comparatorLayer`

 A layer with stride `2^j`. The direction function is shared by the
positions of each block being merged. 

### `runStrides`

 Strides in a phase are applied from `2^(k-1)` down to one. 

### `block_runStrides`

 A phase of addressed layers acts on every aligned block exactly as
`merge`, when that block has the indicated common direction. 

### `phaseDirection`

 Even-numbered blocks in phase `a` are ascending. 

### `runPhases`

 Execute phases one through `a`, choosing the comparator directions
from the global block numbers. 

### `block_runPhases`

 Every phase produces a recursively sorted block, ascending for even
block numbers and descending for odd ones. 

### `runSort`

 Run the network on a specified array width, with the requested direction
for its final merge. Earlier phases use their ordinary alternating directions. 

### `block_runSort`

 Restricting the globally addressed execution to the first finite block
recovers Batcher's network in either requested direction. 
