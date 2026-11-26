---
{
  "module": "OAI/Computability/VPVNP/LiveHeaderScan.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveHeaderScan.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveHeaderScan.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Streaming the long live group index

The one-based group number can have polynomially many bits. Each burst reads
one bit at its processor, appends it to the scratch array, and updates the
index of the last set bit and the number of set bits. At completion these two
word-sized statistics give its base-two logarithm and the power-of-two test.


### `prefixOnes`

 Positions of the set bits observed before the next cursor. 

### `prefixHigh`

 Highest observed position, or zero in the empty prefix. 

### `summary_correct`

 Once all bits have been read, the last set bit is the binary logarithm
and exactly one set bit characterizes a power of two. 

### `indexCell`

 Public words are the bit-array base, high-index cell, and population-count
cell. The persistent state is the next site address. All reads precede writes. 

### `indexUpdate`

 Store one group-index bit, update the highest set position if the bit is one, and add it to
the population count. 

### `indexCell_trace`

 Exactly one call visits this bit. The trace has three reads, three writes,
twenty-one instructions and no branch choices. 
