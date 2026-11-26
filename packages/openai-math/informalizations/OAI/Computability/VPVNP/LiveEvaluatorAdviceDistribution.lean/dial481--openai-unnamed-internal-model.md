---
{
  "module": "OAI/Computability/VPVNP/LiveEvaluatorAdviceDistribution.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveEvaluatorAdviceDistribution.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveEvaluatorAdviceDistribution.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The distributed advice used to initialize the evaluator

The copied header array carries the raw bit length as one little-endian word,
the raw payload in a padded region, and the ordinal lookup table. These are
precisely the three source regions of the native packing stages. The ordinal
region begins at the end of the allocated payload capacity, independently of
the actual raw length.


### `lengthBits`

 Little-endian length field of the raw evaluator input. 

### `ordinalBits`

 Little-endian, row-major ordinal table. 

### `distribution`

 Complete advice layout with the two allocated padding regions. 

### `packSource_of_slice`

 A copied header array supplies every native word read of any contiguous
sublist, including a zero-length sublist. 

### `distribution_sources_of_copied`

 The copied advice bits suffice to identify the three source regions. 

### `distribution_sources`

 The physical header copy supplies exactly the input required by each
native packing call. The source of the ordinal table is fixed by capacity. 

### `packed_length`

 Packing the first full word recovers the actual raw length without truncation. 

### `packMemory_length`

 The native length sweep returns that length in the designated word. 

### `packMemory_raw`

 Each full-width raw payload row is the packed input word of initialization. 

### `packMemory_ordinal`

 Each ordinal keeps its source value when extended to the working word width. 

### `PackSource.after_other_bank`

 Source bits for a later packing stage remain available after a disjoint
earlier stage, including after any partial prefix of its execution. 
