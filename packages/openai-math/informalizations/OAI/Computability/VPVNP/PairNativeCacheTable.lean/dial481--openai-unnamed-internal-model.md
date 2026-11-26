---
{
  "module": "OAI/Computability/VPVNP/PairNativeCacheTable.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairNativeCacheTable.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairNativeCacheTable.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# A native arithmetic prelude followed by the pair's private cache stores

The first addresses are the labels of the arithmetic flow. Its normal exit
enters a chain of 38 private stores, each followed by one cursor increment.
The standalone table accepts at the end. The same row emitter allows a
larger scheduler to place these labels and supply the final continuation.


### `count`

 Number of private stores needed for the four fixed leaf parameters and 34 auxiliary
operands. 

### `size`

 Instruction count for the arithmetic flow, two rows per cache word, and the continuation
and rejection rows. 

### `label`

 Address of a label from the arithmetic flow in the prefix of the cache instruction table. 

### `pc`

 The last even address is the final continuation. 

### `inc`

 Address of the cursor increment immediately following the private store for cache slot `i`. 

### `done`

 Address reached after incrementing past the last cache word, where the enclosing program
supplies its continuation. 

### `bad`

 Rejecting row targeted by a failed branch of the cache arithmetic. 

### `row`

 Emit one row with targets in an ambient scheduler's program-counter type. 

### `template`

 Assemble a two-bit-literal program with the supplied arithmetic entry, 38
store-and-increment pairs, and an accepting continuation. 

### `linked_of_rows`

 Installing these rows anywhere in a machine links the arithmetic flow
to the first cache store. 
