---
{
  "module": "OAI/Computability/VPVNP/CompressorShrinkDemandGatherCall.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorShrinkDemandGatherCall.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorShrinkDemandGatherCall.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Gathering the two demand widths of a shrinking motif

Each visit copies a pair of words from two strided source arrays into adjacent
cells of the demand array. The cursor enumerates rows and columns in row-major
order. The visit reads both widths before writing the pair, so its memory
formula holds even when source and destination addresses coincide.


### `ops`

 Parameter zero is the number of visited columns in a row. Parameters one
and two are the source row strides, three and four the source bases, and five
the output base. Registers five and six retain the two widths until the writes. 

### `pass`

 The scheduled worker that copies a motif's two demand widths into adjacent words and
returns the next motif cursor. 

### `program`

 Instantiate the demand-gather worker with the six words giving its column count, source
strides and bases, and dense output base. 

### `src`

 Decode cursor `i` into a row and column and compute the source address using the specified
stride and base operands. 

### `dst`

 Address of the first of the two dense demand words for cursor `i`, two words per motif from
the output base. 

### `cost`

 Number of native operations for one demand-width pair, including the two reads, two writes
and cursor increment. 

### `visits`

 Complete report of a call, with each read carrying the word from the
incoming memory. The returned cursor points to the next width pair. 

### `visit_run`

 Every cap allowing the 24 instructions and their return produces the stated
report at the normal entry point of the scheduler's finite worker table. 
