---
{
  "module": "OAI/Computability/VPVNP/LiveAuxiliaryDescriptorInit.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveAuxiliaryDescriptorInit.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveAuxiliaryDescriptorInit.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Constructing the auxiliary header descriptors on the live RAM

A fixed straight-line call reads the two exterior cut lengths from live scratch
memory. It calculates all seven packed ends and sparse target addresses, then
writes the twenty-one descriptor words into a contiguous table. All reads precede
the first table write.


### `Ops`

 Straight-line descriptor-initializer operations over 32 registers and 14 public operands. 

### `data`

 The initializer's public operands, including header dimensions, the histogram length,
workspace addresses, and the seven source array bases. 

### `setup`

 Read the two live cut lengths, compute cumulative ends and shadow destinations for all
seven fields, and advance the incoming state word. 

### `ops`

 The complete initializer instruction sequence, performing setup before writing the seven
descriptor triples. 

### `program`

 Instantiate the descriptor initializer on the supplied lengths and addresses, returning the
advanced state word from register 27. 

### `rows`

 The descriptor for one auxiliary field, recording its exclusive packed end, source address,
and destination in the sparse shadow. 

### `putRow`

 Write the cumulative end, source base, and destination base of one row, in order. 

### `storeRows`

 The interpreter stores rows in the order of the supplied list. 

### `storeRows_outside`

 The sequence of row writes preserves every address outside the table. 

### `init_native`

 Construct the descriptor table from the public layout and the two exterior lengths
already stored in scratch memory. A single native call reads two words and writes twenty-one. 
