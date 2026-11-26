---
{
  "module": "OAI/Computability/VPVNP/PairSimulationLeafArena.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationLeafArena.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationLeafArena.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # Private addresses of the cursor-leaf verifier 

### `Regions`

 The node arguments occupy their full stride even at the last genuine
descriptor. The histogram and further reserved scratch precede the cache
of 38 virtual operands. Each verifier stack starts beyond the entire cache. 

### `Regions.arguments`

 The start and stride of the private argument frames indexed by descriptor node addresses. 

### `Regions.nodes`

 Exclusive upper bound on node indices with reserved argument frames. 

### `Regions.histWords`

 Number of private words reserved for the histogram immediately after the node frames. 

### `Regions.otherWords`

 Number of additional scratch words reserved between the histogram and the operand cache. 

### `Regions.histBase`

 First private histogram address, immediately following the last reserved node frame. 

### `Regions.cacheBase`

 First private address for the cached auxiliary operands, after the histogram and its
neighboring scratch interval. 

### `Regions.stackBase`

 First available private address for verifier stacks, immediately after the 38 cached
operand words. 

### `Regions.layout`

 Consecutive pointer slots of the actual virtual verifier's named-port
table. All address widths and counts are runtime parameters. 

### `eventually_fit`

 Any fixed polynomial bound on the public descriptor addresses and
stride gives a single threshold for the histogram, the operand cache,
and all stacks with their verified capacity `n^40`. 
