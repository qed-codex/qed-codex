---
{
  "module": "OAI/Computability/VPVNP/RAMTapeUnaryWord.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapeUnaryWord.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapeUnaryWord.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Preparing the length and the unit as padded binary words

The input is a unary tally of the physical input length. A fixed control
allocates two words, adding a group of `p+1` zero bits to each word for every
mark and one further group. It sets the unit word's low bit and increments
the length word once for each saved mark. All data-dependent loops operate
on individual stack cells.


### `Port`

 Stacks for a unary source tally, pending increments, padded binary length and unit words,
and arithmetic scratch. 

### `Phase`

 Control states for allocating both padded words, setting the unit bit, and counting the
saved unary marks into the length word. 

### `code`

 Allocate padded zero words in groups of the parameter plus one bits, set the unit to one,
and increment the length word for each unary mark. 

### `store`

 Assign the supplied bit lists to the source, pending, length, unit, and temporary stacks. 

### `allocWork`

 Stack steps from the initial allocation to the instruction that sets the unit bit. 

### `count_fixed`

 Enter the counting loop with an already allocated zero word. Each saved
mark increments that word. The source and unit stacks pass through intact. 

### `work`

 Allocate the two words, set the unit's low bit, and scan both directions
through the length word once per input mark. 

### `work_le`

 The degree of the instruction bound is independent of the fixed
program parameter `p`. 

### `runs`

 Starting with only the unary tally, prepare the two fixed-width words.
Their width, including all padding cells, is `(p+1)*(n+1)`. 
